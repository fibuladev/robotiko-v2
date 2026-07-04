# ADR 0001 — Phase→reference map is the single source of truth

- **Status:** Accepted (2026-06-26)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Validation Backbone

## Context

Which reference image belongs in which shot lived only in a human's head:
Robotiko has three body phases (pristine / damaged / kintsugi), each needing a
different reference image, with episode-level exceptions (EP08's body stays
@Damaged at Phase 3; EP09 transitions mid-episode at S27). Nothing encoded this,
so EP09's visual prompts attached the **pristine** reference to a damaged-body
episode and no check could object — the rule it broke wasn't written down.

## Decision

Encode the rule as data in `_assets/cast/character_profiles.json` under
`robotiko.phase_reference_map`:

- `default_by_phase` maps phase 1/2/3 → a named reference (`pristine` / `damaged`
  / `kintsugi`), each defined in `reference_images` with its file path(s).
- `episode_overrides` carries the exceptions: a flat `ref` (EP08) or
  `scene_ranges` for intra-episode transitions (EP09: damaged S01–S26, kintsugi
  S27+).
- A JSON Schema (`character_profiles.schema.json`) constrains the shape. Schema is
  structurally validated by CI (`character_profiles_validator.py`); full JSON Schema
  draft-2020-12 validation is deferred per the stdlib-only constraint.

Phase 3 (`kintsugi`) has no dedicated reference file yet; it explicitly allows
the `damaged` reference as its base plus text/chain refs.

## Consequences

- The reference rule is now machine-readable and one edit away from changing
  behavior everywhere (validator + future tooling read the same map).
- The validator can mechanically derive the expected reference per scene
  (see [ADR 0002](0002-ref-integrity-parses-reference-metadata.md)).
- New episodes add an override entry instead of re-teaching the rule.
- Risk: the map can drift from production reality. Mitigated by the ref-integrity
  check running in CI on every visual-prompt file.
