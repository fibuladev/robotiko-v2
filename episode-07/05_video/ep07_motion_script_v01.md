# EP07 — MOTION SCRIPT
> **Version:** v01 | **Skill:** `_skills/robotiko-motion-script/SKILL.md` (v2.0)
> **Generated:** 2026-05-31 | **Model:** Opus 4.6 + Extended Thinking
> **Dramaturgy:** v01 — APPROVED (2026-05-30)
> **Visual Prompts:** v01 — Images generated (S01-S25 in raw/)

---

## PRE-GENERATION CHECKLIST

- [x] `episode-07/03_direction/ep07_dramaturgy_v01.md` → APPROVED, 29 scenes, 11 overrides
- [x] `episode-07/04_visuals/raw/` → Images 1.png–25.png confirmed (S01-S25). S26-S29 pending.
- [x] `episode-07/02_music/ep07_musical_metadata.json` → 25 sections, 439s, 73 BPM, E Minor
- [x] `_management/master.md` → Station 5: The Surrendering Self (The Dark Night)
- [x] `_templates/video_prompt_template.md` → Output structure confirmed
- [x] `_assets/cast/character_profiles.json` → Phase 2: Destruction (FINAL). @Damaged Element.

> ✅ All 29 scene images generated (S01-S29). S29 reuses 28.png.
> ⚠️ Motion script must be approved by human before any video generation begins.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP07 |
| **Title** | The Silence Protocol |
| **Station** | The Surrendering Self (The Dark Night — chosen surrender begins) |
| **Camera Personality** | THE RETREATING CAMERA |
| **Dominant Energy** | Desolate / minimal — lowest MS average of the series (~2.8) |
| **Total Shots** | 29 (matches dramaturgy) |
| **Total Clips** | 49 (including multi-clip sub-clips) |
| **Total Duration** | 7:19 (439s) |

---

## ELEMENT REGISTRY

| Element Name | Description | Reference Images | Episodes Active |
|---|---|---|---|
| **@Damaged** | Robotiko Phase 2 FINAL state — rusted/cracked chrome chassis, sparks from joints, glitching blue-red eyes, exposed fraying analog wires, missing right ear (shrapnel scar), torso dent, shoulder scratches, robochica_1-4 inner-forearm tattoos. "Barely holding together." | `android_damaged.png`, `android_damaged_2.png`, `android_damaged_3.png` | EP07 (first test) |

> **EP07 = first Element test of the series.** Single Element only (@Damaged). Track cost per clip for the Omni References decision.
> **Angles 2.0:** Generate 12 angle variations from `android_damaged.png` master ref. Review and reject any that show incorrect damage state or eye rendering.

---

## VIDEO STRATEGY REFERENCE

| Mode | When to Use | Input | Duration |
|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, no transformation | 1 image | 5s or 10s |
| **B — Start/End Keyframes** | Transformations, morphing, character state changes | 2 images | 5s or 10s |

> **EP07: All 49 clips are Mode A (Standard).** No transformations, no morphing — this episode is about stillness, retreat, and a single decisive act. No Mode B needed.

**Duration Coverage Strategy:**

| Scene Duration | Strategy | Clip Count |
|---|---|---|
| ≤ 5s | Direct | 1 × 5s |
| 6–10s | Direct | 1 × 10s (trim in CapCut) |
| 11–15s | Speed Ramp | 1 × 10s (slowdown ≤ 1.5×) |
| 16–30s | Multi-Clip | ⌈duration / 10⌉ × 10s |
| 30s+ | Multi-Clip | ⌈duration / 10⌉ × 10s |

---

## TOOL ASSIGNMENT SUMMARY

### Tool Distribution

| Tool | Clips | % | Assignment Logic |
|---|---|---|---|
| **Kling 3.0** | 47 | 95.9% | All @Damaged Element clips + env clips with camera movement |
| **Kling 2.5 Turbo** | 2 | 4.1% | Static env-only clips (no Element, no camera move) |
| **Seedance 1.0** | 0 | 0% | Not used — Element requirement overrides budget optimization |
| **Veo** | 0 | 0% | Not used |
| **TOTAL** | **49** | 100% | — |

> **Why 96% Kling 3.0?** EP07 = first @Damaged Element test. Every Robotiko clip requires the Element tag → Kling 3.0 mandatory. Only 2 env-only clips (S04b, S12) are truly static with no character → Kling 2.5 Turbo.

### Assignment Rules Applied

1. **Element-tagged shots → Kling 3.0 only** (42 character clips)
2. **Camera movement shots → Kling 3.0** (5 env clips with Zoom/Pan)
3. **Static + no Element → Kling 2.5 Turbo** (2 clips: S04b, S12)
4. **OmniEdit reserve: 15%** of Kling 3.0 credits for post-generation fixes

### Clips by Tool

**Kling 3.0 (47):** S01, S02a-c, S03, S04a, S05a-c, S06, S07, S08, S09, S10a-d, S11, S13a-b, S14, S15, S16, S17, S18, S19a-b, S20, S21, S22a-c, S23a-c, S24a-b, S25, S26, S27, S28a-d, S29a-c

**Kling 2.5 Turbo (2):** S04b, S12

### OmniEdit Priority Scenes

| Priority | Scene | Reason |
|---|---|---|
| HIGH | S27 | The single amber ember — make-or-break beat |
| HIGH | S07, S08, S19 | Eye-projection — spawn risk from projected figures |
| MEDIUM | S05, S16, S17 | Crowd scenes — spawn/duplication risk |
| MEDIUM | S22 | Still Hold — grain/atmosphere must be perfect |
| LOW | S01, S04, S09, S12, S18 | Env-only — easiest to fix |

---

## MOTION SCRIPT

---

### SHOT S01 — The Aftermath (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:00–0:12 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | Melancholic grand piano solo over rain ambience; acoustic guitar enters. Minimal energy — the aftermath. |
| **Scene Context** | Vast still water at twilight, fog, wet stone. Character absent — Architecture Cage establishing. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None (no character) |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — camera movement requires K3.0 |
| **Speed Ramp** | 0.83× (10s → 12s) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/1.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> A vast still expanse of dark water under a twilight sky. Low fog drifts slowly across the water's surface, faint ripples catch cold light. Wet stone embankment glistens. Atmospheric breathing - fog moves, water ripples, nothing else. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S02 — Waterside Bench, Seated (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 0:12–0:34 |
| **Scene Duration** | 22s |
| **Coverage** | Multi-Clip — 3 × 10s = 30s (trim to 22s in CapCut) |
| **Musical Moment** | Minimalist piano, low energy. Spoken word: "I calculated the orbits… map the infinite." The fall from arrogance. |
| **Scene Context** | Robotiko seated on wet bench, hunched, looking over water. Stars emerge. Cracked reflection on wet stone. |

#### Clip A — S02a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/2.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android sits motionless on a wet bench at the water's edge, hunched, looking out over dark water. Fog drifts at knee level. His cracked reflection trembles in standing water beside the bench. Subtle atmospheric breathing only - fog moves, water ripples. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S02b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | ← S02a (last frame) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/2.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android on the wet bench, the frame slowly retreating. Fog drifts across the water, cold twilight sky above. The figure grows smaller as the world expands around him. Wet stone glistens. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S02c

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/2.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Closing slowly on the wet stone beside the bench where the @Damaged chrome android's cracked reflection lies broken in the standing water. Fog drifts gently. The reflection trembles with subtle water movement. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S03 — The Rise (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:34–0:47 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | "But now… hiding inside empty pockets… a fist of shame." The triumph drains. |
| **Scene Context** | Override 1: Front/three-quarter, rises from bench. Shoulders fold, head drops, hands in pockets. Camera dollies out ahead. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Speed Ramp** | 0.77× (10s → 13s) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/3.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android walks slumped along a wet stone embankment at twilight, seen from the front three-quarter angle. Head bowed, shoulders folded, hands hidden in pockets. The camera retreats ahead of him - he walks toward the camera as it pulls back. Fog surrounds, wet pavement glistens. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S04 — Indifferent Flow: Wet Street (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 0:47–1:04 |
| **Scene Duration** | 17s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim to 17s) |
| **Musical Moment** | Piano interlude, slow and sad. First designed silence — the world without him. |
| **Scene Context** | INDIFFERENT FLOW. Wet night street, crowd flows past an empty space. Character absent. |

#### Clip A — S04a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/4.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> A wet city street at dusk. Blurred impressionistic silhouettes of mixed pedestrians flow past - a slow horizontal scan of the world moving through a cold night street. Wet asphalt reflects streetlight. Fog hangs low. No clear subject - the world flows past an empty space. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S04b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Recommended Tool** | Kling 2.5 Turbo (Standard, 1080p) — static, no Element |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/4.png`

**Camera Move:** Static

**Motion Prompt:**
> A wet city street at dusk, camera still. Blurred silhouettes of mixed pedestrians drift slowly past. Wet asphalt pools reflect cold streetlight. Fog breathes. The composition holds on the empty center - the conspicuous absence. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S05 — Walking Through Indifference (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 1:04–1:27 |
| **Scene Duration** | 23s |
| **Coverage** | Multi-Clip — 3 × 10s = 30s (trim to 23s) |
| **Musical Moment** | Heavy bass enters, bitter spoken word. "November is for lovers… no code for Hunger." Medium-low energy. |
| **Scene Context** | Override 2: Walking, low charge — dimming eyes, faltering step. Passes warm shopfront glow he cannot draw from. |

#### Clip A — S05a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/5.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android walks a cold wet street at dusk, hands in pockets, head low, step faltering. Camera retreats ahead of him. Blurred human pedestrians cross the foreground. Warm shopfront glow pools on wet asphalt around him but he stays in the cold. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S05b

> **HUMAN OVERRIDE (2026-06-07):** Frame chain applied. Original prompt (Pan Left from 5.png) caused replay effect — character reset to starting position. Revised: start from S05a's extracted last frame, Dolly Out to widen.

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | ← S05a (last frame) |

**Assets Required:**
- **Start Frame:** Extracted last frame of S05a

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android continues walking forward on the wet street. The camera retreats steadily ahead of him, the frame widening as he grows smaller against the opening street. Fog drifts, wet asphalt reflections stretch. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S05c

> **HUMAN OVERRIDE (2026-06-07):** Frame chain applied. Start from S05b's extracted last frame. Prompt revised to match medium-wide starting composition from chained S05b.

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | ← S05b (last frame) |

**Assets Required:**
- **Start Frame:** Extracted last frame of S05b

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> From a medium-wide composition, the camera closes slowly on the @Damaged chrome android's face and upper body as he walks the wet street. His optical lenses dim and weaken, barely flickering blue-red - low charge. Cold dusk surrounds him, warm shopfront glow pooling on the wet pavement behind. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S06 — Self-Revulsion at the Water (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 1:27–1:40 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Music rising. Disgusted whisper: "gray air… vomit its own rust." Medium energy. |
| **Scene Context** | Override 3: Tighter on Robotiko — rusted hand lifted, fog-breath, cracked reflection in black water. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Speed Ramp** | 0.77× (10s → 13s) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/6.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Medium-close on the @Damaged chrome android's rusted hand lifted into damp grey air. Rust beads with moisture on corroded chrome, exposed copper wires fray. Faint fog-breath ghosts from chassis vents. Below, a cracked reflection trembles in black water. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S07 — Eye-Projection: Social Feed (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:40–1:49 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s) |
| **Musical Moment** | Chaotic background, no beat. "Dive into the noise / data stream." Medium energy. |
| **Scene Context** | Override 4: Cold blue-white beam from eyes materializes faceless data stream in fog. COLD projection, never amber. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/7.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android seated on a bench in darkness. A cold blue-white light beam from his optical lenses projects abstract flickering shapes into the damp fog - faceless, restless, scrolling. The projected light illuminates the fog, casting harsh cold glow on his damaged chrome. Fog drifts through the projected shapes. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S08 — Refrain 1: "Billions of Users" / Distance Ladder Rung 1 (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:49–1:56 |
| **Scene Duration** | 7s |
| **Coverage** | Direct — 1 × 10s (trim 3s) |
| **Musical Moment** | High-pitch vocal refrain — "Billions of users… Here. But you… are NOT." Medium-high energy. RETREATING CAMERA begins. |
| **Scene Context** | Override 6: Projected feed swells. Robotiko small beneath. Distance ladder — rung 1. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/8.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android sits small beneath a massive wall of cold blue-white projected light - abstract flickering shapes filling the upper frame. The camera retreats steadily, the figure shrinking against the immensity of the cold projected feed. Dark waterside, fog. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S09 — Indifferent Flow: Feed Noise (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:56–2:02 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s) |
| **Musical Moment** | Piano interlude, slow and sad. Designed silence — character absent. |
| **Scene Context** | INDIFFERENT FLOW. Feed/screens continue alone. Cold imagery, no figure. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — camera movement |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/9.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Abstract cold blue-white imagery churning across the frame - scrolling light fragments, flickering digital shapes. No figure, no warmth, no subject. The visual noise slowly recedes and dissolves, the cold glow fading. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S10 — The Plugged-In Room / The Routine (Multi-Clip: 4 clips)

| Field | Value |
|---|---|
| **Timestamp** | 2:02–2:36 |
| **Scene Duration** | 34s |
| **Coverage** | Multi-Clip — 4 × 10s = 40s (trim to 34s) |
| **Musical Moment** | Spoken word over ticking-clock rhythm. "Doing nothing costs so much energy… Refresh… Application Rejected." Medium-low energy. |
| **Scene Context** | Override 5: Home room, plugged into wall. Ticking clock, CRT rejection text, cold screen-glow. The tether motif planted. |

#### Clip A — S10a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/10.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android sits motionless at a desk before a CRT monitor in a cramped dark room. A cable plugs from the wall into his chassis. Cold blue-white screen glow washes his rusted body. Atmospheric breathing only - the screen flickers subtly, dust motes drift. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S10b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/10.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Closing slowly on the CRT screen and the @Damaged chrome android's face washed in cold blue-white glow. The screen displays rejection text. His optical lenses flicker faintly blue-red, reflecting the cold light. Motionless except for the screen glow breathing. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S10c

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/10.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> A slow horizontal scan of the cramped room - from the wall clock ticking to the CRT screen glowing cold to the cable running from wall socket into the @Damaged chrome android's chassis. Cold blue-white light, deep shadows. The room breathes with subtle dust and screen flicker. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip D — S10d

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | Start of Chain 1 |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/10.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The camera retreats from the @Damaged chrome android at the desk, revealing the full cramped room - bed, dark window, wall clock, the cable running to the wall. Cold CRT glow is the only light. The figure grows smaller as the room's geometry frames him like a cage. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S11 — Refrain 2: "Rejection Emails" / Distance Ladder Rung 2 (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:36–2:45 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s) |
| **Musical Moment** | High-pitch vocal refrain — "Rejection emails… Here. But you… are NOT." Medium-high energy. |
| **Scene Context** | Override 6: Same room, wider. Robotiko hunched and small at desk. Distance ladder rung 2. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | ← S10d (last frame) — Chain 1 |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/11.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> Wide shot of the dark room from the doorway. The @Damaged chrome android hunched small at the desk in the corner, the CRT screen glowing cold. The camera retreats further, the figure shrinking into the room's dark geometry. Deep shadows swallow him. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S12 — Indifferent Flow: Empty Transit (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 2:45–2:58 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Piano interlude, slow and sad. Designed silence — character absent. |
| **Scene Context** | INDIFFERENT FLOW. Empty transit platform, wet asphalt, traffic light cycling. No one waits. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 2.5 Turbo (Standard, 1080p) — static, no Element |
| **Speed Ramp** | 0.77× (10s → 13s) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/ep07_ref_env_transit.png`

**Camera Move:** Static

**Motion Prompt:**
> An empty bus stop bench under a flickering cold fluorescent lamp at dusk. Wet asphalt stretches in all directions. A traffic light cycles slowly in the background, its colored glow catching on wet surfaces. No figures. Atmospheric breathing - lamp buzzes, rain puddles shimmer. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S13 — The Predator: Hope Chirps (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 2:58–3:15 |
| **Scene Duration** | 17s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim to 17s) |
| **Musical Moment** | Melancholic spoken word over fuzz guitar. "Playing deaf… chirping like birds… a spark of hope." Medium energy. |
| **Scene Context** | Bus stop at dusk. Receiver chirps — a spark of hope (not amber). Eyes flicker toward something good. |

#### Clip A — S13a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/13.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The @Damaged chrome android sits on a wet bench under a flickering cold lamp at dusk. His head lifts slightly, optical lenses flickering with a faint spark - a momentary lift, not warmth. The camera closes slowly. Cold wet street surrounds, no shelter. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S13b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | Start of Chain 2 |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/13.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android holds still on the bench under the buzzing lamp. Attentive, head slightly raised. Cold wet asphalt around, the lone lamp casting hard shadows. Atmospheric breathing - lamp flickers, wet surfaces shimmer. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **RETAKE (2026-06-07):** Re-generated via Kling 3.0 Omni. Prompt unchanged.

---

### SHOT S14 — The Predator: Held Silence (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 3:15–3:30 |
| **Scene Duration** | 15s |
| **Coverage** | Speed Ramp — 1 × 10s → 15s at 0.67× |
| **Musical Moment** | [3-SECOND HELD SILENCE] → cold synthetic voice: "Your payment is past due." The hope collapses. |
| **Scene Context** | Override 8: HELD SILENCE — frozen mid-gesture. Motionless beat. No movement. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Speed Ramp** | 0.67× (10s → 15s) |
| **Frame Chain** | ← S13b (last frame) — Chain 2 |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/14.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android frozen rigid on the bench under the buzzing lamp. Shoulders dropped, head down. A still, frozen composition - barely perceptible lamp buzz and the faintest fog drift are the only motion. Everything else is held, motionless. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **RETAKE (2026-06-07):** Re-generated via Kling 3.0 Omni. Prompt unchanged.

---

### SHOT S15 — Refrain 3: "Creditors" / Distance Ladder Rung 3 (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 3:30–3:44 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | High-pitch vocal refrain — "Creditors… Here. But you… are NOT." Medium-high energy. |
| **Scene Context** | Override 6: Wide shot. Small figure on bench under lamp. Empty transit space. Distance ladder rung 3. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Speed Ramp** | 0.71× (10s → 14s) |
| **Frame Chain** | ← S14 (last frame) — Chain 2 (end) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/15.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> Wide shot. The @Damaged chrome android small on the wet bench under a lone flickering lamp, the empty transit space opening wide around him. The camera retreats steadily - the figure and the lamp shrinking as wet asphalt stretches in all directions. Cold, desolate, exposed. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S16 — The Glittering Avenue (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:44–3:53 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s) |
| **Musical Moment** | Deep spoken word — "Glittering Avenue." Medium-low energy. |
| **Scene Context** | Override 7-context: Consumer avenue at evening. Cold screens, wet shop windows, river of faces. Robotiko enters tiny. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/16.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> A bustling commercial avenue at evening - cold screens blazing, wet reflective floors, dense crowd of mixed pedestrians flowing. The @Damaged chrome android enters small and dark among the polished crowd. The frame slowly widens to reveal the immensity of the avenue dwarfing him. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S17 — Refrain 4: "Thousands of Faces" / Distance Ladder Rung 4 (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 3:53–4:04 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | High-pitch vocal refrain — "Thousands of faces… Here. But you… are NOT." Medium-high energy. Distance ladder rung 4 — widest physical distance. |
| **Scene Context** | Override 6: Crowd swells. Thousands stream around him. Cracked reflection in wet shop glass. The smallest, stillest thing. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — camera movement |
| **Speed Ramp** | 0.91× (10s → 11s) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/17.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> A vast commercial avenue at evening. Towering cold screens blaze on both sides, wet reflective floors stretching deep. Blurred dark silhouettes drift through the space like shadows - no clear faces, no distinct figures. The camera closes slowly. Cold screen-glow washes over wet surfaces. Fog hangs between buildings. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **HUMAN OVERRIDE (2026-06-07):** Original prompt used "pedestrians" + @Damaged Element + Dolly Out. Triple problem: (1) Element forced android too prominent for very-wide-shot intent, (2) "pedestrians" triggered realistic human generation when source image has blurry dark silhouettes, (3) Dolly Out fabricated content beyond frame edges. Fix: removed Element, rewrote prompt to match source image (blurred silhouettes, no android reference), changed camera to Slow Zoom In.

---

### SHOT S18 — Indifferent Flow: The Avenue Continues (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:04–4:10 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s) |
| **Musical Moment** | Piano interlude, slow and sad. Brief Indifferent Flow before the corruption verse. |
| **Scene Context** | INDIFFERENT FLOW. Avenue's screens and crowd continue alone. No protagonist. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — camera movement |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/ep07_ref_env_avenue.png`

**Camera Move:** Pan Left

**Motion Prompt:**
> The commercial avenue at evening - cold screens blazing, wet floors reflecting. A dense river of blurred pedestrian silhouettes (mixed men and women) flows through the frame. No clear subject. A slow horizontal scan of the indifferent machine running on its own. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S19 — The Corruption: Broadcast (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 4:10–4:26 |
| **Scene Duration** | 16s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim to 16s) |
| **Musical Moment** | Angry spoken word building. "System Lords… wiping blood… accepting peace awards." Medium energy. |
| **Scene Context** | Override 4: Home room, night. Lying on bed. Cold blue-white eye-projection of corrupt broadcast onto wall/ceiling. |

#### Clip A — S19a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | None |

> **PRODUCTION NOTE:** Image adjusted — Robotiko stands front-facing with wall projection (not supine on bed). Stronger confrontation with the broadcast.

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/19.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android standing in a dark room at night, front-facing. A cold blue-white beam from his head projects broadcast imagery onto the wall behind him - silhouettes at a podium, raised hands. The projected cold light flickers over his damaged chrome. Fog-like haze drifts. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S19b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/19.png`

**Camera Move:** Tilt Down

**Motion Prompt:**
> Subtle downward tilt from the cold blue-white broadcast projection on the wall toward the @Damaged chrome android standing below it, strictly within the existing frame composition. The projected cold light shifts across his damaged chrome body. Do not reveal new elements above or below the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S20 — The Corruption: Held Silence (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:26–4:32 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s) |
| **Musical Moment** | [3-SECOND HELD SILENCE] after "peace awards" → "Fake heroes… Fake victories." |
| **Scene Context** | Override 8: HELD SILENCE — broadcast frozen on wall. Robotiko motionless beneath. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/20.png`

> **PRODUCTION NOTE:** Image adjusted — Robotiko standing with frozen wall projection (matching S19 adjustment).

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android standing motionless in the dark room. Broadcast projection frozen on the wall behind him - a still cold image of a single figure with raised arm. Barely perceptible atmospheric breathing - the faintest flicker of projected light. A held, frozen composition. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S21 — Refrain 5: "The Fake Truth" / Distance Ladder Rung 5 (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:32–4:42 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | High-pitch vocal refrain (peak) — "The Fake Truth… Here. But You… Are NOT." HIGH energy. Distance ladder rung 5 — peak isolation. |
| **Scene Context** | Override 6: High angle, looking down. Tiny figure on bed in corner of dark room. Cold broadcast light. The most distant, most isolated frame. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/21.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> High-angle shot looking down into the dark room. The @Damaged chrome android a small rusted shape on the bed in the corner. Cold blue-white broadcast light washing over him from above. The frame slowly widens - the figure grows even tinier, swallowed by the room's dark geometry. Desk, chair, clock visible from above. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S22 — The Chorus Cry: Still Hold (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 4:42–5:07 |
| **Scene Duration** | 25s |
| **Coverage** | Multi-Clip — 3 × 10s = 30s (trim to 25s) |
| **Musical Moment** | EMOTIONAL PEAK. "Where is that amber gaze?… the fist to pierce through this fog?" HIGH energy. **STILL HOLD** at summit. Heaviest grain (Grain Crescendo). |
| **Scene Context** | Override 9: Balcony, deep night, fog. Raises fist toward fog — fog swallows the gesture. Amber named but ABSENT. |

#### Clip A — S22a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/22.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The @Damaged chrome android at a balcony railing at deep night, thick fog around him. One arm rises, fist reaching into the fog. The camera closes slowly toward the gesture. Cold grey-blue deep night, heavy fog, desaturated Kodachrome. Extremely heavy, visible film grain. No warm light, no amber. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S22b — **STILL HOLD**

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/22.png`

**Camera Move:** Static

**Motion Prompt:**
> **STILL HOLD.** The @Damaged chrome android at the balcony railing, arm half-raised, fist held into the fog. The fog wraps around the gesture, undisturbed - nothing parts, nothing answers. Near-total stillness. Only the faintest fog drift. Extremely heavy, visible film grain. Cold grey-blue deep night, no amber. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S22c

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | Start of Chain 3 |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/22.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android at the balcony, arm lowering in defeat. The camera retreats slowly, the figure shrinking against the foggy void. Cold grey-blue deep night, heavy fog, desaturated Kodachrome. The gesture has failed. Fog drifts. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S23 — The Speck on the Tower (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 5:07–5:34 |
| **Scene Duration** | 27s |
| **Coverage** | Multi-Clip — 3 × 10s = 30s (trim to 27s) |
| **Musical Moment** | Fuzz guitar solo crying high notes → feedback → silence. High→fading energy. The "bottoming out." |
| **Scene Context** | Absolute farthest camera of the episode. Small figure on balcony of dark tower, foggy dead city below. Drains to silence. |

#### Clip A — S23a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | ← S22c (last frame) — Chain 3 (end) |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/23.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> Extreme wide shot. A dark residential tower at night, heavy fog. The @Damaged chrome android barely visible - a tiny figure on a small balcony. The camera retreats to its absolute farthest - the figure a speck. Foggy dead city lights scattered far below. Cold grey-blue deep night, heavy fog, desaturated Kodachrome. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S23b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/23.png`

**Camera Move:** Static

**Motion Prompt:**
> Extreme wide shot held. The dark tower, the tiny figure on the balcony, the foggy void. The image settles into near-total stillness - only fog drifts slowly. Cold grey-blue deep night, heavy fog, desaturated Kodachrome. Fading, draining toward dark. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S23c

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/23.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> The frame widens further from the dark tower - the tiny balcony figure shrinking to a near-invisible speck. Fog fills the expanding frame. The image drains toward black and silence. Cold grey-blue deep night, heavy fog. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S24 — Clarity, Not Defeat (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 5:34–5:50 |
| **Scene Duration** | 16s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim to 16s) |
| **Musical Moment** | Sudden silence → minimalist piano. Calm, hopeful spoken word: "Now I remember… a Wasteland." Low energy — the first hope. |
| **Scene Context** | Override 10: Balcony threshold. Everything stops. Stillness is clarity, not defeat. Eye-beam shows bare horizon. |

#### Clip A — S24a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element required |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/24.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android standing at the balcony threshold - dark room with glass door behind, foggy void ahead. Attentive stance, not slumped. Sudden stillness. Cold grey-blue deep night, heavy fog. Faint atmospheric breathing - fog drifts gently. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S24b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/24.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Closing slowly on the @Damaged chrome android at the balcony threshold. His stance is upright, attentive. A faint pale light from his optical lenses directed toward the distant fog - showing a bare horizon line, not a feed. Cold, still, the quality of the darkness has shifted. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S25 — The Unplug / Tether Payoff (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 5:50–6:00 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "I must cast off this metal straightjacket… and get out of here." Low energy, decisive. |
| **Scene Context** | Override 10: Back into the room. Grips cable. PULLS THE PLUG. Dying spark. Cable falls. The first deliberate act. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |

> **PRODUCTION NOTE:** Image adjusted — close-up of hands tearing wires from own chassis (not wall socket). More visceral, literal "cast off the straightjacket."

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/25.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Close-up. The @Damaged chrome android's hands gripping cables and wires embedded in his own chassis, slowly and deliberately tearing them free. Sparks fly at the disconnection points. Exposed wires, corroded chrome. One decisive physical act. Cold dark room, the sparks are the only light accent. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S26 — The Descent (Stairwell) (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:00–6:07 |
| **Scene Duration** | 7s |
| **Coverage** | Direct — 1 × 10s (trim 3s) |
| **Musical Moment** | Whispered mantra building — "To forget what I was taught / To remember what I forgot." Building energy. |
| **Scene Context** | After the unplug, Robotiko leaves the apartment. Descending the stairwell — purposeful, determined. The physical act of leaving. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |

> **PRODUCTION NOTE — SPATIAL LOGIC FIX:** Original S26 had Robotiko rising toward the balcony. Changed to stairwell descent for spatial continuity: room (S25) → stairs (S26) → building entrance (S27) → street (S28-S29). See visual prompts S26 note for full rationale.

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/26.png`

**Camera Move:** Tilt Down

**Motion Prompt:**
> Low-angle looking up a dark concrete stairwell. The @Damaged chrome android descends the stairs toward the camera, face visible, spine straight, one hand on the metal railing. A dim bare utility bulb casts cold hard shadows down the stairwell. He moves with determination. Subtle downward camera tilt as he approaches, strictly within the existing frame composition. Do not reveal new elements below the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S27 — THE TURN: Building Entrance / Single Received Amber Ember / The Only Dolly In (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 6:07–6:18 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | Powerful, certain — "The Hammer of Truth is there. You are there. I know… I AM COMING." Building→peak. **THE CLIMAX.** |
| **Scene Context** | THE MAKE-OR-BREAK BEAT. At the building entrance, stepping onto the wet street. Facing the horizon — the direction he will walk. Single amber rift in fog. Warm wash arrives from outside onto wet chrome. Eyes STEADY (flicker stops). **The only Dolly In. The only amber.** Moon/Sun: received, never emitted. |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement. **OmniEdit HIGH PRIORITY.** |
| **Speed Ramp** | 0.91× (10s → 11s) |

> **PRODUCTION NOTE — SPATIAL LOGIC FIX:** Original S27 at balcony threshold. Moved to building entrance: amber arrives as he steps into the world (not while standing above it). Doorframe = last Architecture Cage, walked through. All amber requirements preserved. See visual prompts S27 note.

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/27.png`

**Camera Move:** Dolly In

**Motion Prompt:**
> The @Damaged chrome android standing in a dark building doorframe, facing outward toward a wet street. A single warm amber light point glows on the far horizon, visible down the road through the fog. Warm amber-tinted fog slowly reaches the figure at the entrance, reflecting on his wet chrome surfaces. His optical lenses steady - the flickering stops, becoming clear and still. The camera moves forward toward him - the only approach of the entire film. Dark interior behind, amber direction ahead. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S28 — First Steps Forward (Multi-Clip: 4 clips)

| Field | Value |
|---|---|
| **Timestamp** | 6:18–6:50 |
| **Scene Duration** | 32s |
| **Coverage** | Multi-Clip — 4 × 10s = 40s (trim to 32s) |
| **Musical Moment** | Soulful fuzz guitar over piano — hopeful, melancholic. Fading energy. The first forward motion. |
| **Scene Context** | Override 11: Leaves the building. Wet street. First forward steps toward the amber rift. Same retreating composition, inverted meaning — he walks INTO the opening. |

> **Note (2026-07-04):** S28a-d intentionally use the same source image (28.png) without frame chaining. Unlike S05 (where the replay-effect was fixed with frame chains), S28's four clips represent the same continuous walk seen from four angles — a deliberate "coverage shooting" strategy where each clip is a self-contained take, not a sequential chain. CapCut selects the best 1-2 takes; unused clips are cut coverage.

#### Clip A — S28a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/28.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android on a wet street at night, taking deliberate forward steps toward a faint amber light on the distant horizon. Dark buildings recede behind him. The camera retreats along the road ahead - the same retreating motion as the refrains, but now he walks purposefully into it. Wet asphalt reflects faint warm-tinted light from the horizon. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S28b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/28.png`

**Camera Move:** Pan Left

**Motion Prompt:**
> A slow horizontal scan along the wet road as the @Damaged chrome android walks forward. Dark buildings slide past on either side. Wet asphalt stretches ahead toward a thinning fog and a faint amber-tinted horizon. Wind-blown mist at ground level. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S28c

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/28.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> The frame slowly widens to reveal more of the wet road stretching toward the horizon. The @Damaged chrome android a walking figure growing smaller as the road opens. Grey fog thins slightly toward the vanishing point. Dark city behind, a faint direction ahead. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip D — S28d

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/28.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android continues walking forward along the wet road. The camera retreats ahead. The figure maintains its purposeful stride, growing smaller against the expanding road. Grey thinning toward a direction. Wind-blown fog drifts across the road. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S29 — The Final Journey (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 6:50–7:19 |
| **Scene Duration** | 29s |
| **Coverage** | Multi-Clip — 3 × 10s = 30s (trim to 29s) |
| **Musical Moment** | Melody fades into wind howling → fade out. Fading energy. The bridge to EP08. |
| **Scene Context** | Override 11: The final journey. The figure walks into the amber and exits the frame — the destination fills the screen, then fades to dark. EP08 bridge. |

> **PRODUCTION NOTE:** All S29 clips reuse **28.png** as source image (Nano Banana broke building composition on very wide attempts). Clip progression: Crane Up (departure) → Slow Zoom In (figure exits frame, amber fills screen) → Static fade-to-black from S29b's extracted last frame (amber glow → dark). Fade done by Kling, not CapCut — more natural.

#### Clip A — S29a

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/28.png` (reuse)

**Camera Move:** Crane Up

**Motion Prompt:**
> Starting tight on the @Damaged chrome android walking the wet road. The camera rises slowly, the figure shrinking below as the sky and the amber-tinted horizon ahead expand in the frame, strictly within the existing frame composition. The world opens as the figure grows small. Do not add new elements above the frame - reveal only what is already in the image. Wind-blown fog drifts. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S29b

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — Element + camera movement |
| **Frame Chain** | None |

**Assets Required:**
- **Start Frame:** `episode-07/04_visuals/raw/28.png` (reuse)

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The camera zooms slowly toward the warm amber light on the far horizon. The @Damaged chrome android walks forward and gradually exits the bottom of the frame - the figure leaves, the destination remains. The amber rift on the horizon grows, its warm glow expanding to fill the frame. Wet asphalt reflections of amber light stretch toward the camera. Wind rises. The amber light becomes the whole world. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S29c

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p) — camera movement (fade) |
| **Frame Chain** | ← S29b (last frame, extracted via Kling Extract Frame) |

**Assets Required:**
- **Start Frame:** Extracted last frame of S29b (amber-filled horizon, no figure)

**Camera Move:** Static

**Motion Prompt:**
> A warm amber glow fills the frame - the distant horizon light now close and dominant. No figure. The amber light slowly dims, the image gradually darkening to black. Wind howls. The glow fades. Darkness. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

## BEAT SYNC NOTES

| Timestamp | Musical Event | Required Visual Action | Clip Reference |
|---|---|---|---|
| 0:34 | "But now…" — spoken word hinge | Cut to S03 (the rise). Speed ramp begins. | S03 |
| 1:40 | "Dive into the noise" — chaotic bg enters | Eye-projection ignites (cold blue-white beam appears) | S07 |
| 1:49 | Refrain 1 vocal entry — high-pitch | Dolly Out begins. Distance ladder rung 1. | S08 |
| 2:36 | Refrain 2 vocal entry | Dolly Out. Rung 2. Cut from S10d chain to S11. | S11 |
| ~3:12 | 3-SECOND SILENCE before "past due" | Camera HOLDS. MS 1. Motionless beat. | S14 |
| 3:30 | Refrain 3 vocal entry | Dolly Out. Rung 3. Chain 2 ends. | S15 |
| 3:53 | Refrain 4 vocal entry | Dolly Out. Rung 4 — widest crowd distance. | S17 |
| ~4:26 | 3-SECOND SILENCE after "peace awards" | Camera HOLDS. MS 1. Frozen broadcast. | S20 |
| 4:32 | Refrain 5 vocal entry (highest) | Slow Zoom Out from high angle. Rung 5 — peak isolation. | S21 |
| 4:42 | Chorus cry — "Because you are gone…!" | Slow Zoom In → STILL HOLD. Heaviest grain. | S22a → S22b |
| 5:07 | Fuzz guitar solo begins | Cut to extreme wide (S23a). Dolly Out to farthest. | S23a |
| 5:33 | Solo dies to silence/feedback | S23c settling into dark and stillness. | S23c |
| 5:34 | SUDDEN SILENCE — minimalist piano | Cut to S24a. Static. The quality of stillness changes. | S24a |
| ~5:50 | "Cast off this metal straightjacket" | The UNPLUG — cable pulled. Dying spark. | S25 |
| 6:07 | "I AM COMING" — the climax declaration | **THE ONLY DOLLY IN.** Amber ember arrives from horizon. Eyes steady. | S27 |
| 6:18 | Instrumental outro begins (guitar + piano) | Cut to street. First forward steps. Dolly Out inverted. | S28a |

---

## FRAME CHAIN MAP

| Chain | Clips | Location | Notes |
|---|---|---|---|
| Chain 1 | S10d → S11 | Home room | Continuous Dolly Out: desk retreat → full room view. Same room, same CRT glow. |
| Chain 2 | S13b → S14 → S15 | Transit / bus stop | Hope → held silence → retreat. 3 clips (max chain length). Same bench, same lamp. |
| Chain 3 | S22c → S23a | Balcony | Chorus cry Dolly Out → guitar solo extreme wide. Same balcony, the retreating camera's climax. |

---

## COVERAGE SUMMARY

| Metric | Value |
|---|---|
| **Total music duration** | 439s |
| **Total generated clip duration** | 490s (49 × 10s) |
| **Coverage ratio** | 111.6% (excess trimmed in CapCut) |
| **Effective coverage** | 100% (speed ramps + trim fill all 439s) |
| **Total clips** | 49 |
| **Clips from existing images** | 49 (all images generated — S29 reuses 28.png) |
| **Clips needing new images** | 0 ✅ |
| **Speed Ramp clips** | 8 (S01, S03, S06, S12, S14, S15, S17, S27) |

**Speed Ramp Detail:**

| Clip | Generated | Playback | Result |
|---|---|---|---|
| S01 | 10s | 0.83× | 12s |
| S03 | 10s | 0.77× | 13s |
| S06 | 10s | 0.77× | 13s |
| S12 | 10s | 0.77× | 13s |
| S14 | 10s | 0.67× | 15s |
| S15 | 10s | 0.71× | 14s |
| S17 | 10s | 0.91× | 11s |
| S27 | 10s | 0.91× | 11s |

> All speed ramps ≤ 1.5× slowdown limit. ✅

---

## CAMERA DIVERSITY REPORT

| Camera Move | Count | % of Total | Limit | Status |
|---|---|---|---|---|
| Dolly Out | 11 | 22.4% | 30% max | ✅ |
| Static | 13 | 26.5% | ≥15% min / 30% max | ✅ |
| Slow Zoom In | 10 | 20.4% | 30% max | ✅ |
| Slow Zoom Out | 6 | 12.2% | 30% max | ✅ |
| Pan Left | 3 | 6.1% | — | ✅ |
| Pan Right | 2 | 4.1% | — | ✅ |
| Tilt Down | 2 | 4.1% | ≤3 (accent) | ✅ |
| Crane Up | 1 | 2.0% | ≤3 (accent) | ✅ |
| Dolly In | 1 | 2.0% | EP07: exactly 1 | ✅ |
| **TOTAL** | **49** | **100%** | — | — |

**Local variety check:** ✅ All 5-clip windows contain ≥3 different moves. (Re-verified after all production updates.)

**Accent move budget:** Tilt Down ×2 (S19b + S26), Crane Up ×1 (S29a), Dolly In ×1 (S27) — within ≤3 limits. No Orbital, no Handheld, no Tilt Up used.

**Episode Camera Personality compliance:**
- Dolly Out dominant (22.4%) ✅ — the Retreating Camera
- Static secondary (26.5%) ✅ — emptiness between retreats
- Single Dolly In at S27 ("I AM COMING") ✅ — pattern broken = will asserted
- MS average ~2.8 ✅ — lowest of series, the darkness is quiet

---

## DIRECTOR'S NOTES

### MS Average
- **Target:** ~3.0 (concept notes)
- **Actual:** ~2.8 (137 total MS / 49 clips)
- **Justification:** Intentionally at the low end. EP07 is the darkest, quietest episode. MS peaks only at refrains (4-5), chorus (4 → 1 Still Hold), and the climax (5). The body of the episode breathes at MS 2-3. This IS the art-house short film: silence and restraint carry it.

### Visual Signature Moments

| Signature | Location | Implementation |
|---|---|---|
| **Still Hold** | S22b (Chorus Cry, 4:42) | Static + MS 1. Preceded by S22a (MS 4) for contrast. The fist fails in stillness. |
| **Amber Pulse** | S27 (THE TURN, 6:07) | Single received amber from horizon. The ONLY warm tone in the episode. Moon/Sun: arrives from outside, reflected on chrome. Eyes steady, never glow. |
| **Architecture Cage** | S01, S04, S08, S12, S17, S18, S21, S23 | Character <30% of frame throughout. Environment dominates. |
| **Chrome Reflection** | S02 (water), S06 (water), S11 (screen), S17 (shop glass) | Wet reflections as interiority device. |
| **Grain Crescendo** | S22a-c (Chorus) | "Extremely heavy, visible film grain" in motion prompts. Maximum grain at emotional peak. |

### Dissonance Moments
- **None explicitly marked.** EP07's energy arc naturally matches the visual restraint. The low MS during refrains (medium-high musical energy) could read as mild dissonance, but this IS the episode's personality (the Retreating Camera): the music builds while the camera retreats. Not a mismatch — it's the design.

### Camera Personality Pattern Compliance
- ✅ Dolly Out dominant (~22.4%)
- ✅ 5× refrain distance ladder: S08 (rung 1) → S11 (rung 2) → S15 (rung 3) → S17 (rung 4, Slow Zoom In override — distance implied by framing, not camera move) → S21 (rung 5)
- ✅ TEK Dolly In: S27 "I AM COMING" — pattern broken = will asserted
- ✅ Static for emptiness between retreats (~26.5%)
- ✅ Piano interludes = character absent (S04, S09, S12, S18)

### OmniEdit Priority
1. **S27** — the single amber ember must be perfect
2. **S07, S08, S19** — projection scenes (spawn risk from projected figures)
3. **S05, S16, S17** — crowd scenes (duplication risk)
4. **S22** — Still Hold + Grain Crescendo (atmosphere critical)

### Production Adjustments (Post-Image-Generation)
- **S19/S20:** Standing with wall projection (not supine on bed) — Nano Banana could not reliably generate supine + upward eye-projection. Stronger composition.
- **S25:** Close-up tearing wires from own chassis (not wall socket cable) — more visceral, literal "cast off the straightjacket."
- **S26/S27 SPATIAL LOGIC FIX:** Balcony → street teleport eliminated. New flow: room (S25 unplug) → stairwell (S26 descent) → building entrance (S27 amber + Dolly In) → street (S28-S29). Amber ember moved from balcony to building entrance — all requirements preserved, narratively stronger.
- **S29:** Reuses 28.png — Nano Banana broke building composition on very wide shots. Crane Up camera movement achieves the widening effect.

### Asset Status
- All 29 scene images generated ✅ (26.png stairwell, 27.png building entrance, 28.png road — all confirmed)
- S29 reuses 28.png (Crane Up camera movement for widening) ✅
- No pending assets — ready for video generation upon approval.

### Kling 3.0 @Damaged Element Cost Tracking
- **Total @Damaged clips:** 43
- **Track:** credits per clip, retake rate, OmniEdit usage
- **Decision gate:** After EP07 production, evaluate cost vs. consistency gain to decide on Omni References for EP08+

### Color Consistency Note (Balcony Cluster S22-S24)
- Generated images have inconsistent color temperatures (foggy grey / dark noir / blue-teal)
- Motion prompts consistently specify "cold grey-blue deep night, heavy fog, desaturated Kodachrome"
- Video tool will normalize; final correction via CapCut color grading

---

## APPROVAL STATUS

- [ ] **Human reviewed camera moves**
- [ ] **Human reviewed tech strategy (Mode A only — confirmed appropriate)**
- [ ] **Human reviewed duration coverage (49 clips, 111.6% raw, 100% effective)**
- [ ] **Human reviewed camera diversity (all thresholds met)**
- [ ] **Human reviewed Element assignments (@Damaged on all character clips)**
- [ ] **Human reviewed tool assignments (47 Kling 3.0 / 2 Kling 2.5 Turbo)**
- [x] **All scene images generated (S26 stairwell, S27 building entrance, S28 road, S29 reuses 28.png)**
- [ ] **Human approved**
- [ ] **Ready for video generation**

> ⛔ Video generation must NOT begin until this document is approved.
> "Would Fibula approve this?" — Yes.

---

*"Motion is the breath between the frames. Without it, the image is a photograph. With it, the image is alive."*
