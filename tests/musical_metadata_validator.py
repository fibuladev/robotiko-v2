"""
Robotiko v2.0 — Musical Metadata Validator
Validates musical_metadata.json files for structural integrity and vocabulary compliance.

Checks:
  1. Required top-level fields present
  2. Required per-section fields present
  3. Energy vocabulary compliance (SKILL-defined levels only)
  4. Section type vocabulary compliance
  5. Timestamp monotonicity (no overlaps, ordered start/end)
  6. total_duration matches last section's end (±1s tolerance)

Dependencies: standard library only.

Usage:
    python tests/musical_metadata_validator.py --full
    python tests/musical_metadata_validator.py --episode 02

Status: IMPLEMENTED v1.0
"""

import os
import sys
import json
import glob
import argparse

REQUIRED_TOP_LEVEL = {"track_title", "tempo", "key", "time_signature", "total_duration", "mood", "instruments", "sections"}

OPTIONAL_TOP_LEVEL = {"styles", "spoken_intro_duration"}

REQUIRED_SECTION = {"type", "start", "end", "energy"}

VALID_ENERGY = {
    "minimal", "low", "medium-low", "medium", "medium-high", "high",
    "explosive", "building", "rising", "chaotic", "fading", "still",
    "peak", "theatrical", "epic", "slowing",
}

VALID_SECTION_TYPES = {
    "intro", "verse", "pre-chorus", "pre_chorus", "chorus", "bridge",
    "instrumental", "climax", "outro", "spoken_intro", "outro_vocals",
    "outro_whisper", "vocal", "interlude", "refrain", "spoken",
    "silence", "finale",
}

SCAFFOLD_MARKERS = ("auto-populated by Claude", "Do not fill manually", "[Claude generates", "{XX}")


def validate_file(path: str) -> list:
    """Return list of (severity, message) tuples. Empty = clean."""
    findings = []
    rel = os.path.basename(path)

    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except OSError as e:
        return [("ERROR", f"{rel}: cannot read file: {e}")]

    if any(m in raw for m in SCAFFOLD_MARKERS):
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        return [("ERROR", f"{rel}: invalid JSON: {e}")]

    if not isinstance(data, dict):
        return [("ERROR", f"{rel}: top-level value must be an object")]

    missing_top = REQUIRED_TOP_LEVEL - set(data.keys())
    if missing_top:
        findings.append(("FAIL", f"{rel}: missing required top-level fields: {sorted(missing_top)}"))

    unknown_top = set(data.keys()) - REQUIRED_TOP_LEVEL - OPTIONAL_TOP_LEVEL
    if unknown_top:
        findings.append(("WARN", f"{rel}: unknown top-level fields: {sorted(unknown_top)}"))

    sections = data.get("sections", [])
    if not isinstance(sections, list) or len(sections) == 0:
        findings.append(("FAIL", f"{rel}: 'sections' must be a non-empty array"))
        return findings

    prev_end = None
    for i, sec in enumerate(sections):
        label = f"section[{i}]"

        missing_sec = REQUIRED_SECTION - set(sec.keys())
        if missing_sec:
            findings.append(("FAIL", f"{rel}: {label} missing required fields: {sorted(missing_sec)}"))
            continue

        energy = sec["energy"]
        if energy not in VALID_ENERGY:
            findings.append(("FAIL", f"{rel}: {label} invalid energy '{energy}' — allowed: {sorted(VALID_ENERGY)}"))

        sec_type = sec["type"]
        if sec_type not in VALID_SECTION_TYPES:
            findings.append(("FAIL", f"{rel}: {label} invalid section type '{sec_type}' — allowed: {sorted(VALID_SECTION_TYPES)}"))

        start = sec["start"]
        end = sec["end"]

        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            findings.append(("FAIL", f"{rel}: {label} start/end must be numeric"))
            continue

        if end <= start:
            findings.append(("FAIL", f"{rel}: {label} end ({end}) <= start ({start})"))

        if prev_end is not None and start < prev_end - 0.01:
            findings.append(("WARN", f"{rel}: {label} start ({start}) overlaps previous section end ({prev_end})"))

        prev_end = end

    total_dur = data.get("total_duration")
    if total_dur is not None and prev_end is not None:
        if abs(float(total_dur) - float(prev_end)) > 1.0:
            findings.append(("FAIL", f"{rel}: total_duration ({total_dur}) does not match last section end ({prev_end}) — tolerance ±1s"))

    return findings


def run_full(repo_root: str = ".") -> int:
    pattern = os.path.join(repo_root, "episode-*/02_music/ep*_musical_metadata.json")
    files = sorted(glob.glob(pattern))

    if not files:
        print("  No musical metadata files found.")
        return 0

    total_fail = 0
    for path in files:
        findings = validate_file(path)
        rel = os.path.relpath(path, repo_root)
        fails = [f for f in findings if f[0] == "FAIL"]
        warns = [f for f in findings if f[0] == "WARN"]
        errors = [f for f in findings if f[0] == "ERROR"]

        if fails or errors:
            total_fail += len(fails) + len(errors)
            print(f"\n  {rel}")
            for sev, msg in findings:
                print(f"    {sev}: {msg}")
        elif warns:
            print(f"\n  {rel}")
            for sev, msg in findings:
                print(f"    {sev}: {msg}")
        else:
            print(f"  [OK] {rel}")

    if total_fail:
        print(f"\n  MUSICAL METADATA VALIDATION FAILED — {total_fail} issue(s).")
        return 1
    print("\n  MUSICAL METADATA VALIDATION PASSED.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Robotiko Musical Metadata Validator")
    parser.add_argument("--full", action="store_true", help="Validate all episode metadata")
    parser.add_argument("--episode", type=str, help="Validate a single episode (e.g., 02)")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — Musical Metadata Validator")
    print("=" * 50)

    if args.episode:
        ep = args.episode.zfill(2)
        path = f"episode-{ep}/02_music/ep{ep}_musical_metadata.json"
        if not os.path.isfile(path):
            print(f"  File not found: {path}")
            sys.exit(1)
        findings = validate_file(path)
        for sev, msg in findings:
            print(f"  {sev}: {msg}")
        sys.exit(1 if any(f[0] in ("FAIL", "ERROR") for f in findings) else 0)

    sys.exit(run_full("."))


if __name__ == "__main__":
    main()
