# EP10 — VISUAL PROMPTS (FROZEN QUOTED-SENTINEL GOOD FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** It is a complete document
> (scenes present) that also QUOTES the Phase-1 sentinel token inside a fenced code
> block — e.g. a changelog note explaining the two-phase flow. Because the detector
> strips fenced code blocks before looking for the sentinel, the quoted token is NOT
> read as a live sentinel: the file has scenes and no live sentinel, so it takes the
> normal full-validation path and MUST PASS clean. See tests/fixtures/README.md.

---

## MANDATORY STYLE SUFFIX

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## CHANGELOG NOTE (quoted, not live)

This v02 document was written in Phase 2. Its Phase-1 predecessor carried the
scene-pending sentinel, which looked like this and was removed here:

```
## SCENES — PENDING (PHASE 2)
> SCENES_STATUS: PENDING_PHASE_2
```

The token above lives inside a fence, so it is a QUOTE, not a live sentinel.

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
