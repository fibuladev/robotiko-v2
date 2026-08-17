# Case Study — The Validation Backbone

> How one quiet bug in Episode 09 — a test that passed green over a file we *knew*
> was broken — became permanent infrastructure: a set of automated checks, proofs
> that the checks themselves work, and a single gate that blocks a bad merge.
>
> This is written for a reader who has never seen the tools by name. Every term is
> defined the first time it appears, and every decision is paired with the cost we
> would have paid for skipping it — shown through this exact bug.

---

## 1. The lie a green test tells

Episode 09's visual-prompt file passed every automated check. Green across the
board. And it was broken.

A **visual-prompt file** is the document that tells the image generator what to
draw for each shot of an episode — one block of plain-English text per scene, plus
some metadata fields naming which reference image to attach. Robotiko, our android,
has three body phases across the series: pristine (Phase 1), battle-damaged (Phase
2), and gold-mended "kintsugi" (Phase 3). Each phase needs a *different* reference
image so the generated frames stay consistent.

EP09 is a damaged-body episode. But its prompts attached the **pristine** reference
image — the wrong body — to scene after scene. A human would catch it instantly.
Our checks did not. They reported success.

A passing test suite is supposed to be evidence of correctness. When it passes over
a known defect, it is worse than no test at all: it manufactures confidence in the
broken thing. That is the most dangerous state a pipeline can be in, because nobody
goes looking for bugs in a green build.

**The cost of leaving it:** every future episode would inherit the same blind spot.
The one person who could see the error would have to manually re-check every
reference in every file forever — and the day they missed one, a pristine Robotiko
would ship inside a damaged-body episode and break the visual story.

---

## 2. Two blind spots

Why was the check blind? Two reasons, and they compounded.

**It searched the prose for the wrong word.** The check looked for the string
"robotiko" in the prompt text to decide "this scene is about Robotiko, let's police
it." But the prompts never say "robotiko" — they say "the chrome android". So the
character check simply never engaged.

**It never read the field where the bug lived.** The wrong reference wasn't in the
prose at all; it sat in a metadata field (`Image Reference Path` / `Upload`). The
validator only ever parsed the prose. It was the right tool pointed at the wrong
place — checking the description of the painting while the mislabelled canvas hung
untouched beside it.

**The cost of leaving it:** any rule that lives in a metadata field — references,
upload lists, anything structured — is invisible to a prose-only check. Not just
this bug; an entire *category* of bugs passes silently.

---

## 3. Encode the rule nobody wrote down

The deepest problem wasn't the check — it was that the rule the file broke had never
been written down anywhere a machine could read. "Which Robotiko belongs in which
shot" lived only in the director's head.

So we made it data. We created a **source of truth** — a single authoritative place
that defines a fact, so that everything else refers to it instead of repeating it.
Here that's a `phase_reference_map` in `character_profiles.json`: phase 1/2/3 → the
correct reference image, plus episode-level exceptions (EP08's body stays damaged
even at Phase 3; EP09 transitions mid-episode at scene 27). We recorded *why* in
[ADR 0001](adr/0001-phase-reference-map-source-of-truth.md).

An **ADR** (Architecture Decision Record) is a short, dated note that captures one
decision and the reasoning behind it, so the next contributor inherits the *why*
instead of guessing or quietly undoing it. We keep ours in
[`_management/adr/`](adr/).

**The cost of leaving it:** without a written source of truth, every check is just
one more person's opinion hard-coded in a script. There's nothing to check
*against*, no single place to fix when the rule changes, and the rule keeps living
in one fragile human memory.

---

## 4. Red, then green for the right reason

With the rule encoded, we taught the check to read the reference fields and compare
them against the map. We ran it on EP09 and it turned **red** — naming the exact
file, scene, the forbidden reference, and the fix. The bug was finally visible to
the machine.

This is the rhythm of **TDD** (Test-Driven Development): make the test fail first
(prove it can actually detect the problem), then make it pass. A test you've only
ever seen pass is not yet evidence of anything — it might be green because it checks
nothing. The red is the proof of life.

Then we fixed the **cause, not the symptom**. We corrected EP09's references — but
we also fixed the *skill* that generates prompts, so the bug couldn't be re-authored
in the next episode, and we replaced an anti-spawn phrase ("only ONE chrome android")
that backfired in one generator with a tool-aware version. Green — for the right
reason. (See [ADR 0002](adr/0002-ref-integrity-parses-reference-metadata.md).)

**The cost of leaving it:** fix only the symptom — EP09's references — and EP10 is
generated by the same unchanged skill, reproducing the identical bug. You'd be
bailing water without patching the hull.

---

## 5. Grade the graders

A checker with no proof that it works is just a more confident way to be wrong. So
we tested the test.

We froze two permanent **fixtures** — fixed input files used to exercise a check.
[`ep09_visual_prompts_BROKEN.md`](../tests/fixtures/ep09_visual_prompts_BROKEN.md)
is the real bug, captured forever; it MUST fail. Its corrected twin
[`ep09_visual_prompts_GOOD.md`](../tests/fixtures/ep09_visual_prompts_GOOD.md) MUST
pass. **Meta-tests** (tests whose subject is another test) assert both directions,
and — crucially — assert that the broken file fails *only* on the reference check,
pinning the explanation of why it ever shipped green. (See
[ADR 0003](adr/0003-frozen-fixtures-and-meta-tests.md).)

This is the spirit of **BDD** (Behavior-Driven Development): describe the behavior in
plain terms — "given the wrong reference, the check fails; given the right one, it
passes" — and encode exactly that. The check is now defined by the behavior we can
demonstrate, not by the code we happened to write.

**The cost of leaving it:** an untested checker rots silently. Someone loosens a
regular expression six months later, the check quietly stops catching anything, and
you're back to a green that means nothing — except now everyone trusts it more.

---

## 6. One bug is a class — but a red isn't always a bug

We swept the new checks across every episode. Reds lit up in EP02–EP08. The
temptation is to "fix" all of them. That would have been a mistake — because a red
test is not always a bug. We triaged each one into exactly three buckets:

- **FIX** — a real defect. EP04 and EP05 had the same pristine-on-damaged reference
  error. Corrected (text only; the shipped images were kept).
- **WHITELIST** — intentional, and documented. EP08's dream sequence deliberately
  shows hundreds of *pristine copies* around the one damaged original; EP06's story
  pairs the damaged Robotiko against a pristine conformist *foil* android. The
  forbidden word legitimately describes something that isn't our hero. We recorded
  narrow, scene-pinned exceptions with reasons — never a blanket "ignore this word
  in this episode," so a real slip anywhere else still fires.
- **REFINE** — the check over-fired. It flagged "pristine **shelves**" and
  "**iron walls** becoming translucent" — scenery, not Robotiko. We taught it to
  judge the character, not the set. And it flagged EP02/EP03's "cracked" panels,
  which are *canon* damage — so we made the phase rule per-episode (EP01 pristine,
  but EP02–EP03 already battle-worn). (See
  [ADR 0004](adr/0004-triage-policy-and-check-refinements.md).)

The scariest find was hiding under a green: EP06 used a slightly different scene
header format, so the parser matched **zero** scenes and the reference check had been
passing over *nothing* for weeks. A green that means "I checked everything" and a
green that means "I checked nothing" look identical. We now assert every shipped file
parses a non-zero number of scenes.

The discipline that made the loosenings safe: **no check is ever loosened without a
both-directions proof** — one test that it still catches a real bug, one that it now
ignores the intended case.

**The cost of leaving it:** treat every red as a bug and you corrupt correct files
(rewriting EP08's intentional dream, "fixing" canon damage). Treat every red as
noise and you silence real continuity errors. And the zero-scene false-green means
you'd ship an entire episode believing it was checked when it never was.

---

## 7. Make it last

A check only used when someone remembers to run it is a habit, not a guarantee. We
made it durable.

- **One command.** [`tests/run_all.py`](../tests/run_all.py) runs all twelve check
  groups in sequence — naming, pipeline integrity, the visual sweep, prompt hygiene,
  musical metadata, motion script, CapCut guide, character profiles, the meta-tests,
  doc-reference integrity, energy-motion sync (advisory) and the forbidden-terms
  gate — and fails if any group fails.
- **CI that blocks.** **CI** (Continuous Integration) is the service that
  automatically runs your checks on every change pushed to the shared repository.
  Ours ([`validation_suite.yml`](../.github/workflows/validation_suite.yml)) runs the
  one command on every push and pull request; a red fails the job and — with branch
  protection on — blocks the merge.
- **Dependencies pinned.** The code uses only Python's standard library (nothing to
  install — the smallest possible attack surface), the Python version is pinned to an
  exact patch, and the third-party CI actions are pinned to immutable commit
  identifiers rather than moving labels. (See
  [ADR 0005](adr/0005-single-command-ci-gate.md).)

**The cost of leaving it:** scattered, manual checks get skipped under deadline. The
meta-tests existed but weren't in CI, so nothing stopped a future change from
breaking them. Unpinned dependencies mean a check that passes today can fail tomorrow
for reasons that have nothing to do with your code.

---

## 8. When your own rules contradict each other

The last piece was the most interesting, because our own rules pointed in opposite
directions.

- **master.md requires** the sanctioned cultural attribution — the project's
  philosophy credited to the Turkish wisdom tradition, its literature to Turkish
  folk poetry, and historical figures framed geographically ("lived and taught in
  Anatolia"). This attribution is the soul of the project. It is *mandatory* in
  the canon.
- **Production requires** the strings we feed to image and video generators to be
  plain-English ASCII (the basic English character set, no accented or non-Latin
  letters). Non-ASCII characters tokenize unpredictably, and cultural labels bleed
  attribution into the generated picture.

A naïve "no non-ASCII anywhere" lint would punish the canon — flag the very attribution
the project is built to carry. Doing nothing leaves real leaks (EP03's prompts carried
Turkish characters; em-dashes were everywhere). The contradiction looks irreconcilable
only until you notice it isn't about *files* — it's about **audience**: who reads the
string.

So we scoped the rule by audience. The canon and the internal direction notes — and
even the Dramaturgy Reference lines *inside* a visual-prompt file — keep their
sanctioned Turkish. Only the **model-facing prompt strings** (the Text Prompt blocks
in visual-prompt files, the Motion Prompt blocks in motion-script files) must be
ASCII. The lint ([`prompt_hygiene_lint.py`](../tests/prompt_hygiene_lint.py)) reads
*only* those blockquotes and is built so it can never even open master.md or the
direction notes. (See [ADR 0006](adr/0006-scoped-prompt-hygiene.md).)

The proof that the canon is safe is itself a test: the meta-tests assert the lint
catches a tradition label or a non-ASCII character leaking into a real prompt string,
*and* that it ignores the identical decoration when it sits in a Dramaturgy line or
any out-of-scope file — and that master.md exists yet is provably not in the lint's
reach.

**The cost of leaving it:** the wrong fix here is uniquely damaging. An
over-broad lint would have made the project's cultural soul fail CI — training
everyone to see the canon as an error to be silenced. Scope was not a compromise of
the rule; it *was* the resolution.

---

## 9. What's still on a human

Honesty is part of the infrastructure. A green run certifies what it certifies — and
not one inch more. We keep an [Invariant Coverage
Matrix](invariant_coverage_matrix.md) that marks every project rule as
machine-checked, heuristic (an advisory signal that can over- or under-fire),
human-gated, or an outright gap.

The reference check is the reliable, machine-enforced gate. The character-keyword
check is honestly labelled a heuristic — free text can't fully attribute an adjective
to a subject — and it's backed by the reliable check, not trusted alone. The three
rules this document first named as explicit **gaps** — the anti-spawn phrasing, the
no-glow eye rule, the motion video-suffix — have since been closed: all three are
machine-checked today (`motion_script_validator.py` for the anti-spawn guard and the
video suffix, `check_eye_glow` plus `scan_eye_glow` for the eye rule). The [coverage
matrix](invariant_coverage_matrix.md) is the live ledger — what is still unchecked is
named there, not implied away here. And the
creative checkpoints — director approval after dramaturgy, at the visual stage's
reference gate, and after the motion script — are gated by a person on purpose. We
don't pretend to automate taste.

**The cost of leaving it:** a coverage matrix that overclaims is its own false green.
The moment the docs imply a rule is enforced when it isn't, people stop watching for
it — and the gap becomes a blind spot with a badge of safety.

---

## 10. Takeaways

A transferable checklist, earned from one small bug:

1. **A passing test over a known defect is the most dangerous state.** Distrust a
   green you haven't seen turn red.
2. **Check the data where the rule actually lives** — the structured fields, not just
   the prose.
3. **Write the rule down as a source of truth** before you check against it.
4. **Make the test fail first.** Red is the proof the check can see.
5. **Fix the cause, not the symptom** — the generator, not just the artifact.
6. **Grade the graders.** Freeze the bug as a fixture; prove the checker both ways.
7. **A red isn't always a bug.** Triage: fix / whitelist / refine — and never loosen
   a check without a both-directions proof.
8. **A green that checked nothing looks like a green that checked everything.** Assert
   non-zero coverage.
9. **One command, one blocking gate, pinned dependencies.** Make the guarantee
   survive the person.
10. **When your own rules contradict, scope by audience** — the right scope dissolves
    the contradiction without punishing either rule.
11. **Be honest about what isn't covered.** A coverage matrix that overclaims is just
    another lie a green test tells.

---

*Born out of the EP09 "Validation Backbone" build-along. Decisions:
[`_management/adr/`](adr/). Coverage: [`invariant_coverage_matrix.md`](invariant_coverage_matrix.md).
Rules: [`_memory/lessons.md`](../_memory/lessons.md) (Pipeline Validation Backbone).
The transferable method this bug taught — how a correction graduates from note to CI
gate — is named in [`docs/method-lesson-graduation.md`](../docs/method-lesson-graduation.md).*
