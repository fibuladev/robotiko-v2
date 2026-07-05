# The Lesson Graduation Ladder

> The core method of this repo, named so it can be copied. A correction does not
> stay a note. It **graduates** — from a one-time fix in one person's head to a
> gate that blocks the whole team from re-making the mistake. Each rung is more
> durable than the one below it, and each is cheap enough to be worth climbing.

This is a field manual, not a manifesto. Every rung below is something you can do
in an afternoon on your own repo. The worked examples are real — names, dates, and
file paths are pulled straight from this repository so you can go read the actual
code and fixtures.

---

## The ladder

```
  (1) INCIDENT              a correction happens once, in one file, caught by one human
         |
         v
  (2) DATED RULE            _memory/lessons.md — the correction written down, with a date
         |
         v
  (3) VALIDATOR CHECK       tests/ — a function that reads the artifact and fails on the pattern
         |
         v
  (4) BIDIRECTIONAL         tests/test_validators.py — a BAD fixture it must FAIL,
      FIXTURE                 a GOOD fixture it must PASS (grade the grader)
         |
         v
  (5) ADR                   _management/adr/ — the reasoning, dated and immutable
         |
         v
  (6) CI GATE               validation_suite.yml — run_all.py blocks the merge on red
```

**(1) Incident.** Something goes wrong once. A human notices — usually the hard
way, by paying for the mistake (a reshoot, a wrong render, a bad merge). At this
rung the knowledge exists only in that person's memory of the afternoon they lost.

**(2) Dated rule.** The correction is written into `_memory/lessons.md` as a
plain-English rule with a date and the case that produced it. This is the cheapest
possible durability: the next person (or the next session) reads it at start-up and
does not re-derive the lesson from scratch. But a rule in a file is still just a
hope that someone reads and obeys it.

**(3) Validator check.** The rule becomes a function in `tests/` that reads the
artifact and returns a finding when the pattern reappears. Now the rule enforces
itself — but only if the checker is correct, and a checker you have only ever seen
pass is not yet evidence of anything.

**(4) Bidirectional fixture.** The checker gets graded. You freeze a **BAD**
fixture the check must fail and a **GOOD** fixture it must pass, and a meta-test in
`tests/test_validators.py` asserts *both* directions. The BAD fixture proves the
check can still see the bug; the GOOD fixture proves it does not fire on the
intended case. Fixtures are immutable snapshots — you never "fix" them, because
their whole value is that they never change.

**(5) ADR.** The reasoning is recorded as an Architecture Decision Record in
`_management/adr/` — one decision per file, Status / Context / Decision /
Consequences, immutable once accepted. The rule tells you *what*; the ADR tells the
next contributor *why*, so they inherit the trade-off instead of quietly undoing
it.

**(6) CI gate.** The check is wired into the one command, `tests/run_all.py`, which
runs in CI via `.github/workflows/validation_suite.yml` on every push and pull
request. A red fails the job and — with branch protection on — blocks the merge.
The guarantee now survives the person who wrote it.

Not every lesson climbs all six rungs. Many stop at rung 2 forever, because they
are matters of taste that no function can judge (see [Honest limits](#honest-limits-what-the-ladder-cannot-climb)).
The discipline is knowing *which* rung a given lesson can honestly reach — and not
claiming a higher one than it earns.

---

## Flagship case: the EP09 kintsugi reference bug

This is the ladder climbed end to end, by the most expensive bug the pipeline has
produced.

### (1) The incident

Robotiko, the series' android, has three body phases: pristine (Phase 1),
battle-damaged (Phase 2), and gold-mended "kintsugi" (Phase 3). Each phase needs
its own reference image so the image generator keeps the body consistent shot to
shot.

Episode 09 is the most visually novel episode in the series: it introduces the
Phase 3 kintsugi body (never rendered before), a new location (the workshop
interior *and* exterior), a mid-episode body transition (damaged → kintsugi at
scene 27), and a new group (the curious onlookers). Its scene prompts were authored
and generated **before the reference images for those new elements existed**.
`android_kintsugi.png` did not exist yet — so every gold-body scene was conjured
from long text on the *damaged* reference, the wrong base. The result: roughly 8-10
regenerations per scene, nearly every scene rescued by hand, where EP01-EP08 had
hit 80-90% first-pass because their references were ready. That gap is the reshoot
tax, paid in full, once.

### (2) The dated rule

The correction went into `_memory/lessons.md` (category: Reference Image Workflow),
dated 2026-06-29:

> **RULE: REFERENCE-FIRST, OR PAY THE RESHOOT TAX** — Generate every NEW reference
> an episode needs (a new body state, a new location, a new group) BEFORE you author
> or generate scenes against it. [...] A scene must frame to a reference that EXISTS,
> not conjure it from text.

with the honest corollary that it is *healthy*, not failure, to discover at
generation time that a prompt needs a better reference and go back to update it —
the flow is iterative.

### (3) The validator check

The rule became `check_reference_first` in `tests/visual_prompt_validator.py`. It
reads the `phase_reference_map` and `reference_images` from
`_assets/cast/character_profiles.json` and **fails when an episode has Robotiko
scenes in a phase whose dedicated reference is null, or is declared but missing on
disk.** It would have caught EP09 on day one: kintsugi scenes present, kintsugi
reference path null. This is a metadata check — it judges the structured fields
where the rule actually lives, not the prose (the prompts say "the chrome android",
never "robotiko", so a prose-only check would have stayed blind — the sibling
lesson that produced `check_ref_integrity`).

### (4) The bidirectional fixture

The checker is graded by frozen fixtures and both-directions meta-tests in
`tests/test_validators.py`:

- `tests/fixtures/ep09_visual_prompts_BROKEN.md` — the real bug, captured forever.
  It MUST fail.
- `tests/fixtures/ep09_visual_prompts_GOOD.md` — its corrected twin. It MUST pass.

The meta-tests assert both directions and pin *why* the file ever shipped green.
Loosen a regex six months from now and the BROKEN fixture goes green — the meta-test
turns red and tells you the grader has stopped grading.

### (5) The ADR

The reasoning is `_management/adr/0007-reference-first-or-pay-the-reshoot-tax.md`
(Accepted 2026-06-29). It records the single root cause, the decision to reaffirm
reference-first as the pipeline's first principle, and the choice to enforce it with
`check_reference_first`.

Crucially, the ADR is **honest about its own evidence**. Its 2026-07-04 note states
plainly that the "80-90% first-pass" and "8-10x reshoot" figures are experiential
observations from the director's production notes, **not instrumented telemetry** —
no automated retry logging exists. The economics that motivate the whole rule are
labelled as lived experience, not measured fact. An ADR that inflates its evidence
is just a lie with a decision number; this one says exactly how much it knows.

### (6) The CI gate

`check_reference_first` runs inside `tests/run_all.py`, the single gate, wired into
CI through `.github/workflows/validation_suite.yml`. Every push and pull request
runs it; a red blocks the merge. The kintsugi-class root cause cannot recur
silently — CI now blocks any episode that has scenes for a body state with no
reference.

The full narrative of this bug and its sibling (the reference-*integrity* green that
checked nothing) is in [`_management/case_study_validation_backbone.md`](../_management/case_study_validation_backbone.md).

---

## Mini-case: a rule that graduated *down* — honest retirement

Rules can also die, and the ladder has to let them die honestly, or `lessons.md`
becomes a graveyard of advice that quietly contradicts itself.

The top of `_memory/lessons.md` carries a **RULE RETIREMENT CONVENTION**:

> When a rule in this file is replaced by a better formulation, mark the old rule
> with `[SUPERSEDED YYYY-MM-DD — see <successor description>]` rather than deleting
> it. This preserves the audit trail of how rules evolved while making clear which
> version is current.

The clearest case is the anti-spawn image guard. The original rule (added
2026-05-31) told every single-character prompt to say **"only ONE chrome android, no
second robot."** It was well-intentioned and wrong: the negation made some
generators latch onto the word "robot" and spawn exactly the second android it was
trying to forbid. On 2026-06-28 it was superseded — not deleted — by a tool-aware
formulation, `single figure composition, no additional characters`, plus a narrow
exception for *intentional* multi-figure compositions (a character watching its own
ghost-self). The old rule still sits in the file, stamped:

> **[SUPERSEDED 2026-06-28 — see updated single-figure rule below]**

Anyone reading the history sees both the mistake and the correction, in order. The
retirement is itself part of the record. A deleted rule teaches nothing; a
superseded one teaches how the thinking moved.

---

## Start your own ladder in 3 steps

You do not need this repo's tooling, its story, or its file layout. The ladder is
portable. The first three rungs are the whole method in miniature — climb them on
your own repo the next time a mistake costs you an afternoon.

**Step 1 — Write the dated rule.** In a `lessons.md` (or any file your team reads at
start-up), write one line: the mistake, the fix, the date, and the case that caused
it. Date it. The date is what lets you retire it honestly later.

```
## 2025-11-14 — Config files must end with a trailing newline
Incident: deploy #4127 failed because config.yaml had no final newline and the
parser silently truncated the last key. Rule: every *.yaml under config/ ends
with exactly one trailing newline.
```

**Step 2 — Write the 20-line checker.** Turn the rule into a function that reads the
artifact and fails on the pattern. Standard library only — no framework, no
install. It does not need to be clever; it needs to run in CI.

```python
# tests/check_trailing_newline.py
import sys, glob

def check_trailing_newline(paths):
    findings = []
    for p in paths:
        with open(p, "rb") as f:
            data = f.read()
        if data and not data.endswith(b"\n"):
            findings.append(f"FAIL {p}: no trailing newline")
        elif data.endswith(b"\n\n"):
            findings.append(f"FAIL {p}: multiple trailing newlines")
    return findings

if __name__ == "__main__":
    issues = check_trailing_newline(glob.glob("config/**/*.yaml", recursive=True))
    print("\n".join(issues) or "OK: all config files end in one newline")
    sys.exit(1 if issues else 0)
```

**Step 3 — Freeze one BAD fixture.** Save the exact broken input that caused the
incident, next to a good twin, and write a test that asserts the checker fails the
BAD one and passes the GOOD one. This is the step everyone skips and the one that
keeps the checker honest for years.

```python
# tests/test_check.py
from check_trailing_newline import check_trailing_newline

def test_catches_the_bug():
    assert check_trailing_newline(["tests/fixtures/config_BAD.yaml"])   # must FAIL

def test_ignores_the_good_case():
    assert not check_trailing_newline(["tests/fixtures/config_GOOD.yaml"])  # must PASS
```

That is a complete ladder from rungs 1 to 4. Add the ADR (rung 5) when the *why* is
non-obvious enough that someone might undo it, and the CI gate (rung 6) when you
want the guarantee to survive you. Wire the checker into whatever one command your
CI already runs.

The two rules that make the whole thing hold:

- **Make the check fail first.** Run it against the BAD fixture before you trust it.
  A green you have never seen turn red is not evidence — it might be checking
  nothing.
- **Never loosen a check without a both-directions proof.** Any change that makes a
  check pass more (a whitelist, a guard, a tweak) ships with two tests: one proving
  it still catches a real bug, one proving it now ignores the intended case.

---

## Honest limits: what the ladder cannot climb

The ladder mechanizes what can be mechanized. It stops, on purpose, where judgement
begins — and the repo says so out loud rather than pretending otherwise.

`_management/invariant_coverage_matrix.md` marks every project rule as one of:
**Machine** (mechanically checked, CI blocks on failure), **Heuristic** (partially
checked, can over- or under-fire, treat as advisory), **Human** (gated by a person
at a checkpoint, no automation claimed), or **Gap** (a rule we care about with no
automated check yet). The matrix is the coverage truth — not a green run.

Three honest categories the ladder does not close:

- **Human gates.** The two creative checkpoints — director approval after
  dramaturgy, and after the motion script — are gated by a person on purpose. No
  function decides whether a scene serves the story. The ladder protects the
  mechanical floor so the humans can spend their attention on taste.
- **Heuristics, labelled as such.** The body-state keyword check is free text and
  cannot fully attribute an adjective to a subject, so it is marked Heuristic and
  backed by the reliable, metadata-based reference gate — trusted *together*, never
  alone.
- **Named gaps.** Some rules are simply not enforced yet — the no-glow eye rule, for
  one — and the matrix names them as gaps rather than implying coverage that does
  not exist. A gap you have named is a backlog item; a gap you have hidden is a blind
  spot with a badge of safety.

The point of the whole method is not to automate judgement. It is to mechanize
everything that *isn't* judgement, so that when a green run comes back, it certifies
exactly the Machine rows and not one inch more — and the humans are left free to
argue about the things that actually need arguing about.

---

*Method born out of the EP09 "Validation Backbone" build-along. See
[`_management/case_study_validation_backbone.md`](../_management/case_study_validation_backbone.md)
for the flagship bug in full, [`_management/adr/`](../_management/adr/) for the
decisions, [`_management/invariant_coverage_matrix.md`](../_management/invariant_coverage_matrix.md)
for the coverage truth, and [`_memory/lessons.md`](../_memory/lessons.md) for the
rules themselves.*
