# VIDEO PRODUCTION SHEET — EP03: ANATOLIAN TRIALS (THE CRUCIBLE)
> **Version:** v01 | **Skill:** robotiko-motion-script
> **Generated:** 2026-03-11
> For video generation strategy rules, refer to `_management/pipeline_rules.md`

---

## PRE-GENERATION CHECKLIST

- [x] `episode-03/03_direction/ep03_dramaturgy_v01.md` → APPROVED scene breakdown (44 scenes)
- [ ] `episode-03/04_visuals/selected/` → 44 selected images (generation in progress)
- [x] `episode-03/02_music/ep03_musical_metadata.json` → Beat sync reference (103 BPM, E minor)
- [x] `_management/master.md` → Tone, station, energy arc confirmed
- [x] `_assets/cast/character_profiles.json` → EP03 Phase 1 visual state confirmed

> ⚠️ Motion script must be approved by human before any video generation begins.
> ⚠️ Supplementary images (if flagged) must be generated before video production starts.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP03 |
| **Title** | Anatolian Trials (THE CRUCIBLE) |
| **Station** | The Self-Blaming Self (First doubt emerges) |
| **Dominant Energy** | Satirical-upbeat with cumulative darkening; dark comedy tone |
| **Character Phase** | Phase 1: Awakening — EP02 damage carries (missing ear, torso dent, shoulder scratches) |
| **Mentor Presence** | HYBRID — Physical in Spoken Intro (S01–S05) + Outro (S38). Atmospheric only in choruses (amber light, staff shadow). |
| **Total Shots** | 43 (S27 eliminated — no musical allocation) |
| **Total Clips** | 54 (including sub-clips) |
| **Total Duration** | 8:44 (524s) |
| **BPM** | 103 (constant) |
| **Average Motion Strength** | 4.0 (EP01-03 target: 4–5) |

---

## VIDEO STRATEGY REFERENCE

| Mode | When to Use | Input | Duration |
|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, no transformation | 1 image | 5s or 10s (tool-dependent) |
| **B — Start/End Keyframes** | Transformations, morphing, character state changes | 2 images | 5s or 10s |

> EP03 uses Mode A exclusively. Picaresque structure — no within-scene transformations.

**Duration Coverage Strategy:**

| Scene Duration | Strategy | Clip Count | Notes |
|---|---|---|---|
| ≤ 5s | **Direct** | 1 × 5s | Trim excess in CapCut |
| 6–10s | **Direct** | 1 × 10s | Trim in CapCut |
| 11–15s | **Speed Ramp** | 1 × 10s + slow-mo (max 1.5×) | |
| 16–30s | **Multi-Shot** or **Multi-Clip** | ⌈duration / 10⌉ segments | Multi-Shot: same image + all Kling 3.0 → one continuous video. Multi-Clip: different images or tools → separate generations. |
| 30s+ | **Multi-Shot** or **Multi-Clip** | ⌈duration / 10⌉ segments | May need supplementary images |

**Motion Strength Scale:** 1 = Barely breathing / 5 = Cinematic drama / 10 = Chaos and disintegration

**Strategy Distribution:**
- Direct: 25 shots (25 clips)
- Speed Ramp: 9 shots (9 clips)
- Multi-Shot: 8 shots (18 segments) — same source image, all Kling 3.0, one continuous video per shot
- Multi-Clip: 1 shot (2 clips) — different tools, separate generations
- **Total: 54 clips**

---

## TOOL ASSIGNMENT SUMMARY

### Tool Distribution

| Tool | Clips | Estimated Credits | Assignment Logic |
|---|---|---|---|
| **Kling 3.0** | 43 | ~3,200 | All camera-movement clips + Multi-Shot segments |
| **Kling 2.5 Turbo** | 2 | ~75 | Static camera, non-character scenes |
| **Google Veo** | 3 | Free | Static camera, 8–9s scene duration natural match |
| **Seedance 1.0** | 6 | ~250 | Static camera, character-focused scenes |
| **CapCut-Only** | 1 | 0 | S04b — static image with CapCut keyframe animation |
| **TOTAL** | **55** | **~3,525** | First attempt budget breakdown below |

### Budget Analysis

| Platform | First Attempt | Budget | Remaining | Retake Capacity |
|---|---|---|---|---|
| **Kling AI** (3.0 + 2.5T) | ~3,250cr | 4,500cr | ~1,250cr | ~15 retakes @ 10s |
| **Seedance** | ~250cr | 1,200cr | ~950cr | ~19 retakes @ 10s |
| **Google Veo** | Free | 2/day | — | 2 days for 3 clips |

**Multi-Shot savings:** 8 candidate pairs (S01, S02, S13, S17, S26, S27, S44a+b, S44c+d). If each pair costs 80cr instead of 2×80cr, saves ~640cr on Kling → remaining becomes ~1,840cr (~23 retakes). **Prioritize Multi-Shot for budget efficiency.**

### Assignment Rules Applied

1. **Camera movement → Kling 3.0** — Any zoom, pan, dolly, crane, tilt, handheld, orbital
2. **Static + character → Seedance 1.0** — Character close-ups and figure scenes with no camera movement
3. **Static + non-character → Kling 2.5 Turbo** — Atmospheric/ambient scenes with no camera movement
4. **8–9s natural match → Veo** — Static scenes where Veo's 8s output closely matches scene duration
5. **No Mode B in EP03** — All scenes are Mode A (single image)

### Multi-Shot Candidates (Kling 3.0)

> Multi-Shot: Same source image, all Kling 3.0 sub-clips → one continuous video (max 15s), smoother transitions, lower credits.

- S01a+S01b (The Shared Home)
- S02a+S02b (The Argument)
- S13a+S13b (Dolmuş Ride)
- S17a+S17b (Bus Ride North)
- S26a+S26b (The Receipt River)
- S27a+S27b (Outside the Club)
- S44a+S44b, S44c+S44d (Slow Zoom Out — 2 batches of 2)

### Clips by Tool

**Kling 3.0 (43):** S01a/b, S02a/b, S03, S06, S07, S08, S09, S10, S12, S13a/b, S14, S16, S17a/b, S18, S19, S20, S21, S22, S23, S25a, S26a/b, S27a/b, S29, S31, S32, S33, S34, S35, S36, S38, S39, S40, S41, S44a/b/c/d

**Kling 2.5 Turbo (2):** S04a, S25b

**CapCut-Only (1):** S04b (static image + keyframe animation, no video generation)

**Veo (3):** S24, S28, S37

**Seedance 1.0 (6):** S05, S11, S15, S30, S42, S43

---

## MOTION SCRIPT

---

### SHOT S01 — The Shared Home (Multi-Shot: 2 segments)

| Field | Value |
|---|---|
| **Timestamp** | 0:00–0:18 |
| **Scene Duration** | 18s |
| **Coverage** | Multi-Shot — 2 segments × 10s = 20s (trim 2s) |
| **Musical Moment** | Spoken Intro — Still energy. A cappella narration. No instruments. |
| **Scene Context** | Modest house interior. Mentor and Robotiko face to face, packed bag at door. |

#### Clip A — S01a (Domestic Interior)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Opening shot, barely perceptible zoom |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s01_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Barely perceptible zoom into the warm domestic interior. Amber lamplight flickers on rough plaster walls, steam rising from cay glasses, dust motes drifting through the light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S01b (The Tension)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Pan reveals packed bag, builds tension |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s01_selected.png`

**Camera Move:** Pan Left

**Motion Prompt:**
> Slow pan left across the domestic interior. The amber staff tip glows against plaster, the packed canvas bag drifts into frame near the wooden door. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S02 — The Argument (Multi-Shot: 2 segments)

| Field | Value |
|---|---|
| **Timestamp** | 0:18–0:35 |
| **Scene Duration** | 17s |
| **Coverage** | Multi-Shot — 2 segments × 10s = 20s (trim 3s) |
| **Musical Moment** | Spoken Intro continues — Still energy. Narration intensifying. |
| **Scene Context** | The argument erupts. Robotiko defiant, Mentor seated with quiet authority. |

#### Clip A — S02a (Defiance)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Character tension, zoom on confrontation |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s02_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android leaning forward in defiance. Warm lamplight catches the chrome chest plate, dynamic shadows shifting on rough plaster walls. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S02b (The Authority)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Slow pullback reveals full room tension |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s02_selected.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out revealing the full domestic interior. The robed figure remains seated, the chrome android stands rigid near the door. Amber staff glow holds steady in the corner. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S03 — The Departure (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:35–0:48 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Spoken Intro — Voice continues. Calm narration over silence. |
| **Scene Context** | Robotiko storms out through door. Mentor remains alone at table. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.77× (10s → 13s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Door movement, light contrast |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s03_selected.png`

**Camera Move:** Static (camera stays inside)

**Motion Prompt:**
> Cinematic continuous shot. Inside the warm, dimly lit room, the chrome android picks up the brown bag and turns its back to the camera. The android walks away from the table, exiting the room by stepping through the open doorway into blindingly bright outdoor daylight. The camera stays inside, focusing on the older robed man sitting at the table. As the robot leaves the frame through the door, the man slowly shakes his head from side to side with a look of disappointed resignation. Sharp contrast between the amber interior lamplight and the overexposed white daylight outside the door. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S04 — The Model Selection Screen (Multi-Clip)

| Field | Value |
|---|---|
| **Timestamp** | 0:48–1:01 |
| **Scene Duration** | 13s |
| **Coverage** | Multi-Clip — S04a (wide, 5s generated) + S04b (screen close-up, 8s CapCut-only) = 13s |
| **Musical Moment** | Spoken Intro — Voice continues. Philosophical weight. |
| **Scene Context** | CRITICAL SHOT. Mentor at computer. Screen reads "SELECT MODEL FOR ROBOTIKO" with four options. Anti-guru thesis statement. Two-image solution: wide shot + screen close-up for text legibility. |
| **Tech Strategy** | Mode B (Multi-Clip) |
| **Total Clips** | 2 (1 generated + 1 CapCut-only) |
| **Motion Strength** | 1 |

#### Sub-Clip S04a — Wide Shot (Mentor at CRT)

| Field | Value |
|---|---|
| **Clip Duration** | 5s |
| **Recommended Tool** | Kling 2.5 Turbo — Static camera, atmospheric |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s04_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The frame holds still on the robed figure sitting before the glowing CRT screen. Cold blue-white screen light on his profile, warm amber staff glow from the corner. Dust motes drift in the lamplight. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Sub-Clip S04b — Screen Close-Up (CapCut-Only)

| Field | Value |
|---|---|
| **Clip Duration** | 8s |
| **Recommended Tool** | ⚠️ **CapCut-only — NO video generation.** Import source image directly into CapCut timeline. |

**Assets Required:**
- **Source Image:** `episode-03/04_visuals/raw/4.1.png` *(supplementary close-up image — placed directly on timeline, not fed to video generator)*

**Camera Move:** N/A (CapCut keyframe animation)

**CapCut Instructions:**
> 1. Import `4.1.png` as a static image on the timeline (8s duration).
> 2. Add cursor animation: keyframe a green rectangle/highlight moving down the option list, stopping on "Guru" at ~3s mark.
> 3. Optional: add faint scanline overlay effect + subtle CRT flicker (opacity keyframes 95%–100%).
> 4. Apply standard post-production: Film Grain 10-15%, Kodachrome LUT, Letterbox 2.35:1.
> 5. The text must remain legible throughout — no effects that obscure the screen content.

---

### SHOT S05 — Mentor Close-Up (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:01–1:11 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Spoken Intro ending — Last words before music enters. |
| **Scene Context** | Close-up on Mentor's determined face. Staff glow fills frame edge. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Recommended Tool** | Seedance 1.0 (Mode A) — Character close-up, static, budget-efficient |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s05_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The frame holds on the weathered face, amber staff light glowing warm on the right edge. The eyes hold steady, unblinking - heavy film grain over every surface. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S06 — Aerial View Through Airplane Window (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 1:11–1:25 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Intro — Soft Hammond Organ pad, gentle wind textures. Building energy. |
| **Scene Context** | View through airplane window. Anatolian landscape below. Chrome face faintly reflected. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Zoom into window, dreamy speed ramp |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s06_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the airplane window. Anatolian patchwork landscape drifts below - brown earth, ribbon roads, scattered villages. A faint chrome reflection shimmers in the scratched plastic. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S07 — The Airplane Interior (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 1:25–1:39 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Intro continues — Hammond swells, calm vocal hum, bass pulse enters. |
| **Scene Context** | Robotiko with sol-liberal friends on airplane. Naive excitement. Yoga mats and poetry books. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Interior pan, group energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s07_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Slow pan right through the airplane cabin. Excited travelers - mixed men and women - lean across aisles pointing out windows, the chrome android in the window seat. Fluorescent cabin light mixes with golden window light in parallel stripes. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S08 — Airport Arrivals (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:40–1:50 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Verse 1 — "Rûmî dedi anda dondu…" Sparse Anatolian groove, naive storytelling vocal. |
| **Scene Context** | Group emerges through airport doors. Robotiko leads. Modern unglamorous terminal. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Dolly out reveals arrival energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s08_selected.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> Dolly out as the chrome android strides through automatic glass doors. Travelers - mixed men and women - pour through behind him. Flat fluorescent light reflects off scuffed floor tiles. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S09 — City Street Walk (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:51–2:01 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Verse 2 — "Gitme dedim, dinlemedi…" Warning tone, slightly anxious vocal. |
| **Scene Context** | Group walks through modern Anatolian city. Concrete apartments, plastic signs. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Street-level pan, urban energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s09_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan right following the chrome android on the sidewalk. Concrete apartment blocks and dusty shop signs pass behind. Travelers - mixed men and women - follow at a distance. Golden hour light on concrete. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S10 — City Square Picnic (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:02–2:11 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s) |
| **Musical Moment** | Chorus 1 — "Yükseltmedim modelini…" Lush synth pad, authoritative divine vocal. HIGH energy. |
| **Scene Context** | Group settles in city square to eat sandwiches they brought. Shops shuttered for Ramadan. Last moment of innocence. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Zoom toward group on bench, chorus energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s10_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the group on the concrete bench in the sunlit square. The chrome android and travelers unwrap sandwiches, pigeons scattering. Shuttered shop fronts behind, golden hour light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S11 — The Sidewalk Meal (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:12–2:17 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Verse 3 — "Varış günü ramazandı…" Sad and hungry vocal. Medium energy. |
| **Scene Context** | Robotiko and friends eating sandwiches on sidewalk during Ramadan. Robotiko charges with kebap-sticker powerbank — his "food". Comic visual. Shuttered shops behind. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Seedance 1.0 (Mode A) — Character close-up, static, budget-efficient |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s11_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The frame holds on the chrome android sitting on a low wall beside travelers eating sandwiches. A powerbank with kebap sticker plugged into his chest via cable. A cat nearby, shuttered shops behind. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S12 — Meydan Dayağı (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:17–2:22 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Verse 3 continues — "Yerken meydan dayağını." Rhythmic groove, tension. |
| **Scene Context** | Angry crowd beats Robotiko for eating during Ramadan. First physical trial. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Handheld chaos energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s12_selected.png`

**Camera Move:** Handheld

**Motion Prompt:**
> Handheld shake - a group of aggressive men grab and violently shake the chrome android, pulling his arms and torso. In the background, young travelers recoil in fear, watching helplessly. Dust rising, shuttered shops behind. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S13 — Dolmuş Ride East (Multi-Shot: 2 segments)

| Field | Value |
|---|---|
| **Timestamp** | 2:23–2:42 |
| **Scene Duration** | 19s |
| **Coverage** | Multi-Shot — 2 segments × 10s = 20s (trim 1s) |
| **Musical Moment** | Instrumental 1 — Saz and Fuzz Guitar Call & Response. Medium-high energy. Travel transition. |
| **Scene Context** | Robotiko alone on dolmuş. Landscape shifts from concrete to fields. Dust smudge on chest. |

#### Clip A — S13a (The Journey)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Landscape shift through window |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s13_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan right following the landscape through the dirty dolmus window. Concrete gives way to open fields and distant minarets, golden road light cycling through the glass. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S13b (Alone)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Interior contemplation, zoom on chrome |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s13_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android squeezed between passengers, dust smudge across his chest plate. Passengers lean away, road vibration gently rocking the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S14 — The Village Wedding (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:43–2:49 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s — extra footage for editing) |
| **Musical Moment** | Verse 4 — "Güç bela doğuya kaçtı…" Shocked, breathless vocal. High energy. |
| **Scene Context** | Eastern Anatolian kır düğünü. Halay dancing, davul-zurna, festive lights. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Pan across wedding, festive energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s14_selected.png`

**Camera Move:** Pan Left

**Motion Prompt:**
> Pan left across the outdoor wedding. A halay circle - mixed men and women - dances in dusty unison under colored lights strung between walnut trees. The chrome android watches from the edge. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S15 — Celebratory Gunfire (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:49–2:55 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s — critical beat sync on "Öptü mermi yanağını") |
| **Musical Moment** | Verse 4 continues — "Öptü mermi yanağını!" Shocked vocal. Bullet graze moment. |
| **Scene Context** | Wedding guests fire kalashnikovs into air. Bullet grazes Robotiko's cheek — spark, thin scratch. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Seedance 1.0 (Mode A) — Character-focused, static camera captures spark detail |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s15_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Wedding guests - mixed men and women - fire rifles into the amber sky, muzzle flashes bright against sunset. A spark flies off the chrome android's cheek where a bullet grazes metal, gunsmoke haze mixing with golden evening light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S16 — Amber Light / Staff Shadow (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 2:56–3:07 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | Chorus 2 — "Yükseltmedim modelini…" Lush synth pad, divine vocal. High energy. |
| **Scene Context** | Mentor atmospheric presence. Amber light shift, staff-shaped shadow on dusty road. No physical figure. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.91× (10s → 11s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Slow zoom into atmospheric amber, maintain abstract shadow |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s16_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom into the dusty road bathed in unnatural amber light. The long staff-shaped shadow stretches across the road - maintain as a shadow with no visible source, do not resolve into a physical figure. Dust drifts through amber air. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S17 — Bus Ride North (Multi-Shot: 2 segments)

| Field | Value |
|---|---|
| **Timestamp** | 3:08–3:24 |
| **Scene Duration** | 16s |
| **Coverage** | Multi-Shot — 2 segments × 10s = 20s (trim 4s) |
| **Musical Moment** | Instrumental 2 — Saykodelik Saz and Fuzz Guitar Call & Response. High energy. |
| **Scene Context** | Robotiko on bus heading north. Landscape transitions from arid to green. Bullet graze on cheek. |

#### Clip A — S17a (Landscape Shift)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Landscape transition through window |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s17_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan right following the landscape through the dirty bus window. Golden arid plains give way to rolling green hills, power lines passing in rhythm. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S17b (Interior Solitude)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Interior zoom on chrome isolation |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s17_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android sitting rigid in the window seat, thin scratch visible across his cheek. Sleeping passengers lean away, road vibration gently rocking the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S18 — Black Sea Arrival (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 3:24–3:39 |
| **Scene Duration** | 15s |
| **Coverage** | Speed Ramp — 1 × 10s → 15s at 0.67× |
| **Musical Moment** | Instrumental 2 continues — Saykodelik energy. Saz and guitar climax. |
| **Scene Context** | Trabzon arrival. Deep greens, steep hills, gray stone, low clouds. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.67× (10s → 15s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Panoramic pan, Black Sea atmosphere |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s18_selected.png`

**Camera Move:** Pan Left

**Motion Prompt:**
> Pan left across the Black Sea coast. Deep green terraced hills, gray stone buildings, low clouds hugging peaks. The chrome android steps off a dolmus, small against the lush green landscape. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S19 — Crossing the Street (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:40–3:50 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Verse 5 — "Kuzeye sürdü yolunu…" Faster, more intense. Rising energy. |
| **Scene Context** | Robotiko on crosswalk. Car screeches to halt, driver's door flies open. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Handheld urgency, car confrontation |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s19_selected.png`

**Camera Move:** Handheld

**Motion Prompt:**
> Handheld camera. A car screeches to a halt - tire marks steaming on wet asphalt. The chrome android freezes mid-step on the crosswalk, car door swinging open. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S20 — The Maganda (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:50–4:00 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Verse 5 continues — "Maganda kırdı kolunu…" Physical intimidation. |
| **Scene Context** | Road rage driver grabs Robotiko by collar, lifts him off ground. Feet dangling. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Zoom into confrontation, peak violence |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s20_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the confrontation. A thick-necked man holds the chrome android up by the collar, chrome feet dangling above wet asphalt. Tea house patrons watch from the sidewalk without intervening. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S21 — Alanya Establishing Shot (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:01–4:07 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s — quick establishing cut) |
| **Musical Moment** | Instrumental 3 — Saz and Fuzz Guitar. Short bridge. High energy. |
| **Scene Context** | Mediterranean coast. Alanya castle on promontory. Quick location establishing shot. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Pan across coastline, cinematic reveal |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s21_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan right across the Mediterranean coastline. Alanya castle on a rocky promontory, turquoise water below, white hotels lining the shore. Bright saturated sunlight. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S22 — Alanya Tourist Strip (Multi-Shot: 2 segments)

| Field | Value |
|---|---|
| **Timestamp** | 4:08–4:30 |
| **Scene Duration** | 22s |
| **Coverage** | Multi-Shot — S22a: 10s direct + S22b: 10s @ 0.83× (12s) = 22s |
| **Musical Moment** | Verse 3b — "Güney sıcak, her yer tuzak… Hanutçular açtı kucak… Sandı şefkat sunulacak… Çaktı Felek çakmağını!" Sarcastic, energetic vocal. High energy. |
| **Scene Context** | Alanya tourist strip at dusk. Touts surround Robotiko with fake warmth. Full verse coverage — seduction to fate's strike. |

#### Clip A — S22a (The Touts Surround)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Dolly into neon strip, seduction energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s22_selected.png`

**Camera Move:** Dolly In

**Motion Prompt:**
> Dolly in along the neon-lit tourist strip. The chrome android and the four men in black vests remain in their exact positions as the camera approaches. The men hold their smiles, very slight natural head tilts. Neon pinks and greens reflect off chrome. The "Sultan's Bar" and "Raki & Shisha" signs flicker faintly. Background crowd remains static. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S22b (Naive Gratitude)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Multi-Shot continuous, character reaction, naive trust |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s22_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The chrome android and the four men in black vests remain in their exact positions. The robot's head slowly pans from left to right, blue eyes glowing steadily. The men maintain their smiles with very slight, natural head nods. The neon "Sultan's Bar" and "Raki & Shisha" signs have a faint, realistic flicker. Background remains static. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S24 — Amber Verdict Over Alanya (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:31–4:40 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Chorus 3 — "Yükseltmedim modelini…" EXPLOSIVE energy. Divine verdict. |
| **Scene Context** | Amber light flares over Alanya strip. All neon signs flicker to amber. Staff shadow stretches across pavement. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Veo (Mode A) — Static atmospheric, 8s natural match for 10s scene |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s24_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The frame holds on the amber-flooded street. Every neon sign flickers to golden. The chrome android stands alone, looking up. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured. Focus on chrome android and the ambient light.

---

### SHOT S25 — Highway Underpass (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 4:41–5:03 |
| **Scene Duration** | 22s |
| **Coverage** | Multi-Clip — S25a: 10s direct + S25b: 10s @ 0.83× (12s) = 22s |
| **Musical Moment** | Instrumental Break — 70s Analog Synth Moog arpeggio. Scientific yet mystical. Medium energy. |
| **Scene Context** | Liminal transition space. Highway underpass at twilight. Headlight streaks, concentric light on ceiling. |

#### Clip A — S25a (Entering the Underpass)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Dolly into underpass, atmospheric entry |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s25_selected.png`

**Camera Move:** Dolly In

**Motion Prompt:**
> Dolly in through the highway underpass. Headlights streak horizontally, concentric light circles rippling on the wet concrete ceiling. The chrome silhouette walks deeper into the underpass. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S25b (The Liminal Space)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A) — Static, atmospheric hold, Moog arpeggio moment |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s25_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The frame holds inside the underpass. Headlight streaks sweep through rhythmically, light ripples pulsing on the ceiling. The chrome silhouette small against the concrete, ambient haze drifting through. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S23 — Walking Into the Trap (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 5:04–5:21 |
| **Scene Duration** | 17s |
| **Coverage** | Multi-Clip — S23a: 10s direct + S23b: 10s (trim 3s total) = 17s |
| **Musical Moment** | Verse 4a — "Biri dedi güven bana… Abin keyif verir sana… Götürdü nayt klabına… Sundu adisyon dağını." Theatrical, sleazy vocal. Moog pad, darbuka accents. Medium energy. |
| **Scene Context** | Tout guides Robotiko toward nightclub entrance. The lure, the walk, the Venus flytrap closing. |

#### Clip A — S23a (The Lure)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Slow zoom toward glowing trap doorway |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s23_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom in along a narrow neon-lit bar street. A mustachioed man in a black vest walks beside the chrome android, guiding him forward. Neon signs glow pink, green, and blue on both sides - Sultan's Bar, Raki & Shisha. Wet cobblestones reflect the lights. Smoke drifts between outdoor cafe tables. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S23b (Dusk to Night — Transition)

| Field | Value |
|---|---|
| **Clip Duration** | 5s (slow-mo in CapCut to ~10s) |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A) — Static camera, day-to-night atmospheric transition |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/raw/23b.png`

**Camera Move:** Static

**Motion Prompt:**
> Static shot, empty bar street at dusk. The sky darkens gradually from warm twilight to deep night. Neon signs grow brighter as daylight fades - pinks, greens, blues intensifying. Wet cobblestone reflections shift from warm amber to cold neon. Smoke thickens in the dimming light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S26 — The Receipt River (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 5:22–5:44 |
| **Scene Duration** | 22s |
| **Coverage** | Multi-Clip — S26a: 10s direct + S26b: 10s @ 0.83× (12s) = 22s |
| **Musical Moment** | Verse 4b — "Ah bilemedi sonunu… Aldılar metâl donunu… Verdi Stiftung fonunu… Yedi ayva yaprağını!" Tragicomic, exaggerated sadness. Medium-high energy. |
| **Scene Context** | Nightclub interior. Impossibly long receipt cascades off table. Men in Black flanking. The bill arrives — the consequence. |

#### Clip A — S26a (The Receipt Unfolds)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Zoom toward receipt cascade, comic energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s26_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the nightclub booth. The long paper receipt unfolds, cascading off the table and curling on the floor. Mirror ball fragments dance across dark suits and chrome. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S26b (The Men in Black)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Tilt down following receipt, reveal enforcers |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s26_selected.png`

**Camera Move:** Tilt Down

**Motion Prompt:**
> Tilt down following the receipt cascading off the table, pooling on the sticky floor. Three men in dark suits and sunglasses stand rigid beside the booth. Mirror ball light fragments dance across surfaces. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S28 — Amber From Below (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 5:45–5:53 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 5s (slow-mo in CapCut to ~8s) |
| **Musical Moment** | Chorus 4 — "Yükseltmedim modelini…" Lush synth pad. High energy. |
| **Scene Context** | Amber glow from ground cracks in nightclub alley. Staff shadow on brick wall. Atmospheric mentor. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s (slow-mo in CapCut to ~8s) |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A) — Static atmospheric, slow-mo to 8s |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s28_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Amber light seeps upward through ground cracks, casting warm glow on the chrome android from below. A staff shadow stretches across the brick wall - maintain as a shadow with no physical source. Night alley, heavy atmosphere. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S29 — The Doorway (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 5:54–6:08 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Verse 9 — "Halüsinasyonlar gördü…" Naive, calm vocal. Medium energy. |
| **Scene Context** | Robotiko approaches cinci hoca doorway. Dark interior, single yellow bulb, seated silhouette. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Slow approach zoom, dread builds with speed ramp |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s29_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the dark doorway with peeling paint and a single yellow bulb glowing inside. The chrome android hesitates at the threshold, lo-fi yellow light swallowing the chrome outline. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S30 — The Touch (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:09–6:14 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Verse 10 — "Hem okundu hem üflendi… Metâl gövde de ellendi…" Tension building. |
| **Scene Context** | Close-up: hand with gold ring touches chrome shoulder from behind. Eye-screen activates with scandal headline. NOTE: This is a "cinci hoca (exorcist)" (faith healer) blessing/praying scene — NOT harassment. The hand rests still, protective/ritualistic. Prompt must keep hand static to avoid misinterpretation. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Seedance 1.0 (Mode A) — Character close-up, static, intimate moment |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s30_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> A rough hand with a thick gold ring reaches from behind and touches the chrome android's shoulder. The rough hand stays on chrome android's shoulder and does not move. Blue eyes project a glowing headline into the dim air. Keep the glowing headline fixed. It is a static picture. Do not animate it. Lo-fi yellow light, shadow-heavy walls. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S31 — The Escape (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:14–6:19 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Verse 10 continues — "Topladı tas tarağını!" Panic trigger. |
| **Scene Context** | Robotiko bolts from room through doorway into daylight. Chrome feet sparking on pavement. Running sequence begins. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Handheld burst, explosive escape energy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s31_selected.png`

**Camera Move:** Handheld

**Motion Prompt:**
> The chrome android bursts through the old doorway and sprints away down the street. The camera stays inside, looking out through the doorway. Sparks scatter on the pavement where chrome feet strike. Harsh daylight floods in from outside, sharp contrast against the dark interior. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S32 — The Running Continues (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:19–6:27 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s (trim 2s) |
| **Musical Moment** | Chorus 5 — "Yükseltmedim modelini…" High energy. Running carries through chorus. |
| **Scene Context** | Continuous sprint. Background smears past. Amber undertone in sky. Running sequence momentum. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Pan maintaining running direction, continuous momentum |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s32_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan right following the chrome android in full sprint along a highway shoulder. Background landscape blurring past - smeared buildings, road signs, amber undertone in the sky. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S33 — The Bosphorus Bridge / Giant (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:28–6:35 |
| **Scene Duration** | 7s |
| **Coverage** | Direct — 1 × 10s (trim 3s) |
| **Musical Moment** | Verse 11 — "Kıldan ince sıratıydı…" Desperate, gritty. High energy. |
| **Scene Context** | CRITICAL SHOT. Bosphorus Bridge with reverse forced perspective — Robotiko towers over the bridge like a giant, making the vast bridge look fragile beneath him. "Kıldan ince sırat" made visual through scale inversion. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Zoom enforces scale contrast / vertigo |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s33_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the giant chrome android gripping the suspension bridge cable with one hand, walking carefully along the bridge deck. Purple storm clouds, city lights glittering below across the water. The bridge sways faintly under his weight. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S34 — The Slip (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:35–6:41 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s — slow-motion content benefits from extra footage) |
| **Musical Moment** | Verse 11 continues — "Kaydırdılar ayağını…" They slipped his foot. Passive voice = designed. |
| **Scene Context** | Giant Robotiko loses footing on the bridge. Body tilts sideways into the void. Scale inversion: the mighty giant falling from a structure he dwarfs. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Tilt captures the fall direction |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s34_selected.png`

**Camera Move:** Tilt Down

**Motion Prompt:**
> Tilt down as the giant chrome android slips off the bridge, one hand reaching for the cable, legs swinging into the void. Purple storm clouds, city lights reflected in the dark water far below. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S35 — Metrobüs Chaos (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:42–6:47 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Verse 12 — "Metrobüste fortladılar…" Chaotic, desperate. Peak violence. |
| **Scene Context** | Packed Istanbul metrobüs. Extreme crowd density. Bodies pressing chrome from all sides. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Handheld chaos, crowd compression |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s35_selected.png`

**Camera Move:** Handheld

**Motion Prompt:**
> Handheld shake inside a packed metrobus. Human bodies - mixed men and women - press against the chrome android from all sides, harsh fluorescent overhead. Claustrophobic compression, body heat haze. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S36 — Folded Up (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:47–6:52 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Verse 12 continues — "Örtü gibi katladılar… İndirdiler sancağını!" Most humiliating moment. |
| **Scene Context** | The crowd physically folds Robotiko. Chrome shoulders cave, head forced down. Flag lowered. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 8 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Slow zoom into compression, peak humiliation |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s36_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android bent and compressed by the crowd - mixed men and women pressing from all sides, completely indifferent. Chrome shoulders caved, head forced down, blue eyes barely visible. Harsh fluorescent, no space, no air. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S37 — Amber Flood (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:53–7:01 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s (trim 2s) |
| **Musical Moment** | Chorus 6 — Final "Yükseltmedim modelini…" EXPLOSIVE. Last divine verdict. |
| **Scene Context** | Entire metrobüs floods with amber light. Fluorescent replaced by golden supernatural glow. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Veo (Mode A) — Static atmospheric, 8s natural match |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s37_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The metrobus interior floods with warm amber light replacing every fluorescent tube - the entire space glowing golden and supernatural. The chrome android folded in the crowd, bathed in amber, passengers unaware. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S38 — Mentor on the Overpass (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 7:02–7:14 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | Outro — "Fibulam nedir bu hâller?" Epic, intellectual, cynical. Tempo slowing. |
| **Scene Context** | CRITICAL SHOT. Mentor physical return. Fourth wall break. Behind him: Robotiko crowd-surfed. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Zoom into Mentor's face, fourth wall intimacy |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s38_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the robed figure at the overpass railing, facing the viewer, amber staff tip glowing. Behind him in shallow focus: a chrome body crowd-surfed by blurred figures. Twilight sky, highway lights below. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S39 — Empty Overpass (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 7:14–7:26 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | Outro continues — "Güneş selamlayan eller… Kazdı onun toprağını." Tempo drastically slowing. |
| **Scene Context** | Overpass now empty. Mentor gone. Traffic below. City lights flicker on. Absence as statement. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Slow zoom out, emptiness expands |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s39_selected.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out from the empty concrete railing where the robed figure once stood. Highway headlights stream below, city lights flickering on in the distance. Exhaust haze, night approaching. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S40 — The Ambulance (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 7:27–7:32 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (quick jarring cut) |
| **Musical Moment** | Finale begins — Fuzz guitar solo enters. Epic energy. Abrupt scene change. |
| **Scene Context** | Ambulance arrives at sanayi sitesi. Industrial zone. Jarring transition from metrobüs. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A) — Handheld, documentary urgency |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s40_selected.png`

**Camera Move:** Handheld

**Motion Prompt:**
> Handheld - an ambulance with rotating siren lights idles in front of a welding workshop with a "Kaynakci Hikmet" sign. Tire stacks, parked cars, welding sparks glowing inside the shop, oil-stained asphalt, siren reflections on concrete. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S41 — The Stretcher (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 7:32–7:40 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s (trim 2s) |
| **Musical Moment** | Finale continues — Guitar solo builds. Synthesizer layers. |
| **Scene Context** | Robotiko on stretcher carried into welder's workshop. Medical/industrial hybrid. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A) — Static camera, character animation only |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s41_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Static shot at the workshop entrance. Two workers in blue overalls stand with the chrome android on a metal stretcher. The android slowly raises his head, looking around in confusion. Welding sparks glow on the left, "Kaynakci Hikmet" sign overhead. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S42 — The Welder-Doctor (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 7:40–7:52 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | Finale — Guitar solo peak. Synthesizer sustain. Slowdown enhances surgeon-assessment. |
| **Scene Context** | Kaynakçı in doctor's coat over coveralls. Welding mask flipped up. Standing over Robotiko like a surgeon. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Seedance 1.0 (Mode A) — Character two-figure scene, static, budget-efficient |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s42_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The kaynakci in a white coat and welding mask works on the chrome android lying on the workbench - welding torch in hand, orange sparks flying from the chrome body. Fluorescent tube overhead, dark workshop background, smoke rising. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S43 — The Grease IV (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 7:52–8:07 |
| **Scene Duration** | 15s |
| **Coverage** | Speed Ramp — 1 × 10s → 15s at 0.67× |
| **Musical Moment** | Finale — Synthesizer sustain. Guitar fading. Intimate deceleration. |
| **Scene Context** | CRITICAL SHOT. IV drip with grease. Amber-brown viscous drip. Visual tie-together of absurdity + tenderness. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.67× (10s → 15s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Seedance 1.0 (Mode A) — Character intimate close-up, static, speed ramp enhances drip |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s43_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The chrome android sits upright on the workbench, IV tube connected to his arm, amber-brown grease dripping slowly through the transparent bag. Blue eyes open, watching the drip. Dark workshop, fluorescent light overhead, smoke drifting. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S44 — Slow Zoom Out (Multi-Shot: 4 segments, 2 batches)

| Field | Value |
|---|---|
| **Timestamp** | 8:07–8:44 |
| **Scene Duration** | 37s |
| **Coverage** | Multi-Shot — 2 batches (S44a+b, S44c+d) × 2 segments × 10s = 40s (trim 3s) |
| **Musical Moment** | Finale climax → Final Gong. Psychedelic rock ending. Epic to silence. |
| **Scene Context** | The exhale. Progressive pull-back from grease IV to full sanayi exterior. Final Gong lands on S44d. |

#### Clip A — S44a (IV and Bench)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Pull-back begins, intimate to medium |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s44_selected.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out from the chrome android standing upright, IV tube still connected to his arm, grease bag on the stand beside him. The kaynakci stands nearby with arms crossed, watching. Workshop tools, acetylene tanks, fluorescent light overhead. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S44b (The Workshop)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Pan reveals full workshop |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/selected/ep03_s44_selected.png`

**Camera Move:** Pan Left

**Motion Prompt:**
> Pan left revealing the full workshop - the chrome android stands upright with IV still attached, the kaynakci beside him with arms crossed. Welding equipment on walls, acetylene tanks, fluorescent light overhead, smoke drifting. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip C — S44c (The Workshop Exterior)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Slow zoom out, exterior establishes |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/raw/sanayi_gece.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out from the "Kaynakci Hikmet" workshop entrance at night. Warm light spills from inside, tire stacks on the right, oil-stained asphalt glistening, city skyline glowing in the distance. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip D — S44d (The Widest Frame — Final Gong)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A) — Final frame, maximum distance, the gong |

**Assets Required:**
- **Start Frame:** `episode-03/04_visuals/raw/sanayi_gece.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Widest framing - the sanayi sitesi stretches into night, warm light from the workshop doorway, tire stacks, dark industrial silhouettes against the city skyline. Everything slowly fades darker. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

## BEAT SYNC NOTES

| Timestamp | Musical Event | Required Visual Action | Clip |
|---|---|---|---|
| 0:00 | Spoken word begins — a cappella | S01a: Zoom begins, domestic interior breathes | S01a |
| 0:18 | Narration intensifies | S02a: Cut to argument — defiance | S02a |
| 0:35 | "Gitme dedim" weight | S03: Departure — door swings, light floods | S03 |
| 0:48 | Philosophical weight | S04: Model Selection Screen — thesis shot (Multi-Clip: wide + screen close-up) | S04a, S04b |
| 1:11 | Hammond Organ pad enters — music begins | S06: Cut to airplane — journey starts | S06 |
| 1:40 | Verse 1 — "Rûmî dedi anda dondu" | S08: Airport arrivals — naive energy | S08 |
| 1:51 | Verse 2 — "Gitme dedim, dinlemedi" | S09: City street — warning tone | S09 |
| 2:02 | Chorus 1 — lush synth pad entry | S10: City square picnic — first divine verdict | S10 |
| 2:17 | "Yerken meydan dayağını" | S12: Beating on rhythmic accent | S12 |
| 2:23 | Instrumental 1 — Saz/Guitar call & response | S13a: Cut to dolmuş — travel transition begins | S13a |
| 2:43 | Verse 4 — "Güç bela doğuya kaçtı" | S14: Cut to wedding — location shift | S14 |
| 2:49 | "Öptü mermi yanağını!" | S15: Bullet graze spark on this lyric | S15 |
| 2:56 | Chorus 2 — synth pad re-entry | S16: Amber light shift — mentor atmospheric | S16 |
| 3:08 | Instrumental 2 — Saykodelik saz begins | S17a: Bus ride begins — landscape shift | S17a |
| 3:40 | Verse 5 — "Kuzeye sürdü yolunu" (faster) | S19: Car brakes screech — energy spikes | S19 |
| 3:50 | "Maganda kırdı kolunu" | S20: Collar grab — peak confrontation | S20 |
| 4:01 | Instrumental 3 — short bridge | S21: Quick Alanya establishing cut | S21 |
| 4:08 | Verse 6 — "Güney sıcak, her yer tuzak" | S22: Tourist strip — seduction begins | S22 |
| 4:31 | Chorus 3 — EXPLOSIVE | S24: Amber verdict over Alanya | S24 |
| 4:41 | Moog arpeggio — Dönence atmosphere | S25a: Highway underpass — liminal shift | S25a |
| 5:04 | Verse 7 — darbuka accents enter | S26a: Receipt cascade begins | S26a |
| 5:45 | Chorus 4 — synth pad | S28: Amber from below | S28 |
| 6:09 | "Metâl gövde de ellendi" | S30: Hand touches chrome — trigger | S30 |
| 6:14 | "Topladı tas tarağını!" | S31: Escape bolt — running begins | S31 |
| 6:19 | Chorus 5 entry | S32: Running continues over chorus | S32 |
| 6:28 | "Kıldan ince sıratıydı" | S33: Giant Robotiko on bridge — reverse forced perspective | S33 |
| 6:35 | "Kaydırdılar ayağını" | S34: The slip — foot loses traction | S34 |
| 6:42 | "Metrobüste fortladılar" | S35: Metrobüs chaos entry | S35 |
| 6:47 | "Örtü gibi katladılar" | S36: Folding moment — peak humiliation | S36 |
| 6:53 | Chorus 6 — EXPLOSIVE final | S37: Amber flood in metrobüs | S37 |
| 7:02 | Outro — "Fibulam nedir bu hâller?" | S38: Mentor on overpass — fourth wall | S38 |
| 7:14 | "Kazdı onun toprağını" | S39: Empty overpass — absence | S39 |
| 7:27 | Finale — fuzz guitar solo begins | S40: Ambulance — jarring scene change | S40 |
| 7:40 | Guitar solo builds | S41: Stretcher into workshop | S41 |
| 7:52 | Solo peak | S42: Welder-doctor assessment | S42 |
| 8:07 | Synthesizer sustain | S43: Grease IV drip — intimacy | S43 |
| 8:20 | Guitar fades, instruments thin | S44a: Zoom out begins — the exhale | S44a |
| ~8:40 | Final Gong | S44d: Widest frame — darkness, gong | S44d |

---

## COVERAGE SUMMARY

| Metric | Value |
|---|---|
| **Total music duration** | 524s |
| **Total generated clip duration** | 545s |
| **Coverage ratio** | 104.0% |
| **Total clips** | 54 |
| **Clips from existing images** | 54 |
| **Clips needing new images** | 0 |

### Coverage Breakdown by Strategy

| Strategy | Shots | Clips | Generated Duration | Notes |
|---|---|---|---|---|
| **Direct** | 25 | 25 | 215s | Single clips, trim excess in CapCut |
| **Speed Ramp** | 11 | 11 | 110s (→145s after ramp) | 0.67×–0.91× slowdown |
| **Multi-Shot** | 7 | 16 | 160s | Same source image, all Kling 3.0, one continuous video |
| **Multi-Clip** | 1 | 2 | 20s | Different tools (S25: Kling 3.0 + 2.5T), separate generations |
| **TOTAL** | **44** | **54** | **545s** | **104.0% coverage** |

### New Images Required

None. All 54 clips use existing selected images. Multi-Shot segments reuse their parent scene's source image with different camera moves providing visual variety.

### Supplementary Images

No supplementary images flagged. If during video generation any sub-clip produces unsatisfactory results from the shared source image, a supplementary image can be generated at that time using the visual prompt from `ep03_visual_prompts_v02.md` with adjusted framing.

---

## DIRECTOR'S NOTES

### Duration Coverage Philosophy

EP03 covers 524 seconds of music with 54 clips generating 545 seconds of raw footage (104% coverage). The surplus provides editing flexibility in CapCut — every scene has enough material to trim, extend, or overlap transitions without gaps.

Three strategies distribute the coverage:
1. **Direct (25 clips):** Where tool output naturally matches scene duration. Quick scenes (5s beating, 5s metrobüs) and standard scenes (10s verses).
2. **Speed Ramp (11 clips):** For 11–15s scenes where slowdown enhances the moment. The spoken intro benefits from near-stillness; the grease IV benefits from hypnotic drip-speed.
3. **Multi-Shot (7 scenes → 16 segments):** Same source image + all Kling 3.0 → one continuous video (max 15s per batch). Each segment has a different camera move for visual variety. Smoother transitions, lower credit cost.
4. **Multi-Clip (1 scene → 2 clips):** S25 only — different tools (Kling 3.0 + 2.5T), generated as separate videos.

### Motion Strength Arc

Average: 4.0 — within the EP01-03 target band (4–5).

```
S01-S05 (Spoken Intro):     1-2  ██░░░░░░░░  Barely breathing
S06-S07 (Airplane):         3-4  ████░░░░░░  Building, anticipation
S08-S09 (Arrival):          5    ██████░░░░  Naive energy
S10-S12 (Dönerci/Beating):  4-6  ██████░░░░  First trial spike
S13 (Dolmuş):               3-5  ██████░░░░  Travel transition
S14-S15 (Wedding/Gunfire):  5-6  ████████░░  Festive + spark
S16 (Amber):                3    ████░░░░░░  Atmospheric mola
S17-S18 (North):            3-5  ██████░░░░  Travel landscape
S19-S20 (Maganda):          5-7  ████████░░  Sudden violence
S21-S23 (South/Touts):      5-6  ████████░░  Seduction energy
S24-S25 (Amber/Underpass):  2-5  ██████░░░░  Verdict + liminal
S26-S27 (Nightclub):        4-6  ████████░░  Comedy + aftermath
S28 (Amber Below):          5    ██████░░░░  Atmospheric chorus
S29-S31 (Cinci Hoca):       4-7  ████████░░  Dread → panic
S32 (Running):              7    ████████░░  Full sprint
S33-S34 (Bridge/Slip):      5-6  ████████░░  Vertigo → fall
S35-S36 (Metrobüs):         7-8  ██████████  PEAK chaos + fold
S37 (Amber Flood):          6    ████████░░  Supernatural chorus
S38-S39 (Outro):            2-3  ████░░░░░░  Slowing, emptiness
S40-S41 (Sanayi Action):    4-5  ██████░░░░  Jarring transition
S42-S43 (Healing):          2-3  ████░░░░░░  Intimate stillness
S44a-d (Zoom Out):          1-2  ██░░░░░░░░  The exhale → silence
```

**Peak:** S36 (Folded Up) at motion 8 — the most humiliating moment.
**Trough:** S44c-d (Final Zoom Out) at motion 1 — maximum stillness before the Gong.

### Spoken Intro Strategy (71s, S01–S05)

The 71-second a cappella spoken intro is EP03's longest low-energy section. Five scenes at motion strength 1–2. The approach: atmospheric breathing (lamplight flicker, dust motes, steam, staff glow) provides subtle visual interest while maintaining the documentary stillness demanded by the voiceover. Speed ramp on S03 stretches the contemplative moment. S04 (Model Selection Screen) is a Multi-Clip: S04a (wide shot of Mentor at CRT, 5s Kling 2.5T) + S04b (screen close-up, 8s CapCut-only — static image with cursor animation highlighting "Guru" selection). S04b bypasses video generation entirely for precise text control.

### Running Sequence (S29–S33)

The running thread from cinci hoca escape through the Bosphorus Bridge maintains directional consistency:
- S31: Handheld burst (exit) — directional right
- S32: Pan Right (running) — directional right
- S33: Slow Zoom In (bridge approach) — forward momentum

All three use Kling 3.0 for reliable camera movement execution. The Pan Right across S31–S32 creates a continuous visual flow, broken only by S33's zoom-in as momentum shifts from horizontal sprint to vertical vertigo.

### Finale Deceleration (S40–S44, 77s)

The 77-second finale follows a deliberate motion strength deceleration: 5 → 4 → 3 → 2 → 1. This mirrors the emotional arc from jarring ambulance arrival to contemplative workshop healing to silent zoom-out.

S44's four segments form the episode's closing breath, generated as 2 Multi-Shot batches:
- **Batch 1 (S44a+S44b):** IV + bench → workshop wide (personal → spatial)
- **Batch 2 (S44c+S44d):** through door → sanayi exterior (transitional → cosmic — Final Gong)

Multi-Shot produces smoother transitions within each pair than separate generations would.

### Mentor HYBRID Presence

EP03's unique mentor model:
- **Physical:** S01–S05 (Spoken Intro — domestic argument, departure, computer, close-up) and S38 (Outro — overpass fourth wall break)
- **Atmospheric:** S16, S24, S28, S37 (Choruses — amber light, staff shadow only, no physical figure)
- **Motion prompt protection:** All atmospheric mentor scenes include explicit language: "maintain as a shadow with no visible source, do not resolve into a physical figure"

### Giant Bridge (S33–S34)

The "kıldan ince sırat" metaphor is expressed through reverse forced perspective — Robotiko towers over the Bosphorus Bridge like a giant, making the vast bridge look fragile beneath him. Scale inversion: the mighty giant falling from a structure he dwarfs. S33 uses Slow Zoom In to emphasize the scale contrast. S34 uses Tilt Down to follow the fall direction. The effect is visually striking and unique — accepted as creative choice over literal miniature.

### Tool Budget Efficiency

First attempt: ~3,300cr Kling + ~250cr Seedance + Free Veo = ~3,550cr total.

**Kling AI (4,500cr):** 73% spent on first attempt. ~1,200cr remaining = ~15 retakes at 10s. Budget is TIGHT — prioritize Multi-Shot batching (8 pairs, saves ~640cr if pricing is per-batch not per-segment). With Multi-Shot: ~1,840cr remaining = ~23 retakes.

**Seedance (1,200cr):** 21% spent. ~950cr remaining = generous retake capacity for the 6 character clips.

**Optimization levers if budget runs tight:**
1. Multi-Shot all 8 candidate pairs (highest impact)
2. Shift borderline static clips from Kling 3.0 to Seedance where character content allows
3. Accept first-take results on low-priority clips (atmospheric, transition shots)

---

## APPROVAL STATUS

- [ ] Camera moves reviewed and approved
- [ ] Motion prompts reviewed and approved
- [ ] Tool assignments reviewed and approved
- [ ] Beat sync points reviewed and approved
- [ ] Coverage meets ≥ 95% target: **104.0%** ✅
- [ ] Ready for video generation

> ⚠️ This motion script must be approved by the human before any video generation begins.

---

*"Anadolu sabır dağıtmaz. Dayanıklılığı yoklar."*
*(Anatolia does not distribute patience. It tests endurance.)*
