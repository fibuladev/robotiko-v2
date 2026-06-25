# ADR 0005 — Single-command CI gate, dependencies pinned

- **Status:** Accepted (2026-06-26)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Validation Backbone

## Context

The checks existed but were scattered: three separate CI steps, and the
grade-the-graders meta-tests weren't run in CI at all. "Run before you push" was
a human habit, not an enforced gate. For a repo about to go open-source, the
guarantee has to survive any contributor and any forgotten step.

## Decision

- **One command.** `tests/run_all.py` runs every machine check in sequence —
  naming, pipeline integrity, the visual-prompt sweep, and the validator
  meta-tests — and exits non-zero if any group fails. Local and CI run the
  identical entrypoint.
- **CI blocks on failure.** `.github/workflows/validation_suite.yml` runs
  `python tests/run_all.py` on every push and pull request. A red fails the job;
  with branch protection requiring this check, it blocks the merge. (Enabling
  branch protection is a one-time GitHub setting, recorded as a launch checklist
  item.)
- **Dependencies pinned.**
  - The project code is **standard-library only** — no `pip install`, nothing to
    pin at the package level. This is the strongest dependency hygiene: the
    smallest possible attack surface.
  - The Python toolchain is pinned to an exact patch (`3.11.9`).
  - GitHub Actions are pinned to **immutable commit SHAs** (with the human-readable
    version in a trailing comment): `actions/checkout@…34e1148` (v4.3.1),
    `actions/setup-python@…a26af69` (v5.6.0). Tags are mutable; SHAs are not.
  - The workflow runs with least privilege (`permissions: contents: read`).

## Consequences

- The rule that lived in one person's hands now lives in the repo and runs on
  every change.
- Adding a check means adding one entry to `CHECK_GROUPS`; CI picks it up for
  free.
- SHA-pinned actions must be bumped deliberately (a future Dependabot config can
  automate the PRs); this is the accepted trade-off for reproducibility.
