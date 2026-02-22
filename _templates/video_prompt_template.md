# VIDEO PRODUCTION SHEET (SEEDREAM / KLING / VEO)
> **Version:** 2.0 | Skill: `_skills/robotiko-motion-script/SKILL.md`
> This template is auto-populated by Claude. Do not fill manually.
> For video generation strategy rules, refer to `_management/pipeline_rules.md`

---

## PRE-GENERATION CHECKLIST (Claude reads these before writing a single motion prompt)

- [ ] `episode-{XX}/03_direction/ep{XX}_dramaturgy.md` → APPROVED scene breakdown
- [ ] `episode-{XX}/04_visuals/selected/` → Selected images confirmed
- [ ] `episode-{XX}/02_music/ep{XX}_musical_metadata.json` → Beat sync reference
- [ ] `_management/master.md` → Tone, station, energy arc

> ⚠️ Selected images must exist before this file is generated.
> ⚠️ Motion script must be approved by human before any video generation begins.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP{XX} |
| **Title** | [Episode Title] |
| **Station** | [The X Self] |
| **Dominant Energy** | [e.g., building / explosive / desolate / hypnotic] |
| **Total Shots** | [Number] |
| **Total Duration** | [MM:SS] |

---

## VIDEO STRATEGY REFERENCE

| Mode | When to Use | Input | Duration |
|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, no transformation | 1 image | 5s |
| **B — Start/End Keyframes** | Transformations, morphing, travel, character state changes | 2 images | 5s or 10s |
| **C — Extension** | Continuous long takes, slow pans, sustained atmosphere | 1 image + prev clip | Variable |

**Motion Strength Scale:** 1 = Barely breathing / 5 = Cinematic drama / 10 = Chaos and disintegration

---

## MOTION SCRIPT

---

### SHOT S{XX} — [Shot Title]

| Field | Value |
|---|---|
| **Timestamp** | [MM:SS] |
| **Musical Moment** | [What is happening in the music — e.g., "Hammond swirl peaks, drum roll begins"] |
| **Scene Context** | [One sentence from approved dramaturgy] |
| **Tech Strategy** | [Mode A / Mode B / Mode C] |
| **Duration** | [5s / 10s] |
| **Motion Strength** | [1-10] |

**Assets Required:**
- **Start Frame:** `episode-{XX}/04_visuals/selected/ep{XX}_s{XX}_selected.png`
- **End Frame:** `episode-{XX}/04_visuals/selected/ep{XX}_s{XX}_selected.png` *(Mode B only — else N/A)*

**Camera Move:** [Pan Left / Pan Right / Slow Zoom In / Slow Zoom Out / Tilt Up / Tilt Down / Static / Handheld / Crane Up / Crane Down]

**Motion Prompt:**
> [Director's Note: Precise description of the movement, atmosphere, and emotional intent. Reference the musical moment. Describe what should feel alive in the frame.]

---

### SHOT S{XX} — [Shot Title]

| Field | Value |
|---|---|
| **Timestamp** | [MM:SS] |
| **Musical Moment** | [...] |
| **Scene Context** | [...] |
| **Tech Strategy** | [...] |
| **Duration** | [...] |
| **Motion Strength** | [...] |

**Assets Required:**
- **Start Frame:** [...]
- **End Frame:** [...] *(or N/A)*

**Camera Move:** [...]

**Motion Prompt:**
> [...]

---

*(Continue pattern for all shots)*

---

## BEAT SYNC NOTES
*(Claude flags critical musical moments that require precise visual sync)*

| Timestamp | Musical Event | Required Visual Action |
|---|---|---|
| [MM:SS] | [e.g., Snare drum solo drop] | [e.g., Chain explosion — must land on beat] |
| [MM:SS] | [e.g., Hammond organ swell] | [e.g., Slow zoom out begins here] |
| [MM:SS] | [e.g., Chorus explosion] | [e.g., Cut to wide shot — maximum impact] |

---

## APPROVAL STATUS
- [ ] **Human reviewed camera moves**
- [ ] **Human reviewed tech strategy (Mode A/B/C)**
- [ ] **Human approved**
- [ ] **Ready for video generation**

> ⛔ Video generation must NOT begin until this document is approved.