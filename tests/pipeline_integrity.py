"""
Robotiko v2.0 - Pipeline Integrity Checker
Validates that no BLOCKING step was skipped in the production pipeline, that the
disk reality agrees with the declared status in project_metadata.json, and that
every artifact past a human gate has an honest approval record.

Pipeline order: Lyrics -> Musical Metadata -> Concept Notes -> Dramaturgy
                -> Visual Prompts -> Motion Script -> Final Edit

Three things this checker enforces:

  1. SKIPPED STEPS (honest, waiver-aware). A non-sequential pattern (an empty step N
     with a present step N+1) is a skipped step. It is a FAIL unless a legacy waiver
     record exists in the approvals ledger. episode-01 is the one legacy case: its
     visual-prompts stage is a PDF (episode-01/04_visuals/selected/...), so step 5
     reads empty while step 6 (Motion Script) is present. That skip PASSES only
     because approvals.json carries a waiver for it; the identical pattern in a new
     episode with no waiver FAILS. The old summary printed "no skipped steps" while
     its own checkboxes showed one — that contradiction is gone.

  2. DISK vs DECLARED STATE MACHINE. Each episode's stage is computed from disk (the
     step-detection below) and compared against project_metadata.json's per-episode
     production flags. If disk shows a stage DONE that the metadata declares not done
     (disk is ahead of the record), that is a provable contradiction = FAIL. The
     reverse (declared ahead of disk) is deliberately NOT failed: render outputs
     (final .mp4, scene images) are gitignored and "in_progress" work legitimately has
     no committed file yet, so declared-ahead is normal, not a contradiction.

  3. APPROVAL GATES AS DATA (ADR 0008). An episode with artifacts beyond a human gate
     but no ledger record for that gate = FAIL. A sha256 that no longer matches the
     approved artifact on disk = WARN "stale approval - artifact changed after
     approval" (post-approval em-dash cleanups are legitimate; the WARN makes them
     visible, it does not block).

Unfilled scaffold templates / placeholder stubs (the files create_episode.py drops
into a new episode) are treated as "pending", not "done", so a fresh scaffold does
not trip a false violation.

Usage:
    python tests/pipeline_integrity.py --episode 02
    python tests/pipeline_integrity.py --full

Status: IMPLEMENTED v2.0
"""

import os
import re
import sys
import json
import hashlib
import argparse

# Markers that identify an UNFILLED template or placeholder stub (not a real deliverable)
TEMPLATE_MARKERS = [
    "auto-populated by Claude",
    "Do not fill manually",
    "[Claude generates",
    "Shot X: ...",
    "{XX}",
]

# Pipeline steps (from pipeline_rules.md). {EP} -> "ep07".
# Each step matches ANY file in its folder against a regex, so version variants
# (_v01/_v02/...) and the EP01 legacy unversioned forms are all recognized.
PIPELINE_STEPS = [
    {"step": 1, "name": "Lyrics",                "dir": "01_lyrics",    "re": r"^{EP}_lyrics(_v\d{2})?\.md$",        "blocking": True},
    {"step": 2, "name": "Musical Metadata JSON", "dir": "02_music",     "re": r"^{EP}_musical_metadata\.json$",         "blocking": True},
    {"step": 3, "name": "Concept Notes",         "dir": "03_direction", "re": r"^{EP}_concept_notes\.md$",              "blocking": True},
    {"step": 4, "name": "Dramaturgy",            "dir": "03_direction", "re": r"^{EP}_dramaturgy_v\d{2}\.md$",        "blocking": True,  "gate": "Human approval gate 1"},
    {"step": 5, "name": "Visual Prompts",        "dir": "04_visuals",   "re": r"^{EP}_visual_prompts_v\d{2}\.(md|pdf)$", "blocking": False},
    {"step": 6, "name": "Motion Script",         "dir": "05_video",     "re": r"^{EP}_motion_script(_v\d{2})?\.(md|pdf)$", "blocking": True,  "gate": "Human approval gate 2"},
    {"step": 7, "name": "Final Edit",            "dir": "06_edit",      "re": r"^{EP}_final_v\d{2}\.mp4$",            "blocking": False},
]

# Step index (0-based) semantics used by the state machine and gate checks.
IDX_VISUALS = 4   # step 5
IDX_MOTION = 5    # step 6
IDX_EDIT = 6      # step 7

# project_metadata.json production flag -> the pipeline step index it maps to on disk.
# "music" (Suno audio) and "concept" have no single committed artifact in this map and
# are intentionally omitted from the disk-ahead comparison.
PRODUCTION_FLAG_TO_STEP = {
    "lyrics": 0,
    "timestamp_json": 1,
    "dramaturgy": 3,
    "visuals": IDX_VISUALS,
    "video": IDX_MOTION,
}

APPROVALS_PATH = os.path.join("_management", "approvals.json")
METADATA_PATH = os.path.join("_management", "project_metadata.json")


# -------------------------------------------------------------------
# STEP DETECTION (unchanged core)
# -------------------------------------------------------------------

def file_is_real(path: str) -> bool:
    """True if the file is a real deliverable (not an unfilled template/stub)."""
    if path.lower().endswith((".mp4", ".png", ".wav", ".mp3", ".json", ".pdf")):
        return True  # binary / exported deliverables are never templates
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except OSError:
        return True
    return not any(marker in text for marker in TEMPLATE_MARKERS)


def step_done(folder: str, step: dict, ep: str) -> bool:
    """A step is 'done' if its folder contains a real file matching the step regex."""
    step_dir = os.path.join(folder, step["dir"])
    if not os.path.isdir(step_dir):
        return False
    pattern = re.compile(step["re"].replace("{EP}", f"ep{ep}"))
    for name in os.listdir(step_dir):
        full = os.path.join(step_dir, name)
        if os.path.isfile(full) and pattern.match(name) and file_is_real(full):
            return True
    return False


def episode_status(ep: str):
    """Return the 7-bool done-status list for an episode, or None if no folder."""
    folder = f"episode-{ep}"
    if not os.path.isdir(folder):
        return None
    return [step_done(folder, step, ep) for step in PIPELINE_STEPS]


# -------------------------------------------------------------------
# 1. SKIPPED STEPS (waiver-aware)
# -------------------------------------------------------------------

def nonsequential_skips(status) -> list:
    """Return the indexes of steps that are EMPTY but sit before a PRESENT later step.
    That non-sequential pattern is the definition of a skipped step. Covers both
    blocking and non-blocking steps (episode-01's non-blocking visual-prompts skip is
    exactly the case the old blocking-only check let pass silently)."""
    present = [i for i, s in enumerate(status) if s]
    if not present:
        return []
    last = max(present)
    return [i for i in range(last) if not status[i]]


# -------------------------------------------------------------------
# 2. APPROVALS LEDGER
# -------------------------------------------------------------------

def load_approvals(repo_root: str = ".") -> list:
    """Load approvals.json's entry list. Missing/malformed -> [] (checks then WARN)."""
    path = os.path.join(repo_root, APPROVALS_PATH)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return data.get("approvals", []) if isinstance(data, dict) else []


def approvals_for(ledger: list, ep: str) -> list:
    return [e for e in ledger if str(e.get("episode", "")).zfill(2) == str(ep).zfill(2)]


def gate_record(ledger: list, ep: str, gate: int):
    for e in approvals_for(ledger, ep):
        if e.get("gate") == gate:
            return e
    return None


def episode_waiver(ledger: list, ep: str):
    """A waiver is any ledger record for the episode whose note declares a waiver
    (the word 'waiv'). episode-01's gate-1 record carries the PDF-only visuals waiver."""
    for e in approvals_for(ledger, ep):
        if "waiv" in str(e.get("note", "")).lower():
            return e
    return None


def sha256_file(path: str):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except OSError:
        return None


# -------------------------------------------------------------------
# 3. DISK vs DECLARED STATE MACHINE
# -------------------------------------------------------------------

def load_metadata(repo_root: str = ".") -> dict:
    path = os.path.join(repo_root, METADATA_PATH)
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def declared_production(metadata: dict, ep: str) -> dict:
    episodes = metadata.get("episodes", {})
    return episodes.get(f"ep{ep}", {}).get("production", {})


def _truthy(flag_value) -> bool:
    """A production flag counts as 'started/done' unless it is explicitly falsy.
    True, 'retroactive', 'in_progress' all count as present; False / '' / 'no' do not."""
    if flag_value is True:
        return True
    if not flag_value:
        return False
    if isinstance(flag_value, str):
        return flag_value.strip().lower() not in ("false", "no", "0", "none")
    return bool(flag_value)


def disk_declared_conflicts(status, production: dict) -> list:
    """Findings (severity, message-tail) where DISK is ahead of the declared record:
    a step is done on disk but project_metadata declares its production flag falsy.
    Only this direction is flagged (see module docstring); declared-ahead is normal
    because render outputs are gitignored and in-progress work has no committed file."""
    findings = []
    for flag, idx in PRODUCTION_FLAG_TO_STEP.items():
        if not production:
            break
        on_disk = status[idx]
        declared = _truthy(production.get(flag))
        if on_disk and not declared:
            step_name = PIPELINE_STEPS[idx]["name"]
            findings.append((
                "FAIL",
                f"disk shows '{step_name}' done but project_metadata declares "
                f"production.{flag}={production.get(flag)!r} -> declared status "
                f"contradicts disk (update the metadata or the artifact)."
            ))
    return findings


# -------------------------------------------------------------------
# GATE ENFORCEMENT (consumes the ledger + the declared metadata)
# -------------------------------------------------------------------

def gate_findings(ep: str, status, ledger: list, production: dict, repo_root: str = ".") -> list:
    """Findings for the two human gates:
      - artifacts beyond a gate with no ledger record  -> FAIL
      - a ledger sha256 that no longer matches disk     -> WARN (stale approval)
      - a ledger record whose artifact is missing        -> WARN
    """
    findings = []

    # Gate 1 (Dramaturgy): required once anything past dramaturgy exists on disk.
    beyond_gate1 = any(status[i] for i in (IDX_VISUALS, IDX_MOTION, IDX_EDIT))
    rec1 = gate_record(ledger, ep, 1)
    if beyond_gate1 and rec1 is None:
        findings.append((
            "FAIL",
            "has artifacts past the Dramaturgy gate (visuals/motion/edit on disk) "
            "but NO gate-1 approval record in _management/approvals.json."
        ))

    # Gate 2 (Motion Script): required once a motion script exists AND video
    # production has entered (project_metadata production.video is truthy). Render
    # outputs are gitignored, so the video flag is the honest 'beyond gate 2' signal.
    beyond_gate2 = status[IDX_MOTION] and _truthy(production.get("video"))
    rec2 = gate_record(ledger, ep, 2)
    if beyond_gate2 and rec2 is None:
        findings.append((
            "FAIL",
            "has a motion script and video production has begun "
            "(project_metadata production.video is truthy) but NO gate-2 approval "
            "record in _management/approvals.json."
        ))

    # sha256 drift + missing-artifact WARNs for the records that DO exist.
    for gate, rec in ((1, rec1), (2, rec2)):
        if rec is None:
            continue
        artifact = rec.get("artifact", "")
        recorded = rec.get("sha256", "")
        abspath = os.path.join(repo_root, artifact)
        if not os.path.isfile(abspath):
            findings.append((
                "WARN",
                f"gate-{gate} approval references a missing artifact: {artifact}."
            ))
            continue
        actual = sha256_file(abspath)
        if recorded and actual and recorded != actual:
            findings.append((
                "WARN",
                f"gate-{gate} stale approval - artifact changed after approval: "
                f"{artifact} (ledger sha != disk sha)."
            ))
    return findings


# -------------------------------------------------------------------
# PER-EPISODE ASSEMBLY
# -------------------------------------------------------------------

def check_episode(ep: str, ledger: list, metadata: dict, repo_root: str = "."):
    """Return (status, findings) for one episode; findings are (severity, message).
    status is None if the episode folder does not exist."""
    status = episode_status(ep)
    if status is None:
        return None, []

    production = declared_production(metadata, ep)
    findings = []

    # 1. Skipped steps (waiver-aware).
    waiver = episode_waiver(ledger, ep)
    for i in nonsequential_skips(status):
        step = PIPELINE_STEPS[i]
        later = next(
            (PIPELINE_STEPS[j]["name"] for j in range(i + 1, len(status)) if status[j]),
            "a later step",
        )
        detail = (
            f"step {step['step']} ({step['name']}) is empty but a later step "
            f"({later}) is present -> skipped step"
        )
        if waiver is not None:
            findings.append((
                "WARN",
                f"{detail}. WAIVERED by approvals ledger (episode-{ep} gate-"
                f"{waiver.get('gate')}: {waiver.get('note', '').split('.')[0]})."
            ))
        else:
            findings.append((
                "FAIL",
                f"{detail} with NO waiver record in _management/approvals.json."
            ))

    # 2. Disk vs declared state machine.
    findings.extend(disk_declared_conflicts(status, production))

    # 3. Approval gates as data.
    findings.extend(gate_findings(ep, status, ledger, production, repo_root))

    return status, findings


def print_episode(ep: str, status, findings) -> None:
    print(f"\n  Checking episode-{ep}")
    print("  " + "-" * 48)
    for step, done in zip(PIPELINE_STEPS, status):
        mark = "[x]" if done else "[ ]"
        gate = f"   <- {step['gate']}" if step.get("gate") else ""
        state = "" if done else " (pending)"
        print(f"    {mark} Step {step['step']}: {step['name']}{state}{gate}")
    for sev, msg in findings:
        print(f"    {sev}: episode-{ep}: {msg}")


# -------------------------------------------------------------------
# RUNNER
# -------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Robotiko Pipeline Integrity Checker")
    parser.add_argument("--episode", type=str, help="Episode number (e.g., 02)")
    parser.add_argument("--full", action="store_true", help="Scan all episode folders")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 - Pipeline Integrity Checker")
    print("=" * 50)

    if args.episode:
        episodes = [args.episode.zfill(2)]
    elif args.full:
        episodes = sorted(
            d.replace("episode-", "") for d in os.listdir(".")
            if d.startswith("episode-") and os.path.isdir(d)
        )
    else:
        print("  Usage: python tests/pipeline_integrity.py --episode 02 | --full")
        sys.exit(0)

    ledger = load_approvals(repo_root)
    metadata = load_metadata(repo_root)
    if not ledger:
        print("  WARN: approvals ledger (_management/approvals.json) is empty or "
              "unreadable - gate checks cannot run.")

    fails, warns, waivered_skips = [], [], []
    for ep in episodes:
        status, findings = check_episode(ep, ledger, metadata, repo_root)
        if status is None:
            print(f"\n  episode-{ep}: folder not found, skipping")
            continue
        print_episode(ep, status, findings)
        for sev, msg in findings:
            tagged = f"episode-{ep}: {msg}"
            if sev == "FAIL":
                fails.append(tagged)
            elif "WAIVERED" in msg:
                waivered_skips.append(tagged)
            else:
                warns.append(tagged)

    print("\n" + "=" * 50)
    if fails:
        print(f"  PIPELINE INTEGRITY FAILED - {len(fails)} issue(s):")
        for f in fails:
            print(f"    - {f}")
        for w in warns + waivered_skips:
            print(f"    (warn) {w}")
        sys.exit(1)

    # Honest PASS summary: name the waivered legacy skips and any stale approvals
    # instead of the old blanket "no skipped steps detected".
    skip_note = (
        f"{len(waivered_skips)} legacy skip(s) waivered by the approvals ledger"
        if waivered_skips else "no skipped steps"
    )
    warn_note = f"{len(warns)} stale-approval/other warning(s)" if warns else "no stale approvals"
    print(f"  PIPELINE INTEGRITY PASSED - {skip_note}; {warn_note}; "
          f"no unwaivered skipped steps and no disk/metadata contradictions.")
    for w in waivered_skips:
        print(f"    (waivered) {w}")
    for w in warns:
        print(f"    (warn) {w}")
    sys.exit(0)


if __name__ == "__main__":
    main()
