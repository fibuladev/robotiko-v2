# VIDEO PRODUCTION SHEET (KLING / VEO / SEEDANCE)
> **Version:** 5.2 | Skill: `_skills/robotiko-motion-script/SKILL.md`
> This template is auto-populated by Claude. Do not fill manually.
> For video generation strategy rules, refer to `_management/pipeline_rules.md`

---

## PRE-GENERATION CHECKLIST (Claude reads these before writing a single motion prompt)

- [ ] `episode-09/03_direction/ep09_dramaturgy.md` → APPROVED scene breakdown
- [ ] `episode-09/04_visuals/selected/` → Selected images confirmed
- [ ] `episode-09/02_music/ep09_musical_metadata.json` → Beat sync reference
- [ ] `_management/master.md` → Tone, station, energy arc

> ⚠️ Selected images must exist before this file is generated.
> ⚠️ Motion script must be approved by human before any video generation begins.
> ⚠️ Supplementary images (if flagged) must be generated before video production starts.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP09 |
| **Title** | [Episode Title] |
| **Station** | [The X Self] |
| **Dominant Energy** | [e.g., building / explosive / desolate / hypnotic] |
| **Total Shots** | [Number of dramaturgy scenes] |
| **Total Clips** | [Number including sub-clips] |
| **Total Duration** | [MM:SS] |

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

> Claude generates this section based on Step 7 (Tool Assignment Analysis) from the motion-script skill.

### Tool Distribution

| Tool | Clips | Credits Used | Budget | Buffer | Assignment Logic |
|---|---|---|---|---|---|
| **[Tool 1]** | [N] | [X] | [Y] | [Z] | [Brief logic] |
| **[Tool 2]** | [N] | [X] | [Y] | [Z] | [Brief logic] |
| **TOTAL** | **[N]** | — | — | — | — |

### Assignment Rules Applied

1. [Rule 1 — e.g., "Mode B → Kling only"]
2. [Rule 2 — e.g., "Map shots → Seedance 1.0"]
3. [Rule 3]
4. [Rule 4]

### Clips by Tool

**[Tool 1] ([N]):** [clip list]

**[Tool 2] ([N]):** [clip list]

---

## MOTION SCRIPT

---

### SHOT S{XX} — [Shot Title] (Direct)

| Field | Value |
|---|---|
| **Timestamp** | [MM:SS–MM:SS] |
| **Scene Duration** | [Xs] |
| **Coverage** | Direct — 1 × [5s/10s] |
| **Musical Moment** | [What is happening in the music] |
| **Scene Context** | [One sentence from approved dramaturgy] |
| **Tech Strategy** | [Mode A / Mode B] |
| **Clip Duration** | [5s / 10s] |
| **Motion Strength** | [1-10] |
| **Recommended Tool** | [Tool name (Mode, resolution) — rationale] |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/selected/ep09_s{XX}_selected.png`
- **End Frame:** `episode-09/04_visuals/selected/ep09_s{XX}_selected.png` *(Mode B only — else N/A)*

**Camera Move:** [From approved vocabulary]

**Motion Prompt:**
> [Pure visual/motion description for the video generation tool — no character names, no music references]
> Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S{XX} — [Shot Title] (Speed Ramp)

| Field | Value |
|---|---|
| **Timestamp** | [MM:SS–MM:SS] |
| **Scene Duration** | [Xs] |
| **Coverage** | Speed Ramp — 1 × 10s → [Xs at 0.X×] |
| **Musical Moment** | [What is happening in the music] |
| **Scene Context** | [One sentence from approved dramaturgy] |
| **Tech Strategy** | [Mode A / Mode B] |
| **Clip Duration** | 10s |
| **Playback Speed** | [e.g., 0.7× (10s → 14s)] |
| **Motion Strength** | [1-10] |
| **Recommended Tool** | [Tool name (Mode, resolution) — rationale] |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/selected/ep09_s{XX}_selected.png`
- **End Frame:** N/A

**Camera Move:** [From approved vocabulary]

**Motion Prompt:**
> [Pure visual/motion description — no character names, no music references, no speed ramp technical notes]
> Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

### SHOT S{XX} — [Shot Title] (Multi-Clip: N clips)

| Field | Value |
|---|---|
| **Timestamp** | [MM:SS–MM:SS] |
| **Scene Duration** | [Xs] |
| **Coverage** | Multi-Clip — N × [5s/10s] = [Xs total] |
| **Musical Moment** | [Overall musical context for this scene] |
| **Scene Context** | [One sentence from approved dramaturgy] |

#### Clip A — S{XX}a

| Field | Value |
|---|---|
| **Clip Duration** | [5s / 10s] |
| **Motion Strength** | [1-10] |
| **Tech Strategy** | [Mode A / Mode B] |
| **Recommended Tool** | [Tool name (Mode, resolution) — rationale] |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/selected/ep09_s{XX}_selected.png`

**Camera Move:** [From approved vocabulary]

**Motion Prompt:**
> [Pure visual/motion description for this sub-clip — no character names, no music references]
> Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip B — S{XX}b

| Field | Value |
|---|---|
| **Clip Duration** | [5s / 10s] |
| **Motion Strength** | [1-10] |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | [Tool name (Mode, resolution) — rationale] |

**Assets Required:**
- **Start Frame:** `episode-09/04_visuals/selected/ep09_s{XX}_selected.png` *(same image, different camera move)*

**Camera Move:** [From approved vocabulary — different from Clip A]

**Motion Prompt:**
> [Pure visual/motion description for this sub-clip — no character names, no music references]
> Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

#### Clip C — S{XX}c (if needed — with supplementary image)

| Field | Value |
|---|---|
| **Clip Duration** | [5s / 10s] |
| **Motion Strength** | [1-10] |
| **Tech Strategy** | Mode A |
| **Recommended Tool** | [Tool name (Mode, resolution) — rationale] |

**Assets Required:**
- **Start Frame:** ⚠️ NEW IMAGE REQUIRED

**Supplementary Visual Prompt:**
> [Full visual prompt with mandatory suffix — ready to paste into Nano Banana]

**Expected Selected Image:** `episode-09/04_visuals/selected/ep09_s{XX}c_selected.png`

**Camera Move:** [From approved vocabulary]

**Motion Prompt:**
> [Pure visual/motion description for this sub-clip — no character names, no music references]
> Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

---

*(Continue pattern for all shots)*

---

## BEAT SYNC NOTES
*(Claude flags critical musical moments that require precise visual sync)*

| Timestamp | Musical Event | Required Visual Action | Clip Reference |
|---|---|---|---|
| [MM:SS] | [e.g., Snare drum solo drop] | [e.g., Chain explosion — must land on beat] | S{XX} / S{XX}a |
| [MM:SS] | [e.g., Hammond organ swell] | [e.g., Slow zoom out begins here] | S{XX}b |

---

## COVERAGE SUMMARY

| Metric | Value |
|---|---|
| **Total music duration** | [seconds] |
| **Total generated clip duration** | [seconds] |
| **Coverage ratio** | [percentage] |
| **Total clips** | [number] |
| **Clips from existing images** | [number] |
| **Clips needing new images** | [number] |

---

## APPROVAL STATUS
- [ ] **Human reviewed camera moves**
- [ ] **Human reviewed tech strategy (Mode A/B)**
- [ ] **Human reviewed duration coverage**
- [ ] **Human reviewed tool assignments**
- [ ] **Human generated supplementary images (if any)**
- [ ] **Human approved**
- [ ] **Ready for video generation**

> ⛔ Video generation must NOT begin until this document is approved.
