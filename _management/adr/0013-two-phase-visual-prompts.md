# ADR 0013 — Two-phase visual prompts: scenes are framed to approved pixels

- **Status:** Accepted (2026-07-07)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** Visual-Prompts Pipeline Redesign

## Context

The visual-prompts skill wrote reference prompts **and** every scene prompt in one
pass, against a text contract (the Environment Geometry note), and generated the
reference IMAGES *afterward*. A "Framing Pass" was supposed to reconcile the scenes
to the real pixels once they existed — but it was explicitly "never a blocker," so
in practice it was skipped. Reference-first ([ADR 0007](0007-reference-first-or-pay-the-reshoot-tax.md))
was a stated principle that nothing structurally enforced.

Three gaps compounded:

- **GAP A — the artifacts drifted.** The template, `_assets/style/visual_dna.md`, and
  the public docs were a generation behind the SKILL; the story they told no longer
  matched what the skill did.
- **GAP B — a late ref edit forced no scene re-verification.** The REF B reframe
  (2026-07-07 / commit `ea96c34`) rewrote a reference block's note while the 40 scenes
  bound to that space were never re-checked against it. Editing a note is not the same
  as reconciling the scenes.
- **GAP C — locations were under-decomposed.** Step 0's "3+ scenes = 1 ref" heuristic
  collapsed distinct camera spaces into a single reference; EP10's REF E/F were found
  late, by luck rather than by process.

The root cause is ordering: scenes were authored against a text description of a
reference that did not yet exist, and nothing made the pipeline stop and wait for the
real image.

## Decision

**Split the skill into two phases with a hard human gate between them, and record the
gate as data.**

1. **Phase 1 — Reference Authoring** produces a complete `ep{XX}_visual_prompts_v01.md`:
   a location decomposition (an operational site-map + landmark-consistency test that
   replaces the "3+ scenes" heuristic — closes GAP C), every new reference prompt
   (environments AND character/group body states), the ART DIRECTION LOCKS, a
   scene→space coverage map, and a Phase-1 sentinel. **Zero scene prompts.**

2. **⛔ Hard stop — gate 1R (references approved).** The human generates the reference
   IMAGES into gitignored `raw/`, iterates freely, and approves. Approval is recorded
   as a ledger entry in `_management/approvals.json`. This reuses the
   [ADR 0008](0008-approval-gates-as-data.md) "gates as data" pattern verbatim: `"1R"`
   is a new gate id in the **same** ledger, alongside gate 1 (dramaturgy) and gate 2
   (motion script). Phase 2 cannot begin until 1R clears.

3. **Phase 2 — Scene Authoring Against Real Pixels** writes
   `ep{XX}_visual_prompts_v02.md`: every scene is born framed to a reference image that
   already exists and was approved. Its opening move is a batch verification pass — read
   all approved PNGs, walk every scene against the pixels + the coverage map, and collect
   every gap into ONE loop-back batch. This structurally delivers what ADR 0007 asked
   for: a scene frames to a reference that EXISTS, not one conjured from text.

The resolved sub-decisions:

- **D3 — Versioning: frozen v01 + new v02.** Phase 1 ships v01 (refs + locks + map +
  sentinel; zero scenes); gate 1R sha-pins it and its bytes are then FROZEN. Phase 2
  ships v02 (REF blocks carried forward with Environment Geometry notes rewritten to the
  approved pixels, scenes added, sentinel removed). Each version stays a complete
  document. No new routine stale-WARN is introduced: a late edit to the frozen v01 simply
  trips the existing ADR-0008 sha-drift WARN — which becomes the honest **GAP-B
  late-ref-edit signal for free.**

- **D4 — The honest limits of gate 1R.** 1R attests that a human approved the reference
  PROMPTS and signed off the images they generated. The images live in gitignored `raw/`
  and are not machine-verifiable — so the gate is **preventive at the SKILL layer,
  detective at CI**, the same posture as gates 1 and 2. The EP10 v01 (authored before this
  redesign) is admitted by ONE waiver pinned to the v01 artifact and its sha. Because the
  waiver is bound to that specific artifact, it **cannot excuse the future v02** — the
  generic episode-scoped waiver is deliberately NOT reused. A legacy waiver can
  therefore never permanently disarm the gate: it holds only while it pins the latest
  artifact, and the real v02 will demand its own 1R record.

- **D6 — Under-segmentation lint: DECLINED.** Semantic under-decomposition (one reference
  quietly covering two real spaces) is not cleanly machine-judgeable; every cheap proxy
  false-positives on legitimately wide-but-valid spans. Rather than ship a lint that cries
  wolf, this is declared honestly as a 🔵 Human GAP in the coverage matrix. The one cheap
  check that IS worth it — a Reference-Image-Path field lint on tracked REF blocks — ships;
  the semantic judgement stays with the human.

- **The loop-back termination measure (corrected).** When Phase 2 discovers a missing
  space or character reference, it loops back (author prompt → human generates → approves
  → dated note). Because GAP-C decomposition can *split* one space into several, the
  reference set can GROW during loop-back — so the termination measure is NOT "spaces
  remaining." The sound measure is the **count of not-yet-framed scenes, which strictly
  decreases each iteration; the bound is the scene count.** The ref set may grow; the
  unframed-scene set never does.

- **The honest +1-session cost.** This flow costs one additional formalized session
  versus the old single pass. That is not new overhead — it is the Framing Pass debt
  finally paid on the table instead of skipped. In exchange it **buys back the ADR-0007
  reshoot tax** (EP09's 8-10x regenerations on scenes conjured from text against the wrong
  base). One deliberate gate is cheaper than the EP09-scale reshoot tax.

## Consequences

- The GAP-B failure that motivated the redesign cannot recur silently: a reference edited
  after Phase 2 begins triggers the backstop rule (every scene in that reference's
  coverage-map row is re-verified before delivery), and a late edit to the frozen v01
  surfaces as the sha-drift WARN.
- Reference-first (ADR 0007) graduates from a principle the validator checks after the
  fact to a **structural property of the workflow** — Phase 2 literally cannot frame a
  scene to an image that does not exist.
- The approval ledger (ADR 0008) gains a third gate id (`1R`) with no new machinery: the
  same sha-pinning, missing-record-FAIL, stale-WARN, and waiver idioms apply.
- New enforcement is honest about its reach: `check_phase_state` distinguishes an
  intentional Phase-1 file (partial pass) from a refs-only false green; the 1R check is
  preventive/detective, not a pixel verifier; two judgements (scene↔space completeness,
  framing-to-real-pixels) are declared 🔵 Human GAPs rather than faked in code.
- **The honest limit (stated plainly):** the machinery proves a Phase-1 file is
  intentional and that a 1R record exists; it does NOT prove the approved references
  actually match the dramaturgy's spaces, nor that Phase 2 framed each scene to the right
  pixels. That judgement is the human completeness check at the gate — 🔵 Human, by design.
- Cutover is EP10-onward (`TWO_PHASE_FROM_EP = 10`); EP01-EP09 are exempt as a documented
  legacy shape, so there are no perpetual WARNs and no ledger churn. EP10's v02 production
  run — the flow's first live use — is a separate session.
