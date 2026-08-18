# Governance

Stated plainly, because vague governance docs are worse than none.

## One maintainer

There is one maintainer: Can Yalçın (Fibula). There is no team, no core
group, no committee. Decisions about the pipeline and the story are made by
one person — and that person has a full-time day job and a life outside
this repo. The ten-episode arc is complete; what remains is maintenance,
and maintenance happens in evenings and weekends. Your PR may sit for a
week because that week belonged to the day job, not to this repo. This
isn't a rotation problem to be fixed — it's the actual shape of the
project, stated up front so nobody waits on a response time this repo
never promised.

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
- **Creative direction** — the three human approval gates
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

**Branch protection** — `main` is protected on four counts: the required
status check is the validation suite's job context `checks` (workflow
**Validation Suite**), which must pass before merge; force-pushes are
blocked; branch deletion is blocked; and administrators are included, so the
maintainer gets no silent bypass of the same gate contributors face. Those
are GitHub repository settings rather than files in the tree, so no file here
can prove them — read them off the repository's branch-protection settings
page, and read the gate itself in
[`.github/workflows/validation_suite.yml`](.github/workflows/validation_suite.yml).

## Bus factor

This is a solo project. If it goes quiet — if commits stop, issues pile up
unanswered for months — that means the maintainer has moved on, not that the
project is secretly still gatekept. At that point it enters **archive mode**:
no active maintenance, no expectation of response, but nothing locked away.
The method is MIT-licensed specifically so that this outcome isn't a dead
end. Fork it, maintain your own copy, build your universe. That was always
the plan for the method — a maintainer going quiet just means you stop
waiting and start forking sooner.
