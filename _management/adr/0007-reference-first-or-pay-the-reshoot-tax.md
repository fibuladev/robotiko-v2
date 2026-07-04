# ADR 0007 — Reference-first, or pay the reshoot tax

- **Status:** Accepted (2026-06-29)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Visual Production

## Context

EP09 needed far more visual reshooting than any prior episode — nearly every
scene had to be rescued by hand (8-10 regenerations each), where EP01-EP08 hit
roughly 80-90% first-pass. A retrospective found a single root cause, not many.

EP09 is the most visually-novel episode in the series: it introduces the **Phase 3
kintsugi body** (never rendered before), a **new location** (the workshop interior
*and* its exterior), a **mid-episode body transition** (damaged → kintsugi at S27),
and a **new group** (the curious onlookers). And its scene prompts were authored
and generated **before the reference images for those new elements existed**:

- `android_kintsugi.png` did not exist — so every gold-body scene was conjured from
  long text on the *damaged* reference, the wrong base. That fight is the 8-10x
  reshoot tax.
- The exterior (`ep09_ref_exterior.png`) did not exist — so S36-S38 drifted.
- The onlookers group had no reference — so S04 became a generic stadium crowd.

EP01-EP08 succeeded because their references already existed; the generator had a
solid anchor. EP09 inverted the pipeline's first principle: **generate the
reference, THEN write/generate scenes against it.**

## Decision

1. **Reaffirm reference-first as the pipeline's first principle.** Step 0 of the
   visual-prompts skill must produce **all** of an episode's new references — new
   body states, new locations, new groups — before scene prompts are authored or
   generated. A scene must frame to a reference that exists ([ADR 0001](0001-phase-reference-map-source-of-truth.md),
   visual-prompts Rules 4b/4c), not conjure it from text.

2. **Enforce it with a machine check.** `check_reference_first` (in
   `visual_prompt_validator.py`) fails when an episode has Robotiko scenes in a
   phase whose dedicated reference is null in `reference_images`, or declared but
   missing on disk. It would have caught EP09 on day one (kintsugi scenes, null
   kintsugi path). Wired into `run_all.py` / CI; covered by both-directions
   meta-tests.

3. **Prompts may evolve after the visual-prompts stage.** The flow is iterative:
   discovering at image-generation time that a prompt needs the inline-reference
   format, a tighter frame, or a base image, and going back to update it, is
   **healthy, not failure**. The repo holds the version we learned our way to; the
   build-along shows how we got there.

## Consequences

- The kintsugi-class root cause cannot recur silently — CI blocks an episode that
  has scenes for a body state with no reference.
- New episodes front-load reference generation, restoring the 80-90% first-pass
  rate. The reshoot tax was a one-time cost of new visual territory + an inverted
  order, not a property of the pipeline.
- The honest version of this story is itself the most valuable lesson of the
  build-along (see the EP09 Part 05 framing) — the cost of skipping reference-first,
  shown live.

**Note on empirical claims (2026-07-04):** The "80-90% first-pass" and "8-10x reshoot" figures are experiential observations from the director's production notes, not instrumented telemetry. No automated retry logging exists. Raw folders in `04_visuals/raw/` contain unnumbered generation attempts but are not systematically labeled. Future episodes may adopt a lightweight attempt-log convention: an `attempts.md` file in each `raw/` folder noting the attempt count per scene.
