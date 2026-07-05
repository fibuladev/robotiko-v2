"""
Robotiko v2.0 - Attempts-ledger reporter (STANDALONE - not part of run_all.py).

The "80-90% first-pass" figure for image generation has always been experiential -
a number from the director's production notes, never instrumented. The attempts
ledger (`episode-{XX}/04_visuals/raw/attempts.md`, schema in
`_management/pipeline_rules.md`) is where that number finally gets measured, one
generated scene at a time, DURING production. EP10 is the first episode with a
mandatory ledger.

This reporter scans every `episode-*/04_visuals/raw/attempts.md`, and:
  * if none exist yet, says so honestly and exits 0 (the ledgers are a future
    convention, not a backfill obligation);
  * if present, prints per-episode first-pass percentage plus a failure-reason
    histogram.

It is deliberately NOT wired into `tests/run_all.py`: absence of ledgers is not a
failure, and telemetry reporting is not a gate. It defines no `check_` functions on
purpose, so the coverage-matrix lint has nothing to demand of it.

Dependencies: standard library only.

Usage:
    python tests/attempts_report.py
    python tests/attempts_report.py --demo     # render from an inline sample
"""

import argparse
import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEMO_LEDGER = """\
# EP10 Attempts Ledger (DEMO)

| scene_id | attempts | first_pass (y/n) | fail_reason (one phrase) |
|---|---|---|---|
| s01 | 1 | y | - |
| s02 | 1 | y | - |
| s03 | 3 | n | extra characters spawned |
| s04 | 1 | y | - |
| s05 | 2 | n | wrong body phase |
| s06 | 1 | y | - |
| s07 | 4 | n | extra characters spawned |
| s08 | 1 | y | - |
"""


def parse_ledger(text):
    """Parse a ledger's markdown table -> list of row dicts.

    A data row has 4 pipe-delimited cells and a scene_id that looks like sNN.
    Header and separator rows are skipped."""
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        scene_id = cells[0]
        if not re.match(r"(?i)^s\d{1,3}[a-d]?$", scene_id):
            continue  # skips header ("scene_id") and separator ("---") rows
        attempts_raw = cells[1]
        try:
            attempts = int(attempts_raw)
        except ValueError:
            attempts = None
        first_pass = cells[2].strip().lower().startswith("y")
        reason = cells[3].strip()
        rows.append({
            "scene_id": scene_id,
            "attempts": attempts,
            "first_pass": first_pass,
            "fail_reason": reason,
        })
    return rows


def find_ledgers(repo_root):
    """Return sorted list of (episode_label, path) for every attempts.md found."""
    pattern = os.path.join(repo_root, "episode-*", "04_visuals", "raw", "attempts.md")
    found = []
    for path in sorted(glob.glob(pattern)):
        rel = os.path.relpath(path, repo_root).replace("\\", "/")
        ep = rel.split("/")[0]  # episode-XX
        found.append((ep, path))
    return found


def summarize(rows):
    """Compute first-pass stats + failure histogram from parsed rows."""
    total = len(rows)
    first = sum(1 for r in rows if r["first_pass"])
    hist = {}
    for r in rows:
        if not r["first_pass"]:
            key = r["fail_reason"] or "(unspecified)"
            hist[key] = hist.get(key, 0) + 1
    attempts_vals = [r["attempts"] for r in rows if r["attempts"] is not None]
    avg_attempts = (sum(attempts_vals) / len(attempts_vals)) if attempts_vals else None
    return {
        "total": total,
        "first_pass": first,
        "first_pass_pct": (100.0 * first / total) if total else 0.0,
        "avg_attempts": avg_attempts,
        "histogram": hist,
    }


def render_episode(label, rows):
    s = summarize(rows)
    print(f"\n## {label}")
    if not rows:
        print("  (ledger present but no data rows)")
        return s
    avg = f"{s['avg_attempts']:.2f}" if s["avg_attempts"] is not None else "n/a"
    print(f"  Scenes logged     : {s['total']}")
    print(f"  First-pass keepers: {s['first_pass']}/{s['total']} "
          f"({s['first_pass_pct']:.1f}%)")
    print(f"  Avg attempts/scene: {avg}")
    if s["histogram"]:
        print("  Failure reasons:")
        for reason, count in sorted(s["histogram"].items(),
                                    key=lambda kv: (-kv[1], kv[0])):
            print(f"    {count:>3}x  {reason}")
    else:
        print("  Failure reasons: none - every scene landed first-pass.")
    return s


def run_report(ledgers):
    print("Robotiko v2.0 - Attempts-Ledger Report")
    print("=" * 46)
    grand_total = 0
    grand_first = 0
    for label, path in ledgers:
        with open(path, encoding="utf-8") as f:
            rows = parse_ledger(f.read())
        s = render_episode(label, rows)
        grand_total += s["total"]
        grand_first += s["first_pass"]
    print("\n" + "=" * 46)
    if grand_total:
        pct = 100.0 * grand_first / grand_total
        print(f"  ALL EPISODES: {grand_first}/{grand_total} first-pass ({pct:.1f}%)")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Report first-pass yield from attempts ledgers "
                    "(standalone, not part of run_all.py).")
    parser.add_argument("--demo", action="store_true",
                        help="Render the report from an inline sample ledger.")
    args = parser.parse_args()

    if args.demo:
        print("(demo mode - inline sample, not disk data)\n")
        rows = parse_ledger(DEMO_LEDGER)
        print("Robotiko v2.0 - Attempts-Ledger Report")
        print("=" * 46)
        render_episode("episode-10 (DEMO)", rows)
        print("\n" + "=" * 46)
        s = summarize(rows)
        print(f"  ALL EPISODES: {s['first_pass']}/{s['total']} first-pass "
              f"({s['first_pass_pct']:.1f}%)\n")
        return 0

    ledgers = find_ledgers(REPO_ROOT)
    if not ledgers:
        print("No attempts ledgers found yet.")
        print("  Expected at: episode-*/04_visuals/raw/attempts.md")
        print("  First mandatory ledger: EP10 (schema in "
              "_management/pipeline_rules.md).")
        print("  Nothing to report - this is expected before EP10 production.")
        return 0

    run_report(ledgers)
    return 0


if __name__ == "__main__":
    sys.exit(main())
