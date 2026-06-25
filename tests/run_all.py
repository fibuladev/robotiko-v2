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
  5. Validator meta-tests   — grade the graders (fixtures + both-directions proofs)

Dependencies: standard library only. No `pip install`, nothing to pin at the
package level — the strongest form of dependency hygiene. The toolchain (Python
version + CI actions) is pinned in .github/workflows/validation_suite.yml.
"""

import os
import sys
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHECK_GROUPS = [
    ("Naming convention",    [sys.executable, "tests/naming_check.py", "--full"]),
    ("Pipeline integrity",   [sys.executable, "tests/pipeline_integrity.py", "--full"]),
    ("Visual prompt sweep",  [sys.executable, "tests/visual_prompt_validator.py", "--full"]),
    ("Prompt hygiene",       [sys.executable, "tests/prompt_hygiene_lint.py", "--full"]),
    ("Validator meta-tests", [sys.executable, "-m", "unittest", "tests.test_validators"]),
]


def main() -> int:
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


if __name__ == "__main__":
    sys.exit(main())
