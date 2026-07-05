# Validator Fixtures — Frozen Regression Pairs

These files are **frozen snapshots**, not live pipeline output. Do not "fix" them.

| File | State | Must |
|---|---|---|
| `ep09_visual_prompts_BROKEN.md` | The real EP09 v01 ref-integrity bug, frozen | **FAIL** ref-integrity |
| `ep09_visual_prompts_GOOD.md`   | The corrected counterpart | **PASS** every check |
| `doc_ref_BAD.md`  | A doc naming a nonexistent backtick repo path | **FAIL** `doc_reference_check.py` |
| `doc_ref_GOOD.md` | A clean doc (tolerated historical hook mention, `_private/` path, gitignored render output, inline-suppressed anti-example) | **PASS** `doc_reference_check.py` |
| `pdf_only_visuals/04_visuals/selected/ep01_visual_prompts_v01.pdf` | A PDF placed in a `selected/` SUBDIR, mirroring EP01's real layout | be **found** by `visual_prompt_validator.find_pdf_visuals` (the M4 regression: the old one-level `os.listdir` never saw it) |
| `musical_metadata_overlay_GOOD.json` | A section marked `"overlay": true` contained in its neighbor's span (the EP08 section[21] vocal-hum shape) | **PASS** `musical_metadata_validator.py` with zero findings |
| `musical_metadata_overlap_BAD.json` | The identical overlap WITHOUT the `overlay` flag | **FAIL** `musical_metadata_validator.py` (unmarked overlap = data error, graduated from WARN) |

## Why they exist

The ref-integrity bug (EP09 attached Robotiko's **pristine** reference
`ref_robotiko_master.png` to a **damaged/kintsugi** body episode) passed every
text-based check green, because:

1. the text prompts say "chrome android", not "robotiko"; and
2. nothing ever parsed the `Image Reference Path` / `Upload` metadata fields.

`ep09_visual_prompts_BROKEN.md` freezes that exact failure so it can never come
back silently. `ep09_visual_prompts_GOOD.md` is the same scenes with the
phase-correct reference (`android_damaged.png`) and the tool-aware anti-spawn
phrasing ("single figure composition no additional characters").

The meta-tests in [`tests/test_validators.py`](../test_validators.py) grade the
graders: they assert the suite **fails** on BROKEN (and fails *only* on
ref-integrity — proving the other checks were the blind ones) and **passes** on
GOOD. If either direction ever flips, a grader has rotted.

Scenes kept minimal but faithful: S01/S02 = damaged range (S01-S26), S27a =
kintsugi range (S27+). Behavior is driven by `character_profiles.json`
(`phase_reference_map`) — the single source of truth — exactly as in production.
