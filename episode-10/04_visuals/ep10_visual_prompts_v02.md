# EP10 — VISUAL PROMPTS

> **Version:** v02 | **Generated:** 2026-07-07 | **Phase:** 1+2 (References + Scenes framed to approved pixels)
> **Skill:** `_skills/robotiko-visual-prompts/SKILL.md` (two-phase v2.0)
> **Inputs:** Approved `ep10_dramaturgy_v01.md` (Gate-1, 2026-07-06), the 6 APPROVED reference images (gate 1R, 2026-07-07), `master.md`, `character_profiles.json`, `ep10_musical_metadata.json`, `ep10_concept_notes.md`
>
> This is the **Phase 1+2 deliverable**: the six approved REF blocks carried forward (Environment Geometry notes rewritten to the ACTUAL approved pixels), the ART DIRECTION LOCKS, the coverage map, the per-space Camera Ledger, the ref-less scene gate, and all 40 scene prompts framed to the real reference images. The Phase-1 sentinel is removed.

---

## PRE-GENERATION CHECKLIST

- [x] `_management/master.md` — Visual DNA, color palette, forbidden list, mandatory suffix (Sec. 3)
- [x] `episode-10/03_direction/ep10_dramaturgy_v01.md` — APPROVED scene breakdown (35 scenes, S35 = edit card)
- [x] `_assets/cast/character_profiles.json` — Phase 3 full kintsugi, `phase_reference_map` → kintsugi for EP10
- [x] `_assets/cast/android_kintsugi.png` — Phase 3 body reference (chain from this file for EVERY scene)
- [x] EP09 dawn-exterior lineage (`episode-09/04_visuals/ep09_ref_exterior.png` + EP09 final dawn frames) — S01-S02 chain
- [x] **6 approved reference images read pixel-by-pixel (gate 1R):** `ep10_ref_stone_meadow.png`, `ep10_ref_crossroads.png`, `ep10_ref_moonsun_sky.png`, `ep10_ref_dawn_town.png`, `ep10_ref_market_edge.png`, `ep10_ref_far_edge.png`

---

## CHARACTER REFERENCE — CRITICAL NOTE

EP10 is **Phase 3, full kintsugi, stable from frame one** — no damage progression, no transformation beats. `phase_reference_map.default_by_phase["3"]` = **kintsugi** → chain every Robotiko scene from **`_assets/cast/android_kintsugi.png`**.

- **Do NOT** use `ref_robotiko_master.png` (pristine Phase 1) or `android_damaged.png` (Phase 2). Either would break continuity.
- **The kintsugi reference carries the body detail** (patchwork chrome, gold-filled seams, translucent skin over the bioluminescent core, calm steady blue optical lenses, missing right ear, torso dent). Per the reference-brevity rule, prompts use the short identifier **"the chrome android (android_kintsugi.png)"** and do NOT restate that detail. Describe only what is NOT in the reference (a new light state, a gaze direction, a pose).
- **S01-S02 exterior:** chain from EP09's dawn-exterior lineage (`ep09_ref_exterior.png` / EP09 final dawn frame family) so the workshop and industrial-edge town read identically to EP09's last frames.
- **Eye canon (ADR-0010):** material-lens idiom ONLY in every Text Prompt — `calm steady blue optical lenses set into chrome sockets, like polished sapphires`. Never "glow" within reach of an eye/lens word. Kintsugi **body** gold-glow is allowlisted (seams may read gold); the eyes never do.
- **Mouthless-face guard (verified against `android_kintsugi.png`):** the face has NO mouth. Never prompt a smile, grin, teeth, or mouth in any scene — warmth (esp. S34) is carried by head tilt, beckoning hand, and the held gaze. Any take that invents a mouth is a reject.
- **Rear-view ear rule:** for any behind-the-head framing, angle from his LEFT (intact ear toward camera) — the missing right ear does not render from a direct rear. Applied to S13, S14, S18, S28.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP10 |
| **Title** | The Glitch Scripture / I Came to Walk Beside |
| **Station** | The Integrated Self — Arrival (Enlightenment. 8 -> infinity) |
| **Character Phase** | Phase 3: Reconstruction (full kintsugi — complete, worn as ordinary skin) |
| **Robotiko Visual State** | Patchwork chrome body repaired with mismatched rusted scrap metal, translucent digital skin over a bioluminescent core, cracks filled with glowing gold light, calm steady blue optical lenses set into chrome sockets like polished sapphires. Right ear missing, torso dent, shoulder scratches carried; inner-forearm etchings present but **never featured, never lit, never framed**. |
| **Camera Personality** | THE COMPANION CAMERA — alongside, never above; the reserved beside-space kept open in every frame (lineage finale: EP07 Retreating -> EP08 Witnessing -> EP09 Discovering -> EP10 Companion). |
| **Reference (body)** | `_assets/cast/android_kintsugi.png` — chain for every scene |
| **Total Scenes** | 35 (34 image-generated + S35 edit card) |
| **Total Image Prompts** | **40** (sub-splits: S02a/b, S08a/b/c, S10a/b, S27a/b, S34a/b; S35 = edit card, no image) |
| **Environment References** | 6 (A-F) + EP09 chain-base for S01-S02 + `android_kintsugi.png` body ref |
| **Phase status** | Phase 1+2 complete — all references approved, all scenes framed to real pixels |

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
- **Color journey — self-made gold -> indistinguishable from sunrise.** Intro: his gold distinct in pre-dawn grey-blue (S01-S03). Verses/climb: the world's warmth rises to meet his; grass-gold and seam-gold converge (S13-S18). Meadow/finale: one warmth — kintsugi seams read as ordinary highlights (S30 onward). Kodachrome warm bias throughout; heavy grain constant, never crescendoing.
- **The single Amber Pulse — S10b ONLY.** Reflected sunlight on the staff's raw amber tip; a warm glint, never a light source. NO amber anywhere else in the episode. Embers (S21, S25-S26) are **orange-red**, never amber.
- **Environmental rules — one road, one dawn.** Continuous geography, continuous time (pre-dawn grey-blue -> early golden hour). No flashbacks, no cosmic sets, no teleports, no rain/storm/night. CyberAnatolian texture stays background, never foregrounded.
- **Body — full kintsugi from frame one, stable.** No damage progression, no transformation beats. Chain from `android_kintsugi.png`.
- **What is NOT shown:** the stone 8 standing or transforming; the Mentor embodied or projected; Robochica in any form; the Mechanic; the workshop interior (S02 doorway stays pure unreadable light); any screen-world / virtual space; any monument framing of the infinity stone; eye contact before S34; any lemniscate / path-shape reveal; **any invented mouth on Robotiko**.
- **Gaze discipline:** the ONLY direct look into the lens is S34a (held into S34b). S27 (the offered hand) and S31 (the wait) keep the gaze BELOW / BESIDE the lens — any eye-contact take there is a reject.
- **Composition for motion:** every frame leaves headroom + the open beside-space + fore/background depth for the motion stage; cuts land on the felt stomp-clap pulse (76.5 BPM, beat = footstep). No camera-movement words in prompts (angle/placement only).

---

## LOCATION DECOMPOSITION (carried from Phase 1, confirmed against pixels)

The approved dramaturgy names three walk locations that resolve into distinct camera-spaces. The single label "dawn town" is **three** camera-spaces, not one:

| Location label | Camera-spaces | Refs |
|---|---|---|
| Monolith meadow / infinity-stone country | 1 | **A** |
| The crossroads (village exit onto highland) | 1 | **B** |
| Ridge / Moon-Sun crest | 1 | **C** |
| **Dawn town** | **3** — residential lane / market edge / far-edge descent | **D + E + F** |

Confirmed at Phase-2 batch verification: the three town siblings (D, E, F) came back as distinct site-maps with the required through-anchors intact (see REF blocks). No decomposition gap remained; no loop-back was triggered.

---

## ENVIRONMENT REFERENCE BLOCKS (carried forward; Environment Geometry rewritten to approved pixels)

All six approved and frozen at gate 1R (`raw/`). Each Environment Geometry note below has been **rewritten to describe the ACTUAL approved image** (the post-approval rewrite that structurally replaces the old Framing Pass). Scenes frame to THESE notes, i.e. to the real pixels.

---

### REF A: Toppled-Infinity Stone in Green Meadow (S18 distant, S24-S34 meadow identity)

**Design Brief:** The EP01 monolith country, now green with morning. The great stone figure-eight fell long ago and lies in the grass as an infinity shape — mossed, split, half-sunk, utterly ordinary. Prophecy became furniture. NO monument framing, NO light from within the stone, NO awe.

**Environment Geometry (approved pixels, 2026-07-07):** Low eye-level camera close to the grass. The two joined cracked-and-mossed stone loops lie across the near mid-ground and foreground, the **larger near loop toward the camera in the lower-center**, the joined smaller loop receding to the right; loose stone blocks scattered at the left and right frame edges. **Tall jagged monolith rock towers stand in the LEFT background**, softer rolling green hills to the right; morning mist burns off the valley floor in the mid-distance between them. Warm low sun from the **right**, gold rim on the grass-tips. Thick green foreground grass; big open sky in the upper third, low horizon. Beside-space = the open grass foreground and to the right of the near loop (a good place to sit).

**Narrative anchors:** the open meadow foreground stays clear for the beside-space (the companion's seat); the infinity-stone is ordinary furniture, never a monument; the LEFT-background monolith towers are the world-identity through-anchor tying the meadow to the ridge (REF C) and crossroads highland (REF B).

**Reference Image Path:** `episode-10/04_visuals/raw/ep10_ref_stone_meadow.png` — APPROVED, frozen (2026-07-06).

**Text Prompt:**
> Wide establishing shot of a green meadow at full morning in old monolith mountain country, no characters, a great toppled stone figure-eight lying in the grass as an infinity shape of two joined stone loops, mossed and split by old weather, half-sunk in the meadow grass, utterly unremarkable and ordinary, tall monolith mountains standing in the background, morning mist burning off the valley floor beyond, warm morning gold, eye-level camera treating the stone as an ordinary place to sit, the stone lying across the mid-ground with the near loop toward the camera, low horizon under a big open sky, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF B: The Crossroads + Waymark Staff (S09-S10)

**Design Brief:** The crossroads at the exit / upper edge of the Anatolian mountain village, where the town's lanes give onto the climbing road. The Mentor's only echo: his amber-tipped staff planted upright as a waymark. Houses out of frame (village behind the traveler). A waymark, not a monument.

**Environment Geometry (approved pixels, 2026-07-07):** Pre-dawn cool blue-grey. The waymark staff planted **near-center in the foreground**, upright and slightly leaning, dark gnarled wrapped wood with pale cloth strips knotted below the head; the **raw amber crystalline tip dark and dormant**, catching only a faint warm touch (still reads as amber that can catch light — needed for S10b). A **Y-fork of dirt tracks** converges at the staff and climbs away into the misty valley (both forks rising). Semi-arid green-grey highland scrub; low weathered stone remnants (ruined low wall stumps) around a central island behind the staff; a **lone satellite dish on the LEFT hillside**, mid-ground; a faint **cyan retrofit light-line low mid-right** (CyberAnatolian texture); distant mountains on the horizon, one center-right peak catching the first warm dawn light; morning mist pooling in the valley. NO houses (removed at the image stage — see Framing Pass note). Eye-level.

**Narrative anchors:** the staff is a waymark left standing for the next traveler (farewell to received warmth), never a monument; the amber tip stays dormant so S10b's single Amber Pulse is the sun's reflected light; the highland scrub + distant peaks are the through-anchor to REF C / REF A (one continuous highland world, village behind camera).

**Reference Image Path:** `episode-10/04_visuals/raw/ep10_ref_crossroads.png` — APPROVED, frozen (2026-07-07).
**Framing Pass note (2026-07-07):** Locked. Gen 1 drifted (glowing amber + European castle); gen 2 fixed the amber + Anatolian village; final edit **removed the background houses** so the shot reads as the village EXIT onto open highland — sidesteps the flat-roof vs REF D tile-roof clash and ties the crossroads into REF C / REF A's green-highland world. Landscape anchor = distant peaks + highland scrub; lone retrofit dish + cyan light-line kept. For S10b the tip reads as amber that can catch the sun when it flares.

**Text Prompt:**
> Wide establishing shot of a crossroads at the open upper edge of an Anatolian mountain village where the lanes give onto the climbing road, no characters, open semi-arid green highland opening ahead with rolling hills all around, multiple dirt tracks converging at the crossroads and roads climbing away into the misty background, a wooden waymark staff of dark road-worn gnarled wood planted upright in packed earth slightly off-center and leaning a little, a few small faded cloth strips tied below its head by travelers, its raw amber tip dark and dormant, a dull matte unlit amber in the cool shade catching no light, low weathered stone remnants and green highland scrub around the central island of the crossroads, a single small satellite dish on a far hillside as ordinary CyberAnatolian retrofit texture, distant sharp rocky peaks on the horizon, the earth packed by many feet with old track lines, cool earth tones with the sun not yet reaching the crossroads, morning mist in the valley, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF C: Ridge Moon-Sun Sky (S14-S18)

**Design Brief:** The film's one wide-sky passage. The series' epigraph resolved by an ordinary morning: a pale full Moon still hanging while the Sun rises, both in the same real dawn sky. Both temperatures at peace.

**Environment Geometry (approved pixels, 2026-07-07):** High ridge vantage looking out and down over a valley. Sky fills the upper **~75-80%**: **pale full Moon on the LEFT** (mid-left, just above the far ridgeline, cool), **bright rising Sun on the RIGHT** (right third, low near the horizon, warm orange blaze); layered dawn clouds — cooler blue-purple left, warm gold right. Below the sky: a deep valley with a **winding river and a small town on the valley floor** (left-center), blue-hazed mountain ridges receding. **Lower-right foreground: a rocky grassy ridge crest with a footpath** running along it toward the Sun side. Room for a small walking figure on the ridge path (lower-center/right) and a crane line across the open sky without touching Moon or Sun.

**Narrative anchors:** the two bodies stay locked and at peace (the Moon has no light of its own, yet shines) — the episode's resolved epigraph; the lower-right ridge grass/path keeps the beside-space and room for the small figure and the crane line; the valley town below is the same town he left (through-anchor).

**Reference Image Path:** `episode-10/04_visuals/raw/ep10_ref_moonsun_sky.png` — APPROVED, frozen (2026-07-06).
**Note:** S16's flock is a **variant generated against this ref** (base = S15/REF C output) so the two bodies stay locked — the flock must be IN the source, never prompted to "enter frame."

**Text Prompt:**
> Wide establishing sky shot from a high open ridge above a distant town, no characters, the dawn sky filling roughly eighty percent of the frame, a pale full Moon hanging low on the left side and a newly risen Sun standing on the right side, both present in the same real dawn sky, cool Moon-light on the left and warm Sun-light on the right meeting at peace, a low ridge line with grass along the bottom edge, a big open sky above, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF D: Dawn Town — Residential Lane (S03-S08)

**Design Brief:** The waking Anatolian town, intimate residential lane — narrow enclosed cobblestone street, stone-and-plaster houses with red tile roofs, wooden doors and shutters, potted plants, chimney smoke, warm sunrise at the curving far end. CyberAnatolian texture present but never foregrounded. The intimate street canyon of the walk's first movement.

**Environment Geometry (approved pixels, 2026-07-07):** Warm golden sunrise. A **narrow cobblestone lane curving and receding toward the town** and a forested hill at the far (sun-hazed) end. Stone-and-plaster houses with **red tile roofs** framing both sides, overhanging timber upper floors (cumba), wooden shutters and doors; **potted geraniums along the base of the LEFT wall**; a **chimney trailing smoke, left-center**; a **utility pole with a satellite dish on the RIGHT** and cables crossing overhead; a solar panel on a mid roof. Eye-level, lane receding center and curving to the right. Warm amber palette (fuller sun than pre-dawn). Beside-space open along the lane.

**Narrative anchors:** the beside-space stays open along the street (companion's side); the lane runs open toward the town = the walk's direction of travel; the tile roofs + stone-plaster walls + roof-dish motif are the town's through-anchor shared with REF E and REF F.

**Reference Image Path:** `episode-10/04_visuals/raw/ep10_ref_dawn_town.png` — APPROVED, frozen (2026-07-06).
**Scope note:** serves **S03-S08 only**; S11-S12 -> REF E, S19-S22 -> REF F (see LOCATION DECOMPOSITION).

**Text Prompt:**
> Wide establishing shot of a narrow Anatolian small-town street at early sunrise, no characters, weathered stone and plaster buildings with shutters and low rooftops framing the street, ordinary weathered technology grown quietly into everyday life in the background such as a patched antenna, an old cable run and a salvaged panel, never foregrounded, the street running open and receding toward the town, warm sunrise light entering the lanes, chimney smoke and morning haze, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

**Dawn Workers (anonymous ensemble):** no dedicated character reference required (none recurs, none reacts). Generate per-scene; keep mixed men and women of varied ages, plain everyday clothes; flag if drift becomes visible.

---

### REF E: Dawn Town — Market Edge (S11-S12)

**Design Brief:** The town's near/entry market edge, waking at six in the morning — the station of the steadfast souls. A widening in the lanes where dawn vendors set up. Four gestures, one grammar — hands extending. Bread-and-smoke warmth. A sibling of REF D (same town, one movement later, one street wider).

**Environment Geometry (approved pixels, 2026-07-07):** Wider cobblestone street at golden sunrise (a **widening** vs REF D's enclosed lane). **RIGHT side:** a baker's shopfront with a **dark wood-fired oven mouth glowing orange**, a metal roll-up shutter, a **red simit cart** stacked with bread rings, and a **tea stand with a tall samovar and glasses on a white-clothed table**. **LEFT side:** stone houses with red tile roofs, one with **green-painted upper plaster**, potted plants, wooden doors. **Near foreground center-left: a metal dog-food bowl on the cobbles.** Utility pole center with wires; a TV antenna on a right roof; a satellite dish on a right roof. Scrubby hills behind the rooftops, warm sun-haze at the street's far bend. Eye-level. Beside-space open along the street.

**Narrative anchors:** the four extending hands (vendor, baker, woman feeding the animals, shopkeeper) are the "steadfast souls" grammar Robotiko's walking rhymes against — composable without anyone reacting to or framing him as special; the beside-space stays open; the dog-bowl and the trotting street dog (S12) live in the near foreground.

**Through-anchors (sibling of REF D + REF F):** shared morning-palette (fuller sunrise than REF D's lane, one continuous dawn); single low eastern sun, shadows consistent with REF D/REF F; co-visible landmarks — **red tile roofs, stone-and-plaster walls, roof satellite-dish + utility-pole motif, the highland ridge behind**. No cross-ref typology clash.

**Reference Image Path:** `episode-10/04_visuals/raw/ep10_ref_market_edge.png` — APPROVED, frozen (2026-07-07).

**Text Prompt:**
> Wide establishing shot of a small Anatolian town market edge at full sunrise, no characters, a widening in the narrow lanes where dawn vendors are setting up, weathered stone and plaster buildings with red tile roofs and low rooftops framing the space, a simit bread cart and a small tea stand on one side, a baker's shopfront with a dark wood-fired oven mouth, a metal roll-up shopfront shutter half raised, a low bowl of food set out at the curb in the near foreground for street dogs and cats, ordinary weathered technology grown quietly into everyday life in the background such as a patched antenna, a roof satellite dish, utility poles and an old cable run, never foregrounded, full warm sunrise light entering the lanes from a low eastern sun, bread and wood-smoke haze in the air, the highland ridge line just visible behind the rooftops, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF F: Dawn Town — Far-Edge Descent (S19-S22)

**Design Brief:** The town's far/exit edge on the descent — a more commercial outer street sloping downhill out of town, opening onto an open horizon where a distant glass tower stands (the System, intact, still operating, a cold sun-glint). Full morning. A sibling of REF D and REF E — the same town, seen on the way out and down.

**Environment Geometry (approved pixels, 2026-07-07):** Descending commercial street, low warm morning sun near the horizon. **LEFT:** stone houses with red tile roofs (a **satellite dish on the near roof**) giving way to shopfronts with large display windows. **RIGHT:** a long row of **metal roll-up shutters throwing hard striped light/shadow bands across the road**; a streetlight and utility poles. **Near foreground center-right: a curbside charcoal brazier of glowing orange-red embers**, smoke drifting up through a bar of sun. The cobblestone road **slopes downhill and opens to the horizon** where a **single distant glass tower stands small**, the sun blazing right beside it as a cold glint. Dry open hills on the far-left horizon. Warm gold with the striped shutter-shadows on the right. Beside-space open along the descending road.

**Narrative anchors:** the distant glass tower is a cold glint in a warm world — the System no longer inside him; the ref places it small on the horizon so a scene keeps his gaze on the road; the brazier embers are orange-red (Amber Pulse lock: amber is S10 only); the fence/shutter stripes are "binary as daylight" underfoot texture; the beside-space stays open.

**Through-anchors (sibling of REF D + REF E):** shared morning-palette (full morning, one continuous dawn resolved to day); single low eastern sun consistent with REF D/REF E; co-visible landmarks — **red tile roofs, stone-and-plaster walls, roof satellite-dish + utility-pole motif**. The **distant glass tower** is the one NEW landmark unique to this sibling. No cross-ref typology clash.

**Reference Image Path:** `episode-10/04_visuals/raw/ep10_ref_far_edge.png` — APPROVED, frozen (2026-07-07).

**Text Prompt:**
> Wide establishing shot of the far edge of a small Anatolian town on the descending road out of town at full morning, no characters, the street sloping downhill and opening toward an open horizon, weathered stone and plaster buildings with red tile roofs giving way to more commercial shopfronts along the descent, a row of shop display windows on one side, a long fence and half-raised metal shutters throwing striped bands of light and shadow across the road, a curbside charcoal brazier of orange-red embers low in the frame with smoke drifting sideways through a bar of sun, ordinary weathered technology grown quietly into everyday life such as a roof satellite dish, utility poles and an old cable run, never foregrounded, on the far horizon a single distant glass tower standing small and intact with cold morning sun flaring off its glass face as a cold glint in a warm world, full warm morning light across the street from a low eastern sun, the highland ridge line behind the town, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## SCENE-TO-SPACE COVERAGE MAP

Every dramaturgy scene mapped to its camera-space and reference. Ref-less scenes carry the emotional payload and are signed off against dramaturgy grammar (see Ref-less Scene Gate), not framed to an image.

| Scene | Camera-space | Ref | Narrative role |
|---|---|---|---|
| S01 | workshop exterior in landscape | EP09 chain-base (Rule 4c) | The world before the walk |
| S02a/b | workshop shutter + doorway (silhouette) | EP09 chain-base (Rule 4c) | The shutter opens |
| S03 | mouth of the residential lane | **D** | The threshold |
| S04 | road-level macro (foot + dew) | ref-less (macro), D-anchored | First footstep |
| S05 | roadside detail: machine carcass + ivy | **D** | Duality composted I |
| S06 | roof/roadside detail: antenna nest + sign | **D** | Duality composted II |
| S07 | close faces at lane windows/doorways | **D** (near ref-less) | Faces at dawn |
| S08a/b/c | macro triptych: leaf / frost / forearm seam | ref-less (macro) | The fractal rhyme |
| S09 | crossroads + planted staff | **B** | The crossroads |
| S10a/b | crossroads + staff (hand, Amber Pulse) | **B** | The touch and the Amber Pulse |
| S11 | market edge (four extending hands) | **E** | The steadfast souls |
| S12 | walking through the waking market | **E** | Among them |
| S13 | leaving town, town below and behind | D->C transition (chain) | Leaving the town |
| S14 | ridge path, grass waves, town sinking | **C** (lower ridge vantage) | The climb |
| S15 | ridge crest, Moon-Sun sky | **C** | The Moon-Sun sky |
| S16 | ridge crest, Moon-Sun sky + crane flock | **C** (base = S15 output) | The crane flock |
| S17 | ridge crest, close profile, sky on chrome | **C** | Beside him at the crest |
| S18 | ridge turning to far side; meadow distant | **C** (meadow A distant in bg) | The far slope |
| S19 | far-edge descent, distant glass tower | **F** | The tower, distant |
| S20 | far-edge shop-window row (loops) | **F** | The loops, powerless |
| S21 | far-edge curbside brazier (embers) | **F** | Amid these embers |
| S22 | far-edge fence + shutters, striped shadow | **F** | Binary as daylight |
| S23 | body macro: forearm/chest gold seam | ref-less (macro/body) | Love's vein of light |
| S24 | last rocky slope into the meadow | **A** (chain from S18) | Down from the peaks |
| S25 | meadow + infinity stone (children, kettle) | **A** | The infinity stone, ordinary |
| S26 | meadow + infinity stone (pours two glasses) | **A** (chain S25) | Two glasses, one pot |
| S27a/b | fourth-wall close: hand extends glass | ref-less (fourth-wall), A-anchored | The Hand (beat one) |
| S28 | meadow at the stone (walk resumes) | **A** (chain S26) | The walk resumes |
| S29 | low meadow ground: two track-lines | ref-less (tracks), A-anchored | The tracks |
| S30 | open meadow, full-stride walking | **A** | Refrain one, straight |
| S31 | mid-meadow, half-turn to companion | **A** (grammar-break scene) | The wait |
| S32 | meadow road through monolith country | **A** | Refrain two, elongated |
| S33 | meadow, walking into low sun, wind/flare | **A** | Refrain three, the scream |
| S34a/b | fourth-wall close: look + tilt + beckon | ref-less (fourth-wall), A-anchored | The look and the beckon (beat two) |
| S35 | white text on black | N/A — edit card, no image | The gong = the door |

**Coverage verdict:** all 35 scenes accounted for. Environment refs A-F + EP09 chain-base (S01-S02) + ref-less macro/fourth-wall/tracks scenes. All six references exist and are approved. No loop-back triggered at Phase-2 batch verification.

---

## PER-SPACE CAMERA LEDGER

One row per env-referenced scene, confirming angles vary within each space (Camera Diversity) and landmarks stay on consistent screen-sides (no unexplained flips). Ref-less scenes appear in the Ref-less Scene Gate instead.

| Space | Ref | Scene | Camera position & heading | Landmark screen-side |
|---|---|---|---|---|
| workshop exterior | EP09 base | S01 | wide, town in landscape, workshop small low-center | workshop low-center; ridge back |
| workshop exterior | EP09 base | S02a | street-level frontal on the closed shutter | shutter fills back wall |
| workshop exterior | EP09 base | S02b | street-level frontal, shutter up, silhouette in doorway | doorway/glow center |
| residential lane | **D** | S03 | eye-level at the lane mouth, heading down-lane toward town, android off-center left | dish right; lane recedes center; plants left |
| residential lane | **D** | S05 | eye-level three-quarter facing the left wall base, android passing left mid-ground | machine carcass + plants left |
| residential lane | **D** | S06 | eye-level looking up toward a low roof, android small at street level | roof dish + shop sign upper |
| residential lane | **D** | S07 | intimate eye-level at a window then a doorstep | window left / doorway right |
| crossroads | **B** | S09 | eye-level wide, android approaching from foreground left, staff center-right | staff center-right; dish far-left |
| crossroads | **B** | S10a | eye-level medium three-quarter, hand on the wood, staff center | staff center; peaks behind |
| crossroads | **B** | S10b | eye-level medium, android stepped back, sun on the amber tip | staff center; warm tip |
| market edge | **E** | S11 | eye-level facing the vendor side, four extending hands | oven/cart right; dog-bowl foreground |
| market edge | **E** | S12 | tracking-height among the street, heading down-lane, dog trotting | oven right; dog-bowl foreground |
| ridge (Moon-Sun) | **C** | S14 | three-quarter from beside-left on the ridge path, town sinking below-left | valley/town below-left |
| ridge (Moon-Sun) | **C** | S15 | wide, sky 80%, android small on the ridge line between the bodies | Moon left; Sun right |
| ridge (Moon-Sun) | **C** | S16 | wide (base=S15), crane V crossing Moon-side to Sun-side, android low | Moon left; Sun right; flock mid-sky |
| ridge (Moon-Sun) | **C** | S17 | close profile facing the Sun side (right), sky on chrome | sky behind; profile faces right |
| ridge (Moon-Sun) | **C** | S18 | wide from beside-left, android turned down the far slope, meadow far below | meadow/valley below; ridge behind |
| far edge | **F** | S19 | eye-level, heading down-road, head forward, tower on horizon | tower horizon center-right |
| far edge | **F** | S20 | eye-level facing the left shop-window row, android passing | shop windows left |
| far edge | **F** | S21 | eye-level, brazier in near foreground, android passing within arm's reach | brazier foreground center-right |
| far edge | **F** | S22 | eye-level, android walking through the striped bands | shutters right; stripes across road |
| meadow | **A** | S24 | eye-level on the last rocky slope, ridge backlit behind, meadow ahead | monolith mountains left/behind; meadow ahead |
| meadow | **A** | S25 | eye-level wide, infinity-stone across mid-ground, android arriving frame edge | infinity-stone center-foreground; monolith left-bg |
| meadow | **A** | S26 | eye-level medium, android seated on the fallen loop, two glasses on the stone | stone foreground; two glasses center |
| meadow | **A** | S28 | three-quarter rear-left, android walking away, glass left on the stone behind | infinity-stone behind him; meadow ahead |
| meadow | **A** | S30 | eye-level full-stride, open meadow, beside-space level with shoulder | monolith mountains bg; open meadow |
| meadow | **A** | S31 | eye-level medium, android stopped, half-turned to the beside-space | open meadow behind; beside-space foreground |
| meadow | **A** | S32 | wide, meadow road ahead through monolith country, android small mid-frame | monolith mountains bg; road ahead |
| meadow | **A** | S33 | eye-level, android walking into the low frontal sun, flare crossing | low sun ahead; wind-silvered grass |

Landmark screen-sides are internally consistent within each space (dish right in the lane; oven right + dog-bowl foreground in the market; Moon left / Sun right across all ridge shots; tower horizon center-right at the far edge; monolith mountains left/back across the meadow). No unexplained flips.

---

## REF-LESS SCENE GATE (signed off against dramaturgy grammar, not against an image)

These scenes have no environment reference. Each is checked against its dramaturgy grammar obligations (the LOCKS), not framed to pixels.

| Scene | Type | Grammar checks (must pass) |
|---|---|---|
| S04 | macro (foot + dew), D-anchored | foot lands on the first stomp-clap beat; beat = step from here; no full figure; warm side-light; no invented second foot/figure |
| S08a | macro (leaf veins) | branching pattern enters lower-left at the match-cut diagonal; backlit gold-on-dark; no figure |
| S08b | macro (frost on glass) | same corner + matching diagonal as S08a; melting edges; backlit gold-on-dark |
| S08c | macro (forearm gold seam) | same corner + matching diagonal; OUTER forearm only (inner etchings kept off-frame, never lit); gold seam = kintsugi (allowlisted), not eye-glow |
| S23 | body macro (forearm/chest seam) | outer forearm + chest only; inner forearm turned away from the light; seam-gold = sun-gold; no eyes in frame (no glow risk) |
| S27a/b | fourth-wall (hand + glass), A-anchored | **GAZE: eyes on the glass, BELOW the lens — NO eye contact** (reject any eye-contact take); mouthless face (no mouth/smile); second glass left on the stone; steam between hand and lens |
| S29 | tracks-only, A-anchored | two track-lines side by side (metal tread + bare human foot), same direction/stride; low grass-height; the human never shown; empty meadow around the tracks (no spawned figure) |
| S34a | fourth-wall (the look), A-anchored | **GAZE: the ONLY direct look into the lens in the episode**; level, patient, kind; mouthless face (warmth without a mouth); Still Hold (no camera-move words) |
| S34b | fourth-wall (tilt + beckon), A-anchored | gaze held into the lens (from S34a); soft head tilt = the machine's smile (mouthless — NO mouth/teeth); one open palm-up hand rising, fingers curling once in a small beckon; no big wave |

---

## GENERATED PROMPTS

---

## INTRO — THE WORLD, FIRST (0:00 - 0:27)

#### S01 — The World, First
- **Timestamp:** 0:00 - 0:09
- **Dramaturgy Reference:** S01 ("THE WORLD, FIRST" — exactly where EP09 left the world; nothing moves but the smoke)
- **Characters Present:** None
- **Image Reference Path:** EP09 chain-base (`ep09_ref_exterior.png` + EP09 final dawn frame)
- **Video Tech Strategy:** Standard (Mode A), minimal motion (smoke only)
- **Composition Notes:** Color-journey band 1 — his gold distinct in pre-dawn grey-blue (the workshop seams). Beside-space N/A (no figure). Headroom above the roofs for the ridge rim.
- **Upload:** base: EP09 final dawn frame; env chain: `ep09_ref_exterior.png`
- **Text Prompt:**
> Wide establishing shot of an Anatolian town in pre-dawn grey-blue, no characters, a small workshop building low in the landscape (ep09_ref_exterior.png) with warm gold light seeping from its closed shutter seams and wall cracks, thin chimney smoke rising straight in the still air, red tile rooftops holding the last cold of night, beyond the roofs a ridge line carrying the first warm rim of the coming sun, cold blue-grey air with one warm gold accent at the shutter, everything still and one breath before waking, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S02a — The Shutter Opens (start frame)
- **Timestamp:** 0:10 - 0:18
- **Dramaturgy Reference:** S02 ("THE SHUTTER OPENS" — EP09's final image reversed) — Mode B start
- **Characters Present:** None (shutter closed)
- **Image Reference Path:** EP09 chain-base
- **Video Tech Strategy:** Start-End (Mode B) — this is the START frame (shutter down)
- **Composition Notes:** Headroom above the shutter for the rise. Grey-blue street, gold leaking at the seams (color band 1). Interior never shown.
- **Upload:** base: EP09 dawn-threshold frame; env chain: `ep09_ref_exterior.png`
- **Text Prompt:**
> Exterior street-level shot at dawn, no characters, a workshop corrugated metal roll-up shutter fully closed (ep09_ref_exterior.png), warm gold light leaking through the shutter seams and the gap at its base into the grey-blue street, worn threshold stones in the foreground, cold blue-grey morning air, quiet and still, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S02b — The Shutter Opens (end frame)
- **Timestamp:** 0:10 - 0:18
- **Dramaturgy Reference:** S02 — Mode B end (shutter up, silhouette in the light-filled doorway)
- **Characters Present:** Robotiko (silhouette, full kintsugi edge-lit)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — END frame; one clear change (shutter up)
- **Composition Notes:** Doorway reads as pure warm light — **interior must stay unreadable**. Silhouette = single figure (no guard needed). Mouthless (silhouette, no face detail). Two golds meeting on the ground.
- **Upload:** `android_kintsugi.png`; base: EP09 dawn-threshold frame; env chain: `ep09_ref_exterior.png`
- **Text Prompt:**
> Exterior street-level shot at dawn, the workshop roll-up shutter now fully raised (ep09_ref_exterior.png), warm gold interior light spilling across the threshold stones into the grey-blue street, the chrome android (android_kintsugi.png) standing in the doorway as a dark patchwork silhouette against the pure warm glow, gold-seamed edges catching the light, the interior behind him unreadable pure warm light, two golds meeting on the ground his spilling out and the morning arriving, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S03 — The Threshold
- **Timestamp:** 0:19 - 0:27
- **Dramaturgy Reference:** S03 ("THE THRESHOLD" — steps onto the street, stands, looks outward, no look back; bass pulse enters)
- **Characters Present:** Robotiko (full kintsugi)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** LOCKS bound here — Companion Camera (beside-space open at his RIGHT); color band 1 (his gold distinct in grey-blue lifting). Framed to REF D at the lane mouth. He faces outward down the lane (positive pose, not "no look back" as an instruction). Headroom + open right side for motion.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_dawn_town.png`
- **Text Prompt:**
> Eye-level wide shot at the mouth of a narrow Anatolian cobblestone lane at early sunrise (ep10_ref_dawn_town.png), the chrome android (android_kintsugi.png) standing on the street off-center left with his weight settling onto the leading foot, facing outward down the lane toward the town, stone-and-plaster houses with red tile roofs framing both sides, potted geraniums along the left wall, a chimney trailing smoke, the lane running open and receding toward the town, grey-blue light lifting to warm at the far end, the space at his right kept open, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## VERSE 1 — THE FIRST FOOTSTEP (0:28 - 0:46)

#### S04 — The First Footstep
- **Timestamp:** 0:28 - 0:33
- **Dramaturgy Reference:** S04 ("THE FIRST FOOTSTEP" — foot lands on the first stomp-clap downbeat; from here beat = step)
- **Characters Present:** Robotiko (foot/legs only)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), macro
- **Composition Notes:** Ref-less macro (D-anchored). No full figure -> no anti-spawn guard. Dew scatter + dust ring on the beat. Warm low side-light.
- **Upload:** `android_kintsugi.png` (foot detail)
- **Text Prompt:**
> Low macro shot at road level on a dirt-and-cobble Anatolian street at sunrise, a patched chrome android foot (android_kintsugi.png) swinging forward and landing on the ground, dew scattering and a small ring of dust lifting at the point of impact, warm low side-light raking across the dirt and the dew drops, shallow focus on the foot and the scattering dew, the morning street softly blurred behind, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S05 — Duality, Composted I
- **Timestamp:** 0:34 - 0:40
- **Dramaturgy Reference:** S05 ("DUALITY, COMPOSTED — I" — ivy through a rusted machine carcass; he passes without stopping)
- **Characters Present:** Robotiko (passing)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF D, three-quarter facing the left wall base. Green + rust in one warmth (color band 1 easing warmer). Beside-space open. The camera notices, he does not (positive: walking at pace).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_dawn_town.png`
- **Text Prompt:**
> Eye-level three-quarter shot along a narrow Anatolian lane at sunrise (ep10_ref_dawn_town.png), at the roadside a rusted machine carcass with green ivy growing straight through its empty ribcage and servo sockets, dew resting on leaf and metal alike, the chrome android (android_kintsugi.png) walking past at the left mid-ground at an even pace, stone-and-plaster walls and red tile roofs, warm building sunrise light, green and rust held in one warmth, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S06 — Duality, Composted II
- **Timestamp:** 0:41 - 0:46
- **Dramaturgy Reference:** S06 ("DUALITY, COMPOSTED — II" — dish antenna with a straw nest, shop sign patched with a circuit board; the world's repairs match his own)
- **Characters Present:** Robotiko (passing, small)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF D looking up toward a low roof. CyberAnatolian texture foregrounded here intentionally (the repair rhyme) but not neon. Warm low sun.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_dawn_town.png`
- **Text Prompt:**
> Eye-level shot looking up along a waking Anatolian lane at sunrise (ep10_ref_dawn_town.png), a dish antenna tilted skyward on a low tile roof with a wild straw bird nest packed in its bowl, below it a hand-painted shop sign patched neatly with a salvaged circuit board whose solder traces continue the painted vine, the chrome android (android_kintsugi.png) passing small at street level, warm low sun on the straw, the paint and the copper traces, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## VERSE 2 — FACES AND THE FRACTAL (0:47 - 0:59)

#### S07 — Faces at Dawn
- **Timestamp:** 0:47 - 0:52
- **Dramaturgy Reference:** S07 ("FACES AT DAWN" — a woman at a window with a tea glass, an old man lacing shoes; no one poses, no one notices him)
- **Characters Present:** Dawn Workers (faces; no reaction to Robotiko)
- **Image Reference Path:** N/A (Dawn Workers — no dedicated ref; per-scene, mixed)
- **Video Tech Strategy:** Standard (Mode A), intimate
- **Composition Notes:** Near ref-less (D-anchored). Intentional multi-figure (two townsfolk) -> no solo anti-spawn guard; specify count + mixed. Warm window/doorway light. No one looks at the camera (positive: unposed, faces turned to their tasks).
- **Upload:** env: `ep10_ref_dawn_town.png`
- **Text Prompt:**
> Warm intimate close shots of ordinary Anatolian faces at sunrise along a stone lane (ep10_ref_dawn_town.png), a middle-aged woman at a shuttered window holding a steaming tea glass and an old man on a stone doorstep lacing worn shoes, both sleep-creased and unposed with their attention on their own morning, low warm window-light and doorway light, brow lines and laugh lines reading like the town's own weathering, two ordinary townsfolk a woman and a man, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S08a — The Fractal Rhyme (leaf)
- **Timestamp:** 0:53 - 0:59
- **Dramaturgy Reference:** S08 frame a ("THE FRACTAL RHYME" — leaf veins backlit by sunrise)
- **Characters Present:** None
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Three quick images (~2s each), rhyme made in the edit — do NOT morph
- **Composition Notes:** Ref-less macro. Branching structure enters from the same corner at the same angle as S08b/c (match-cut contract). Backlit gold-on-dark.
- **Upload:** none
- **Text Prompt:**
> Macro shot of green leaf veins backlit by sunrise, the branching vein pattern glowing gold-on-dark, the structure entering from the lower-left corner along a diagonal, warm backlight through the leaf, shallow focus, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S08b — The Fractal Rhyme (frost)
- **Timestamp:** 0:53 - 0:59
- **Dramaturgy Reference:** S08 frame b (frost branching across a windowpane, melting at its edges)
- **Characters Present:** None
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Second of three match-cut images
- **Composition Notes:** Same corner + matching diagonal as S08a. Melting edges. Backlit gold-on-dark.
- **Upload:** none
- **Text Prompt:**
> Macro shot of frost branching across a windowpane at sunrise, the fractal ice pattern glowing gold-on-dark, melting to clear droplets at its edges, the structure entering from the lower-left corner along a matching diagonal, warm backlight behind the glass, shallow focus, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S08c — The Fractal Rhyme (forearm seam)
- **Timestamp:** 0:53 - 0:59
- **Dramaturgy Reference:** S08 frame c (gold seams branching along Robotiko's forearm mid-stride)
- **Characters Present:** Robotiko (forearm only)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Third of three match-cut images
- **Composition Notes:** Same corner + matching diagonal. OUTER forearm only (inner-forearm etchings kept off-frame, never lit). Gold seam = kintsugi (allowlisted), not eye-glow. Backlit gold-on-dark.
- **Upload:** `android_kintsugi.png` (outer forearm detail)
- **Text Prompt:**
> Macro shot of the gold kintsugi seams branching along a chrome android outer forearm (android_kintsugi.png) mid-stride, the gold seam pattern glowing warm gold-on-dark, the structure entering from the lower-left corner along a matching diagonal, warm sunrise backlight on the patched chrome, the outer forearm surface only, shallow focus, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## VERSE 3 — THE CROSSROADS AND THE STEADFAST SOULS (1:00 - 1:20)

#### S09 — The Crossroads
- **Timestamp:** 1:00 - 1:05
- **Dramaturgy Reference:** S09 ("THE CROSSROADS" — the Mentor's staff planted as a waymark; his stride slows as he approaches)
- **Characters Present:** Robotiko; the staff (Mentor's echo — object only)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF B; android approaches from foreground left so the staff sits center-right and the beside-space stays open. **Amber tip DORMANT here** (the Pulse is S10b). Cool earth tones (color band still cool). No amber except the future S10b.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_crossroads.png`
- **Text Prompt:**
> Eye-level wide shot of a highland crossroads at pre-dawn where dirt tracks converge (ep10_ref_crossroads.png), a wooden waymark staff of dark gnarled wood planted upright in the packed earth center-right, a few faded cloth strips knotted below its head, its raw amber tip dark and dormant in the cool shade, the chrome android (android_kintsugi.png) approaching from the foreground left at a slowing walk, semi-arid green highland scrub and low weathered stone remnants, a lone satellite dish on the far-left hillside, distant peaks catching the first faint dawn light, morning mist in the valley, cool earth tones, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S10a — The Touch (start frame)
- **Timestamp:** 1:06 - 1:11
- **Dramaturgy Reference:** S10 ("THE TOUCH AND THE AMBER PULSE" — full stop #1) — Mode B start (hand on wood, tip in shade)
- **Characters Present:** Robotiko; the staff
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — START frame (tip in shade)
- **Composition Notes:** Framed to REF B, medium three-quarter on the hand-on-wood. **Tip still DORMANT** (the Pulse fires in S10b). One element will change (light state); environment stable.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_crossroads.png`
- **Text Prompt:**
> Eye-level medium shot at a highland crossroads at dawn (ep10_ref_crossroads.png), the chrome android (android_kintsugi.png) stopped at the planted waymark staff and laying his patched hand on the dark gnarled wood, the raw amber tip still dark and dormant in shade above his hand, faded cloth strips knotted below the head, cool earth tones with the sun not yet on the crossroads, distant peaks behind, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S10b — The Amber Pulse (end frame)
- **Timestamp:** 1:06 - 1:11
- **Dramaturgy Reference:** S10 — Mode B end (hand released, the rising sun catches the amber tip; the episode's single Amber Pulse)
- **Characters Present:** Robotiko; the staff
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — END frame (Amber Pulse)
- **Composition Notes:** **THE SINGLE AMBER PULSE of the episode — S10b only.** The flare is reflected sunlight (a warm glint), not a light source, and appears ONLY on the staff tip; the surrounding highland stays cool. Budget spent here; no amber anywhere else. The amber is on the staff, not the eyes (eye-glow rule intact).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_crossroads.png`
- **Text Prompt:**
> Eye-level medium shot at a highland crossroads as the sun clears the horizon (ep10_ref_crossroads.png), the chrome android (android_kintsugi.png) stepping back with his hand released from the planted waymark staff, the rising sun catching the raw amber tip so it flares warm for one breath as reflected sunlight, a single warm amber glint on the staff tip and nowhere else, the surrounding highland still in cool morning tones, faded cloth strips below the head, distant peaks behind, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S11 — The Steadfast Souls
- **Timestamp:** 1:12 - 1:16
- **Dramaturgy Reference:** S11 ("THE STEADFAST SOULS" — four gestures, one grammar: hands extending; the station of the steadfast souls is a town at six in the morning)
- **Characters Present:** Dawn Workers (mixed ensemble; none reacts). Robotiko NOT in frame.
- **Image Reference Path:** N/A (Dawn Workers — per-scene, mixed)
- **Video Tech Strategy:** Standard (Mode A), crowd micro-motion
- **Composition Notes:** Framed to REF E facing the vendor side. Intentional multi-figure (4 townsfolk) -> no solo guard; specify count + mixed. Oven mouth glows orange (not amber — this is fire, allowed). Full sunrise. None looks at the camera.
- **Upload:** env: `ep10_ref_market_edge.png`
- **Text Prompt:**
> Eye-level wide shot of a waking Anatolian market edge at full sunrise (ep10_ref_market_edge.png), four townsfolk in one rhyme of extending hands, a simit vendor handing a bread ring to a tea boy at a red cart, a baker sliding bread from a dark glowing wood-fired oven mouth with flour to the elbows, a woman setting a bowl of food down at the curb for street dogs, and a shopkeeper raising a metal shutter with both hands, stone-and-plaster houses with red tile roofs, a tea stand with a tall samovar, full warm sunrise and bread-and-smoke haze, mixed men and women of varied ages going about the morning, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S12 — Among Them
- **Timestamp:** 1:17 - 1:20
- **Dramaturgy Reference:** S12 ("AMONG THEM" — he walks the market at their pace, unremarkable and belonging; a dog trots past toward the bowl)
- **Characters Present:** Robotiko + Dawn Workers
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), tracking-height
- **Composition Notes:** Framed to REF E, tracking-height among the street heading down-lane. He is neither lit nor framed as special (Companion grammar). Intentional multi-figure (townsfolk + dog) -> no solo guard. Oven right, dog-bowl foreground (consistent with S11).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_market_edge.png`
- **Text Prompt:**
> Eye-level tracking-height shot through a waking Anatolian market street at sunrise (ep10_ref_market_edge.png), the chrome android (android_kintsugi.png) walking down the lane at the townsfolk's own pace, one ordinary figure in the traffic of bread and shutters, a street dog trotting past him toward a food bowl at the curb, vendors and a red simit cart to the side, no one greeting him or staring, red tile roofs and warm sunrise haze, mixed townsfolk going about the morning, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## INSTRUMENTAL BREAK — THE RIDGE, THE ONE WIDE SKY (1:21 - 2:21)

#### S13 — Leaving the Town
- **Timestamp:** 1:21 - 1:32
- **Dramaturgy Reference:** S13 ("LEAVING THE TOWN" — the road rises out of the lanes; the town gathers its first full sun below and behind; thin gold in the world's seams)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), D->C transition (chain)
- **Composition Notes:** Color band 2 begins — the world's warmth rising to meet his. **Rear-view ear rule:** three-quarter view from his LEFT (intact left ear toward camera). Town rooftops below-left, ridge ahead. Chain from the town texture (REF D) toward the ridge (REF C).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_dawn_town.png` + `ep10_ref_moonsun_sky.png`
- **Text Prompt:**
> Eye-level shot on a rising dirt road leaving an Anatolian town at full sunrise (ep10_ref_dawn_town.png), the chrome android (android_kintsugi.png) climbing the road away from the camera at an unhurried walk seen from behind in three-quarter view from his left with the intact left side of his head toward the camera, below and behind him the town gathering its first full sun on red tile rooftops antennas and vine-trellises, thin gold showing in the world's own seams of mortar lines and gutter edges, the highland ridge rising ahead, warm gold light, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S14 — The Climb
- **Timestamp:** 1:33 - 1:44
- **Dramaturgy Reference:** S14 ("THE CLIMB" — alongside him on the ridge path, grass in waves, town sinking; grass-gold and seam-gold converging)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF C's lower ridge path. Beside-space open on the valley side (companion given the view). **Rear-view ear rule:** left side toward camera. Color band 2 — grass-gold and seam-gold read as one metal.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_moonsun_sky.png`
- **Text Prompt:**
> Three-quarter shot from beside and slightly behind on a highland ridge path at high morning (ep10_ref_moonsun_sky.png), the chrome android (android_kintsugi.png) walking the grassy path with the intact left side of his head toward the camera, tall grass bending in waves around him, the town sinking away in the valley below to the left, the sunlit grass-tips and the gold in his seams reading as the same metal, the valley side of the path kept open beside him, high clear morning air, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S15 — The Moon-Sun Sky
- **Timestamp:** 1:45 - 1:56
- **Dramaturgy Reference:** S15 ("THE MOON-SUN SKY" — Moon still hanging while the Sun rises, both in one real dawn sky; he walks the ridge line between them, small)
- **Characters Present:** Robotiko (small in frame)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) with frame-lock (celestial bodies persistent)
- **Composition Notes:** Framed to REF C. Sky 80%; Moon LEFT, Sun RIGHT (both steady). Small figure in big empty sky -> anti-spawn guard ON. Beside-space along the ridge path. The episode's cosmic center.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_moonsun_sky.png`
- **Text Prompt:**
> Wide shot from a high ridge at dawn (ep10_ref_moonsun_sky.png), the dawn sky filling most of the frame with a pale full Moon low on the left and a newly risen Sun on the right, cool Moon-light left and warm Sun-light right meeting at peace, the chrome android (android_kintsugi.png) small on the ridge line in the mid-ground walking between them along the grassy crest, the valley and town far below, a big open sky above, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S16 — The Crane Flock
- **Timestamp:** 1:57 - 2:06
- **Dramaturgy Reference:** S16 ("THE CRANE FLOCK" — a real migrating flock crosses Moon-side to Sun-side; he watches the whole way)
- **Characters Present:** Robotiko (low in frame); crane flock
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A) with strict frame-lock — flock IN the source (base = S15/REF C output), never "birds enter frame"
- **Composition Notes:** **Highest generation-risk shot.** Both celestial bodies persistent, no drift/scale change. Flock as a single coherent V (12-18 birds). Intentional living flock -> no solo anti-spawn guard (the birds are wanted; the guard would fight them). He lifts his head to watch.
- **Upload:** `android_kintsugi.png`; base: 15.png (S15 output); env: `ep10_ref_moonsun_sky.png`
- **Text Prompt:**
> Wide shot from a high ridge at dawn (ep10_ref_moonsun_sky.png), the same dawn sky with a pale full Moon low on the left and a risen Sun on the right, a loose long V of migrating cranes already crossing the open sky from the Moon side toward the Sun side, living birds as dark calligraphy against the clouds, the chrome android (android_kintsugi.png) small and low on the ridge below lifting his head to watch the flock, both celestial bodies steady and unchanged, a big open sky, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S17 — Beside Him at the Crest
- **Timestamp:** 2:07 - 2:13
- **Dramaturgy Reference:** S17 ("BESIDE HIM AT THE CREST" — close profile, dawn sky on chrome, blue lenses tracking the last of the flock; the calmest frame so far)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), Static candidate ("rests with the world")
- **Composition Notes:** Close profile facing the Sun side (right). **Eye canon** — material-lens idiom ("calm steady blue optical lenses ... like polished sapphires"), no glow. **Mouthless guard.** The camera rests in the beside-space. Sky-light on chrome.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_moonsun_sky.png`
- **Text Prompt:**
> Close profile shot at a highland ridge crest at dawn (ep10_ref_moonsun_sky.png), the chrome android head and shoulder (android_kintsugi.png) in profile facing the Sun side to the right, the dawn sky mirrored on his patched chrome, his calm steady blue optical lenses set into chrome sockets like polished sapphires tracking the last of a distant flock, wind pressing the grass in slow waves at his feet, the mouthless face calm, the soft sky behind him, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S18 — The Far Slope
- **Timestamp:** 2:14 - 2:21
- **Dramaturgy Reference:** S18 ("THE FAR SLOPE" — he turns from the sky and starts down; the meadow country opens far below, one pale stone fleck too far to read)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF C, far side; REF A meadow distant in bg (one pale stone fleck, unemphasized). **Rear-view ear rule:** beside his left. Destination shown casually from above (allowed — landscape, not Robotiko, is the high element).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_moonsun_sky.png`
- **Text Prompt:**
> Wide shot from the far side of a highland ridge at morning (ep10_ref_moonsun_sky.png), the chrome android (android_kintsugi.png) turned away from the sky and starting down the far slope seen from beside his left, far below a green meadow valley opening among old monolith mountains with mist burning off it and one small pale fleck of toppled stone too far to read, the destination shown casually from above on the way down, warm morning green, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## VERSE 4 — THE ANSWER BEGINS (2:22 - 2:43)

#### S19 — The Tower, Distant
- **Timestamp:** 2:22 - 2:29
- **Dramaturgy Reference:** S19 ("THE TOWER, DISTANT" — the glass tower small on the horizon, intact; his head does not turn toward it; the System is not destroyed, he is simply no longer inside it)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF F, heading down-road. Tower small on the horizon center-right (a cold glint in a warm world). His head faces forward (positive pose; the not-turning is carried by keeping his heading down-road). Beside-space open at his right.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_far_edge.png`
- **Text Prompt:**
> Eye-level shot on a descending Anatolian street at full morning (ep10_ref_far_edge.png), the chrome android (android_kintsugi.png) walking down the sloping cobbled road with his head facing forward down the road, on the far horizon a single distant glass tower standing small and intact with cold morning sun flaring off its face as a cold glint in the warm world, stone houses with red tile roofs giving way to shopfronts, warm morning light, the space at his right kept open, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S20 — The Loops, Powerless
- **Timestamp:** 2:30 - 2:36
- **Dramaturgy Reference:** S20 ("THE LOOPS, POWERLESS" — shop windows play cold looping screens; the light slides across his chrome and never enters the calm blue lenses, which stay on the road)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF F facing the left shop-window row. Cold blue-white screen flicker against warm street light. **Eye canon** — lenses stay on the road, material-lens idiom, no glow. Forbidden: generic cyberpunk neon (keep the screens cold and cheap, not glamorous).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_far_edge.png`
- **Text Prompt:**
> Eye-level shot along a descending Anatolian street at warm full morning, use ep10_ref_far_edge.png as inspiration for the town architecture and cobblestone style, a row of shop display windows on the left playing cold blue-white looping screens with illegible garbled content, the chrome android (android_kintsugi.png) passing at walking pace with his body angled forward down the road, the cold screen-light sliding across his passing chrome and falling away, his calm steady blue optical lenses set into chrome sockets staying on the road ahead, warm morning gold against the cold flicker, no streetlights on, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S21 — Amid These Embers
- **Timestamp:** 2:37 - 2:43
- **Dramaturgy Reference:** S21 ("AMID THESE EMBERS" — a charcoal brazier glows orange-red at the curb; he passes within arm's reach of the fire that once burned him, now domestic)
- **Characters Present:** Robotiko; vendor + work crew (no reaction)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF F, brazier in the near foreground center-right. **Embers ORANGE-RED, never amber** (Amber Pulse budget already spent at S10b). Intentional multi-figure (vendor + crew, no reaction) -> no solo guard. Smoke through a bar of sun.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_far_edge.png`
- **Text Prompt:**
> Eye-level shot on a descending Anatolian street at morning (ep10_ref_far_edge.png), a street vendor charcoal brazier glowing orange-red at the curb in the near foreground toasting bread, smoke drifting sideways through a bar of sun, the chrome android (android_kintsugi.png) passing within arm's reach of the fire, a small work crew standing at the brazier for their breakfast and paying him no attention, the embers orange-red and domestic, warm morning gold around them, mixed men and women, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## VERSE 5 — LOVE'S VEIN OF LIGHT (2:44 - 2:58)

#### S22 — Binary as Daylight
- **Timestamp:** 2:44 - 2:48
- **Dramaturgy Reference:** S22 ("BINARY AS DAYLIGHT" — striped shadows across the road; he walks through the on-off bands without breaking stride; the old prison as morning texture underfoot)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF F, the shutter/fence stripes across the road. Hard light/dark bands over patchwork chrome; everything else soft. Beside-space open. The stripes are the "binary" cipher (Master numerical cipher — 0/1 underfoot).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_far_edge.png`
- **Text Prompt:**
> Eye-level shot on a descending Anatolian street at morning (ep10_ref_far_edge.png), a long row of half-raised metal shutters and a fence throwing hard striped bands of light and shadow clean across the cobbled road, the chrome android (android_kintsugi.png) walking through the alternating light-and-dark bands without breaking stride, the stripes sliding over his patchwork chrome, everything else soft in warm morning light, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S23 — Love's Vein of Light
- **Timestamp:** 2:49 - 2:53
- **Dramaturgy Reference:** S23 ("LOVE'S VEIN OF LIGHT" — close pass along the gold seam up the outer forearm and across the chest; the repair and the morning one material; inner forearm turned away)
- **Characters Present:** Robotiko (forearm/chest)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), macro
- **Composition Notes:** Ref-less body macro. OUTER forearm + chest only; **inner-forearm etchings turned away from the light, unfeatured.** Seam-gold = sun-gold (kintsugi allowlisted). No eyes in frame (no glow risk). Color band 3 approaching — one warmth.
- **Upload:** `android_kintsugi.png` (forearm/chest detail)
- **Text Prompt:**
> Close macro pass along the gold kintsugi seam running the outside of a chrome android forearm and up across the chest plate (android_kintsugi.png), morning sunlight lying in the seam so evenly that the gold repair and the light are one material, warm gold-on-chrome, the outer forearm and chest surface only with the inner forearm turned away from the light, shallow focus, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S24 — Down from the Peaks
- **Timestamp:** 2:54 - 2:58
- **Dramaturgy Reference:** S24 ("DOWN FROM THE PEAKS" — the last slope out of the high ground; the summit conquered by descending it; the meadow's green has color now)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), chain from S18
- **Composition Notes:** Framed to REF A, the descent INTO the meadow. Ridge backlit behind him; meadow green ahead (color band 3 — one warmth). Beside-space open. This "summit" scene is a descent (Companion grammar — the camera never above him even here).
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`; base: 18.png (S18 output)
- **Text Prompt:**
> Eye-level shot on the last rocky slope down into a green meadow valley at morning (ep10_ref_stone_meadow.png), the chrome android (android_kintsugi.png) stepping down through boulders and broom-grass, the monolith ridge rearing behind him in backlight, ahead the meadow green taking on full color among old monolith mountains, warm morning light, the space at his side kept open, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## VERSE 6 — THE INFINITY STONE AND THE HAND (2:59 - 3:14)

#### S25 — The Infinity Stone, Ordinary
- **Timestamp:** 2:59 - 3:04
- **Dramaturgy Reference:** S25 ("THE INFINITY STONE, ORDINARY" — the toppled stone 8 as an infinity in the green meadow; children on the near loop, shepherd against the far loop, kettle on embers; eye-level, no monument awe)
- **Characters Present:** Robotiko (arriving, edge of frame); girl + boy; old shepherd
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), crowd micro-motion (exact counts, positions locked)
- **Composition Notes:** Framed to REF A. **Eye-level, NO low-angle monument framing, NO light from within the stone.** Intentional multi-figure (2 children + shepherd) -> no solo guard; specify counts, mixed (girl + boy), no reaction to Robotiko. Kettle on **orange-red** embers (not amber). Verse 6 at full band over the ordinary.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`
- **Text Prompt:**
> Eye-level wide shot of a green meadow at full morning in monolith mountain country (ep10_ref_stone_meadow.png), a great toppled stone figure-eight lying in the grass as an infinity of two joined mossed and cracked stone loops across the mid-ground, two children a girl and a boy clambering on the near loop and arguing happily, an old shepherd in a cap leaning against the far loop with a few sheep grazing loose, a blackened kettle resting on orange-red ember-coals near his feet, the chrome android (android_kintsugi.png) just arriving at the edge of the frame, the stone treated as an ordinary place to sit with no monument framing and no light from within it, tall monolith mountains behind, full morning gold, mixed ordinary people paying him no attention, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S26 — Two Glasses, One Pot
- **Timestamp:** 3:05 - 3:09
- **Dramaturgy Reference:** S26 ("TWO GLASSES, ONE POT" — he sits on the fallen loop and pours from the communal kettle into two glasses side by side; two halves of one whole, paid without the apple) [DISSONANCE intentional]
- **Characters Present:** Robotiko; shepherd (asleep, background)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), chain from S25
- **Composition Notes:** Framed to REF A, medium on the seated figure. Two glasses, one pour, steam in cold bright air. Orange-red ember-glow at frame edge. Multi-figure (shepherd bg asleep) -> no solo guard. [DISSONANCE] full band over a quiet act — do not "fix."
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`; base: 25.png (S25 output)
- **Text Prompt:**
> Eye-level medium shot at the toppled infinity stone in a green meadow at morning (ep10_ref_stone_meadow.png), the chrome android (android_kintsugi.png) sitting on the fallen stone loop and pouring tea from a blackened kettle into two small tea glasses set side by side on the stone, steam rising from both glasses in the cold bright air, a shepherd resting asleep against the far loop in the background, orange-red ember-glow at the frame edge, full morning gold, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S27a — The Hand (start frame)
- **Timestamp:** 3:10 - 3:14
- **Dramaturgy Reference:** S27 ("THE HAND" — fourth wall beat one; he lifts one glass, gaze on the glass just below the lens, NO eye contact; second glass stays for the next traveler) — Mode B start
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — START (glass lifted at chest, gaze down)
- **Composition Notes:** Ref-less fourth-wall (A-anchored). Camera at seated companion height (slightly below his eye line). **GAZE DISCIPLINE: eyes on the glass, BELOW the lens — NO eye contact** (the look belongs to S34 alone). **Mouthless guard.** Steam between hand and lens.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png` (anchor)
- **Text Prompt:**
> Fourth-wall close shot at seated companion height in a green meadow at morning, the chrome android (android_kintsugi.png) holding one small steaming tea glass at chest height, his calm steady blue optical lenses set into chrome sockets looking down at the glass just below the camera lens with no eye contact, the mouthless face calm, warm steam between his hand and the lens, a second steaming glass resting on the toppled stone beside him, morning gold, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S27b — The Hand (end frame)
- **Timestamp:** 3:10 - 3:14
- **Dramaturgy Reference:** S27 — Mode B end (arm extended toward the lens into the beside-space, gaze still on the glass; the divide Love broadcasts across is the screen itself)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Start-End (Mode B) — END (arm extended toward lens, gaze still down)
- **Composition Notes:** Same as S27a but the glass is offered toward the camera. **GAZE still on the glass, below the lens — NO eye contact** (reject any eye-contact take). **Mouthless guard.** Second glass left on the stone.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png` (anchor)
- **Text Prompt:**
> Fourth-wall close shot at seated companion height in a green meadow at morning, the chrome android (android_kintsugi.png) extending one small steaming tea glass forward toward the camera into the open space beside him, his calm steady blue optical lenses set into chrome sockets still lowered to the glass just below the lens with no eye contact, the mouthless face calm, warm steam rising between the offered glass and the lens, a second steaming glass left on the toppled stone, morning gold complete, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## FINALE — THE WALK, THE REFRAINS, THE LOOK, THE DOOR (3:15 - 4:34)

#### S28 — The Walk Resumes
- **Timestamp:** 3:15 - 3:23
- **Dramaturgy Reference:** S28 ("THE WALK RESUMES" — he rises and walks on, leaving the second glass steaming on the stone; the guitar solo ignites; the walk continues mid-breath)
- **Characters Present:** Robotiko; children, shepherd (background)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), chain from S26
- **Composition Notes:** Framed to REF A. **Rear-view ear rule:** three-quarter rear from his left (walking away, glass left behind on the stone). Multi-figure (children + shepherd bg still present) -> no solo guard. Nothing announced (Companion grammar). Solo ignites — but the image stays quiet.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`; base: 26.png (S26 output)
- **Text Prompt:**
> Eye-level shot in a green meadow at morning (ep10_ref_stone_meadow.png), the chrome android (android_kintsugi.png) risen and walking on into the meadow away from the toppled infinity stone, seen in three-quarter view from his left with the intact left side of his head toward the camera, a single steaming tea glass left behind on the stone, two children still clambering on the near loop and a shepherd still resting against the far loop in the background, monolith mountains beyond, warm morning gold, the walk continuing unhurried, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S29 — The Tracks
- **Timestamp:** 3:24 - 3:32
- **Dramaturgy Reference:** S29 ("THE TRACKS" — two lines of tracks side by side, a metal tread and a bare human footprint, same direction and stride; the human never shown; two arise)
- **Characters Present:** None in frame (tracks only)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A), Static candidate, macro
- **Composition Notes:** Ref-less tracks (A-anchored). Low grass-height. Two track-lines: patched metal foot + bare human footprint, parallel silver threads in the low sun. The human never shown; the frame never lifts. Empty meadow around the tracks (positive framing, not "no figure").
- **Upload:** none
- **Text Prompt:**
> Low shot almost at grass height in a dew-silver meadow at morning, two lines of tracks pressed side by side into the wet grass, one the tread of a patched metal foot and one a bare human footprint, running in the same direction at the same easy stride, catching the low sun as parallel silver threads, backlit grass bokeh, the meadow grass quiet and empty around the two track-lines, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S30 — Refrain One, Straight
- **Timestamp:** 3:33 - 3:44
- **Dramaturgy Reference:** S30 ("REFRAIN ONE — STRAIGHT" — full-stride walking, the most alive walk; grass parting at his shins; gold complete and indistinguishable; the beside-space keeps pace level with his shoulder)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF A, full-stride. **Color band 3 complete — his gold and the sun's indistinguishable.** Beside-space level with his shoulder. Open meadow -> anti-spawn guard ON. Headroom + forward space for motion.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`
- **Text Prompt:**
> Eye-level full-stride shot of the chrome android (android_kintsugi.png) walking through an open green meadow at full morning (ep10_ref_stone_meadow.png), grass parting at his shins, the gold of his kintsugi seams and the gold of the morning now indistinguishable, monolith mountains warm in the background, the open space kept level with his shoulder beside him, the most alive walk of the morning, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S31 — The Wait
- **Timestamp:** 3:45 - 3:53
- **Dramaturgy Reference:** S31 ("THE WAIT" — the single camera-grammar break; he stops, half-turns toward the beside-space, gaze at companion height NOT the lens, waits, then walks on together)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), body-lock then half-turn (head-turn 5-step pattern at motion stage)
- **Composition Notes:** Framed to REF A. **GAZE: half-turn toward the beside-space, gaze rests at companion height BESIDE the lens — NO eye contact into the lens** (eye contact reserved for S34). **Mouthless guard.** Beside-space foreground clear so the "catching up" reads. Still morning air.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`
- **Text Prompt:**
> Eye-level medium shot of the chrome android (android_kintsugi.png) stopped mid-meadow at morning (ep10_ref_stone_meadow.png), half-turned toward the open space beside him, his calm steady blue optical lenses set into chrome sockets resting at companion height to the side of the camera with no eye contact into the lens, the mouthless face patient and kind, open meadow depth behind him and the beside-space foreground clear, still morning air, warm gold, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S32 — Refrain Two, Elongated
- **Timestamp:** 3:54 - 4:07
- **Dramaturgy Reference:** S32 ("REFRAIN TWO — ELONGATED" — wider; the meadow road ahead through monolith country; the land is only land, the road only a road; no path-shape reveal ever)
- **Characters Present:** Robotiko (small, mid-frame)
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Framed to REF A, widest warmth. Android small mid-frame, beside-space at his shoulder. **NO lemniscate / path-shape reveal** (LOCKS) — the land stays only land, the road only a road. Open meadow, small figure -> anti-spawn guard ON. Epic held quiet.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`
- **Text Prompt:**
> Wide shot of a meadow road running ahead through monolith mountain country at full morning (ep10_ref_stone_meadow.png), the chrome android (android_kintsugi.png) at walking scale mid-frame with the open space kept at his shoulder, gold-lit mountains and an enormous ordinary sky, the land only land and the road only a plain road, widest warm light of the morning, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S33 — Refrain Three, The Scream
- **Timestamp:** 4:08 - 4:15
- **Dramaturgy Reference:** S33 ("REFRAIN THREE — THE SCREAM" — the album's epic peak; he walks into the low sun, flare crossing; one long gust silvers the whole meadow; dew sparks; stride unchanged)
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Standard (Mode A), the episode's highest motion energy (wind + flare + walking), placed before the Still Hold for contrast
- **Composition Notes:** Framed to REF A. Sun low and frontal; flare permitted to cross the lens. **Energy carriers = wind, light, grass ONLY — NO birds, no added elements** (spawn risk; the crane moment stays unique to S16). Grain constant, no crescendo. Open meadow -> anti-spawn guard ON.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png`
- **Text Prompt:**
> Eye-level shot of the chrome android (android_kintsugi.png) walking straight into a low morning sun across an open meadow (ep10_ref_stone_meadow.png), warm lens flare crossing the frame, one long gust sending a bright wave through the whole meadow and throwing dew off the grass in sparks of light, his stride unchanged, the aliveness carried by wind and light and grass, monolith country warm behind, single figure composition, no additional characters, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S34a — The Look (start frame)
- **Timestamp:** 4:16 - 4:29
- **Dramaturgy Reference:** S34 ("THE LOOK AND THE BECKON" — fourth wall beat two, STILL HOLD; the solo fades, he stops, turns his head, the episode's ONLY direct look into the lens; it lands and holds) — the look
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Multi-Clip, camera Static (Still Hold); S34a = head-turn 5-step, hold
- **Composition Notes:** Ref-less fourth-wall (A-anchored), companion height. **GAZE: the ONLY direct look into the lens in the whole episode** — level, patient, kind. **MOUTHLESS GUARD — warmth without any mouth or smile; any invented mouth is a reject.** The most important shot pair of the series. Medium close.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png` (anchor)
- **Text Prompt:**
> Fourth-wall medium close shot at companion height in a green meadow at morning, the chrome android (android_kintsugi.png) eased to a stop and turning his head to give one direct calm look into the camera lens, his calm steady blue optical lenses set into chrome sockets like polished sapphires meeting the lens level and patient and kind, the mouthless face warm and carrying no mouth, morning gold complete, the open space beside him now at the lens, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S34b — The Beckon (end frame)
- **Timestamp:** 4:16 - 4:29
- **Dramaturgy Reference:** S34 — the beckon (a soft head tilt = the machine's smile; one open palm-up hand rising, fingers curling once in a small beckon toward the lens; the gong cuts on the offered hand) — Mode B end from the look-holding state
- **Characters Present:** Robotiko
- **Image Reference Path:** `_assets/cast/android_kintsugi.png`
- **Video Tech Strategy:** Multi-Clip / Mode B candidate — pose held from S34a end-state; single action: head tilt + palm-up beckon
- **Composition Notes:** Gaze held into the lens (from S34a). **The head tilt IS the smile — MOUTHLESS, no mouth/teeth/grin** (a literal smile would invent a mouth = design break; hard reject). One open hand rising palm-up from the lower frame edge, small amplitude (no wave). The series' final image before the gong/door.
- **Upload:** `android_kintsugi.png`; env: `ep10_ref_stone_meadow.png` (anchor); base: 34a.png (S34a output)
- **Text Prompt:**
> Fourth-wall medium close shot at companion height in a green meadow at morning, the chrome android (android_kintsugi.png) holding his direct gaze into the camera lens with his calm steady blue optical lenses set into chrome sockets, his head tilted gently to one side as the machine warmth, the mouthless face carrying no mouth and no smile, one open hand rising palm-up into the lower frame with the fingers curling once in a small beckon toward the lens, morning gold complete, unhurried and ordinary, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

#### S35 — The Gong = The Door
- **Timestamp:** 4:30 - 4:34
- **Dramaturgy Reference:** S35 ("THE GONG = THE DOOR" — fourth wall beat three; on the single final gong, hard cut to black, white text on black for 5 seconds — the GitHub end screen)
- **Characters Present:** None
- **Image Reference Path:** N/A — **EDIT CARD, no image generation.** Sound and cut are one event.
- **Video Tech Strategy:** N/A — packaging/edit deliverable (the series' one end-screen exception)
- **Composition Notes:** White text on black. The repository is the hand extended through the screen; EP01's handshake answered. **No image prompt** — assembled at the edit/packaging stage.
- **Upload:** N/A
- **No Text Prompt:** this is an edit card (white text on black), produced at the CapCut/packaging stage, not generated in Nano Banana. It has no image-generation prompt by design.

---

## POST-GENERATION QUALITY CHECKLIST

Phase-1 items (carried forward):
- [x] Location decomposition applied (operational site-map + landmark test); alarm band checked; <2-scene spaces chained (S01-S02, S13)
- [x] Every reference enumerated and gated at 1R — 6 environment refs + kintsugi body ref; Dawn Workers honestly ref-less
- [x] Sibling refs (D/E/F) declare through-anchors (shared dawn palette, single low eastern sun, red-tile + roof-dish + ridge co-visible landmarks); no cross-ref typology clash
- [x] Each REF block carries Design Brief + Environment Geometry (rewritten to pixels) + Narrative anchors + canonical Reference Image Path + the exact Text-Prompt marker spelled as required
- [x] ART DIRECTION LOCKS present (color bands, single Amber Pulse budget, Companion Camera + gaze discipline, mouthless body-lock, "what is NOT shown")
- [x] Scene->space coverage map complete; ref-less scenes listed
- [x] Phase-1 sentinel REMOVED (this is v02)

Phase-2 items:
- [x] Batch verification pass done — all 6 ref PNGs read pixel-by-pixel; all 35 scenes walked against pixels + coverage map; no gap, no loop-back
- [x] Environment Geometry notes rewritten to the ACTUAL approved pixels (all 6)
- [x] Each scene's Dramaturgy Reference is a cited Shot-ID pointer, not a fresh paraphrase; binding LOCKS named in Composition Notes
- [x] Ref-less scenes signed off against dramaturgy grammar (Ref-less Scene Gate: S04, S08a/b/c, S23, S27a/b, S29, S34a/b)
- [x] Per-space Camera Ledger present; angles vary within each space; no unexplained landmark screen-side flips
- [x] No loop-back references invented (all 6 refs are pre-existing/approved)
- [x] **Completeness check by the Gate-1 (dramaturgy) approver against the approved dramaturgy — Human approved 2026-07-08 (2.6): 35/35 scenes anchor the space their dramaturgy text describes; no scene mapped to another space's ref; all ref-less scenes pass their grammar check.**
- [x] Sentinel ABSENT from v02
- [x] Every image prompt ends with the mandatory style suffix (40/40; S35 is an edit card, no image)
- [x] Short character identifiers bound inline `element (filename.png)` matching Upload; no restated ref detail
- [x] Every Robotiko scene references the phase-correct ref (`android_kintsugi.png`)
- [x] Anti-spawn guard uses Nano Banana phrasing (`single figure composition, no additional characters`); OMITTED on macro/foot (S04, S08, S23, S29), silhouette (S02), fourth-wall solo close (S27, S34), and intentional multi-figure (S07, S11, S12, S16, S21, S25, S26, S28)
- [x] No forbidden aesthetics in any prompt
- [x] Composition space (headroom + beside-space) in every prompt
- [x] Each scene angled to its environment reference — no default dead-centre frontal; angle/composition only, no camera-movement words
- [x] Total image-prompt count matches dramaturgy: 40 (34 scenes + sub-splits; S35 edit card, no image)
- [x] Lighting direction specified in every prompt; no prompt references another prompt
- [x] Every Text Prompt is plain ASCII (no em-dash / non-ASCII inside blockquotes)
- [x] EP10 LOCKS enforced: single Amber Pulse (S10b only; embers orange-red S21/S25/S26); eye canon material-lens idiom; mouthless-face guard (esp. S17/S27/S31/S34); gaze discipline (direct lens ONLY at S34a/b; below/beside at S27/S31); rear-view ear rule (S13/S14/S18/S28); no path-shape reveal (S32)
- [x] **"Would Fibula approve this?" — Human approved 2026-07-08.**

---

## WHAT HAPPENS NEXT

1. **Fibula performs the completeness check (2.6)** against the approved dramaturgy — confirming every scene's reference anchors the same physical space its dramaturgy text describes, no scene is mapped to another space's reference, and every ref-less scene passes its grammar check.
2. Human feeds each scene prompt to Nano Banana (all 6 references already exist from Phase 1) -> variants into `04_visuals/raw/`; attempts logged in `raw/attempts.md` (EP10 = last first-pass-yield window).
3. Human selects the best variant per scene -> `04_visuals/selected/` as `ep10_s01_selected.png`, `ep10_s02a_selected.png`, and so on per scene.
4. Selected images -> `_skills/robotiko-motion-script/SKILL.md` (Checkpoint 2: human approval before video generation).

*Highest-risk shots:* S16 (celestial bodies + flock), S25 (children staging), S27b (gaze discipline), **S34a/b (the series' most important pair — mouthless guard, the only eye-contact frame).*


