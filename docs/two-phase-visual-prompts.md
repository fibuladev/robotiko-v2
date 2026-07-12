# Two-Phase Visual Prompts — why scenes are framed to real pixels

> The visual-prompts stage used to do one thing in one pass: write the environment
> references *and* every scene prompt together, against a text description of a space
> that did not exist yet. It now does two things, with a human gate between them.
> First it authors the references and stops. A human generates and approves the real
> images. *Then* it writes the scenes, framed against the pixels that actually came
> back. This page explains why the stage was split, what each half owes, and — just as
> important — what the split still cannot promise.

This is the load-bearing explanation behind one line in
[`../_management/pipeline_rules.md`](../_management/pipeline_rules.md) and one gate in
[`../_skills/robotiko-visual-prompts/SKILL.md`](../_skills/robotiko-visual-prompts/SKILL.md).
If you only read the pipeline overview, the visual stage looks like a single box
between dramaturgy and image generation. It is two, and the seam between them is a
mandatory checkpoint. Here is the reasoning that put the seam there.

---

## The principle it protects: reference-first

Robotiko is rendered by an image generator that has no memory between shots. The only
way a location or a body-state stays the same from scene to scene is a **reference
image** every prompt points back to. Author the references first, and each scene
*frames to* a picture that exists. Author the scenes first, and each one *conjures*
its world from long text — the same long text, subtly different every time.

That principle already has a name and a scar. It is
[ADR-0007, "reference-first, or pay the reshoot tax"](../_management/adr/0007-reference-first-or-pay-the-reshoot-tax.md),
and it was earned the hard way on EP09: the kintsugi body-state and the workshop location
were prompted before their references existed, and nearly every gold-body scene had to
be regenerated 8-10 times to claw back a consistency the reference would have given for
free. The reshoot tax, paid in full, once. The full climb of that lesson from incident
to CI gate is told in
[method-lesson-graduation.md](method-lesson-graduation.md).

ADR-0007 fixed *ordering*: generate the references before the scenes. What it did not
fix is subtler, and it is what this page is about. You can generate the references
first and **still** write all your scenes against the *text* of those references
instead of the *images*. That is exactly what the old single-pass stage did, and it
left three gaps open.

---

## Why one pass was not enough: three gaps

### Gap 1 — a "framing pass" that was never a blocker

The old stage ended with a reconciliation step: after the real references came back,
walk the scenes and fix any that the pixels contradict. On paper, correct. In practice
it was marked "never a blocker," and a step that never blocks is a step that gets
skipped.

The clearest case is dated **2026-07-07**, commit **`27f375b`** on EP10. Reference B —
a crossroads with the Mentor's waymark staff — was generated and drifted from its
authoring note: the first generation came back with a glowing amber tip and a *European
castle* in the background; a later edit fixed the amber and removed the houses so the
shot reads as an Anatolian village exit onto open highland. The REF block was dutifully
updated to match the locked image:

> **Framing Pass note (2026-07-07):** Locked. Gen 1 drifted (glowing amber + European
> castle); gen 2 fixed the amber + Anatolian village; final edit removed the background
> houses so the shot reads as the village EXIT onto open highland — this sidesteps the
> flat-roof vs tile-roof clash with REF D and ties the crossroads into the
> green-highland world of REF C / REF A.

The reference note was reconciled. The **forty scene prompts written against the old
description were not re-checked**. The single commit touched the REF block and nothing
else. That is the gap made concrete: a late reference edit had no mechanism forcing the
scenes bound to it to be re-verified, so they silently kept describing a world that no
longer existed. (See the full block in
[`../episode-10/04_visuals/ep10_visual_prompts_v01.md`](../episode-10/04_visuals/ep10_visual_prompts_v01.md).)

### Gap 2 — under-decomposed locations, found late by luck

The old heuristic for deciding how many references a location needs was crude: roughly
"three or more scenes sharing a place get one reference." A wide location — a whole town
seen from three very different vantage points — collapses under that rule into a single
reference that cannot actually hold all three shots. On EP10 the town needed to be split
into distinct camera-spaces (the lane, the market edge, the far edge with its tower);
the shipped v01 mapped them to one reference and paid for it, with the missing spaces
(REF E and REF F) discovered late, essentially by luck, rather than named up front.

A gap you find by luck is a gap you will eventually not find.

### Gap 3 — the scenes carrying the emotional weight had no reference at all

Some of the most important shots have no environment reference by design — a
fourth-wall close-up, a macro on a hand, an eye. Under the old flow these were simply
outside the reconciliation net. The scenes least anchored to a picture were also the
ones the pipeline checked least. That is precisely backwards.

The root fix for all three is structural: **split the stage in two, put a human gate in
the middle, and record the gate as data** — the same "gates as data, not checkboxes"
pattern as
[ADR-0008](../_management/adr/0008-approval-gates-as-data.md).

---

## Phase 1 — author the references, then stop

Phase 1 produces a complete, valid deliverable that contains **zero scene prompts**. Its
whole job is to specify the world so precisely that a human can generate it, look at it,
and approve it before a single scene is written. It carries five things.

**1. Decomposition, by an operational test.** The vague "3+ scenes" rule is replaced by
two concrete questions asked of any two scenes that might share a reference:

- *Site-map test* — can both cameras sit as viewpoints on one drawable floor-plan of a
  single space?
- *Landmark-consistency test* — does every landmark named in both keep the same relative
  position from both viewpoints?

If either fails, they are **different spaces** and need different references. The ceiling
is the dramaturgy's own location labels (never segment finer than the story does); the
alarm band is roughly one reference per three scenes. This is the test that would have
caught EP10's town before REF E/F went missing.

**2. Through-anchors.** Sibling references of one location must share a palette journey,
a single light-direction and time-of-day contract, and at least one co-visible
landmark that ties them into the same world. EP10's monolith silhouettes are the
through-anchor for its highland; the REF B/D flat-roof-vs-tile-roof clash is the worked
failure the check exists to prevent.

**3. Narrative anchors.** Each reference block records not only how the space *looks* but
what the story needs it to *do* — the beside-space kept open for a figure to enter, the
street that must run toward the town because that direction is the direction of desire.
These story obligations travel with the reference so Phase 2 cannot frame them away.

**4. Art Direction Locks — a mandatory section.** The cross-scene working memory: the
color-journey scene-bands, the per-episode budgets (how many amber moments the whole
film is allowed), the camera personality and gaze discipline, the body-state locks, and
an explicit list of *what is not shown*. This is the memory Phase 2 resumes from so no
individual scene drifts off the episode's spine.

**5. The scene→space coverage map.** A plain table — `scene-id | camera-space |
one-line narrative role` — authored **before** anything is generated. The director reads
it against the approved dramaturgy on cheap text and confirms that every scene has a
home and every reference earns its place, days before spending real time and credits
generating. This table is also the backstop for Gap 1: if a reference is ever edited
late, the map names exactly which scenes are bound to it and therefore which must be
re-verified.

Character and group references are enumerated and gated here too, not just environments
— ADR-0007's original scar was a *character* reference (the kintsugi body), so a new
body-state or a new crowd is a Phase-1 obligation like any location.

---

## The reference gate

Phase 1 ends at a hard human checkpoint. The pipeline will not write a scene prompt
until a human has generated the references into
`episode-10/04_visuals/raw/` (gitignored production output), iterated on them
freely, approved them, and recorded that approval.

The approval is **data, not a checkbox**. It lands as a record in
[`../_management/approvals.json`](../_management/approvals.json) — the same ledger that
holds the dramaturgy and motion-script gates — pinning the exact bytes of the approved
Phase-1 document by SHA-256. From that moment the Phase-1 file (`…_v01.md`) is **frozen**:
its references, locks, coverage map, and geometry notes are the contract. Phase 2 writes
a *new* version (`…_v02.md`) that carries the reference blocks forward and adds the
scenes. If someone edits the frozen v01 after the fact, the ledger's existing SHA-drift
warning fires on its own — which is, for free, the honest signal that a reference was
changed late (the Gap-1 alarm the old flow lacked).

Internally the gate carries the id **"1R"** — the reference gate, sitting one rung
before the existing dramaturgy and motion-script gates. It is enforced from EP10 onward;
earlier episodes predate the flow and are exempt by design, exactly as the other
data-recorded gates handle their own cutover. The honest limit of the gate is stated
plainly at the end of this page.

---

## Phase 2 — write the scenes against the pixels

Phase 2 opens the approved reference PNGs and only then writes scene prompts. It carries
five obligations.

**1. Batch verification first.** Before writing a single prompt, read every approved
reference and walk *all* scenes against the pixels and the coverage map. Collect every
gap — a missing space, a missing character reference, a location that needs splitting —
into **one** loop-back batch. No mid-authoring interruptions; find the holes once, up
front.

**2. Re-anchor to the story, not the image alone.** Re-read the approved dramaturgy and
the Art Direction Locks first. Each scene's dramaturgy reference is a cited pointer back
into the approved breakdown, not a fresh paraphrase invented from staring at the
picture. The episode-wide rules — gaze discipline, the open beside-space, the color
band, the amber budget — are named in each scene's notes where they bind.

**3. The ref-less scene gate.** Scenes with no environment reference — the fourth-wall
close-ups, the macros, the tracking shots — cannot be "framed to pixels," so they are
checked instead against their **dramaturgy grammar obligations**, explicitly and by
name. This closes Gap 3: the shots that carry the emotional payload are the ones now
signed off most deliberately against the story, not the ones quietly skipped.

**4. A per-space camera ledger.** The output carries a table — `space | ref | scene |
camera position & heading | landmark screen-side` — so a geography contradiction across
scenes (the mountain on the left in one shot and the right in the next) is visible on
one screen instead of discovered in the edit.

**5. Loop-back, with an honest termination bound.** If batch verification found a gap,
the fix is a mini-Phase-1: prompt the new reference, a human generates and approves it,
a dated note records it. A new reference must carry its parent location's through-anchors
and narrative anchors and must be checked against the dramaturgy's own location text —
it may add a *sub-space*, it may **not** invent a new *place*. REF B's "European castle"
is the cautionary tale: a drift into a place the story never named. The loop terminates
because the measure is the count of not-yet-framed scenes, which strictly decreases;
the bound is the scene count itself. Decomposition may split a space and *grow* the
reference set, but it can never grow the set of unframed scenes — so the loop cannot run
forever.

Phase 2's output is the `…_v02.md`: reference blocks carried forward, every scene
written and framed, geometry notes rewritten wherever the real pixels diverged from the
authoring spec.

---

## The sentinel: PENDING is a designed state

A Phase-1 file has no scenes. Left unexplained, that looks exactly like an abandoned
draft — and a validator that cannot tell the two apart would either wave through every
half-finished file or block every legitimate Phase-1 deliverable. So the Phase-1
document ends with an explicit sentinel where the scenes will later go:

```
## SCENES — PENDING (PHASE 2)

> STATUS: this is a valid, designed Phase 1 deliverable, not an unfinished draft.
> Reference prompts above are authored and human-approved; scene prompts are intentionally
> not written yet. They are authored in Phase 2, framed against the REAL reference images
> once a human has generated and approved them. Why: docs/two-phase-visual-prompts.md
>
> SCENES_STATUS: PENDING_PHASE_2
```

The human-facing block says what the state means. The last line is the machine token.
The validator reads it and reports a **partial pass** — "Phase 1 only: N reference
prompts validated, 0 scenes (pending)" — running the suffix, forbidden-aesthetic, and
hygiene checks over the reference prompts while honestly skipping the scene-level checks
there are no scenes for. The token is designed to be unmistakable in both directions: a
Phase-1 file with the token and zero scenes passes as partial; a file with the token
*and* scenes fails as a stale sentinel; a file with no scenes and no token fails as a
refs-only false green. The one state that used to slip through — "no scenes, looks
done" — can no longer be mistaken for finished work.

---

## The honest reproducibility line

There is a limit here that the repo refuses to paper over.

> The repo tracks the ref PROMPT + geometry note — the reproducible spec. It does not
> track the pixels. Your fork generates its own refs from the same prompt; they will
> differ; Phase 2 frames to YOURS. Process reproducible; assets, deliberately, not.

The reference images live in `raw/`, which is gitignored — they are far too large for
version control, and they are the one thing a fork *should* regenerate for itself. What
git carries is the *recipe*: the reference prompt and the geometry note that describes
the space. Run the recipe in your own universe and your crossroads will not be this
crossroads. Phase 2 frames your scenes to your pixels, not ours. The method transfers
exactly; the assets, by design, do not.

---

## What this still cannot promise

The two-phase split makes framing *structural* — it is no longer an optional pass that
gets skipped. But two of the judgments at its heart remain human, and the repo names
them as gaps rather than claiming a coverage it does not have (the honesty discipline of
[`../_management/invariant_coverage_matrix.md`](../_management/invariant_coverage_matrix.md)).

- **Scene↔space completeness is a human call.** Whether every scene's reference anchors
  the *same physical space its dramaturgy describes* — and no scene is quietly mapped to
  a neighbor's reference — is judged by the gate's human approver against the approved
  dramaturgy. No function decides whether a space *is* the space the story meant.

- **Framing to real pixels is a human call.** Phase 2 makes the act of framing
  structural, but the *judgment* that a prompt genuinely matches the approved image is a
  person looking at both. The machine can enforce that Phase 1 happened before Phase 2;
  it cannot look at a picture and certify the words fit it.

And the gate itself is honest about its reach. A recorded 1R attests that a human
approved the reference **prompts** — the spec the repo can hold. It cannot verify the
**pixels**, because the pixels live in gitignored `raw/` and never enter CI. This is the
same preventive-at-the-skill, detective-at-CI posture as the other two gates: the
structure is enforced, the taste is human, and the repo says exactly which is which.

---

*Related: the reference-first principle this builds on lives in
[ADR-0007](../_management/adr/0007-reference-first-or-pay-the-reshoot-tax.md); the
gate-as-data pattern in
[ADR-0008](../_management/adr/0008-approval-gates-as-data.md); the whole stage in
context in [anatomy-of-an-episode.md](anatomy-of-an-episode.md), Stage 6.*
