# ADR 0012 - Episode-scaffold automation opens a PR, not a direct push

- **Status:** Accepted (2026-07-05)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** Repo-Readiness Program (WS9 - release engineering)

## Context

The `Create New Episode Scaffolding` workflow
(`.github/workflows/create_episode.yml`) generates a new episode directory with
`scripts/create_episode.py`. Until now, after running the validation gate it
committed and **pushed the scaffold straight to the default branch**.

Two things change that make direct push the wrong shape at go-public:

1. **Branch protection is about to be real.** Go-public sets a required-status
   rule on `main` (the `validation_suite` check) and disallows force-push
   (`GOVERNANCE.md`, evidenced in the release runbook (private) §3). A workflow that pushes
   directly to `main` either has to be exempted from that protection - punching
   a hole in the exact guarantee we are advertising - or it breaks. Neither is
   acceptable.
2. **Uniform gate.** The project's stated model is "one gate for the whole repo":
   `python tests/run_all.py`, enforced identically for every contributor PR
   (`GOVERNANCE.md`, ADR-0005). An automation that writes to `main` without a PR
   is a second, privileged path. Removing it makes the automation obey the same
   rule as a human contributor.

## Decision

**The scaffold workflow opens a pull request instead of pushing to `main`.**

- It creates a branch `scaffold/ep{XX}`, commits the scaffold there, pushes the
  branch, and opens a PR via `gh` using the built-in `GITHUB_TOKEN`.
- The `permissions:` block gains `pull-requests: write` (added to the existing
  `contents: write`); nothing else is widened.
- The validation gate (`python tests/run_all.py`) still runs **before** the
  branch is pushed - a red scaffold never becomes a PR. The PR body records that
  the gate already passed in the run.
- An **empty-diff guard** exits cleanly with no branch and no PR when the
  scaffold produces no changes (e.g. the episode already exists), so re-runs
  are no-ops rather than empty commits.
- A **concurrency guard** (`group: create-episode-${{ inputs.episode_number }}`)
  serializes runs for the same episode number.
- All prior hardening is kept: two-digit `episode_number` regex validation,
  Actions pinned to immutable commit SHAs with human-readable version comments,
  and an emoji-free commit message.

The maintainer merges the PR. `main` is only ever written to through a reviewed,
gate-passing PR - by humans and by this automation alike.

## Consequences

- The automation no longer needs an exemption from branch protection; it works
  *with* the protection instead of around it. The "one uniform gate" claim in
  `GOVERNANCE.md` stays literally true.
- Scaffolding a new episode now has a human merge step. That is a deliberate
  extra click, not friction to be optimized away: it is the same review surface
  every other change to `main` gets, and scaffolding a fresh episode is rare.
- `pull-requests: write` is the minimum scope for `gh pr create`; the token is
  still the ephemeral per-run `GITHUB_TOKEN`, not a stored credential.
- If a future need ever justifies a direct-push automation again, it would
  require a superseding ADR that also explains how it coexists with branch
  protection - the reasoning is captured here so that conversation starts from
  the trade-off, not from scratch.
