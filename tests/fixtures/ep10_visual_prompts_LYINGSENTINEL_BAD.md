# EP10 — VISUAL PROMPTS (FROZEN LYING-SENTINEL BAD FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** The scenes ARE written, but
> the author forgot to remove the Phase-1 scene-pending sentinel. A file that both
> carries the sentinel AND parses scenes is a contradiction — the sentinel is stale.
> The validator MUST FAIL this file on the phase-state check (stale sentinel). Every
> other check on the single scene is clean, so the ONLY error is the stale sentinel.
> See tests/fixtures/README.md.

---

## MANDATORY STYLE SUFFIX

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## SCENES — PENDING (PHASE 2)

> STATUS: this is a valid, designed Phase 1 deliverable, not an unfinished draft.
> Reference prompts above are authored and human-approved; scene prompts are intentionally
> not written yet. They are authored in Phase 2, framed against the REAL reference images
> once a human has generated and approved them. Why: docs/two-phase-visual-prompts.md
>
> SCENES_STATUS: PENDING_PHASE_2

---

## GENERATED PROMPTS

---

#### Scene S30 - The Meadow, Beside

- **Timestamp:** 3:30-3:45
- **Dramaturgy Reference:** Robotiko sits beside the toppled infinity stone in the green meadow; the beside-space open.
- **Characters Present:** Robotiko (Phase 3, full kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Eye-level, beside-space open to the right, meadow ahead.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png`

**Text Prompt:**
> Eye-level wide shot, a chrome android seated in a green morning meadow beside a great toppled stone figure-eight lying in the grass, patchwork chrome body repaired with mismatched rusted scrap metal, gold-filled seams, translucent digital skin over a soft bioluminescent core, calm steady blue optical lenses set into chrome sockets like polished sapphires, missing right ear, torso dent, the beside-space open in the grass to his right, warm morning gold, tall monolith mountains behind, low horizon under a big open sky, 16:9 widescreen composition, single figure composition no additional characters, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
