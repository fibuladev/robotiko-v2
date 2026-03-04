# VIDEO PRODUCTION SHEET — EP02: THE TECH GURU'S DOWNFALL
> **Version:** v02 | **Skill:** robotiko-motion-script
> **Generated:** 2026-02-27
> **Supersedes:** ep02_motion_script_v01.md (v01 had 39% coverage gap — see lessons.md)
> For video generation strategy rules, refer to `_management/pipeline_rules.md`

---

## PRE-GENERATION CHECKLIST

- [x] `episode-02/03_direction/ep02_dramaturgy_v01.md` → APPROVED scene breakdown (2026-02-26)
- [x] `episode-02/04_visuals/selected/` → 41 selected images confirmed (including 6 keyframe pairs)
- [x] `episode-02/02_music/ep02_musical_metadata.json` → Beat sync reference (104 BPM, G Major)
- [x] `_management/master.md` → Tone, station, energy arc confirmed

> ⚠️ Motion script must be approved by human before any video generation begins.
> ⚠️ Supplementary images (if flagged) must be generated before video production starts.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP02 |
| **Title** | The Tech Guru's Downfall |
| **Station** | The Commanding Self (Nafs al-Ammara — Arrogance, cracks forming) |
| **Dominant Energy** | Satirical-energetic with cumulative darkening |
| **Total Shots** | 35 (from approved dramaturgy) |
| **Total Clips** | 49 (including sub-clips) |
| **Total Duration** | 7:28 (448s) |
| **BPM** | 104 (constant until War Zone tempo slow at 5:48) |
| **Average Motion Strength** | 4.1 (EP01-03 target: 4-5) |

---

## VIDEO STRATEGY REFERENCE

| Mode | When to Use | Input | Duration |
|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, no transformation | 1 image | 5s or 10s (tool-dependent) |
| **B — Start/End Keyframes** | Transformations, morphing, character state changes | 2 images | 5s or 10s |

**Duration Coverage Strategy:**

| Scene Duration | Strategy | Clip Count | Notes |
|---|---|---|---|
| ≤ 5s | **Direct** | 1 × 5s | Trim excess in CapCut |
| 6–10s | **Direct** | 1 × 10s | Trim in CapCut |
| 11–15s | **Speed Ramp** | 1 × 10s + slow-mo (max 1.5×) | |
| 16–30s | **Multi-Clip** | ⌈duration / 10⌉ clips | Each sub-clip gets own camera move |
| 30s+ | **Multi-Clip** | ⌈duration / 10⌉ clips | May need supplementary images |

**Motion Strength Scale:** 1 = Barely breathing / 5 = Cinematic drama / 10 = Chaos and disintegration

**Strategy Distribution:**
- Direct: 18 shots (18 clips)
- Speed Ramp: 8 shots (8 clips)
- Multi-Clip: 9 shots (23 sub-clips)
- **Total: 49 clips**

---

## TOOL ASSIGNMENT SUMMARY

> Added: 2026-02-28 | Based on tool inventory analysis and credit optimization.

### Tool Distribution

| Tool | Clips | Credits Used | Budget | Buffer | Assignment Logic |
|---|---|---|---|---|---|
| **Kling 3.0** | 36 | ~2,275 | 3,000 | 725 (~10 retakes) | All Mode B + priority Mode A (character, chorus, finale) |
| **Google Veo** | 4 | Free | Free | 2/day | Mode A shots with 8-9s scene duration (natural match) |
| **Seedance 1.0 (CapCut)** | 9 | ~425 | 1,200 | 775 (~15 retakes) | All map/texture shots (1080p, CapCut Pro subscription, budget-efficient) |
| **TOTAL** | **49** | — | — | — | — |

### Assignment Rules Applied

1. **Mode B → Kling only** — All 6 keyframe transformation shots need 1080p for dramatic impact
2. **Map shots → Seedance 1.0** — 9 vintage paper texture shots (1080p, CapCut Pro credits included in subscription)
3. **8s scene match → Veo** — 4 Mode A shots where Veo's 8s output matches scene duration (8-9s)
4. **Everything else → Kling** — 30 Mode A clips at 1080p (opening, locations, choruses, finale)

### Clips by Tool

**Kling 3.0 (24):** S01, S02, S03, S04, S05, S09, S10, S11, S12, S14a/b/c, S15, S20a/b, S22, S24b/c, S30a, S31, S32, S33b, S34a/b

**Kling 2.5 Turbo (12):** S07, S13, S19, S23, S24a, S26, S28, S30b, S33a, S34c, S35a/b

**Veo (4):** S06, S17, S18, S27

**Seedance 1.0 (9):** S08, S16, S21, S25a/b, S29a/b/c/d

### Video Style Suffix

> Append this to every motion prompt before feeding to the video generation tool:
>
> `Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.`

This suffix is NOT included in the individual motion prompts below (to keep them readable). The human must append it when copying prompts to Kling/Veo/Seedance. EP03+ motion scripts will include the suffix inline.

---

## MOTION SCRIPT

---

### SHOT S01 — The Commander's Map Room (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:00–0:14 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Opening Anatolian psychedelic guitar riff — building energy, solo duel begins |
| **Scene Context** | Robotiko at retro-futuristic command console, leaning forward to study a backlit world map embedded in console surface |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Opening shot, first impression |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s01_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android at the command console. The android leans slightly forward, studying the backlit map. Amber route lines pulse in sequence across the console surface — each line brightens then fades. Analog dials and toggle switches flicker with amber indicator light. Dust motes drift through the overhead light cone falling on chrome shoulders. The zoom tightens from the wide room toward the commander and his glowing map. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S02 — The Chrome Messiah (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:14–0:28 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Hammond organ swell — sustained chord, cathedral-scale grandeur |
| **Scene Context** | Pristine Robotiko at elevated podium, arms spread messianic, golden spotlight |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Character reveal, podium grandeur |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s02_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android at the podium. Holographic data streams cascade downward behind him. Dark abstract audience silhouettes — mixed men and women — shift subtly in the darkness, maintain as featureless dark shapes, do not resolve into detailed figures. The golden spotlight narrows imperceptibly. Volumetric fog drifts upward from the floor. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S03 — Monument to Certainty (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:28–0:42 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Guitar vs. Hammond solo duel peaks — climactic intro passage |
| **Scene Context** | Close-up of pristine chrome torso and face, crowd reflected in chest plate |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Chrome close-up, detail critical |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s03_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Intimate zoom toward the chrome android's face. Blue eyes pulse with faint brightness fluctuations. Reflected crowd light shimmers across the chrome chest plate. Exposed analog wires (blue and red) vibrate subtly. Every chrome scratch, every wire bundle, every dust mote becomes visible as the frame tightens. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S04 — Davos Landing (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:43–0:52 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | Verse 1 begins — medium energy, Anatolian guitar riff |
| **Scene Context** | Chrome private jet on snowy alpine runway, Robotiko descends stairs |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — First location, jet + alps |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s04_selected.png`
- **End Frame:** N/A

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan right following the chrome android's descent down the jet stairs. Jet exhaust billows in massive white clouds, drifting left as the camera pans right. Snow particles swirl in the exhaust wash. The Swiss Alps hold steady in the background, monolithic and cold. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S05 — The Emissions Sermon (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:52–1:01 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s) |
| **Musical Moment** | Verse 1 continues — "Burning the fuel to preach: 'Emissions Low!'" |
| **Scene Context** | Robotiko at conference podium, jet visible through windows, faceless suited audience |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Conference scene, character acting |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s05_selected.png`
- **End Frame:** N/A

**Camera Move:** Dolly In

**Motion Prompt:**
> Steady dolly push toward the podium. The "SAVE THE PLANET" globe graphic rotates slowly. Through tall windows, jet exhaust persists as a slow plume. Abstract suited silhouettes — mixed men and women — shift slightly in their seats, maintain as featureless dark shapes, do not add facial detail. Fluorescent tubes above flicker once. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S06 — The Gasket Builds (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:02–1:10 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s (trim 2s) |
| **Musical Moment** | Verse 2 — medium-high energy. Bass syncs to discomfort. Funk-rock pocket. |
| **Scene Context** | Robotiko at podium, hand gripping midsection, chrome plates vibrating |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Google Veo (Mode A, 8s natural match) — Scene=8s, Veo=8s perfect |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s06_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Zoom tightening on the chrome android's midsection. Chrome abdominal plates vibrate visibly — rhythmic tremor. A hydraulic fluid bead on the temple descends slowly. Dark abstract audience silhouettes — mixed men and women — lean forward slightly, maintain as featureless dark shapes, do not resolve into detailed figures. Spotlight shifts from gold to warm amber. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S07 — The Gasket Blows (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:10–1:19 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s Mode B (trim 1s) |
| **Musical Moment** | "He blew a gasket in the hall" — Hammond swirl accent, hit on the downbeat |
| **Scene Context** | TRANSFORMATION: Steam and sparks erupt from torso seams, audience recoils |
| **Tech Strategy** | Mode B — Start/End Keyframes |
| **Clip Duration** | 10s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode B, 1080p) — Static camera, comedy transformation |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s07a_selected.png`
- **End Frame:** `episode-02/04_visuals/selected/ep02_s07b_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Frame holds still. Steam bursts from chrome seam lines in radial jets. Orange sparks cascade outward. Papers spiral upward. Abstract audience silhouettes — mixed men and women — topple backward in their seats, maintain as featureless dark shapes, do not add realistic features. The "SAVE THE PLANET" screen behind the podium flickers and dies. The eruption is sudden and comedic — a burst, not a destruction. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S08 — Map Flash: Davos Complete (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:19–1:20 |
| **Scene Duration** | 1s |
| **Coverage** | Direct — 1 × 5s (trim 4s — use as 1s transition beat) |
| **Musical Moment** | Hammond swirl — single accent beat |
| **Scene Context** | World map: Davos route burns solid, remaining routes pulse |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — 1s screen time, 720p invisible |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s08_selected.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> The vintage map holds still. Davos route burns solid amber, remaining routes pulse faintly. Film grain rolls across the steel surface. A single pulse of light brightens the next destination marker. Atmospheric dust settles. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S09 — San Francisco Neon (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:20–1:25 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Verse 3 begins — "He landed in San Francisco Bay" |
| **Scene Context** | SF skyline at night, neon startup logos, Golden Gate in fog |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Neon reflections on chrome, detail matters |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s09_selected.png`
- **End Frame:** N/A

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan right following the chrome android's stride along the waterfront. Neon signs flicker — startup logos, crypto tickers, wellness apps. Fog drifts across the Golden Gate silhouette in the distance. Wet pavement reflections of pink and green neon shimmer beneath chrome feet. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S10 — The Alley Pitch (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:25–1:30 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | "He saw a junkie with a knife / And thought: 'A pitch!'" Guitar accent on "pitch" |
| **Scene Context** | Narrow neon alley: Robotiko with holographic pitch deck, disheveled figure |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Character interaction, switchblade glint |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s10_selected.png`
- **End Frame:** N/A

**Camera Move:** Dolly In

**Motion Prompt:**
> Dolly push into the narrow neon-lit alley. The holographic pitch deck rotates, casting blue-white light. "$GURU" token charts pulse upward. A switchblade in the disheveled figure's hand catches neon light — single glint. The figure's eyes track downward toward the chrome leg. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S11 — The Leg Theft (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:30–1:34 |
| **Scene Duration** | 4s |
| **Coverage** | Direct — 1 × 5s Mode B (trim 1s) |
| **Musical Moment** | "The junkie grabbed his metal leg" — bass drop accent |
| **Scene Context** | TRANSFORMATION: Thief sprints with Robotiko's leg, Robotiko balances on one leg |
| **Tech Strategy** | Mode B — Start/End Keyframes |
| **Clip Duration** | 5s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Mode B, 1080p) — Fast transformation, keyframe quality critical |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s11a_selected.png`
- **End Frame:** `episode-02/04_visuals/selected/ep02_s11b_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Sparks trail from the severed chrome joint rightward. The holographic pitch deck continues spinning, untouched. Pan follows the escaping figure clutching the metal leg while the chrome android holds a one-legged pose in frame left — perfectly still, bewildered. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S12 — The Egg Vendor (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:34–1:39 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 5s (perfect match) |
| **Musical Moment** | Energy dips slightly — breath in the groove. Warmth in bass line. |
| **Scene Context** | Egg vendor reattaches Robotiko's leg with wrench. Only genuine care in the episode. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 5s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Intimate scene, warm lighting detail |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s12_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Gentle zoom toward the vendor's hands working the wrench. Egg cart heat lamp casts warm golden light over the scene. The chrome android's blue eyes flicker slightly brighter. Background neon recedes to soft bokeh. Warm, intimate lighting. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S13 — Chorus 1: The Split Screen (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 1:39–1:52 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Chorus 1 explodes — "Guru Talks never lie!" Rock choir + heavy fuzz guitar |
| **Scene Context** | Triptych: Instagram perfection (left) vs. raw reality (right) vs. Robotiko center |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.77× (10s → 13s) |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, triptych complexity |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s13_selected.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> Frame holds still. Left panel: emojis float upward, Instagram filter pulses with warm color. Right panel: a rat crosses the foreground, trash shifts on the ground. Center: the chrome android's body reflects both realities — warm gold from the left, cold neon from the right. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S14 — The Hype Montage (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 1:52–2:06 |
| **Scene Duration** | 14s |
| **Coverage** | Multi-Clip — 3 × 5s = 15s (trim 1s total in CapCut) |
| **Musical Moment** | Post-chorus heavy fuzz riff — aggressive, grinding. Each cut on beat 1. |
| **Scene Context** | Rapid-fire montage: phone screens → Robotiko alone in darkness, apps projecting onto body |

#### Clip A — S14a (Phone Screens)

| Field | Value |
|---|---|
| **Clip Duration** | 5s |
| **Motion Strength** | 6 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Digital projections on chrome |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s14_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Zoom into the upper-left region of the composition where the phone screen projections are brightest. Podcast wave graphics pulse rhythmically. "VIRAL FILTER" overlay text flickers. Light shifts from blue to pink in rapid bursts. The zoom pushes into the digital noise. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S14b (Career App Assault)

| Field | Value |
|---|---|
| **Clip Duration** | 5s |
| **Motion Strength** | 6 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — App light across body |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s14_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Pan across the chrome android's body as app projections cascade across his surface — "YOU WILL RISE!" gradient scrolls from pink to white rightward. Multiple app color cycles flash across the chrome surface. The pan reveals every surface of the body covered in projected light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip C — S14c (Isolation Reveal)

| Field | Value |
|---|---|
| **Clip Duration** | 5s |
| **Motion Strength** | 5 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Void reveal |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s14_selected.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Zoom out from the chrome android to reveal the surrounding void. App projections overlap into white noise on the body while darkness expands at the frame edges. A harsh white spotlight isolates the figure in the center of blackness. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S15 — The Salt Flat (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 2:06–2:20 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Psychedelic guitar solo — sustained bends, wah-pedal swells |
| **Scene Context** | Wide landscape: Robotiko walks alone across endless salt flat, bruised purple-orange sky |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Beautiful wide landscape, needs resolution |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s15_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out reveals the salt flat's immensity — the chrome android shrinks in the frame. His reflection ripples in shallow water. Heat shimmer distorts the horizon in slow organic waves. In the extreme distance, a thin vertical line — possibly a mirage — is barely visible. Bruised purple-orange sky above. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S16 — Map: Congo Incoming (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 2:20–2:34 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Hammond organ swirls beneath guitar solo, transition beat |
| **Scene Context** | World map: two routes solid, Congo pulse begins. Coffee ring stain, creases. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Vintage map, 720p suits paper grain |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s16_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow push toward the Congo destination marker. Two completed routes glow steady amber. The Congo marker pulse brightens and fades rhythmically. Map surface shows first signs of age — coffee ring stain catches light. Film grain intensifies. Dust motes drift through the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S17 — Congo Mine Arrival (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:34–2:42 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s (trim 2s) |
| **Musical Moment** | Verse 5 — "He reached the Congo, deep and red." Guitar descends chromatically. |
| **Scene Context** | Vast open-pit mine, Robotiko at rim in conquering-hero pose, fitness tracker glowing |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Google Veo (Mode A, 8s natural match) — Scene=8s, Veo=8s perfect |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s17_selected.png`
- **End Frame:** N/A

**Camera Move:** Crane Down

**Motion Prompt:**
> Descending crane from above the mine rim — revealing terraced depth layer by layer. Red dust particles hang in angled light shafts. Tiny abstract figures — mixed men and women — on the terraces shift incrementally, maintain as distant indistinct shapes, do not resolve into detailed people. A green fitness tracker glow pulses on the chrome android's wrist — the only non-red light in the scene. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S18 — The Fitness Tracker (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:42–2:51 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s) |
| **Musical Moment** | "Oh, such a powerful work-out rig!" — accent on "work-out" |
| **Scene Context** | Robotiko peers at mining hands, tracker reads "GREAT WORKOUT DETECTED" |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Google Veo (Mode A, 8s→9s at 89% speed) — Minimal stretch in CapCut |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s18_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Zoom toward the fitness tracker screen as it flashes its reading. The tracker's blue-green glow pulses twice. Red dust drifts upward, coating the chrome lower legs. In the background, an overloaded truck crawls up the mine road, sluggish and heavy. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S19 — The Boss / Shoulder Scrape (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 2:52–3:04 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s Mode B → 12s at 0.83× |
| **Musical Moment** | Verse 6 — "While Boss scraps off his shoulder steel!" Heavy drums accent scraping. |
| **Scene Context** | TRANSFORMATION: Boss scrapes chrome from Robotiko's shoulder. First real damage. |
| **Tech Strategy** | Mode B — Start/End Keyframes |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode B, 1080p) — Static camera, first real damage |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s19a_selected.png`
- **End Frame:** `episode-02/04_visuals/selected/ep02_s19b_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Metal tool drags across chrome shoulder — each pass produces orange sparks cascading downward. The transformation from pristine to scraped chrome is cumulative — each pass strips a layer of surface. The chrome android holds a bodybuilder pose, grinning wider. Sparks cascade against the ochre dust backdrop. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S20 — Transition: Red to Yellow (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 3:04–3:24 |
| **Scene Duration** | 20s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s |
| **Musical Moment** | Psychedelic guitar + Hammond solo — sustained, exploratory, wandering quality |
| **Scene Context** | Robotiko walks through liminal landscape shifting from red earth to industrial haze |

#### Clip A — S20a (Red Earth Phase)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Transition walk, shoulder damage visible |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s20_selected.png`

**Camera Move:** Pan Right

**Motion Prompt:**
> Slow pan following the chrome android's solitary walk. The color palette holds in red earth and ochre. The bright scrape on the left shoulder catches amber light differently than the surrounding chrome. Dust and low fog interweave at ground level. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S20b (Industrial Haze Phase)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Color shift landscape |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s20_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Zoom pushes past the chrome android toward the emerging industrial landscape ahead — power lines and smokestacks materialize from yellow-green haze. The color shift from red-ochre to sickly yellow-green is visible across the frame. The haze thickens as the zoom advances. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S21 — Map: Bangladesh Incoming (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 3:24–3:38 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Guitar solo fades, Hammond leads into next section |
| **Scene Context** | Map — three routes solid, Bangladesh pulse begins. More worn. |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Same map aesthetic, worn paper |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s21_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Push toward the Bangladesh marker. Three amber routes glow steady. The Bangladesh marker pulse is more urgent — flickering faster than previous markers. New creases and a torn corner are visible on the map. Halftone dots smear. The map's damage is accumulating. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S22 — Bangladesh Factory (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:38–3:48 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Verse 7 — rising energy. Tempo rise begins. Driving rhythm section. |
| **Scene Context** | Enormous garment factory, Robotiko attempts Downward Dog, workers stare |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Complex interior, many elements |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s22_selected.png`
- **End Frame:** N/A

**Camera Move:** Dolly In

**Motion Prompt:**
> Dolly push into the factory interior. Steam from pressing stations drifts upward through flickering fluorescent tubes, creating undulating low fog. Fabric piles shudder with machine vibration. Workers' heads turn incrementally toward the chrome android in disbelief. Sewing machine needles pulse rhythmically. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S23 — The Press Slam (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:48–3:57 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s Mode B (trim 1s) |
| **Musical Moment** | "A Heavy Press gave a sudden skip" — drum fill accents press slam |
| **Scene Context** | TRANSFORMATION: Industrial press slams torso, creating visible dent. Shrug and smile. |
| **Tech Strategy** | Mode B — Start/End Keyframes |
| **Clip Duration** | 10s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode B, 1080p) — Static camera, factory transformation |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s23a_selected.png`
- **End Frame:** `episode-02/04_visuals/selected/ep02_s23b_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Hydraulic press slams downward — catches fluorescent light on its edge, flash of white on impact. Sparks shower from the chrome impact point. Fluorescent tubes flicker from the vibration. When the press lifts: a fist-sized dent is visible on the right torso. The chrome android shrugs casually. The factory continues unchanged around him. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S24 — Chorus 2: The Cracking Split (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 3:57–4:25 |
| **Scene Duration** | 28s |
| **Coverage** | Multi-Clip — 3 × 10s = 30s (trim 2s total) |
| **Musical Moment** | Chorus 2 — same lyrics, higher intensity. Choir louder, fuzz heavier. Post-chorus riff. |
| **Scene Context** | Escalated split-screen: Instagram glitchier, reality with shoulder scrape + torso dent |

#### Clip A — S24a (Split Screen Holds)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, escalated split screen |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s24_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The split-screen composition holds static while its contents degrade. Left panel: digital artifacts cascade, buffering circles spin, filter glitches reveal the shoulder scratch beneath. Right panel: factory steam rolls across damaged torso, a child's "HELP" sign sways. Center: the chrome android's arms raise asymmetrically — the dented side pulls differently. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S24b (Reality Side Zoom)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Factory side close-up |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s24_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Zoom pushes toward the right panel — the reality side. The filtered Instagram panel slides off-frame to the left. Factory steam, the child's sign, and the damaged chrome torso fill the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip C — S24c (Center: The Guru Cracking)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Full triptych wide, asymmetric pose |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s24_selected.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Zoom pulls back to reveal the full triptych again — wider perspective that emphasizes the damage in the center panel. The chrome android's asymmetric pose is more visible at this distance. All three panels visible: filtered perfection, raw reality, and the cracking figure between them. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S25 — Map: Paris Incoming (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 4:25–4:42 |
| **Scene Duration** | 17s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim 3s total) |
| **Musical Moment** | Psychedelic guitar + Hammond — urgent, almost frantic |
| **Scene Context** | Map — four routes solid, Paris pulse. Map tearing along fold lines. |

#### Clip A — S25a (Map Overview)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Map with tearing fold lines |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s25_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Push toward the Paris marker — faster zoom than previous map transitions. Four amber routes blaze across the damaged surface. Paris marker pulse is erratic and rapid. Fold lines are becoming tears — paper fibers visibly separating. Halftone printing bleeds into itself. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S25b (Map Close-Up)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Paper texture detail |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s25_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Tight framing on the Paris marker and surrounding map damage. Paper grain visible, smearing ink, tearing fold lines at texture-level detail. The Paris pulse fills a large portion of the frame. The map surface shows extreme wear — tears, ink bleeding, paper fibers separating. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S26 — Hallucination Mode: Paris Split (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:42–4:52 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Bridge — chaotic. Dissonant Hammond. "Hallucination Mode" engaged. |
| **Scene Context** | Paris split: romantic fantasy (left) vs. garbage riot (right), Robotiko straddling, eyes glitching |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, dual reality split |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s26_selected.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> Frame holds still. Left side: cafe lights twinkle, couples walk in slow motion. Right side: barricade fires crackle, smoke billows, riot police shift positions. Center: the chrome android's left eye glows steady blue, right eye strobes between blue and red in rapid irregular pulses. Chrome body reflects both realities — warm gold and dirty gray fighting on every surface. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S27 — The Baguette and the Rat (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:52–5:01 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s) |
| **Musical Moment** | "'No bread? Eat rats!'" — chord stab on "rats." Dissonance peaks. |
| **Scene Context** | Robotiko offers baguette with rat to angry strikers |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Google Veo (Mode A, 8s→9s at 89% speed) — Minimal stretch in CapCut |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s27_selected.png`
- **End Frame:** N/A

**Camera Move:** Dolly In

**Motion Prompt:**
> Dolly toward the confrontation. The rat on the baguette twitches its nose, whiskers catching firelight. The chrome android extends the offering with sommelier-like confidence. Strikers — mixed men and women, rough impressionistic figures matching the source image — recoil as a wave, do not add photorealistic facial detail. Barricade fire flickers behind them. Orange firelight fights gray smoke. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S28 — The Sensor Smash (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 5:02–5:12 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s Mode B (perfect match) |
| **Musical Moment** | Verse 9 — "And smashed the sensors on his back." Aggressive drums. |
| **Scene Context** | TRANSFORMATION: Mob attacks from behind, sensor panels torn, head rotates 180° |
| **Tech Strategy** | Mode B — Start/End Keyframes |
| **Clip Duration** | 10s |
| **Motion Strength** | 7 |
| **Recommended Tool** | Kling 2.5 Turbo (Mode B, 1080p) — Static camera, mob attack transformation |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s28a_selected.png`
- **End Frame:** `episode-02/04_visuals/selected/ep02_s28b_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Multiple hands — diverse skin tones, mixed men and women — grab the chrome android from behind. Sparks cascade from torn wiring in sheets. The head rotates slowly from forward to 180° — mechanical owl-turn with an expression of innocent confusion. Back panels peel progressively — first one, then two, colorful wires spilling out. Hands and figures remain rough and impressionistic as in the source image, do not add photorealistic detail. Firelight illuminates the shower of sparks. Expression throughout: bewildered, not angry. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S29 — Map: The Final Marker (Multi-Clip: 4 clips)

| Field | Value |
|---|---|
| **Timestamp** | 5:12–5:48 |
| **Scene Duration** | 36s |
| **Coverage** | Multi-Clip — 4 × 10s = 40s (trim 4s total) |
| **Musical Moment** | Extended psychedelic guitar + Hammond — darker tonality, sustained, heavy, inevitable |
| **Scene Context** | Map barely holding together — charred edges, dissolved halftone. War zone marker pulses RED. |

#### Clip A — S29a (Full Map, Maximum Damage)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Charred edges, dissolved halftone |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s29_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The map holds in its fullest deterioration. Five routes glow faintly through the damage — amber barely visible through charring. The final destination marker pulses RED, not amber. The red pulses slowly, like a heartbeat. No movement — just the pulse and the heavy film grain. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S29b (Slow Approach)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Zoom into deterioration |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s29_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the red war zone marker. The map's tears and charring slide past as the frame pushes in. Paper fibers separate at fold lines. Halftone dots bleed. The zoom is heavy and deliberate. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip C — S29c (Texture Detail)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Extreme close-up |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s29c_selected.png` ✅

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Extreme close-up of the map's texture. Halftone dots appear large as coins, paper fibers visible as individual strands. The red pulse from the war zone marker fills the frame with rhythmic red light. Minimal zoom — the texture detail provides the visual interest. Dust particles settle on the deteriorated surface. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip D — S29d (Red Pulse Isolation)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Seedance 1.0 (Mode A, 1080p, map texture) — Tight red marker framing |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s29c_selected.png` *(uses the supplementary image from Clip C)*

**Camera Move:** Static

**Motion Prompt:**
> Tight framing on the red pulse. The marker fills a quarter of the frame, beating slowly, hypnotically. The surrounding charred paper is near-abstract — textured like a landscape of decay. The red pulse continues alone against the deteriorated surface. Heavy film grain. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S30 — The War Zone (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 5:48–6:07 |
| **Scene Duration** | 19s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim 1s) |
| **Musical Moment** | Verse 10 — LOW energy. Tempo slows. Sparse guitar, minimal drums. |
| **Scene Context** | Bombed-out landscape. Desaturated monochrome. Robotiko in peace pose. Distant explosions. |

#### Clip A — S30a (Wide Desolation)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Desolation panorama, explosions |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s30_selected.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Slow zoom out reveals the devastation. The chrome android stands motionless in a peace pose — the only saturated colors in a desaturated monochrome landscape: blue eyes, blue-red wires. Distant explosions bloom in slow motion behind him. Dust hangs permanently in the air. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S30b (Sustained Stillness)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, sustained stillness |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s30_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The frame holds at its widest. The chrome android is small in the devastation, arms still open. A new distant explosion blooms slowly — an orange-black cloud against gray sky. Rubble does not move. Complete visual stillness. The figure remains motionless in the ruined landscape. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S31 — Noise-Canceling (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:07–6:17 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s (perfect match) |
| **Musical Moment** | Verse 11 — theatrical whisper. "I block the hate, I block the fear." Wide, sparse. |
| **Scene Context** | Close-up: Robotiko with oversized 70s headphones, calm and half-lidded, unheard explosions behind |
| **Tech Strategy** | Mode A |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Close-up, explosion bokeh, headphone detail |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s31_selected.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Gentle zoom toward the chrome android's face — oversized 70s headphones filling the frame. Blue eyes steady, half-lidded, serene. Lips move slightly. Behind him, out of focus: an explosion lifts a vehicle in extreme slow motion. Scorched leather headphone edges catch faint orange glow. The zoom is gentle, almost intimate. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S32 — THE EAR SHOT (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:17–6:25 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s Mode B (excess 2s — use for emphasis: HOLD THIS SHOT) |
| **Musical Moment** | "A shrapnel took away his ear" — whisper BREAKS. One beat silence. Chorus 3 detonates. |
| **Scene Context** | CRITICAL TRANSFORMATION: Shrapnel strikes right ear. Headphone shatters. Ear tears away. First acknowledgment. Red eye. |
| **Tech Strategy** | Mode B — Start/End Keyframes |
| **Clip Duration** | 10s |
| **Motion Strength** | 8 |
| **Recommended Tool** | Kling 3.0 (Mode B, 1080p) — **EP02 critical turning point. HIGHEST PRIORITY.** |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s32a_selected.png`
- **End Frame:** `episode-02/04_visuals/selected/ep02_s32b_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Barely perceptible zoom tightening. The headphone cup shatters outward from a shrapnel impact. Sparks erupt — vivid orange-white against near-total black. Silver-blue hydraulic fluid seeps in a slow drip from the torn ear cavity. The chrome hand reaches toward the damage. The right eye shifts from blue to red in a slow iris-change. Mouth opens. The transformation from serene calm to devastation. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S33 — The Damaged Guru (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 6:26–6:44 |
| **Scene Duration** | 18s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim 2s) |
| **Musical Moment** | Chorus 3 — Grand Finale. Maximum energy. Full choir, maximum fuzz, all instruments at peak. |
| **Scene Context** | Robotiko alone in void under spotlight. All damage visible. Not smiling. The guru is gone. |

#### Clip A — S33a (The Hero Shot)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, full damage inventory |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s33_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Frame does not move. Spotlight does not shift. The chrome android holds a pose — arms raised, mechanical, without conviction. All damage visible: shoulder scrape, torso dent, exposed back sensor wires, missing right ear sparking intermittently. Left eye blue, right eye red. No smile. Sparks from the ear cavity flicker at irregular intervals. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S33b (The Damage Inventory)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Clinical zoom on accumulated damage |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s33_selected.png`

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Slow zoom toward the chrome android's torso. The zoom inventories the damage in sequence — shoulder scrape passes through frame, torso dent fills the center, exposed back sensor wires visible at the edge. The zoom is clinical, forensic. Ear sparks slow to a faint pulse. The spotlight narrows imperceptibly. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S34 — The Pullback (Multi-Clip: 3 clips)

| Field | Value |
|---|---|
| **Timestamp** | 6:44–7:08 |
| **Scene Duration** | 24s |
| **Coverage** | Multi-Clip — 3 × 10s = 30s (trim 6s total in CapCut) |
| **Musical Moment** | Outro — spoken word over fading guitar. Instruments drop out one by one. |
| **Scene Context** | Slow pull-back from Robotiko in the void. Damage more apparent. Spotlight narrows. |

#### Clip A — S34a (Arms Lower)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Pullback begins, spotlight narrows |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s34_selected.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> The pullback begins. Slow zoom out from the figure. The chrome android's arms lower slowly to his sides. Ear sparks slow from bright orange to dim amber. The visual darkens by a fraction. The spotlight begins to narrow. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S34b (The Void Expands)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 3.0 (Mode A, 1080p) — Spotlight cone visible, continued zoom out |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s34_selected.png` *(reuses S34 image — zoom out creates wider framing)*

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Continued pullback from a wider starting position. The spotlight cone is clearly visible against the void — a shrinking circle of light. The chrome android's damage details are harder to read at this distance — becoming a silhouette with points of light: dim blue eye, steady red eye, dying ear sparks. The zoom pulls back steadily. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip C — S34c (Near-Silhouette)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, maximum distance |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s34_selected.png` *(reuses S34 image — maximum distance framing)*

**Camera Move:** Static

**Motion Prompt:**
> The frame holds at maximum distance. The chrome android is a small figure in a vast dark frame — the spotlight cone barely contains him. Only points of light remain: dim blue eye, steady red eye, last ember from the ear. The visual darkens incrementally. Near-darkness approaches. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S35 — Fade to Nothing (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 7:08–7:28 |
| **Scene Duration** | 20s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (perfect match) |
| **Musical Moment** | Final guitar harmonic sustains and decays. Feedback. Hiss. Silence. |
| **Scene Context** | Near darkness. Points of light: blue eye (fading), red eye (steady), ear sparks (dying). Distant amber dot (Mentor). |

#### Clip A — S35a (The Last Lights)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, near-darkness |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s35_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> Near-total darkness. The chrome android reduced to points of light. The blue eye dims incrementally — each blink lasts longer than the last. The red eye holds steady. Ear sparks fire once, twice. In the extreme far background, a barely perceptible amber dot. Heavy film grain dominates the frame. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S35b (Silence)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | Kling 2.5 Turbo (Mode A, 1080p) — Static camera, final fade to black |

**Assets Required:**
- **Start Frame:** `episode-02/04_visuals/selected/ep02_s35_selected.png`

**Camera Move:** Static

**Motion Prompt:**
> The blue eye blinks one final time and holds closed — then fades. The ear sparks die. Only the red eye remains — a single point of steady red in total black. Heavy film grain dissolves the image into abstract texture. The red eye holds. Then fades to black. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

## BEAT SYNC NOTES

| Timestamp | Musical Event | Required Visual Action | Clip Reference |
|---|---|---|---|
| 0:00 | Opening guitar riff — first note | S01: Zoom begins, first route line pulse | S01 |
| 0:14 | Hammond organ sustain | S02: Cut to podium — Robotiko revealed | S02 |
| 0:43 | Verse 1 — guitar riff rhythm | S04: Pan begins — steps sync to BPM | S04 |
| ~1:12 | "He blew a gasket in the hall" | S07: Eruption on exact downbeat | S07 |
| 1:19 | Hammond swirl accent | S08: Map flash — one-second hold | S08 |
| ~1:31 | "The junkie grabbed his metal leg" — bass drop | S11: Leg grab syncs to bass drop | S11 |
| 1:34 | Energy dip — breath | S12: Cut to egg vendor — warmth in the pause | S12 |
| 1:39 | Chorus 1 — choir entry | S13: Split-screen locks into place | S13 |
| 1:52 | Post-chorus fuzz riff | S14a: Montage projections begin | S14a |
| 2:06 | Instrumental solo begins | S15: Cut to salt flat — visual exhale | S15 |
| ~2:52 | "While Boss scraps off his shoulder steel!" | S19: Scraping rhythm syncs to drums | S19 |
| ~3:50 | "A Heavy Press gave a sudden skip" | S23: Press slam on drum fill | S23 |
| 3:57 | Chorus 2 — choir re-entry | S24a: Escalated split-screen | S24a |
| 4:42 | Bridge — "Hallucination Mode" | S26: Paris split engages | S26 |
| ~5:02 | "And smashed the sensors" — drums | S28: First mob impact on drum accent | S28 |
| 5:48 | Tempo slows — sparse guitar | S30a: Cut to war zone — stillness | S30a |
| ~6:20 | "A shrapnel took away his ear" | S32: Impact on "took away" — then silence | S32 |
| 6:26 | Chorus 3 DETONATION | S33a: Hard cut to hero shot | S33a |
| 6:44 | Instruments dropping out | S34a: Pullback begins — each dropout dims visual | S34a |
| ~7:25 | Final harmonic decays to silence | S35b: Red eye last light. Then black. | S35b |

---

## COVERAGE SUMMARY

| Metric | Value |
|---|---|
| **Total music duration** | 448s |
| **Total generated clip duration** | 450s |
| **Coverage ratio** | 100.4% |
| **Total clips** | 49 |
| **Clips from existing images** | 49 |
| **Clips needing new images** | 0 (all resolved) |

### Coverage Breakdown by Strategy

| Strategy | Shots | Clips | Generated Duration | Notes |
|---|---|---|---|---|
| **Direct** | 18 | 18 | 155s | Single clips, trim excess in CapCut |
| **Speed Ramp** | 8 | 8 | 80s (→109s after ramp) | 0.71×–0.83× slowdown |
| **Multi-Clip** | 9 | 23 | 215s | Sub-clips with varied camera moves |
| **TOTAL** | **35** | **49** | **450s** | **100.4% coverage** |

### New Images Required

| Sub-clip | Description | Status |
|---|---|---|
| S29c | Extreme close-up of deteriorated map, charred edges, red pulse | ✅ GENERATED |
| ~~S34b~~ | ~~Robotiko in void, wider framing~~ | ✅ CANCELLED — S34 image reused, zoom-out creates wider framing |

> S29d reuses S29c image. S34b and S34c reuse S34 image — zoom-out provides progressively wider framing.

---

## DIRECTOR'S NOTES

### Duration Coverage Philosophy

v01 of this motion script had a critical flaw: 448s of music covered by only 175s of generated video (39%). v02 resolves this through three strategies:

1. **Speed Ramp** for atmospheric/instrumental shots (8 shots): A 10s clip slowed to 0.71× gives 14s — ideal for slow, contemplative moments where the slowdown enhances the dreamlike quality.

2. **Multi-Clip** for long scenes (9 shots): Sub-clips with different camera moves create visual variety within the same scene. This prevents monotony and gives the editor real choices in CapCut.

3. **Direct** for well-matched scenes (18 shots): Where the tool's 5s/10s output already covers the music, no intervention is needed.

### Motion Strength Arc (v02)

The average motion strength is 4.1 — within the EP01-03 target of 4-5. The arc follows the episode's cumulative darkening:

- **Intro (S01-S03):** 3-4 — Establishing, restrained, speed-ramped dreaminess
- **Davos (S04-S08):** 2-7 — First comedy peak (gasket)
- **SF (S09-S12):** 3-6 — Leg theft energy, egg vendor breath
- **Chorus 1 + Montage (S13-S14):** 5-6 — Energetic but contained
- **Salt Flat + Maps (S15-S16):** 2 — Critical pause
- **Congo (S17-S19):** 4-6 — First damage
- **Transition + Map (S20-S21):** 2-3 — Second breath
- **Bangladesh (S22-S23):** 5-7 — Second damage peak
- **Chorus 2 (S24):** 5-6 — Escalation via sub-clips
- **Paris (S25-S28):** 3-7 — Third damage peak
- **Map Final (S29):** 2-3 — Extended deterioration, hypnotic pacing
- **War Zone (S30-S32):** 2-8 — LOW to MAXIMUM at the ear
- **Finale (S33-S35):** 1-4 — Stillness after the scream

### Camera Move Decisions

- **Mode B shots (S07, S11, S19, S23, S28) use Static** — transformation IS the movement. Exception: **S11 (Pan Right)** for thief escape tracking, **S32 (Slow Zoom In)** for the zoom into the wound.
- **Speed Ramp shots favor Slow Zoom In/Out** — the slowdown enhances the zoom's contemplative quality.
- **Multi-Clip sub-clips vary camera moves** — no two sub-clips within a shot share the same camera move (prevents visual monotony over 20-36 second scenes).
- **S33a (Hero Shot) is Static** — stillness against Chorus 3's maximum sonic energy.

### Supplementary Image Strategy

Only 1 new image required (out of 49 clips):

1. **S29c** — The map has been zoomed into progressively through S29a and S29b. By S29c, we need an extreme close-up that the wide-shot composition of S29 cannot provide. A new image at texture-level detail of the map's deterioration. Supplementary prompt included inline above, ready to paste into Nano Banana.

~~2. **S34b** — CANCELLED. The existing S34 image is sufficient — video generator's zoom-out naturally creates wider framing across S34a→S34b→S34c. No supplementary image needed.~~

---

## APPROVAL STATUS
- [ ] **Human reviewed camera moves**
- [ ] **Human reviewed tech strategy (Mode A/B)**
- [ ] **Human reviewed duration coverage (49 clips, 100.4%)**
- [ ] **Human generated supplementary image (S29c only — S34b cancelled)**
- [ ] **Human approved**
- [ ] **Ready for video generation**

> ⛔ Video generation must NOT begin until this document is approved.
