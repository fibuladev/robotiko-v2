# EP09 — VISUAL PROMPTS (FROZEN BROKEN FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** It freezes the real
> EP09 v01 reference-integrity bug: a damaged/kintsugi-body episode that attaches
> Robotiko's PRISTINE reference (`ref_robotiko_master.png`) to every scene, and
> uses the "only ONE chrome android" phrasing that backfires in Nano Banana.
> The validator suite MUST fail ref-integrity on this file. See tests/fixtures/README.md.

---

## MANDATORY STYLE SUFFIX

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

#### Scene S01 - The Myth
- **Timestamp:** 0:00-0:14
- **Dramaturgy Reference:** Low worshipper's-eye angle. Robotiko descends toward camera. Cold sun as false halo. Silhouette - the savior image.
- **Characters Present:** Robotiko (@Damaged - silhouette only, damage not visible)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Low angle. Leave headroom above the figure for the halo effect. Space below for the descending path. The figure occupies the upper-center third.
- **Upload:** char: `ref_robotiko_master.png` (proportions guide for silhouette)

**Text Prompt:**
> Low angle looking up from ground level, a chrome android descending a grey barren rocky path toward the camera, visible as a dark silhouette against a pale cold sun directly behind creating a false halo effect, arms slightly apart, silhouette appears whole and radiant, grey overcast sky, barren grey-brown rocky terrain falling away behind the figure, cold desaturated palette, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S02 - The Puncture
- **Timestamp:** 0:15-0:26
- **Dramaturgy Reference:** Camera pulls back. Halo = flat daylight. Body broken: rusted, missing ear, torso dent. The lens undoes the sacred image.
- **Characters Present:** Robotiko (@Damaged, full body revealed)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium-wide. The figure occupies the center third. Blurred indistinct shapes below on the path. Space on both sides for the pulled-back composition.
- **Upload:** char: `ref_robotiko_master.png` · chain: S01 output

**Text Prompt:**
> Medium-wide shot, a chrome android standing on a grey barren rocky path, full body revealed in flat overcast daylight, battle-scarred rusted chrome, missing right ear with exposed wires at the ear socket, a deep dent gouged into the torso, shoulder scratches, calm steady blue eyes, the false halo gone, grey desaturated terrain stretching behind, cold palette, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S27a - The Glitch Is Scripture (Start Frame)
- **Timestamp:** 4:09-4:28
- **Dramaturgy Reference:** CAMERA STOPS. Robotiko presses scrap to chassis - first gold hairline in a single crack. Phase 2 to Phase 3 transition begins.
- **Characters Present:** Robotiko (@Damaged to first gold)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B) - this is the START frame.
- **Composition Notes:** Medium-wide, STATIC. Robotiko left of center at bench. Scraps on bench surface. The single gold hairline is the brightest element.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S26 output

**Text Prompt:**
> Medium-wide shot, a chrome android seated at a workbench, battle-scarred rusted chrome, missing right ear with exposed wires, torso dent, calm steady blue eyes, one hand pressing a piece of rusted scrap metal against his cracked chassis, a thin hairline of warm gold light beginning to glow from a single crack where the scrap meets the chrome, body still fully battle-damaged, scattered scraps on the bench around him, warm low light in the workshop, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
