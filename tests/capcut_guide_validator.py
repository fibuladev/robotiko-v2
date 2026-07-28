"""
Robotiko v2.0 — CapCut Guide Validator
Validates capcut_guide markdown files for timing integrity.

Checks:
  1. Scene Dur matches Timestamp span (the gap-propagation bug)
  2. Timestamps are contiguous (no gaps between scenes)
  3. Total timeline equals music duration (from musical metadata)
  4. Speed values are correct: clip_dur / scene_dur (±0.02 tolerance)
  5. Trim values are correct: clip_dur - scene_dur (±1s tolerance)

Dependencies: standard library only.

Usage:
    python tests/capcut_guide_validator.py --full
    python tests/capcut_guide_validator.py --file episode-09/06_edit/ep09_capcut_guide_v01.md

Status: IMPLEMENTED v1.0
"""

import os
import re
import sys
import json
import glob
import argparse


SCAFFOLD_MARKERS = ("[Claude generates", "{XX}")


def parse_timestamp(ts):
    """Parse M:SS or MM:SS into total seconds."""
    parts = ts.strip().split(":")
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]) * 60 + int(parts[1])
    except ValueError:
        return None


def parse_duration(dur_str):
    """Parse '14s', '~9s', or '~9.5s' into (rounded_int, is_approx) tuple."""
    stripped = dur_str.strip()
    approx = stripped.startswith("~")
    m = re.match(r"~?(\d+(?:\.\d+)?)s", stripped)
    if not m:
        return None, False
    return round(float(m.group(1))), approx


def parse_speed(speed_str):
    """Parse '0.71×' or '—' into float or None."""
    speed_str = speed_str.strip().replace("×", "").replace("x", "")
    if speed_str in ("—", "-", ""):
        return None
    try:
        return float(speed_str)
    except ValueError:
        return None


def parse_trim(trim_str):
    """Parse 'trim 3s' or '—' into integer seconds or None."""
    trim_str = trim_str.strip()
    if trim_str in ("—", "-", ""):
        return None
    m = re.search(r"trim\s+(\d+)s", trim_str)
    return int(m.group(1)) if m else None


def extract_episode_number(path):
    """Extract episode number from path like episode-09/06_edit/ep09_capcut_guide_v01.md."""
    m = re.search(r"episode-(\d{2})", path)
    return m.group(1) if m else None


def load_music_duration(repo_root, ep_num):
    """Load total_duration from the episode's musical metadata."""
    meta_path = os.path.join(repo_root, f"episode-{ep_num}", "02_music",
                             f"ep{ep_num}_musical_metadata.json")
    if not os.path.isfile(meta_path):
        return None
    try:
        with open(meta_path, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("total_duration")
    except (json.JSONDecodeError, OSError):
        return None


def parse_timeline_table(content):
    """Parse the Timeline Map table from the guide content.

    Returns list of dicts with keys: shot, ts_start, ts_end, scene_dur,
    clip_dur, speed, trim, trim_raw, line_num.
    """
    rows = []
    in_table = False
    header_seen = False

    for line_num, line in enumerate(content.splitlines(), 1):
        stripped = line.strip()

        if re.match(r"\|\s*Shot\s*\|.*Timestamp.*Scene Dur", stripped, re.IGNORECASE):
            in_table = True
            header_seen = False
            continue

        if in_table and re.match(r"\|\s*-+", stripped):
            header_seen = True
            continue

        if in_table and header_seen and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")]
            cells = [c for c in cells if c != ""]

            if len(cells) < 6:
                continue

            shot = cells[0]

            ts_match = re.match(r"(\d+:\d+)\s*[–—-]\s*(\d+:\d+)", cells[1])
            if not ts_match:
                continue

            ts_start = parse_timestamp(ts_match.group(1))
            ts_end = parse_timestamp(ts_match.group(2))

            scene_dur, scene_dur_approx = parse_duration(cells[3])
            clip_dur, _ = parse_duration(cells[4])
            speed = parse_speed(cells[5])
            trim_raw = cells[6] if len(cells) > 6 else ""
            trim = parse_trim(trim_raw)

            if ts_start is None or ts_end is None:
                continue

            rows.append({
                "shot": shot,
                "ts_start": ts_start,
                "ts_end": ts_end,
                "scene_dur": scene_dur,
                "scene_dur_approx": scene_dur_approx,
                "clip_dur": clip_dur,
                "speed": speed,
                "trim": trim,
                "trim_raw": trim_raw,
                "line_num": line_num,
            })

        elif in_table and header_seen and not stripped.startswith("|") and not stripped.startswith(">"):
            break

    return rows


def validate_file(path, repo_root="."):
    """Return list of (severity, message) tuples. Empty = clean."""
    findings = []
    rel = os.path.relpath(path, repo_root)

    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError as e:
        return [("ERROR", f"{rel}: cannot read file: {e}")]

    if any(m in content for m in SCAFFOLD_MARKERS):
        return []

    rows = parse_timeline_table(content)
    if not rows:
        findings.append(("WARN", f"{rel}: no Timeline Map table found"))
        return findings

    ep_num = extract_episode_number(path)
    music_dur = load_music_duration(repo_root, ep_num) if ep_num else None

    total_scene_dur = 0
    prev_end = None

    for i, row in enumerate(rows):
        shot = row["shot"]
        ts_span = row["ts_end"] - row["ts_start"]
        scene_dur = row["scene_dur"]
        scene_dur_approx = row["scene_dur_approx"]
        clip_dur = row["clip_dur"]
        speed = row["speed"]
        trim = row["trim"]
        ln = row["line_num"]

        if scene_dur is not None:
            total_scene_dur += ts_span

            tolerance = 1 if scene_dur_approx else 0
            if abs(ts_span - scene_dur) > tolerance:
                findings.append((
                    "FAIL",
                    f"{rel} L{ln}: {shot} Scene Dur ({scene_dur}s) != "
                    f"Timestamp span ({ts_span}s) — gap-propagation bug"
                ))

        if prev_end is not None and row["ts_start"] != prev_end:
            gap = row["ts_start"] - prev_end
            findings.append((
                "FAIL",
                f"{rel} L{ln}: {shot} timestamp gap — starts at "
                f"{row['ts_start']}s but previous scene ended at {prev_end}s "
                f"(gap = {gap}s)"
            ))

        prev_end = row["ts_end"]

        if speed is not None and scene_dur is not None and clip_dur is not None:
            if abs(speed - 1.0) < 0.01:
                pass
            else:
                expected_speed = round(clip_dur / scene_dur, 2)
                if abs(speed - expected_speed) > 0.02:
                    findings.append((
                        "FAIL",
                        f"{rel} L{ln}: {shot} Speed ({speed}×) != "
                        f"clip_dur/scene_dur ({clip_dur}/{scene_dur} = "
                        f"{expected_speed}×)"
                    ))

        if trim is not None and scene_dur is not None and clip_dur is not None:
            expected_trim = clip_dur - scene_dur
            if abs(trim - expected_trim) > 1:
                findings.append((
                    "FAIL",
                    f"{rel} L{ln}: {shot} Trim ({trim}s) != "
                    f"clip_dur - scene_dur ({clip_dur} - {scene_dur} = {expected_trim}s)"
                ))

        if (speed is None and trim is None and scene_dur is not None
                and clip_dur is not None and scene_dur != clip_dur):
            if scene_dur > clip_dur:
                findings.append((
                    "WARN",
                    f"{rel} L{ln}: {shot} needs speed ramp "
                    f"({clip_dur}s → {scene_dur}s) but none specified"
                ))
            else:
                findings.append((
                    "WARN",
                    f"{rel} L{ln}: {shot} needs trim "
                    f"({clip_dur}s → {scene_dur}s) but none specified"
                ))

    if music_dur is not None and total_scene_dur > 0:
        if abs(total_scene_dur - music_dur) > 1:
            findings.append((
                "FAIL",
                f"{rel}: total Scene Dur ({total_scene_dur}s) != "
                f"music duration ({music_dur}s) — deficit = {music_dur - total_scene_dur}s"
            ))

    return findings


def run_full(repo_root="."):
    pattern = os.path.join(repo_root, "episode-*/06_edit/ep*_capcut_guide_v*.md")
    files = sorted(glob.glob(pattern))

    if not files:
        print("  No CapCut guide files found.")
        return 0

    total_fail = 0
    for path in files:
        findings = validate_file(path, repo_root)
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
        print(f"\n  CAPCUT GUIDE VALIDATION FAILED — {total_fail} issue(s).")
        return 1
    print("\n  CAPCUT GUIDE VALIDATION PASSED.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Robotiko CapCut Guide Validator")
    parser.add_argument("--full", action="store_true",
                        help="Validate all episode CapCut guides")
    parser.add_argument("--file", type=str,
                        help="Validate a single guide file")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — CapCut Guide Validator")
    print("=" * 50)

    if args.file:
        if not os.path.isfile(args.file):
            print(f"  File not found: {args.file}")
            sys.exit(1)
        findings = validate_file(args.file, ".")
        for sev, msg in findings:
            print(f"  {sev}: {msg}")
        if not findings:
            print("  [OK] No issues found.")
        sys.exit(1 if any(f[0] in ("FAIL", "ERROR") for f in findings) else 0)

    sys.exit(run_full("."))


if __name__ == "__main__":
    main()
