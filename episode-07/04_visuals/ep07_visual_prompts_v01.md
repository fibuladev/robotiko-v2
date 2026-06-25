# EP07 — VISUAL PROMPTS
> **Version:** v01 | **Skill:** `_skills/robotiko-visual-prompts/SKILL.md`
> **Generated:** 2026-05-30 | **Model:** Opus + Extended Thinking
> **Dramaturgy:** v01 — APPROVED (2026-05-30)

---

## PRE-GENERATION CHECKLIST

- [x] `_management/master.md` → Visual DNA (Section 3), color palette, forbidden list, mandatory suffix
- [x] `episode-07/03_direction/ep07_dramaturgy_v01.md` → APPROVED, 29 scenes, 11 overrides
- [x] `episode-07/03_direction/ep07_concept_notes.md` → APPROVED, cinematic strategy locked
- [x] `_assets/cast/character_profiles.json` → Phase 2: Destruction (FINAL). Mentor absent. Robochica absent.
- [x] `_assets/cast/android_damaged.png` + `_2.png` + `_3.png` → @Damaged references (3 angles)
- [x] `_memory/lessons.md` → Eye rules, brevity rules, suffix rules internalized

> **Dramaturgy APPROVED. Visual prompt generation authorized.**

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP07 |
| **Title** | The Silence Protocol |
| **Station** | The Surrendering Self (The Dark Night — chosen surrender begins) |
| **Character Phase** | Phase 2: Destruction (FINAL — "barely holding together") |
| **Robotiko Visual State** | Rusted and cracked chrome chassis, sparks flying from joints, glitching blue-red eyes, exposed and fraying analog wires, battle-damaged retro-futuristic body. Cumulative: right ear missing (shrapnel scar, exposed wires at ear socket), torso dent, shoulder scratches, `robochica_1-4` inner-forearm tattoos. |
| **Mentor** | ABSENT — never shown |
| **Robochica** | ABSENT — only forearm tattoos remain |
| **Total Prompts** | 29 (matches dramaturgy scene count) |

---

## MANDATORY STYLE SUFFIX

> Every prompt ends with this exact string. No exceptions.

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## FORBIDDEN AESTHETICS REMINDER

- Clean Apple design
- Pixar-style rendering
- Generic cyberpunk neon
- Smooth plastic textures
- Cheap melodrama or ornamental excess
- "Glowing eyes" / "amber eyes" / any eye-glow keyword (lessons.md)
- Active rain (this is AFTERMATH — wet surfaces, not falling rain)

---

## EP07 ART DIRECTION LOCKS (Never Override)

| # | Lock | Rule |
|---|---|---|
| 1 | **Wet-Grey Aftermath** | Drained Kodachrome — cold grey-blue → black. Wet asphalt, fog, standing water. NOT active rain. One atmosphere unifies every location. |
| 2 | **Temporal Spine** | Twilight (S01-S03) → dusk (S04-S06) → dusk/evening (S10-S17) → night (S19-S21) → deep night (S22-S24) → first-light direction (S27-S29). |
| 3 | **Architecture Cage** | Robotiko <30% of frame. Vast indifferent modern spaces. Depth composition (FG/MG/BG). |
| 4 | **Dual Device** | Wet reflections = the SELF. Eye-projection = the WORLD'S NOISE (COLD BLUE-WHITE only, never amber). Projection used only S07-S08 and S19. |
| 5 | **Amber Discipline** | ZERO amber in the entire episode except S27 "I AM COMING." The single received ember arrives from the horizon (Moon/Sun: reflected, never emitted). Eyes STEADY at S27 — never glow. |
| 6 | **@Damaged State** | Phase 2 FINAL throughout. Never pristine. Cumulative damage visible. "Barely holding together." |

---

## REFERENCE IMAGES — CHARACTER

**Primary:** `_assets/cast/android_damaged.png` — the @Damaged reference (front/default angle).
**Alt angles:** `_assets/cast/android_damaged_2.png`, `android_damaged_3.png` — use the angle most appropriate for the scene's camera position.

> For Kling 3.0 video generation (motion script stage), all three images build the @Damaged Element. For Nano Banana image generation (this stage), upload ONE as character reference per scene.

**Identifier in prompts:** "the chrome android" — the reference image carries all visual details.

---

## REFERENCE IMAGES — ENVIRONMENT (Generate These First)

Generate these 7 environment reference images before any scene images. Each is a wide, empty establishing shot. Upload `ref-env-06.png` (`episode-05/04_visuals/raw/ref-env-06.png`) as a spatial reference when generating ENV-03 and ENV-06.

Save generated environment references to: `episode-07/04_visuals/raw/`

---

### ENV-01: Waterside Embankment at Twilight
**Filename:** `ep07_ref_env_waterside.png`
**Used in:** S01, S02, S03, S06, S07, S08
**Generate ref:** None required — standalone.

**Text Prompt:**
> Photorealistic, not a painting, not an illustration. A desolate modern urban waterside embankment at twilight, the sun already set, the sky draining from cold grey to black - post-storm, clouds dispersing, no active rain. A single weathered wooden bench sits near the water's edge on cracked wet concrete pavement. Dark still water stretches to a fog-shrouded urban horizon, low fog sitting on the surface, faint ripples disturbing the dark water. Standing water pools on the concrete. A single dim sodium streetlamp glows weakly in the far distance. Modern steel railing, wet concrete, no vegetation, no ruins, no fantasy elements. No figures. No text, no borders, no frames. Depth composition: wet concrete foreground, bench and water's edge midground, fog-shrouded water and darkening sky background. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### ENV-02: Wet City Street at Dusk
**Filename:** `ep07_ref_env_street.png`
**Used in:** S04, S05
**Generate ref:** None required — standalone.

**Text Prompt:**
> Photorealistic, not a painting, not an illustration. A wide modern urban street at dusk, wet asphalt gleaming with reflected cold streetlight. Fog hangs low between worn modern concrete buildings. On one side, warm light spills from shopfronts - a vendor's steam cart, a soft glowing advertising panel, blurred impressionistic silhouettes of mixed pedestrians (men and women) walking. On the other side, cold darkness and shuttered storefronts. Standing water in gutter channels reflects contrasting warm and cold light sources. Post-storm, no active rain - only wet surfaces. No clear protagonist visible - all figures are abstract blurred shapes. No text, no borders, no frames. Depth composition: wet asphalt foreground, flowing silhouettes and shopfronts midground, fog-shrouded buildings and fading sky background. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### ENV-03: Home Room (Cooled)
**Filename:** `ep07_ref_env_home.png`
**Used in:** S10, S11, S19, S20, S21, S25, S26
**Generate ref:** Upload `episode-05/04_visuals/raw/ref-env-06.png` as spatial reference — same room layout, warmth stripped.

**Text Prompt:**
> Photorealistic, not a painting, not an illustration. A cramped, austere modern room stripped of all warmth. A desk with an old CRT monitor against one wall, its cold blue-white screen the dominant light source. A narrow bed against the opposite wall. A wall clock with visible hands on the wall. A power cable runs visibly from a wall socket across the floor toward the desk. A desk lamp is present but switched OFF - dark. No warm tones anywhere. Dying dusk light fading through a small window, turning grey. The room is modern and minimal - no fantasy elements, no ruins, no vegetation. No figures. No text, no borders, no frames. Depth composition: cable and floor foreground, desk and CRT midground, bed and window background. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### ENV-04: Transit / Bus Stop at Dusk
**Filename:** `ep07_ref_env_transit.png`
**Used in:** S12, S13, S14, S15
**Generate ref:** None required — standalone.

**Text Prompt:**
> Photorealistic, not a painting, not an illustration. An exposed modern bus stop or transit bench on a wet open street at dusk, the sky overcast and light failing - post-storm, no active rain, only wet surfaces. A single flickering cold fluorescent lamp illuminates the bench from above, buzzing. Wet asphalt stretches in all directions - no sheltering structures nearby, nowhere to hide. A dim traffic light cycles in the background, its colored glow catching on wet surfaces. Cold sodium and fluorescent mix. Modern urban infrastructure - no fantasy elements, no vegetation, no ruins. No figures. No text, no borders, no frames. Depth composition: wet ground foreground, bench and lamp midground, empty wet road and traffic light background. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### ENV-05: Glittering Avenue / Mall at Evening
**Filename:** `ep07_ref_env_avenue.png`
**Used in:** S16, S17, S18
**Generate ref:** None required — standalone.

**Text Prompt:**
> Photorealistic, not a painting, not an illustration. A vast modern consumer avenue or mall concourse at evening, blazing with cold blue-white commercial light against the darkness outside. Towering advertising screens, illuminated shop windows, reflective wet floors. A dense river of mixed pedestrians (men and women) flows through as blurred impressionistic silhouettes - no detailed faces. Cold screens cast competing light pools on wet surfaces. Reflective shop glass shows distorted shapes. Modern architecture dwarfs any individual - immense scale, glass and steel, no fantasy elements. The outside beyond glass walls is pure dark. No clear protagonist. No text, no borders, no frames. Depth composition: wet reflective floor foreground, dense crowd silhouettes and screens midground, towering far screens and dark ceiling background. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### ENV-06: Balcony at Deep Night
**Filename:** `ep07_ref_env_balcony.png`
**Used in:** S22, S23, S24, S27
**Generate ref:** Upload `episode-05/04_visuals/raw/ref-env-06.png` as spatial reference — the balcony extends from the same room.

**Text Prompt:**
> Photorealistic, not a painting, not an illustration. A narrow residential balcony extending from a dark modern apartment tower at deep night. Iron railing, wet concrete floor, moisture beading on every surface. Beyond the railing: a vast dark void - a foggy dead modern city far below, scattered dim urban lights like dying embers in the fog. The sky is black, heavy with low cloud and fog. Volumetric fog wraps around the balcony, thickening into the distance. Behind the balcony, a glass door leads back into a dark room, barely visible interior. Cold grey-blue tones only - no warmth, no stars, no direction. Modern urban setting - no fantasy, no ruins, no vegetation. No figures. No text, no borders, no frames. Depth composition: balcony floor and railing foreground, fog void midground, distant foggy cityscape and black sky background. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### ENV-07: Wet Road Toward the Horizon (First-Light Direction)
**Filename:** `ep07_ref_env_road.png`
**Used in:** S28, S29
**Generate ref:** None required — standalone.

**Text Prompt:**
> Photorealistic, not a painting, not an illustration. A long, straight wet road stretching toward a distant horizon at the edge of night. Dark modern buildings of a dead city recede on both sides. Wet asphalt reflects a faint warm-tinted light from a distant amber rift at the horizon - not a sunrise, only the first hint that darkness might thin. Grey fog drifts across the road, thinning slightly toward the vanishing point. Wind-blown mist at ground level. Modern urban infrastructure - concrete, asphalt, steel, no fantasy elements, no vegetation, no ruins. No figures. No text, no borders, no frames. Depth composition: wet road surface foreground, flanking dark buildings midground, thinning fog and distant amber-tinted horizon crack background. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## REFERENCE IMAGE UPLOAD GUIDE

For each scene, upload the listed references alongside the text prompt in Nano Banana.

- **Char Ref** = Character reference (`android_damaged.png` or alt angle `_2`/`_3`)
- **Env Ref** = Environment reference (generated from ENV prompts above)
- **Chain Ref** = Previous scene output for visual continuity
- **Special Ref** = Additional reference for specific effects

| Scene | Char Ref | Env Ref | Chain Ref | Special Ref | Notes |
|:---|:---|:---|:---|:---|:---|
| S01 | — | waterside | — | — | Tiny silhouette, no char ref needed |
| S02 | damaged | waterside | — | — | |
| S03 | damaged | waterside | S02 output | — | Front/three-quarter angle — select appropriate damaged ref angle |
| S04 | — | street | — | — | Indifferent Flow, no character |
| S05 | damaged | street | — | — | |
| S06 | damaged | waterside | S02 output | — | Tighter framing, waterside continuity |
| S07 | damaged | waterside | — | `ep05/04_visuals/raw/28.png` | Projection callback — EP05 ref for projection style |
| S08 | damaged | waterside | S07 output | — | Same location, projection continuity |
| S09 | — | — | S08 output | — | Indifferent Flow, use S08 projection glow as color ref |
| S10 | damaged | home | — | — | Cable/tether must be visible |
| S11 | damaged | home | S10 output | — | Same room |
| S12 | — | transit | — | — | Indifferent Flow |
| S13 | damaged | transit | — | — | |
| S14 | damaged | transit | S13 output | — | Held silence, same location |
| S15 | damaged | transit | S14 output | — | Same location, wider |
| S16 | damaged | avenue | — | — | |
| S17 | damaged | avenue | S16 output | — | Same location, wider |
| S18 | — | avenue | S17 output | — | Indifferent Flow |
| S19 | damaged | home | S10 output | `ep05/04_visuals/raw/28.png` | Deeper night. Projection scene — EP05 ref for projection style |
| S20 | damaged | home | S19 output | — | Frozen broadcast, same room |
| S21 | damaged | home | S20 output | — | High angle, same room |
| S22 | damaged | balcony | — | — | |
| S23 | damaged | balcony | S22 output | — | Much wider framing |
| S24 | damaged | balcony | S23 output | — | |
| S25 | damaged | home | S10 output | — | Same room as S10 — cable payoff |
| S26 | damaged | — | S25 output | — | Stairwell descent — new location, no env ref (one-off) |
| S27 | damaged | road | S26 output | — | Building entrance — amber rift from horizon (road ref for street visible through entrance) |
| S28 | damaged | road | — | — | |
| S29 | — | — | — | — | REUSES 28.png — widening via Crane Up camera movement |

---

## GENERATED PROMPTS

---

### SECTION: INTRO (0:00–0:12)

---

#### Scene S01 — The Aftermath
- **Timestamp:** 0:00
- **Dramaturgy Reference:** Vast still water, twilight sky draining to black, wet stone, fog. Character absent or tiny distant silhouette.
- **Characters Present:** None (or distant tiny silhouette)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide establishing shot. Mostly emptiness — Architecture Cage pure. Headroom above for sky, breathing space in all directions. A tiny silhouette (if present) at frame edge, not center.
- **Upload:** USE ENV REF DIRECTLY — `ep07_ref_env_waterside.png` as scene image. No separate generation needed. If a tiny distant silhouette is desired, apply minimal inpainting on the env ref.

**Text Prompt:**
> N/A - env ref serves as scene image.

---

### SECTION: VERSE 1 — THE FALL FROM ARROGANCE (0:12–0:46)

---

#### Scene S02 — Waterside Bench, Seated
- **Timestamp:** 0:12
- **Dramaturgy Reference:** Robotiko seated on wet bench, hunched, looking over water. Stars prick the darkening sky. Cracked reflection on wet stone.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot, small figure in wide frame. Headroom for sky and stars. Breathing space toward the water. Wet stone beside him for the reflection.
- **Upload:** `android_damaged.png` + `ep07_ref_env_waterside.png`

**Text Prompt:**
> Wide shot, a chrome android seated alone on a wet wooden bench at the water's edge, hunched, looking out over the dark water. First faint stars prick the darkening twilight sky. His cracked, distorted reflection lies broken on the wet stone beside him. Hands rest open on his knees. Small figure in a wide cold frame - wet embankment, fog on the water, grey-blue twilight. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S03 — The Rise (Front / Three-Quarter)
- **Timestamp:** 0:34
- **Dramaturgy Reference:** "But now…" — Robotiko rises, shoulders fold, head drops, hands in pockets. Walking slumped along the embankment. Override 1: shown from the FRONT, not from behind.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png` (select front/three-quarter angle variant)
- **Video Tech Strategy:** Standard (this is Clip B of a two-clip beat — Clip A = S02 tail)
- **Composition Notes:** Front/three-quarter framing — we read his bowed head and empty pockets. Deep recession down the foggy embankment behind him. Camera positioned ahead of him. Headroom above for fog.
- **Upload:** `android_damaged.png` (3/4 angle) + `ep07_ref_env_waterside.png` + chain: S02 output

**Text Prompt:**
> Three-quarter front view, a chrome android walking slumped along a wet stone embankment at twilight. Head dropped, shoulders folded, hands hidden in empty pockets. Shown from the front so the bowed head and defeated posture read clearly. Small figure against the receding foggy embankment, the frame retreating ahead of him. Cold grey-blue light, wet stone, fog. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: INTERLUDE — INDIFFERENT FLOW 1 (0:47–1:04)

---

#### Scene S04 — Indifferent Flow: Wet Street
- **Timestamp:** 0:47
- **Dramaturgy Reference:** A wet night street. People and traffic flow through the frame. Composition centers on an empty space where a figure should be. The world without him.
- **Characters Present:** None (Robotiko absent)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** The empty center is the subject. Crowd flows around it. Breathing space at center for the conspicuous absence.
- **Upload:** USE ENV REF DIRECTLY — `ep07_ref_env_street.png` as scene image. No separate generation needed. The env ref already contains the wet street with blurred crowd silhouettes and the conspicuous empty space.

**Text Prompt:**
> N/A - env ref serves as scene image.

---

### SECTION: VERSE 2 — NOVEMBER IS FOR LOVERS (1:04–1:26)

---

#### Scene S05 — Walking Through Indifference (Low Charge)
- **Timestamp:** 1:04
- **Dramaturgy Reference:** Walking a cold wet street at dusk. Couples pass. "Hunger" = low charge — dimming eyes, faltering step, warm light he cannot draw from. Override 2.
- **Characters Present:** Robotiko (Phase 2, @Damaged — eyes dimming); background crowd (mixed)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium-wide, depth staging. Robotiko small in midground, blurred bodies crossing foreground. Warm shopfront pools vs. cold street — he stays in the cold. Breathing space for Dolly Out.
- **Upload:** `android_damaged.png` + `ep07_ref_env_street.png`

**Text Prompt:**
> Photorealistic, not a painting. Medium-wide shot, city street at dusk after rain - puddles on the asphalt but no active rain falling, no umbrellas. Only ONE chrome android walks alone with hands in pockets, head low, step faltering - small in the midground. Around him, mixed couples (men and women) walk arm in arm under warm shopfront glow. A vendor's steam rises, a romantic advertising panel glows softly. He stays in the cold, unable to draw from the warm light - his optical lenses dim and weak, barely flickering blue-red. Blurred human pedestrians cross the foreground. Wet asphalt reflects warm shop light against cold street darkness. Only one android in the entire frame, no second robot. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: VERSE 2.5 — SELF-REVULSION AT THE WATER (1:27–1:39)

---

#### Scene S06 — Rusted Hand, Cracked Reflection
- **Timestamp:** 1:27
- **Dramaturgy Reference:** Back at the water, near-dark. Tighter on Robotiko — rusted hand lifted, fog-breath from vents, cracked reflection in water. Override 3.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium-close, tighter than S02. Focus on the hand, the rust, the wet reflection. Foreground: rusted hand in damp air. Midground: chassis vents, fog-breath. Background: black water with cracked reflection.
- **Upload:** `android_damaged.png` + `ep07_ref_env_waterside.png` + chain: S02 output

**Text Prompt:**
> Medium-close shot, waterside at near-dark. A chrome android's rusted, fraying hand lifted into the damp grey air - rust beads with moisture on corroded chrome, exposed copper wires fraying at the wrist. Faint fog-breath ghosts from chassis vents. Below, his cracked trembling reflection in the black water. Tighter framing - on the hand, the chassis damage, the wet reflection. Cold grey, near-black atmosphere, fog. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: VERSE 3 + REFRAIN 1 — THE NOISE & FIRST RETREAT (1:40–1:55)

---

#### Scene S07 — Eye-Projection: Social Feed (COLD)
- **Timestamp:** 1:40
- **Dramaturgy Reference:** Bench in the dark. Cold blue-white beam from eyes materializes a teeming faceless data stream in the fog. Override 4: projection is COLD blue-white, never amber.
- **Characters Present:** Robotiko (Phase 2, @Damaged); projected crowd (abstract, faceless)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Projection occupies upper frame / foreground fog volume. Robotiko lower frame, small. Dark water behind for projection readability. Projected figures MUST remain abstract — no detailed faces.
- **Upload:** `android_damaged.png` + `ep07_ref_env_waterside.png` + special: `episode-05/04_visuals/raw/28.png` (projection style ref)

**Text Prompt:**
> Medium shot, dark waterside. A chrome android seated on the bench in darkness. From his optical lenses, a cold blue-white beam projects into the damp fog before him, materializing a teeming scroll of abstract faceless shapes - countless flickering silhouettes and avatars hanging in the foggy air. The projection is cold and restless, illuminating the fog and his damaged chrome in harsh blue-white light. Dark water and fog behind. The projected figures remain abstract and faceless - impressionistic shapes, not detailed people. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S08 — Refrain 1: "Billions of Users" (Distance Ladder — Rung 1)
- **Timestamp:** 1:49
- **Dramaturgy Reference:** Projected feed swells to a wall of avatars. Robotiko small beneath. Frame pulls back — figure shrinks against the immensity. Override 4+6.
- **Characters Present:** Robotiko (Phase 2, @Damaged); projected crowd (abstract)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot beginning the distance ladder. Projection fills upper frame as immense wall. Robotiko dwarfed in lower frame. Breathing space for the Dolly Out that begins here.
- **Upload:** `android_damaged.png` + `ep07_ref_env_waterside.png` + chain: S07 output

**Text Prompt:**
> Wide shot. A massive wall of cold blue-white projected avatars and abstract faceless shapes fills the upper frame - countless, indifferent, immense. A chrome android sits small beneath the projection, cold light washing his damaged chrome. The figure is shrinking against the feed's immensity. Dark waterside, fog, black water beyond. The projected wall is abstract - impressionistic silhouettes, not detailed faces. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: INTERLUDE — INDIFFERENT FLOW 2 (1:56–2:01)

---

#### Scene S09 — Indifferent Flow: Feed Noise
- **Timestamp:** 1:56
- **Dramaturgy Reference:** Feed/screens continue alone. A churn of cold imagery, no figure. The world's noise without anyone listening.
- **Characters Present:** None (Robotiko absent)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** Pure abstract cold noise. No anchor figure, no warm tones. The noise IS the composition. This is a unique abstract scene — NOT a location reuse.
- **Upload:** chain: S08 output (color/glow ref only)

**Text Prompt:**
> Abstract cold blue-white imagery churning across the frame - scrolling light, flickering fragmented screen data, abstract digital silhouettes. A restless wash of cold digital noise with no figure present, no warmth, no subject. Pure visual static - the world's indifferent feed grinding on without anyone watching. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: VERSE 4 + REFRAIN 2 — THE ROUTINE (2:02–2:44)

---

#### Scene S10 — The Plugged-In Room (Tether Motif)
- **Timestamp:** 2:02
- **Dramaturgy Reference:** Home room (ref-env-06 cooled). At desk, PLUGGED INTO THE WALL — cable from wall socket into chassis. CRT rejection text. Wall clock. Cold screen-glow only light. Override 5.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot framing the tether visibly: cable runs from wall socket to his chassis. CRT screen text readable. Wall clock in background. Desk lamp dark. Dusk dying through window. The cable is the planted prop — it MUST be clearly visible.
- **Upload:** `android_damaged.png` + `ep07_ref_env_home.png`

**Text Prompt:**
> Medium shot, cramped room at dusk dying to evening. A chrome android sits motionless at a desk before a CRT monitor, a cable visibly plugged from the wall socket into his chassis - tethered. Cold blue-white screen glow washes his face and rusted body, the only significant light. On the screen, lines of text: "Do Not Reply." "Application Rejected." A wall clock on the wall. A desk lamp present but dark, switched off. Dying dusk through a small window. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S11 — Refrain 2: "Rejection Emails" (Distance Ladder — Rung 2)
- **Timestamp:** 2:36
- **Dramaturgy Reference:** Camera pulls back from S10 — same room, wider framing. Robotiko hunched and small at the desk, dwarfed by the dark room. Distance ladder rung 2 — more distant than S10. Override 6.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot — significantly wider than S10. Same room, same desk, same CRT, but the camera has retreated. Robotiko is now a small hunched shape. The room's darkness swallows him. Only one android, only one desk.
- **Upload:** `android_damaged.png` + `ep07_ref_env_home.png` + chain: S10 output

**Text Prompt:**
> Photorealistic. Wide shot of a cramped dark room seen from the doorway. Only ONE chrome android sits hunched at a desk in the far corner, small in the frame, occupying less than 20% of the image. A CRT monitor glows cold blue-white - the only light source, washing the walls. The screen shows rejection text. A wall clock on the wall, a narrow bed, a desk lamp switched off. Night outside a small window. The android is dwarfed by the dark empty space of the room. Only one android, only one desk setup. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: INTERLUDE — INDIFFERENT FLOW 3 (2:45–2:57)

---

#### Scene S12 — Indifferent Flow: Empty Transit
- **Timestamp:** 2:45
- **Dramaturgy Reference:** Empty transit platform, wet asphalt, traffic light cycling. No one waits where someone should be.
- **Characters Present:** None (Robotiko absent)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** The empty bench is the subject. Wet reflections of cycling traffic lights. Breathing space where the figure should be.
- **Upload:** USE ENV REF DIRECTLY — `ep07_ref_env_transit.png` as scene image. No separate generation needed. The env ref already shows the empty bench, buzzing lamp, and wet desolate transit space.

**Text Prompt:**
> N/A - env ref serves as scene image.

---

### SECTION: VERSE 5 + REFRAIN 3 — THE PREDATOR (2:58–3:39)

---

#### Scene S13 — The Predator: Hope Chirps
- **Timestamp:** 2:58
- **Dramaturgy Reference:** Bus stop at dusk. Robotiko under flickering lamp. Receiver chirps — a spark of hope, not amber. Eyes flicker toward something good.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. Exposed under the single lamp. Built-in antenna on the left side of his head receives the signal — no handheld device. Faint lift in the eyes — but not warm, not amber. Wet open street around, no shelter.
- **Upload:** `android_damaged.png` + `ep07_ref_env_transit.png`

**Text Prompt:**
> Medium shot, bus stop at failing dusk. A chrome android sits exposed on a wet bench under a flickering cold fluorescent lamp. Wet open street stretches around him, no shelter. The single buzzing lamp is the only overhead light, casting hard cold shadows on wet asphalt. No handheld devices. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S14 — The Predator: Held Silence (3-Second Beat)
- **Timestamp:** 3:15
- **Dramaturgy Reference:** [3-SECOND HELD SILENCE] — frozen mid-gesture, receiver held, hope collapses. Then the creditor's cold voice. Override 8: motionless beat.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Same bus stop location as S13. STILL composition — motionless, frozen. Hard shadow from the buzzing lamp. Shoulders dropping. The antenna still extended — the cold creditor voice came through it. A held beat, not an action frame. No movement implied.
- **Upload:** `android_damaged.png` + `ep07_ref_env_transit.png` + chain: S13 output

**Text Prompt:**
> Medium shot, same bus stop (13.png). A chrome android frozen rigid on the bench under the buzzing cold lamp. His shoulders drop, head down. The lamp buzzes overhead, wet asphalt around him empty and exposed. A still, frozen composition - a motionless beat in cold failing dusk. No handheld devices. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S15 — Refrain 3: "Creditors" (Distance Ladder — Rung 3)
- **Timestamp:** 3:30
- **Dramaturgy Reference:** Wide shot. Robotiko small on bench under lamp. Empty transit space opens wide. Override 6.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot — wider than S13/S14. Transit space opens in all directions. Robotiko small under the lone lamp. Breathing space for the Dolly Out (rung 3 of distance ladder).
- **Upload:** `android_damaged.png` + `ep07_ref_env_transit.png` + chain: S14 output

**Text Prompt:**
> Wide shot. A chrome android small on the wet bench under a lone flickering lamp, the empty transit space opening wide around him in failing dusk. Wet asphalt stretches in all directions - no other figures, no shelter, exposed. The widest framing of the transit location, cold and desolate. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: VERSE 6 + REFRAIN 4 — THE VANITY (3:44–4:03)

---

#### Scene S16 — The Glittering Avenue
- **Timestamp:** 3:44
- **Dramaturgy Reference:** Consumer avenue at evening. Cold screens, wet shop windows, river of faces. Robotiko enters tiny — a rusted dark smudge in the polished crowd.
- **Characters Present:** Robotiko (Phase 2, @Damaged); dense crowd (mixed men and women)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot. Robotiko the smallest, darkest shape among the crowd. Cold commercial light blazing. Wet shop windows for reflections. Architecture Cage — the avenue dwarfs the figure. Breathing space for Dolly Out.
- **Upload:** `android_damaged.png` + `ep07_ref_env_avenue.png`

**Text Prompt:**
> Wide shot of a bustling commercial avenue (ep07_ref_env_avenue) at evening. A small android (android_damaged.png) as a silhouette walking among a dense crowd of diverse human pedestrians (men and women). 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S17 — Refrain 4: "Thousands of Faces" (Distance Ladder — Rung 4, Widest)
- **Timestamp:** 3:53
- **Dramaturgy Reference:** Crowd swells. Thousands stream around him under towering screens. His cracked reflection in wet shop glass. The smallest, stillest thing. Override 6: widest physical distance of the distance ladder.
- **Characters Present:** Robotiko (Phase 2, @Damaged); thousands (mixed)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Very wide shot — the widest crowd composition of the episode. Robotiko barely identifiable, a rusted speck. Architecture Cage at maximum. Reflective shop glass in foreground for the cracked reflection. Immense scale.
- **Upload:** `android_damaged.png` + `ep07_ref_env_avenue.png` + chain: S16 output

**Text Prompt:**
> Very wide shot of the same commercial avenue (S16 output as ref). A tiny android silhouette among thousands of pedestrians, even smaller than S16. Towering cold screens, wet reflective floors. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: INTERLUDE — INDIFFERENT FLOW 4 (4:04–4:09)

---

#### Scene S18 — Indifferent Flow: The Avenue Continues
- **Timestamp:** 4:04
- **Dramaturgy Reference:** Avenue's screens and crowd continue alone. Pure Architecture Cage, no protagonist. The city indifferent.
- **Characters Present:** None (Robotiko absent)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** No figure. The commercial machine running on its own. An empty space in the flow where a character might have been.
- **Upload:** USE ENV REF DIRECTLY — `ep07_ref_env_avenue.png` as scene image. No separate generation needed. The env ref already contains the blazing screens, blurred crowd, and protagonist-free Architecture Cage composition.

**Text Prompt:**
> N/A - env ref serves as scene image.

---

### SECTION: VERSE 7 + REFRAIN 5 — THE CORRUPTION (4:10–4:41)

---

#### Scene S19 — The Corruption: Broadcast (COLD Projection)
- **Timestamp:** 4:10
- **Dramaturgy Reference:** Home room, deeper night. Cold blue-white eye-projection throws broadcast onto wall — System Lords at podium, peace award. Override 4.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. Robotiko standing in the dark room, front-facing, projection beam from his head to the wall behind him. Broadcast silhouettes appear on the wall (figures at a podium, raised hands). Cold blue-white glow is the only significant light. Room in deeper night.
- **Upload:** `android_damaged.png` + `ep07_ref_env_home.png` + chain: S10 output + special: `episode-05/04_visuals/raw/28.png` (projection style ref)

> **PRODUCTION NOTE:** Original prompt had Robotiko lying on the bed with projection on the ceiling. Nano Banana could not reliably generate a supine figure with upward eye-projection. Adjusted to standing front-facing composition with wall projection — stronger visual: he confronts the broadcast rather than being washed over by it. Generated image (19.png) approved.

**Text Prompt:**
> Medium shot, cramped dark room at night. One chrome android standing front-facing. A cold blue-white light beam from his head projecting broadcast imagery onto the wall behind him - silhouettes at a podium, raised hands. Cold projected light on his damaged chrome body, the only light source. Dark room. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S20 — The Corruption: Held Silence (3-Second Beat)
- **Timestamp:** 4:26
- **Dramaturgy Reference:** [3-SECOND HELD SILENCE] — broadcast freezes on clean hands and medal. "Fake heroes… Fake victories." Override 8: motionless beat.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Same room as S19. FROZEN composition — Robotiko standing, projection frozen on the wall behind him (single figure with raised hand/arm — the "fake hero" medal moment). Cold glow. Motionless beat.
- **Upload:** `android_damaged.png` + `ep07_ref_env_home.png` + chain: S19 output

> **PRODUCTION NOTE:** Updated to match S19 production adjustment — standing composition with wall projection, not supine on bed. Generated image (20.png) shows the same room and angle as 19.png with different projection content (single figure, raised arm). Approved.

**Text Prompt:**
> Medium shot, same dark room (19.png). One chrome android standing motionless, front-facing. Broadcast projection frozen on the wall behind him - a single silhouette figure with raised arm. Cold blue-white projected glow on his motionless damaged chrome. A still, frozen composition. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S21 — Refrain 5: "The Fake Truth" (Distance Ladder — Rung 5, Peak Isolation)
- **Timestamp:** 4:32
- **Dramaturgy Reference:** High angle, looking down. Robotiko tiny on bed in corner. Cold broadcast light. The most distant, most isolated frame — distance as confinement. Override 6.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** HIGH ANGLE looking straight down. The room's geometry frames him like a cage from above — desk, chair, monitor, clock. Robotiko a small rusted shape on the bed in the corner. Peak isolation of the entire episode. Cold broadcast light washing down.
- **Upload:** `android_damaged.png` + `ep07_ref_env_home.png` + chain: S20 output

**Text Prompt:**
> High-angle shot looking straight down into a cramped dark room. One small rusted chrome android on the bed in the far corner, occupying less than 15% of the frame. Cold blue-white broadcast light washing over him. Room furniture visible from above - desk, chair, monitor, wall clock. Deep shadows, dark room. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: CHORUS — THE CRY (4:42–5:06)

---

#### Scene S22 — The Chorus Cry: Amber Named, Amber Absent (Still Hold)
- **Timestamp:** 4:42
- **Dramaturgy Reference:** THE BOTTOM. Balcony at deep night, fog thick. Raised fist toward fog — fog swallows the gesture. The amber gaze he calls for is NOT THERE. Still Hold candidate. Heaviest grain. Override 9.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard — **STILL HOLD** (minimal motion at emotional summit). Heaviest film grain (Grain Crescendo).
- **Composition Notes:** Medium shot. Robotiko at the balcony railing, fog void before and below. Arm raised, fist toward the fog. Room for the fog to "absorb" the gesture. **NO AMBER anywhere — this is amber's most conspicuous absence.** Maximum grain.
- **Upload:** `android_damaged.png` + `ep07_ref_env_balcony.png`

**Text Prompt:**
> Medium shot, deep night. One chrome android standing at a balcony railing, thick fog around him, dark foggy city far below. One arm raised, fist reaching into the fog. Fog surrounding the raised fist, undisturbed. No warm light, no amber - only cold grey-blue fog and darkness. Maximum film grain. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: GUITAR SOLO — THE BOTTOMING OUT (5:07–5:33)

---

#### Scene S23 — The Speck on the Tower
- **Timestamp:** 5:07
- **Dramaturgy Reference:** Absolute farthest camera of the episode. Small chrome figure on balcony of dark tower, foggy dead city below. Fading to near-total dark and stillness.
- **Characters Present:** Robotiko (Phase 2, @Damaged — a speck)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** EXTREME wide shot — the farthest remove of the entire episode. Robotiko barely a speck on the balcony. The dark tower, the foggy void below, the black sky. Settling into stillness and dark. The bottoming out.
- **Upload:** `android_damaged.png` + `ep07_ref_env_balcony.png` + chain: S22 output

**Text Prompt:**
> Extreme wide shot. A dark residential tower at night, heavy fog, scattered dim city lights far below. One tiny chrome figure barely visible on a small balcony, occupying less than 5% of the frame. Near-total darkness, heavy fog. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: OUTRO — THE AWAKENING (5:34–5:59)

---

#### Scene S24 — Clarity, Not Defeat
- **Timestamp:** 5:34
- **Dramaturgy Reference:** Sudden silence. Balcony threshold. Stillness is clarity, not defeat. Eye-beam flickers — shows a bare horizon, not a feed. Override 10.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. Robotiko at the balcony threshold — glass door to dark room behind, foggy void ahead. His stance is attentive, not slumped. A faint pale light from his lenses reveals a bare horizon line through the fog. A sense of space opening. Still cold, but the quality of the stillness has changed.
- **Upload:** `android_damaged.png` + `ep07_ref_env_balcony.png` + chain: S23 output

**Text Prompt:**
> Medium shot, balcony threshold. One chrome android standing upright between a dark room with glass door behind and foggy void ahead. Attentive stance, not slumped. A faint pale light from his eyes toward the distant fog, revealing a bare horizon line. Cold, still. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: MANTRA / CLIMAX — THE TURN (6:00–6:17)

---

#### Scene S25 — The Unplug (Tether Payoff)
- **Timestamp:** 5:50
- **Dramaturgy Reference:** "Cast off this metal straightjacket." The first deliberate act. Override 10.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Close-up on hands and chassis. Robotiko tears cables/wires from his own body — sparks fly at the disconnection point. Visceral, decisive. The "straightjacket" is literal: wires embedded in his chassis, ripped out by his own hand.
- **Upload:** `android_damaged.png` + `ep07_ref_env_home.png` + chain: S10 output (cable continuity)

> **PRODUCTION NOTE:** Original prompt had Robotiko pulling a wall-socket cable. Generated image (25.png) is far stronger: close-up of his hands tearing wires/cable from his own chassis, sparks flying. More visceral, more literal "cast off the straightjacket" — he removes the tether FROM his own body, not from the wall. Narratively superior: the system was inside him, and he tears it out. Approved.

**Text Prompt:**
> Close-up shot, dark room. A chrome android's hands gripping cables and wires embedded in his own chassis, tearing them free. Sparks fly at the disconnection points. Exposed wires, corroded chrome, the decisive physical act. Cold dark room, sparks are the only light accent. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S26 — The Descent (Stairwell)
- **Timestamp:** 6:00
- **Dramaturgy Reference:** After the unplug, Robotiko leaves the apartment. Descending the building's stairwell — purposeful, determined, spine straight. The first forward movement after the decisive act.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Low-angle shot from below, looking up the stairwell. Robotiko descending toward the camera — face visible, determined expression readable. Stairs recede upward behind him. Purposeful stride — contrast with S03's slumped walk. Dim emergency/utility lighting. Industrial apartment stairwell — concrete, metal railing, cold. He is LEAVING, not arriving.
- **Upload:** `android_damaged.png`

> **PRODUCTION NOTE — SPATIAL LOGIC FIX:** Original S26 had Robotiko rising from the unplug and turning toward the balcony, then S27 at the balcony threshold with amber, then S28 on the street. This created a spatial teleport (balcony → street with no exit shown). Fixed: S26 = descending the apartment stairwell (the physical act of leaving). S27 = at the building entrance, stepping onto the street (amber arrives here). This creates a continuous spatial chain: room (S25 unplug) → stairs (S26 descent) → building entrance (S27 amber + first step) → street (S28-S29 journey). The balcony arc (S22-S24) concludes the cry/clarity; the exit arc (S25-S27) is the action.

**Text Prompt:**
> Low-angle shot looking up a dark concrete apartment stairwell. One chrome android descending the stairs toward the camera, face visible, spine straight, one hand on the metal railing. Dim cold utility light from a bare bulb above casts hard shadows down the stairwell. Industrial concrete walls, worn metal railing. He moves downward with determination, his face readable. Cold, stark, minimal. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S27 — THE TURN: Building Entrance / The Single Received Amber Ember (The Only Dolly In)
- **Timestamp:** 6:07
- **Dramaturgy Reference:** THE MAKE-OR-BREAK BEAT. At the building entrance, stepping onto the wet street. Facing the horizon — the direction he will walk. Single amber rift opens in the fog down the road. Warm amber wash travels through fog, catches on wet chrome. Eyes STEADY — flicker stops. Override 10. Moon/Sun: amber from OUTSIDE, reflected, never emitted.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard — **THE SINGLE DOLLY IN** of the episode. **THE SINGLE AMBER MOMENT.**
- **Composition Notes:** Medium shot. Robotiko at the building entrance/doorway, framed by the dark doorframe, facing OUT toward the wet street and the horizon beyond. The road stretches away (ENV-07 road composition visible through the entrance). Fog volume between him and the amber source. Wet chrome catches the arriving warmth. The amber is RECEIVED from outside — reflected on his chrome, never emitted. Eyes STEADY, never glow. The doorframe = the last Architecture Cage; he steps through it.
- **Upload:** `android_damaged.png` + `ep07_ref_env_road.png` (for the street/horizon visible through the entrance)

> **PRODUCTION NOTE — SPATIAL LOGIC FIX:** Original S27 was at the balcony threshold. Moved to the building entrance for spatial continuity (see S26 note). The amber ember requirements are fully preserved: (1) amber rift on horizon ✅ (more visible from street level down the road), (2) warm wash on chrome ✅, (3) eyes steady ✅, (4) the only Dolly In ✅. Narratively stronger: the amber arrives as he steps into the world, not while standing on a balcony above it. The building entrance doorframe provides a final Architecture Cage that he walks through.

**Text Prompt:**
> Medium shot, building entrance at night. One chrome android standing in the dark doorframe of an apartment building, facing outward toward a wet street stretching into the distance. A single small warm amber light point on the far horizon, visible down the road through fog. Warm amber-tinted fog reaching the figure at the entrance, reflecting on wet chrome surfaces. Eyes still and clear, not flickering. Dark building interior behind, wet street and amber direction ahead. The amber comes from the horizon, not from the android. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: INSTRUMENTAL OUTRO — THE FINAL JOURNEY (6:18–7:19)

---

#### Scene S28 — First Steps Forward
- **Timestamp:** 6:18
- **Dramaturgy Reference:** Leaves the building. Wet street below. First forward steps toward the amber rift. Same retreating-distance composition, inverted meaning — he walks INTO it. Override 11.
- **Characters Present:** Robotiko (Phase 2, @Damaged)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium-wide. Robotiko on the wet street, walking forward along the road toward the distant amber-rift horizon. Dead night city receding behind. The frame composition rhymes with the refrains' retreating shots, but the meaning inverts — he moves forward into the distance, not shrinking from it.
- **Upload:** `android_damaged.png` + `ep07_ref_env_road.png`

**Text Prompt:**
> Medium-wide shot, wet road at night (ep07_ref_env_road). One chrome android (android_damaged.png) walking forward toward a faint amber light on the horizon. Dark buildings behind. Wet asphalt reflecting warm-tinted light from the horizon. Grey fog thinning ahead. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S29 — The Final Journey
- **Timestamp:** 6:50
- **Dramaturgy Reference:** Wide, patient. Small chrome figure on wet grey road toward a lightening horizon — NOT a sunrise, only a direction. Wind rises. Fading. Override 11.
- **Characters Present:** Robotiko (Phase 2, @Damaged — small, moving)
- **Image Reference Path:** `_assets/cast/android_damaged.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Uses **28.png as source image** — same road composition. The "widening" effect is achieved through camera movement (Crane Up: tilt + zoom out) in the motion script, not through a different image. This preserves the building composition that Nano Banana kept breaking when attempting a very wide shot.
- **Upload:** REUSE `28.png` — no new generation needed

> **PRODUCTION NOTE:** Original plan required a separate very wide shot of the road. Nano Banana consistently broke the building composition when zooming out to very wide — flanking buildings changed shape, position, and style across generations. Fix: reuse 28.png (which has perfect composition) and achieve the "widening/opening" feeling through Crane Up camera movement in the video generation stage. Proven technique from lessons.md (Speed Variation Reuse): same image, different camera = different emotional experience.

**Text Prompt (original, kept for reference — image = 28.png):**
> Very wide shot, wet grey road (ep07_ref_env_road). One small chrome figure (android_damaged.png) walking forward toward a faint amber-tinted crack of light on the horizon, occupying less than 10% of the frame. Dark city buildings behind. Wind-blown fog across the road. Only one android. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## QUALITY CHECKLIST

- [x] Every prompt ends with the mandatory style suffix (verified all 29 + 7 env refs)
- [x] Every prompt specifies `16:9 widescreen composition`
- [x] Short character identifier ("the chrome android") used — reference images carry visual details
- [x] Every scene with character references `android_damaged.png` (correct `master_ref_path`)
- [x] Character visual state = Phase 2 Destruction FINAL — no pristine, cumulative damage
- [x] No forbidden aesthetics (no clean/sterile/neon/Pixar/plastic/melodrama)
- [x] No "glowing eyes" / "amber eyes" — eyes described as optical lenses (physical material)
- [x] AMBER DISCIPLINE: zero amber in S01-S26, S28-S29 lightening ≠ amber glow. S27 = the single received ember
- [x] Eye-projection = COLD BLUE-WHITE (S07, S08, S19) — never amber, never warm
- [x] S27 amber: arrives from OUTSIDE (horizon rift), REFLECTED on chrome — never emitted from eyes; eyes STEADY, not glow
- [x] Wet-grey aftermath throughout — no active rain
- [x] Temporal spine: twilight (S01-S03) → dusk (S04-S06) → dusk/evening (S10-S17) → night (S19-S21) → deep night (S22-S24) → first-light direction (S27-S29)
- [x] Architecture Cage: Robotiko <30% in wide shots
- [x] Distance ladder: S08 (rung 1) < S11 (rung 2) < S15 (rung 3) < S17 (rung 4) < S21 (rung 5, peak)
- [x] Indifferent Flow interludes: S04, S09, S12, S18 — character absent
- [x] Held silences: S14 and S20 — motionless, frozen compositions
- [x] Mixed gender in all crowd scenes (S04, S05, S12, S16, S17, S18)
- [x] All prompts composed with headroom and breathing space for camera movement
- [x] Total prompts = 29 (matches dramaturgy scene count)
- [x] No Start-End keyframe pairs needed (S03 is two-clip at motion script stage, not keyframe)
- [x] Mentor NEVER shown — not in any scene
- [x] Reference Image Upload Guide complete (per-scene table)
- [x] Environment reference prompts complete (7 locations)
- [x] "Would Fibula approve this?" — Yes.

---

> **APPROVAL STATUS:**
> - [ ] Human reviewed
> - [ ] Human approved
> - [ ] Ready for image generation
>
> Visual prompts delivered for review. Awaiting human approval before image generation begins.
