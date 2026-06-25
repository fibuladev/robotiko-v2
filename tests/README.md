# Tests
> **Status:** v2.0 — one-command gate; ref-integrity + grade-the-graders meta-tests.

---

## One command

```bash
python tests/run_all.py        # runs every check; exits non-zero if any fails
```

This is the single gate. CI runs the identical entrypoint and blocks the merge on
failure. Code is standard-library only — no `pip install`.

---

## Available Tests

| Script | Purpose | Status |
|---|---|---|
| `run_all.py` | One command — runs all checks below, exits non-zero on any failure | v2.0 |
| `naming_check.py` | Validates file names against `naming_convention.md` | Implemented |
| `pipeline_integrity.py` | Ensures no pipeline steps were skipped | Implemented |
| `visual_prompt_validator.py` | Visual prompt content: suffix · forbidden aesthetics · character phase · **reference integrity** | v2.0 |
| `prompt_hygiene_lint.py` | **Scoped** — model-facing prompt strings (Text/Motion blocks only) must be plain-English ASCII; never reads canon/direction notes | v1.0 |
| `test_validators.py` | Meta-tests — grade the graders (fixtures + both-directions proofs) | v1.0 |
| `naming_check_hook.py` | Lightweight hook script for Claude Code PostToolUse | Implemented |
| `fixtures/` | Frozen BROKEN/GOOD regression pair (see `fixtures/README.md`) | — |

---

## Usage

```bash
# Validate naming convention for a specific episode
python tests/naming_check.py --episode 02

# Validate naming convention for all episodes
python tests/naming_check.py --full

# Validate visual prompt content for a specific episode
python tests/visual_prompt_validator.py --episode 02

# Validate visual prompt content for a specific file
python tests/visual_prompt_validator.py --file episode-02/04_visuals/ep02_visual_prompts_v01.md

# Check pipeline integrity for an episode
python tests/pipeline_integrity.py --episode 02
```

---

## Claude Code Hook Integration

The naming convention hook is configured in `.claude/settings.json` and runs automatically after every Write tool call. It checks if files written inside `episode-XX/` folders follow the naming convention.

**Note:** The hook uses pure bash (no Python dependency) for maximum compatibility.

---

## What Each Validator Checks

### naming_check.py
- File name matches one of 12 known patterns (lyrics, metadata, dramaturgy, etc.)
- Episode number consistency (file ep02_* lives in episode-02/)
- Skips raw folders and non-episode directories

### visual_prompt_validator.py
- Every prompt contains the mandatory visual suffix
- No forbidden aesthetics (Pixar, clean Apple design, generic cyberpunk neon, etc.)
- Character phase consistency — per-episode (EP01 pristine; EP02–03 canon-damaged;
  Phase-3 markers forbidden pre-Phase-3), with a subject-guard (judge Robotiko, not
  the scenery) and a scene-pinned whitelist for intentional non-Robotiko subjects
- **Reference integrity** — every Robotiko scene uses the phase-correct reference
  image, derived from `character_profiles.json` `phase_reference_map` (the reliable,
  metadata-based gate)

### prompt_hygiene_lint.py (scoped)
- Reads ONLY the `Text Prompt` blocks in visual-prompt files and the `Motion
  Prompt` blocks in motion-script files — never master.md or the direction notes
- Flags non-ASCII characters and tradition-label decoration in those prompt
  strings (the canon keeps its sanctioned Turkish; only model-facing strings are
  policed — see [ADR 0006](../_management/adr/0006-scoped-prompt-hygiene.md))
- `--fix` ASCII-normalizes the prompt blocks in place, leaving everything else untouched

### pipeline_integrity.py
- Checks each pipeline step has its required output file
- Flags missing steps and mandatory checkpoints

### test_validators.py (meta-tests)
- The graders, graded: the suite must FAIL the frozen BROKEN fixture and PASS the
  GOOD one; every loosening is proven both directions (still catches a real bug,
  ignores the intended case); a parser-coverage guard kills the zero-scene false-green

See [`_management/invariant_coverage_matrix.md`](../_management/invariant_coverage_matrix.md)
for what is machine-checked vs. human-gated, and [`_management/adr/`](../_management/adr/)
for the decisions behind these checks.

---

## GitHub Actions Integration

Everything runs on every push and pull request through the single entrypoint, via
[`.github/workflows/validation_suite.yml`](../.github/workflows/validation_suite.yml):

```
python tests/run_all.py
```

A red fails the job and blocks the merge. Run it locally the same way before opening
a PR. The Python version and the CI actions (pinned to commit SHAs) are pinned in the
workflow; the code itself has no third-party dependencies.