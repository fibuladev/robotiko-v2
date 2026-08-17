# Tests
> **Status:** v2.0 — one-command gate; ref-integrity + grade-the-graders meta-tests.

---

## One command

```bash
python tests/run_all.py        # runs every check; exits non-zero if any fails
python tests/run_all.py --coverage   # print the coverage summary and exit (no checks run)
```

This is the single gate. CI runs the identical entrypoint and blocks the merge on
failure. Code is standard-library only — no `pip install`. `run_all.py` executes
12 check groups: naming convention, pipeline integrity, visual prompt sweep, prompt
hygiene, musical metadata, motion script, CapCut guide, character profiles, validator
meta-tests, doc reference integrity, energy-motion sync (advisory tier —
its warnings are printed but never block), and the forbidden-terms gate.

`--coverage` reads `_management/invariant_coverage_matrix.md` and prints a per-tier
count (Machine / Heuristic / Human / Gap) plus every Human- and Gap-tier row by name,
so one command answers both "did it pass" and "what do we NOT guarantee".

---

## Available Tests

| Script | Purpose | Status |
|---|---|---|
| `run_all.py` | One command — runs all checks below, exits non-zero on any failure | v2.0 |
| `universe_config.py` | **Single source** for universe-specific gate constants (mandatory suffixes, forbidden aesthetics, anti-spawn guard); the validators import from here | v1.0 |
| `naming_check.py` | Validates file names against `naming_convention.md` | Implemented |
| `pipeline_integrity.py` | Waiver-aware skipped-step detection + disk-vs-declared state machine + approval-gate ledger enforcement | v2.0 |
| `visual_prompt_validator.py` | Visual prompt content: suffix · forbidden aesthetics · character phase · **reference integrity** · **eye-glow** (model-facing) · **style-suffix variant** | v2.1 |
| `prompt_hygiene_lint.py` | **Scoped** — model-facing prompt strings (Text/Motion blocks only) must be plain-English ASCII; never reads canon/direction notes | v1.0 |
| `musical_metadata_validator.py` | Validates `musical_metadata.json` structure and vocabulary compliance: required fields, energy/section-type vocabulary, timestamp monotonicity (unmarked overlap = FAIL), **overlay convention** (`"overlay": true` + containment), `total_duration` match | v1.1 |
| `motion_script_validator.py` | Validates motion scripts: mandatory video suffix, anti-spawn guard, camera diversity (global quotas + **5-clip local window** + **accent budget** + **one-move-per-clip** + personality WARN) | v1.1 |
| `energy_motion_check.py` | **Advisory tier** — cross-checks each clip's Motion Strength against the SKILL energy band of its musical section; `[DISSONANCE]` exempt, ramps widened, pre-SKILL-v2 skipped; warnings never block | v1.0 |
| `character_profiles_validator.py` | Structural check of `character_profiles.json` against `schema.json` + **eye-glow guard** on model-facing prompt fields (ADR-0010) | v1.1 |
| `test_validators.py` | Meta-tests — grade the graders (fixtures + both-directions proofs) | v1.0 |
| `doc_reference_check.py` | **Doc-reality drift lint** — curated docs' backtick repo paths must exist on disk; no hook-rot; coverage-matrix ↔ `check_` sync | v1.0 |
| `forbidden_terms_gate.py` | **Forbidden-terms gate** — public prose (canon docs, direction notes, musical metadata JSON) never names a banned religion/order/sect/scripture term (case-insensitive, diacritic-insensitive, word-ish boundary); a narrow, pinned allowlist covers the one sanctioned mention | v1.0 |
| `fixtures/` | Frozen BROKEN/GOOD + doc-ref BAD/GOOD + musical overlay GOOD/BAD + forbidden-terms BAD/GOOD regression pairs (see `fixtures/README.md`) | — |

---

## Universe configuration

The universe-specific strings the gate enforces — the mandatory **visual** and **video**
suffixes, the **forbidden aesthetics** list, and the **anti-spawn guard** — live in one
place: [`universe_config.py`](universe_config.py). The visual and motion validators
import from it, and the meta-tests derive their expectations from it too, so changing a
value there re-points the gate instead of fighting it.

Forking for your own universe? Change your constants **there and only there** (and mirror
the suffixes in `CLAUDE.md`, which is what the skills read when they generate prompts —
see CONTRIBUTING §3 step 4). Generation-physics rules (the eye-glow keyword lists) and the
"declare your variant in the header" mechanism deliberately stay with their checks — they
are not universe styling. A meta-test (`TestUniverseConfigIsLive`) proves the override is
live in both directions.

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
- **Eye-glow (model-facing)** — a glow keyword within 3 tokens of an eye/lens word in
  a Text Prompt blockquote (ADR-0010). Kintsugi body gold-glow is allowlisted; "light"
  (lens projection) is not a glow keyword. FAIL for version-stamped files, WARN for
  shipped unstamped ones (measured legacy debt; canon appearance is never read)
- **Style-suffix variant** — the base suffix stays mandatory (`check_suffix`); the
  EP07+ photoreal modifier is allowed only when the file declares a `## STYLE MODE`
  header (ADR-0009), else WARN (legacy) / FAIL (version-stamped)
- **PDF-only skip is visible** — `--full` searches the whole `04_visuals` subtree
  (including `selected/` and `raw/`), so a pre-method PDF-only visuals stage prints a
  clear skip line instead of being silently dropped (the M4 fix — the old one-level
  `os.listdir` never saw a subdir PDF). EP01's own pre-pipeline visuals PDF is now
  personal working material, kept private; its stage is waived
  in `_management/approvals.json` and named in the pipeline-integrity summary, and the
  detector is proven by the synthetic fixture `fixtures/pdf_only_visuals/`

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
  `_management/approvals.json`. episode-01's waived visual-prompts stage is the one legacy
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
- Timestamp monotonicity (ordered start/end) — an **unmarked overlap is a FAIL**
  now that intentional layering has a sanctioned expression
- **Overlay convention** — a section marked `"overlay": true` (a deliberate layer,
  e.g. EP08's vocal hum riding over the boardroom verse) is exempt from
  monotonicity, but must genuinely intersect the preceding section's span
  (containment check); a floating overlay is a data error wearing a flag
- `total_duration` matches the last section's end (±1s tolerance)

### motion_script_validator.py
- Mandatory video suffix present on every motion prompt
- Anti-spawn guard present on every motion prompt
- Global camera diversity quotas (no single move type >30%, Static >=15%)
- **Local diversity window** — every 5 consecutive clips must use >=3 distinct
  moves (catches A-B-A-B monotony the global quota is blind to)
- **Accent-move budget** — Orbital / Handheld / Crane Up / Crane Down max 3 uses
  each per episode (SKILL soft zone is 2-3; >3 is the finding)
- **One camera move per clip** — a Camera Move value naming 2+ vocabulary moves
  is a combined move (conflicting model instructions)
- **Episode camera personality** (EP07-09) — declared dominant move must be among
  the top-3 most-used; always WARN (artistic judgement)
- Severity: SKILL-v2+ scripts FAIL on machine rules; pre-v2 scripts WARN-only

### energy_motion_check.py (advisory tier)
- For each clip with a parseable timestamp, finds its musical section (by
  midpoint) in the episode's `musical_metadata.json` and verifies the clip's
  Motion Strength falls in the SKILL's energy band
- Exemptions: `[DISSONANCE]`-tagged shots (the tag's purpose), ramp/transition
  energies (band widened ±1), pre-SKILL-v2 episodes (skipped)
- A ±1 soft tolerance is applied by default (`--strict` disables it for audits)
- WARN everywhere — heuristic, art-adjacent territory; warnings never block

### character_profiles_validator.py
- Lightweight stdlib-only structural check of `character_profiles.json` against
  `character_profiles.schema.json` (full JSON Schema draft-2020-12 validation is
  deferred per the stdlib-only constraint)
- **Eye-glow guard** on model-facing prompt fields (`base_visual_prompt`,
  `visual_prompt_addition`) — reuses the visual validator's detector; the JSON is a
  live production input, so a glow-near-eyes leak here is FAIL (ADR-0010)

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

### forbidden_terms_gate.py
- **Scope.** Tracked files only (`git ls-files`, so gitignored/untracked paths never
  enter): every top-level `*.md` (repo root, not recursive), `_management/` /
  `docs/` / `_memory/` / `_skills/` / `_templates/` / `_assets/` / `.github/`
  (every `*.md`, recursive — includes `_management/adr/`),
  `episode-*/03_direction/*.md`, and `episode-*/02_music/*_musical_metadata.json`
  (scanned as text — a forbidden term in a JSON string value appears verbatim on
  some line). Excludes `tests/fixtures/**` (intentional bad content) and
  `episode-*/01_lyrics/**` (lyric sheets are untouchable shipped artifacts).
- **Matching.** Case-insensitive, diacritic-insensitive (NFKD-normalized, so
  `Halvetî` / `dergâh` / `etvârnâme` match their plain-ASCII root), word-ish
  boundary — no partial hit inside a longer unrelated word (`sufficient` never
  trips `sufi`).
- **Terms banned.** Religion/order/sect/scripture NAMES only (`sufi`, `halveti`,
  `etvarname`, `tarikat`, `dergah`, `naqshbandi`, `bektashi`, `mevlevi`, `sunni`,
  `alevi`, `islamic`, `quran`/`koran`, `eschatology`/`eschatological`, `vedanta`,
  `atman`, `brahman`, `sunyata`). Broad adjectives (`sacred`, `divine`, `mystical`,
  `dervish`, `zen`) stay OUT by design — sanctioned in-fiction/satire uses remain
  human-judged.
- **Allowlist.** A narrow, pinned, in-file `file -> exact substring` mapping — a
  hit is exempted only if its own line contains the pinned substring verbatim.
  Seeded with one entry: the `_memory/lessons.md` rule line that names "Sufi" as
  the rule's own object (the ban's documentation), not a used tradition label.
- Catches the class of bug two real audit findings were: a named-tradition block in
  `_management/master.md` and a `"Sufi"` mention inside
  `episode-08/02_music/ep08_musical_metadata.json`'s prose.

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