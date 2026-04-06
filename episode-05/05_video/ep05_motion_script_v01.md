# VIDEO PRODUCTION SHEET (KLING / VEO / SEEDANCE)
> **Version:** v01 | Skill: `_skills/robotiko-motion-script/SKILL.md`
> **Generated:** 2026-04-02
> This template is auto-populated by Claude. Do not fill manually.
> For video generation strategy rules, refer to `_management/pipeline_rules.md`

---

## PRE-GENERATION CHECKLIST

- [x] `episode-05/03_direction/ep05_dramaturgy_v01.md` → APPROVED scene breakdown (32 scenes)
- [x] `episode-05/04_visuals/raw/` → All 33 scene images confirmed (1.png–32.png + 15a.png/15b.png)
- [x] `episode-05/02_music/ep05_musical_metadata.json` → Beat sync reference (122 BPM, E Minor, 267s)
- [x] `_management/master.md` → Tone, station, energy arc
- [x] `_assets/cast/character_profiles.json` → Phase 2: Destruction visual state
- [x] `_memory/lessons.md` → Anti-spawn guard, motion prompt simplicity, character movement direction, crowd micro-motion

> ⚠️ All 33 scene images exist in `episode-05/04_visuals/raw/` — approved by human.
> ⚠️ Motion script must be approved by human before any video generation begins.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP05 |
| **Title** | First Love / Blue Screen |
| **Station** | The Inspired Self (but misread) |
| **Dominant Energy** | Comedy-to-tragedy arc: kinetic funk (Acts 1-2) → desolate collapse (Act 3) |
| **Total Shots** | 32 |
| **Total Clips** | 32 |
| **Total Duration** | 4:27 (267s) |

---

## VIDEO STRATEGY REFERENCE

| Mode | When to Use | Input | Duration |
|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, no transformation | 1 image | 5s or 10s (tool-dependent) |
| **B — Start/End Keyframes** | Transformations, morphing, travel, character state changes | 2 images | 5s or 10s |

**Duration Coverage Strategy:**

| Scene Duration | Strategy | Clip Count | Notes |
|---|---|---|---|
| ≤ 5s | **Direct** | 1 × 5s | Trim excess in CapCut |
| 6–10s | **Direct** | 1 × 10s | Trim in CapCut |
| 11–15s | **Speed Ramp** | 1 × 10s + slow-mo (max 1.5×) | |
| 16–30s | **Multi-Clip** | ⌈duration / 10⌉ clips | Each sub-clip gets own camera move |
| 30s+ | **Multi-Clip** | ⌈duration / 10⌉ clips | May need supplementary images |

**Motion Strength Scale:** 1 = Barely breathing / 5 = Cinematic drama / 10 = Chaos and disintegration

---

## TOOL ASSIGNMENT SUMMARY

### Tool Distribution

| Tool | Clips | Credits Used | Budget | Buffer | Assignment Logic |
|---|---|---|---|---|---|
| **Kling 3.0** | 20 | N/A (Kling credits) | Kling pool | — | Camera movement shots, Mode B, character close-ups requiring motion |
| **Kling 2.5 Turbo** | 1 | N/A (Kling credits) | Kling pool | — | S32 only — 13s scene exceeds Veo 8s + 1.5× speed ramp limit |
| **Seedance 1.0** | 4 | 200cr (4×50cr) | 1200cr/mo | 1000cr (83%) | Character-focused static shots where figure fidelity is critical |
| **Google Veo** | 7 | Free (daily limit) | Free tier | — | Static atmospheric scenes, simple compositions, ≤9s scenes or near-still speed ramps |
| **TOTAL** | **32** | — | — | — | — |

> **Seedance budget note:** 4 clips × 50cr (10s) = 200cr. Remaining: 1000cr (83% buffer). Highly retake-safe.
> **Veo daily limit note:** 7 Veo clips may require 2-3 days of generation. Plan accordingly.

### Assignment Rules Applied

1. **Mode B → Kling 3.0** — S15 is the only Mode B shot (hacker mask → cloud cutting). Keyframe support mandatory.
2. **Camera movement shots → Kling 3.0** — All zoom, dolly, pan, crane shots assigned to Kling 3.0.
3. **Static atmospheric scenes → Veo** — Free tier saves Kling/Seedance credits. S04, S08, S09, S11 (simple static compositions), S26, S30, S31 (Act 3 near-still scenes).
4. **S32 → Kling 2.5 Turbo** — 13s scene requires 10s clip (8s Veo + 1.5× = 12s max, insufficient). Only Kling 2.5 Turbo can cover this.
5. **Critical character moments → Seedance 1.0** — S20 (Album Cover), S23 (folders flying action), S25 (electric arcs spectacle), S28 (eye projection): character-focused static shots where figure fidelity and complex effects demand maximum quality.
6. **Veo speed ramp scenes** — S04, S26 (8s → 9s at 0.89×, barely perceptible), S31 (8s → 11s at 0.73×, near-still scene so 1.37× slowdown invisible).

### Clips by Tool

**Kling 3.0 (20):** S01, S02, S03, S05, S06, S07, S10, S12, S13, S14, S15, S16, S17, S18, S19, S21, S22, S24, S27, S29

**Kling 2.5 Turbo (1):** S32

**Seedance 1.0 (4):** S20, S23, S25, S28

**Google Veo (7):** S04, S08, S09, S11, S26, S30, S31

---

## MOTION SCRIPT

---

### ACT 1: THE ENCOUNTER (0:00 – 1:31)

---

### SHOT S01 — Searching Eyes (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:00–0:08 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Blues lick entry — clean guitar with chorus effect, smooth bass line, light drums. Low energy groove. |
| **Scene Context** | Close-up of Robotiko's face — steady blue eyes from EP04's finale, now scanning and hungry. Phase 2 damage visible. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — camera movement + character close-up |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/1.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android's face. Faint sparks flicker at the right ear socket. Blue eyes pulse with a searching, anticipatory glow. Subtle heat shimmer at the damaged temple crack. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S02 — Supermarket Walk (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:08–0:16 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Smooth bass line + light drums establish the head-nodding groove. |
| **Scene Context** | Wide shot of retro-futuristic supermarket. Robotiko walks through aisle. Sparks catch amber light. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — camera movement + environment walk |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/2.png`

**Camera Move:** Dolly In

**Motion Prompt:**
> The chrome android walks slowly through the supermarket aisle, moving away from camera toward the depth of the shelves. Sparks crackle from his right shoulder. Overhead amber strip lights cast warm pools along the chrome shelving. Faint vapor drifts from the refrigeration unit. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S03 — First Sight (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:16–0:24 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Guitar blues lick peaks — the musical spark matching the visual moment of discovery. |
| **Scene Context** | Robotiko rounds aisle end and sees Robochica through shelves. Profile, fractal shoulder, one amber eye. His eyes widen. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — subtle zoom toward the discovery moment |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/3.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the gap between chrome supermarket shelves. In the foreground, the chrome android freezes, his blue eyes widening. Steam drifts gently from the refrigeration unit. Amber overhead light catches the chrome surfaces warmly. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S04 — System Acceleration (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:24–0:33 |
| **Scene Duration** | 9s |
| **Coverage** | Speed Ramp — 1 × 8s → 9s at 0.89× |
| **Musical Moment** | Head-nodding beat established — groove locked in. Bass and drums in full pocket. |
| **Scene Context** | Close-up of Robotiko frozen mid-step. Chrome food item slips from hand. Sparks increase. Cooling vents hiss. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 8s |
| **Playback Speed** | 0.89× (8s → 9s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Veo (Mode A, ~1080p) — static, atmospheric, free tier saves credits |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/4.png`

**Camera Move:** Static

**Motion Prompt:**
> Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged.
> Action: The chrome android stays in the exact pose pictured. The only motion is a single chrome canister slowly slipping from its mechanical fingers and falling vertically toward the floor. Electrical sparks at the damaged shoulder joints flicker and crackle with increasing frequency. Thin, wispy puffs of white vapor drift slowly from the neck vents. The amber overhead lighting remains constant, reflecting on the chrome surfaces. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.

---

### SHOT S05 — Both in Frame (Direct) ⭐ User Override #1

| Field | Value |
|---|---|
| **Timestamp** | 0:33–0:41 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Don't you walk so slow..." — soft baritone, half-spoken, playful. Verse 1a begins. |
| **Scene Context** | Street scene. Robochica walks slowly, Robotiko watches transfixed. Both in frame. Sparks increase rhythmically. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — pan to follow walking figure |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/5.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Slow pan right following the chrome female android as she walks gracefully along the retro-futuristic sidewalk. The damaged chrome android remains frozen in the right third, his sparks bursting in rhythmic pulses. Warm vapor rises from a sidewalk grate. Amber street lamps cast golden pools. Both figures remain in their exact positions relative to each other. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S06 — Warming Wires (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:41–0:50 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Your name is blazing... burning through the night..." — whispered line endings, building warmth. |
| **Scene Context** | Medium shot of Robotiko watching her pass. Wire shifts from blue to warm hue. Spark from chest crack like a heartbeat. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — subtle zoom into emotional reaction |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/6.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android standing on the sidewalk, his head turned to the right. His blue eyes pulse brighter. A single spark arcs from his chest crack like a mechanical heartbeat. The exposed wire at his chest shifts subtly warmer in hue. Amber street lamp reflections intensify on his chrome. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S07 — The Drool (Direct) ⭐ User Override #2

| Field | Value |
|---|---|
| **Timestamp** | 0:50–0:58 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Your twin reactors... are swelling up the mesh!" — bass gets groovy, funky rhythm. Verse 1b begins. |
| **Scene Context** | ZOOM on Robotiko's face. Oil drips from mouth. Ultra-comic arousal. The drool catches amber light. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — slow zoom into the comedic drool moment |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/7.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android's face. Golden-brown oil drips slowly from the corner of his chrome mouth, catching the warm amber light as it stretches downward. His blue eyes are wide and glazed, flickering with warm pulses. More oil beads at his lower lip. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S08 — Overheating Chest (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:58–1:04 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 8s |
| **Musical Moment** | "Straining the fabric... of your metal flesh!" — funky rhythm continues, bass groove. |
| **Scene Context** | Medium shot of Robotiko's chest. Exposed wires glowing intensely. Heat distortion above shoulders. Steam from neck joints. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 8s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Veo (Mode A, ~1080p) — static atmospheric, free tier saves Seedance credits |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/8.png`

**Camera Move:** Static

**Motion Prompt:**
> Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged.
> Action: The chrome android's torso remains in the exact pose pictured. The exposed analog wires at the chest glow with slowly intensifying heat, pulsing between orange and red. Heat distortion shimmers subtly above the chrome shoulders. Small puffs of white vapor escape from cracks in the neck joints and chassis seams. The warm amber lighting remains constant. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.

---

### SHOT S09 — Peak Arousal (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:04–1:10 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 8s |
| **Musical Moment** | "Mmm... your metal... flesh..." — the moan. Slight pause in groove. Peak Verse 1b. |
| **Scene Context** | Extreme close-up of face. Eyes half-closed. Long slow oil drip. Steam wisps. Steam burst from damaged ear socket. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 8s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Veo (Mode A, ~1080p) — static close-up, atmospheric steam effects, free tier |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/9.png`

**Camera Move:** Static

**Motion Prompt:**
> Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged.
> Action: The chrome android's face remains in the exact pose pictured with half-closed eyes. A long strand of golden-brown oil slowly stretches downward from the lower lip. Thin steam wisps curl upward from both sides of the chrome neck. A single visible puff of white steam bursts from the right ear socket. The warm amber lighting remains constant on all chrome surfaces. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.

---

### SHOT S10 — Cafe Earnestness (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:10–1:17 |
| **Scene Duration** | 7s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "If my Mother... had your electric VIBE..." — keyboard/organ enters. Crooning, smooth. Bridge begins. |
| **Scene Context** | Interior of retro-futuristic cafe. Robotiko at table, leaning forward with earnest intensity. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — slow zoom builds intimacy of his delivery |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/10.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android seated at a small chrome table in the retro-futuristic cafe. He leans forward with earnest intensity, his expression animated and engaged. Warm amber pendant lamp light casts golden reflections on his damaged chrome. The mechanical coffee machine hisses softly in the background. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S11 — Elderly Robot Couple (Direct) ⭐ User Override #3

| Field | Value |
|---|---|
| **Timestamp** | 1:17–1:24 |
| **Scene Duration** | 7s |
| **Coverage** | Direct — 1 × 8s |
| **Musical Moment** | "My dead father... would come back alive!" — melodic singing, keyboard/organ, comedic peak. |
| **Scene Context** | Elderly robot couple in dreamlike setting. Old Man raises cane. Old Woman projects amber energy aura. Imagination filter. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 8s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Veo (Mode A, ~1080p) — static, dreamlike atmospheric, free tier saves Seedance credits |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/11.png`

**Camera Move:** Static

**Motion Prompt:**
> Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged.
> Action: Both elderly chrome robots remain seated in their exact positions. The male robot slowly raises his chrome walking cane with a gentle upward motion. The female robot's warm amber energy aura pulses slowly and hypnotically outward from her chassis. Soft diffused dreamlike edges throughout. The warm amber lighting remains constant. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.

---

### SHOT S12 — Dreamy Satisfaction (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:24–1:32 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Yeah... he'd come back alive..." — melodic singing, organ swell. Bridge ending. |
| **Scene Context** | Back to Robotiko in cafe. Pleased with his metaphor. Slight smile, leaning back. Warmth peak of Act 1. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — slow zoom out reveals contentment and cafe life |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/12.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out from the chrome android leaning back contentedly in a chrome chair, one arm draped over the back. A satisfied smile on his chrome face. The warm amber pendant lamps of the retro-futuristic cafe glow around him. Soft-focus robot figures visible at distant tables. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### ACT 2: THE DECLARATION (1:32 – 3:23)

---

### SHOT S13 — robochica_1 Tattoo (Direct) ⭐ User Override #4

| Field | Value |
|---|---|
| **Timestamp** | 1:32–1:40 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "I laser-etched your name on my metal shell!" — chorus entry, soulful rock, HIGH energy. |
| **Scene Context** | Close-up of inner forearm. Laser from fingertip etches "robochica_1" in amber-gold. The "_1" must be legible. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — zoom into the etching detail |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/13.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android's inner forearm. An amber laser beam from his fingertip actively etches glowing lines into the chrome surface. The amber-gold text burns bright as each character is inscribed. The freshly etched lines glow intensely then cool to a permanent mark. Amber glow is the primary light source. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S14 — Memory Cell Embedding (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:40–1:48 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Embedded it deep in a memory cell!" — chorus continues, passionate but controlled. |
| **Scene Context** | Robotiko presses finger to temple. Translucent data visualization around head — punch-card patterns, vacuum-tube glow. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — zoom into data visualization effect |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/14.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android pressing a finger to his temple. Translucent streams of retro-futuristic data flow outward around his head — punch-card patterns and vacuum-tube amber glow spiraling in geometric structures. One highlighted memory cell glows brighter in warm amber. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S15 — Cloud Release (Direct) ⭐ User Override #5

| Field | Value |
|---|---|
| **Timestamp** | 1:48–1:56 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "I didn't download you from the Cloud above..." — chorus continues, the "Cloud" lyric matches the literal visual. |
| **Scene Context** | Wide shot — seated at workstation, the cord is severed and the blue cloud with the data center drifts upward like a released kite. The moment of liberation from passive consumption. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — single physical motion (cloud drifting upward), character close-up detail |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/15b.png`

> **Note:** Originally planned as Mode B with 15a → 15b keyframes, but the environment shift from foggy close-up (15a) to full workstation (15b) was too complex for keyframe interpolation. Simplified to Mode A using only 15b. 15a is preserved as a dramaturgy reference but not used in this clip.

**Camera Move:** Static

**Motion Prompt:**
> The chrome-mesh masked figure at the retro-futuristic workstation remains in the exact pose pictured. The thick cord extending from his hand to the blue cloud above severs at the cut point with a final burst of sparks. The fluffy blue cloud, with the miniature data center on top, slowly drifts upward and out of the top of the frame, the severed upper half of the cord trailing behind it like the string of a released kite. The lower stump of the cord remains in the figure's grip. CRT monitors glow steadily in the background. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S16 — Hacking the Mainframe (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:56–2:05 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "I hacked the mainframe to code this love!" — chorus peak energy, final chorus line. |
| **Scene Context** | Robotiko at massive mainframe. Wires plugged into machine. CRT screens show hearts and waveforms. Hands dance across switches. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — zoom out reveals massive mainframe scale |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/16.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out revealing the massive retro-futuristic mainframe stretching floor to ceiling. The chrome android's hands dance urgently across mechanical switches. Reel-to-reel tape drives spin. Rows of indicator lights blink in rhythmic patterns. CRT screens pulse with warm amber waveforms. Vacuum tubes glow throughout the machine. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S17 — Night Walk Entry (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 2:05–2:16 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | Guitar solo entry — slow blues, clean tone. Crying gently, sexy bends. Comedy pauses. |
| **Scene Context** | Two chrome figures walk into vast iron vault. Massive arched walls, broken skylights, amber light shafts, polished chrome floor. Walking 3-4 body-widths apart. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.91× (10s → 11s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — dolly forward into vast space |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/17.png`

**Camera Move:** Dolly In

**Motion Prompt:**
> Slow dolly forward into the vast colossal iron vault. Two chrome figures walk side by side, separated by several body-widths of distance. Massive iron arched walls stretch into deep shadow above. Shafts of pale amber light fall through broken skylights onto the polished chrome floor. Dust motes drift through the light beams. Their reflections stretch beneath them on the mirror surface. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S18 — Closing Distance (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 2:16–2:27 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | Blues solo continues — crying gently, sexy guitar bends. The emotional heart of the solo. |
| **Scene Context** | Two figures continue walking. Distance closed to 2 body-widths. Sparks leave amber trail on floor. Chrome reflections. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.91× (10s → 11s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — pan following the walking pair |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/18.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Slow pan right following two chrome figures walking through the colossal iron vault. The distance between them has closed. The damaged chrome android's sparks leave a trail of tiny amber lights on the polished floor behind him. The chrome female android's gold wires catch the skylight and glow softly. Their reflections stretch on the mirror floor below. Warm amber traces on the distant walls. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S19 — Inner Light / Kintsugi Preview (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:27–2:37 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Blues solo — most emotional bend, sustained note. The apex of feeling. |
| **Scene Context** | Close-up of Robotiko's cracked chest. A few thin beams of warm amber light seep through fractures from within. Subtle, temporary, unnoticed. Unconscious Kintsugi preview. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — intimate slow zoom into the glowing cracks |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/19.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android's cracked chest. A few thin beams of warm amber light seep through the fractures from within, casting delicate lines on the iron vault floor. The light pulses very gently — fragile, quiet, temporary. The surrounding iron vault is cool blue-gray. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S20 — Album Cover Shot (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:37–2:45 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Blues solo — sustained, emotional, warm. THE defining musical moment. |
| **Scene Context** | THE poster image. Wide shot. Two figures in vast iron vault. Amber light shafts. Chrome floor reflections. Amber horizon. Frank Frazetta scale. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p) — static, poster-quality, character pair fidelity paramount |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/20.png`

**Camera Move:** Static

**Motion Prompt:**
> Two chrome figures stand close together in the vast colossal iron vault. Dust motes drift slowly through shafts of amber light falling from broken skylights above. Their reflections shimmer on the polished chrome floor. Minimal movement — the epic stillness is the power. Faint amber glow on the distant horizon. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S21 — Return to Reality (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:45–2:50 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s |
| **Musical Moment** | Blues solo ending — final clean guitar notes fading. Transitional. |
| **Scene Context** | Iron vault dissolves. Walls become translucent. Reality reasserts. Last amber shaft lingers. Dream ending. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — zoom out as the dream space dissolves |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/21.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> The chrome android stands still in the exact pose pictured at the threshold between two worlds already visible in the frame — warm amber iron vault on the left, cool retro-futuristic office with CRT terminals on the right. Slow zoom out keeping the same composition intact. Dust motes drift gently through the amber shaft of light on the left. The fluorescent light on the right flickers subtly. Both environments remain exactly as pictured — do not transform, morph, or replace either side. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S22 — System Saint with Folders (Direct) ⭐ User Override #6

| Field | Value |
|---|---|
| **Timestamp** | 2:50–2:58 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "I was a system saint... playing it so cool..." — bass only, intimate. Verse 2a begins. |
| **Scene Context** | Retro-futuristic office. Robotiko holds armful of Windows-style file folders. Model AI employee. Then he sees Robochica at a distant desk. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — dolly in toward his discovery moment |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/22.png`

**Camera Move:** Dolly In

**Motion Prompt:**
> A continuous, slow camera push-in toward the chrome android standing at his workstation in the retro-futuristic office, holding a tall stack of yellow file folders against his chest. He remains in the exact pose pictured, folders held firmly. Then, he slowly and deliberately turns his head toward the left side of the frame (screen-left), looking directly toward the golden-brass female android standing in the distant background among the rows of desks. His glowing blue eyes lock onto her. CRT terminals glow steadily with green phosphor text on the chrome desks around him. Fluorescent overhead lighting with warm amber accents remains constant. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything exactly as pictured.

---

### SHOT S23 — Folders Flying (Direct) ⭐ User Override #6 continued

| Field | Value |
|---|---|
| **Timestamp** | 2:58–3:06 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Saw your wireframe... and broke every rule..." — bass builds, groove returning. |
| **Scene Context** | Robotiko THROWS folders. Yellow folder icons flying, papers exploding, data sheets like confetti. Eyes locked on Robochica. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p) — static camera, character action with flying objects |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/23.png`

**Camera Move:** Static

**Motion Prompt:**
> Yellow file folders and papers scatter through the air in all directions — tumbling, spinning, fluttering down like confetti. The chrome android's arms are still extended from the throw. Data sheets and punch-cards drift through the fluorescent light. His blue eyes are bright, locked on something across the office. Papers settle slowly on chrome desks around him. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S24 — Bright Red Body (Direct) ⭐ User Override #7

| Field | Value |
|---|---|
| **Timestamp** | 3:06–3:15 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Now I'm fully turned on..." — groove returns, music builds. Verse 2b begins. |
| **Scene Context** | Full body — Robotiko turned BRIGHT RED. Full-body overheating. Rust glows orange. All wires red. Heat distortion. Ecstatic expression. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — slow zoom into the incandescent figure |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/24.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android standing with arms slightly spread. His entire chassis glows bright red with intense overheating. Heat distortion shimmers around his silhouette. His exposed wires pulse with red-hot intensity. The red glow radiating from his body paints the surrounding space in warm crimson. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S25 — High-Voltage Fool (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:15–3:24 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "A high-voltage fool! Oh yes, a high... voltage... fool...!" — playful growl, comedy PEAK. |
| **Scene Context** | Tighter on body. Electricity ARCS across red-hot chassis. Blue-white bolts between joints and cracks. The LAST moment of pure joy. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 8 |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p) — static, character close-up, electric arc spectacle |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/25.png`

**Camera Move:** Static

**Motion Prompt:**
> Electricity arcs visibly across the chrome android's red-hot upper body — blue-white bolts jumping between joints, cracks, and exposed wires. Each bolt illuminates the surrounding chrome in sharp white-blue flashes against the deep red glow. The arcs crawl and leap unpredictably across the chrome surface. Maximum visual intensity. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### ACT 3: THE CRACK (3:24 – 4:27)

> **Post-production note:** The Kodachrome → Blue Screen color transition beginning at S26 will be handled by CapCut color grading. Motion prompts describe atmosphere and movement ONLY — no color shift instructions.

---

### SHOT S26 — Tired But Happy (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:24–3:33 |
| **Scene Duration** | 9s |
| **Coverage** | Speed Ramp — 1 × 8s → 9s at 0.89× |
| **Musical Moment** | Outro begins — funky bass riff fading. "Soft spoken, tired but happy." |
| **Scene Context** | Robotiko's room. Sits on cot edge. Heat fading back to chrome. Content, tired. Single amber desk lamp. The warmth begins to leave. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 8s |
| **Playback Speed** | 0.89× (8s → 9s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Veo (Mode A, ~1080p) — static, atmospheric stillness, free tier saves credits |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/26.png`

**Camera Move:** Static

**Motion Prompt:**
> Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged. Do not add water drops, leaks, dripping, moisture, or any decay elements that are not in the source image.
> Action: The chrome android remains seated on the edge of the cot in the exact pose pictured. The only motion is a barely perceptible rise and fall of his chest. His exposed analog wires pulse very faintly with residual warmth. The amber desk lamp glows steadily, warm and quiet. The ceiling, walls, and all surfaces remain completely static and dry. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.

---

### SHOT S27 — The Searching (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:33–3:42 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Bass riff continuing to fade. Energy draining from the track. |
| **Scene Context** | Same room. Leaned forward, elbows on knees. Eyes scan the room — searching. Desk lamp flickers. Warmth drops. Sparks now look like damage again. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — slow zoom builds tension as he searches |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/27.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android leaned forward on the cot, elbows on knees. His blue eyes scan the room slowly. The amber desk lamp flickers, its light unsteady. Faint sparks at his damaged joints — small, pathological, no longer celebratory. The room feels empty. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S28 — Eye Projection (Direct) ⭐ User Override #8

| Field | Value |
|---|---|
| **Timestamp** | 3:42–3:50 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "If we don't sync..." — THE MASK DROP. Vocal change: small, fragile, afraid. Outro vocals begin. |
| **Scene Context** | Close-up. From his eyes, a PROJECTION emanates — Robochica's holographic image. Room is cold. Projection is the only warm light. EP03 callback. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p) — static, character close-up, complex projection light effect |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/28.png`

**Camera Move:** Static

**Motion Prompt:**
> The chrome android remains completely motionless in the exact pose pictured — head fixed, eyes fixed, the twin amber beams from his eyes remain locked in position pointing straight ahead. The projected golden female figure in front of him stays in the exact same spot. The only motion is a gentle, slow pulsing of the projection's amber glow — brightening and dimming rhythmically, like a heartbeat of light. The cold dark room around them remains completely static. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S29 — Projection Dying (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:50–3:58 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "I am beyond repair..." — vulnerable, afraid. The comedy armor is completely gone. |
| **Scene Context** | Eye projection FLICKERS. Scan lines. Robochica's form fragments, pixelates. Robotiko reaches toward it — fingers pass through light. Cold blue invades. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — slow zoom into the desperate reaching moment |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/29.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android reaching both hands toward a flickering, dying holographic projection. The projection fragments — scan lines cut across the figure, the form pixelates and dissolves at the edges. His chrome fingers pass through the light, grasping nothing. The warm amber light of the projection stutters and dies. Cold blue creeps in from the edges of the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S30 — Blue Screen (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:58–4:03 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 8s |
| **Musical Moment** | "System Fatal... Infinite Despair..." — the mask is completely gone. Low energy. |
| **Scene Context** | Projection dead. Alone in cold blue light. Desk lamp dead. CRT shows blank blue. The "robochica_1" tattoo visible as a scar in blue light. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 8s |
| **Motion Strength** | 1 |
| **Recommended Tool** | Veo (Mode A, ~1080p) — static, near-still, cold blue atmosphere, free tier |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/30.png`

**Camera Move:** Static

**Motion Prompt:**
> Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged.
> Action: The chrome android remains in the exact pose pictured, nearly motionless. The only motion is a very faint, slow flicker in the CRT terminal's blue glow, casting subtle shifting reflections on the chrome wall surfaces. No character movement. Total stillness. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.

---

### SHOT S31 — Beyond Repair (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 4:03–4:14 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 8s → 11s at 0.73× |
| **Musical Moment** | "Beyond... Repair..." — whispered, barely audible. Near-silence. The seed of EP06. |
| **Scene Context** | Extreme close-up. Eyes filling frame. Blue flickers between dead blue and complete darkness. No sparks. A machine that has stopped processing. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 8s |
| **Playback Speed** | 0.73× (8s → 11s — 1.37× slowdown, near-still scene makes it invisible) |
| **Motion Strength** | 1 |
| **Recommended Tool** | Veo (Mode A, ~1080p) — static, lingering, near-still, free tier |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/31.png`

**Camera Move:** Static

**Motion Prompt:**
> Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged.
> Action: Extreme close-up of the chrome android's eyes remains in the exact framing pictured. The only motion is the dying blue light in his irises — flickering weakly, stuttering between a faint glow and complete darkness. Each return of blue light is weaker than the last. No other movement anywhere in the frame. Absolute stillness. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.

---

### SHOT S32 — Power Down (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 4:14–4:27 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Instrumental end — slow-funky bass riff fading to silence. The final breath. |
| **Scene Context** | The blue flickers one final time and goes dark. Chrome face briefly visible. Then black. Not a fade — a powering down. EP06 begins in this darkness. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.77× (10s → 13s) |
| **Motion Strength** | 1 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — static, the final breath, near-darkness |

**Assets Required:**
- **Start Frame:** `episode-05/04_visuals/raw/32.png`

**Camera Move:** Static

**Motion Prompt:**
> Near-total darkness. The faintest ghost of chrome catches one final, weak flicker of cold blue light — then nothing. A single faint horizontal scan line, barely perceptible, crosses the darkness. The screen powers down. Deep black fills the composition. Absolute silence. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

## BEAT SYNC NOTES

| Timestamp | Musical Event | Required Visual Action | Clip Reference |
|---|---|---|---|
| 0:00 | Blues lick entry — clean guitar | S01 opens with searching eyes, match the first guitar note with the zoom beginning | S01 |
| 0:33 | Verse 1a — "Don't you walk so slow" | CUT to S05 (both in frame) on first vocal entry | S05 |
| 0:50 | Verse 1b — bass gets funky | CUT to S07 (drool close-up) on the bass groove shift | S07 |
| 1:10 | Bridge — keyboard/organ enters | CUT to S10 (cafe) on organ entry | S10 |
| 1:17 | "My dead father would come back alive!" | CUT to S11 (elderly couple) on the word "father" | S11 |
| 1:32 | Chorus entry — full band, HIGH energy | CUT to S13 (tattoo) on chorus downbeat — the laser activation matches the energy surge | S13 |
| 1:48 | "Cloud" lyric | CUT to S15 (hacker mask → cloud) on the word "Cloud" | S15 |
| 2:05 | Guitar solo begins — clean blues tone | CUT to S17 (night walk) — the tonal shift from chorus energy to solo intimacy | S17 |
| 2:27 | Most emotional guitar bend | S19 (inner light) — amber light pulse should sync with the sustained bend | S19 |
| 2:37 | Sustained solo note — emotional apex | S20 (album cover shot) — the stillness of the wide shot matches the sustained note | S20 |
| 2:45 | Solo ending — guitar fading | S21 (return to reality) — dissolving space matches fading guitar | S21 |
| 2:50 | Verse 2a — bass only, intimate | CUT to S22 (office, folders) — the quiet intimacy matches bass-only arrangement | S22 |
| 2:58 | Bass builds | CUT to S23 (folders flying) — the energy return triggers the throw | S23 |
| 3:06 | "Fully turned on" — groove returns | CUT to S24 (bright red body) — the red ignition matches the groove returning | S24 |
| 3:15 | "High-voltage fool!" — playful growl peak | S25 (electric arcs) — maximum visual spectacle on the comedy peak | S25 |
| 3:24 | **THE TONAL SHIFT** — Outro begins, bass fading | CUT to S26 (tired but happy) — the EXACT moment comedy becomes tragedy. Hard cut to the room. | S26 |
| 3:42 | **THE MASK DROP** — vocal change, small and afraid | CUT to S28 (eye projection) on "If we don't sync..." — the projection begins with the vulnerability | S28 |
| 3:50 | "Beyond repair" — first utterance | S29 (projection dying) — the projection fragments on the word "repair" | S29 |
| 4:03 | Whispered "Beyond... Repair..." | CUT to S31 (eyes close-up) — the whisper syncs with the flickering eyes | S31 |
| 4:14 | Final bass notes fading | S32 (power down) — the last blue flicker dies with the last bass note | S32 |

---

## COVERAGE SUMMARY

| Metric | Value |
|---|---|
| **Total music duration** | 267s |
| **Total generated clip duration** | 278s (21 × 10s + 7 × 8s + 2 × 10s speed ramp + 2 × 8s speed ramp) |
| **Coverage ratio** | 104% (278s / 267s) — excess trimmed in CapCut |
| **Total clips** | 32 |
| **Clips from existing images** | 32 |
| **Clips needing new images** | 0 |
| **Mode A clips** | 31 |
| **Mode B clips** | 1 (S15) |
| **Speed Ramp clips** | 6 (S04: 0.89×, S17: 0.91×, S18: 0.91×, S26: 0.89×, S31: 0.73×, S32: 0.77×) |
| **Average Motion Strength** | 3.8 (Acts 1-2 avg: 4.3, Act 3 avg: 2.7) |

### Duration Verification (Scene-by-Scene)

| Shot | Timestamp | Scene Duration | Clip Duration | Strategy | Speed Factor | Effective Duration |
|---|---|---|---|---|---|---|
| S01 | 0:00–0:08 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S02 | 0:08–0:16 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S03 | 0:16–0:24 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S04 | 0:24–0:33 | 9s | 8s (Veo) | Speed Ramp | 0.89× | 9s |
| S05 | 0:33–0:41 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S06 | 0:41–0:50 | 9s | 10s | Direct | 1× | 10s (trim 1s) |
| S07 | 0:50–0:58 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S08 | 0:58–1:04 | 6s | 8s (Veo) | Direct | 1× | 8s (trim 2s) |
| S09 | 1:04–1:10 | 6s | 8s (Veo) | Direct | 1× | 8s (trim 2s) |
| S10 | 1:10–1:17 | 7s | 10s | Direct | 1× | 10s (trim 3s) |
| S11 | 1:17–1:24 | 7s | 8s (Veo) | Direct | 1× | 8s (trim 1s) |
| S12 | 1:24–1:32 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S13 | 1:32–1:40 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S14 | 1:40–1:48 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S15 | 1:48–1:56 | 8s | 10s | Direct (B) | 1× | 10s (trim 2s) |
| S16 | 1:56–2:05 | 9s | 10s | Direct | 1× | 10s (trim 1s) |
| S17 | 2:05–2:16 | 11s | 10s | Speed Ramp | 0.91× | 11s |
| S18 | 2:16–2:27 | 11s | 10s | Speed Ramp | 0.91× | 11s |
| S19 | 2:27–2:37 | 10s | 10s | Direct | 1× | 10s |
| S20 | 2:37–2:45 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S21 | 2:45–2:50 | 5s | 5s | Direct | 1× | 5s |
| S22 | 2:50–2:58 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S23 | 2:58–3:06 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S24 | 3:06–3:15 | 9s | 10s | Direct | 1× | 10s (trim 1s) |
| S25 | 3:15–3:24 | 9s | 10s | Direct | 1× | 10s (trim 1s) |
| S26 | 3:24–3:33 | 9s | 8s (Veo) | Speed Ramp | 0.89× | 9s |
| S27 | 3:33–3:42 | 9s | 10s | Direct | 1× | 10s (trim 1s) |
| S28 | 3:42–3:50 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S29 | 3:50–3:58 | 8s | 10s | Direct | 1× | 10s (trim 2s) |
| S30 | 3:58–4:03 | 5s | 8s (Veo) | Direct | 1× | 8s (trim 3s) |
| S31 | 4:03–4:14 | 11s | 8s (Veo) | Speed Ramp | 0.73× | 11s |
| S32 | 4:14–4:27 | 13s | 10s | Speed Ramp | 0.77× | 13s |
| **TOTAL** | — | **267s** | **302s** | — | — | **267s** |

**Coverage: 267s / 267s = 100%.** ✅ All seconds accounted for. No gaps.

---

## APPROVAL STATUS
- [ ] **Human reviewed camera moves**
- [ ] **Human reviewed tech strategy (Mode A/B)**
- [ ] **Human reviewed duration coverage**
- [ ] **Human reviewed tool assignments**
- [ ] **Human generated supplementary images (if any)** — N/A (none needed)
- [ ] **Human approved**
- [ ] **Ready for video generation**

> ⛔ Video generation must NOT begin until this document is approved.

---

*"Motion is the breath between the frames. Without it, the image is a photograph. With it, the image is alive."*
*"Would Fibula approve this?"*
