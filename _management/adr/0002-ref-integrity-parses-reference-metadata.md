# ADR 0002 — Ref-integrity parses the reference metadata fields

- **Status:** Accepted (2026-06-26)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Validation Backbone

## Context

The original visual-prompt validator only read prose: it searched the text
prompt for the word "robotiko" and for forbidden style terms. The EP09 bug was
invisible to it for two compounding reasons:

1. **Identifier blindness** — the prompts call the subject "the chrome android",
   not "robotiko", so the character check never engaged.
2. **Field blindness** — the wrong reference lived in the `Image Reference Path`
   and `Upload` metadata fields, which nothing ever parsed.

A text-only check is fundamentally the wrong instrument for a reference-image
rule: the prompt names the subject, but the *uploaded reference* carries the
visual truth.

## Decision

Add a `check_ref_integrity` validator that:

- parses each scene block's `Characters Present`, `Image Reference Path` and
  `Upload` fields (`extract_scenes`);
- for every scene where Robotiko is present, looks up the expected reference via
  the phase→reference map ([ADR 0001](0001-phase-reference-map-source-of-truth.md));
- fails when a forbidden reference file appears and no allowed one is present
  (the `has_allowed` guard handles dual-reference scenes like EP08 S22, where a
  damaged original and pristine dream-copies legitimately coexist).

Identifier detection was widened to `["robotiko", "chrome android"]`, and the
parser accepts both `#### Scene S11` and `#### S11` header forms.

## Consequences

- The reliable gate is now **metadata-based**, not prose-based. Ref-integrity is
  treated as the authoritative character-state check; the text keyword check
  ([ADR 0004](0004-triage-policy-and-check-refinements.md)) is a secondary
  heuristic.
- A scene parser that silently matches zero blocks would report PASS over an
  unchecked file — a false green. This is guarded by a coverage meta-test
  ([ADR 0003](0003-frozen-fixtures-and-meta-tests.md)).
- The check is only as correct as the source-of-truth map; the two evolve
  together.
