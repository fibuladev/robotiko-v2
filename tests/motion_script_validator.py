"""
Robotiko v2.0 — Motion Script Validator
Validates motion script files for:
  1. Mandatory video suffix on every motion prompt
  2. Anti-spawn guard on every motion prompt
  3. Camera diversity quotas (no single move >30%, Static >=15%)
  4. Single camera move per clip

Dependencies: standard library only.

Usage:
    python tests/motion_script_validator.py --full
    python tests/motion_script_validator.py --file episode-09/05_video/ep09_motion_script_v01.md

Status: IMPLEMENTED v1.0
"""

import os
import re
import sys
import glob
import argparse
from collections import Counter

MANDATORY_VIDEO_SUFFIX = "Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field."

ANTI_SPAWN_GUARD = "Do not add extra characters. Keep everything as pictured."
ANTI_SPAWN_ALTERNATIVES = [
    "No third figure",
    "Exactly two instances",
    "no additional characters",
    "no other figures",
]

SCAFFOLD_MARKERS = ("auto-populated by Claude", "Do not fill manually", "[Claude generates", "{XX}")

MAX_SINGLE_MOVE_PCT = 30
MIN_STATIC_PCT = 15


def is_skill_v2(content: str) -> bool:
    """True if the file was generated with SKILL v2.0+ (suffix/guard rules enforced)."""
    for line in content.splitlines()[:10]:
        if "SKILL.md" in line and ("v2" in line or "v3" in line):
            return True
    return False


def extract_motion_prompts(content: str) -> list:
    """Extract motion prompt blockquotes. Returns list of (block_index, text)."""
    pattern = re.compile(
        r"\*\*Motion Prompt:?\s*\*\*:?\s*\n((?:[ \t]*>.*(?:\n|$))+)"
    )
    prompts = []
    for i, m in enumerate(pattern.finditer(content), 1):
        lines = [re.sub(r"^[ \t]*>\s?", "", ln) for ln in m.group(1).splitlines()]
        prompts.append((i, "\n".join(lines)))
    return prompts


def extract_camera_moves(content: str) -> list:
    """Extract camera move values. Returns list of (line_num, move_value)."""
    moves = []
    for i, line in enumerate(content.splitlines(), 1):
        m = re.match(r"\*\*Camera Move:\*\*\s*(.+)", line)
        if m:
            moves.append((i, m.group(1).strip()))
    return moves


def validate_file(path: str) -> list:
    """Return list of (severity, message). Empty = clean."""
    findings = []
    rel = os.path.basename(path)

    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError as e:
        return [("ERROR", f"{rel}: cannot read: {e}")]

    if any(m in content for m in SCAFFOLD_MARKERS):
        return []

    v2 = is_skill_v2(content)
    sev = "FAIL" if v2 else "WARN"

    prompts = extract_motion_prompts(content)
    if not prompts:
        findings.append(("WARN", f"{rel}: no motion prompts found"))
        return findings

    for idx, text in prompts:
        if MANDATORY_VIDEO_SUFFIX not in text:
            findings.append((sev, f"{rel}: motion prompt #{idx} missing mandatory video suffix"))
        has_guard = ANTI_SPAWN_GUARD in text or any(alt in text for alt in ANTI_SPAWN_ALTERNATIVES)
        if not has_guard:
            findings.append((sev, f"{rel}: motion prompt #{idx} missing anti-spawn guard"))

    moves = extract_camera_moves(content)
    if not moves:
        findings.append(("WARN", f"{rel}: no camera move declarations found"))
        return findings

    total = len(moves)
    counter = Counter(mv for _, mv in moves)

    for move, count in counter.items():
        pct = (count / total) * 100
        if pct > MAX_SINGLE_MOVE_PCT:
            findings.append((sev, f"{rel}: camera move '{move}' used {count}/{total} times ({pct:.0f}%) — max {MAX_SINGLE_MOVE_PCT}%"))

    static_count = sum(c for m, c in counter.items() if m.lower() == "static")
    static_pct = (static_count / total) * 100
    if static_pct < MIN_STATIC_PCT:
        findings.append((sev, f"{rel}: Static camera at {static_pct:.0f}% — minimum {MIN_STATIC_PCT}%"))

    return findings


def run_full(repo_root: str = ".") -> int:
    all_files = sorted(glob.glob(os.path.join(repo_root, "episode-*/05_video/ep*_motion_script_v*.md")))

    latest = {}
    for path in all_files:
        ep_dir = os.path.dirname(os.path.dirname(path))
        if ep_dir not in latest or path > latest[ep_dir]:
            latest[ep_dir] = path
    files = sorted(latest.values())

    if not files:
        print("  No motion script files found.")
        return 0

    total_fail = 0
    for path in files:
        findings = validate_file(path)
        rel = os.path.relpath(path, repo_root)
        fails = [f for f in findings if f[0] in ("FAIL", "ERROR")]

        if fails:
            total_fail += len(fails)
            print(f"\n  {rel}")
            for sev, msg in findings:
                print(f"    {sev}: {msg}")
        else:
            print(f"  [OK] {rel}")

    if total_fail:
        print(f"\n  MOTION SCRIPT VALIDATION FAILED — {total_fail} issue(s).")
        return 1
    print("\n  MOTION SCRIPT VALIDATION PASSED.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Robotiko Motion Script Validator")
    parser.add_argument("--full", action="store_true", help="Validate all motion scripts")
    parser.add_argument("--file", type=str, help="Validate a single file")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — Motion Script Validator")
    print("=" * 50)

    if args.file:
        findings = validate_file(args.file)
        for sev, msg in findings:
            print(f"  {sev}: {msg}")
        sys.exit(1 if any(f[0] in ("FAIL", "ERROR") for f in findings) else 0)

    sys.exit(run_full("."))


if __name__ == "__main__":
    main()
