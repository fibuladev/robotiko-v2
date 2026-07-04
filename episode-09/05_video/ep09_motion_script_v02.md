# VIDEO PRODUCTION SHEET (KLING / VEO / SEEDANCE)
> **Version:** v02 | Skill: `_skills/robotiko-motion-script/SKILL.md` v2.1
> Generated: 2026-06-30 (v01) → 2026-07-04 (v02: em-dash cleanup + eye-glow fix; content unchanged from approved v01)
> Model: Opus (Max Effort)
> Inputs: ep09_dramaturgy_v01.md (APPROVED), ep09_musical_metadata.json, ep09_concept_notes.md (APPROVED), character_profiles.json

---

## PRE-GENERATION CHECKLIST

- [x] `episode-09/03_direction/ep09_dramaturgy_v01.md` — APPROVED scene breakdown (38 scenes)
- [x] `episode-09/04_visuals/raw/` — All 38 scene images confirmed (1.png–38.png + 11b.png, 27b.png)
- [x] `episode-09/02_music/ep09_musical_metadata.json` — 22 sections, 423s, 77 BPM, E Minor
- [x] `_management/master.md` — Station 7: The Integrated Self (Kintsugi)
- [x] `_assets/cast/character_profiles.json` — Phase 2→3 transition at S27, refs confirmed on disk
- [x] `_memory/lessons.md` — All motion prompt rules internalized

> Image source: `episode-09/04_visuals/raw/` (selected/ empty — raw keepers used per SKILL.md fallback)
> Mode B end-frames: 11b.png (shutter), 27b.png (kintsugi)
> Reference images excluded from shots: ref_command_bridge.png, ref_exterior.png, ref_mechanic.png, ref_onlookers.png, ref_workshop.png

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP09 |
| **Title** | Shadow Debugging |
| **Station** | The Integrated Self (Kintsugi — making peace with flaws) |
| **Camera Personality** | The Discovering Camera — Slow Zoom Out = understanding widens (NOT retreat). Climax Still Hold at S25 ("The Unsolvable"). |
| **Dominant Energy** | Stark / hypnotic / doom / contemplative / kintsugi |
| **Total Shots** | 38 |
| **Total Clips** | 41 (3 multi-clip scenes: S27, S35, S36) |
| **Total Duration** | 7:03 (423s) |
| **MS Average** | 3.15 (target: 3.0–3.5 for spoken word pacing) |
| **Phase Transition** | @Damaged (S01–S26) → @Kintsugi (S27–S38) at 4:09 |

---

## ELEMENT REGISTRY

| Element Name | Reference Images | Scenes Active | Description |
|---|---|---|---|
| **@Damaged** | `_assets/cast/android_damaged.png` + `_2.png`, `_3.png` | S01–S26 | Phase 2 — rusted chrome, missing right ear, torso dent, shoulder scratches, fraying wires |
| **@Kintsugi** | `_assets/cast/android_kintsugi.png` | S27–S35 | Phase 3 — patchwork body, gold-filled cracks, translucent digital skin, bioluminescent core |

> S27a uses @Damaged (start state — Mode B handles the gold progression visually).
> S36–S38 have no character in frame — no Element tags.

---

## VIDEO STRATEGY REFERENCE

| Mode | When to Use | Input | Duration |
|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, no transformation | 1 image | 5s or 10s |
| **B — Start/End Keyframes** | Transformations, state changes | 2 images | 5s or 10s |

**Duration Coverage Strategy:**

| Scene Duration | Strategy | Clip Count | Notes |
|---|---|---|---|
| ≤ 5s | **Direct** | 1 × 10s | Trim excess in CapCut (10s for coverage) |
| 6–10s | **Direct** | 1 × 10s | Trim in CapCut |
| 11–15s | **Speed Ramp** | 1 × 10s + slow-mo (max 1.5×) | |
| 16–30s | **Multi-Clip** | ⌈duration / 10⌉ clips | Each sub-clip gets own camera move |

**Motion Strength Scale:** 1 = Barely breathing / 5 = Cinematic drama / 10 = Chaos and disintegration

---

## TOOL ASSIGNMENT SUMMARY

### Tool Distribution

| Tool | Clips | % | Assignment Logic |
|---|---|---|---|
| **Kling 3.0** | 38 | 92.7% | All camera moves + Element-tagged + Mode B clips |
| **Kling 2.5 Turbo** | 2 | 4.9% | Static + no Element (budget shots) |
| **Seedance 1.0** | 1 | 2.4% | Static + no character (standalone landscape) |
| **TOTAL** | **41** | **100%** | — |

> EP09 is heavily Kling 3.0 because nearly every shot has either Robotiko (needs Elements) or camera movement. The spoken-word pacing means character close-ups dominate. This is honest for the episode's visual grammar.
> All Kling 3.0 clips use Omni References (confirmed same cost as standard, EP07 test conclusive).
> OmniEdit reserve: 10–15% of Kling budget for post-generation corrections.

### Assignment Rules Applied

1. Mode B → Kling 3.0 only (S11, S27a)
2. Element-tagged shots → Kling 3.0 only (all @Damaged and @Kintsugi scenes)
3. Camera movement → Kling 3.0 (full camera vocabulary)
4. Static + no Element + no character → Kling 2.5 Turbo or Seedance

### Clips by Tool

**Kling 3.0 (38):** S01, S02, S03, S05, S06, S07, S08, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27a, S27b, S28, S29, S30, S31, S32, S33, S34, S35a, S35b, S36a, S36b, S37

**Kling 2.5 Turbo (2):** S04, S09

**Seedance 1.0 (1):** S38

---

## MOTION SCRIPT

---

### SECTION 1: THE FAILED MESSIAH (Exterior Prologue, 0:00–0:59)

---

### SHOT S01 — The Myth (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:00–0:14 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Faint fuzz guitar drone decaying into void — near-nothingness |
| **Scene Context** | Silhouette descending grey path, false halo from cold sun behind — worshipper's-eye angle |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + opening shot quality |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/1.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> Silhouette of a chrome android descending a grey path toward the camera. Cold sun behind creates a false halo effect. Fog drifts at ground level, barely perceptible movement in the figure's slow step forward. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S02 — The Puncture (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:15–0:26 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | Dry spoken word enters — "I came down from the mountain" |
| **Scene Context** | The halo punctured — body revealed: rusted chrome, missing ear, torso dent |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.91× (10s → 11s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/2.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> The @Damaged chrome android walks forward on a grey threshold - rusted chassis, missing right ear, torso dent visible. Flat daylight replaces the halo. Blurred shapes of onlookers in the distance below. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S03 — The Held Silence (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 0:27–0:39 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | "Nothing comes out" — held silence in the vocal delivery |
| **Scene Context** | Face close-up, mouth opens, nothing comes out — held too long |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + face close-up |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/3.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Close-up of the @Damaged chrome android's face - calm steady blue eyes, chrome surface catching overcast light. Mouth mechanism barely opens. Hold. Subtle atmospheric dust drift. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S04 — The Myth-Engine (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:40–0:49 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | "Every stone a rule" — first "Deeper than..." refrain pattern |
| **Scene Context** | Robotiko's POV: raised phones, bright sealed faces, hopeful and demanding |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 2.5 Turbo (Standard, 1080p) — Static + no Element (budget) |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/4.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> POV shot: a crowd of people with raised phones, bright sealed faces glowing in phone-screen light. Subtle head micro-movements and phone-screen flicker. Overcast grey surroundings. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S05 — The First Reveal (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 0:50–0:59 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | First "Deeper than the blueprint" — structural spine begins |
| **Scene Context** | Exterior grey gives way to workshop interior — first Discovering Camera zoom-out |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/5.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> A blueprint pinned to a rough workshop wall, tools hanging, scrap metal on a bench. Warm rust tones emerging from cold grey. Dust motes drift in the first indoor light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SECTION 2: THE WORKSHOP — ARRIVAL & DEPARTURE (1:00–1:40)

---

### SHOT S06 — The Welcome (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:00–1:05 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 10s (trim 5s in CapCut) |
| **Musical Moment** | Hypnotic slow bass pulse enters, eerie electric saz |
| **Scene Context** | Workshop interior — mechanic at bench, tea glass, gestures Robotiko in |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/6.png`
- **End Frame:** N/A

**Camera Move:** Dolly In

**Motion Prompt:**
> Workshop interior: an old man in a greenish work coat stands by a workbench cluttered with tools and scrap metal. A Turkish tea glass steams on the bench. The @Damaged chrome android enters the doorway. Oil-dark walls, warm amber-yellow work lamp. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S07 — The Amber Pulse (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:06–1:12 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s in CapCut) |
| **Musical Moment** | Eerie saz sustain peak — amber coincides with saz peak |
| **Scene Context** | Mechanic under lamp, wrench held upright echoes Mentor — amber pulse fails |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/7.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> An old man in a greenish work coat holds a long wrench upright under a warm work lamp. Amber light pulses once on the wrench tip - a single warm flicker - then fades back to ordinary lamp-yellow. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **[AMBER PULSE]** — Single permitted amber moment of EP09 (Visual Signature).

---

### SHOT S08 — Digital Solomon (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:13–1:23 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | "Digital Solomon" — dry spoken word over heavy bass drone |
| **Scene Context** | Flashback: sovereign command bridge over ocean, data cascades, clinical separation |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/8.png`
- **End Frame:** N/A

**Camera Move:** Pan Right

**Motion Prompt:**
> A sovereign command bridge suspended over an ocean - glass walls, data cascading across screens, drones in formation above waves. Cold blue-steel palette, clinical separation. Data streams flicker across surfaces. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S09 — The Indifferent Beat (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:23–1:28 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 10s (trim 5s in CapCut) |
| **Musical Moment** | Bass drone continues — ordinary present against grandiose past |
| **Scene Context** | Mechanic at bench, working metal, not watching — the most ordinary person |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 2.5 Turbo (Standard, 1080p) — Static + no Element (budget) |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/9.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> An old man in a greenish work coat works a piece of metal at a bench. Tea glass half-empty beside him. He does not look up. Subtle hand movements only, remains in exact position. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S10 — Dry Behind Glass (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:28–1:34 |
| **Scene Duration** | 6s |
| **Coverage** | Direct — 1 × 10s (trim 4s in CapCut) |
| **Musical Moment** | "Deeper than the data" — second Discovering Camera zoom-out |
| **Scene Context** | Close-up glass surface, ocean beyond — near side dry, far side wet |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/10.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Extreme close-up of a glass surface - ocean visible beyond, far side wet with condensation, near side dry. Light refracts through the glass. Subtle moisture movement on the far side. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S11 — The Shutter (Direct, Mode B)

| Field | Value |
|---|---|
| **Timestamp** | 1:35–1:40 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 10s (trim 5s in CapCut) |
| **Musical Moment** | Dark creeping fuzz guitar enters, slow heavy heartbeat pulse |
| **Scene Context** | Mechanic pulls shutter down — day transforms to night, he goes home |
| **Tech Strategy** | Mode B |
| **Generation Mode** | Mode B (Start/End Keyframes) |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Mode B, 1080p, Omni Ref) — Mode B requires Kling 3.0 |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/11.png`
- **End Frame:** `episode-09/04_visuals/raw/11b.png`

**Camera Move:** Static

**Motion Prompt:**
> The silhouetted figure in the doorway pulls the roll-up shutter down - fading daylight narrows to a slit, then darkness. Tea glass on the bench catches the last light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SECTION 3: THE THREE FAILURES (1:41–3:43)

---

### SHOT S12 — Self-Surgery (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:41–1:50 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | Tense spoken word over heartbeat drum — blade turns inward |
| **Scene Context** | Chest panel open, hand reaching inside own mechanism — single-body self-surgery |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/12.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The @Damaged chrome android at a workbench, chest panel open, one hand reaching inside the mechanism. A single hard white work lamp throws deep shadows. Orange sparks drift from exposed wires. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S13 — The Shadow Grips (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:51–1:56 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 10s (trim 5s in CapCut) |
| **Musical Moment** | "Deeper than the self" — third Discovering Camera zoom-out |
| **Scene Context** | Close-up hand gripping inside open chest — shadow hand closes on nothing |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/13.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Close-up: chrome hand gripping inside an open chest cavity, reaching into dark interior. Hard white lamp casts a large shadow on the workshop wall behind. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S14 — The Inversion (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 1:57–2:05 |
| **Scene Duration** | 8s |
| **Coverage** | Direct — 1 × 10s (trim 2s in CapCut) |
| **Musical Moment** | Heavy hypnotic fuzz rock — chorus energy, "I fix the code" |
| **Scene Context** | Shadow starts leading — the debugger being debugged |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/14.png`
- **End Frame:** N/A

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android at the workbench, hard lamp flickering and unstable. Shadows shift on the wall behind. Sparks arc intermittently from exposed wires. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **Shadow Note:** Shadow's autonomous leading behavior = CapCut compositing. Motion prompt covers light flicker + sparks only.

---

### SHOT S15 — Shadow World (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:06–2:11 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 10s (trim 5s in CapCut) |
| **Musical Moment** | "The code fixed me" — rhythmic fuzz sustain |
| **Scene Context** | Shadow dominates frame — Robotiko small beneath, inversion complete |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/15.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android stands small in the foreground, dim and diminished. A massive shadow dominates the wall behind - sharp, dark, filling the frame. Lamp flickers, casting shifting light. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S16 — Aftermath (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:12–2:21 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | Single dark drone — heavy silence, near-total void |
| **Scene Context** | Heavy silence, arms at sides, chest open — the weight of the inversion lingers |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/16.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android stands still in the workshop, arms at sides, chest panel open. Dim lamp barely illuminating. Dust settles, no sparks. Shadow normal-sized on the wall. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S17 — The Mirror (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:22–2:31 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | Ghostly whispery spoken word, minimal synth drone |
| **Scene Context** | Cracked workshop glass — reflection has no face, chrome where features should be |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/17.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The @Damaged chrome android stands before a cracked piece of glass leaning against the wall. Reflection visible - chrome without features where the face should be. Light refracts through cracks. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **[CHROME REFLECTION]** — Action shown through reflective surface (Visual Signature).

---

### SHOT S18 — The Hand Passes Through (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:32–2:41 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | "Deeper than reflection" — fourth Discovering Camera zoom-out |
| **Scene Context** | Chrome hand meets glass surface and passes through — no resistance |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/18.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Close-up: a chrome hand reaches toward a cracked glass surface. The hand meets the surface and seems to pass through - no resistance. Ghostly dim light, glass-fragmented refractions. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S19 — The Doom (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:42–2:52 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Heavy slow tribal drum hit + fuzz guitar — first real percussive weight |
| **Scene Context** | Workshop in deepening shadow, Robotiko small, doom atmosphere |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + accent camera |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/19.png`
- **End Frame:** N/A

**Camera Move:** Crane Down

**Motion Prompt:**
> Wide shot of the workshop in deepening shadow. The @Damaged chrome android sits small at the bench, tools scattered. Metal surfaces vibrate subtly, dust lifts from the bench. Extremely heavy, visible film grain. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **[GRAIN CRESCENDO]** begins — film grain thickens through S19–S23.

---

### SHOT S20 — The Pull (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 2:53–3:02 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | Heavy exhausted spoken word — "I pulled the plug" |
| **Scene Context** | Reaches behind neck and pulls a cable — work lamp dims as power drains |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/20.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The @Damaged chrome android reaches behind its own neck and slowly pulls a cable - the work lamp dims as power drains from the body. Workshop begins to darken. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S21 — Total Darkness (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:03–3:12 |
| **Scene Duration** | 9s |
| **Coverage** | Direct — 1 × 10s (trim 1s in CapCut) |
| **Musical Moment** | "Deeper than the void" — fifth Discovering Camera zoom-out |
| **Scene Context** | Near-total darkness — faintest dying blue from where eyes were |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/21.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Near-total darkness. The faintest blue pinpoint reflected in the dark amber glass lenses where the chrome android's eyes were. No lamp, no workshop details visible - only shadow and void. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S22 — The Build (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:13–3:18 |
| **Scene Duration** | 5s |
| **Coverage** | Direct — 1 × 10s (trim 5s in CapCut) |
| **Musical Moment** | Rising tribal drums + dark saz — short aggressive build toward peak |
| **Scene Context** | Systems rebooting, lamp blazes on strobing, shadow thrashing |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + accent camera |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/22.png`
- **End Frame:** N/A

**Camera Move:** Handheld

**Motion Prompt:**
> The workshop shudders back to harsh light - the @Damaged chrome android's systems rebooting. Lamp blazes on, unstable, strobing. Sparks arc from exposed joints. Extremely heavy, visible film grain. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **[GRAIN CRESCENDO]** peaks here — maximum grain weight.

---

### SHOT S23 — I Am The Bug (Speed Ramp) — [DISSONANCE]

| Field | Value |
|---|---|
| **Timestamp** | 3:19–3:30 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | Massive doom rock — "I AM THE BUG" — track's emotional apex |
| **Scene Context** | STILL HOLD: every light blazing, sparks arcing, camera absolutely still — [DISSONANCE] |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.91× (10s → 11s) |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + emotional apex |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/23.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> Every practical light in the workshop blazes and flickers simultaneously. The @Damaged chrome android stands at the workbench, chest panel open, sparks arcing from exposed wires into the dim air. Extremely heavy, visible film grain. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **[DISSONANCE]** — Explosive music + static camera. The Discovering Camera does not flinch.
> **Shadow Note:** Shadow thrashing = CapCut compositing (hard-light keyframes). Not in motion prompt.

---

### SHOT S24 — The Collapse (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 3:31–3:43 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | Doom atmosphere, fuzz guitar — post-climax decompression |
| **Scene Context** | Hand drops, tool falls, shadow deflates — violence exhausted itself |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/24.png`
- **End Frame:** N/A

**Camera Move:** Dolly Out

**Motion Prompt:**
> The @Damaged chrome android's hand drops to the bench. A tool falls from its grip. Workshop debris settles, lamp steadying to a dim glow. Dust drifting down. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SECTION 4: THE TURN — INTEGRATION (3:44–5:04)

---

### SHOT S25 — The Unsolvable (Speed Ramp) — STILL HOLD

| Field | Value |
|---|---|
| **Timestamp** | 3:44–3:57 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Pure silence — a cappella spoken word, no instruments at all |
| **Scene Context** | Face close-up, near-darkness — "I am the unsolvable" — the philosophical core |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.77× (10s → 13s) |
| **Motion Strength** | 1 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + face close-up |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/25.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> Close-up of the @Damaged chrome android's face in near-darkness. Calm steady blue eyes. Single dim ambient glow. Absolutely still - barely perceptible breathing, no movement. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **[STILL HOLD]** — Primary Still Hold of EP09. Static + MS 1 after S22 (MS 6) and S23 (MS 5). The stillness IS the punch.

---

### SHOT S26 — The Turn (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 3:58–4:08 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Slow melancholic saz + brooding synth — grief toward acceptance |
| **Scene Context** | Hand passes blade and tools, picks up rusted scrap — first warmth returns |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Damaged |
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/26.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The @Damaged chrome android's hand moves across the workbench - past tools, past a blade. It picks up a piece of rusted scrap metal. Scraps glint in low warm light. First warmth returning. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S27 — The Glitch Is Scripture (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 4:09–4:28 |
| **Scene Duration** | 19s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim 1s in CapCut) |
| **Musical Moment** | Warm spoken word — "the glitch is scripture... Deeper than the wound" |
| **Scene Context** | CAMERA STOPS. Phase 2→3 transition — first gold flows from cracks. Sixth Discovering Camera reveal. |

#### Clip A — S27a (Mode B — Gold Progression)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode B |
| **Generation Mode** | Mode B (Start/End Keyframes) |
| **Element Tags** | @Damaged |
| **Recommended Tool** | Kling 3.0 (Mode B, 1080p, Omni Ref) — Mode B + Element + phase transition |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/27.png`
- **End Frame:** `episode-09/04_visuals/raw/27b.png`

**Camera Move:** Static

**Motion Prompt:**
> The @Damaged chrome android presses a piece of rusted scrap against its cracked chassis. Gold light begins to flow from the junction, spreading slowly through the crack. Warm glow intensifying. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **Phase 3 transition:** @Damaged start → first gold in cracks. Mode B handles the visual progression.

#### Clip B — S27b (Sixth Reveal)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/27b.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> The @Kintsugi chrome android at the workbench, gold light flowing through cracks in the chassis. Mismatched scrap metal pieces gathered around. Gold glow intensifying, spreading through the body. The perspective widens. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S28 — Gold Spreading (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 4:29–4:39 |
| **Scene Duration** | 10s |
| **Coverage** | Direct — 1 × 10s |
| **Musical Moment** | Brooding saz + slow heavy fuzz swelling — Kintsugi build |
| **Scene Context** | Close-up gold flowing through multiple cracks, bioluminescent core beginning |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Clip Duration** | 10s |
| **Motion Strength** | 4 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/28.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> Close-up: gold flowing through multiple cracks in a chrome chassis. Bioluminescent core beginning to glow beneath patches of translucent digital skin. Mismatched scrap pieces welded into place. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S29 — The Lighting Flip (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 4:40–4:52 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | Chorus 3 — massive fuzz rock wall, tribal drums, saz — "Revealing" |
| **Scene Context** | THE LIGHTING FLIP: external lamp dims, internal core brightens — self-luminous |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 5 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/29.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> The external work lamp dims visibly as the @Kintsugi chrome android's body glows from within - core light radiating through gold-filled cracks and translucent skin. Shadow on the wall softens into gentle contrast. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **Lighting = Philosophy:** External (sought from outside) → internal (found in own cracks). S07 amber (fails) → S29 gold (succeeds). Static justified: the lighting change IS the action.

---

### SHOT S30 — Full Kintsugi (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 4:53–5:04 |
| **Scene Duration** | 11s |
| **Coverage** | Speed Ramp — 1 × 10s → 11s at 0.91× |
| **Musical Moment** | Pounding tribal drums + wailing saz — "Deeper than the scar" |
| **Scene Context** | Widest interior zoom-out — full kintsugi body revealed, self-luminous |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.91× (10s → 11s) |
| **Motion Strength** | 6 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/30.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Full body: the @Kintsugi chrome android standing in the workshop - mismatched scavenged panels welded with gold in the seams, translucent digital skin revealing bioluminescent core. Self-luminous, lighting the space. Shadow as warm contrast on the wall. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SECTION 5: THE BECOMING (Outro Vocals, 5:05–5:45)

---

### SHOT S31 — The Frame That Glows (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 5:05–5:17 |
| **Scene Duration** | 12s |
| **Coverage** | Speed Ramp — 1 × 10s → 12s at 0.83× |
| **Musical Moment** | Dry intimate spoken word + wind entering + distant clarinet |
| **Scene Context** | Gold-cracked body self-luminous, wind entering through shutter gaps |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.83× (10s → 12s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/31.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom In

**Motion Prompt:**
> The @Kintsugi chrome android standing in the workshop, gold-cracked body self-luminous. Wind beginning to enter through gaps in the shutter. Warm internal radiance, dust motes stirring. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S32 — It Holds Me (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 5:18–5:31 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Spoken word fading — "it holds me" |
| **Scene Context** | Lamp off, core-glow IS the light source — tools, bench, tea glass all lit by him |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.77× (10s → 13s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/32.png`
- **End Frame:** N/A

**Camera Move:** Pan Left

**Motion Prompt:**
> The @Kintsugi chrome android in the workshop - self-luminous body lighting the space. Wind stirring dust and metal shavings. Lamp off - the core-glow illuminates tools, bench, and tea glass around it. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S33 — I— (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 5:32–5:45 |
| **Scene Duration** | 13s |
| **Coverage** | Speed Ramp — 1 × 10s → 13s at 0.77× |
| **Musical Moment** | Final "I—" hangs unresolved — music dissolves |
| **Scene Context** | Face close-up, gold-cracked — sentence never finishes, frame holds |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.77× (10s → 13s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + face close-up |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/33.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> Close-up: calm steady blue eyes set in gold-cracked chrome surface. Warm internal radiance. Gold slowly pulsing in the cracks. Minimal atmospheric particles. The frame holds. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **Near-Still-Hold:** The unfinished sentence suspended in time. 0.77x speed ramp deepens the suspension.

---

### SECTION 6: THE DAWN PULL (Outro Instrumental, 5:46–7:03)

> The widest pull of the series: 77 seconds, 5 scenes, 8 clips. Frame chaining locks visual continuity.

---

### SHOT S34 — The Pull Begins (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 5:46–6:00 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Slow heavy fuzz guitar solo begins — dark psychedelic groove |
| **Scene Context** | Close-medium: Robotiko at bench, luminous — camera starts its long retreat |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 3 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |
| **Frame Chain** | Chain 1 START |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/34.png`
- **End Frame:** N/A

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> The @Kintsugi chrome android at the bench, gold-cracked body luminous. Core-glow lighting immediate surroundings - tea glass, tools, scrap metal on the bench. Warm gold light against oil-dark workshop walls. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S35 — The Workshop Revealed (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 6:01–6:20 |
| **Scene Duration** | 19s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim 1s in CapCut) |
| **Musical Moment** | Fuzz guitar solo continues — groove building then dissolving |
| **Scene Context** | Full workshop visible — Robotiko luminous at center, gold leaking from building seams |

#### Clip A — S35a (Workshop Scan)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 3 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |
| **Frame Chain** | ← S34 (last frame) |

**Assets Required:**
- **Start Frame:** `← S34 (last frame)` | Fallback: `episode-09/04_visuals/raw/35.png`

**Camera Move:** Pan Left

**Motion Prompt:**
> Full workshop visible - oil-dark walls, hanging tools, roll-up shutter closed. A luminous figure at center radiates gold light. Gold light leaking from the building's own seams - cracks in walls, floor edges, shutter seams. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S35b (Workshop Retreat)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | @Kintsugi |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — Element + camera move |
| **Frame Chain** | ← S35a (last frame) — Chain 1 END |

**Assets Required:**
- **Start Frame:** `← S35a (last frame)` | Fallback: `episode-09/04_visuals/raw/35.png`

**Camera Move:** Dolly Out

**Motion Prompt:**
> The workshop recedes - gold light from the luminous figure at center illuminates every surface. Oil-dark walls, shutter closed. Gold leaking from cracks in the walls and floor. Wind stirring dust. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S36 — Through The Shutter (Multi-Clip: 2 clips)

| Field | Value |
|---|---|
| **Timestamp** | 6:21–6:40 |
| **Scene Duration** | 19s |
| **Coverage** | Multi-Clip — 2 × 10s = 20s (trim 1s in CapCut) |
| **Musical Moment** | Guitar solo dissolving — wind entering, music fading |
| **Scene Context** | Camera passes through/past the shutter into dawn — threshold between repair and world |

#### Clip A — S36a (Through The Shutter)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — camera move |
| **Frame Chain** | Chain 2 START |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/36.png`

**Camera Move:** Dolly In

**Motion Prompt:**
> The camera moves toward or past a partially open roll-up metal shutter. Dawn light from outside mixes with warm gold light from within. The threshold between workshop interior and exterior world. Wind rising. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

#### Clip B — S36b (Dawn Breaks)

| Field | Value |
|---|---|
| **Clip Duration** | 10s |
| **Motion Strength** | 2 |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — camera move |
| **Frame Chain** | ← S36a (last frame) — Chain 2 END |

**Assets Required:**
- **Start Frame:** `← S36a (last frame)` | Fallback: `episode-09/04_visuals/raw/36.png`

**Camera Move:** Slow Zoom Out

**Motion Prompt:**
> Dawn light mixing with gold light at a workshop threshold. The workshop recedes behind as warm first light fills the frame. Wind stirring metal shavings and dust at the shutter edge. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S37 — The Dawn (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | 6:41–6:55 |
| **Scene Duration** | 14s |
| **Coverage** | Speed Ramp — 1 × 10s → 14s at 0.71× |
| **Musical Moment** | Music gradually dissolving into wind |
| **Scene Context** | Exterior dawn — workshop from outside, gold leaking from every seam |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Playback Speed** | 0.71× (10s → 14s) |
| **Motion Strength** | 2 |
| **Recommended Tool** | Kling 3.0 (Standard, 1080p, Omni Ref) — accent camera |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/37.png`
- **End Frame:** N/A

**Camera Move:** Crane Up

**Motion Prompt:**
> Exterior: warm dawn sky, first light. A metal workshop building seen from outside - gold light leaking from every seam, every crack in the metal walls, the shutter edges. Wind stirring the landscape. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

---

### SHOT S38 — The Ordinary World (Direct)

| Field | Value |
|---|---|
| **Timestamp** | 6:56–7:03 |
| **Scene Duration** | 7s |
| **Coverage** | Direct — 1 × 10s (trim 3s in CapCut) |
| **Musical Moment** | Fade to silence — wind — the final seconds |
| **Scene Context** | Widest shot of the series — workshop small in Anatolian dawn, tea glass visible |
| **Tech Strategy** | Mode A |
| **Generation Mode** | Standard |
| **Element Tags** | None |
| **Clip Duration** | 10s |
| **Motion Strength** | 1 |
| **Recommended Tool** | Seedance 1.0 (Standard, 1080p) — Static + no character (standalone landscape) |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/raw/38.png`
- **End Frame:** N/A

**Camera Move:** Static

**Motion Prompt:**
> Ultra-wide Anatolian dawn landscape. A small metal workshop building in the lower center, gold light leaking faintly from its seams. A tea glass barely visible through a gap. Wind stirring dust. Fade toward stillness. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

> **[GRAIN CRESCENDO]** inverts — grain lightens to near-clean as the dawn opens.
> **Fade to black:** Last 2-3s in CapCut.

---

## BEAT SYNC NOTES

| # | Timestamp | Musical Event | Required Visual Action | Clip Reference |
|---|---|---|---|---|
| 1 | 0:27 | "Nothing comes out" — held vocal silence | Face close-up hold, mouth opens, nothing | S03 |
| 2 | 1:06 | Saz sustain peak | Amber flicker on wrench tip — one pulse | S07 |
| 3 | 1:35 | Creeping fuzz guitar + heartbeat pulse enters | Shutter begins closing — Mode B transition | S11 |
| 4 | 1:41 | Tense heartbeat drum | Self-surgery begins — hand enters chest | S12 |
| 5 | 1:57 | Heavy fuzz rock chorus entry | Shadow starts leading — Dolly Out | S14 |
| 6 | 2:12 | Single dark drone — heavy silence | Aftermath: stillness, dust settling | S16 |
| 7 | 2:42 | First tribal drum hit | Doom frame vibration — metal resonates, dust lifts | S19 |
| 8 | 3:13 | Rising tribal drums + dark saz | Reboot — lamp strobing, sparks, Handheld | S22 |
| 9 | 3:19 | Massive doom rock — "I AM THE BUG" | Static camera, frame blazes [DISSONANCE] | S23 |
| 10 | 3:44 | Pure silence — a cappella | **STILL HOLD** — Static, MS 1, absolute stillness | S25 |
| 11 | 4:09 | "Glitch is scripture" — warm spoken word | Camera stops — first gold, Mode B | S27a |
| 12 | 4:40 | Chorus 3 — massive fuzz rock wall | Lighting flip — lamp dims, core brightens | S29 |
| 13 | 4:53 | Pounding tribal drums + wailing saz | Full kintsugi reveal — widest interior zoom-out | S30 |
| 14 | 5:32 | "I—" unfinished | Face close-up, frame holds, 0.77x suspension | S33 |
| 15 | 5:46 | Fuzz guitar solo begins | Dawn pull starts — Slow Zoom Out, Chain 1 | S34 |

---

## FRAME CHAIN MAP

| Chain | Clips | Location | Direction | Notes |
|---|---|---|---|---|
| **Chain 1** | S34 → S35a → S35b | Workshop interior | Continuous pull-back | Bench → full workshop → retreat. 3 clips (max). Last frame of each feeds next. |
| **Chain 2** | S36a → S36b | Threshold → dawn | Through the shutter | Interior gold + exterior dawn light mixing. 2 clips. |

> S37 and S38 are standalone — different exterior framings, no chain continuity needed.

---

## COVERAGE SUMMARY

| Metric | Value |
|---|---|
| **Total music duration** | 423s |
| **Total generated clip duration** | 410s (41 × 10s) |
| **Coverage ratio (raw)** | 97.0% (target >= 95%) |
| **Effective coverage (with speed ramps)** | 100% — all 423s covered |
| **Total clips** | 41 |
| **Clips from existing images** | 41 |
| **Clips needing new images** | 0 |
| **Speed Ramp clips** | 13 |
| **Multi-Clip scenes** | 3 (S27: 2 clips, S35: 2 clips, S36: 2 clips) |
| **Mode B clips** | 2 (S11, S27a) |
| **Frame-chained clips** | 5 (S34 → S35a → S35b, S36a → S36b) |

---

## CAMERA DIVERSITY REPORT

### Distribution

| Camera Move | Clips | % | Role |
|---|---|---|---|
| **Static** | S01, S04, S09, S11, S15, S16, S23, S25, S27a, S29, S33, S38 | 12 (29.3%) | Silence, witnessing, Still Hold, [DISSONANCE] |
| **Slow Zoom Out** | S02, S05, S10, S13, S18, S21, S27b, S30, S34, S36b | 10 (24.4%) | Discovering Camera signature — understanding widens |
| **Slow Zoom In** | S03, S07, S12, S17, S20, S26, S28, S31 | 8 (19.5%) | Intimacy, approach, tension |
| **Dolly Out** | S14, S24, S35b | 3 (7.3%) | Retreat, departure, collapse |
| **Pan Left** | S32, S35a | 2 (4.9%) | Scanning, environmental reveal |
| **Pan Right** | S08 | 1 (2.4%) | Flashback scanning |
| **Dolly In** | S06, S36a | 2 (4.9%) | Workshop entry, threshold crossing |
| **Handheld** | S22 | 1 (2.4%) | Instability, reboot chaos |
| **Crane Down** | S19 | 1 (2.4%) | Doom descending |
| **Crane Up** | S37 | 1 (2.4%) | Dawn ascending |

### Validation

| Rule | Target | Actual | Status |
|---|---|---|---|
| No single move > 30% | <= 30% | Static 29.3% (highest) | PASS |
| Static >= 15% | >= 15% | 29.3% | PASS |
| Accent moves (Handheld/Crane) <= 3 each | <= 3 | Handheld x1, Crane Down x1, Crane Up x1 | PASS |
| Every 5 consecutive clips >= 3 different moves | >= 3 | All 37 windows verified | PASS |
| Episode Camera Personality honored | Slow Zoom Out dominant | 24.4%, 10 clips, 2nd highest | PASS |

### The Six "Deeper Than" Zoom-Outs

| # | Scene | Lyric | Camera |
|---|---|---|---|
| 1 | S05 | "Deeper than the blueprint" | Slow Zoom Out |
| 2 | S10 | "Deeper than the data" | Slow Zoom Out |
| 3 | S13 | "Deeper than the self" | Slow Zoom Out |
| 4 | S18 | "Deeper than reflection" | Slow Zoom Out |
| 5 | S21 | "Deeper than the void" | Slow Zoom Out |
| 6 | S27b | "Deeper than the wound" | Slow Zoom Out |

---

## ART DIRECTION SIGNATURES

| Signature | Scene(s) | Usage |
|---|---|---|
| **Chrome Reflection** | S17 | Faceless reflection in cracked workshop glass |
| **Architecture Cage** | S08, S16 | Command bridge glass walls; workshop as cage in heavy silence |
| **Amber Pulse** | S07 | Single amber flicker on wrench tip — fails, collapses to lamp-yellow |
| **Still Hold** | S25 | Primary: Static + MS 1 after S22 (MS 6) / S23 (MS 5). The stillness IS the punch. |
| **Grain Crescendo** | S19-S23, S38 (invert) | Grain thickens S19-S23 (doom to peak), lightens at S38 (dawn opens) |

---

## DIRECTOR'S NOTES

### The Discovering Camera — How It Operates in EP09

The primary move (Slow Zoom Out) appears at every "deeper than" lyric moment, mapping the camera's physical pull-back to the text's philosophical widening. The zoom-out never means retreat — it means "you thought the close-up was the thing; the wider view shows it was part of something larger."

The camera personality has three behavioral modes:
1. **Active discovery** (S05, S10, S13, S18, S21, S27b, S30, S34) — Slow Zoom Out during reveals
2. **Cold witness** (S23) — Static during maximum violence. The camera records but does not participate. [DISSONANCE] with explosive music.
3. **Surrender** (S25, S33) — Still Hold. The camera stops because the paradox cannot be resolved by looking harder.

### Shadow Compositing Protocol (S12-S24)

The shadow's autonomous behavior (leading in S14-S15, thrashing in S22-S23, deflating in S24) is built with **hard-light keyframes + CapCut compositing**, NOT Kling motion generation. Motion prompts describe what Kling can animate:
- Lamp flicker and instability (S14, S15, S22, S23)
- Sparks from exposed wires (S12, S14, S22, S23)
- The shadow AS IT APPEARS in the source image (static element)

Do NOT instruct Kling to animate shadows independently. The shadow's autonomous behavior is post-production.

### Phase Transition at S27

The transition from @Damaged to @Kintsugi is handled in two steps:
- **S27a (Mode B):** Start = @Damaged (27.png), End = first gold (27b.png). Element tag = @Damaged (start state). Mode B handles the visual gold progression.
- **S27b onward:** @Kintsugi Element tag. Uses `android_kintsugi.png` as reference.

Gold is progressive — S27b shows early gold, S28-S30 show spreading gold, S31+ show full self-luminous kintsugi. Each motion prompt escalates the gold description accordingly.

### Tool Assignment Justification

EP09 runs 92.7% Kling 3.0 — higher than the 70-80% guideline. Justified:
- 32 of 38 scenes feature Robotiko (needs Elements for visual consistency)
- Most scenes have camera movement (only Kling 3.0 supports full camera vocabulary)
- Only 3 scenes are both Static AND character-free (S04, S09, S38)
- Budget tools assigned where possible: S04 + S09 (Kling 2.5 Turbo), S38 (Seedance)

### Energy Arc

```
S01 ##                  S22 ######
S02 ###                 S23 #####            [DISSONANCE]
S03 ##                  S24 ###
S04 ###                 S25 #                [STILL HOLD]
S05 ###                 S26 ###
S06 ###                 S27a ###
S07 ###                 S27b ####
S08 ####                S28 ####
S09 ##                  S29 #####
S10 ##                  S30 ######           [PEAK 2]
S11 ####                S31 ###
S12 ####                S32 ###
S13 ###                 S33 ##
S14 #####               S34 ###
S15 ####                S35a ###
S16 ##                  S35b ##
S17 ###                 S36a ##
S18 ###                 S36b ##
S19 #####               S37 ##
S20 ####                S38 #               [SILENCE]
S21 ##
```

MS Average: 3.15 (target: 3.0-3.5) — PASS

Two peaks: S22-S23 (violence — "I AM THE BUG") and S29-S30 (integration — full kintsugi). The valley between them (S25, MS 1) is the philosophical core. The dawn pull (S34-S38) fades linearly from 3 to 1.

---

## APPROVAL STATUS
- [x] **Human reviewed camera moves**
- [x] **Human reviewed tech strategy (Mode A/B)**
- [x] **Human reviewed duration coverage**
- [x] **Human reviewed tool assignments**
- [x] **Human generated supplementary images (if any)** — N/A (0 needed)
- [x] **Human approved**
- [x] **Ready for video generation**

> Video generation must NOT begin until this document is approved.

---

*"Would Fibula approve this?"*
*Ask before every delivery.*
