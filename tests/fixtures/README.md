# Validator Fixtures — Frozen Regression Pairs

These files are **frozen snapshots**, not live pipeline output. Do not "fix" them.

| File | State | Must |
|---|---|---|
| `ep09_visual_prompts_BROKEN.md` | The real EP09 v01 ref-integrity bug, frozen | **FAIL** ref-integrity |
| `ep09_visual_prompts_GOOD.md`   | The corrected counterpart | **PASS** every check |
| `doc_ref_BAD.md`  | A doc naming a nonexistent backtick repo path | **FAIL** `doc_reference_check.py` |
| `doc_ref_GOOD.md` | A clean doc (tolerated historical hook mention, `_private/` path, gitignored render output, inline-suppressed anti-example) | **PASS** `doc_reference_check.py` |
| `pdf_only_visuals/04_visuals/selected/ep01_visual_prompts_v01.pdf` | A PDF placed in a `selected/` SUBDIR, mirroring EP01's real layout | be **found** by `visual_prompt_validator.find_pdf_visuals` (a one-level `os.listdir` cannot see a PDF in a subfolder, so the skip branch never fires and the stage passes unexamined) |
| `musical_metadata_overlay_GOOD.json` | A section marked `"overlay": true` contained in its neighbor's span (the EP08 section[21] vocal-hum shape) | **PASS** `musical_metadata_validator.py` with zero findings |
| `musical_metadata_overlap_BAD.json` | The identical overlap WITHOUT the `overlay` flag | **FAIL** `musical_metadata_validator.py` (unmarked overlap = data error, graduated from WARN) |
| `ep07_style_eye_v2_BAD.md`  | Version-stamped (SKILL v2.0) file with the photoreal modifier but NO declared style mode, plus an eye-glow Text Prompt | **FAIL** both `check_style_mode` (ADR-0009) and `check_eye_glow` (ADR-0010) |
| `ep07_style_eye_v2_GOOD.md` | Same, but it declares its style mode (modifier sanctioned) and describes eyes with the material-lens idiom | **PASS** every check |
| `capcut_guide_BAD.md`  | The real EP09 v01 gap-propagation bug, frozen: Scene Dur values 1s short of their timestamp span, a genuine 1s timestamp gap (S01->S02), and a wrong Speed value (S04) | **FAIL** `capcut_guide_validator.py` (Scene Dur mismatch, timestamp gap, speed mismatch) |
| `capcut_guide_GOOD.md` | Contiguous timestamps, Scene Dur matching each span exactly, correct speed/trim values | **PASS** `capcut_guide_validator.py` with zero findings |
| `ep10_visual_prompts_PHASE1_GOOD.md` | A legitimate two-phase **Phase-1 deliverable** (ADR-0013): reference prompts authored, scene section intentionally pending behind the human ref-approval gate, declared by the scene-pending sentinel | **partial-PASS** `visual_prompt_validator.py` — print "PHASE 1 ONLY" and exit clean, never a false green |
| `ep10_visual_prompts_NOSCENES_BAD.md` | The refs-only **false green**: reference prompts present, ZERO scene prompts, and no sentinel declaring that state as designed | **FAIL** `visual_prompt_validator.py` on the phase-state check |
| `ep10_visual_prompts_LYINGSENTINEL_BAD.md` | Scenes ARE written but the Phase-1 sentinel was never removed — a stale sentinel contradicting the file's own content. Every other check on its single scene is clean | **FAIL** `visual_prompt_validator.py` on the phase-state check, and *only* there |
| `ep10_visual_prompts_BADSENTINEL_BAD.md` | Carries BOTH the Phase-1 sentinel AND a scaffold template marker ("auto-populated by Claude"), so an ordering bug could swallow a real Phase-1 deliverable into the silent scaffold-skip path. Its real defect: REF Q's Text Prompt is missing the mandatory style suffix | **FAIL** `visual_prompt_validator.py` on the missing suffix — proving the sentinel is checked before the scaffold skip and the file was not silently dropped |
| `ep10_visual_prompts_QUOTEDSENTINEL_GOOD.md` | A complete document (scenes present) that also QUOTES the sentinel token inside a fenced code block, e.g. a changelog note explaining the two-phase flow | **PASS** every check — the detector strips fenced code before looking for the sentinel, so a quoted token is not a live one |
| `forbidden_terms_BAD.md` | Prose that names a specific order directly instead of keeping the framing universal — a banned tradition NAME used as a label | **FAIL** `forbidden_terms_gate.py` |
| `forbidden_terms_GOOD.md` | The deliberate near miss: the same subject matter, written with the sanctioned geographic/universal framing and naming no order, sect, or scripture — proving the gate matches specific banned words, not topic proximity | **PASS** `forbidden_terms_gate.py` with zero findings |

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
