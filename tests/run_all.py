"""
Robotiko v2.0 — One command to run the whole validation backbone.

Runs every machine check in sequence and exits non-zero if ANY of them fails.
This is the single gate: CI calls `python tests/run_all.py`, and a red here blocks
the merge. Locally, run it before you push.

Check groups:
  1. Naming convention      — file/folder names obey the convention
  2. Pipeline integrity     — no silently-skipped pipeline steps
  3. Visual prompt sweep    — suffix · forbidden aesthetics · character phase · ref integrity
  4. Prompt hygiene         — model-facing prompt strings are plain-English ASCII (scoped)
  5. Musical metadata       — JSON structure · energy/type vocabulary · timestamps · overlay convention · total_duration
  6. Motion script          — video suffix · anti-spawn guard · camera diversity (global quotas + 5-clip local window + accent budget + one-move-per-clip + personality)
  7. Character profiles     — structural validation against schema.json
  8. Validator meta-tests   — grade the graders (fixtures + both-directions proofs)
  9. Doc reference integrity — curated docs' backtick paths exist · no hook-rot · matrix sync
 10. Energy-motion sync     — ADVISORY tier: clip Motion Strength vs the musical
     section's energy band (heuristic; warnings are printed but never block)
 11. Forbidden terms        — public prose (canon docs, direction notes, musical
     metadata) never names a banned religion/order/sect/scripture term; a narrow,
     pinned allowlist covers the one sanctioned mention (the rule that bans it)

Dependencies: standard library only. No `pip install`, nothing to pin at the
package level — the strongest form of dependency hygiene. The toolchain (Python
version + CI actions) is pinned in .github/workflows/validation_suite.yml.
"""

import os
import re
import sys
import argparse
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX_PATH = os.path.join(REPO_ROOT, "_management", "invariant_coverage_matrix.md")

# Coverage tiers, keyed by the emoji the matrix uses in its Coverage column. Emoji
# appear ONLY inside table rows (the legend uses bullet lines), so an emoji in a
# pipe-row reliably marks a real coverage cell. Output stays ASCII (tier names).
COVERAGE_TIERS = [
    ("Machine", "\U0001F7E2"),    # green circle
    ("Heuristic", "\U0001F7E1"),  # yellow circle
    ("Human", "\U0001F535"),      # blue circle
    ("Gap", "⚪"),            # white circle
]

CHECK_GROUPS = [
    ("Naming convention",    [sys.executable, "tests/naming_check.py", "--full"]),
    ("Pipeline integrity",   [sys.executable, "tests/pipeline_integrity.py", "--full"]),
    ("Visual prompt sweep",  [sys.executable, "tests/visual_prompt_validator.py", "--full"]),
    ("Prompt hygiene",       [sys.executable, "tests/prompt_hygiene_lint.py", "--full"]),
    ("Musical metadata",     [sys.executable, "tests/musical_metadata_validator.py", "--full"]),
    ("Motion script",        [sys.executable, "tests/motion_script_validator.py", "--full"]),
    ("Character profiles",   [sys.executable, "tests/character_profiles_validator.py", "--full"]),
    ("Validator meta-tests", [sys.executable, "-m", "unittest", "tests.test_validators"]),
    ("Doc reference integrity", [sys.executable, "tests/doc_reference_check.py"]),
    ("Energy-motion sync (advisory)", [sys.executable, "tests/energy_motion_check.py", "--full"]),
    ("Forbidden terms",       [sys.executable, "tests/forbidden_terms_gate.py", "--full"]),
]


def parse_matrix_rows(text: str) -> list:
    """Yield (invariant_name, [tier, ...]) for every coverage-bearing table row in the
    matrix. A row counts toward EVERY tier whose emoji appears in its Coverage cell, so
    a mixed row (e.g. 'Machine (linkage) + Human (judgement)') is counted in both."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2:
            continue
        name, coverage = cells[0], cells[1]
        tiers = [tier for tier, emoji in COVERAGE_TIERS if emoji in coverage]
        if not tiers:
            continue   # header / separator / non-coverage row (no tier emoji)
        # Strip markdown emphasis from the invariant name for a clean listing.
        name = re.sub(r"[*`]", "", name).strip()
        rows.append((name, tiers))
    return rows


def coverage_summary() -> int:
    """Print the coverage summary derived from the Invariant Coverage Matrix: a count
    per tier, and every Human + Gap row by name (what we do NOT machine-guarantee).
    One command answers both 'did it pass' (run_all) and 'what is not guaranteed'."""
    if not os.path.isfile(MATRIX_PATH):
        print(f"  Coverage matrix not found: {MATRIX_PATH}")
        return 1
    with open(MATRIX_PATH, encoding="utf-8") as f:
        rows = parse_matrix_rows(f.read())

    counts = {tier: 0 for tier, _ in COVERAGE_TIERS}
    human_gap = []
    for name, tiers in rows:
        for t in tiers:
            counts[t] += 1
        flagged = [t for t in tiers if t in ("Human", "Gap")]
        if flagged:
            human_gap.append((name, flagged))

    print(f"\n{'=' * 64}\n  COVERAGE SUMMARY (from invariant_coverage_matrix.md)\n{'=' * 64}")
    print(f"  Rows: {len(rows)}   "
          + "   ".join(f"{counts[t]} {t}" for t, _ in COVERAGE_TIERS))
    print(f"\n  Not machine-guaranteed ({len(human_gap)} row(s) - Human-gated or Gap):")
    if human_gap:
        for name, flagged in human_gap:
            print(f"    [{'/'.join(flagged)}] {name}")
    else:
        print("    (none)")
    print()
    return 0


def run_checks() -> int:
    results = []
    for name, cmd in CHECK_GROUPS:
        print(f"\n{'=' * 64}\n  >> {name}\n{'=' * 64}", flush=True)
        rc = subprocess.run(cmd, cwd=REPO_ROOT).returncode
        results.append((name, rc))

    print(f"\n{'=' * 64}\n  SUMMARY\n{'=' * 64}")
    failed = 0
    for name, rc in results:
        if rc != 0:
            failed += 1
        print(f"  [{'PASS' if rc == 0 else 'FAIL'}] {name}")

    if failed:
        print(f"\n  {failed} check group(s) FAILED — blocking.\n")
        return 1
    print("\n  All check groups passed.\n")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Robotiko validation backbone - one gate.")
    parser.add_argument("--coverage", action="store_true",
                        help="Print the coverage summary from the matrix and exit "
                             "(tier counts + Human/Gap rows by name).")
    args = parser.parse_args()
    if args.coverage:
        return coverage_summary()
    return run_checks()


if __name__ == "__main__":
    sys.exit(main())
