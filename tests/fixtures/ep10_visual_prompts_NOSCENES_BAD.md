# EP10 — VISUAL PROMPTS (FROZEN NOSCENES BAD FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** It is the refs-only FALSE
> GREEN the phase-state gate exists to catch: reference prompts are present but there
> are ZERO scene prompts AND no Phase-1 sentinel declaring that state as designed.
> Without the gate, every text check passes over a file that checks nothing
> scene-level. The validator MUST FAIL this file on the phase-state check. See
> tests/fixtures/README.md.

---

## MANDATORY STYLE SUFFIX

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## REFERENCE IMAGES (Step 0 — generate BEFORE any scene prompt, ADR-0007)

---

### REF A: Toppled-Infinity Stone in Green Meadow (recurring)

**Design Brief:** The monolith country, now green with morning. The great stone figure-eight lies in the grass as an infinity shape — ordinary.

**Environment Geometry:** Eye-level camera. The stone loops lie across the mid-ground; monolith mountains behind; low horizon, big warm sky.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_stone_meadow.png`

**Text Prompt:**
> Wide establishing shot of a green meadow at full morning in old monolith mountain country, no characters, a great toppled stone figure-eight lying in the grass as an infinity shape of two joined stone loops, mossed and split by old weather, tall monolith mountains standing in the background, morning mist burning off the valley floor beyond, warm morning gold, eye-level camera, low horizon under a big open sky, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF C: Ridge Moon-Sun Sky (recurring)

**Design Brief:** A pale full Moon still hanging while the Sun rises, both in the same real dawn sky.

**Environment Geometry:** Sky fills roughly 80% of the frame. Moon pale-full on the left, Sun newly risen on the right; a low ridge line with grass along the bottom edge.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_moonsun_sky.png`

**Text Prompt:**
> Wide establishing sky shot from a high open ridge above a distant town, no characters, the dawn sky filling roughly eighty percent of the frame, a pale full Moon hanging low on the left side and a newly risen Sun standing on the right side, cool Moon-light on the left and warm Sun-light on the right meeting at peace, a low ridge line with grass along the bottom edge, a big open sky above, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## GENERATED PROMPTS

_(none — the author stopped here and shipped, forgetting both the scenes and the Phase-1 sentinel; this is the false green the gate catches.)_
