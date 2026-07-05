"""
Robotiko v2.0 - Energy -> Motion Cross-Check (ADVISORY TIER)

The motion SKILL ("Step 2: Map Energy to Motion") maps each musical energy
level to a Motion Strength (MS) band. This check verifies, clip by clip, that
a motion script's MS values fall inside the band of the musical section the
clip sits in (section found by the clip's timestamp midpoint in the episode's
musical_metadata.json).

This is HEURISTIC, art-adjacent territory - the SKILL itself sanctions
intentional mismatch ("Musical Dissonance as Choice"). Therefore:

  * Severity is WARN everywhere. This check NEVER fails the build; run_all
    treats a non-zero exit as blocking, so we exit 0 unless a file is
    unreadable/corrupt (ERROR).
  * [DISSONANCE]-tagged shots are exempt - that is the tag's entire purpose.
    The tag is shot-scoped: it lives in the shot's Musical Moment field and
    covers all of that shot's sub-clips.
  * Ramp/transition energies (building, rising, fading, slowing) get their
    band widened by +-1 - a ramp passes through values by design.
  * Pre-SKILL-v2 episodes are SKIPPED: the band mapping is a v2 rule; grading
    EP01-06 against it would be anachronistic noise.
  * A global +-1 soft tolerance is applied by default (MS is a coarse 1-10
    dial; one step off the band is an equivalent artistic reading, not a
    deviation worth surfacing). `--strict` disables it for audits.

Dependencies: standard library only.

Usage:
    python tests/energy_motion_check.py --full
    python tests/energy_motion_check.py --full --strict
    python tests/energy_motion_check.py --episode 08

Status: IMPLEMENTED v1.0
"""

import os
import re
import sys
import json
import glob
import argparse

# SKILL "Step 2: Map Energy to Motion" - energy level -> (MS low, MS high).
# Ramp energies ("ramps progressively") have no fixed band in the SKILL; they
# are given the widest sensible span and are additionally widened +-1 below.
ENERGY_MS_BANDS = {
    "minimal":     (1, 1),
    "low":         (1, 3),
    "medium-low":  (2, 3),
    "medium":      (4, 5),
    "medium-high": (5, 6),
    "high":        (6, 8),
    "peak":        (8, 10),
    "explosive":   (9, 10),
    "theatrical":  (5, 7),
    "epic":        (6, 8),
    "chaotic":     (8, 10),
    "still":       (1, 2),
    # Ramps - MS "ramps progressively within the section":
    "building":    (4, 8),
    "rising":      (4, 8),
    "fading":      (1, 5),
    "slowing":     (1, 4),
}

RAMP_ENERGIES = {"building", "rising", "fading", "slowing"}

# One MS step off the band is an equivalent reading of a coarse dial.
DEFAULT_TOLERANCE = 1

SCAFFOLD_MARKERS = ("[Claude generates", "{XX}")


def is_skill_v2(content: str) -> bool:
    """Same v2 detection as motion_script_validator.py (header line check)."""
    for line in content.splitlines()[:10]:
        if "SKILL.md" in line and ("v2" in line or "v3" in line):
            return True
    return False


def _mmss_to_seconds(ts: str) -> float:
    minutes, seconds = ts.strip().split(":")
    return int(minutes) * 60 + int(seconds)


def parse_timestamp_range(value: str):
    """Parse '0:15-0:26' (any dash flavor) -> (15.0, 26.0). None if unparseable."""
    normalized = value.replace("–", "-").replace("—", "-")
    m = re.search(r"(\d+:\d+)\s*-\s*(\d+:\d+)", normalized)
    if not m:
        return None
    return _mmss_to_seconds(m.group(1)), _mmss_to_seconds(m.group(2))


def extract_clips(content: str) -> list:
    """Parse a motion script into clips: dicts with shot id, (start, end)
    timestamp, motion strength, and shot-scoped dissonance flag. Sub-clips of
    a multi-clip shot share the shot's timestamp (midpoint approximation)."""
    clips = []
    shot = None
    ts = None
    dissonant = False
    for line in content.splitlines():
        header = re.match(r"###\s+SHOT\s+(S\d+\w?)", line)
        if header:
            shot = header.group(1)
            ts = None
            dissonant = False
            continue
        if re.match(r"##\s+[^#]", line):
            # h2 section boundary (Beat Sync Notes, Diversity Report, ...):
            # leave shot scope so a [DISSONANCE] mention in a summary table
            # cannot retroactively exempt the last shot.
            shot = None
            dissonant = False
            continue
        if shot is None:
            continue
        ts_row = re.search(r"\*\*Timestamp\*\*\s*\|\s*([^|]+)\|", line)
        if ts_row:
            ts = parse_timestamp_range(ts_row.group(1))
            continue
        if "[DISSONANCE]" in line:
            dissonant = True
            # retroactively exempt sub-clips of this shot already collected
            for clip in clips:
                if clip["shot"] == shot:
                    clip["dissonance"] = True
            continue
        ms_row = re.search(r"\*\*Motion Strength\*\*\s*\|\s*(\d+)", line)
        if ms_row:
            clips.append({
                "shot": shot,
                "ts": ts,
                "ms": int(ms_row.group(1)),
                "dissonance": dissonant,
            })
    return clips


def load_sections(metadata_path: str):
    with open(metadata_path, encoding="utf-8") as f:
        return json.load(f)["sections"]


def section_at(sections: list, t: float):
    """The musical section containing time t (start-inclusive, end-exclusive).
    None if t falls in a gap between sections."""
    for sec in sections:
        if sec["start"] <= t < sec["end"]:
            return sec
    return None


def check_energy_motion(clips: list, sections: list, rel: str,
                        tolerance: int = DEFAULT_TOLERANCE) -> list:
    """WARN findings for clips whose MS falls outside the SKILL band of their
    musical section's energy. DISSONANCE shots exempt; ramp bands widened +-1."""
    findings = []
    for clip in clips:
        if clip["ts"] is None or clip["dissonance"]:
            continue
        start, end = clip["ts"]
        midpoint = (start + end) / 2.0
        sec = section_at(sections, midpoint)
        if sec is None:
            continue  # gap between sections - nothing to grade against
        energy = sec.get("energy")
        band = ENERGY_MS_BANDS.get(energy)
        if band is None:
            findings.append(("WARN", f"{rel}: {clip['shot']} sits in a section with "
                                     f"unmapped energy '{energy}' - extend ENERGY_MS_BANDS"))
            continue
        lo, hi = band
        widen = tolerance + (1 if energy in RAMP_ENERGIES else 0)
        lo, hi = max(1, lo - widen), min(10, hi + widen)
        if not (lo <= clip["ms"] <= hi):
            findings.append(("WARN", f"{rel}: {clip['shot']} MS {clip['ms']} outside "
                                     f"band {lo}-{hi} for '{energy}' ({sec.get('type')} "
                                     f"@ {sec['start']:.0f}-{sec['end']:.0f}s) - in-band, "
                                     f"or tag [DISSONANCE] with justification"))
    return findings


def validate_episode(ep: str, repo_root: str = ".", tolerance: int = DEFAULT_TOLERANCE) -> list:
    """Findings for one episode: latest motion script vs its musical metadata."""
    scripts = sorted(glob.glob(os.path.join(
        repo_root, f"episode-{ep}", "05_video", f"ep{ep}_motion_script_v*.md")))
    metadata = os.path.join(
        repo_root, f"episode-{ep}", "02_music", f"ep{ep}_musical_metadata.json")
    if not scripts or not os.path.isfile(metadata):
        return []

    path = scripts[-1]
    rel = os.path.basename(path)
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError as e:
        return [("ERROR", f"{rel}: cannot read: {e}")]

    if any(m in content for m in SCAFFOLD_MARKERS):
        return []
    if not is_skill_v2(content):
        return []  # pre-v2 episode: the band mapping postdates it - skip

    try:
        sections = load_sections(metadata)
    except (OSError, json.JSONDecodeError, KeyError) as e:
        return [("ERROR", f"{os.path.basename(metadata)}: cannot load sections: {e}")]

    clips = extract_clips(content)
    if not clips:
        return [("WARN", f"{rel}: SKILL-v2 script parsed to zero MS clips - "
                         f"nothing cross-checked (format drift?)")]
    return check_energy_motion(clips, sections, rel, tolerance)


def run_full(repo_root: str = ".", tolerance: int = DEFAULT_TOLERANCE) -> int:
    episodes = sorted(
        re.match(r".*episode-(\d\d)$", d).group(1)
        for d in glob.glob(os.path.join(repo_root, "episode-*"))
        if re.match(r".*episode-\d\d$", d)
    )
    total_error = 0
    any_warn = False
    for ep in episodes:
        findings = validate_episode(ep, repo_root, tolerance)
        errors = [f for f in findings if f[0] == "ERROR"]
        warns = [f for f in findings if f[0] == "WARN"]
        total_error += len(errors)
        if findings:
            any_warn = any_warn or bool(warns)
            print(f"\n  episode-{ep} - {len(warns)} advisory deviation(s)")
            for sev, msg in findings:
                print(f"    {sev}: {msg}")
        else:
            print(f"  [OK] episode-{ep}")

    if total_error:
        print(f"\n  ENERGY-MOTION CHECK ERRORED - {total_error} unreadable input(s).")
        return 1
    if any_warn:
        print("\n  ENERGY-MOTION CHECK PASSED (advisory warnings above - heuristic tier, non-blocking).")
    else:
        print("\n  ENERGY-MOTION CHECK PASSED.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Robotiko Energy->Motion Cross-Check (advisory)")
    parser.add_argument("--full", action="store_true", help="Check all episodes")
    parser.add_argument("--episode", type=str, help="Check a single episode (e.g., 08)")
    parser.add_argument("--strict", action="store_true",
                        help="Disable the +-1 soft tolerance (audit mode)")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)
    tolerance = 0 if args.strict else DEFAULT_TOLERANCE

    print("Robotiko v2.0 - Energy->Motion Cross-Check (advisory tier)")
    print("=" * 50)

    if args.episode:
        ep = args.episode.zfill(2)
        findings = validate_episode(ep, ".", tolerance)
        for sev, msg in findings:
            print(f"  {sev}: {msg}")
        if not findings:
            print(f"  [OK] episode-{ep}")
        sys.exit(1 if any(f[0] == "ERROR" for f in findings) else 0)

    sys.exit(run_full(".", tolerance))


if __name__ == "__main__":
    main()
