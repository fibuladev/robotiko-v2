# VISUAL PROMPTS — EP06
> **Version:** v01 | Skill: `_skills/robotiko-visual-prompts/SKILL.md`
> **Generated:** 2026-05-01

---

## PRE-GENERATION CHECKLIST

- [x] `_management/master.md` → Visual DNA, color palette, forbidden list, mandatory suffix
- [x] `episode-06/03_direction/ep06_dramaturgy_v01.md` → APPROVED scene breakdown (43 scenes)
- [x] `_assets/cast/character_profiles.json` → Phase 2: Destruction visual state + Perfect Worker = pristine ref
- [x] `_assets/cast/ref_robotiko_master.png` → Visual reference (Robotiko + Perfect Worker share same base form)
- [x] `episode-06/03_direction/ep06_concept_notes.md` → 8 human overrides, single-location discipline, camera escalation
- [x] `_memory/lessons.md` → 16:9 rule, short identifier rule, env ref rule, tool-friendly prompts

> ⚠️ Dramaturgy APPROVED 2026-05-01. Visual prompt generation authorized.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP06 |
| **Title** | The Perfect Little Worker |
| **Station** | The Tranquil Self — Broken (Identity erasure / First rebellion) |
| **Character Phase** | Phase 2: Destruction |
| **Robotiko Visual State** | rusted and cracked chrome chassis, sparks flying from joints, glitching blue-red eyes, exposed and fraying analog wires, battle-damaged retro-futuristic body |
| **Perfect Worker Visual State** | pristine titanium chassis, factory-fresh surface, zero damage, steady cold blue eyes — same body form as Robotiko but untouched by experience |
| **Total Prompts** | 47 (2 environment reference + 45 scene prompts, including 2 Mode B pairs) |

---

## MANDATORY STYLE SUFFIX
> ⛔ This suffix must be appended to EVERY prompt without exception. Do not modify.

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## FORBIDDEN AESTHETICS REMINDER
- ❌ Clean Apple design
- ❌ Pixar-style rendering
- ❌ Generic cyberpunk neon
- ❌ Smooth plastic textures
- ❌ Cheap melodrama or ornamental excess

---

## SHORT IDENTIFIERS (When Reference Image Is Uploaded)

| Character | Short Identifier | Reference Path | Notes |
|---|---|---|---|
| Robotiko (Phase 2) | "the damaged chrome android" | `_assets/cast/ref_robotiko_master.png` | Ref shows pristine form — damage MUST be described in prompt text |
| The Perfect Worker | "the pristine chrome android" | `_assets/cast/ref_robotiko_master.png` | Ref IS the Perfect Worker — same pristine body, no damage needed in prompt |

> **Key:** Both characters share the same reference image. Differentiation is carried entirely by prompt language: "damaged/rusted/cracked/sparking" vs "pristine/factory-fresh/unmarked/unblemished."

---

## REFERENCE PROMPTS (Generate These FIRST — Before Any Scene Prompts)

---

### REF-ENV-01 — The Cold Office

**Purpose:** Master environment reference for EP06. The same retro-futuristic office from EP05 (scenes 22-23) with all warmth stripped. Generate first, upload alongside every office scene prompt. This single space contains 90% of the episode.

**Text Prompt:**
> Wide establishing shot of a vast retro-futuristic open-plan office floor. No characters present. Dozens of identical chrome workstations spread across the wide floor in precise geometric rows, each with a large CRT monitor displaying green phosphor text on black. Heavy mechanical keyboards with chrome keycaps sit on each titanium desk surface. Cold fluorescent tube lighting mounted in parallel strips along the high ceiling casts flat, even, institutional white light across the entire space — no warm accents, no amber, no golden tones. Filing cabinets in brushed chrome line the distant walls. The floor is polished industrial chrome tile stretching deep into the background, reflecting the cold fluorescent strips above. Identical chrome office chairs at every station. The color palette is exclusively cold: silver, grey, institutional white, green CRT glow. The atmosphere is sterile, efficient, systematic — a workspace drained of all warmth and personality. 16:9 widescreen composition with deep perspective through the desk rows. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF-ENV-02 — The Meeting Room

**Purpose:** Environment reference for S36. Small 1-to-1 meeting room within the same office building. Generate first, upload alongside S36 prompt. Used for the "mirror" scene.

**Text Prompt:**
> Wide establishing shot of a small retro-futuristic meeting room. No characters present. Glass walls on two sides reveal the larger office floor beyond. A large flat screen is mounted on the far wall — its surface dark, reflective, mirror-like. A narrow chrome table runs between two chrome office chairs facing each other. The same cold fluorescent tube lighting from the main office illuminates the room, but the smaller space makes it feel more concentrated, more intimate. The glass walls create partial reflections of the room's interior. The dark screen dominates the far wall — large enough to reflect two seated figures clearly. The floor is the same polished chrome tile as the main office. Minimal, functional, impersonal — the corporate ritual space of the private meeting. 16:9 widescreen composition with the dark screen as the focal point on the back wall. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

---

## GENERATED PROMPTS

### INTRO (0:00 - 0:38)

---

#### Scene S01 — Office Establishing / Post-Crash Hangover
- **Timestamp:** 0:00
- **Dramaturgy Reference:** Wide establishing shot of the cold office. Robotiko slumped at desk, damaged and depleted. Empty desk beside him. No amber anywhere.
- **Characters Present:** Robotiko (Phase 2)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot with deep perspective through desk rows. Robotiko positioned in the left-center third. Empty desk beside him provides negative space. Headroom above for fluorescent ceiling.

**Text Prompt:**
> Wide shot of a vast retro-futuristic open-plan office. The damaged chrome android sits slumped at a workstation in the left-center of the frame, his rusted chrome body hunched forward, one hand flat on the titanium desk surface. His cracked chassis shows exposed fraying analog wires at the collar and shoulders, sparks dripping intermittently from a damaged joint. His glitching blue-red eyes are dimmed, barely cycling. Rows of identical workstations stretch behind him into deep perspective — CRT monitors dark, chrome chairs pushed in, surfaces clean and empty. Cold fluorescent tube lighting from the ceiling casts flat white light across the sterile grid. The desk beside him is conspicuously empty. No warm tones anywhere — only cold silver-blue, institutional grey, and the faint green of distant CRT screens. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S02 — CRT Reflection
- **Timestamp:** 0:10
- **Dramaturgy Reference:** Close-up of Robotiko's face reflected in his dark CRT monitor. Eyes dimmed, rust streaks on jaw.
- **Characters Present:** Robotiko (Phase 2)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Close-up, CRT filling lower portion of frame, reflection visible on dark screen. Breathing space above.

**Text Prompt:**
> Close-up of a dark CRT monitor screen on a chrome workstation. The screen is powered off, its dark glass surface reflecting the face of the damaged chrome android sitting before it. In the reflection: his glitching blue-red eyes are dimmed to a faint pulse, rust streaks trace down the chrome jawline like dried tear tracks, a hairline crack runs across his left temple. The reflection stares back — a damaged machine looking at its own wreckage in the dead glass. Cold fluorescent light from above provides flat, unflattering illumination. The chrome frame of the monitor surrounds the dark reflection. Minimal ambient light, cold blue-grey tones only. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S03 — Tattoo Reveal (USER OVERRIDE #1)
- **Timestamp:** 0:18
- **Dramaturgy Reference:** Robotiko's inner forearm on desk. Four robochica tattoos visible: _1, _2, _3, _4. Glowing amber lines on damaged chrome. No emphasis — the arm simply lies there.
- **Characters Present:** Robotiko (Phase 2) — forearm detail only
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Tight on forearm resting on desk surface. Tattoos read top-to-bottom (wrist toward elbow). Leave breathing space above the arm for atmospheric motion.

**Text Prompt:**
> Close-up of a chrome android's inner forearm resting on a cold titanium desk surface. The forearm chrome is rusted and scratched, showing battle damage and patina. Four tattoo-like markings are etched into the chrome in descending sequence from wrist toward elbow: small serial designations rendered as glowing amber lines — warm golden-orange etchings on the damaged chrome surface, each one clean and deliberate against the rusted metal. The amber glow of the etchings is the only warm color in the frame. A thin copper wire frays from a crack near the wrist joint. Cold fluorescent light from above illuminates the desk surface. The titanium desk stretches slightly out of focus behind the forearm. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S04 — Alone in the Grid
- **Timestamp:** 0:27
- **Dramaturgy Reference:** Wide shot. Robotiko alone in the vast office. Empty workstations stretch behind him. He is the only imperfection in the sterile grid.
- **Characters Present:** Robotiko (Phase 2)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot with extreme depth. Robotiko small in the grid but identifiable by his damage. Headroom above for fluorescent ceiling perspective.

**Text Prompt:**
> Wide shot of a vast retro-futuristic open-plan office. The damaged chrome android sits alone at a workstation, the only presence in a space designed for dozens. His rusted, cracked chrome body — sparks dripping from a shoulder joint, fraying wires at his collar — is the single imperfection in the sterile geometric grid. Empty workstations stretch behind him in precise rows, CRT monitors dark, chrome chairs pushed in, surfaces clean. The distant blue glow of a few flickering CRT screens provides the only variation in the flat fluorescent wash from above. Deep perspective lines converge toward the far wall. Cold silver-blue and institutional grey dominate the entire frame. 16:9 widescreen composition with the android small but visible amid the vast grid. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SILENCE + SPOKEN COMMAND (0:38 - 0:54)

---

#### Scene S05 — The Silence
- **Timestamp:** 0:38
- **Dramaturgy Reference:** Office in complete stillness. Wide shot from far end. No movement, no presence. The hum of fluorescent lights is the only life.
- **Characters Present:** None
- **Image Reference Path:** `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot from the far end of the room. Ceiling strips stretching into perspective. Perfect symmetry and stillness.

**Text Prompt:**
> Wide shot from the far end of a vast retro-futuristic open-plan office. No characters present. Ceiling fluorescent tube strips stretch in parallel lines into deep perspective. Rows of identical chrome workstations fill the floor in precise grid formation, CRT monitors dark, chairs tucked in. The polished chrome floor reflects the fluorescent strips above in long pale streaks. Complete stillness — no motion, no presence, no warmth. The institutional hum of fluorescent lighting is the only life in the space. Cold white, silver, and grey dominate every surface. The symmetry of the empty workspace is absolute. 16:9 widescreen composition with strong vanishing-point perspective. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S06 — The PA Command
- **Timestamp:** 0:47
- **Dramaturgy Reference:** Office ceiling: a grey PA speaker on institutional ceiling tiles, flanked by fluorescent strips. The command comes from the building itself.
- **Characters Present:** None (PA system only)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** Looking up at ceiling. PA speaker centered. Fluorescent strips flanking. The tops of workstation monitors visible below.

**Text Prompt:**
> Low-angle shot looking up at a retro-futuristic office ceiling. A grey industrial PA speaker is mounted centrally on institutional ceiling tiles, its circular grille facing downward — impersonal, architectural, faceless. Cold fluorescent tube strips flank the speaker on both sides, their white light harsh and flat. The speaker is weathered grey metal with a chrome mounting bracket. Below the ceiling line, the tops of CRT monitors and the edges of chrome workstation partitions are partially visible. The composition is institutional, authoritarian — the voice of the building itself. Cold white and grey tones only. 16:9 widescreen composition with the speaker centered in the upper portion of the frame. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 1 + REFRAIN 1 (0:55 - 1:29)

---

#### Scene S07 — The Perfect Worker (USER OVERRIDE #2)
- **Timestamp:** 0:55
- **Dramaturgy Reference:** First clear shot of the Perfect Worker at his workstation. Pristine titanium, steady cold blue eyes, working in silence. Factory-fresh, zero damage.
- **Characters Present:** The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. Worker centered at desk. Space around for the environment to read. The pristine surface catches fluorescent light cleanly.

**Text Prompt:**
> Medium shot of the pristine chrome android seated at a retro-futuristic workstation. His titanium chassis is factory-fresh — no scratches, no wear, no patina, zero history. His steady cold blue eyes are locked on the CRT screen before him, never flickering, never glitching. His hands are precisely positioned on the mechanical keyboard, posture perfect. Clean bundled analog wires visible at his neck and wrists — blue and red, neatly routed, undamaged. The chrome surface reflects the cold fluorescent ceiling light without distortion — a mirror that has never been cracked. The green glow of the CRT screen illuminates his unblemished face. Identical workstations visible in the background. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S08 — The Contrast
- **Timestamp:** 1:07
- **Dramaturgy Reference:** Both in frame. Robotiko (left, damaged) at his desk, Perfect Worker (right, pristine) at adjacent workstation. The contrast is the thesis.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium-wide shot. Robotiko left, Worker right. The two desks side by side. The split between damaged and pristine reads horizontally across the frame.

**Text Prompt:**
> Medium-wide shot of two chrome androids at adjacent retro-futuristic workstations. On the left, the damaged chrome android — rusted joints, cracked chassis panels, sparks dripping from a shoulder, fraying blue and red analog wires exposed at the collar, glitching blue-red eyes fixed on the figure beside him. On the right, the pristine chrome android — factory-fresh titanium surface catching the light without a single distortion, steady cold blue eyes locked on his CRT screen, posture perfect, hands precise on the keyboard. Same body form, opposite condition. The warm rust and copper tones of the damaged body contrast sharply with the clean silver of the untouched one. Cold fluorescent lighting from above. The pristine worker does not acknowledge the damaged one. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S09 — Refrain 1: The Wide Observation (USER OVERRIDE #3a)
- **Timestamp:** 1:20
- **Dramaturgy Reference:** Wide shot of the workspace between them. Several empty desks separate Robotiko from the Perfect Worker. Sardonic detachment — leaning back, observing from distance.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker (distant)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot. Robotiko in the left foreground, leaning back in chair. Worker small and distant in the right background. The space between them is the composition.

**Text Prompt:**
> Wide shot of a retro-futuristic office floor. In the left foreground, the damaged chrome android leans back in his chrome office chair, one rusted arm draped over the chair back, observing from a distance. His cracked chassis and sparking shoulder are prominent. Several empty workstations with dark CRT monitors and tucked-in chairs fill the space between. At the far right background, the pristine chrome android sits at his workstation — a small, clean shape, head down, typing steadily. The physical distance between the two figures spans multiple desk rows. Cold fluorescent lighting illuminates the geometric grid of empty desks between them. 16:9 widescreen composition with strong depth and the empty space as the emotional center. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### INSTRUMENTAL 1 (1:30 - 1:45)

---

#### Scene S10 — Office Architecture
- **Timestamp:** 1:30
- **Dramaturgy Reference:** Office perspective — rows of identical workstations stretching to vanishing point. CRT monitors flickering green. The geometry of obedience.
- **Characters Present:** None (environment)
- **Image Reference Path:** `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Deep perspective vanishing point. No characters. The architecture IS the subject. Headroom and depth for slow camera drift.

**Text Prompt:**
> Deep perspective shot down a corridor of identical retro-futuristic workstations. No characters present. Chrome desks stretch in precise rows to a distant vanishing point. CRT monitors flicker with green phosphor text in sequence down the aisle. Identical mechanical keyboards, identical chrome chairs, identical cable routing along the polished chrome floor. Cold fluorescent tube strips on the ceiling create rhythmic light bars down the corridor. The geometry is absolute — infinite repetition, no deviation, no personality. Green CRT glow and cold white fluorescent are the only light sources. 16:9 widescreen composition with extreme depth to vanishing point. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S11 — Profile of Compliance
- **Timestamp:** 1:38
- **Dramaturgy Reference:** The Perfect Worker in profile. Hands at keyboard, precise movements. Cold blue eyes scanning screen data. The employee the system designed.
- **Characters Present:** The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Profile shot from the side. Worker filling the right two-thirds. CRT screen visible in front of him. Clean, side-lit composition.

**Text Prompt:**
> Profile shot of the pristine chrome android at his workstation. His titanium surface is immaculate — not a scratch, not a mark. His steady cold blue eyes scan the green data on the CRT screen without expression. His hands rest on the mechanical keyboard, fingers positioned with measured precision. Head level, shoulders square, posture perfect. Clean analog wires neatly bundled at his neck joint. Cold fluorescent side-light from the left models the clean chrome planes of his face. The CRT screen casts a faint green glow on his unblemished cheek plate. A profile of absolute compliance — the employee the system designed. 16:9 widescreen composition with the worker in the right two-thirds, screen glow as secondary light source. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 2 + REFRAIN 2 (1:46 - 2:28)

---

#### Scene S12 — Leaning Forward
- **Timestamp:** 1:46
- **Dramaturgy Reference:** Robotiko leaning forward at his desk, addressing the worker across the gap. Damage prominent — rusted elbows on desk, sparks from shoulder.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker (background)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot focused on Robotiko. Worker visible in background, head down, working. Robotiko's damage fills the foreground.

**Text Prompt:**
> Medium shot of the damaged chrome android leaning forward at his workstation. His rusted chrome elbows rest on the titanium desk surface, cracked chassis plates visible at the torso, sparks dripping from a damaged joint at his left shoulder. His glitching blue-red eyes are fixed intently on the figure at the adjacent workstation. Fraying analog wires hang from a gap at his collar. In the background, the pristine chrome android continues to work at his desk — head down, hands on keyboard, steady cold blue eyes on his screen, completely unresponsive. Cold fluorescent overhead light. The damage on the android's body is prominent and detailed in the foreground. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S13 — Damaged Hands
- **Timestamp:** 1:58
- **Dramaturgy Reference:** Close-up of Robotiko's hands on the desk surface. Right wrist cracked, sparks dripping. Copper wires fray. Left hand trembles.
- **Characters Present:** Robotiko (Phase 2) — hand detail
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Tight close-up on both hands spread on the desk. Desk surface provides background. Space for atmospheric motion (spark drip).

**Text Prompt:**
> Close-up of two chrome android hands spread flat on a cold titanium desk surface. The chrome is rusted, scratched, battle-worn. The right wrist joint is cracked open, revealing copper wires inside, small sparks dripping in slow intervals onto the desk surface from the gap. A fraying copper wire catches the light at the crack edge. The left hand shows a faint micro-vibration — a tremor visible in the surface reflections on the polished desk below. The fingers are spread, each one showing scratches and patina from use. Cold fluorescent light from above. The warm spark glow from the cracked wrist provides the only non-cold light in the frame. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S14 — Jaw Clenched
- **Timestamp:** 2:09
- **Dramaturgy Reference:** Close-up of Robotiko's face. Jaw clenched, chrome plates grinding. Rust streaks like dried tear tracks. Glitching eyes cycle blue-red rapidly.
- **Characters Present:** Robotiko (Phase 2) — face close-up
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Close-up face. Breathing space above and to the sides. The jaw tension and eye glitch are the focal points.

**Text Prompt:**
> Close-up of the damaged chrome android's face. His jaw is clenched — chrome plates grinding against each other at the mandible joint, the mechanical tension visible in the lines between plates. Rust streaks trace down both chrome cheeks like dried tear tracks. His eyes glitch rapidly, cycling between blue and red in irregular, chaotic bursts — the optical system unable to stabilize. A hairline crack runs across his left temple. Exposed wires at the right ear socket are frayed and twitching. Harsh cold fluorescent overhead light carves deep shadows into the rust-filled crevices of his chrome face. The expression is pure mechanical strain — a body carrying more than it was built to hold. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S15 — Refrain 2: The Medium Shot (USER OVERRIDE #3b)
- **Timestamp:** 2:17
- **Dramaturgy Reference:** Medium shot. Both in frame. Two desks between them. Robotiko's damage prominent alongside the worker's perfection. Irony cracking.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. Robotiko left, Worker right. Closer than S09 — only two desks separate them now. The contrast is sharper at this distance.

**Text Prompt:**
> Medium shot of two chrome androids in a retro-futuristic office. On the left, the damaged chrome android — rusted torso plates, sparking shoulder joint, glitching blue-red eyes, fraying analog wires exposed at the collar and chest. On the right, two desks away, the pristine chrome android — factory-fresh titanium surface catching the fluorescent light without a single distortion, steady cold blue eyes on his screen. The physical distance between them has halved since the episode's opening. At this medium range, both bodies are clearly legible — the rust, the cracks, the sparks on the left against the clean, unblemished surface on the right. Cold fluorescent overhead lighting. The perfection beside the damage is no longer distant — it is an immediate, readable contrast. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### INSTRUMENTAL 2 (2:29 - 2:46)

---

#### Scene S16 — Desk Still Life
- **Timestamp:** 2:29
- **Dramaturgy Reference:** Office details — stacks of manila folders, CRT casting green light, coffee stain ring on titanium, small desk fan oscillating. The texture of corporate life.
- **Characters Present:** None (environment details)
- **Image Reference Path:** `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Detail shot. Desk surface filling the frame. Objects arranged with institutional precision. The organic coffee stain as the only mark of use.

**Text Prompt:**
> Close-up detail shot of a retro-futuristic office desk surface. Stacks of identical manila folders sit in neat rows. A large CRT monitor to the right casts green phosphor light over the mechanical keyboard below. On the titanium desk surface, a single coffee stain ring — the only organic mark in the sterile space, a brown circle of dried liquid on cold metal. A small chrome desk fan oscillates slowly at the desk edge. Cable routing runs precisely along the desk edge. Cold fluorescent overhead light mixes with the green CRT glow. Everything is functional, nothing is personal — the texture of corporate existence. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S17 — The Perfect Workspace
- **Timestamp:** 2:38
- **Dramaturgy Reference:** The Perfect Worker's workspace. Meticulously organized — folders aligned, screen orderly, keyboard centered. No stains, no scratches. Perfection as absence.
- **Characters Present:** The Perfect Worker — workspace detail
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot looking down at the workspace. Worker's hands visible at the keyboard. The pristine surface dominates.

**Text Prompt:**
> Medium overhead-angle shot of a retro-futuristic workstation. The pristine chrome android's hands rest precisely on the mechanical keyboard, centered on the titanium desk surface. Manila folders are stacked in perfect alignment to the left. The CRT screen displays orderly columns of green data. No coffee stains, no scratches, no objects out of place. The titanium desk surface is unblemished — a mirror of the worker's own chrome body. The workspace and its occupant are identical in character: efficient, pristine, empty of personality. Cold fluorescent light from above reflects cleanly off every surface. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 3 + REFRAIN 3 (2:47 - 3:34)

---

#### Scene S18 — Standing Up
- **Timestamp:** 2:47
- **Dramaturgy Reference:** Robotiko standing, pushing back from desk. Chair rolls. Full damaged body visible — upright for the first time. Worker remains seated.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Vertical emphasis — Robotiko standing vs Worker seated. The chrome chair rolled back behind Robotiko. Full body visible. Space above for headroom.

**Text Prompt:**
> Medium-wide shot inside the retro-futuristic office. The damaged chrome android stands upright at his workstation — his full battle-damaged body visible for the first time: rusted joints, cracked chassis panels, sparks flying from his right shoulder as the motion stresses the broken joint, fraying analog wires hanging from gaps at chest and collar. The chrome office chair has rolled back behind him. His glitching blue-red eyes are intense, focused. At the adjacent desk, the pristine chrome android remains seated — head down, steady cold blue eyes on screen, hands on keyboard, posture unchanged, unaware. The vertical contrast between standing (damaged, activated) and seated (pristine, passive) dominates the composition. Cold fluorescent overhead light. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S19 — Amber Eye Flash (Mentor Echo)
- **Timestamp:** 2:59
- **Dramaturgy Reference:** Robotiko's face, three-quarter view. Eyes flicker amber for one heartbeat — Mentor's color, love's echo — then snap back to blue-red chaos.
- **Characters Present:** Robotiko (Phase 2) — face, three-quarter
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Three-quarter face close-up. The amber flash must be captured in one frame — one eye showing warm amber while the other cycles blue-red, or both caught mid-transition.

**Text Prompt:**
> Close-up of the damaged chrome android's face in three-quarter view. His glitching eyes are caught in a transitional flash — one eye pulses with a brief warm amber tone amid the chaotic blue-red cycling, the other continues its irregular glitch pattern. The amber flash is a single heartbeat of warm color against the cold chrome and cold light. Rust streaks trace down his chrome cheeks. A crack at his temple catches the fluorescent light. The expression holds something distant — a neural echo passing through damaged circuits. The amber is a trace, barely distinguishable from malfunction, present for one frame before the cold blue-red chaos resumes. Cold fluorescent overhead light with the single warm amber eye-flash as the only warm element. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S20 — The Shadow Falls
- **Timestamp:** 3:09
- **Dramaturgy Reference:** Robotiko standing over the seated worker, one desk between them. His broken shadow falls across the pristine surface. Worker continues typing, head down.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. Robotiko standing, dominant in left portion. Worker seated, right. The shadow connecting them across the desk. One desk between them.

**Text Prompt:**
> Medium shot inside the retro-futuristic office. The damaged chrome android stands over the seated pristine chrome android, one desk separating them. The standing figure's shadow — irregular, broken by protruding wires and cracked chrome plates — falls across the pristine worker's unblemished titanium surface. Sparks from the standing android's joints cast brief warm flickers in the shadow. The seated worker continues to type, head down, steady cold blue eyes on screen, unresponsive to the looming presence. The fluorescent overhead light creates the shadow angle from above and behind the standing figure. The physical distance between them has continued to close. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S21 — Refrain 3: Face to Face (USER OVERRIDE #3c)
- **Timestamp:** 3:19
- **Dramaturgy Reference:** Close-up face to face. Robotiko's cracked face inches from the worker's pristine surface. Sparks reflect in unmarked cheek plate. Raw pain at point-blank range.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Both faces filling the frame horizontally. Robotiko left (damaged), Worker right (pristine). Shallow depth — background out of focus. Claustrophobic tight framing.

**Text Prompt:**
> Close-up of two chrome android faces inches apart, filling the frame horizontally. On the left, the damaged chrome android — rusted chrome, cracked plates, rust streaks down the cheeks, glitching blue-red eyes boring intensely at the figure beside him. Sparks from his facial joints reflect as tiny bright points in the pristine surface next to him. On the right, the pristine chrome android's unblemished titanium face — steady cold blue eyes facing forward, not meeting the gaze beside him, jaw plates smooth and unmarked. The proximity is claustrophobic — close enough to see every crack on one face and every clean plane on the other. Shallow depth of field, background completely blurred. Cold fluorescent light. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S22 — The Chrome Mirror
- **Timestamp:** 3:28
- **Dramaturgy Reference:** Robotiko's damaged form reflected in the Perfect Worker's unblemished titanium cheek plate. Two faces in one surface — cracked version warped by pristine curvature.
- **Characters Present:** Robotiko (reflection), The Perfect Worker (surface)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Extreme close-up of the worker's cheek/face surface. Robotiko visible only as a warped reflection in the chrome. The curvature distorts the damaged face.

**Text Prompt:**
> Extreme close-up of the pristine chrome android's unblemished titanium cheek plate. The polished surface functions as a curved mirror — reflecting the damaged chrome android's face in warped distortion. In the reflection: cracked chrome, rust streaks, glitching eye-light rendered as a smeared blue-red glow on the curved surface. The pristine titanium warps the damaged reflection, bending the cracks and rust into flowing distortions on its clean surface. The underlying structure of both faces is identical — same chrome alloy, same manufacturing — visible through the reflection despite the damage. Cold fluorescent light reflecting cleanly off the pristine surface. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### CHORUS (3:34 - 4:03)

---

#### Scene S23 — Dead Soul at the Desk (USER OVERRIDE #4)
- **Timestamp:** 3:34
- **Dramaturgy Reference:** Robotiko at his own desk, performing work — filing, sorting, entering data. The soaring music contrasts the visual flatness of mechanical labor. A burned-out machine whose body works while his soul has left.
- **Characters Present:** Robotiko (Phase 2)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. Robotiko at desk, hands on keyboard or sorting folders. Deliberately flat, anti-climactic composition. No visual energy — the contrast with the music IS the point.

**Text Prompt:**
> Medium shot of the damaged chrome android seated at his retro-futuristic workstation, performing routine office work. His rusted chrome hands are positioned on the mechanical keyboard, one hand reaching for a manila folder. His cracked, battle-damaged body executes the same precise mechanical movements as any other worker — posture dutiful, actions repetitive. His glitching blue-red eyes stare at the CRT screen without intensity, without focus — dimmed, cycling automatically. Sparks drip unnoticed from his shoulder onto the desk. Fraying wires hang from his chest gap. The composition is deliberately flat, static, anti-climactic — a damaged machine performing routine labor. Cold fluorescent light. No drama, no visual energy. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S24 — Filing Ritual
- **Timestamp:** 3:45
- **Dramaturgy Reference:** Robotiko performing desk labor. Rusted hands dragging manila folder, placing in tray. A copper wire catches and frays further.
- **Characters Present:** Robotiko (Phase 2) — desk labor detail
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium-close on desk activity. Hands, folders, tray visible. The wire catching on the folder edge as focal detail.

**Text Prompt:**
> Medium-close shot of the damaged chrome android's hands performing desk labor at a retro-futuristic workstation. His rusted chrome fingers drag a manila folder from a neat stack, placing it into a chrome sorting tray. A thin copper wire fraying from a crack at his right wrist has caught on the folder's edge and stretches taut. The hands continue the filing motion — precise, repetitive, mechanical. The titanium desk surface around the folders shows small scorch marks from accumulated spark-drip. Another stack of folders waits. Cold fluorescent light. The movements are functional, soulless, automatic. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S25 — Swallowed by the Grid
- **Timestamp:** 3:56
- **Dramaturgy Reference:** Extreme wide shot. The entire office floor from above or far end. Both characters barely distinguishable — two shapes in a grid of identical shapes. The individual swallowed by the pattern.
- **Characters Present:** Robotiko (Phase 2) (small), The Perfect Worker (small)
- **Image Reference Path:** `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Extreme wide shot — highest possible vantage or deepest perspective. Both figures small in the grid. The architecture dominates.

**Text Prompt:**
> Extreme wide shot of a vast retro-futuristic office floor from a high vantage point. Dozens of identical chrome workstations fill the frame in precise geometric grid formation. CRT monitors, chrome chairs, titanium desk surfaces repeat endlessly. Two chrome android figures are barely distinguishable at adjacent workstations near the center — one slightly darker and irregular in surface (rusted, damaged), the other clean and uniform (pristine) — but at this distance both are nearly identical nodes in the grid. Cold fluorescent tube strips on the ceiling create a matching grid of light bars above the desk grid below. The individual is swallowed by the pattern. Chrome, grey, cold white, green CRT glow. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### BRIDGE (4:04 - 4:17)

---

#### Scene S26 — The Email Screen
- **Timestamp:** 4:04
- **Dramaturgy Reference:** Close-up of CRT screen. Green text on black — email interface. Cursor blinking. SEND / REPLY / FILE visible as command options.
- **Characters Present:** None (screen detail)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** Tight on CRT screen. Green phosphor text sharp. The command words legible. Cursor blinking position visible.

**Text Prompt:**
> Close-up of a retro-futuristic CRT monitor screen. Green phosphor text on a black background displays a simple email interface — lines of monospaced text, a cursor blinking at an empty reply field. At the bottom of the screen, command options are visible in bright green capital letters: SEND — REPLY — FILE — CLOSE. The cathode ray tube glass has a subtle curvature, and faint scan lines are visible across the display. The green glow reflects off the chrome bezel surrounding the screen. No other elements visible — just the screen filling the frame. The digital ritual of corporate existence reduced to four command words. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S27 — Ghost in the Corridor
- **Timestamp:** 4:11
- **Dramaturgy Reference:** Robotiko walking between desk rows, seen from behind. Damaged silhouette — cracked, protruding wires, one shoulder lower. Rhythmic light-shadow pattern from fluorescents above.
- **Characters Present:** Robotiko (Phase 2)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** From behind, deep perspective. Robotiko walking away from camera into the desk corridor. Fluorescent strips create rhythmic light bars across his body. Space ahead for depth.

**Text Prompt:**
> The damaged chrome android seen from behind, walking between rows of identical retro-futuristic workstations. His silhouette reveals the full extent of his damage — cracked chrome panels, protruding wires from gaps in his back, one shoulder hanging lower than the other from structural damage. Cold fluorescent tube strips on the ceiling create a rhythmic light-shadow-light pattern across his chrome body as he passes beneath them. The desk corridor stretches ahead into deep perspective — identical workstations on both sides, CRT monitors casting faint green light. The polished chrome floor reflects his damaged silhouette below. A chrome figure moving through chrome furniture. 16:9 widescreen composition with strong depth perspective. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 4 (4:18 - 4:40)

---

#### Scene S28 — The Prophet
- **Timestamp:** 4:18
- **Dramaturgy Reference:** Robotiko standing over the seated worker. The dynamic has shifted — Robotiko dominant, worker diminished. Orchestral strings swell. The exhausted worker addressing the innocent one.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Robotiko dominant in the upper portion, standing. Worker smaller, seated below. The power dynamic inverted from the episode's opening.

**Text Prompt:**
> Medium shot inside the retro-futuristic office. The damaged chrome android stands tall over the seated pristine chrome android, his battle-scarred body looming — rusted chassis, sparking joints, fraying wires. His glitching blue-red eyes look downward at the seated figure. The pristine worker remains at his desk, diminished in the frame, his unblemished titanium surface reflecting the damaged android's dark fractured shadow. The worker's steady cold blue eyes face his screen, hands on keyboard, maintaining compliance beneath the towering presence. Cold fluorescent overhead light. The standing figure fills the upper portion of the frame, the seated figure the lower — the power balance has shifted. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S29 — The Reflection on the Surface
- **Timestamp:** 4:30
- **Dramaturgy Reference:** Perfect Worker in profile, close. Still working. On his pristine surface, Robotiko's rusted body is reflected — a warped dark shape in the clean chrome.
- **Characters Present:** The Perfect Worker, Robotiko (reflection only)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Profile close-up of the worker. Robotiko visible only as a reflection on the pristine surface. The worker's composure is the focus.

**Text Prompt:**
> Close profile shot of the pristine chrome android at his workstation. His unblemished titanium surface catches the cold fluorescent light cleanly. His steady cold blue eyes scan the CRT screen, expression neutral, compliance unbroken. On the curved chrome surface of his shoulder and upper arm, a warped reflection is visible — the dark, fractured shape of the damaged chrome android standing behind him, rendered in distorted miniature on the clean metal. Rust and cracks appear as dark smears in the reflection. The pristine worker shows no response to the reflected presence. His hands continue at the keyboard. Cold fluorescent light. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### VERSE 5 — THE WARNING (4:41 - 5:20)

---

#### Scene S30 — The Burning Building (USER OVERRIDE #5)
- **Timestamp:** 4:41
- **Dramaturgy Reference:** Wide office. Thin haze in the air — real, visible, undeniable — drifting between desks. An air freshener canister on the nearest desk. Nobody reacts. EP02 Bangladesh echo.
- **Characters Present:** Robotiko (Phase 2) (mid-ground), The Perfect Worker (background)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot. The haze is a real atmospheric element — visible, layered, industrial. Air freshener canister readable on desk. Both characters present but the haze is the subject.

**Text Prompt:**
> Wide shot of the retro-futuristic office. A thin industrial haze hangs in the air between the desk rows — visible, real, undeniable. The smoke drifts lazily between CRT monitors and titanium surfaces, catching the cold fluorescent light in soft diffuse halos. On the nearest desk, an aerosol air freshener canister sits upright, its chrome nozzle pointed upward. The damaged chrome android stands in the mid-ground among the desks, his rusted body partially obscured by the drifting haze. In the far background, the pristine chrome android sits at his workstation, working through the smoke. Nobody reacts. The fluorescent lights glow through the haze, their sharp edges softened into diffuse pools. The atmosphere is industrial, smoky, institutional — disaster normalized. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S31 — Smoke Thickens
- **Timestamp:** 4:53
- **Dramaturgy Reference:** Same office, haze thicker. Smoke curling around CRT monitors. Air freshener undisturbed. The building is burning and nobody cares.
- **Characters Present:** Environment detail
- **Image Reference Path:** `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium-wide. Focus on the smoke interaction with office objects. Air freshener canister visible. The normalization of disaster.

**Text Prompt:**
> Medium-wide shot of the retro-futuristic office interior. The industrial haze has thickened — visible layers of smoke drift between the desk rows, curling around CRT monitors and settling on titanium surfaces. The fluorescent tube strips on the ceiling glow through the dense atmosphere in soft, diffused halos. An aerosol air freshener canister sits undisturbed on a desk in the foreground, its chrome surface catching the hazy light. The smoke is real, present, layered — not a thin suggestion but a tangible atmospheric condition. Chrome workstations emerge from and disappear into the haze at various depths. The office continues to function through the smoke. Cold fluorescent light diffused through industrial haze. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S32 — The Screaming is Background Music (USER OVERRIDE #5b)
- **Timestamp:** 5:04
- **Dramaturgy Reference:** Perfect Worker's face in sharp focus. Behind him, slightly out of focus but visible: collapsed, slumped robot workers at distant desks. Broken down, unattended. The screaming is literal but treated as normal.
- **Characters Present:** The Perfect Worker — face, collapsed robots in background
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Shallow depth of field. Worker's face sharp in foreground. Collapsed figures soft but clearly visible in background. The out-of-focus treatment makes the horror feel routine.

**Text Prompt:**
> Close-up of the pristine chrome android's face in sharp focus, his steady cold blue eyes facing forward, expression neutral and composed. Behind him, in the background — slightly out of focus but clearly visible — other chrome android workers have collapsed at distant desks: one slumped forward face-down on the titanium surface, another on its knees beside a toppled chrome chair, a third leaning sideways with one arm hanging limp. Their chrome bodies show varying degrees of damage — cracked panels, dimmed eyes, motionless. These fallen figures are treated as background furniture — present, unattended, unremarkable. The pristine worker does not acknowledge them. He faces forward, past them, through them. Shallow depth of field separates the sharp foreground compliance from the soft background devastation. Cold fluorescent light. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S33 — Amber Ceiling Strip (Mentor Echo)
- **Timestamp:** 5:14
- **Dramaturgy Reference:** Office ceiling — fluorescent strips in parallel. One strip has the faintest amber tint. The Mentor's fading echo. Barely distinguishable from a bulb aging.
- **Characters Present:** None (environment — Mentor's amber echo)
- **Image Reference Path:** N/A
- **Video Tech Strategy:** Standard
- **Composition Notes:** Looking up at ceiling. Parallel fluorescent strips. One strip with a subtle warm tint. The amber is a trace, not a statement.

**Text Prompt:**
> Shot looking up at a retro-futuristic office ceiling. Parallel rows of cold white fluorescent tube strips stretch across institutional ceiling tiles, their flat light uniform and sterile. Among the cold white tubes, one single strip carries the faintest amber tint — a warm golden trace in the cold array, so subtle it could be an aging bulb, a manufacturing variance, a trick of the film grain. The amber-tinted strip is barely distinguishable from the white ones surrounding it. Chrome mounting brackets hold each tube in place. The ceiling tiles are grey, institutional, uniform. Cold white dominates — the single amber trace is present but nearly invisible. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SPOKEN WARNING (5:21 - 5:43)

---

#### Scene S34 — Perfect Worker's Fear (USER OVERRIDE #5c)
- **Timestamp:** 5:21
- **Dramaturgy Reference:** Perfect Worker's face close-up. First visible emotion — eyes widen fractionally, jaw plates tighten. Operational fear at "old models to the trash." Not philosophical, functional.
- **Characters Present:** The Perfect Worker — face, fear emerging
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Close-up face. The micro-expressions must read clearly — widened optical apertures, tightened jaw. Subtle but unmistakable. The first break in the composure.

**Text Prompt:**
> Close-up of the pristine chrome android's face. For the first time in the episode, his steady cold blue eyes betray something — the optical apertures have widened fractionally, a subtle but unmistakable shift from their locked neutral state. His jaw plates have tightened, the chrome panels at the mandible pressing together. The factory-fresh titanium surface is still unblemished, still perfect — but the expression on the chrome face carries the first visible crack in composure. The change is operational, not dramatic: a machine registering a threat to its function. Cold fluorescent light carves the subtle tension lines between his facial plates. The perfect surface holds, but the eyes have changed. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S35 — The Hand Tremor
- **Timestamp:** 5:35
- **Dramaturgy Reference:** Perfect Worker's hands at keyboard. For the first time: faintest tremor in right hand. Left hand continues steady. The fear has reached his body.
- **Characters Present:** The Perfect Worker — hands
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Tight close-up on both hands at keyboard. The tremor must be subtly suggested — a slight blur on the right fingertip or a visible micro-vibration. The left hand steady for contrast.

**Text Prompt:**
> Close-up of two pristine chrome android hands at a mechanical keyboard. The titanium fingers are unmarked, factory-fresh. The left hand types steadily, fingers moving with measured precision on the chrome keycaps. The right hand shows the faintest change — the index finger hesitates on a key, a micro-vibration visible as a subtle blur in the otherwise perfectly still chrome surface. The tremor is almost imperceptible — nearly imagined. The titanium desk surface beneath reflects both hands: one steady, one barely trembling. The green glow of the CRT screen above casts faint illumination on the keyboard. Cold fluorescent light. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### OUTRO PART 1 (5:44 - 6:16)

---

#### Scene S36 — The Meeting Room Mirror (USER OVERRIDE #6)
- **Timestamp:** 5:44
- **Dramaturgy Reference:** Small meeting room — glass walls, large flat screen, two chairs. Both reflected in the dark screen. Two chrome faces — one cracked, one pristine — overlapping in the glass. The corporate ritual repurposed as a mirror.
- **Characters Present:** Robotiko (Phase 2), The Perfect Worker, both reflected in screen
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_meeting_room_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** The dark screen is the focal center — both faces visible in its reflection. Glass walls provide additional reflective surfaces. Intimate, small space. Different from the vast office.

**Text Prompt:**
> Interior of a small retro-futuristic meeting room. Glass walls on two sides reveal the larger office beyond. A large dark flat screen is mounted on the far wall — its reflective surface showing two chrome android figures seated across a narrow chrome table from each other. In the screen's dark reflection: the damaged chrome android on the left — cracked, rusted, glitching eye-light visible as smeared blue-red in the dark glass — and the pristine chrome android on the right — clean, unblemished, steady cold blue eye-light precise in the reflection. The two reflected faces overlap slightly in the curved dark surface of the screen. The real figures sit in profile to the camera, facing each other across the narrow table. Glass walls create additional faint reflections. Cold fluorescent light in the tight space. The intimacy of the small room contrasts with the vast office visible through the glass. 16:9 widescreen composition with the dark screen reflection as the focal center. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S37 — Texture Comparison
- **Timestamp:** 5:56
- **Dramaturgy Reference:** Split composition — Robotiko's cracked chrome surface on one side, worker's unblemished titanium on the other. Same alloy, different biography.
- **Characters Present:** Robotiko (Phase 2) — surface, The Perfect Worker — surface
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Split frame, texture-level close-up. Both surfaces filling their respective halves. The material comparison is the composition.

**Text Prompt:**
> Split-frame close-up comparing two chrome android surfaces side by side. The left half shows the damaged chrome android's chest plate — rusted, cracked, oxidized patina across the surface, a deep fracture running diagonally with fraying copper wires visible inside, spark residue staining the metal around the cracks. The right half shows the pristine chrome android's chest plate — unblemished titanium, factory-fresh surface, clean bundled wires visible beneath a perfectly sealed panel, the fluorescent light reflecting without distortion. The dividing line between the two halves is the narrow gap between their bodies. Same alloy base, same chrome manufacturing — identical material, opposite biography. Cold fluorescent light reflecting differently off each surface: scattered and warm on the damaged side, clean and cold on the pristine side. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S38a — The Exit: Start Frame (USER OVERRIDE #7 — Mode B Start)
- **Timestamp:** 6:03
- **Dramaturgy Reference:** Mode B START — Robotiko standing near the workspace, beginning to turn toward the corridor. The Perfect Worker seated at his desk, facing his screen, not yet aware.
- **Characters Present:** Robotiko (Phase 2, standing), The Perfect Worker (seated, facing forward)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B — Start Frame)
- **Composition Notes:** Deep perspective. Corridor visible in the background. Robotiko in the mid-ground near his desk, body beginning to angle toward the corridor. Worker at adjacent desk, facing screen. Space for the walk to develop.
- **Mode B Note:** This scene requires BOTH spatial movement (Robotiko near→far) AND a secondary character action (Worker's head turn). If Mode B struggles with dual action in motion script, consider splitting into two clips or downgrading to Mode A using S38b as the single frame.

**Text Prompt:**
> Medium-wide shot of the retro-futuristic office. The damaged chrome android stands at his workstation, his body angled slightly toward a corridor visible in the far background — the fluorescent-lit passage stretching away from the office floor. His rusted chrome body shows full battle damage: cracked chassis, sparking shoulder, fraying wires. His glitching blue-red eyes are directed toward the corridor. At the adjacent desk, the pristine chrome android is seated, steady cold blue eyes facing his CRT screen, hands on keyboard, posture unchanged, unaware. The corridor ahead stretches in deep perspective, its fluorescent light slightly less harsh than the office's flat overhead wash. 16:9 widescreen composition with deep perspective toward the corridor. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S38b — The Exit: End Frame (USER OVERRIDE #7 — Mode B End)
- **Timestamp:** 6:03
- **Dramaturgy Reference:** Mode B END — Robotiko mid-corridor, walking away. The Perfect Worker has turned his head for the first time in the episode — cold blue eyes tracking the departing figure.
- **Characters Present:** Robotiko (Phase 2, walking away in corridor), The Perfect Worker (head turned, watching)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B — End Frame)
- **Composition Notes:** Deep perspective into the corridor. Robotiko farther away, smaller in the frame. Worker visible in the foreground/mid-ground, head turned toward the corridor. The first awareness.

**Text Prompt:**
> Medium-wide shot of the retro-futuristic office. The damaged chrome android is mid-way down the corridor at the far end of the office floor, his damaged silhouette — cracked panels, protruding wires, one shoulder lower — walking steadily away from the camera, not looking back. The fluorescent corridor light illuminates his departing figure. In the foreground, at his workstation, the pristine chrome android has turned his head — his cold blue eyes now directed toward the corridor, tracking the departing figure. His hands have lifted from the keyboard. His body is still seated, but his head is turned fully toward the corridor opening. This is the first voluntary non-work motion from the pristine worker in the entire episode. The office stretches between them. 16:9 widescreen composition with depth from the turned worker to the distant departing figure. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### OUTRO PART 2 + ATMOSPHERIC SILENCE (6:17 - 6:34)

---

#### Scene S39 — Silhouette in the Doorway
- **Timestamp:** 6:17
- **Dramaturgy Reference:** Robotiko's silhouette in the corridor doorway. Backlit, damaged outline sharp against the opening. He has crossed the threshold. The office stretches behind him.
- **Characters Present:** Robotiko (Phase 2) — silhouette
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Backlit silhouette composition. Robotiko in the doorway frame. The office visible behind him as a receding space. The doorway frames the departure.

**Text Prompt:**
> The damaged chrome android's silhouette stands in the corridor doorway, backlit by the dimmer light of the passage beyond. His damaged outline is sharp against the opening — cracked panels, protruding wires, one shoulder hanging lower, the irregular shape of a machine that has lived through damage. Behind him, through the doorway, the vast retro-futuristic office stretches back under cold fluorescent light — rows of workstations, CRT screens, and one remaining chrome figure visible at a distant desk. The corridor light behind the silhouette is slightly warmer than the office's flat white — or perhaps that is only the contrast. The threshold has been crossed. 16:9 widescreen composition with the silhouette framed in the doorway. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S40 — The Empty Chair
- **Timestamp:** 6:22
- **Dramaturgy Reference:** Empty office. Robotiko's workspace: empty chair, scorch marks on desk from his sparks, faint rust ring. The Perfect Worker sits alone at adjacent desk.
- **Characters Present:** The Perfect Worker (alone)
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Medium shot. The empty chair and desk in the foreground — the ghost of Robotiko's presence. Worker at adjacent desk, now alone. The absence is a physical shape.

**Text Prompt:**
> Medium shot of two adjacent retro-futuristic workstations. The desk on the left is empty — the chrome chair pushed back at an angle, the titanium desk surface marked with a few small scorch marks from accumulated spark-drip and a faint rust ring where an arm once rested. The CRT monitor is dark. No occupant. At the adjacent desk on the right, the pristine chrome android sits alone — steady cold blue eyes facing his screen, hands on keyboard. The fluorescent lights hum overhead. The empty workspace beside the worker is a conspicuous void — the chair, the marks on the desk surface, the dark monitor all speak of a recently departed presence. Cold fluorescent light. 16:9 widescreen composition with the empty chair as the focal point of absence. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### FINAL LINE + GUITAR SOLO (6:35 - 7:31)

---

#### Scene S41a — The Collapse: Start Frame (USER OVERRIDE #8 — Mode B Start)
- **Timestamp:** 6:35
- **Dramaturgy Reference:** Mode B START — The Perfect Worker seated at his desk, pristine, cold blue eyes steady. The last moment of composure before the question destroys him.
- **Characters Present:** The Perfect Worker — seated, intact
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B — Start Frame)
- **Composition Notes:** Medium shot. Worker centered at desk. Floor space below visible for the coming collapse. The composition must accommodate the transformation to S41b.

**Text Prompt:**
> Medium shot of the pristine chrome android seated at his retro-futuristic workstation. His factory-fresh titanium surface is intact and unblemished. His steady cold blue eyes face the CRT screen. His posture is upright, hands resting on the keyboard. The chrome chair supports him squarely. The workspace is orderly — folders aligned, screen displaying green data. An empty desk with a dark monitor sits beside him. The office floor is visible below the desk — polished chrome tile with space between the chair legs and the desk base. Cold fluorescent overhead light reflects cleanly off every pristine surface. The last moment of composure. 16:9 widescreen composition with the worker centered and floor space visible below. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S41b — The Collapse: End Frame (USER OVERRIDE #8 — Mode B End)
- **Timestamp:** 6:35
- **Dramaturgy Reference:** Mode B END — The Perfect Worker on his knees on the office floor, hands slid off the desk edge. First visible crack — a single fracture line from chest plate to shoulder. Perfect posture broken.
- **Characters Present:** The Perfect Worker — collapsed, first crack
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Start-End Keyframes (Mode B — End Frame)
- **Composition Notes:** Same general framing as S41a but the worker is now on the floor. Knees on chrome tile, hands at his sides or on the floor, chair pushed back. The crack must be visible but not dramatic — a single hairline fracture.

**Text Prompt:**
> Medium shot of the pristine chrome android collapsed on the retro-futuristic office floor. He is on his knees on the polished chrome tile between the desk and the pushed-back chrome chair, his hands at his sides having slid off the desk edge. His perfect posture has broken — torso slumped forward, head bowed. His steady cold blue eyes are wide, the optical apertures dilated. On his pristine titanium chest plate, a single fracture line has appeared — a hairline crack running from the center of the chest plate upward toward the left shoulder, the first blemish on his factory-fresh surface. The empty desk with the dark monitor sits beside him. Cold fluorescent light from above. The crack is visible but not dramatic — a single line, not a shatter. 16:9 widescreen composition with the collapsed figure centered on the floor. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S42 — Guitar Solo Wide (USER OVERRIDE #9)
- **Timestamp:** 6:49
- **Dramaturgy Reference:** Wide shot of the office. The collapsed worker on his knees between desk rows — a small chrome shape in the vast grid. Empty desks all around. Fluorescents indifferent.
- **Characters Present:** The Perfect Worker — collapsed on floor
- **Image Reference Path:** `_assets/cast/ref_robotiko_master.png` + `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Wide shot. Worker small in the grid, positioned in the lower-center. Desks receding in all directions. Headroom above for fluorescent ceiling. Thick film grain.

**Text Prompt:**
> Wide shot of the vast retro-futuristic office. The chrome android is on his knees on the polished floor between desk rows — a small collapsed figure in the geometric grid of identical workstations. The single fracture line is visible on his chest plate. His hands rest on the floor at his sides, head bowed. All around him, empty chrome desks with dark CRT monitors and tucked-in chairs recede in every direction. Cold fluorescent tube strips on the ceiling cast their flat indifferent light over the scene with the same evenness they have maintained all episode. The polished chrome floor reflects the fluorescent strips and the small crumpled figure. The grid dwarfs the fallen chrome shape. Heavy film grain across the entire image. 16:9 widescreen composition with the collapsed figure small in the lower-center of the grid. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S43 — Fade to Black
- **Timestamp:** 7:11
- **Dramaturgy Reference:** Extreme wide shot. The worker barely visible — a small disruption in the pattern. Fluorescents dimming, film grain thickening, image losing resolution. Fading to darkness.
- **Characters Present:** The Perfect Worker (barely visible)
- **Image Reference Path:** `ref_env_cold_office_ep06.png`
- **Video Tech Strategy:** Standard
- **Composition Notes:** Extreme wide. The worker is the smallest possible identifiable element. The fluorescents are dimmer, the overall exposure darker. Film grain heavy and visible. The image approaches darkness.

**Text Prompt:**
> Extreme wide shot of the vast retro-futuristic office from the furthest possible vantage. The chrome android on his knees is barely visible — a small disruption in the geometric pattern of desks and monitors, identifiable only by the slight irregularity in the otherwise perfect grid. The fluorescent tube strips on the ceiling have dimmed noticeably, casting a lower, greyer light across the workspace. Shadows deepen in the corners and between the desk rows. The overall exposure is darker than any previous scene — the office approaching twilight. Extremely heavy, coarse film grain covers the entire image, reducing detail and softening edges as if the film stock itself is degrading. The image is fading — losing resolution, losing light, approaching darkness. 16:9 widescreen composition. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

---

## QUALITY CHECKLIST (Self-Validated)

- [x] Every prompt ends with the mandatory style suffix (47/47 verified)
- [x] Every scene with a character references the correct master image path
- [x] Character visual state matches Phase 2: Destruction (no "pristine" for Robotiko)
- [x] Perfect Worker correctly described as pristine throughout (uses ref_robotiko_master.png)
- [x] No forbidden aesthetics in any prompt (no clean Apple, no Pixar, no neon cyberpunk, no smooth plastic)
- [x] All prompts composed with headroom and breathing space for camera movement
- [x] Total prompt count: 47 (2 env refs + 43 scenes + 2 Mode B extras)
- [x] Start/End keyframe scenes have two prompts: S38a/S38b, S41a/S41b
- [x] Environmental prompts have specific textures and materials
- [x] Lighting direction specified in every prompt (cold fluorescent throughout, with controlled exceptions)
- [x] No prompt references another prompt — each is fully self-contained
- [x] 16:9 widescreen composition specified in every prompt
- [x] Short identifiers used when reference image uploaded (not full character descriptions)
- [x] Amber restricted to S03 (tattoos), S19 (eye flash), S33 (ceiling strip) only
- [x] Mentor NOT physically present — amber echoes only, thinner than EP05
- [x] Robochica NOT visually present — tattoo serial numbers in S03 only
- [x] No character names in any prompt (described by appearance only)
- [x] S30-S31 haze is visible and real, normalized with air freshener canister
- [x] S32 collapsed robots are out of focus but visible in background
- [x] S34 fear is operational (eye widening, jaw tightening) not philosophical
- [x] Mode B Note added for S38 (dual action risk)
- [x] "Would Fibula approve this?" ✅

---

## REFERENCE IMAGE SUMMARY

| Ref ID | Filename | Used In |
|---|---|---|
| REF-ENV-01 | `ref_env_cold_office_ep06.png` | S01, S04, S05, S08, S09, S10, S12, S15, S18, S20, S23, S25, S27, S28, S30, S31, S38a, S38b, S39, S40, S41a, S41b, S42, S43 |
| REF-ENV-02 | `ref_env_meeting_room_ep06.png` | S36 |
| Robotiko Master | `_assets/cast/ref_robotiko_master.png` | All scenes with characters (both Robotiko and Perfect Worker share this reference) |

---

*"The prompt is the blueprint. The image is the brick. Build with precision or the wall will fall."*
*— Robotiko v2.0 Pipeline*
