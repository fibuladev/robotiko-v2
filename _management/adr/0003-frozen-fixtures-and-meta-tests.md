# ADR 0003 — Frozen fixtures + meta-tests (grade the graders)

- **Status:** Accepted (2026-06-26)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Validation Backbone

## Context

A checker with no proof it works is just a more confident way to be wrong. Once
the ref-integrity check existed, nothing stopped a future edit from quietly
breaking it — loosening a regex, mis-scoping a guard — and leaving us with a
green that means "nothing was checked."

## Decision

Freeze the bug as a permanent regression pair and test the checkers themselves:

- `tests/fixtures/ep09_visual_prompts_BROKEN.md` — the real EP09 bug, frozen.
  Must FAIL ref-integrity.
- `tests/fixtures/ep09_visual_prompts_GOOD.md` — the corrected counterpart.
  Must PASS every check.
- `tests/test_validators.py` — meta-tests (stdlib `unittest`, no new dependency)
  that assert the suite fails on BROKEN and passes on GOOD; that BROKEN fails
  **only** on ref-integrity (pinning *why* the bug shipped green — the text
  checks are blind to it); and that grade each check in isolation: it must fire
  when it should and stay silent when it shouldn't.

Two structural guards travel with this: every fixture must parse a non-zero
number of prompts/scenes (green can't mean "nothing checked"), and every
loosening of a check must ship with a both-directions proof
([ADR 0004](0004-triage-policy-and-check-refinements.md)).

## Consequences

- The reference bug is now a permanent, self-verifying regression.
- The graders are themselves graded; a rotted check trips a meta-test.
- Fixtures are immutable snapshots — they are not "fixed" when production files
  change. New classes of bug get new fixtures.
