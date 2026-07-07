<!-- NOTE: this fixture deliberately keeps a scaffold marker: auto-populated by Claude -->
# EP10 — VISUAL PROMPTS (FROZEN BAD-SENTINEL BAD FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** It carries BOTH the Phase-1
> scene-pending sentinel AND a scaffold template marker ("auto-populated by Claude",
> above). Before the run_full reorder, `is_unfilled_template` would have swallowed
> this file into the silent scaffold-skip path — a Phase-1 deliverable never
> validated. After the reorder (sentinel checked FIRST), the file is validated, and
> its real defect surfaces: REF Q's Text Prompt is MISSING the mandatory style suffix.
> The validator MUST FAIL this file (proving it was not silently skipped). See
> tests/fixtures/README.md.

---

## MANDATORY STYLE SUFFIX

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## REFERENCE IMAGES (Step 0 — generate BEFORE any scene prompt, ADR-0007)

---

### REF Q: Ridge Moon-Sun Sky (recurring)

**Design Brief:** A pale full Moon still hanging while the Sun rises, both in the same real dawn sky.

**Environment Geometry:** Sky fills roughly 80% of the frame; a low ridge line with grass along the bottom edge.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_moonsun_sky.png`

**Text Prompt:**
> Wide establishing sky shot from a high open ridge above a distant town, no characters, the dawn sky filling roughly eighty percent of the frame, a pale full Moon hanging low on the left side and a newly risen Sun standing on the right side, a low ridge line with grass along the bottom edge, a big open sky above, 16:9 widescreen composition.

---

## SCENES — PENDING (PHASE 2)

> STATUS: this is a valid, designed Phase 1 deliverable, not an unfinished draft.
> Reference prompts above are authored and human-approved; scene prompts are intentionally
> not written yet. They are authored in Phase 2, framed against the REAL reference images
> once a human has generated and approved them. Why: docs/two-phase-visual-prompts.md
>
> SCENES_STATUS: PENDING_PHASE_2
