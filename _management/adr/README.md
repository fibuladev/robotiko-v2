# Architecture Decision Records

Short, durable records of the non-obvious engineering decisions behind the
pipeline's validation backbone — the "why", so the next contributor (or the next
us) inherits the reasoning instead of re-deriving it.

Format: Status · Context · Decision · Consequences. One decision per file.
The decision in an Accepted ADR is never rewritten; dated clarification notes
may be appended (see ADR-0007's "Note on empirical claims"). To change a
decision, add a new ADR that supersedes the old one.

| ADR | Title | Status |
|---|---|---|
| [0001](0001-phase-reference-map-source-of-truth.md) | Phase→reference map is the single source of truth | Accepted |
| [0002](0002-ref-integrity-parses-reference-metadata.md) | Ref-integrity parses the reference metadata fields | Accepted |
| [0003](0003-frozen-fixtures-and-meta-tests.md) | Frozen fixtures + meta-tests (grade the graders) | Accepted |
| [0004](0004-triage-policy-and-check-refinements.md) | Triage policy: fix / whitelist / refine | Accepted |
| [0005](0005-single-command-ci-gate.md) | Single-command CI gate, dependencies pinned | Accepted |
| [0006](0006-scoped-prompt-hygiene.md) | Scoped prompt hygiene: ASCII only where it's model-facing | Accepted |
| [0007](0007-reference-first-or-pay-the-reshoot-tax.md) | Reference-first, or pay the reshoot tax | Accepted |
| [0008](0008-approval-gates-as-data.md) | Approval gates as data, not checkboxes | Accepted |
| [0009](0009-style-suffix-v2.md) | Style-suffix variant family (photoreal short-film modifier) | Accepted |
| [0010](0010-eye-canon-reconciliation.md) | Eye-canon reconciliation: appearance vs. prompt language | Accepted |
| [0011](0011-git-history-exposure.md) | Git-history exposure of the internal golden-release report | Accepted |
| [0012](0012-scaffold-pr-flow.md) | Episode-scaffold automation opens a PR, not a direct push | Accepted |
| [0013](0013-two-phase-visual-prompts.md) | Two-phase visual prompts: scenes are framed to approved pixels | Accepted |

Born out of the EP09 "Validation Backbone" build-along (the reference-integrity
bug that passed every check green). See also
[`_management/invariant_coverage_matrix.md`](../invariant_coverage_matrix.md).
