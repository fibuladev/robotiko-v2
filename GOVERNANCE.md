# Governance

Stated plainly, because vague governance docs are worse than none.

## One maintainer

There is one maintainer: Can Yalcin (Fibula). There is no team, no core
group, no committee. Decisions about the pipeline and the story are made by
one person, and that person is also, most weeks, in active production on an
episode. Your PR may sit for a week because that week I'm shooting a film,
not reviewing one. This isn't a rotation problem to be fixed — it's the
actual shape of the project, stated up front so nobody waits on a response
time this repo never promised.

## What's open to contribution

- **Validators and tests** (`tests/`) — new checks, sharper checks, fixed
  false positives.
- **Docs** (`docs/`, process docs in `_management/` that aren't canon) —
  clearer explanations, corrected drift, better examples.
- **Tooling** (`scripts/`, `_tools/mcp-gdrive/`) — automation improvements,
  bug fixes.
- **Translations** — of docs, not of the ROBOTIKO lyrics themselves (those
  are creative content, see below).
- **Your own universe** — not "contribution" in the PR sense, but the
  primary way this project wants to be used. See
  [UNIVERSES.md](UNIVERSES.md) and
  [CONTRIBUTING.md §1(a)](CONTRIBUTING.md#1-two-ways-to-contribute).

## What's closed

- **ROBOTIKO canon** — `_management/master.md`,
  `_assets/cast/character_profiles.json`, and the published creative files
  of released episodes. Licensed CC BY-NC 4.0, not MIT — see
  [LICENSE-CONTENT](LICENSE-CONTENT) and
  [CONTRIBUTING.md §2](CONTRIBUTING.md#2-what-is-canon-locked). These aren't
  closed because outside ideas are unwelcome; they're closed because this
  repo is the canonical home of one specific, authored story, and a
  crowd-edited canon stops being that story. If you want to change the
  canon, fork it — your fork's canon is entirely yours.
- **Creative direction** — the two human approval gates
  (`_management/pipeline_rules.md`), the mandatory suffixes, the golden
  rules in `CLAUDE.md`. These are the taste layer. They don't get voted on.

## Decisions

Non-obvious engineering and process decisions are recorded as ADRs in
[`_management/adr/`](_management/adr/) — Status · Context · Decision ·
Consequences, one per file, immutable once accepted. To change a past
decision, a new ADR supersedes it; history isn't rewritten. This is how the
reasoning behind the validation backbone survives past the session that
built it.

## Pull requests

Best-effort weekly review, not a guaranteed SLA. Small, focused PRs against
the open method (see [CONTRIBUTING.md §5](CONTRIBUTING.md#5-pull-request-process))
get reviewed faster than large ones. `python tests/run_all.py` must pass —
that's the one gate, enforced identically in CI.

**Branch protection** — the intended rule on `main` is that the
`validation_suite` CI check is required to pass before merge. That's a
GitHub repository setting, not something enforceable from inside the repo
itself, so it can't be verified by reading a file here. It is evidenced in
[RELEASE.md §3](RELEASE.md): the branch-protection API check runs at
go-public, once the setting is live and can be confirmed against the actual
branch protection API — not claimed in advance of that.

## Bus factor

This is a solo project. If it goes quiet — if commits stop, issues pile up
unanswered for months — that means the maintainer has moved on, not that the
project is secretly still gatekept. At that point it enters **archive mode**:
no active maintenance, no expectation of response, but nothing locked away.
The method is MIT-licensed specifically so that this outcome isn't a dead
end. Fork it, maintain your own copy, build your universe. That was always
the plan for the method — a maintainer going quiet just means you stop
waiting and start forking sooner.
