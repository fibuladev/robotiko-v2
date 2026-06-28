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

_Last updated: 2026-06-26 (EP09 Validation Backbone)._

## Pipeline / content invariants

| Invariant | Coverage | Mechanism | Honest notes |
|---|---|---|---|
| Phase-correct **reference image** per scene | 🟢 Machine | `check_ref_integrity` + `phase_reference_map` ([ADR 0001](adr/0001-phase-reference-map-source-of-truth.md), [0002](adr/0002-ref-integrity-parses-reference-metadata.md)) | The reliable gate. Metadata-based, not prose. Only as correct as the source-of-truth map. |
| **Reference-first** — the reference exists before its scenes | 🟢 Machine | `check_reference_first` ([ADR 0007](adr/0007-reference-first-or-pay-the-reshoot-tax.md)) | Fails when an episode has scenes in a phase whose dedicated reference is null / missing on disk. The EP09 kintsugi root-cause guard. |
| Mandatory **visual suffix** on every prompt | 🟢 Machine | `check_suffix` | Exact-substring; robust. |
| **Forbidden aesthetics** (Pixar, unreal engine, …) | 🟢 Machine | `check_forbidden_aesthetics` | Fixed term list; extend as new offenders appear. |
| **File naming** convention | 🟢 Machine | `naming_check.py --full` | 85 checks. |
| No silently **skipped pipeline steps** | 🟢 Machine | `pipeline_integrity.py --full` | |
| Scene parser actually **parses** the file | 🟢 Machine | `TestParserCoverage` meta-tests | Guards the zero-scene false-green that started TAKE 05. |
| The **checkers themselves** are correct | 🟢 Machine | `test_validators.py` (fixtures + both-directions proofs, [ADR 0003](adr/0003-frozen-fixtures-and-meta-tests.md)) | Grade-the-graders. |
| Robotiko **body-state keywords** match phase | 🟡 Heuristic | `check_character_phase` + subject-guard + scene-pinned whitelist ([ADR 0004](adr/0004-triage-policy-and-check-refinements.md)) | Free-text; cannot fully attribute an adjective to a subject. Backed up by the 🟢 reference check. |
| **Prompt strings are plain-English ASCII** (model-facing only) | 🟢 Machine | `prompt_hygiene_lint.py` ([ADR 0006](adr/0006-scoped-prompt-hygiene.md)) | Scoped to Text/Motion prompt blockquotes; non-ASCII + tradition-label decoration. |
| **Cultural attribution** scoping (canon vs prompt) | 🟢 Machine (prompt) + 🔵 Human (canon) | `prompt_hygiene_lint.py` for prompts; canon is human-authored | Was ⚪ Gap. The lint enforces ASCII/no-label in prompt strings and deliberately never reads master.md or direction notes — canon keeps its sanctioned Turkish. |
| **Anti-spawn guard** phrasing (tool-aware) | ⚪ Gap | — (skill rule only) | The visual-prompts SKILL mandates the phrasing; nothing validates its presence/shape yet. Candidate next check. |
| **Eye rule** — no glow keyword for eyes | ⚪ Gap | — (lesson + skill only) | "dark amber glass lenses…" formula is documented, not enforced. Candidate next check. |
| Mandatory **video suffix** on motion prompts | ⚪ Gap | — | No motion-script validator exists; suffix is human-checked. |

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
