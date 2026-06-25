# Architecture Decision Records

Short, durable records of the non-obvious engineering decisions behind the
pipeline's validation backbone — the "why", so the next contributor (or the next
us) inherits the reasoning instead of re-deriving it.

Format: Status · Context · Decision · Consequences. One decision per file.
ADRs are immutable once Accepted; to change a decision, add a new ADR that
supersedes the old one (don't rewrite history).

| ADR | Title | Status |
|---|---|---|
| [0001](0001-phase-reference-map-source-of-truth.md) | Phase→reference map is the single source of truth | Accepted |
| [0002](0002-ref-integrity-parses-reference-metadata.md) | Ref-integrity parses the reference metadata fields | Accepted |
| [0003](0003-frozen-fixtures-and-meta-tests.md) | Frozen fixtures + meta-tests (grade the graders) | Accepted |
| [0004](0004-triage-policy-and-check-refinements.md) | Triage policy: fix / whitelist / refine | Accepted |
| [0005](0005-single-command-ci-gate.md) | Single-command CI gate, dependencies pinned | Accepted |
| [0006](0006-scoped-prompt-hygiene.md) | Scoped prompt hygiene: ASCII only where it's model-facing | Accepted |

Born out of the EP09 "Validation Backbone" build-along (the reference-integrity
bug that passed every check green). See also
[`_management/invariant_coverage_matrix.md`](../invariant_coverage_matrix.md).
