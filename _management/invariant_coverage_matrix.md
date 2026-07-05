# Invariant Coverage Matrix

> What the machine guarantees, what a heuristic only *suggests*, and what still
> rests on a human eye. The point of this table is honesty: a green CI run does
> **not** mean every Golden Rule is enforced. Read the Coverage column before you
> trust a check.

**Legend**
- 🟢 **Machine** — mechanically checked; CI blocks on failure.
- 🟡 **Heuristic** — partially checked; can over/under-fire by nature, treat as an
  advisory signal, not a guarantee.
- 🔵 **Human** — gated by a person at a checkpoint; no automation claimed.
- ⚪ **Gap** — an invariant we care about with **no** automated check yet.

_Last updated: 2026-07-05 (canon/style bundle — eye-glow lint closes the last original Gap (ADR-0010), style-suffix variant family (ADR-0009), Final-mix AV sync declared as Human)._

## Pipeline / content invariants

| Invariant | Coverage | Mechanism | Honest notes |
|---|---|---|---|
| Phase-correct **reference image** per scene | 🟢 Machine | `check_ref_integrity` + `phase_reference_map` ([ADR 0001](adr/0001-phase-reference-map-source-of-truth.md), [0002](adr/0002-ref-integrity-parses-reference-metadata.md)) | The reliable gate. Metadata-based, not prose. Only as correct as the source-of-truth map. |
| **Reference-first** — the reference exists before its scenes | 🟢 Machine | `check_reference_first` ([ADR 0007](adr/0007-reference-first-or-pay-the-reshoot-tax.md)) | Fails when an episode has scenes in a phase whose dedicated reference is null / missing on disk. The EP09 kintsugi root-cause guard. |
| Mandatory **visual suffix** on every prompt (variant family) | 🟢 Machine | `check_suffix` (base) + `check_style_mode` (photoreal variant, [ADR 0009](adr/0009-style-suffix-v2.md)) | Base suffix is an exact substring, required always. The EP07+ photoreal modifier ("Photorealistic, not a painting") is a sanctioned variant, allowed only when the file declares a `## STYLE MODE` header; an undeclared modifier is WARN (legacy) / FAIL (version-stamped). Daylight "volumetric fog" is a documented cargo-token, not a new variant. |
| **Forbidden aesthetics** (Pixar, unreal engine, …) | 🟢 Machine | `check_forbidden_aesthetics` | Fixed term list; extend as new offenders appear. |
| **File naming** convention | 🟢 Machine | `naming_check.py --full` | 85 checks. |
| No silently **skipped pipeline steps** | 🟢 Machine | `pipeline_integrity.py --full` | Now waiver-aware and honest: a non-sequential skip (empty step N, present step N+1) FAILs unless a waiver record exists in `_management/approvals.json`. The summary names the one legacy waivered skip (episode-01, PDF-only visuals) instead of the old false "no skipped steps". |
| **Disk vs declared** state machine | 🟢 Machine | `pipeline_integrity.py --full` (disk_declared_conflicts) vs `project_metadata.json` ([ADR 0008](adr/0008-approval-gates-as-data.md)) | Each episode's stage is read from disk and compared to the declared production flags. Disk AHEAD of the record (a step done on disk that metadata declares falsy) = FAIL. Declared-ahead is tolerated by design — render outputs are gitignored and in-progress work has no committed file yet. |
| **Approval gates as data** (two human checkpoints) | 🟢 Machine (linkage) + 🔵 Human (the judgement) | `_management/approvals.json` consumed by `pipeline_integrity.py` ([ADR 0008](adr/0008-approval-gates-as-data.md)) | Artifacts past a gate with no ledger record = FAIL; a ledger sha256 that no longer matches disk = WARN (stale approval — a legitimate post-approval edit, made visible). The machine verifies THAT a human approved a named artifact on a date; it cannot verify the taste behind the approval — that stays 🔵 Human. |
| Scene parser actually **parses** the file | 🟢 Machine | `TestParserCoverage` meta-tests | Guards the zero-scene false-green that started TAKE 05. |
| The **checkers themselves** are correct | 🟢 Machine | `test_validators.py` (fixtures + both-directions proofs, [ADR 0003](adr/0003-frozen-fixtures-and-meta-tests.md)) | Grade-the-graders. |
| **Docs match disk reality** (no doc-rot) | 🟢 Machine | `doc_reference_check.py` | Curated load-bearing docs: every backtick-quoted repo path must exist; a hook-rot guard forbids re-describing the removed naming hook as live; and a matrix↔`check_` sync fails a new enforcement check that ships without a row here. Skips URLs, placeholders, `_private/`, and gitignored render outputs. |
| Robotiko **body-state keywords** match phase | 🟡 Heuristic | `check_character_phase` + subject-guard + scene-pinned whitelist ([ADR 0004](adr/0004-triage-policy-and-check-refinements.md)) | Free-text; cannot fully attribute an adjective to a subject. Backed up by the 🟢 reference check. |
| **Prompt strings are plain-English ASCII** (model-facing only) | 🟢 Machine | `prompt_hygiene_lint.py` ([ADR 0006](adr/0006-scoped-prompt-hygiene.md)) | Scoped to Text/Motion prompt blockquotes; non-ASCII + tradition-label decoration. |
| **Cultural attribution** scoping (canon vs prompt) | 🟢 Machine (prompt) + 🔵 Human (canon) | `prompt_hygiene_lint.py` for prompts; canon is human-authored | Was ⚪ Gap. The lint enforces ASCII/no-label in prompt strings and deliberately never reads master.md or direction notes — canon keeps its sanctioned Turkish. |
| **Musical metadata** structure + vocabulary | 🟢 Machine | `musical_metadata_validator.py` | Required fields, energy/type vocabulary, timestamp monotonicity, total_duration match. An UNMARKED overlap is now a FAIL — intentional layering must carry `"overlay": true` (see next row). |
| **Overlay convention** — sanctioned section layering | 🟢 Machine | `check_overlay_containment` in `musical_metadata_validator.py` | A section marked `"overlay": true` (EP08's vocal hum over the boardroom verse) is exempt from monotonicity but MUST genuinely intersect the preceding section's span — an overlay that overlaps nothing is a data error wearing a flag. Fixture pair proves both directions. |
| **Anti-spawn guard** on motion prompts | 🟢 Machine | `motion_script_validator.py` | Checks standard guard + recognized alternatives ("No third figure", "Exactly two instances"). Pre-SKILL-v2 episodes are WARN-only. |
| Mandatory **video suffix** on motion prompts | 🟢 Machine | `motion_script_validator.py` | Exact-substring match. Pre-SKILL-v2 episodes are WARN-only. |
| **Camera diversity** — global quotas | 🟢 Machine | `motion_script_validator.py` | No single move >30%, Static >=15%. Pre-SKILL-v2 episodes are WARN-only (EP06's 42% zoom-in is a known shipped issue). |
| **Camera diversity** — local 5-clip window | 🟢 Machine | `check_local_diversity` in `motion_script_validator.py` | Every 5 consecutive clips must use >=3 distinct moves — catches the A-B-A-B monotony the global quota is blind to. SKILL-v2 episodes FAIL; pre-v2 WARN (measured legacy debt: EP02=4, EP03=1, EP04=3, EP05=8, EP06=6 windows; EP07-09 clean). |
| **Accent-move budget** (Orbital/Handheld/Crane) | 🟢 Machine | `check_accent_budget` in `motion_script_validator.py` | SKILL says "max 2-3 uses per episode": 2-3 is the soft zone, >3 is the finding. Pre-v2 WARN (EP03's Handheld x5 is known legacy). v2+ FAIL. |
| **One camera move per clip** | 🟢 Machine | `check_single_move` in `motion_script_validator.py` | A Camera Move value naming 2+ vocabulary moves is a combined move (conflicting model instructions). Was a docstring claim with no check behind it — now real. Pre-v2 WARN (EP01 has 4 combined values). |
| **Episode camera personality** honored (EP07-09) | 🟡 Heuristic | `check_camera_personality` in `motion_script_validator.py` | The declared dominant move (EP07 Dolly Out, EP08 Static, EP09 Slow Zoom Out) must be among the top-3 most-used moves. Always WARN — whether the camera "feels like" its personality is artistic judgement, not arithmetic. EP10 has no single declared move; skipped. |
| **Energy -> Motion Strength** mapping | 🟡 Heuristic | `check_energy_motion` in `energy_motion_check.py` (run_all group 10, advisory) | Each clip's MS graded against the SKILL band of its musical section (timestamp midpoint). `[DISSONANCE]` shots exempt (the tag's purpose); ramp energies widened +-1; +-1 soft tolerance by default (`--strict` for audits); pre-v2 episodes skipped. WARN everywhere — never blocks. Current advisory debt: EP07=8, EP08=11 deviations, EP09=0. |
| **Eye rule** — no glow keyword for eyes (model-facing) | 🟢 Machine | `check_eye_glow` (Text Prompt blockquotes) + `scan_eye_glow` (`character_profiles.json` prompt fields), [ADR 0010](adr/0010-eye-canon-reconciliation.md) | Was ⚪ Gap — the last of the three original gaps to close. A glow keyword within 3 tokens of an eye/lens word in a MODEL-FACING string. Kintsugi body gold-glow allowlisted; canon appearance (master.md) is never read (two-layer doctrine). FAIL for the live JSON + version-stamped files; WARN for shipped unstamped visual prompts (EP09 S31 "self-luminous" is the one known legacy WARN, not retrofitted). |
| **Final-mix AV sync** (audio/video alignment) | 🔵 Human | Human sync-QC pass at pipeline_rules Step 11, recorded per episode (`_templates/ep_sync_qc_template.md`) | Declared limit: CI cannot see or hear the final mix, so it cannot certify lip/beat/cut alignment. Gated by a person at Step 11; the record is the evidence, not a green run. |
| EP01 visual prompts | 🔵 Human (visibly skipped) | `visual_prompt_validator.py --full` prints the skip | EP01 visuals are a PDF (`episode-01/04_visuals/selected/ep01_visual_prompts_v01.pdf`) — pre-method episode, not machine-parseable. The M4 fix makes the skip **visible**: the detector now searches the whole `04_visuals` subtree (was a one-level `os.listdir` that never saw the `selected/` PDF, so EP01 was silently dropped). The pipeline skip is waivered in `_management/approvals.json`. |

## Golden Rules (narrative / philosophical)

| Golden Rule | Coverage | Notes |
|---|---|---|
| #1 Glitch is Scripture | 🔵 Human | Aesthetic judgement; not automatable. |
| #2 Master First | 🔵 Human | Process discipline. |
| #3 Character State | 🟢 Machine (ref) + 🟡 Heuristic (text) | The one Golden Rule now substantially machine-enforced. |
| #4 The Suffix | 🟢 Machine | `check_suffix`. |
| #5 No Revenge / #6 No Cheap Emotion / #7 No Drama / #8 The 8 Turns | 🔵 Human | Dramaturgy + motion-script checkpoints. |
| #9 Cultural Attribution | 🟢 Machine (prompt strings) + 🔵 Human (canon) | The scoped lint keeps attribution out of model-facing prompts while the canon keeps it. See pipeline table. |

## Human checkpoints (gated by design, not gaps)

| Checkpoint | When |
|---|---|
| Dramaturgy approval | After dramaturgy, before visual prompts |
| Motion-script approval | After motion script, before video generation |

## Reading guidance

- A green `tests/run_all.py` certifies the 🟢 rows and that the 🟡 row didn't
  trip on the current files — nothing more.
- The ⚪ gaps are the honest backlog; each is a candidate for a future check with
  its own fixture and both-directions proof before it's trusted.
