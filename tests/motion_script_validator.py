"""
Robotiko v2.0 — Motion Script Validator
Validates motion script files for:
  1. Mandatory video suffix on every motion prompt
  2. Anti-spawn guard on every motion prompt
  3. Global camera-diversity quotas (no single move >30%, Static >=15%)
  4. Local camera diversity — every 5 consecutive clips use >=3 distinct moves
  5. Accent-move budget — Orbital / Handheld / Crane Up / Crane Down <=3 uses each
  6. One camera move per clip — no combined moves ("Pan Left + Zoom In")
  7. Episode camera personality — declared dominant move is among the most-used (WARN)

Severity model: files generated with SKILL v2.0+ FAIL on a machine rule
(1-6); pre-v2 files WARN-only (they predate the rule). Personality (7) is
always WARN — it is an artistic-judgement signal, not a hard gate.

Dependencies: standard library only.

Usage:
    python tests/motion_script_validator.py --full
    python tests/motion_script_validator.py --file episode-09/05_video/ep09_motion_script_v01.md

Status: IMPLEMENTED v1.1
"""

import os
import re
import sys
import glob
import argparse
from collections import Counter

# universe_config lives beside this file — the single source for universe-specific
# validator constants (video suffix, anti-spawn guard, ...). Insert its directory so the
# import resolves whether we run as a script (tests/ is sys.path[0]), as a subprocess
# from the repo root, or loaded by path in the meta-tests (repo root is sys.path[0]).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import universe_config

# Universe-specific values come from universe_config (fork there, not here). The
# module-level aliases keep existing references pointing at the single source.
MANDATORY_VIDEO_SUFFIX = universe_config.VIDEO_SUFFIX

ANTI_SPAWN_GUARD = universe_config.ANTI_SPAWN_GUARD
ANTI_SPAWN_ALTERNATIVES = universe_config.ANTI_SPAWN_ALTERNATIVES

# Scaffold detection is STRUCTURAL placeholders only ("{XX}", "[Claude generates").
# 2026-07-05: the prose markers ("auto-populated by Claude", "Do not fill manually")
# were dropped — EP05's real, shipped 32-clip script keeps that template note line
# at the top, and the coarse marker silently skipped the whole file (a false skip,
# same shape as the EP01 PDF story). A true scaffold always carries {XX} tokens.
SCAFFOLD_MARKERS = ("[Claude generates", "{XX}")

MAX_SINGLE_MOVE_PCT = 30
MIN_STATIC_PCT = 15

# Local camera-diversity rule (SKILL "Camera Move Diversity Rule", ~line 424):
# every window of 5 consecutive clips must use at least 3 different moves.
WINDOW_SIZE = 5
WINDOW_MIN_DISTINCT = 3

# Accent moves are reserved for emotional peaks. SKILL says "max 2-3 uses per
# episode" and the post-generation checklist pins it as "<=3 uses each": 2-3 is
# the soft zone, >3 is the violation.
ACCENT_MOVES = ("Orbital", "Handheld", "Crane Up", "Crane Down")
ACCENT_BUDGET = 3

# Approved camera-move vocabulary (SKILL "Camera Move Vocabulary").
CAMERA_VOCAB = {
    "Static", "Slow Zoom In", "Slow Zoom Out", "Pan Left", "Pan Right",
    "Tilt Up", "Tilt Down", "Crane Up", "Crane Down", "Handheld",
    "Dolly In", "Dolly Out", "Orbital",
}

# Declared dominant camera move per Episode Camera Personality (SKILL EP07-10).
# EP10 ("The Companion Camera") has no single declared dominant move -> skipped.
EPISODE_PERSONALITY = {
    "07": "Dolly Out",     # THE RETREATING CAMERA
    "08": "Static",        # THE WITNESSING CAMERA (Static + Crane)
    "09": "Slow Zoom Out", # THE DISCOVERING CAMERA
}
# "Among the most-used" == within the top-N distinct move-counts. A 13-move
# vocabulary makes rank-3 still a legitimate reading of "the camera feels like X".
PERSONALITY_TOP_N = 3


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


def _strip_annotation(move: str) -> str:
    """Drop a trailing parenthetical annotation: 'Static (locked off)' -> 'Static'."""
    return re.sub(r"\s*\(.*\)\s*$", "", move).strip()


def _vocab_moves_in(value: str) -> list:
    """All approved vocabulary moves that appear inside one Camera Move value."""
    return sorted(m for m in CAMERA_VOCAB if m in value)


def check_single_move(moves: list, sev: str, rel: str) -> list:
    """One camera move per clip: a Camera Move value naming 2+ vocabulary moves
    is a combined move ('Pan Left | Slow Zoom In') — conflicting instructions."""
    findings = []
    for line_num, move in moves:
        found = _vocab_moves_in(move)
        if len(found) >= 2:
            findings.append((sev, f"{rel}: line {line_num} combines multiple camera moves "
                                  f"in one clip ({' | '.join(found)}) - one move per clip"))
    return findings


def check_local_diversity(moves: list, sev: str, rel: str) -> list:
    """Local variety: every WINDOW_SIZE consecutive clips must use at least
    WINDOW_MIN_DISTINCT different moves (catches A-B-A-B monotony that the
    global 30% quota is blind to)."""
    findings = []
    values = [_strip_annotation(mv) for _, mv in moves]
    for i in range(0, len(values) - WINDOW_SIZE + 1):
        window = values[i:i + WINDOW_SIZE]
        distinct = len(set(window))
        if distinct < WINDOW_MIN_DISTINCT:
            findings.append((sev, f"{rel}: clips {i + 1}-{i + WINDOW_SIZE} use only "
                                  f"{distinct} distinct moves ({', '.join(window)}) - "
                                  f"every {WINDOW_SIZE} consecutive clips need >={WINDOW_MIN_DISTINCT}"))
    return findings


def check_accent_budget(moves: list, sev: str, rel: str) -> list:
    """Accent moves (Orbital/Handheld/Crane Up/Crane Down) are reserved for
    emotional peaks. SKILL says 'max 2-3 uses per episode': 2-3 is the soft
    zone, >ACCENT_BUDGET (3) is the violation."""
    findings = []
    counter = Counter(_strip_annotation(mv) for _, mv in moves)
    for accent in ACCENT_MOVES:
        count = counter.get(accent, 0)
        if count > ACCENT_BUDGET:
            findings.append((sev, f"{rel}: accent move '{accent}' used {count} times - "
                                  f"max {ACCENT_BUDGET} per episode (SKILL soft zone is 2-3)"))
    return findings


def check_camera_personality(episode: str, moves: list, rel: str) -> list:
    """EP07-09 declare a camera personality with a dominant move; verify it is
    among the most-used moves (top PERSONALITY_TOP_N). Always WARN — whether the
    camera 'feels like' its personality is artistic judgement, not arithmetic."""
    declared = EPISODE_PERSONALITY.get(episode)
    if not declared or not moves:
        return []
    counter = Counter(_strip_annotation(mv) for _, mv in moves)
    top = [m for m, _ in counter.most_common(PERSONALITY_TOP_N)]
    if declared not in top:
        return [("WARN", f"{rel}: EP{episode} personality move '{declared}' is not among "
                         f"the top {PERSONALITY_TOP_N} used moves ({', '.join(top)}) - "
                         f"verify the episode camera personality is honored")]
    return []


def episode_number_from_path(path: str) -> str:
    m = re.search(r"ep(\d\d)_motion_script", os.path.basename(path))
    return m.group(1) if m else ""


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

    findings.extend(check_single_move(moves, sev, rel))
    findings.extend(check_local_diversity(moves, sev, rel))
    findings.extend(check_accent_budget(moves, sev, rel))
    findings.extend(check_camera_personality(episode_number_from_path(path), moves, rel))

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
        warns = [f for f in findings if f[0] == "WARN"]

        if fails:
            total_fail += len(fails)
            print(f"\n  {rel}")
            for sev, msg in findings:
                print(f"    {sev}: {msg}")
        elif warns:
            print(f"\n  {rel} - {len(warns)} warning(s) (pre-SKILL-v2 / advisory)")
            for sev, msg in warns:
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
