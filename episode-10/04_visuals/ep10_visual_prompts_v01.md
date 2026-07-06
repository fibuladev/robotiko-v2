# EP10 — VISUAL PROMPTS
> **Version:** v01 | **Generated:** 2026-07-06
> **Skill:** `_skills/robotiko-visual-prompts/SKILL.md`
> **Inputs:** Approved `ep10_dramaturgy_v01.md` (Gate-1, 2026-07-06), `master.md`, `character_profiles.json`, `ep10_musical_metadata.json`, `ep10_concept_notes.md`

---

## PRE-GENERATION CHECKLIST

- [x] `_management/master.md` — Visual DNA, color palette, forbidden list, mandatory suffix (Sec. 3)
- [x] `episode-10/03_direction/ep10_dramaturgy_v01.md` — APPROVED scene breakdown (35 scenes, S35 = edit card)
- [x] `_assets/cast/character_profiles.json` — Phase 3 full kintsugi, `phase_reference_map` → kintsugi for EP10
- [x] `_assets/cast/android_kintsugi.png` — Phase 3 body reference (chain from this file for EVERY scene)
- [x] EP09 dawn-exterior lineage (`episode-09/04_visuals/ep09_ref_exterior.png` + EP09 final dawn frames) — S01–S02 chain
- [x] `_assets/cast/ref_mentor_master.png` — NOT USED as a figure (Mentor is GONE); the staff object only (S09–S10)

---

## CHARACTER REFERENCE — CRITICAL NOTE

EP10 is **Phase 3, full kintsugi, stable from frame one** — no damage progression, no transformation beats. `phase_reference_map.default_by_phase["3"]` = **kintsugi** → chain every Robotiko scene from **`_assets/cast/android_kintsugi.png`**.

- **Do NOT** use `ref_robotiko_master.png` (pristine Phase 1) or `android_damaged.png` (Phase 2). Either would break continuity.
- **The kintsugi reference carries the body detail** (patchwork chrome, gold-filled seams, translucent skin over the bioluminescent core, calm steady blue optical lenses, missing right ear, torso dent). Per the reference-brevity rule, the prompts use the short identifier **"the chrome android (android_kintsugi.png)"** and do NOT restate that detail. Describe only what is NOT in the reference (a new light state, a gaze direction, a pose).
- **S01–S02 exterior:** chain from EP09's dawn-exterior lineage (`ep09_ref_exterior.png` / EP09 final dawn frame `episode-09` raw `5.png` family) so the workshop and industrial-edge town read identically to EP09's last frames — S01 is "exactly where EP09 left the world," S02 is EP09's final image reversed.
- **Eye canon (ADR-0010):** material-lens idiom ONLY in every Text Prompt — `calm steady blue optical lenses set into chrome sockets, like polished sapphires`. Never "glow" within reach of an eye/lens word. Kintsugi **body** gold-glow is allowlisted (seams may "glow gold"); the eyes never do.
- **Mouthless-face guard (verified against `android_kintsugi.png`):** the face has NO mouth. Never prompt a smile, grin, teeth, or mouth in any scene — warmth (esp. S34) is carried by head tilt, beckoning hand, and the held gaze. Any take that invents a mouth is a reject.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP10 |
| **Title** | The Glitch Scripture / I Came to Walk Beside |
| **Station** | The Integrated Self — Arrival (Enlightenment. 8 → ∞) |
| **Character Phase** | Phase 3: Reconstruction (full kintsugi — complete, worn as ordinary skin) |
| **Robotiko Visual State** | Patchwork chrome body repaired with mismatched rusted scrap metal, translucent digital skin over a bioluminescent core, cracks filled with glowing gold light, calm steady blue optical lenses set into chrome sockets like polished sapphires. Right ear missing, torso dent, shoulder scratches carried; inner-forearm etchings present but **never featured, never lit, never framed**. |
| **Camera Personality** | THE COMPANION CAMERA — alongside, never above; the reserved beside-space kept open in every frame (lineage finale: EP07 Retreating → EP08 Witnessing → EP09 Discovering → EP10 Companion). |
| **Reference (body)** | `_assets/cast/android_kintsugi.png` — chain for every scene |
| **Total Scenes** | 35 (34 image-generated + S35 edit card) |
| **Total Prompts** | 44 (40 scene prompts incl. S02a/b, S08a/b/c, S10a/b, S27a/b, S34a/b; S35 = no image) + 4 reference-image prompts |

---

## MANDATORY STYLE SUFFIX
> This suffix is appended to EVERY prompt. No exceptions. No modifications.

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## FORBIDDEN AESTHETICS REMINDER

- Clean Apple design
- Pixar-style rendering
- Generic cyberpunk neon glow
- Smooth plastic textures
- Cheap melodrama or ornamental excess

---

## ART DIRECTION LOCKS (EP10)

- **Camera personality — THE COMPANION CAMERA.** The reserved beside-space (recommended his RIGHT — the wounded/missing-ear side worn openly toward the companion) is kept open in every composition. Never frame from above him (no high-angle, no crane-down on Robotiko; crane may serve sky/landscape only). Deviations require Director's Notes justification.
- **Color journey — self-made gold → indistinguishable from sunrise.** Intro: his gold distinct in pre-dawn grey-blue (S01–S03). Verses/climb: the world's warmth rises to meet his; grass-gold and seam-gold converge (S13–S18). Meadow/finale: one warmth — kintsugi seams read as ordinary highlights (S30 onward). Kodachrome warm bias throughout; heavy grain constant, never crescendoing.
- **The single Amber Pulse — S10 ONLY.** Reflected sunlight on the staff's raw amber tip; a warm glint, never a light source. NO amber anywhere else in the episode. Embers (S21, S25–S26) are **orange-red**, never amber.
- **Environmental rules — one road, one dawn.** Continuous geography, continuous time (pre-dawn grey-blue → early golden hour). No flashbacks, no cosmic sets, no teleports, no rain/storm/night. CyberAnatolian texture stays background, never foregrounded.
- **Body — full kintsugi from frame one, stable.** No damage progression, no transformation beats. Chain from `android_kintsugi.png`.
- **What is NOT shown:** the stone 8 standing or transforming; the Mentor embodied or projected; Robochica in any form; the Mechanic; the workshop interior (S02 doorway stays pure unreadable light); any screen-world / virtual space; any monument framing of the ∞ stone; eye contact before S34; any lemniscate / path-shape reveal; **any invented mouth on Robotiko**.
- **Gaze discipline:** the ONLY direct look into the lens is S34a. S27 (the offered hand) and S31 (the wait) keep the gaze BELOW / BESIDE the lens — any eye-contact take there is a reject.
- **Composition for motion:** every frame leaves headroom + the open beside-space + fore/background depth for the motion stage; cuts land on the felt stomp-clap pulse (76.5 BPM, beat = footstep). No camera-movement words in prompts (angle/placement only).

---

## REFERENCE IMAGES (Step 0 — generate BEFORE any scene prompt, ADR-0007)

Reference-first is mandatory this episode (EP10 = last first-pass-yield measurement window). Generate all four below, confirm each against its Environment Geometry note in a Framing Pass, then generate scenes.

---

### REF A: Toppled-∞ Stone in Green Meadow (recurring — S18 distant, S25–S29, meadow identity S30–S34)

**Design Brief:** The EP01 monolith country, now green with morning. The great stone figure-eight fell long ago and lies in the grass as an infinity shape — mossed, split, half-sunk, utterly ordinary. Prophecy became furniture. NO monument framing, NO light from within the stone, NO awe.

**Environment Geometry:** Eye-level camera (the world treats the stone as a good place to sit — never low-angle). The two joined stone loops lie roughly across the mid-ground, the **near loop toward the camera**; tall monolith mountains stand in the background; the valley floor with burning-off mist opens beyond. Low horizon, big warm sky. Open meadow foreground for the beside-space.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_stone_meadow.png`
**Source rhyme:** full-res EP01 original `_curation_staging/ep01/61.png` (intact monolith — same place, new state).

**Text Prompt:**
> Wide establishing shot of a green meadow at full morning in old monolith mountain country, no characters, a great toppled stone figure-eight lying in the grass as an infinity shape of two joined stone loops, mossed and split by old weather, half-sunk in the meadow grass, utterly unremarkable and ordinary, tall monolith mountains standing in the background, morning mist burning off the valley floor beyond, warm morning gold, eye-level camera treating the stone as an ordinary place to sit, the stone lying across the mid-ground with the near loop toward the camera, low horizon under a big open sky, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF B: The Crossroads + Waymark Staff (S09–S10)

**Design Brief:** The crossroads at the **exit / upper edge of the Anatolian mountain village**, where the town's lanes give onto the climbing road toward the ridge. The Mentor's only echo: his amber-tipped staff planted upright in the earth as a waymark — dark road-worn gnarled wood, faded cloth strips tied by travelers, packed earth at its base. A waymark, not a monument. **Houses are out of frame** (the village is behind the traveler): the built texture was removed at the image stage to avoid a roof-typology clash with REF D and to give a clean highland-transition read — semi-arid **green highland scrub**, low weathered stone remnants around the central island, distant peaks, a lone hillside satellite dish (CyberAnatolian retrofit). The **amber tip is dark and dormant here** — the single Amber Pulse (reflected sunlight) is reserved for S10b, so the ref must show it unlit.

**Environment Geometry:** The staff planted roughly centre / slightly **off-centre**, leaning a little; multiple dirt tracks (the town's lanes) converge at the crossroads and the roads climb away into the misty background for depth; open semi-arid green highland all around with distant peaks on the horizon, village behind camera (no houses in frame); cool earth tones with the sun not yet reaching the crossroads (so the amber tip sits in shade until S10's sun clears the roofline). Eye-level.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_crossroads.png`
**Source rhyme:** Mentor staff canon (`ref_mentor_master.png` staff detail — staff only, no figure).
**Framing Pass note (2026-07-07):** Locked. Gen 1 drifted (glowing amber + European castle); gen 2 fixed the amber + Anatolian village; final edit **removed the background houses** so the shot reads as the village EXIT onto open highland — this sidesteps the flat-roof (REF B) vs tile-roof (REF D) clash and ties the crossroads into the green-highland world of REF C / REF A. Landscape anchor = distant peaks + highland scrub; lone retrofit dish kept. **For S10b:** the tip must still read as *amber that can catch light* when the sun flares it — dormant, not opaque wood.

**Text Prompt:**
> Wide establishing shot of a crossroads at the open upper edge of an Anatolian mountain village where the lanes give onto the climbing road, no characters, open semi-arid green highland opening ahead with rolling hills all around, multiple dirt tracks converging at the crossroads and roads climbing away into the misty background, a wooden waymark staff of dark road-worn gnarled wood planted upright in packed earth slightly off-center and leaning a little, a few small faded cloth strips tied below its head by travelers, its raw amber tip dark and dormant, a dull matte unlit amber in the cool shade catching no light, low weathered stone remnants and green highland scrub around the central island of the crossroads, a single small satellite dish on a far hillside as ordinary CyberAnatolian retrofit texture, distant sharp rocky peaks on the horizon, the earth packed by many feet with old track lines, cool earth tones with the sun not yet reaching the crossroads, morning mist in the valley, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF C: Ridge Moon-Sun Sky (S15–S18)

**Design Brief:** The film's one wide-sky passage. The series' epigraph resolved by an ordinary morning: a pale full Moon still hanging while the Sun rises, both in the same real dawn sky. Both temperatures at peace.

**Environment Geometry:** Sky fills roughly **80%** of the frame. **Moon pale-full on the left** (cool), **Sun newly risen on the right** (warm); both persistent, no drift, no scale change. A **low ridge line with grass along the bottom edge** — room for a small walking figure (S15/S17) and a crossing crane flock (S16) without touching the celestial bodies. Big open sky above.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_moonsun_sky.png`
**Note:** S16's flock is a **variant generated against this ref** (base = S15/REF C output) so the two bodies stay locked — the flock must be IN the source, never prompted to "enter frame."

**Text Prompt:**
> Wide establishing sky shot from a high open ridge above a distant town, no characters, the dawn sky filling roughly eighty percent of the frame, a pale full Moon hanging low on the left side and a newly risen Sun standing on the right side, both present in the same real dawn sky, cool Moon-light on the left and warm Sun-light on the right meeting at peace, a low ridge line with grass along the bottom edge, a big open sky above, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF D: Dawn Town Street (S03–S08, S11–S12, S19–S22)

**Design Brief:** The waking Anatolian town — narrow streets, market edge, the far edge on the descent. CyberAnatolian texture (weathered technology grown into ordinary life) present in the background but never foregrounded. The continuous world of the walk through town.

**Environment Geometry:** A narrow street **receding toward the town** (depth into the background), weathered stone-and-plaster buildings framing both sides, low rooftops. Warm sunrise light entering the lanes; palette lifts from grey-blue (S03) to full sunrise (S11–S12) to full morning on the far edge (S19–S22). Eye-level / tracking height. Beside-space open along the street.

**Reference Image Path:** `episode-10/04_visuals/ep10_ref_dawn_town.png`
**Source rhyme:** EP09 workshop-exterior lineage for continuity.

**Text Prompt:**
> Wide establishing shot of a narrow Anatolian small-town street at early sunrise, no characters, weathered stone and plaster buildings with shutters and low rooftops framing the street, ordinary weathered technology grown quietly into everyday life in the background such as a patched antenna, an old cable run and a salvaged panel, never foregrounded, the street running open and receding toward the town, warm sunrise light entering the lanes, chimney smoke and morning haze, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

**Dawn Workers (anonymous ensemble):** no dedicated character reference required (none recurs, none reacts, per dramaturgy). Generate per-scene; keep mixed men and women of varied ages, plain everyday clothes; flag if drift becomes visible.

---

## REFERENCE IMAGE UPLOAD GUIDE

| Scene(s) | Body ref | Env / chain ref |
|---|---|---|
| S01 | — (no figure) | `ep09_ref_exterior.png` + chain EP09 dawn frame |
| S02a/b | `android_kintsugi.png` (silhouette) | `ep09_ref_exterior.png` + chain EP09 dawn frame |
| S03, S04, S05, S06, S07 | `android_kintsugi.png` (S07 = none) | `ep10_ref_dawn_town.png` |
| S08a/b/c | `android_kintsugi.png` (frame c only) | — (macro) |
| S09, S10a/b | `android_kintsugi.png` | `ep10_ref_crossroads.png` |
| S11, S12 | `android_kintsugi.png` (S11 = none) | `ep10_ref_dawn_town.png` |
| S13, S14 | `android_kintsugi.png` | `ep10_ref_dawn_town.png` (S13 town below) |
| S15, S17 | `android_kintsugi.png` | `ep10_ref_moonsun_sky.png` |
| S16 | `android_kintsugi.png` | `ep10_ref_moonsun_sky.png` + base S15 output |
| S18 | `android_kintsugi.png` | `ep10_ref_stone_meadow.png` (distant) |
| S19, S20, S21, S22 | `android_kintsugi.png` | `ep10_ref_dawn_town.png` |
| S23 | `android_kintsugi.png` | — (macro) |
| S24 | `android_kintsugi.png` | `ep10_ref_stone_meadow.png` (meadow ahead) |
| S25 | `android_kintsugi.png` | `ep10_ref_stone_meadow.png` |
| S26, S27a/b | `android_kintsugi.png` | `ep10_ref_stone_meadow.png` + chain S25 |
| S28 | `android_kintsugi.png` | `ep10_ref_stone_meadow.png` + chain S26 |
| S29 | — (tracks only) | `ep10_ref_stone_meadow.png` (grass) |
| S30, S31, S32, S33 | `android_kintsugi.png` | `ep10_ref_stone_meadow.png` (meadow country) |
| S34a/b | `android_kintsugi.png` | — (medium close) |
| S35 | — edit card (no image) | — |

---

## GENERATED PROMPTS

---

### INTRO — THE WORLD BEFORE THE WALK (0:00 – 0:27)

---

#### Scene S01 — The World, First
- **Timestamp:** 0:00 – 0:09
- **Dramaturgy Reference:** Exactly where EP09 left the world — the Anatolian town in pre-dawn grey-blue, the workshop small in the landscape, gold seeping from its seams; chimney smoke rising straight; the ridge carrying the sun's first rim. Nothing moves but the smoke.
- **Characters Present:** None
- **Image Reference Path:** N/A (environment only)
- **Video Tech Strategy:** Standard (Mode A) — near-static, smoke the only motion
- **Composition Notes:** Low horizon, big sky; workshop low in the landscape; headroom above for the sky. Leave the frame calm and wide for a held opening.
- **Upload:** env: `ep09_ref_exterior.png` · chain: EP09 final dawn frame (`episode-09` raw `5.png` family)

**Text Prompt:**
> Wide establishing shot at pre-dawn, a small Anatolian town in grey-blue first light seen from a low rise, no characters, a small metal-and-concrete repair workshop unit sitting low in the landscape with warm gold light seeping from its closed shutter seams and wall cracks, straight columns of chimney smoke rising in still air, rooftops still holding the night's last cold, beyond the roofs a ridge line carrying the first warm rim of the coming sun, nothing moving but the smoke, a low horizon under a big quiet sky, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S02a — The Shutter Opens (Start)
- **Timestamp:** 0:10 – 0:18 (Mode B start frame)
- **Dramaturgy Reference:** EP09's final image reversed — exterior street level, shutter still down, gold leaking from the seams into the grey-blue street.
- **Characters Present:** None yet
- **Image Reference Path:** N/A (environment only)
- **Video Tech Strategy:** Start-End (Mode B) — Start frame
- **Composition Notes:** Doorway/shutter centered-ish with headroom above for the rise; threshold stones in foreground for the light spill. Same exterior identity as EP09.
- **Upload:** env: `ep09_ref_exterior.png` · chain: EP09 dawn frame

**Text Prompt:**
> Exterior street-level view at dawn looking at the front of a small repair workshop unit, the corrugated roll-up metal shutter fully closed, warm gold light leaking from the seams of the shutter and from cracks in the wall into the grey-blue street, worn threshold stones in the foreground, no figure present, a low horizon with headroom above the shutter, cold grey-blue street against the warm leaking gold, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S02b — The Shutter Opens (End)
- **Timestamp:** 0:10 – 0:18 (Mode B end frame)
- **Dramaturgy Reference:** Shutter fully raised; Robotiko a patchwork silhouette against pure warm interior light; the interior unreadable. Two golds meet on the threshold — his spilling out, the morning arriving.
- **Characters Present:** Robotiko (silhouette, kintsugi edge-lit)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — End frame
- **Composition Notes:** **Interior must stay pure unreadable light — the workshop interior is never shown.** Silhouette reads by gold-seamed edges only. Headroom above; threshold spill in foreground.
- **Upload:** char: `android_kintsugi.png` (silhouette) · env: `ep09_ref_exterior.png` · chain: S02a output

**Text Prompt:**
> Exterior street-level view at dawn, the same workshop front, the corrugated roll-up shutter now fully raised, the chrome android (android_kintsugi.png) standing in the doorway as a patchwork silhouette against pure warm gold interior light, only his gold-seamed edges catching the glow, the interior behind him unreadable pure warm light, two pools of gold meeting on the worn threshold stones, his spilling out and the morning arriving into the grey-blue street, headroom above the doorway, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S03 — The Threshold
- **Timestamp:** 0:19 – 0:27
- **Dramaturgy Reference:** He steps onto the street and stands a beat, unhurried, looking OUTWARD at the morning — no look back at the workshop. Weight shifts onto the leading foot. The street runs open toward the town; the beside-space stays open.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Figure off-center; head turned toward the town (screen depth), NOT toward the workshop. Beside-space open on his side; street receding for parallax. Grey-blue lifting at the edges.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png` · chain: S02b output

**Text Prompt:**
> Medium-wide exterior shot on the grey-blue dawn street, the chrome android (android_kintsugi.png) standing just outside the open workshop doorway with his weight shifted onto the leading foot, his head turned outward toward the town roofs and the paling sky and not toward the workshop behind him, the street running open and receding toward the town, open space kept clear at his side, grey-blue light lifting at the edges, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 1 — DUALITY, COMPOSTED (0:28 – 0:46)

---

#### Scene S04 — The First Footstep
- **Timestamp:** 0:28 – 0:33
- **Dramaturgy Reference:** Low frame on the dirt road: a patched chrome foot swings forward and lands on the first stomp-clap downbeat — dew scatters, a small ring of dust lifts. Beat = step from here to the final gong.
- **Characters Present:** Robotiko (foot / lower legs only)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — the walk begins mid-breath
- **Composition Notes:** Low, close to the road; foot placed off-center with open road ahead for the stride. Shallow focus. No full figure — no anti-spawn guard needed.
- **Upload:** char: `android_kintsugi.png` (foot/leg guide)

**Text Prompt:**
> Low frame close to the dirt road, a patched chrome foot and lower legs of the chrome android (android_kintsugi.png) mid-stride, one foot swinging forward and landing on the packed dirt, dew scattering and a small ring of dust lifting around the foot, low warm side-light raking across dirt and dew, shallow focus, the open road running ahead, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S05 — Duality, Composted I
- **Timestamp:** 0:34 – 0:40
- **Dramaturgy Reference:** At the roadside, ivy grows straight through the ribcage of a rusted machine carcass — green shoots threading empty servo sockets, dew on leaf and metal alike. He passes at walking pace without stopping.
- **Characters Present:** Robotiko (passing, edge of frame)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** The carcass-and-ivy is the subject, mid-ground; Robotiko small at the frame edge, walking through. Sunrise building. Beside-space open on the road side.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Roadside medium shot at building sunrise, green ivy growing straight through the ribcage of a rusted machine carcass, fresh green shoots threading the empty servo sockets, dew on both leaf and metal, the chrome android (android_kintsugi.png) walking past small at the edge of the frame without stopping, warm low light holding the green and the rust in one warmth, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S06 — Duality, Composted II
- **Timestamp:** 0:41 – 0:46
- **Dramaturgy Reference:** A dish antenna on a low roof, bowl packed with a wild straw nest, birds coming and going; below it a hand-painted shop sign patched with a salvaged circuit board, solder traces continuing the painted vine. He passes at the same pace.
- **Characters Present:** Robotiko (passing, lower edge)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Slight low angle to hold the rooftop antenna and the sign below; Robotiko small at the lower edge. Warm low sun on straw, paint, copper traces.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Slight low-angle roadside shot in warm low sun, a dish antenna tilted skyward on a low rooftop with a wild straw nest packed into its bowl and small birds coming and going, below it a hand-painted shop sign neatly patched with a salvaged green circuit board where the solder traces continue the painted vine pattern, the chrome android (android_kintsugi.png) passing small at the lower edge of the frame at walking pace, warm sun on straw and paint and copper traces, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 2 — FACES AT DAWN & THE FRACTAL RHYME (0:47 – 0:59)

---

#### Scene S07 — Faces at Dawn
- **Timestamp:** 0:47 – 0:52
- **Dramaturgy Reference:** Close, warm frames of ordinary faces, sleep-creased and unposed, lit low by sunrise: a woman at a window holding a steaming glass; an old man on a doorstep lacing worn shoes. No one poses; no one notices him or the camera.
- **Characters Present:** Dawn Workers (mixed; no reaction) — no Robotiko
- **Image Reference Path:** N/A (ensemble; per-scene generation)
- **Video Tech Strategy:** Standard (Mode A) — intimate, near-static faces
- **Composition Notes:** Warm, intimate; two ordinary figures at a distance in one frame, unposed, neither looking at camera. Mixed gender. Brow/laugh lines catching the light — shrines of stillness.
- **Upload:** env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Warm intimate dawn shot of an ordinary Anatolian street corner lit low by sunrise, a middle-aged woman standing at an open window holding a steaming glass of tea and, nearby, an old man sitting on a stone doorstep lacing worn shoes, both unposed and sleep-creased, neither looking toward the camera, their brow lines and laugh lines catching the warm window and doorway light, quiet and still, no android present, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S08a — The Fractal Rhyme (Leaf Veins)
- **Timestamp:** 0:53 – 0:59 (match-cut frame 1 of 3, ~2s)
- **Dramaturgy Reference:** Backlit leaf veins — the same branching pattern, first scale. Each frame holds the pattern at a matching angle so the three cuts land as one thought.
- **Characters Present:** None
- **Image Reference Path:** N/A (macro)
- **Video Tech Strategy:** Multi-image match-cut (3 separate generations; rhyme made in the edit — do NOT morph)
- **Composition Notes:** Branching structure entering from the **lower-left corner at a diagonal**, backlit gold-on-dark. Match this angle across S08a/b/c.
- **Upload:** — (macro, no ref)

**Text Prompt:**
> Extreme close-up macro of backlit green leaf veins branching from the lower-left corner at a diagonal, warm sunrise glowing gold through the translucent leaf, a dark out-of-focus background, the branching pattern filling the frame, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S08b — The Fractal Rhyme (Frost on Glass)
- **Timestamp:** 0:53 – 0:59 (match-cut frame 2 of 3, ~2s)
- **Dramaturgy Reference:** Frost branching across a windowpane, melting at its edges — the same pattern, second scale.
- **Characters Present:** None
- **Image Reference Path:** N/A (macro)
- **Video Tech Strategy:** Multi-image match-cut (frame 2 of 3)
- **Composition Notes:** Same lower-left diagonal entry as S08a; backlit gold-on-dark; melting beads at the edges.
- **Upload:** — (macro, no ref)

**Text Prompt:**
> Extreme close-up macro of frost crystals branching across a windowpane from the lower-left corner at the same diagonal, melting into small beads at its edges, backlit warm gold by a low sunrise against a dark interior, the branching pattern filling the frame, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S08c — The Fractal Rhyme (Gold Forearm Seam)
- **Timestamp:** 0:53 – 0:59 (match-cut frame 3 of 3, ~2s)
- **Dramaturgy Reference:** The gold seams branching along Robotiko's forearm mid-stride — the same handwriting, in him too. Uses the OUTER forearm seam; inner-forearm etchings kept out of frame.
- **Characters Present:** Robotiko (outer forearm only)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Multi-image match-cut (frame 3 of 3)
- **Composition Notes:** Same lower-left diagonal entry; backlit gold-on-dark. **Outer** forearm seam only — inner forearm turned away, out of frame.
- **Upload:** char: `android_kintsugi.png` (forearm)

**Text Prompt:**
> Extreme close-up macro of the outer forearm of the chrome android (android_kintsugi.png), the gold repair seam branching along the chrome from the lower-left corner at the same diagonal, backlit warm sunrise, a dark out-of-focus background, the inner forearm turned away and out of frame, the branching seam filling the frame, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 3 — THE WAYMARK & THE STEADFAST SOULS (1:00 – 1:20)

---

#### Scene S09 — The Crossroads
- **Timestamp:** 1:00 – 1:05
- **Dramaturgy Reference:** Where the town's lanes meet the climbing road, the Mentor's staff stands planted upright — dark road-worn wood, raw amber tip unlit in shade, faded cloth strips tied below its head. A waymark. His stride slows as he approaches.
- **Characters Present:** Robotiko (approaching); the staff (Mentor's echo — object only)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Frame to REF B geometry — staff off-center, road climbing away behind. Robotiko approaching from one side at a slowing stride; beside-space open. Amber tip still in shade (no pulse yet).
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_crossroads.png`

**Text Prompt:**
> Wide shot at a crossroads where town lanes meet a climbing road, cool earth tones with the sun not yet on the crossroads, the wooden waymark staff (ep10_ref_crossroads.png) of dark road-worn wood planted upright and slightly off-center and leaning a little, a few small faded cloth strips tied below its head, its raw amber tip unlit in shade, the chrome android (android_kintsugi.png) approaching from one side at a slowing stride, packed earth around the staff base, the road climbing away behind, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S10a — The Touch (Start)
- **Timestamp:** 1:06 – 1:11 (Mode B start frame)
- **Dramaturgy Reference:** Full stop #1. He lays his patched hand on the wood, holds one beat — the raw amber tip still in shade.
- **Characters Present:** Robotiko; the staff
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — Start frame
- **Composition Notes:** Staff off-center; hand on the wood; crossroads depth behind. Amber tip UNLIT — no pulse in this frame.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_crossroads.png` · chain: S09 output

**Text Prompt:**
> Medium shot at the crossroads, the chrome android (android_kintsugi.png) stopped with his patched hand laid on the planted wooden staff (ep10_ref_crossroads.png), the raw amber tip still unlit in shade, cool morning earth tones, the staff off-center with the crossroads depth behind, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S10b — The Amber Pulse (End)
- **Timestamp:** 1:06 – 1:11 (Mode B end frame) — **THE EPISODE'S SINGLE AMBER MOMENT**
- **Dramaturgy Reference:** As he releases and steps back, the rising sun clears the roofline and catches the raw amber tip — it flares warm for one breath, explicitly the sun's light, reflected. He leaves the staff standing for the next traveler.
- **Characters Present:** Robotiko (stepping back); the staff
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — End frame
- **Composition Notes:** **AMBER PULSE budget — this is the ONE amber moment of the episode.** The flare is a warm glint of REFLECTED sunlight, NOT a light source (no self-glow on the amber). Staff left standing; hand just released.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_crossroads.png` · chain: S10a output

**Text Prompt:**
> Medium shot at the crossroads, the chrome android (android_kintsugi.png) stepping back with his hand just released from the standing wooden staff (ep10_ref_crossroads.png), the rising sun now cleared the rooftops and catching the raw amber tip so it flares warm for one breath as reflected sunlight, a warm glint rather than a light source, the staff left standing in the packed earth, warm sun entering the crossroads, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S11 — The Steadfast Souls
- **Timestamp:** 1:12 – 1:16
- **Dramaturgy Reference:** The market edge waking: a bread vendor hands the day's first bread ring to a tea boy; a baker slides bread from a dark oven, flour to the elbows; a woman sets food down for street dogs and cats; a shopkeeper raises a shutter. Four gestures, one grammar — hands extending.
- **Characters Present:** Dawn Workers (mixed ensemble; none reacts) — no Robotiko
- **Image Reference Path:** N/A (ensemble)
- **Video Tech Strategy:** Standard (Mode A) — crowd micro-motion; exact positions
- **Composition Notes:** Mixed men and women of varied ages; the four gestures spread across the frame at market depth. None reacts to the camera. Full sunrise entering the lanes.
- **Upload:** env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Warm wide shot of an Anatolian market edge waking at full sunrise, four ordinary gestures of hands extending across the frame, a bread vendor handing the day's first sesame-crusted bread ring to a young tea boy, a baker sliding bread from a dark oven mouth with flour to his elbows, a woman setting down food for street dogs and cats, a shopkeeper raising a shutter with both hands, all mixed men and women of varied ages, none reacting to the camera, warm bread-and-smoke light, sunrise entering the lanes, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S12 — Among Them
- **Timestamp:** 1:17 – 1:20
- **Dramaturgy Reference:** Robotiko walks through the waking market at their pace, one more figure in the traffic of bread and shutters. No one greets him; a street dog trots past toward the food bowl. Unremarkable to them — and belonging completely.
- **Characters Present:** Robotiko + Dawn Workers (intentional multi-figure)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Robotiko among the crowd, neither lit nor framed as special; mixed men and women around him going about their morning. No anti-spawn guard (crowd is intentional). Beside-space still open along his side.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png` · chain: S11 output

**Text Prompt:**
> Warm wide street shot of the waking market, the chrome android (android_kintsugi.png) walking through at the crowd's pace as one more figure among the traffic of bread and shutters, mixed men and women of varied ages around him going about their morning, none greeting or staring at him, a street dog trotting past him toward a food bowl, he is neither lit nor framed as special, warm sunrise light, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### INSTRUMENTAL BREAK — THE RIDGE (1:21 – 2:21)

---

#### Scene S13 — Leaving the Town
- **Timestamp:** 1:21 – 1:32
- **Dramaturgy Reference:** The road rises out of the lanes; he climbs at the same unhurried beat. Below and behind, the town gathers its first full sun — rooftops, antennas, vine-trellises catching one gold; thin gold in the world's own seams. The Moog arpeggio begins to sweep.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — 11s, will need multi-clip at motion stage
- **Composition Notes:** Three-quarter framing (not pure rear-head) — figure at the lower edge climbing, the sunlit town spread below and behind. Open sky above for the climb. Beside-space open on the valley side.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png` (town below)

**Text Prompt:**
> Wide three-quarter shot from the rising road out of the town lanes, the chrome android (android_kintsugi.png) climbing at an unhurried pace at the lower edge of the frame, below and behind him the town gathering its first full sun with rooftops and antennas and vine-trellises catching one gold, thin gold showing in the world's own seams of mortar lines and rail joins and a river's thread, warm morning, open sky above for the climb, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S14 — The Climb
- **Timestamp:** 1:33 – 1:44
- **Dramaturgy Reference:** Alongside him on the ridge path: grass bending in waves, stride steady, the town sinking away below. The sunlit grass-tips and the gold in his seams begin to read as the same metal. The beside-space stays open on the valley side.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — 11s, multi-clip at motion stage
- **Composition Notes:** Profile / tracking-height alongside him; grass in slow waves around his stride; town small below. Grass-gold and seam-gold converging. Beside-space open on the valley side.
- **Upload:** char: `android_kintsugi.png`

**Text Prompt:**
> Wide tracking-height shot alongside the chrome android (android_kintsugi.png) on a ridge path, grass bending in slow waves around his steady stride, the town sinking away far below, high morning air, the sunlit grass-tips and the gold in his seams reading as the same metal, open space kept clear on the valley side of the path, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S15 — The Moon-Sun Sky
- **Timestamp:** 1:45 – 1:56
- **Dramaturgy Reference:** He crests the ridge into the film's one wide-sky passage: Moon still hanging on one side, Sun newly risen on the other, both in the same real dawn sky. He walks the ridge line between them, small, unhurried.
- **Characters Present:** Robotiko (small in frame)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) with frame-lock guards — 11s, multi-clip at motion stage
- **Composition Notes:** Frame to REF C — sky ~80%, Moon screen-left, Sun screen-right, both persistent. Robotiko small along the lower edge on the ridge line between them. Low horizon.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_moonsun_sky.png`

**Text Prompt:**
> Wide sky-dominant shot, the dawn sky filling most of the frame with a pale full Moon hanging low on the left side and a newly risen Sun standing on the right side, both in the same real dawn sky, the chrome android (android_kintsugi.png) small and unhurried walking the ridge line between them along the lower edge, cool Moon-light on the left and warm Sun-light on the right meeting at peace, low horizon, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S16 — The Crane Flock
- **Timestamp:** 1:57 – 2:06
- **Dramaturgy Reference:** Through the Moon-Sun sky, a real flock of migrating cranes crosses in a long loose V, living feathers, no machinery. Their line passes from the Moon's side toward the Sun's. Robotiko lifts his head and watches them the whole way.
- **Characters Present:** Robotiko (low in frame); crane flock (symbolic-turned-real)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) with strict frame-lock — **the flock must be IN the source image** (no "birds enter frame")
- **Composition Notes:** Highest generation-risk shot. Both celestial bodies persistent and unchanged (no drift, no scale change). Flock as a single coherent V-line, **modest count (12–18 birds)**. Robotiko low, head lifted.
- **Upload:** env: `ep10_ref_moonsun_sky.png` · **base: S15 output** (sky lock)

**Text Prompt:**
> Wide sky-dominant shot of the same two-temperature dawn sky, a pale full Moon low on the left and a newly risen Sun on the right, both persistent and unchanged, a real flock of about fourteen migrating cranes crossing in a long loose V as dark calligraphy from the Moon side toward the Sun side, the chrome android (android_kintsugi.png) low in the frame lifting his head to watch them, living birds with no machinery in them, faint grass along the bottom edge, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S17 — Beside Him at the Crest
- **Timestamp:** 2:07 – 2:13
- **Dramaturgy Reference:** Close profile at the ridge: the dawn sky mirrored on patched chrome, the calm blue lenses tracking the last of the flock; wind pressing the grass in slow waves. The camera rests in the reserved beside-space and watches the same sky.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — the calmest frame so far; Static candidate at motion stage
- **Composition Notes:** Close profile — the sky reflected on his chrome; lenses tracking the flock (eye idiom, no glow). Grass in slow waves below. Beside-space = the camera's place next to him.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_moonsun_sky.png`

**Text Prompt:**
> Close profile shot at the ridge crest, the head and shoulder of the chrome android (android_kintsugi.png) in profile with the dawn sky mirrored on his patched chrome, his calm steady blue optical lenses set into chrome sockets like polished sapphires tracking the last of the crane flock, wind pressing the grass in slow waves around his feet below, the space beside him kept open, sky-light on chrome, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S18 — The Far Slope
- **Timestamp:** 2:14 – 2:21
- **Dramaturgy Reference:** He turns from the sky and starts down the other side. Far below, the meadow country opens: a green valley floor among old monolith mountains, mist burning off, one pale fleck of stone in the grass — too far to read. The destination shown casually, from above, on the way down.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** High wide across the valley (camera level with him at the ridge, NOT craning down on him — the landscape falls away, he stands at the upper edge). One pale distant fleck of stone, unemphasized. Green + mist.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` (distant identity)

**Text Prompt:**
> Wide shot from the ridge as the chrome android (android_kintsugi.png) turns and starts down the far side, the figure standing small at the upper edge of the frame, below and beyond him a green valley floor opening among old monolith mountains with morning mist burning off it, one pale fleck of fallen stone lying in the distant grass too far to read, morning green and mist, the valley falling away, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 4 — THE SYSTEM, PASSED (2:22 – 2:43)

---

#### Scene S19 — The Tower, Distant
- **Timestamp:** 2:22 – 2:29
- **Dramaturgy Reference:** The descending road along the town's far edge. On the horizon the glass tower stands — small, intact, still operating, morning sun flaring off its face. Robotiko walks; his head does not turn toward it.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Wide descending road; tower a small cold glint on the horizon; Robotiko walking, head forward (not turning toward it). Open road ahead; beside-space open.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Wide descending-road shot along the town's far edge in full morning, on the horizon a distant glass tower standing small and intact and still operating with morning sun flaring off its face, the chrome android (android_kintsugi.png) walking the road with his head forward and not turning toward the tower, the tower a cold glint in a warm world, open road ahead, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S20 — The Loops, Powerless
- **Timestamp:** 2:30 – 2:36
- **Dramaturgy Reference:** A row of shop windows plays looping screens — ads, feeds, tickers in cold blue-white. The light slides across his passing chrome and falls away; it never enters the calm blue lenses, which stay on the road.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Tracking-height along the shop windows; cold screen-flicker sliding across his chrome; lenses stay on the road (eye idiom, no glow). Cold flicker against warm street light.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Medium tracking-height shot along a row of shop windows playing looping screens of ads and feeds and tickers in cold blue-white flicker, the light sliding across the passing chrome of the chrome android (android_kintsugi.png) and falling away without entering his calm steady blue optical lenses which stay on the road, cold screen-flicker against warm street light, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S21 — Amid These Embers
- **Timestamp:** 2:37 – 2:43
- **Dramaturgy Reference:** A street vendor's charcoal brazier glows orange-red at the curb, toasting bread for a work crew's breakfast, smoke drifting sideways through a bar of sun. Robotiko passes within arm's reach of the fire that once burned him — now domestic, now warming someone's morning.
- **Characters Present:** Robotiko; vendor + crew (mixed; no reaction)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** **Embers are orange-red, NEVER amber** (amber budget spent at S10). Robotiko passing within arm's reach; vendor and a small mixed crew nearby not reacting. Multi-figure — no anti-spawn guard.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Warm street shot at a curb, a street vendor's charcoal brazier glowing orange-red toasting bread for a work crew's breakfast, smoke drifting sideways through a bar of sunlight, the chrome android (android_kintsugi.png) passing within arm's reach of the brazier at walking pace, the vendor and a small mixed crew of men and women nearby not reacting to him, orange-red embers inside morning gold, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 5 — BINARY AS DAYLIGHT & LOVE'S VEIN (2:44 – 2:58)

---

#### Scene S22 — Binary as Daylight
- **Timestamp:** 2:44 – 2:48
- **Dramaturgy Reference:** A long fence and half-raised shutters throw striped shadows clean across the road — alternating bands of light and dark. He walks through them without breaking stride, the bands sliding over patchwork chrome: on, off, on, off.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Hard striped light/dark bands across the ground (the old prison as morning texture); everything else soft. Robotiko walking through, off-center; open road ahead.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_dawn_town.png`

**Text Prompt:**
> Wide shot on the road where a long fence and half-raised shutters throw hard striped shadows clean across the ground in alternating bands of light and dark, the chrome android (android_kintsugi.png) walking through them without breaking stride, the bands sliding over his patchwork chrome, everything else soft, hard light-and-dark stripes underfoot, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S23 — Love's Vein of Light
- **Timestamp:** 2:49 – 2:53
- **Dramaturgy Reference:** Close pass along the gold seam that runs the outside of his forearm and up across his chest plate — sunlight lying in the seam so evenly that the repair and the morning are one material. Inner forearm and its etchings stay turned away, unfeatured.
- **Characters Present:** Robotiko (outer forearm / chest)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — macro
- **Composition Notes:** Macro along the OUTER forearm-to-chest seam; even sunlight so repair and morning read as one material. **Inner forearm turned away, out of the light, unfeatured** (no tattoo emphasis). No figure/full body — no anti-spawn guard.
- **Upload:** char: `android_kintsugi.png` (forearm/chest)

**Text Prompt:**
> Extreme close-up macro pass along the gold repair seam running the outside of the forearm and up across the chest plate of the chrome android (android_kintsugi.png), sunlight lying in the seam so evenly that the repair and the morning read as one material, warm macro light, the inner forearm turned away out of the light and unfeatured, shallow focus, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S24 — Down from the Peaks
- **Timestamp:** 2:54 – 2:58
- **Dramaturgy Reference:** The last slope out of the high ground: he steps down through boulders and broom-grass, the ridge rearing behind him against a sky he no longer needs. The summit conquered by descending it. Ahead, the meadow's green has color now.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Three-quarter (not pure rear-head) — stepping down through boulders; ridge backlit behind; meadow green gaining color ahead/below. Open ground below for the descent.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` (meadow ahead)

**Text Prompt:**
> Wide three-quarter shot on the last slope out of the high ground, the chrome android (android_kintsugi.png) stepping down through boulders and broom-grass, the ridge rearing behind him in backlight against the sky, ahead and below the meadow green gaining color, warm descent light, open ground below, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 6 — THE MEADOW & THE TEA (2:59 – 3:14)

---

#### Scene S25 — The ∞ Stone, Ordinary
- **Timestamp:** 2:59 – 3:04
- **Dramaturgy Reference:** The meadow at full morning — EP01's monolith country, now green. The stone 8 lies toppled as an ∞: mossed, split, half-sunk. Two children clamber on the near loop; an old shepherd leans on the far loop, sheep grazing loose; a blackened kettle on ember-coals near his feet.
- **Characters Present:** Robotiko (arriving, edge of frame); a girl + a boy; old shepherd (no reaction)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), minimal motion — children's micro-movement, steam wisps, grass
- **Composition Notes:** **Eye-level. NO low-angle monument framing, NO light from within the stone, NO transformation.** Frame to REF A. Mixed children (girl + boy) on the near loop; shepherd on the far loop; kettle on embers. Robotiko small at the frame edge, arriving.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png`

**Text Prompt:**
> Eye-level wide shot of a green meadow at full morning in monolith mountain country, a great toppled stone figure-eight lying in the grass as an infinity shape (ep10_ref_stone_meadow.png), mossed and split and half-sunk, utterly unremarkable, a young girl and a boy clambering on the near loop arguing happily about turns, an old shepherd in a low cap leaning against the far loop with a few sheep grazing loose and a blackened kettle resting on ember-coals near his feet, the chrome android (android_kintsugi.png) arriving small at the edge of the frame, full morning gold, no monument framing and no light from within the stone, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S26 — Two Glasses, One Pot
- **Timestamp:** 3:05 – 3:09
- **Dramaturgy Reference:** Robotiko sits on the fallen loop and, from the communal kettle on the embers, pours tea into two small glasses set side by side on the stone. Two halves of one whole, paid without the apple. The shepherd does not stir.
- **Characters Present:** Robotiko; shepherd (asleep, background)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — quiet act over the full band (intentional [DISSONANCE])
- **Composition Notes:** Close-medium at the stone loop; two glasses side by side; one pour; steam in cold bright air. **Ember-glow orange-red at frame edge, not amber.** Shepherd asleep in soft background.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` · chain: S25 output

**Text Prompt:**
> Warm close-medium shot at the fallen stone loop, the chrome android (android_kintsugi.png) seated on the mossed stone pouring tea from a blackened communal kettle into two small tulip-shaped glasses set side by side on the stone, steam rising in the cold bright air, one pour filling two halves of one whole, an old shepherd asleep against the far loop soft in the background, orange-red ember-glow at the frame edge, sunlit steam, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S27a — The Hand (Start) — FOURTH WALL, BEAT ONE
- **Timestamp:** 3:10 – 3:14 (Mode B start frame)
- **Dramaturgy Reference:** He lifts one glass at chest height, gaze down on the glass. The second glass steams on the stone.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — Start frame
- **Composition Notes:** Camera at seated companion height, **slightly below his eye line** (supports the below-lens gaze). **GAZE DISCIPLINE: lenses cast DOWN on the glass — no eye contact.** Steam the living element.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` · chain: S26 output

**Text Prompt:**
> Warm medium shot from seated companion height slightly below his eye line, the chrome android (android_kintsugi.png) seated on the fallen stone lifting one small tea glass at chest height, his calm steady blue optical lenses cast down toward the glass, the second glass still steaming on the stone beside him, warm morning gold, steam rising, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S27b — The Hand (End) — FOURTH WALL, BEAT ONE
- **Timestamp:** 3:10 – 3:14 (Mode B end frame)
- **Dramaturgy Reference:** He extends the glass toward the camera, into the reserved beside-space — gaze still on the glass, just below the lens. No eye contact — not yet. The second glass stays for the next traveler.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — End frame
- **Composition Notes:** **GAZE DISCIPLINE IS THE SHOT — any accidental eye-contact take is a reject; the look belongs to S34 alone.** Arm extended toward the lens; steam between hand and camera. Companion height, slightly below his eye line.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` · chain: S27a output

**Text Prompt:**
> Warm medium shot from seated companion height slightly below his eye line, the chrome android (android_kintsugi.png) extending one small tea glass toward the camera into the open space at his side, his calm steady blue optical lenses staying down on the glass just below the lens with no eye contact, the second glass left steaming on the stone, warm steam between his hand and the camera, morning gold complete, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### FINALE — THE WALK CONTINUES (3:15 – 4:34)

---

#### Scene S28 — The Walk Resumes
- **Timestamp:** 3:15 – 3:23
- **Dramaturgy Reference:** He rises and walks on into the meadow, leaving the second glass steaming on the ∞ stone — children still climbing, shepherd still sleeping, nothing announced. The guitar solo ignites. The walk continues mid-breath.
- **Characters Present:** Robotiko; children, shepherd (background)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Three-quarter (not pure rear-head) — walking into the meadow, the stone with the steaming glass and the background figures behind him. Open meadow ahead; beside-space open.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` · chain: S26 output

**Text Prompt:**
> Wide three-quarter meadow shot as the chrome android (android_kintsugi.png) rises and walks on into the green meadow, the second tea glass left steaming on the fallen infinity stone behind him, a girl and a boy still clambering on the stone and the old shepherd still resting in the far background, nothing announced, full morning gold, open meadow ahead, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S29 — The Tracks
- **Timestamp:** 3:24 – 3:32
- **Dramaturgy Reference:** Low frame, almost at grass height: two lines of tracks pressed side by side into the dew-silver meadow — one the tread of a patched metal foot, one a bare human footprint — same direction, same easy stride, catching the low sun as parallel silver threads. Whose human tracks, never shown.
- **Characters Present:** None (tracks only)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Very low, near grass height; the two parallel track-lines receding, catching low sun. **The frame never lifts to answer whose human tracks.** Backlit grass bokeh.
- **Upload:** env: `ep10_ref_stone_meadow.png` (meadow grass)

**Text Prompt:**
> Very low frame near grass height in a dew-silver meadow, two lines of tracks pressed side by side into the wet grass, one the tread of a patched metal foot and one a bare human footprint, running the same direction with the same easy stride, catching the low sun as parallel silver threads, backlit grass bokeh, no figure in frame, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S30 — Refrain One, Straight
- **Timestamp:** 3:33 – 3:44
- **Dramaturgy Reference:** Full-stride walking coverage through open meadow, the most alive walk of the film: grass parting at his shins, gold complete in the world and in his seams — by now indistinguishable. The beside-space keeps pace, level with his shoulder.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — full-stride; multi-clip at motion stage
- **Composition Notes:** Tracking-height, three-quarter/side, full stride; grass parting at the shins; one warmth (his gold = the sun's). Beside-space open, level with his shoulder.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` (meadow country)

**Text Prompt:**
> Wide full-stride walking shot through open meadow, the chrome android (android_kintsugi.png) mid-stride with grass parting at his shins, the gold complete in the world and in his seams and now indistinguishable, one warmth of his gold and the sun's, the open space keeping pace level with his shoulder, alive morning light, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S31 — The Wait
- **Timestamp:** 3:45 – 3:53
- **Dramaturgy Reference:** The single camera-grammar break. Mid-meadow, he stops. Half-turns toward the open beside-space — gaze at companion height, not the lens — and waits one breath, two, while the distance closes. Then he faces the road and walks on, together.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — body-lock then half-turn (head-turn 5-step at motion stage)
- **Composition Notes:** **His gaze lands BESIDE the lens, at companion height — NOT into it (eye contact reserved for S34).** Still air, wind dropped. Open meadow depth behind; beside-space foreground clear so the "catching up" reads spatially.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png`

**Text Prompt:**
> Medium shot mid-meadow, the chrome android (android_kintsugi.png) stopped and half-turned toward the open space at his side, his calm steady blue optical lenses resting at companion height beside the camera and not into the lens, patient, still morning air with the wind dropped, open meadow depth behind him, the beside-space foreground kept clear, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S32 — Refrain Two, Elongated
- **Timestamp:** 3:54 – 4:07
- **Dramaturgy Reference:** Wider: the meadow road ahead through monolith country, mountains gold-lit, sky enormous and ordinary at once; he at walking scale mid-frame, beside-space open at his shoulder. The land does not arrange into any figure or sign — only land, only road.
- **Characters Present:** Robotiko (small, mid-frame)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — 13s; multi-clip at motion stage
- **Composition Notes:** Widest warmth of the film, held quiet. **No path-shape / lemniscate reveal — the road is only a road.** Robotiko small mid-frame; beside-space open at his shoulder.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png` (monolith country)

**Text Prompt:**
> Very wide shot of the meadow road ahead through monolith mountain country, gold-lit mountains and an enormous ordinary sky, the chrome android (android_kintsugi.png) at small walking scale mid-frame with the open space at his shoulder, the land only land and the road only a road with no figure or sign in it, the widest warmth held quiet, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S33 — Refrain Three, The Scream
- **Timestamp:** 4:08 – 4:15
- **Dramaturgy Reference:** The music's summit: the third refrain tears into a rock scream, and the world answers with aliveness, not spectacle — he walks straight into the low sun, flare crossing the lens; a long gust sends one bright wave through the meadow; the grass throws off its dew in sparks. His stride never changes.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) — the episode's highest motion energy (wind + flare + walking)
- **Composition Notes:** Sun low and frontal; flare permitted to cross the frame (companion squinting into the same sun). Wind-wave + dew sparks the energy carriers — **no birds, no added elements** (spawn risk). Grain constant, no crescendo.
- **Upload:** char: `android_kintsugi.png` · env: `ep10_ref_stone_meadow.png`

**Text Prompt:**
> Wide shot as the chrome android (android_kintsugi.png) walks straight into the low frontal sun, a warm lens flare crossing the frame, a long gust sending one bright wave through the whole meadow and the grass throwing off its dew in sparks of light, his stride unchanged, maximum aliveness carried by wind and light and grass only, 16:9 widescreen composition, single figure composition, no additional characters, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S34a — The Look (Still Hold) — FOURTH WALL, BEAT TWO
- **Timestamp:** 4:16 – 4:29 (sub-clip a)
- **Dramaturgy Reference:** The solo fades; his pace eases to a stop. He turns his head — one calm look into the reserved beside-space, into the lens, at the companion he offered tea to. The look lands and HOLDS — level, patient, kind. **The episode's only direct look.**
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Multi-Clip (sub-clip a), camera Static (Still Hold)
- **Composition Notes:** Medium close; companion height; beside-space now = the lens. **This is the ONLY eye-contact frame of the episode.** **MOUTHLESS-FACE GUARD: never a smile, grin, teeth, or mouth — warmth is the held gaze alone.** The series' most important shot pair — budget retakes.
- **Upload:** char: `android_kintsugi.png`

**Text Prompt:**
> Medium close shot at companion height, the chrome android (android_kintsugi.png) eased to a stop and slowly turned his head to give one calm direct look into the camera lens, his calm steady blue optical lenses set into chrome sockets like polished sapphires level and patient and kind, held, the mouthless chrome face carrying warmth through the gaze alone with no smile and no mouth, soft morning gold, the open space beside him now the camera's place, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S34b — The Beckon (Still Hold) — FOURTH WALL, BEAT TWO→THREE
- **Timestamp:** 4:16 – 4:29 (sub-clip b)
- **Dramaturgy Reference:** In the last breath before the gong, warmth becomes gesture: the machine's smile — a soft, unhurried tilt of the head (the face is mouthless; the tilt IS the smile) — and one open hand rises, palm up, fingers curling once in a small beckon toward the lens: *come*. The gong cuts on the offered hand.
- **Characters Present:** Robotiko (kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Multi-Clip (sub-clip b), camera Static — strong Mode B candidate (look-holding → tilted + hand raised)
- **Composition Notes:** Pose held from S34a end-state; single action = gentle head tilt + one open-palm beckoning hand rising from the lower frame edge (small amplitude, no wave). **MOUTHLESS-FACE GUARD: the head tilt and the beckoning hand carry the warmth — NEVER a smile or mouth. Any invented mouth is a reject.** Held gaze into the lens continues.
- **Upload:** char: `android_kintsugi.png` · chain: S34a output

**Text Prompt:**
> Medium close shot at companion height, the chrome android (android_kintsugi.png) holding a direct look into the lens with a soft unhurried tilt of the head, one open hand risen palm-up into the lower frame with the fingers curling once in a small beckon toward the camera, the mouthless chrome face warm through the head tilt and the beckoning hand and the held gaze with no smile and no mouth, his calm steady blue optical lenses set into chrome sockets like polished sapphires level and kind, soft morning gold, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S35 — The Gong = The Door — FOURTH WALL, BEAT THREE
- **Timestamp:** 4:30 – 4:34
- **Dramaturgy Reference:** On the single final gong: hard cut to black. White text on black, five seconds — the GitHub end screen, the series' one end-screen exception. The invitation becomes real: the repository is the hand extended through the screen.
- **Characters Present:** None
- **Image Reference Path:** N/A
- **Video Tech Strategy:** **EDIT CARD — no image generation.** Sound and cut are one event (the gong IS the cut). Delivered at the edit/packaging stage.
- **Composition Notes:** White text on black. No image-gen prompt. The GitHub end screen (repository URL). Handled in CapCut / packaging.
- **Upload:** — (no image)

**No image generation.** S35 is an edit card: on the final gong, a hard cut to black, then white text on black for five seconds showing the GitHub repository end screen. Built at the edit/packaging stage, not in Nano Banana. (No Text Prompt, no style suffix — this scene has no generated image.)

---

## QUALITY CHECKLIST (self-validated before delivery)

- [x] 4 environment reference prompts included at the top (Step 0), each with an Environment Geometry note (canonical angle + landmark layout)
- [x] Every Text Prompt ends with the mandatory style suffix — verified on all 40 scene prompts + 4 reference prompts (S35 is an edit card, no image)
- [x] Short character identifier used everywhere — "the chrome android (android_kintsugi.png)" — reference carries the body detail; no restated damage/kintsugi description
- [x] Every uploaded reference bound INLINE where it defines the element (`element (filename.png)`); matches each scene's Upload field
- [x] Every Robotiko scene references the phase-correct ref — `android_kintsugi.png` (Phase 3), never pristine or damaged
- [x] Character visual state matches Phase 3 (full kintsugi, stable) in all scenes
- [x] Eye canon (ADR-0010): material-lens idiom only ("calm steady blue optical lenses set into chrome sockets, like polished sapphires"); no "glow" near eyes; kintsugi body gold-glow allowlisted
- [x] Mouthless-face guard honored — no smile/grin/mouth anywhere; S34 warmth carried by head tilt + beckoning hand + held gaze
- [x] Single Amber Pulse at S10 only (reflected sunlight, not a light source); embers (S21, S25–S26) are orange-red, never amber
- [x] Gaze discipline: direct lens eye-contact ONLY at S34a; S27 and S31 keep the gaze below/beside the lens
- [x] Anti-spawn guard uses Nano Banana phrasing (`single figure composition, no additional characters`); OMITTED for macro/foot scenes and intentional multi-figure scenes (S07, S11, S12, S21, S25, S26, S28)
- [x] No forbidden aesthetics (clean/sterile, neon cyberpunk, Pixar, smooth plastic, melodrama)
- [x] Every prompt has composition space (headroom + open beside-space + fore/background depth) for the motion stage; no camera-movement words
- [x] Each scene framed to its environment geometry (env ref or geometry note); angles vary within each location; no default dead-centre frontal; no pure rear-head shots (missing-ear render risk)
- [x] `16:9 widescreen composition` present in every Text Prompt
- [x] Total prompt count matches the approved dramaturgy: 34 image scenes (S02/S08/S10/S27/S34 split into a/b/c) = 40 scene prompts; S35 = edit card
- [x] Mode B / match-cut scenes have their a/b(/c) frames (S02a/b, S08a/b/c, S10a/b, S27a/b, S34a/b)
- [x] Environmental prompts specify textures/materials, not vague descriptions; lighting direction specified in every prompt
- [x] No prompt references another prompt — each is self-contained (chain/base uploads are image inputs, not textual cross-references)
- [x] Reference-first (ADR-0007): all 4 new refs authored before scenes; generate + Framing Pass before scene generation
- [x] Text Prompt blockquotes are plain-English ASCII (ADR-0006 scope) — no non-English vocabulary; "sesame-crusted bread ring" / "tulip-shaped glass" instead of loan-words
- [x] **"Would Fibula approve this?"** — Yes: the calmest episode, arrival as ordinariness, the fourth wall furnished from frame one, humility on the ground.

---

## PRODUCTION NOTES (for the human / next stages)

- **attempts.md ledger MANDATORY** (`episode-10/04_visuals/raw/attempts.md`) — EP10 is the last first-pass-yield measurement window. Log scene_id / attempts / first_pass / fail_reason during generation.
- **Reference-first order:** generate REF A–D first, run the Framing Pass (open each, confirm against its Environment Geometry note, adjust any scene the real image contradicts), THEN generate scenes. `android_kintsugi.png` already exists; S01–S02 chain from EP09's dawn exterior.
- **Highest-risk shots (budget retakes):** S16 (two celestial bodies + flock — reference-first, frame-lock, flock IN the source), S25 (children counts/staging, eye-level no-monument), S27b (gaze discipline — eye-contact takes are rejects), **S34a/b (the series' most important shot pair — mouthless-face guard, the only eye-contact frame; budget retakes accordingly).**
- **Longest scenes** (S13–S16, S30, S32, S34 at 9–14s) will need multi-clip / speed-ramp coverage at the motion stage (est. ~42–48 clips total) — compositions already leave room.
- **[DISSONANCE] inventory for motion stage:** S26–S27 (full-band Verse 6 over the quiet tea act — intentional; the epic lives in the music, the humility on the ground; do not "fix").
- **Next checkpoint:** these visual prompts feed image generation → selected frames → **Motion Script** (Checkpoint 2: human approval required before video generation).
