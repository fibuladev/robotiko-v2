# SKILL: robotiko-capcut-editor
> **Version:** 1.0
> **Trigger:** `"Edit EP{XX} in CapCut"`
> **Output:** `episode-{XX}/06_edit/ep{XX}_capcut_guide_v{VV}.md`

---

## PURPOSE

Generate an episode-specific CapCut editing guide that walks the human through the complete post-production assembly: from importing raw clips to exporting the final 1080p video. The guide translates the motion script's shot sequence into a concrete timeline map with exact timestamps, speed ramp values, beat sync checkpoints, transition decisions, and effect settings.

Final delivery is 1080p — the AI-generated source material is 1080p native, and upscaling adds no information.

This skill bridges the gap between video generation (Phase 4) and final delivery (Phase 6). It ensures every episode receives the same cinematic post-production treatment regardless of which AI tools generated the clips.

---

## PREREQUISITE

> **Three conditions must be met before this skill executes:**
> 1. All video clips must be generated and selected (`episode-{XX}/05_video/selected/` populated).
> 2. The approved motion script must exist (`episode-{XX}/05_video/ep{XX}_motion_script_v{VV}.md`).
> 3. The audio file must exist (`episode-{XX}/02_music/ep{XX}_audio_v{VV}.wav` or `.mp3`).
>
> If any condition is not met, STOP. Inform the human.

---

## MANDATORY INPUTS (Read Before Generating the Guide)

Read these files in this exact order:

| # | File | What to Extract |
|---|---|---|
| 1 | `episode-{XX}/05_video/ep{XX}_motion_script_v{VV}.md` | Shot sequence, timestamps, clip durations, speed ramp values, camera moves, tool assignments, beat sync notes, coverage summary |
| 2 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | BPM, sections with timestamps, energy levels per section |
| 3 | `episode-{XX}/05_video/selected/` | Verify which selected video clips exist (file listing) |
| 4 | `_management/master.md` | Episode phase, character state, visual aesthetic rules |
| 5 | `_management/pipeline_rules.md` | CapCut Post-Production Protocol, QA checklist |

**If selected video clips are missing:** STOP. List which clips are absent. The timeline cannot have gaps.
**If musical metadata is missing:** STOP. Beat sync verification is impossible without temporal data.

---

## PRE-GENERATION ANALYSIS

### Step 1: Inventory Selected Clips
- List all files in `05_video/selected/`
- Map each `ep{XX}_s{XX}_selected.mp4` (and sub-clips `s{XX}a`, `s{XX}b`, etc.) to its corresponding shot in the motion script
- Flag any missing clips — every shot in the motion script must have a corresponding video file
- Note the source tool for each clip (from filename suffix: `_kling`, `_veo`, `_seedance`)

### Step 2: Extract Timeline Grid
- From the motion script, build the complete shot sequence:
  - Shot ID → Timestamp → Scene Duration → Clip Duration → Speed Ramp (if any)
  - Multi-clip scenes: list all sub-clips in order
- From the musical metadata, extract BPM and section boundaries
- Calculate: `total_timeline = sum of all scene durations` — must equal music duration (±1s)

### Step 3: Identify Tool-Specific Adjustments
- **Kling clips (3.0 & 2.5 Turbo):** 5s or 10s native. Trim to scene duration in CapCut.
- **Veo clips:** ~8s native. May need slight speed adjustment to match scene duration.
- **Seedance clips:** 5s or 10s native. Trim to scene duration in CapCut.
- Note which clips need speed correction vs. simple trimming.

### Step 4: Map Beat Sync Points
- Extract the Beat Sync Notes table from the motion script
- Cross-reference with musical metadata section boundaries
- Identify which clip boundaries must land exactly on which beats
- These become the mandatory verification points in the guide

### Step 5: Determine Transition Points
- Default: **Hard cut** (the majority of transitions)
- Apply transition rules (see Transition Strategy section below)
- Map each transition to a specific point between two shots

---

## WORKFLOW (9-Phase Assembly)

The generated guide walks the human through these phases in order:

### Phase 1: Project Setup
- Create new CapCut project: **1080p (1920×1080), 24fps, 16:9**
- Import the episode's audio track to the main audio timeline
- Import all selected video clips from `05_video/selected/`
- Run **Auto Beat Detection** on the audio track to generate beat markers
- Create a dedicated **Adjustment Layer** track (for global effects later)

### Phase 2: Timeline Assembly
- Place clips on the video track in motion script order (S01 → last shot)
- Match each clip's start position to its timestamp from the motion script
- Multi-clip scenes: place sub-clips sequentially (e.g., S24a → S24b → S24c)
- **CapCut-Only clips:** Some shots bypass video generation entirely — they use a static source image placed directly on the timeline with CapCut keyframe animation (e.g., cursor movement on a CRT screen). Check the motion script for shots marked "CapCut-Only" and follow their inline CapCut Instructions.
- Leave no gaps — every second of audio must have corresponding video
- Preliminary trim: rough-cut each clip to approximate scene duration

### Phase 3: Trim & Speed Ramp
For each clip, apply one of these strategies (from the motion script):

| Strategy | Action |
|---|---|
| **Direct (≤10s)** | Trim clip to exact scene duration. Cut from the end unless motion script specifies otherwise. |
| **Speed Ramp** | Apply speed curve: set playback speed to the rate specified in the motion script (e.g., 0.71×). Verify resulting duration matches scene duration. |
| **Multi-Clip** | Each sub-clip trimmed individually. Total duration of all sub-clips = scene duration. |
| **Veo Adjustment** | Veo clips are ~8s native. If scene is 8-9s, trim. If scene requires different duration, apply minor speed adjustment. |

After all clips are placed and adjusted:
- Verify **total timeline duration = music duration** (±1s tolerance)
- If timeline is short: identify which clip(s) can absorb extra frames
- If timeline is long: identify which clip(s) have trimmable excess

### Phase 4: Beat Sync Verification
- Enable beat marker visibility on the audio track
- Walk through each critical sync point from the Beat Sync Notes table:
  - Does the visual action (cut, eruption, impact) land on the beat marker?
  - If not, adjust clip boundary by frames until it does
- Pay special attention to:
  - **Chorus entries** — visual cuts must hit the first beat of the chorus
  - **Drum fills/drops** — impact shots must land on the downbeat
  - **Silence/breakdowns** — visual stillness must begin exactly when music drops
- Mark any clips that cannot be sync'd without compromising neighboring clips — flag for human decision
- After export, record the measured spot-checks in `episode-{XX}/06_edit/ep{XX}_sync_qc_v01.md` (from `_templates/ep_sync_qc_template.md`, min 5 checks) — the committed evidence CI cannot produce, since the render is gitignored. See `_management/pipeline_rules.md` (Step 11, Sync-QC Record).

### Phase 5: Transition Strategy
Apply transitions between shots using these rules:

| Transition Type | When to Use | Duration |
|---|---|---|
| **Hard Cut** | Default. Between most shots. Between sub-clips within the same scene. | Instant |
| **Cross Dissolve** | Map/location transitions only (map shot → location shot). Creates geographic flow. | 0.5-1s |
| **Light Leak** | Chorus entries only. Maximum 3 per episode. Warm amber tone only. | 0.5-1s |
| **Fade to Black** | Final shot of the episode only. | 2-3s |

**FORBIDDEN transitions:** Glitch, zoom, spin, slide, wipe, swipe, shape, or any "trendy" preset. These break the analog aesthetic.

**Multi-clip scenes:** Sub-clips within the same scene (e.g., S24a → S24b → S24c) use **hard cuts** — they are meant to feel like continuous coverage, not separate scenes.

### Phase 6: Global Effects (Adjustment Layer)
Apply these effects to the Adjustment Layer spanning the full timeline. Order matters — apply in this sequence:

| # | Effect | Setting | Notes |
|---|---|---|---|
| 1 | **Kodachrome LUT** | Import .cube file → Apply | See LUT Guide below. Sets the base color palette. |
| 2 | **Color Match** | Select reference clip → Match all | Choose the clip with the best Kodachrome warmth as reference. |
| 3 | **Film Grain** | 10-15% intensity | Breaks AI smoothness. Apply via Filters → Vintage → Film Grain. Adjust with Filter Parameter slider. |
| 4 | **Vignette** | Subtle (15-25%) | Darkens frame edges. Pulls focus to center. Mimics older lens limitations. |
| 5 | **Letterbox 2.35:1** | Custom aspect ratio | Player panel → Ratio dropdown → Customized → 2.35:1. Creates cinematic black bars. |

**Effect application order rationale:** LUT first (sets color base) → Color Match (unifies tool differences on top of LUT) → Film Grain (texture on top of color) → Vignette (spatial focus) → Letterbox (final framing crop).

### Phase 7: Color Unification
After global effects, review the timeline for color consistency:

- **Reference clip selection:** Choose the clip with the best Kodachrome warmth (golden amber, saturated, vintage feel). This is typically a well-lit character close-up.
- **Color Match:** Use CapCut's Color Match tool to align all other clips to the reference.
- **Tool-specific corrections:**
  - Kling clips tend to run slightly cool → boost warmth via HSL (orange/amber +5-10%)
  - Veo clips may have inconsistent saturation → normalize via Curves
  - Seedance clips usually match well with LUT alone
- **Verification:** Scrub through the full timeline. At any cut point, the color temperature should feel continuous, not jarring.

### Phase 8: Selective Effects
Apply these effects to specific clips only — NOT globally:

| Effect | Where to Apply | Setting |
|---|---|---|
| **Light Leak overlay** | Chorus entry transitions (max 3 per episode) | Warm amber tone, 0.5-1s duration, 50-70% opacity |
| **Chromatic Aberration** | Damage/impact moments only | "Shift Channels" effect, subtle RGB split, 1-2s duration |
| **Freeze Frame** | Optional — beat-sync punctuation on high-impact moments | Single frame held for 0.25-0.5s, then resume |

**Chromatic Aberration target shots** (episode-specific — extracted from motion script scenes tagged as damage/glitch/eruption):
- Identify all shots where Robotiko takes physical damage
- Apply subtle Shift Channels effect centered on the impact frame
- Duration: 1-2 seconds, starting just before impact

**FORBIDDEN selective effects:** Neon glow, digital glitch, motion blur presets, speed zoom, VHS full-clip. These are too modern or too heavy for the analog aesthetic.

### Phase 9: Export & QA
1. **Full preview:** Watch the entire timeline at 1× speed with audio. Note any issues.
2. **Run QA checklist** (see Post-Generation Checklist below).
3. **Export settings:**
   - Resolution: **1080p (1920×1080)**
   - Frame rate: **24fps**
   - Codec: **H.265 (HEVC)**
   - Bitrate: **35-60 Mbps** (higher for complex scenes)
   - Format: **MP4**
   - No watermark (CapCut Pro)
4. **Output path:** `episode-{XX}/06_edit/ep{XX}_final_v{VV}.mp4`

---

## OUTPUT FORMAT

The generated guide contains these sections:

### 1. Episode Header
| Field | Value |
|---|---|
| Episode | EP{XX} |
| Title | [from motion script] |
| Total Shots | [number] |
| Total Clips | [number, including sub-clips] |
| Music Duration | [MM:SS] |
| BPM | [from musical metadata] |
| Frame Rate | 24fps |

### 2. Clip Import Checklist
A checkable list of every video file to import:
```
- [ ] ep{XX}_s01_selected.mp4 (Kling 3.0)
- [ ] ep{XX}_s02_selected.mp4 (Kling 3.0)
...
```

### 3. Timeline Map
Shot-by-shot placement with exact values:

| Shot | Timestamp | Clip File | Scene Duration | Clip Duration | Speed | Trim |
|------|-----------|-----------|----------------|---------------|-------|------|
| S01 | 0:00–0:14 | ep{XX}_s01_selected.mp4 | 14s | 10s | 0.71× | — |
| S02 | 0:14–0:28 | ep{XX}_s02_selected.mp4 | 14s | 10s | 0.71× | — |
| ... | ... | ... | ... | ... | ... | ... |

### 4. Speed Ramp Table
Only clips requiring speed adjustment:

| Clip | Native Duration | Playback Speed | Target Duration | Notes |
|------|----------------|----------------|-----------------|-------|
| S01 | 10s | 0.71× | 14s | Speed Ramp — smooth curve |
| ... | ... | ... | ... | ... |

### 5. Beat Sync Checklist
Critical moments requiring frame-level verification:

| # | Timestamp | Musical Event | Visual Action | Clip |
|---|-----------|---------------|---------------|------|
| 1 | 0:00 | Opening riff — first note | Zoom begins | S01 |
| 2 | 1:12 | "He blew a gasket" — downbeat | Eruption | S07 |
| ... | ... | ... | ... | ... |

### 6. Transition Map
Only non-default transitions (hard cuts are implicit):

| Between | Transition | Duration | Notes |
|---------|------------|----------|-------|
| S08 → S09 | Cross Dissolve | 0.5s | Map → Location |
| S12 → S13 | Light Leak | 0.5s | Chorus 1 entry |
| ... | ... | ... | ... |

### 7. Effect Settings
Exact values for the Adjustment Layer:

| Effect | Value | CapCut Path |
|--------|-------|-------------|
| Kodachrome LUT | [filename].cube | Filters → Custom → Import |
| Film Grain | [X]% | Filters → Vintage → Film Grain |
| Vignette | [X]% | Effects → Vignette |
| Letterbox | 2.35:1 | Player → Ratio → Customized |

### 8. Selective Effects Map
Per-clip special effects:

| Clip | Effect | Setting | Timing |
|------|--------|---------|--------|
| S07 | Chromatic Aberration | Subtle RGB split | On eruption frame |
| S13 | Light Leak | Warm amber, 60% | Chorus 1 entry |
| ... | ... | ... | ... |

### 9. Color Reference
- **Reference clip:** [Shot ID] — [reason for selection]
- **Tool-specific adjustments:** [list any per-tool HSL corrections]

### 10. Export Settings
| Setting | Value |
|---------|-------|
| Resolution | 1080p (1920×1080) |
| Frame Rate | 24fps |
| Codec | H.265 (HEVC) |
| Bitrate | 35-60 Mbps |
| Format | MP4 |

### 11. QA Checklist
Pre-export verification (see Post-Generation Checklist).

---

## KODACHROME LUT GUIDE

CapCut Pro supports .cube LUT import. A Kodachrome LUT is essential for the unified 70s analog color palette.

### Recommended Free Sources
- Sources that offered free Kodachrome-style .cube LUTs at time of writing (verify availability): **FilterGrade**, **Lutify.me**, **SmallHD**
- Any Kodachrome 64 emulation in .cube format works

### What to Look For
- **Kodachrome 64** emulation: warm, saturated, golden highlights, rich reds
- Format: `.cube` (industry standard, CapCut compatible)
- Avoid: Kodachrome 200 (too grainy/contrasty for our needs)

### How to Apply in CapCut
1. Go to **Filters** tab in the right panel
2. Click **Custom** → **Import**
3. Select the `.cube` file
4. Adjust intensity with the **Filter Parameter** slider (start at 80-100%)
5. Fine-tune with HSL if needed

### Verification
After applying: the image should have warm amber highlights, slightly saturated reds and oranges, and a vintage film quality. If it looks too cold or too modern, try a different LUT or boost amber/orange in HSL.

---

## CAPCUT PRO FEATURE REFERENCE

### Approved Effects (70s Analog Aesthetic)

| Category | Feature | Usage | Notes |
|----------|---------|-------|-------|
| **Grain** | Film Grain overlay | 10-15% on adjustment layer | Breaks AI smoothness |
| **Color** | .cube LUT import | Kodachrome base palette | See LUT Guide above |
| **Color** | Color Match | Unify clips from different tools | Single reference clip |
| **Color** | HSL / Curves | Fine-tune Kodachrome warmth | Per-tool corrections |
| **Overlay** | Light Leak | Chorus entries, max 3/episode | Warm amber only |
| **Overlay** | Vignette | Subtle edge darkening, all clips | 15-25% |
| **Overlay** | Chromatic Aberration | Damage moments only | "Shift Channels" effect |
| **Aspect** | 2.35:1 Letterbox | Cinematic framing | Custom ratio |
| **Speed** | Speed Ramp/Curve | Motion script speed values | Drag curve points |
| **Speed** | Freeze Frame | Optional beat punctuation | 0.25-0.5s max |
| **Sync** | Auto Beat Detection | Beat markers from audio | Enable on audio track |
| **Keyframe** | Position, Scale, Opacity | Ken Burns if needed | Rarely used |
| **Layers** | Adjustment Layer | Global effects carrier | Spans full timeline |
| **Export** | 1080p H.265 | Final delivery | 35-60 Mbps, 24fps |

### FORBIDDEN Effects (Break Aesthetic)

| Category | Forbidden Items | Why |
|----------|----------------|-----|
| **Transitions** | Glitch, zoom, spin, slide, wipe, swipe, shape | Too modern, too TikTok |
| **Effects** | Neon glow, motion blur presets, digital glitch | Too clean/digital |
| **Filters** | Any "trending" or "popular" preset | Aesthetic contamination |
| **Text** | Motion graphics templates, animated titles | Not album art style |
| **Color** | High-saturation neon grades, teal-orange presets | Too contemporary |

---

## VERSIONING

- First output is always `v01`.
- If the human requests revisions, increment: `v02`, `v03`, etc.
- Each version is a complete document, not a diff.
- Version number in the filename: `ep{XX}_capcut_guide_v{VV}.md`

---

## POST-GENERATION CHECKLIST

Before delivering the CapCut guide to the human, verify:

- [ ] **Clip coverage:** Every shot in the motion script has a corresponding clip in the import checklist
- [ ] **No timeline gaps:** Every second of audio has corresponding video (total timeline = music duration ±1s)
- [ ] **Speed ramps correct:** All speed ramp values match the motion script exactly
- [ ] **Beat sync points:** All critical sync points from motion script are included in the checklist
- [ ] **Transitions:** Only approved transition types used (hard cut, cross dissolve, light leak, fade to black)
- [ ] **Light leak count:** Maximum 3 per episode
- [ ] **Chromatic aberration:** Applied only to damage/impact moments
- [ ] **Effect order:** LUT → Color Match → Film Grain → Vignette → Letterbox
- [ ] **Film grain:** 10-15% specified
- [ ] **Letterbox:** 2.35:1 specified
- [ ] **Color reference:** A specific clip is recommended as the Color Match reference
- [ ] **Export settings:** 1080p, H.265, 35-60 Mbps, 24fps
- [ ] **No forbidden effects:** No modern/trendy/digital effects anywhere in the guide
- [ ] **Sub-clips ordered:** Multi-clip scenes have sub-clips in correct sequence
- [ ] **Veo clips flagged:** Any Veo clips (~8s native) have adjustment notes
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Selected video clips missing | STOP. List which clips are absent. Cannot build timeline with gaps. |
| Musical metadata missing | Generate guide without beat sync checklist. Flag the omission prominently. |
| Motion script not approved | STOP. Cannot generate edit guide from unapproved motion script. |
| Clip count doesn't match motion script | STOP. Reconcile the difference. A new clip may have been added or removed during video selection. |
| Total timeline doesn't equal music duration | Flag the discrepancy. Calculate which clips need speed adjustment to close the gap. |
| No Kodachrome LUT file available | Include LUT Guide section with download links. Proceed with Color Match as primary color tool. |
| CapCut project crashes or corrupts | Recommend saving incremental project versions (after Phase 2, after Phase 6, before export). |

---

*"The edit is where the vision meets the frame. Every cut is a breath, every transition a heartbeat. Make it invisible — the best edit is the one the viewer never notices."*
*— Robotiko v2.0 Pipeline*
