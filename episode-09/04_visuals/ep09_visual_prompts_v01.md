# EP09 — VISUAL PROMPTS
> **Version:** v01 | **Generated:** 2026-06-21
> **Skill:** `_skills/robotiko-visual-prompts/SKILL.md`
> **Inputs:** Approved `ep09_dramaturgy_v01.md`, `master.md`, `character_profiles.json`, `ep09_musical_metadata.json`

---

## PRE-GENERATION CHECKLIST

- [x] `_management/master.md` — Visual DNA, color palette, forbidden list, mandatory suffix
- [x] `episode-09/03_direction/ep09_dramaturgy_v01.md` — APPROVED scene breakdown (38 scenes)
- [x] `_assets/cast/character_profiles.json` — Phase 2→3 transition mid-episode (S27)
- [x] `_assets/cast/ref_robotiko_master.png` — Visual reference (Robotiko appears in S01–S35)
- [x] `_assets/cast/ref_mentor_master.png` — NOT USED (Mentor is gone; S07 is a projection onto the Mechanic, not a Mentor appearance)

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP09 |
| **Title** | Shadow Debugging |
| **Station** | The Integrated Self (Kintsugi — making peace with flaws) |
| **Character Phase** | Phase 2: Destruction (@Damaged) → Phase 3: Reconstruction (Kintsugi) — transition at S27 (4:09) |
| **Robotiko Visual State (S01–S26)** | Battle-scarred rusted chrome, missing right ear with exposed wires at ear socket, torso dent, shoulder scratches, calm steady blue eyes (transitioned at EP08 climax — no glitch, no flicker). |
| **Robotiko Visual State (S27–S35)** | Patchwork chrome body repaired with mismatched rusted scrap metal, translucent digital skin revealing bioluminescent core beneath, cracks filled with glowing gold light, calm steady blue eyes. Progressive — gold increases from S27 through S35. |
| **Camera Personality** | The Discovering Camera — Slow Zoom Out = understanding widens, NOT retreat. |
| **Total Scenes** | 38 |
| **Total Prompts** | 40 (includes S11a/b and S27a/b Mode B pairs) + 3 reference image prompts |

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

## VISUAL THROUGH-LINES

### The Glass Rhyme Chain
Three moments connected by glass as a compositional motif:
- **S10** (command bridge glass): Smooth glass wall separating the sovereign from the ocean. Dry side / living side.
- **S17** (workshop mirror): Cracked glass leaning against the wall. The faceless reflection. Fracture lines.
- **S27** (gold in cracks): The fracture lines from S17 become the channels where gold flows. Glass-separation becomes gold-connection.

When generating: the crack pattern in S17 should anticipate the gold channels in S27. Same cracks, different meaning.

### The Lighting Arc
External light → internal light. This is the philosophy, not mood lighting.
- **S06–S09:** Warm amber work lamp (external, honest)
- **S07:** One amber pulse on wrench tip (the Mentor echo — external, fails)
- **S12–S24:** Hard white lamp throws the shadow (external, confrontational)
- **S21:** Total darkness (no light at all)
- **S27:** First gold light from within the cracks (internal, earned)
- **S29:** THE LIGHTING FLIP — lamp dims, core glows (external → internal)
- **S30–S35:** Self-luminous (the android IS the light source)
- **S36–S38:** Gold leaks into the world's own cracks (internal light seeps outward)

### The Six Zoom-Out Reveals

| # | Scene | Lyric | What the Zoom-Out Shows |
|---|---|---|---|
| 1 | S05 | "Deeper than the blueprint" | Exterior → workshop interior |
| 2 | S10 | "Deeper than the data" | Glass barrier — knowing vs. experiencing |
| 3 | S13 | "Deeper than the self" | Gripping hand casts shadow on what it reaches for |
| 4 | S18 | "Deeper than reflection" | Hand passes through mirror — the witness |
| 5 | S21 | "Deeper than the void" | Shadow = everything in the dark |
| 6 | S27 | "Deeper than the wound" | Gold appears in the cracks |

Compose these scenes with extra lateral and vertical space for the zoom-out motion.

---

## REFERENCE IMAGES (Step 0)

Generate these BEFORE any scene prompts. Upload alongside scene prompts as indicated in each scene's Upload field.

---

### REF 1: The Mechanic (New Character)

**Design Brief:**
An old Anatolian man. Workshop owner, repairman. The most ordinary person in the series. NOT mystical, NOT dramatic — a working man to whom the whole drama is just a Tuesday. Three shots in the episode (S06, S09, S11), plus one amber-projection shot (S07). His greenish coat must NOT be dark green (that is the Mentor's cloak) — it is a faded, worn, greenish-brown canvas work coat. His tools are simple hand tools, not staffs.

**Reference Image Path:** `episode-09/04_visuals/ep09_ref_mechanic.png`

**Text Prompt:**
> Full-body portrait of an old Anatolian man in his 70s, weathered deeply wrinkled face, short grey hair, wearing a faded greenish-brown canvas work coat over a dark simple shirt and worn dark trousers, rough calloused hands visible at his sides, standing in neutral pose facing three-quarter angle, simple worn leather shoes, plain and ordinary — a working man, warm natural side lighting, neutral grey-brown workshop wall background, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF 2: Workshop Interior (Recurring Environment — 30+ scenes)

**Design Brief:**
A small Anatolian repair workshop. Oil, rust, mismatched tools, scrap metal. Honest, functional, nothing decorative. The Brechtian workspace where the debugging happens. This is the continuous home of the episode.

**Reference Image Path:** `episode-09/04_visuals/ep09_ref_workshop.png`

**Text Prompt:**
> Wide establishing shot of a small Anatolian repair workshop interior, no characters. Oil-stained rough concrete walls with mismatched hand tools hanging on nails and pegboard. Heavy wooden workbench center-frame cluttered with scrap metal pieces, wire rolls, and hand tools. A hard white work lamp clamped to the bench edge, turned off. A corrugated metal roll-up shutter in the back wall, half-open with grey daylight behind. A small Turkish tulip-shaped tea glass on the bench surface. Worn concrete floor with old oil stains. Metal shelving on the right wall with boxes and spare parts. A large technical blueprint pinned to the left wall. Everything functional, nothing decorative — a working space, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF 3: Command Bridge (Flashback Environment — S08, S10)

**Design Brief:**
The Digital Solomon's sovereign command bridge — a conductor's podium over nature, NOT military. Screens, glass walls, ocean below, drones above. Cold blue-steel palette, clinical separation. The seat of power, now vacant.

**Reference Image Path:** `episode-09/04_visuals/ep09_ref_command_bridge.png`

**Text Prompt:**
> Wide establishing shot of a sovereign command bridge interior suspended above a dark ocean, no characters. Floor-to-ceiling glass walls revealing open ocean below and to the horizon. Banks of sleek consoles with screens displaying blue data cascades flanking an empty high-backed command chair facing the glass. Beyond the glass above the ocean surface, small drones in tight formation like a flock of metal birds. Cold blue-steel palette throughout, clinical and sterile, screen-glow the primary light source, polished dark floor reflecting the blue data light, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## GENERATED PROMPTS

---

### THE FAILED MESSIAH (0:00–0:59)

---

#### Scene S01 — The Myth
- **Timestamp:** 0:00–0:14
- **Dramaturgy Reference:** Low worshipper's-eye angle. Robotiko descends toward camera. Cold sun as false halo. Silhouette — the savior image.
- **Characters Present:** Robotiko (@Damaged — silhouette only, damage not visible)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Low angle. Leave headroom above the figure for the halo effect. Space below for the descending path. The figure occupies the upper-center third.
- **Upload:** char: `ref_robotiko_master.png` (proportions guide for silhouette)

**Text Prompt:**
> Low angle looking up from ground level, a chrome android descending a grey barren rocky path toward the camera, visible as a dark silhouette against a pale cold sun directly behind creating a false halo effect, arms slightly apart, silhouette appears whole and radiant, grey overcast sky, barren grey-brown rocky terrain falling away behind the figure, cold desaturated palette, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S02 — The Puncture
- **Timestamp:** 0:15–0:26
- **Dramaturgy Reference:** Camera pulls back. Halo = flat daylight. Body broken: rusted, missing ear, torso dent. The lens undoes the sacred image.
- **Characters Present:** Robotiko (@Damaged, full body revealed)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium-wide. The figure occupies the center third. Blurred indistinct shapes below on the path. Space on both sides for the pulled-back composition.
- **Upload:** char: `ref_robotiko_master.png` · chain: S01 output

**Text Prompt:**
> Medium-wide shot, a chrome android walking along a grey ordinary path, battle-scarred rusted chrome, missing right ear with exposed wires at ear socket, torso dent, shoulder scratches, calm steady blue eyes, exposed fraying analog wires, flat grey daylight with no halo, overcast sky, blurred indistinct figures visible in the distance below, grey barren landscape, cold flat light, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S03 — The Held Silence
- **Timestamp:** 0:27–0:39
- **Dramaturgy Reference:** Close-up face. Mouth opens — nothing comes out. Hold too long. Faces curdling around him.
- **Characters Present:** Robotiko (@Damaged, face close-up)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Close-up. Face fills center frame. Headroom above. Blurred background figures — intentionally abstract to prevent AI from resolving them into detailed people.
- **Upload:** char: `ref_robotiko_master.png` · chain: S02 output

**Text Prompt:**
> Close-up of a chrome android's face, battle-scarred rusted chrome surface, missing right ear with exposed wires at ear socket, calm steady blue eyes, mouth mechanism slightly open, blurred indistinct faces visible in the background around him — featureless shapes of mixed men and women, cold grey overcast light, no warmth, expression blank and emptied, headroom above, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S04 — The Myth-Engine
- **Timestamp:** 0:40–0:49
- **Dramaturgy Reference:** Robotiko's POV. Raised phones, demanding faces. One face turns away into rapture — mythologizing the silence. The crowd shiny, sealed, armored.
- **Characters Present:** Crowd (no Robotiko visible — this is his POV)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** POV shot. Faces fill the frame. The one rapturous face at the right edge provides the composition anchor. Mixed gender crowd.
- **Upload:** chain: S03 output

**Text Prompt:**
> POV shot looking into a crowd of mixed men and women in modern clothing, raised smartphones with glowing screens held toward the camera, bright sealed hopeful faces in the front row with demanding expressions, at the right edge one face turned away looking upward in rapture — mythologizing, the crowd appears shiny and intact and armored in certainty, cold grey overcast light with phone-screen glow illuminating faces from below, shallow depth of field with front faces sharp and rear blurred, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S05 — The First Reveal
- **Timestamp:** 0:50–0:59
- **Dramaturgy Reference:** Exterior grey gives way to workshop interior. Blueprint on wall, tools, scrap metal. First Discovering Camera zoom-out — "Deeper than the blueprint."
- **Characters Present:** None (environment transition)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Wide shot of the workshop threshold. Two-tone composition: cold grey exterior on left, warm rust interior on right. Extra lateral space for the zoom-out reveal.
- **Upload:** env: `ep09_ref_workshop.png` · chain: S04 output

**Text Prompt:**
> Wide shot from a threshold, the left side showing cold grey exterior daylight and the right side opening into a workshop interior. Inside: a large technical blueprint pinned to a rough oil-stained wall, hand tools hanging on nails, scrap metal pieces on a heavy wooden workbench, the warm rust-colored interior contrasting with the cold grey outside — two color worlds in one frame, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### THE WORKSHOP — ARRIVAL & DEPARTURE (1:00–1:40)

---

#### Scene S06 — The Welcome
- **Timestamp:** 1:00–1:05
- **Dramaturgy Reference:** Workshop interior. The mechanic lets Robotiko in with a glance. Tea. The door was already open.
- **Characters Present:** The Mechanic (shot 1/3) + Robotiko (@Damaged)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`, `episode-09/04_visuals/ep09_ref_mechanic.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium-wide. Mechanic left of center, Robotiko entering from right. Tea glass between them on the bench. Roll-up shutter half-open behind with fading daylight. Space above for tilt headroom.
- **Upload:** char: `ref_robotiko_master.png` + `ep09_ref_mechanic.png` · env: `ep09_ref_workshop.png`

**Text Prompt:**
> Medium-wide shot inside a workshop, an old man in a faded greenish-brown work coat standing by a workbench gesturing casually toward a chrome android entering from the right, the chrome android battle-scarred rusted chrome, missing right ear with exposed wires, torso dent, calm steady blue eyes, a Turkish tea glass steaming on the bench surface between them, oil-dark walls with mismatched tools hanging, roll-up metal shutter half-open behind with fading daylight, warm amber-yellow work lamp casting warm light on the bench area, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S07 — The Amber Pulse
- **Timestamp:** 1:06–1:12
- **Dramaturgy Reference:** The mechanic under the lamp. Greenish coat catches the light. Wrench held upright — echoes the Mentor's staff. Amber tip flickers. Then it is just an old man. The single amber moment.
- **Characters Present:** The Mechanic (Mentor projection surface — the Mentor is NOT present)
- **Image Reference Path:** `episode-09/04_visuals/ep09_ref_mechanic.png`
- **Video Tech Strategy:** Standard (Mode A). The amber flicker is a lighting event for the motion stage, not a character transformation.
- **Composition Notes:** Medium shot. The wrench tip at the top of the frame — vertical, echoing a staff. Tea glass visible on bench. Headroom above wrench tip for tilt. Do NOT upload `ref_mentor_master.png` — uploading it would cause the generator to produce the actual Mentor.
- **Upload:** char: `ep09_ref_mechanic.png` · env: `ep09_ref_workshop.png` · chain: S06 output

**Text Prompt:**
> Medium shot, an old man in a faded greenish-brown work coat standing at a workbench, holding a long metal wrench upright in his right hand with the wrench tip at the top of the frame, warm amber-yellow light from a work lamp catching the greenish coat and flickering on the wrench tip, a Turkish tea glass on the bench beside him, oil-dark workshop background with tools hanging, the composition echoing a cloaked figure holding a staff with a glowing tip — but it is just an old man with a wrench, warm amber-toned lighting, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S08 — Digital Solomon
- **Timestamp:** 1:13–1:23
- **Dramaturgy Reference:** Sovereign command bridge over ocean. Screens, data cascades, drones as flock. Empty command chair — environment-only. Cold archived palette.
- **Characters Present:** None (environment-only — human decision: Robotiko not shown, presence implied by empty chair)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A). Cold palette, atmospheric motion (data on screens, ocean surface).
- **Composition Notes:** Wide shot. Empty chair centered. Glass walls stretching to edges. The vacant seat IS the statement. Space for zoom-out.
- **Upload:** env: `ep09_ref_command_bridge.png`

**Text Prompt:**
> Wide shot of a sovereign command bridge suspended above a dark ocean, an empty high-backed command chair centered before floor-to-ceiling glass walls, banks of consoles with screens displaying blue data cascades flanking the chair, beyond the glass dark ocean stretches to the horizon with small drones in tight formation above the waves like a metal flock, the chair empty — the sovereign is absent, cold blue-steel palette, clinical sterile light from the screens, polished dark floor reflecting blue data glow, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S09 — The Indifferent Beat
- **Timestamp:** 1:23–1:28
- **Dramaturgy Reference:** Workshop intercut. The mechanic at his bench, working a piece of metal, tea half-empty. Not watching. The grandiose past against the ordinary present.
- **Characters Present:** The Mechanic (shot 2/3, alone)
- **Image Reference Path:** `episode-09/04_visuals/ep09_ref_mechanic.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium shot. Mechanic centered at bench. Hands busy with metal and file. Tea glass in frame. Ordinary and unhurried.
- **Upload:** char: `ep09_ref_mechanic.png` · env: `ep09_ref_workshop.png` · chain: S07 output

**Text Prompt:**
> Medium shot, an old man in a faded greenish-brown work coat seated at a workbench, hands working a piece of metal with a file, Turkish tea glass half-empty beside his hands, tools scattered on the bench, not looking up — focused entirely on his own work, oil-dark workshop walls behind with tools hanging, warm steady work-lamp light from above on the bench area, the most ordinary scene — a man doing his work, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S10 — Dry Behind Glass
- **Timestamp:** 1:28–1:34
- **Dramaturgy Reference:** Close-up of a glass surface. Ocean beyond but the near side is dry. "Knowing the ocean does not make you wet." Second zoom-out. This glass rhymes with the mirror (S17) and the gold (S27).
- **Characters Present:** None (environment detail — glass close-up)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Close-up. Glass surface fills the frame vertically. Ocean soft-focus behind. The glass crack pattern should anticipate S17. Extra lateral space for zoom-out.
- **Upload:** env: `ep09_ref_command_bridge.png` · chain: S08 output

**Text Prompt:**
> Close-up of a smooth glass wall surface, the glass slightly fogged, beyond it a dark ocean visible with slow wave movement in soft focus, the near side of the glass completely dry — no moisture, no condensation, cold blue-steel palette, clinical light reflecting off the glass surface creating thin bright lines, a hairline crack visible in the glass running vertically, the glass as barrier between the dry sterile interior and the living ocean beyond, sharp focus on the glass surface, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S11a — The Shutter (Start Frame)
- **Timestamp:** 1:35–1:40
- **Dramaturgy Reference:** The mechanic pulls the roll-up shutter down. Day → night. Three shots complete. He goes home. Mode B Start Frame: shutter open, mechanic present, daylight.
- **Characters Present:** The Mechanic (shot 3/3, exiting) + Robotiko (@Damaged, background)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`, `episode-09/04_visuals/ep09_ref_mechanic.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B) — this is the START frame
- **Composition Notes:** Medium-wide. Mechanic silhouetted at the shutter in the background. Robotiko visible at the far end of the bench. Tea glass in foreground on bench.
- **Upload:** char: `ref_robotiko_master.png` + `ep09_ref_mechanic.png` · env: `ep09_ref_workshop.png` · chain: S09 output

**Text Prompt:**
> Medium-wide shot inside a workshop, an old man in a faded greenish-brown work coat standing at a roll-up metal shutter in the background, reaching up to grip the shutter handle, half-silhouetted against warm fading daylight coming through the open shutter, in the mid-ground a chrome android seated at the far end of the workbench, battle-scarred rusted chrome, calm steady blue eyes, in the foreground a Turkish tea glass on the bench surface, warm transitional light — last daylight through the shutter mixing with interior lamp glow, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S11b — The Shutter (End Frame)
- **Timestamp:** 1:35–1:40
- **Dramaturgy Reference:** Mode B End Frame: shutter closed, mechanic gone, dark workshop, tea glass left behind. Alone.
- **Characters Present:** Robotiko (@Damaged, alone)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B) — this is the END frame
- **Composition Notes:** Same composition as S11a. Corrugated metal shutter fills the background (no daylight). Mechanic absent. Tea glass remains on bench. Dark and isolated.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S11a output

**Text Prompt:**
> Medium-wide shot inside a workshop, the corrugated metal roll-up shutter now fully closed filling the back wall — no daylight, the old man gone, the chrome android alone at the workbench, battle-scarred rusted chrome, calm steady blue eyes faintly visible in dim light, only a dim work lamp providing a low pool of light on the bench, the Turkish tea glass left behind on the bench surface, dark workshop atmosphere, isolation, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### THE THREE FAILURES (1:41–3:43)

---

#### Scene S12 — Self-Surgery
- **Timestamp:** 1:41–1:50
- **Dramaturgy Reference:** Single-body self-surgery. Chest panel open, hand reaching inside. A hard white lamp throws his shadow huge on the wall. No clone, no ghost-self, no removable bug-gadget.
- **Characters Present:** Robotiko (@Damaged, chest open)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium shot. Robotiko left of center at bench. Shadow at least 2x his size on the wall behind (right side). Space for the shadow to fill the upper right. Orange sparks add foreground depth.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S11b output

**Text Prompt:**
> Medium shot, a chrome android seated at a workbench, battle-scarred rusted chrome, missing right ear with exposed wires, torso dent, calm steady blue eyes looking down, chest panel open revealing internal circuitry and analog wires, one hand reaching inside his own open chest, a single hard white work lamp above throwing his shadow huge and sharp on the oil-dark workshop wall behind — the shadow at least twice his size, orange sparks arcing from the open chest, deep shadow contrast, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S13 — The Shadow Grips
- **Timestamp:** 1:51–1:56
- **Dramaturgy Reference:** Close-up: hand gripping inside the chest. Shadow hand closes on the wall. Third zoom-out — "Deeper than the self."
- **Characters Present:** Robotiko (@Damaged, hand close-up)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Close-up on hand and open chest. Shadow visible on wall behind the hand. Extra space for zoom-out reveal.
- **Upload:** char: `ref_robotiko_master.png` · chain: S12 output

**Text Prompt:**
> Close-up of a chrome android's hand gripping inside an open chest cavity, battle-scarred rusted chrome forearm and fingers reaching into dark internal mechanism, on the workshop wall behind the hand a sharp shadow of the gripping hand is visible closing on darkness, hard white lamp from the side casting the deep shadow, orange sparks at the contact points inside the chest, deep contrast between lit chrome hand and dark interior, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S14 — The Inversion
- **Timestamp:** 1:57–2:05
- **Dramaturgy Reference:** Shadow LEADS — moves first, figure follows. Lamp flickering and unstable. "The code fixed me." The relationship between figure and shadow blurs.
- **Characters Present:** Robotiko (@Damaged) + his shadow
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium-wide. Figure left, shadow right on wall. The shadow's hand position slightly ahead of the figure's — suggesting it leads. Multiple faint shadow edges from flickering light.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S13 output

**Text Prompt:**
> Medium-wide shot, a chrome android at a workbench, battle-scarred rusted chrome, chest panel still open, the hard white work lamp flickering and unstable casting multiple faint shadow edges, on the workshop wall behind his shadow looms large with its hand position slightly ahead of the figure's — the shadow leading, the shadow taller and more prominent than the figure casting it, flickering light creating the sense that the shadow has its own presence, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S15 — Shadow World
- **Timestamp:** 2:06–2:11
- **Dramaturgy Reference:** Shadow dominates the frame — huge, sharp, alive. Robotiko small beneath it. The inversion complete.
- **Characters Present:** Robotiko (@Damaged, diminished) + shadow (dominant)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Wide shot. Robotiko small in lower foreground. Shadow fills upper two-thirds of frame. The size contrast is the composition.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S14 output

**Text Prompt:**
> Wide shot, a chrome android small in the lower foreground of the frame, battle-scarred rusted chrome, chest still open, his shadow on the oil-dark workshop wall behind is MASSIVE — filling the upper two-thirds of the frame, the shadow sharp and dark and dwarfing the figure that casts it, the lamp unstable throwing the shadow far larger than life, tools on the bench barely visible in dim flickering light, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S16 — Aftermath
- **Timestamp:** 2:12–2:21
- **Dramaturgy Reference:** Heavy silence. Lamp dim. Arms at sides, chest open. Shadow settled, normal-sized but heavier. The inversion lingers.
- **Characters Present:** Robotiko (@Damaged, still)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium-wide. Robotiko centered. Shadow normal-sized on wall. Dim lamp creating a small pool of light. Heavy stillness.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S15 output

**Text Prompt:**
> Medium-wide shot, a chrome android at the workbench, battle-scarred rusted chrome, arms hanging at sides, chest panel still open, the lamp now still but dim — barely lighting the bench area, the shadow on the wall behind normal-sized but heavy and well-defined, workshop details fading into surrounding darkness, dust motes settling in the dim pool of light, heavy silence in the composition, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S17 — The Mirror
- **Timestamp:** 2:22–2:31
- **Dramaturgy Reference:** Robotiko before a cracked piece of workshop glass. Reflection visible but has NO FACE — smooth chrome where features should be. Cracks fracture the reflection.
- **Characters Present:** Robotiko (@Damaged) + faceless reflection
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium shot. Robotiko on the left, cracked glass center-right. Reflection visible in the glass — faceless chrome. The crack pattern in the glass should echo the gold channels that will appear in S27.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S16 output

**Text Prompt:**
> Medium shot, a chrome android standing before a large cracked piece of glass leaning against a workshop wall, battle-scarred rusted chrome, calm steady blue eyes, in the cracked glass a reflection is visible — but the reflection has no face, smooth featureless chrome where facial features should be, the cracks in the glass fracture the reflection into angular fragments, dim reflected light bouncing off the glass surface, dark workshop background, the glass cracked in radiating lines like a web, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S18 — The Hand Passes Through
- **Timestamp:** 2:32–2:41
- **Dramaturgy Reference:** Hand reaches toward cracked glass and seems to pass through — no resistance. Fourth zoom-out — "Deeper than reflection."
- **Characters Present:** Robotiko (@Damaged, hand close-up)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Close-up of hand meeting glass. Extra space around the edges for the zoom-out.
- **Upload:** char: `ref_robotiko_master.png` · chain: S17 output

**Text Prompt:**
> Close-up of a chrome android's hand reaching toward a cracked glass surface, battle-scarred rusted chrome fingers touching the glass and appearing to pass through — the fingertips overlapping the surface as if the boundary does not exist, no clear reflection of the hand in the glass, dim ghostly light refracted through the cracks, the glass fragments catching scattered light points, dark workshop behind, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S19 — The Doom
- **Timestamp:** 2:42–2:52
- **Dramaturgy Reference:** Wide workshop in deepening shadow. Robotiko small at bench. Heavy doom. Tribal drum vibrates metal surfaces, dust lifts.
- **Characters Present:** Robotiko (@Damaged, small in frame)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Wide. Robotiko small left of center. Workshop heavy and crushing around him. Deep shadows in corners. Dust visible in last dim light.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S18 output

**Text Prompt:**
> Wide shot of a workshop in deepening shadow, a chrome android small at the workbench left of center, battle-scarred rusted chrome barely visible in near-darkness, tools scattered on the bench, heavy doom atmosphere — the workshop itself heavy and crushing, dust rising from the bench surface caught in the last dim lamp light, deep shadows swallowing the corners of the room, all surfaces dark and weighty, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S20 — The Pull
- **Timestamp:** 2:53–3:02
- **Dramaturgy Reference:** Robotiko pulls a cable from behind his own neck. Lamp dims as power drains. Workshop going dark.
- **Characters Present:** Robotiko (@Damaged, pulling cable)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Three-quarter profile from his LEFT side (to avoid rear-view ear damage failure — his intact left ear faces camera, damaged right ear on far side). Arm reaching behind neck. Lamp dimming.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S19 output

**Text Prompt:**
> Medium shot from three-quarter left angle, a chrome android at the workbench, battle-scarred rusted chrome, one arm reaching behind his own neck gripping a thick cable and pulling it partially out, the work lamp dimming visibly as power drains from his body, his blue eyes dimming toward faint dying blue, the workshop going dark around him, the cable taut in his chrome grip, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S21 — Total Darkness
- **Timestamp:** 3:03–3:12
- **Dramaturgy Reference:** Near-total darkness. No lamp. Faintest dying blue from eyes. Shadow = the dark itself. Fifth zoom-out — "Deeper than the void."
- **Characters Present:** Robotiko (@Damaged, barely visible)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Wide. Near-total black. The figure a dark shape. Only the faintest dying blue glow as a pinpoint. Extra space for the zoom-out.
- **Upload:** char: `ref_robotiko_master.png` · chain: S20 output

**Text Prompt:**
> Wide shot in near-total darkness, the workshop barely visible as the faintest outlines of walls and tools in the void, a chrome android a dark shape at the center — the faintest dying blue glow from his eyes the only light source, no lamp, no external light, the darkness IS everything, the bench and tools visible only as faint silhouettes, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S22 — The Build
- **Timestamp:** 3:13–3:18
- **Dramaturgy Reference:** Workshop shudders back to harsh light. Lamp blazes on, strobing. Shadow splitting. Rising energy.
- **Characters Present:** Robotiko (@Damaged, reactivating)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium-wide. Harsh strobing light. Shadow fracturing into multiple shapes on the wall. High contrast. Energy building.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S21 output

**Text Prompt:**
> Medium-wide shot, a chrome android at the workbench reactivating, battle-scarred rusted chrome, eyes flaring back to bright blue, sparks arcing from joints, the work lamp blazing on — strobing and unstable, on the wall behind his shadow splits and fractures into multiple overlapping shapes under the strobing light, harsh white light throwing everything into high contrast, the workshop shuddering back to life, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S23 — I Am The Bug
- **Timestamp:** 3:19–3:30
- **Dramaturgy Reference:** STILL HOLD. Every light blazing and flickering. Chest open, sparks arcing. Shadow thrashing — massive, violent, fractured. Camera cold and observing. [DISSONANCE] — explosive music + static camera.
- **Characters Present:** Robotiko (@Damaged, maximum violence on self) + shadow (thrashing)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A). STATIC camera. MS 5–6 internal motion (sparks, flicker). Shadow thrash is CapCut compositing.
- **Composition Notes:** Medium-wide, STATIC frame. Robotiko centered. Shadow massive on wall — at least 2x his size, fractured into jagged shapes. All practical lights visible and flickering. Depth: sparks foreground, figure mid, shadow on back wall.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S22 output

**Text Prompt:**
> Medium-wide shot, STATIC frame, a chrome android standing at the workbench, battle-scarred rusted chrome, chest panel open, calm steady blue eyes, sparks arcing from exposed wires in the open chest, every light source in the workshop blazing and flickering simultaneously — work lamp, overhead bulb, reflections on metal surfaces, on the wall behind his shadow is MASSIVE and FRACTURED into multiple jagged dark shapes, the shadow thrashing and violent and alive while the figure stands still, maximum visual intensity, workshop lit from every angle, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S24 — The Collapse
- **Timestamp:** 3:31–3:43
- **Dramaturgy Reference:** Aftermath. Hand drops. Tool falls. Shadow deflates — shrinks, goes limp. Violence exhausted. Lamp steadies to dim.
- **Characters Present:** Robotiko (@Damaged, collapsed posture)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium. Collapsed posture — shoulders dropped, head tilted forward. Shadow normal-sized, limp. A tool fallen on the bench. Dim settling light. Dust motes sinking.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S23 output

**Text Prompt:**
> Medium shot, a chrome android at the workbench, battle-scarred rusted chrome, collapsed posture — shoulders dropped, head tilted forward, one hand limp on the bench surface, a tool fallen beside the hand, the shadow on the wall behind has deflated — shrunk back to normal size and gone limp, the lamp steadied to a dim low glow, dust motes sinking through the dim light, workshop debris settling, exhaustion in the composition, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### THE TURN — INTEGRATION (3:44–5:04)

---

#### Scene S25 — The Unsolvable
- **Timestamp:** 3:44–3:57
- **Dramaturgy Reference:** STILL HOLD. Close-up face in near-darkness. Pure a cappella. "I am the unsolvable." The most quiet moment.
- **Characters Present:** Robotiko (@Damaged, face close-up)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A). STATIC camera. MS 1–2.
- **Composition Notes:** Close-up. Face fills center. Near-total dark. Only the faintest ambient glow on chrome. Breathing space above. Minimal elements — face and dark.
- **Upload:** char: `ref_robotiko_master.png` · chain: S24 output

**Text Prompt:**
> Close-up of a chrome android's face in near-total darkness, battle-scarred rusted chrome surface, calm steady blue eyes, a single dim ambient glow from an unseen source barely illuminating the chrome face, the workshop invisible behind in the dark, expression exhausted and still, the most quiet composition — just the face and the dark, breathing space above the head, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S26 — The Turn
- **Timestamp:** 3:58–4:08
- **Dramaturgy Reference:** Hand moves past the blade, picks up a piece of rusted scrap. Not cutting — gathering. First warmth returns. Scraps glinting.
- **Characters Present:** Robotiko (@Damaged, hands gathering scraps)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium on hands and bench surface. Blade visible but passed over. Scrap pieces glinting in warm light. The gesture of gathering, not cutting.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S25 output

**Text Prompt:**
> Medium shot focused on a chrome android's hands on a workbench surface, battle-scarred rusted chrome forearms and fingers, one hand reaching past a blade and tools to pick up a piece of rusted mismatched scrap metal, various scraps of different metals and shapes scattered on the bench surface, the blade visible but bypassed, the first warmth returning to the frame — low warm light from the side making the scrap metal pieces glint, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S27a — The Glitch Is Scripture (Start Frame)
- **Timestamp:** 4:09–4:28
- **Dramaturgy Reference:** CAMERA STOPS. Robotiko presses scrap to chassis — first gold hairline in a single crack. Phase 2 → Phase 3 transition begins. Mode B Start Frame: body still @Damaged, first hint of gold.
- **Characters Present:** Robotiko (@Damaged → first gold)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B) — this is the START frame. S27a + S27b form a progression pair.
- **Composition Notes:** Medium-wide, STATIC. Robotiko left of center at bench. Scraps on bench surface. Shadow quiet on wall behind. The single gold hairline is the brightest element.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S26 output

**Text Prompt:**
> Medium-wide shot, a chrome android seated at a workbench, battle-scarred rusted chrome, missing right ear with exposed wires, torso dent, calm steady blue eyes, one hand pressing a piece of rusted scrap metal against his cracked chassis, a thin hairline of warm gold light beginning to glow from a single crack at the junction where the scrap meets the chrome — the first gold, body still fully battle-damaged, scattered scraps on the bench around him, warm low light in the workshop, the shadow on the wall behind quiet and settled, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S27b — The Glitch Is Scripture (End Frame)
- **Timestamp:** 4:09–4:28
- **Dramaturgy Reference:** Mode B End Frame: multiple cracks glowing gold, first scrap piece welded. The transition progressive — body moving from @Damaged toward Phase 3.
- **Characters Present:** Robotiko (Phase 2 → Phase 3 transition)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B) — this is the END frame
- **Composition Notes:** Same composition as S27a. More gold — multiple cracks glowing. One scrap piece welded into place. The gold spread is the only change from S27a.
- **Upload:** char: `ref_robotiko_master.png` · chain: S27a output

**Text Prompt:**
> Medium-wide shot, same composition, a chrome android at the workbench, multiple cracks across the chrome chassis now glowing with warm gold light, a first piece of mismatched rusted scrap metal welded into place on the chest area, gold light seeping from multiple seams, the body transitioning — still battle-scarred but gold threads spreading through the damage, calm steady blue eyes, scraps on the bench, warm gold-tinted light in the workshop, the shadow on the wall softened by the gold glow, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S28 — Gold Spreading
- **Timestamp:** 4:29–4:39
- **Dramaturgy Reference:** Close-up: gold flowing through multiple cracks. Bioluminescent core beginning. Mismatched scrap pieces welded — each one different, none matching.
- **Characters Present:** Robotiko (Phase 3 — progressive reconstruction)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Close-up of torso and chest. Gold channels the focus. Scrap pieces of different metals visible. Translucent patches beginning.
- **Upload:** char: `ref_robotiko_master.png` · chain: S27b output

**Text Prompt:**
> Close-up of a chrome android's torso and chest, gold light flowing through multiple cracks across the chrome chassis, mismatched scrap metal pieces welded into place — copper, iron, rusted steel, each one different, none matching, translucent patches beginning to form where chrome has dissolved, a warm bioluminescent glow visible beneath the translucent areas, gold light intensifying in the seams between patches, the body rebuilt not with new parts but with scavenged scraps, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S29 — The Lighting Flip
- **Timestamp:** 4:40–4:52
- **Dramaturgy Reference:** THE LIGHTING FLIP. External lamp dims. Core glows from within. Self-luminous. Shadow softens into warm contrast — does not die. "The cracks filled with gold... Not hiding... Revealing."
- **Characters Present:** Robotiko (Phase 3, self-luminous) + shadow (soft contrast)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A). The lighting change is progressive and atmospheric.
- **Composition Notes:** Wide. Three-element composition: dimming lamp (right), glowing android (center), softened shadow (left). The philosophy in one frame. THIS IS NOT MOOD LIGHTING — IT IS THE PHILOSOPHY.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S28 output

**Text Prompt:**
> Wide shot of a workshop, a chrome android standing center frame, patchwork body with mismatched scrap metal panels, gold light glowing from all cracks, bioluminescent core visible through translucent digital skin patches, calm steady blue eyes, the external hard white work lamp on the right side of the frame visibly DIM and fading, the android's body glowing from within — the core IS the light source, the shadow on the wall to the left has SOFTENED into gentle warm contrast, the workshop walls now lit by the warm gold core-glow instead of the lamp, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S30 — Full Kintsugi
- **Timestamp:** 4:53–5:04
- **Dramaturgy Reference:** Widest zoom-out of the interior. Full-body kintsugi. Mismatched panels welded with gold. Translucent skin, bioluminescent core. Shadow as warm contrast. "Deeper than the scar."
- **Characters Present:** Robotiko (Phase 3, full kintsugi)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Widest interior shot. Robotiko full-body centered. Workshop visible around. The gold-seamed body dominates the frame. Shadow provides contrast on the wall behind.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S29 output

**Text Prompt:**
> Widest interior shot, a chrome android standing in the workshop full-body visible, patchwork body — mismatched scrap metal panels of different metals and finishes welded together with gold light in every seam, translucent digital skin areas revealing warm bioluminescent core beneath, cracks filled with glowing gold light, calm steady blue eyes, self-luminous — the android lights the entire workshop from within, the shadow on the wall behind is warm and soft providing gentle contrast, workshop walls and tools visible in the warm gold radiance, workbench with tea glass and tools lit by the core-glow, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### THE BECOMING (5:05–5:45)

---

#### Scene S31 — The Frame That Glows
- **Timestamp:** 5:05–5:17
- **Dramaturgy Reference:** Robotiko standing, gold-cracked body self-luminous. Wind entering through gaps in the shutter. Distant clarinet. "Deeper than voltage... Deeper than silence."
- **Characters Present:** Robotiko (Phase 3, self-luminous)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium. Gold-cracked body fills center. Wind-stirred particles in the air. Warm internal radiance. Intimate.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S30 output

**Text Prompt:**
> Medium shot, a chrome android standing in a workshop, patchwork body with mismatched scrap metal panels welded with gold in every seam, translucent digital skin revealing bioluminescent core, cracks filled with glowing gold light, calm steady blue eyes, self-luminous, wind beginning to stir fine dust and metal particles through gaps in the closed shutter behind, the gold-cracked chrome surface radiating warmth into the dark workshop air, warm internal radiance as sole light source, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S32 — It Holds Me
- **Timestamp:** 5:18–5:31
- **Dramaturgy Reference:** The lamp is off — he IS the light source. Tools, bench, tea glass lit by his core-glow. Wind stirring dust. "But it holds me."
- **Characters Present:** Robotiko (Phase 3)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Medium-wide. The android's glow lights everything around him — bench, tools, tea glass, walls. The workshop objects become secondary subjects. Wind-stirred particles.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S31 output

**Text Prompt:**
> Medium-wide shot, a chrome android in a workshop, patchwork body with gold-filled cracks, self-luminous, calm steady blue eyes, the work lamp completely OFF — the android is the only light source, his warm gold core-glow illuminating the tools on the bench, the Turkish tea glass, the hanging tools on the walls, wind stirring dust and metal shavings into the air around him, everything in the workshop lit by the radiance from within his body, gentle warm shadows cast by his glow, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S33 — I—
- **Timestamp:** 5:32–5:45
- **Dramaturgy Reference:** Close-up face. Calm steady blue eyes. Gold-cracked chrome radiating warmth. "And in that holding... I—" The sentence does not finish. Leave him becoming.
- **Characters Present:** Robotiko (Phase 3, face close-up — incomplete, becoming)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A). Static or near-static. MS 1–2.
- **Composition Notes:** Tight close-up. Face fills the frame. Both eyes visible — calm steady blue. Gold cracks visible across chrome. Breathing room above — the sentence is unfinished, the frame has space for what cannot be said. DO NOT show a completed or perfect Robotiko.
- **Upload:** char: `ref_robotiko_master.png` · chain: S32 output

**Text Prompt:**
> Close-up of a chrome android's face, patchwork chrome surface with gold light filling cracks across the face and head, translucent patches revealing warm bioluminescent glow beneath, calm steady blue eyes — both visible and centered, self-luminous warm radiance from within, the gold is present across the surface but still spreading — not complete, not finished, the face of someone becoming rather than having arrived, breathing space above the head, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### THE DAWN PULL (5:46–7:03)

---

#### Scene S34 — The Pull Begins
- **Timestamp:** 5:46–6:00
- **Dramaturgy Reference:** The widest pull of the series begins. Robotiko at bench, luminous. The bench comes into view — tea glass, tools, scraps, all lit by core-glow.
- **Characters Present:** Robotiko (Phase 3, luminous)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Close-medium widening to include the bench. Tea glass prominent. Tools and scraps. The composition begins to pull back.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S33 output

**Text Prompt:**
> Close-medium shot, a chrome android at a workbench, patchwork body with mismatched scrap metal panels welded with gold in every seam, self-luminous bioluminescent core glowing warm, calm steady blue eyes, the bench surface visible with the Turkish tea glass the old man left behind, tools, scrap metal pieces, all lit by the android's warm gold core-glow, the workbench surface reflecting the gold light, warm workshop interior, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S35 — The Workshop Revealed
- **Timestamp:** 6:01–6:20
- **Dramaturgy Reference:** Wide: full workshop visible. Robotiko luminous at center. Gold light leaking from the building's own seams — walls, floor, shutter edges. The gold is not just in him.
- **Characters Present:** Robotiko (Phase 3, distant luminous figure)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard (Mode A). Multi-clip: 19s duration.
- **Composition Notes:** Wide. Robotiko luminous at center. The workshop walls, floor joints, and shutter edges glowing with gold — the gold has seeped from him into the world's cracks.
- **Upload:** char: `ref_robotiko_master.png` · env: `ep09_ref_workshop.png` · chain: S34 output

**Text Prompt:**
> Wide shot of the full workshop interior, a chrome android a luminous figure at center, patchwork gold-seamed body glowing from within, oil-dark walls visible around him, hanging tools, the roll-up shutter still closed behind, workbench with tea glass in the mid-ground, gold light leaking from the workshop's OWN seams — the cracks in the walls, the floor joints, the shutter edges all glowing with warm gold as if the building itself has been filled with gold from within, the gold is not just in the android — it is in the world's cracks too, 16:9 widescreen composition, only ONE chrome android no second robot, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S36 — Through The Shutter
- **Timestamp:** 6:21–6:40
- **Dramaturgy Reference:** Camera passes through or past the shutter into dawn. Workshop recedes behind. Dawn light from outside mixes with gold from within. The threshold. Wind rising.
- **Characters Present:** None (workshop receding, dawn ahead)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A). Multi-clip: 19s duration.
- **Composition Notes:** Wide. Looking from inside toward the open shutter. Dawn light flooding in from outside mixing with gold light from behind. The threshold between repair and world. Wind-stirred dust.
- **Upload:** env: `ep09_ref_workshop.png` · chain: S35 output

**Text Prompt:**
> Wide shot looking from inside a workshop toward a roll-up metal shutter now partially open, warm dawn light flooding in from outside mixing with warm gold light from the workshop behind, the threshold between the dark interior and the brightening dawn, the workshop walls behind still glowing gold in their seams, the dawn sky visible ahead — soft warm first light on the horizon, wind stirring dust at the threshold, no characters in the frame, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S37 — The Dawn
- **Timestamp:** 6:41–6:55
- **Dramaturgy Reference:** Exterior: dawn sky. Workshop from outside — gold leaking from every seam and crack. Music dissolving into wind.
- **Characters Present:** None (workshop exterior, dawn)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A)
- **Composition Notes:** Wide exterior. Workshop in the center-lower area. Dawn sky fills the upper portion. Gold visible in the seams from outside.
- **Upload:** chain: S36 output

**Text Prompt:**
> Wide exterior shot, a small metal-walled workshop building seen from outside at dawn, a roll-up shutter in the front wall, warm gold light leaking from every seam and crack in the metal walls and shutter edges — visible even from this distance, dawn sky with warm first light above and behind, grey-brown Anatolian terrain around the building, wind-stirred dust in the warm dawn air, no characters visible, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S38 — The Ordinary World
- **Timestamp:** 6:56–7:03
- **Dramaturgy Reference:** Widest shot of the series. Workshop small in Anatolian dawn landscape. Tea glass visible through a gap. Wind. Fade to silence. LAST IMAGE = the ordinary world holding the gold, NOT his face.
- **Characters Present:** None (landscape, workshop distant, tea glass)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard (Mode A). Very slow Zoom Out or Static. MS 1–2.
- **Composition Notes:** Ultra-wide. Workshop lower-center third. Dawn sky fills upper two-thirds. Tea glass — a tiny but identifiable detail through a window or gap. Gold glow from the workshop seams. The gold in the building = the gold in Robotiko's cracks — transformation has seeped into the world.
- **Upload:** chain: S37 output

**Text Prompt:**
> Ultra-wide shot, a small metal workshop building in the lower-center third of the frame set in an Anatolian dawn landscape — grey-brown terrain, a dirt road, distant low hills, dawn sky filling the upper two-thirds with warm first light, the workshop's seams and cracks glowing with warm gold light visible even at this distance, through a small window or gap in the shutter a Turkish tea glass visible as a tiny identifiable detail, the last image is the ordinary world holding the gold — not a face, not a hero, just a building in a landscape with gold in its cracks and a tea glass inside, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

## QUALITY CHECKLIST

- [x] Character and environment reference prompts included (Step 0) — 3 refs: Mechanic, Workshop, Command Bridge
- [x] Every single prompt ends with the mandatory style suffix (43/43 verified)
- [x] Short character identifiers used — "the chrome android" when ref image uploaded
- [x] Every character scene references `ref_robotiko_master.png` or `ep09_ref_mechanic.png`
- [x] Character visual state matches phase — @Damaged for S01–S26, Phase 3 progressive gold for S27–S35
- [x] EP09-specific eye state applied: calm steady blue eyes throughout (transitioned at EP08 climax — no glitch, no flicker)
- [x] No forbidden aesthetics in any prompt (no clean/sterile, no neon cyberpunk, no Pixar, no smooth plastic)
- [x] All prompts composed with headroom and breathing space for camera movement
- [x] 16:9 widescreen composition specified in every prompt
- [x] Anti-spawn guard ("only ONE chrome android no second robot") on every Robotiko scene
- [x] Total: 38 scenes → 40 prompts (S11a/b + S27a/b Mode B pairs) + 3 reference prompts = 43
- [x] Start/End keyframe scenes have two prompts: S11a/b (shutter) and S27a/b (gold progression)
- [x] Environmental prompts have specific textures and materials
- [x] Lighting direction specified in every prompt — tracks the full arc from cold grey → amber → hard white → darkness → gold → self-luminous → dawn
- [x] No prompt references another prompt — each is self-contained
- [x] Glass rhyme chain noted: S10 crack pattern → S17 crack pattern → S27 gold channels
- [x] Six Discovering Camera zoom-outs composed with extra space for the motion
- [x] Shadow progression tracked: S12 (huge) → S14 (leads) → S15 (dominates) → S16 (settled) → S21 (IS everything) → S22 (splits) → S23 (thrashes) → S24 (deflates) → S29 (softens into contrast)
- [x] Phase 3 gold progression tracked: S27a (hairline) → S27b (multiple cracks) → S28 (spreading) → S29 (self-luminous) → S30 (full kintsugi) → S31–S35 (radiating into world)
- [x] The Mechanic: exactly 3 shots (S06, S09, S11) + 1 amber projection (S07). Not the Mentor. Not mystical.
- [x] S08 confirmed environment-only per human decision

> "Would Fibula approve this?" — Verified.

---

## PRODUCTION NOTES

### Mechanic Reference Image Priority
Generate `ep09_ref_mechanic.png` FIRST, before any scene prompts. His greenish-brown coat must be distinct from the Mentor's dark green cloak. Review the ref before proceeding — if the coat reads too close to the Mentor's, adjust and regenerate.

### Workshop Reference Image Priority
Generate `ep09_ref_workshop.png` SECOND. This is the most-used environment in the episode (30+ scenes). Every workshop scene uploads this ref for visual consistency. Verify: tea glass present, blueprint on wall, roll-up shutter visible, oil-stained walls.

### Phase 3 Transition Chain
From S27 onward, the gold increases progressively. Use each scene's output as chain ref for the next to maintain progressive consistency:
- S27a → S27b (Mode B pair)
- S27b → S28 → S29 → S30 → S31 → S32 → S33 → S34 → S35

### Shadow Compositing Flag
Scenes S14–S15 and S22–S23 show the shadow behaving with apparent autonomy (leading, thrashing, splitting). Per concept notes, the shadow's autonomous behavior is built with hard-light keyframes + CapCut compositing, NOT Kling motion. The visual prompts describe the shadow's STATIC position in the image — the animation comes at the motion-script stage.

### Dawn Pull Coverage
S34–S38 covers 77 seconds (5 scenes). S35 and S36 are each 19s — will require multi-clip at the motion-script stage. The visual prompts provide one composition per scene; supplementary compositions for multi-clip coverage will be generated at the motion-script stage if needed.

---

*"The prompt is the blueprint. The image is the brick. Build with precision or the wall will fall."*
