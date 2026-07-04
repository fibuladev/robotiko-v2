# Roadmap

> *"Glitch is Scripture."*

## Season 1: EP01 → EP10

The arc this repo exists to ship. EP01-EP08 are launched on YouTube. EP09 is
in motion-script validation. EP10 closes the season — and is the day the
repo itself goes public (see [AUTHOR.md](AUTHOR.md) and
[CONTRIBUTING.md](CONTRIBUTING.md) for what that means for forkers).

There is no Season 2 committed here. What comes after EP10, if anything, is
undecided on purpose — Season 1 is a complete bildungsroman, not a pilot for
a franchise.

## After EP10: open invitations, not a task list

These aren't promises of features the maintainer will build on a schedule —
they're honest invitations to the kind of help that would make the method
better, offered instead of apologized for. Some the maintainer intends to
pick up; some are explicitly "help wanted, no ETA."

| Invitation | Who's expected to drive it |
|---|---|
| **Independent fork stress-test** — build a real universe on the method (different genre, different suffix, different cast) and report what assumption broke. This is the single most valuable thing an outside contributor can do; see [UNIVERSES.md](UNIVERSES.md). | Help wanted — the maintainer can't stress-test their own assumptions from inside them. |
| **AV-sync measurement** — the pipeline claims beat-synced visuals from `musical_metadata.json` timestamps through to motion scripts, but there's no automated measurement of actual audio-visual sync drift in rendered output today. A validator or a manual methodology would close a real gap. | Help wanted. |
| **Retry-telemetry tooling** — image/video generation retries (Nano Banana, Kling/Veo/Seedance) aren't currently logged anywhere machine-readable. Lightweight tooling to track retry counts and failure modes per episode would sharpen the tool-selection guidance in `docs/tools-setup.md`. | Help wanted. |
| **Reproducibility discussion** — how deterministic *should* a creative pipeline built on generative tools be, and what would "reproducible" even mean here (same prompts, same seeds, same episode)? An open discussion thread, not a fixed spec. | Maintainer will open the thread; direction depends on who shows up. |
| **Validator coverage** — the nine check groups behind `python tests/run_all.py` are tracked against known invariants in `_management/invariant_coverage_matrix.md`. New checks are welcome per [GOVERNANCE.md](GOVERNANCE.md)'s "open to contribution" list. | Maintainer maintains the matrix; PRs add checks. |

## What the maintainer will do regardless of outside help

- Ship EP09 and EP10 to close Season 1.
- Keep the validation suite green and the docs honest as the repo evolves.
- Respond to [UNIVERSES.md](UNIVERSES.md) registrations and canon questions
  ([canon question template](.github/ISSUE_TEMPLATE/canon_question.md))
  on a best-effort basis, per [GOVERNANCE.md](GOVERNANCE.md).

If none of the invitations above ever get picked up, the method still stands
on its own — a complete, working example is better documentation than a
roadmap of things nobody built yet.
