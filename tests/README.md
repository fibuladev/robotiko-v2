# Tests
> **Status:** v2.0 — one-command gate; ref-integrity + grade-the-graders meta-tests.

---

## One command

```bash
python tests/run_all.py        # runs every check; exits non-zero if any fails
```

This is the single gate. CI runs the identical entrypoint and blocks the merge on
failure. Code is standard-library only — no `pip install`. `run_all.py` executes
9 check groups: naming convention, pipeline integrity, visual prompt sweep, prompt
hygiene, musical metadata, motion script, character profiles, validator
meta-tests, and doc reference integrity.

---

## Available Tests

| Script | Purpose | Status |
|---|---|---|
| `run_all.py` | One command — runs all checks below, exits non-zero on any failure | v2.0 |
| `naming_check.py` | Validates file names against `naming_convention.md` | Implemented |
| `pipeline_integrity.py` | Waiver-aware skipped-step detection + disk-vs-declared state machine + approval-gate ledger enforcement | v2.0 |
| `visual_prompt_validator.py` | Visual prompt content: suffix · forbidden aesthetics · character phase · **reference integrity** | v2.0 |
| `prompt_hygiene_lint.py` | **Scoped** — model-facing prompt strings (Text/Motion blocks only) must be plain-English ASCII; never reads canon/direction notes | v1.0 |
| `musical_metadata_validator.py` | Validates `musical_metadata.json` structure and vocabulary compliance: required fields, energy/section-type vocabulary, timestamp monotonicity, `total_duration` match | v1.0 |
| `motion_script_validator.py` | Validates motion scripts: mandatory video suffix, anti-spawn guard, camera diversity quotas, single camera move per clip | v1.0 |
| `character_profiles_validator.py` | Lightweight stdlib-only structural check of `character_profiles.json` against `schema.json` | v1.0 |
| `test_validators.py` | Meta-tests — grade the graders (fixtures + both-directions proofs) | v1.0 |
| `doc_reference_check.py` | **Doc-reality drift lint** — curated docs' backtick repo paths must exist on disk; no hook-rot; coverage-matrix ↔ `check_` sync | v1.0 |
| `fixtures/` | Frozen BROKEN/GOOD + doc-ref BAD/GOOD regression pairs (see `fixtures/README.md`) | — |

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

## Claude Code Hook (removed)

A Claude Code PostToolUse hook (`naming_check_hook.py` + a hook entry in
`.claude/settings.json`) once auto-checked naming on every Write. It was removed
2026-07-04 — it never reliably fired. The real gate is `tests/naming_check.py --full`,
run via `tests/run_all.py` and enforced in CI.

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
- **PDF-only skip is visible** — `--full` searches the whole `04_visuals` subtree
  (including `selected/` and `raw/`), so EP01's PDF-only, pre-method visuals now print
  a clear skip line instead of being silently dropped (the M4 fix — the old one-level
  `os.listdir` never saw the `selected/` PDF)

### prompt_hygiene_lint.py (scoped)
- Reads ONLY the `Text Prompt` blocks in visual-prompt files and the `Motion
  Prompt` blocks in motion-script files — never master.md or the direction notes
- Flags non-ASCII characters and tradition-label decoration in those prompt
  strings (the canon keeps its sanctioned Turkish; only model-facing strings are
  policed — see [ADR 0006](../_management/adr/0006-scoped-prompt-hygiene.md))
- `--fix` ASCII-normalizes the prompt blocks in place, leaving everything else untouched

### pipeline_integrity.py
- **Skipped steps (waiver-aware).** A non-sequential pattern (empty step N, present
  step N+1) is a skipped step — a FAIL unless a waiver record exists in
  `_management/approvals.json`. episode-01's PDF-only visuals stage is the one legacy
  waivered skip; the summary names it instead of the old false "no skipped steps"
- **Disk vs declared state machine.** Each episode's on-disk stage is compared against
  `project_metadata.json`'s production flags; disk ahead of the declared record = FAIL
  (declared-ahead is tolerated — render outputs are gitignored, in-progress work has no
  committed file yet)
- **Approval gates as data** ([ADR 0008](../_management/adr/0008-approval-gates-as-data.md)).
  Consumes `_management/approvals.json`: artifacts past a human gate with no ledger
  record = FAIL; a ledger sha256 that no longer matches disk = WARN (stale approval —
  a legitimate post-approval edit, made visible)

### musical_metadata_validator.py
- Required top-level and per-section fields present in `musical_metadata.json`
- Energy vocabulary and section-type vocabulary compliance (SKILL-defined levels only)
- Timestamp monotonicity (no overlaps, ordered start/end)
- `total_duration` matches the last section's end (±1s tolerance)

### motion_script_validator.py
- Mandatory video suffix present on every motion prompt
- Anti-spawn guard present on every motion prompt
- Camera diversity quotas (no single move type >30%, Static >=15%)
- Single camera move per clip

### character_profiles_validator.py
- Lightweight stdlib-only structural check of `character_profiles.json` against
  `character_profiles.schema.json` (full JSON Schema draft-2020-12 validation is
  deferred per the stdlib-only constraint)

### test_validators.py (meta-tests)
- The graders, graded: the suite must FAIL the frozen BROKEN fixture and PASS the
  GOOD one; every loosening is proven both directions (still catches a real bug,
  ignores the intended case); a parser-coverage guard kills the zero-scene false-green

### doc_reference_check.py
- **Doc-reference existence.** Scans a curated list of load-bearing docs
  (`architecture.md`, this README, the coverage matrix, `CONTRIBUTING.md`,
  `README.md`, and the four `docs/` guides) and fails if any backtick-quoted
  repo-relative path no longer exists on disk — the doc-rot the sweep just cleaned,
  now machine-caught forever
- **Scope discipline.** Only tokens that look like repo paths are checked; URLs,
  `{XX}`/glob/placeholder tokens, absolute and `~` paths, `_private/` (gitignored),
  and render outputs (`.mp4`/`.wav`/`raw/`/`selected/`, absent in git by design) are
  skipped. A line is tolerated by an inline `<!-- doc-ref: ignore -->` marker or the
  word "removed" (historical notes)
- **Hook-rot guard.** A present-tense claim about the removed naming hook (a line
  naming `naming_check_hook` or `PostToolUse` with no nearby removed/historical/was
  cue) fails, so the removed hook can never be re-described as live
- **Coverage-matrix sync.** Every `check_` function in `tests/*.py` must be
  represented in `invariant_coverage_matrix.md` or admitted as an internal helper in
  the script's `ALLOWLIST` — a new enforcement check can't ship without a ledger row

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