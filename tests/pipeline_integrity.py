"""
Robotiko v2.0 - Pipeline Integrity Checker
Validates that no BLOCKING step was skipped in the production pipeline.
Pipeline order: Lyrics -> Musical Metadata -> Concept Notes -> Dramaturgy
                -> Visual Prompts -> Motion Script -> Final Edit

This checker detects SKIPPED STEPS (a later deliverable exists while an earlier
blocking step is missing), NOT completeness. An in-progress or freshly scaffolded
episode (a contiguous prefix of completed steps) is valid and passes.

Unfilled scaffold templates / placeholder stubs (the files create_episode.py drops
into a new episode) are treated as "pending", not "done", so a fresh scaffold does
not trip a false skipped-step violation.

Usage:
    python tests/pipeline_integrity.py --episode 02
    python tests/pipeline_integrity.py --full

Status: IMPLEMENTED v1.1
"""

import os
import re
import sys
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


def check_episode(ep: str):
    """Return (status_list, violations) for one episode, or (None, []) if no folder."""
    folder = f"episode-{ep}"
    if not os.path.isdir(folder):
        return None, []

    status = [step_done(folder, step, ep) for step in PIPELINE_STEPS]

    done_indexes = [i for i, s in enumerate(status) if s]
    last_done = max(done_indexes) if done_indexes else -1

    violations = []
    for i in range(last_done + 1):
        step = PIPELINE_STEPS[i]
        if step["blocking"] and not status[i]:
            later = next(PIPELINE_STEPS[j]["name"] for j in range(i + 1, last_done + 1) if status[j])
            violations.append(
                f"episode-{ep}: blocking step {step['step']} ({step['name']}) is missing "
                f"but a later step ({later}) is present -> skipped step"
            )
    return status, violations


def print_episode(ep: str, status, violations) -> None:
    print(f"\n  Checking episode-{ep}")
    print("  " + "-" * 48)
    for step, done in zip(PIPELINE_STEPS, status):
        mark = "[x]" if done else "[ ]"
        gate = f"   <- {step['gate']}" if step.get("gate") else ""
        state = "" if done else " (pending)"
        print(f"    {mark} Step {step['step']}: {step['name']}{state}{gate}")
    if violations:
        for v in violations:
            print(f"    VIOLATION: {v}")


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

    all_violations = []
    for ep in episodes:
        status, violations = check_episode(ep)
        if status is None:
            print(f"\n  episode-{ep}: folder not found, skipping")
            continue
        print_episode(ep, status, violations)
        all_violations.extend(violations)

    print("\n" + "=" * 50)
    if all_violations:
        print(f"  PIPELINE INTEGRITY FAILED - {len(all_violations)} skipped-step violation(s):")
        for v in all_violations:
            print(f"    - {v}")
        sys.exit(1)
    print("  PIPELINE INTEGRITY PASSED - no skipped steps detected.")
    sys.exit(0)


if __name__ == "__main__":
    main()
