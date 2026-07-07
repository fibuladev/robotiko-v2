# EP10 — VISUAL PROMPTS (FROZEN PHASE-1 GOOD FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** It is a legitimate
> **Phase-1 deliverable** (ADR-0013 two-phase visual prompts): the reference prompts
> and the kintsugi body ref are authored and the scene section is intentionally
> pending behind the human ref-approval gate. The validator MUST partial-pass this
> file — print "PHASE 1 ONLY" and exit clean — NOT report a false green. See
> tests/fixtures/README.md.

---

## MANDATORY STYLE SUFFIX

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## REFERENCE IMAGES (Step 0 — generate BEFORE any scene prompt, ADR-0007)

---

### REF K: Kintsugi Body (Phase 3 — chained into every Robotiko scene)

**Design Brief:** The full Phase-3 body reference. A character/group ref, so it is gated and pseudo-scene linted (eye-glow + phase) even though no scene exists yet.

**Environment Geometry:** Not applicable — neutral character reference on a dark background.

**Narrative anchors:** The body is complete and worn as ordinary skin; no damage progression across the episode.

**Reference Image Path:** `episode-10/04_visuals/raw/ep10_ref_kintsugi_body.png`

**Text Prompt:**
> Full-body character reference of a chrome android, Phase 3 full kintsugi, patchwork chrome repaired with mismatched rusted scrap metal, gold-filled seams, translucent digital skin over a soft bioluminescent core, calm steady blue optical lenses set into chrome sockets like polished sapphires, missing right ear, torso dent, shoulder scratches, neutral dark background, 16:9 widescreen composition, single figure composition no additional characters, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF A: Toppled-Infinity Stone in Green Meadow (recurring)

**Design Brief:** The monolith country, now green with morning. The great stone figure-eight fell long ago and lies in the grass as an infinity shape — ordinary. No monument framing, no light from within the stone.

**Environment Geometry:** Eye-level camera. The two joined stone loops lie across the mid-ground, near loop toward the camera; monolith mountains behind; low horizon, big warm sky; open meadow foreground for the beside-space.

**Narrative anchors:** Beside-space kept open in the meadow foreground; prophecy has become furniture.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_stone_meadow.png`

**Text Prompt:**
> Wide establishing shot of a green meadow at full morning in old monolith mountain country, no characters, a great toppled stone figure-eight lying in the grass as an infinity shape of two joined stone loops, mossed and split by old weather, half-sunk in the meadow grass, utterly unremarkable, tall monolith mountains standing in the background, morning mist burning off the valley floor beyond, warm morning gold, eye-level camera, the stone lying across the mid-ground with the near loop toward the camera, low horizon under a big open sky, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF C: Ridge Moon-Sun Sky (recurring)

**Design Brief:** The film's one wide-sky passage — a pale full Moon still hanging while the Sun rises, both in the same real dawn sky, both temperatures at peace.

**Environment Geometry:** Sky fills roughly 80% of the frame. Moon pale-full on the left (cool), Sun newly risen on the right (warm); both persistent. A low ridge line with grass along the bottom edge for a small walking figure.

**Narrative anchors:** The series epigraph resolved by an ordinary morning; room along the ridge for the beside-space.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_moonsun_sky.png`

**Text Prompt:**
> Wide establishing sky shot from a high open ridge above a distant town, no characters, the dawn sky filling roughly eighty percent of the frame, a pale full Moon hanging low on the left side and a newly risen Sun standing on the right side, both present in the same real dawn sky, cool Moon-light on the left and warm Sun-light on the right meeting at peace, a low ridge line with grass along the bottom edge, a big open sky above, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## REFERENCE IMAGE UPLOAD GUIDE

| Scene(s) | Camera-space | Body ref |
|---|---|---|
| S18, S24-S34 | REF A stone meadow | `ep10_ref_kintsugi_body.png` |
| S15-S18 | REF C ridge sky | `ep10_ref_kintsugi_body.png` |

---

## SCENES — PENDING (PHASE 2)

> STATUS: this is a valid, designed Phase 1 deliverable, not an unfinished draft.
> Reference prompts above are authored and human-approved; scene prompts are intentionally
> not written yet. They are authored in Phase 2, framed against the REAL reference images
> once a human has generated and approved them. Why: docs/two-phase-visual-prompts.md
>
> SCENES_STATUS: PENDING_PHASE_2
