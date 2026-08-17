# ADR 0007 — Reference-first, or pay the reshoot tax

- **Status:** Accepted (2026-06-29)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Visual Production

## Context

EP09 needed far more visual reshooting than any prior episode — nearly every
scene had to be rescued by hand (8-10 regenerations each), where EP01-EP08 hit
roughly 65-70% first-pass for images. A retrospective found a single root cause, not many.

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
- New episodes front-load reference generation, restoring the ~65-70% image
  first-pass rate (~80% for video from approved images). The reshoot tax was a
  one-time cost of new visual territory + an inverted order, not a property of
  the pipeline.
- The honest version of this story is itself the most valuable lesson of the
  build-along (see the EP09 Part 05 framing) — the cost of skipping reference-first,
  shown live.

**Note on empirical claims (2026-07-10):** The "65-70% image first-pass" and "~80% video first-pass" figures are experiential observations from the director's production notes, not instrumented telemetry — image generation is where the universe is created (dense prompts + reference images can confuse the tools); video generation from a strong image is far more predictable. No automated retry logging exists yet. Raw folders in `04_visuals/raw/` contain unnumbered generation attempts but are not systematically labeled. EP10 adopts a mandatory attempts ledger (`attempts.md` in each `raw/` folder) so the number starts being measured.

---

**Update (2026-08-18):** The attempts ledger was never adopted. No `attempts.md` exists
anywhere in the tree — not in EP10's `raw/` folders, not in any other episode — and
`tests/attempts_report.py` describes the ledgers as "a future convention, not a backfill
obligation" rather than as shipped practice. The reshoot tax therefore stayed
**unmeasured** through EP10: read the 8-10x regeneration figure above as the director's
production-note estimate it always was, not as an instrumented number. Separately, the
build-along "Part 05" material referenced in the Consequences is not part of the public
tree, so that pointer is to the published video series, not to a file in this repo.
