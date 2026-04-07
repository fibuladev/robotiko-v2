# EP01 — CAPCUT EDITING GUIDE
> **Episode:** EP01 — "The Cycle Break / First Contact"
> **Type:** Re-edit + Post-Production Polish (video exists, specific clips being replaced)
> **Version:** v01 | Skill: `_skills/robotiko-capcut-editor/SKILL.md`

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP01 |
| **Title** | The Cycle Break / First Contact |
| **Total Shots** | 77 (after S72-S73 merge into single Mode B) |
| **Music Duration** | 7:22 (442s) |
| **BPM** | 75 |
| **Key** | B Minor |
| **Frame Rate** | 24fps |
| **Export** | 4K (3840×2160) |

---

## PHASE 1: PROJECT SETUP

1. **Open existing EP01 project** in CapCut Pro (or create new if starting fresh)
2. **Project settings:** 4K (3840×2160), 24fps, 16:9
3. **Import audio:** `episode-01/02_music/ep01_audio_v01.mp3` (or .wav)
4. **Run Auto Beat Detection** on the audio track — 75 BPM markers will appear
5. **Create Adjustment Layer** track spanning full 7:22 duration (for global effects)

---

## PHASE 2: RE-SHOT CLIP REPLACEMENT

### 2.1 Clips to Replace

16 new video clips replace their older versions at exact timestamps:

#### Anatolian Grounding (7 clips — Kling 3.0, Mode A, 5s)

| Shot | Timestamp | Old Content | New Content | Camera |
|------|-----------|-------------|-------------|--------|
| **S07** | 0:30–0:35 | Generic desert | Anatolian steppe with mechanical rock formations | Pan Right |
| **S08** | 0:35–0:40 | Generic monolith | Megalithic stone pillars (Göbekli Tepe-inspired) | Slow Zoom In |
| **S09** | 0:40–0:45 | Generic monolith wide | Megaliths + blue digital sphere | Slow Zoom Out |
| **S10** | 0:45–0:50 | Generic golden ruins | Celsus Library (Ephesus) + futuristic airships | Slow Zoom In |
| **S11** | 0:50–0:55 | Generic ruins variant | Library engulfed by dust storm | Pan Left |
| **S20** | 1:35–1:39 | Desert chains | Steppe wreckage sinking into earth | Pan Left |
| **S27** | 2:18–2:22 | Mentor + generic towers | Mentor + Hagia Sophia backdrop | Pan Left |

#### Stone 8 Motif (4 clips — Kling 3.0)

| Shot | Timestamp | Old Content | New Content | Mode | Camera |
|------|-----------|-------------|-------------|------|--------|
| **S50** | 4:11–4:16 | Dark flat "8" | Intact stone 8, Anatolian mountains | A | Static |
| **S51** | 4:16–4:21 | Dark "8" variant | Same 49-50.png, wider reveal | A | Slow Zoom Out |
| **S71** | 6:26–6:30 | Old cracking 8 | New cracking stone 8, same location | A | Static |
| **S72** | 6:30–6:37 | Old S72+S73 (2 clips) | Single Mode B: 61→63.png | **B** | Static |

> **CRITICAL — S72:** The old edit used 2 separate clips (S72 + S73). The new edit uses 1 Mode B clip (7 seconds). Remove both old clips and replace with the single new clip.

#### Aesthetic Fixes (5 clips — Kling 3.0)

| Shot | Timestamp | Old Content | New Content | Mode | Camera |
|------|-----------|-------------|-------------|------|--------|
| **S47** | 3:52–3:59 | Neon infographic cipher | Prog rock cipher diagram | **B** | Static |
| **S59** | 5:02–5:11 | Mountain cliff | Energy portal (warm amber) | A | Slow Zoom In |
| **S60** | 5:12–5:17 | Cyan crystal towers | Same energy portal, different angle | A | Crane Up |
| **S69** | 6:18–6:22 | Rusty handshake | Pristine chrome handshake | A | Static |
| **S70** | 6:22–6:25 | Rusty handshake variant | Same pristine handshake | A | Slow Zoom Out |

### 2.2 Replacement Procedure

For each clip:
1. Locate the old clip's start point on the timeline (by timestamp)
2. Select the old clip → Delete
3. Place the new clip at the exact same start point
4. Trim to scene duration (most clips are 5s or 10s native, scene duration may differ)
5. Verify no gaps or overlaps with neighboring clips

---

## PHASE 3: TRIM & SPEED STRATEGY

### 75 BPM Beat Reference

| Beat | Duration |
|------|----------|
| 1 beat | 0.8s |
| 2 beats | 1.6s |
| 4 beats (1 bar) | 3.2s |
| 8 beats (2 bars) | 6.4s |

### Clips Requiring Speed Adjustment

Most EP01 scenes are 5s clips for 5s scenes (direct trim). Longer scenes:

| Shot | Scene Duration | Clip Native | Strategy | Speed |
|------|---------------|-------------|----------|-------|
| S25 (chorus1a) | 8s | 10s | Trim from end | — |
| S26 (chorus1b) | 7s | 10s | Trim from end | — |
| S57 (mountain) | 6s | 10s | Trim from end | — |
| S58 (mountain reuse) | 9s | 10s | Trim from end | — |
| S59 (energy portal) | 9s | 10s | Trim from end | — |
| S72 (8→∞ Mode B) | 7s | 5-10s | Speed ramp if 5s native | 0.71× |
| S74-S78 (outro) | 9s each | 10s each | Trim from end | — |

> **General rule:** 75 BPM = slow. Most scenes are 5s. Trim 10s clips to scene duration. Speed ramp only when clip duration < scene duration.

---

## PHASE 4: BEAT SYNC VERIFICATION

### Critical Sync Points

At 75 BPM, each beat is 0.8 seconds. Verify these at frame level:

| # | Timestamp | Musical Event | Visual Action | Shot | Re-shot? |
|---|-----------|---------------|---------------|------|----------|
| 1 | **0:00** | Hammond organ — first note | First frame appears | S01 | |
| 2 | **~0:30** | Fuzz guitar entry | S07 steppe panorama begins | S07 | ⚡ |
| 3 | **~0:40** | **Drums enter (Boom-Cha)** | S09 digital sphere + megaliths | S09 | ⚡ |
| 4 | **1:22** | **First vocal entry** | S17 gold coins | S17 | |
| 5 | **1:48** | **Music stops. Solo snare roll.** | S23 chain breaking | S23 | |
| 6 | **2:01** | **Chorus 1 explosion — full band** | S25 hood dissolving | S25 | |
| 7 | **2:35** | **"Two halves" — Cymbal crash** | S31 Apple Start-End begins | S31 | |
| 8 | **2:47** | Moog solo entry — texture shift | S33 tunnel begins | S33 | |
| 9 | **3:04** | Music swells — acceleration | S36 FAST tunnel begins | S36 | |
| 10 | **3:17** | Pre-Ch2 — same lyrics, new visual | S39 Sistine fingers | S39 | |
| 11 | **3:30** | **Wall of Sound — Chorus 2** | S42 blue dome | S42 | |
| 12 | **3:52** | **Cipher chant begins (marching)** | S47 CRT→cipher Mode B | S47 | ⚡ |
| 13 | **4:06** | "Two is lost" — melodic peak | S49 finger touch + clock | S49 | |
| 14 | **4:11** | "Take my hand" | S50 intact stone 8 | S50 | ⚡ |
| 15 | **4:22** | **Bridge — music slows completely** | S52 crane twin wings | S52 | |
| 16 | **~4:35** | "Hello... new realms" — music lifts | S54 crane over city | S54 | |
| 17 | **4:37** | **Reprise explosion — full power** | S55 Mentor+Robot face to face | S55 | |
| 18 | **5:12** | "Two halves" reprise — cymbal | S60 energy portal | S60 | ⚡ |
| 19 | **5:37** | **ULTIMATE CLIMAX begins** | S63a cosmic waves | S63 | |
| 20 | **6:00** | "Zero-one, in thrall!" — chant | S66 ulti.png binary face | S66 | |
| 21 | **6:15** | "Two is lost" ultimate | S68 handshake begins | S68 | |
| 22 | **6:26** | **"The eight turns sideways..." whisper** | S71 stone 8 cracking | S71 | ⚡ |
| 23 | **6:30** | Whisper fading | S72 Mode B 8→∞ transformation | S72 | ⚡ |
| 24 | **6:37** | Moog + guitar solo begins | S74 infinity ride | S74 | |
| 25 | **~7:18** | **Final heavy chord** | S78 cosmic fade to black | S78 | |

> ⚡ = Re-shot clip. Pay extra attention to beat sync at these points.

---

## PHASE 5: TRANSITION STRATEGY

### Transition Map

EP01 uses mostly **hard cuts.** Exceptions:

| Between | Transition | Duration | Reason |
|---------|------------|----------|--------|
| S06 → S07 | **Cross Dissolve** | 1.0s | Cave → Steppe (location shift) |
| S11 → S12 | **Cross Dissolve** | 0.8s | Ruins → Mentor boots (location → character) |
| S24 → S25 | **Light Leak** | 0.5s | Pre-chorus → **Chorus 1 explosion.** Warm amber. |
| S38 → S39 | **Cross Dissolve** | 0.5s | Data ignite → First Contact fingers (transition moment) |
| S41 → S42 | **Light Leak** | 0.5s | Pre-chorus → **Chorus 2 explosion.** Warm amber. |
| S51 → S52 | **Cross Dissolve** | 1.0s | Stone 8 → Crane bridge (energy drops, soft transition) |
| S54 → S55 | **Light Leak** | 0.5s | Bridge end → **Reprise explosion.** Warm amber. |
| S61 → S62a | **Cross Dissolve** | 0.5s | Vortex → Cosmic spiral (cosmic transition) |
| S78 | **Fade to Black** | 3.0s | Final frame — slow fade to silence |

**Light Leak count: 3** (Chorus 1, Chorus 2, Reprise entries) ✓ Within limit.

**FORBIDDEN:** Glitch, zoom, spin, slide, wipe, swipe, shape presets. These break the analog aesthetic.

---

## PHASE 6: GLOBAL EFFECTS (Adjustment Layer)

Apply to the Adjustment Layer in THIS ORDER (sequence matters):

| # | Effect | Setting | CapCut Path | Notes |
|---|--------|---------|-------------|-------|
| 1 | **Kodachrome LUT** | .cube file, 80-100% intensity | Filters → Custom → Import | Sets warm amber base. See LUT sources below. |
| 2 | **Color Match** | Reference: **S14 (amber staff close-up)** | Adjust → Color Match | Best Kodachrome warmth. Match all clips to this. |
| 3 | **Film Grain** | 12% intensity | Filters → Vintage → Film Grain | Breaks AI smoothness. Range: 10-15%. |
| 4 | **Vignette** | 20% | Effects → Vignette | Darkens edges, pulls focus to center. Range: 15-25%. |
| 5 | **Watermark Crop Zoom** | Scale 105-110% on ALL clips | Select all clips → Basic → Scale | Must be applied BEFORE letterbox. Pushes corner watermarks out of frame. |
| 6 | **Letterbox 2.35:1** | Custom aspect ratio | Player → Ratio → Customized → 2.35:1 | Cinematic black bars on top of zoomed footage. |

### Watermark Crop Strategy (EP01-EP04)

Most EP01-EP04 video clips have tool watermarks in the bottom-right corner. The zoom-then-letterbox approach:

1. **Select ALL clips on the timeline** (Ctrl+A on video track)
2. **Basic → Scale → 108%** (start here — adjust if watermark still visible)
3. Check all four corners — watermark should now be outside the visible frame
4. If still visible at 108%, increase to 110%. Do not exceed 112% (too much composition loss).
5. **Then apply 2.35:1 letterbox** — the black bars frame the already-zoomed footage

**What you lose:** ~5-8% of edge composition. On wide landscape shots this is negligible. On tight close-ups, verify important details are not cropped.

**EP05+ clips (watermark-free):** Apply letterbox only, no zoom needed. Keep Scale at 100% for these clips.

**Fallback:** If zoom+letterbox does not work satisfactorily, remove both and use 16:9 clean at 100% scale. Update this guide accordingly.

### Kodachrome LUT Sources (Free)
- **FilterGrade** — Free Kodachrome Film Emulation pack (.cube)
- **Lutify.me** — Free Kodachrome 64 emulation
- **SmallHD** — Free Cinema LUT pack

### Reference Clip Selection
**S14 (amber staff close-up)** recommended because:
- Warm amber light dominant
- Natural textures (wood, leather)
- Film grain feels organic
- The "gold standard" for Kodachrome warmth in EP01

**Alternatives:** S17 (gold coins) or S30 (bone.png) — both strong Kodachrome examples.

---

## PHASE 7: COLOR UNIFICATION

### Tool-Specific Corrections

| Tool | Tendency | Fix |
|------|----------|-----|
| **Kling 3.0** | Slight cool shift | HSL: Orange/Amber +5-10% |
| **Veo** | Inconsistent saturation | Normalize via Curves |
| **Mode B (Kling)** | Generally good | LUT usually sufficient |

### Verification Points
Scrub through the full timeline. At every cut point, color temperature must feel CONTINUOUS. Check especially:
- S06→S07: Cave → Steppe (interior → exterior color transition)
- S35→S36: Data tunnel slow → fast (must be identical color)
- S51→S52: Stone 8 → Crane (dusk/evening transition)
- S70→S71: Handshake → Stone 8 cracking (different location, same warmth)

---

## PHASE 8: SELECTIVE EFFECTS

### EP01-Specific Rules

EP01 has NO physical damage (Phase 1 = PRISTINE). Therefore: **NO Chromatic Aberration.** That effect is reserved for EP02+ damage moments.

| Clip | Effect | Setting | Timing |
|------|--------|---------|--------|
| S23 | **Brightness spike** | +50% brightness, 3 frames | Chain breaking impact |
| S24 | **Brightness spike** | +30% brightness, 5 frames | Light burst peak |
| S31-S32 | **Subtle glow** | Warm amber overlay, 30% opacity | During Apple transformation |
| S71 | **Brightness spike** | +40% brightness, 4 frames | Stone 8 crack moment |
| S72 | **Bloom/Glow** | White glow overlay, 20-30% opacity | When ∞ symbol first appears |

### Light Leak Details

| Shot | Position | Color | Opacity | Duration |
|------|----------|-------|---------|----------|
| S24→S25 | Chorus 1 entry | Warm amber | 60% | 0.5s |
| S41→S42 | Chorus 2 entry | Warm amber | 50% | 0.5s |
| S54→S55 | Reprise entry | Warm amber | 70% | 0.5s |

> Light Leaks MUST be warm amber only. Blue, green, pink FORBIDDEN.

---

## PHASE 9: ENERGY & PACING CHECK

### EP01 Energy Map

During final scrub, verify this energy curve:

```
0:00-1:21  ░░░▓   INTRO: Slow, breathing, world-building. 16 images flow gently.
                   Pace: No rush. Each frame breathes for 5 seconds.

1:22-2:00  ▓▓▓    VERSES: Storytelling. Steady cuts.
                   Pace: Regular, narrative rhythm.

2:01-2:46  █████  CHORUS 1: Explosion. Denser cuts, more dynamic.
                   Pace: Cuts match musical energy. Apple transformation = peak.

2:47-3:16  ▓▓▓    VERSE 2: Tunnel journey. Steady → accelerating.
                   Pace: S33-35 slow → S36 FAST. Contrast must be felt.

3:17-4:21  ██████ CHORUS 2: Wall of Sound. Cipher chant. Stone 8 monolith.
                   Pace: Dense, powerful, marching rhythm. Each chant line = one cut.

4:22-4:36  ░░     BRIDGE: BREATH! Crane wings. Minimal.
                   Pace: SLOW DOWN. This is the only rest. Viewer must exhale.

4:37-5:22  █████  REPRISE: Characters together, ascending.
                   Pace: Powerful again but different from first chorus — more intimate.

5:23-5:36  ▓▓▓    INTERLUDE 2: Cosmic transition.
                   Pace: Transition energy. Not too fast, not too slow.

5:37-6:25  ███████ ULTIMATE: PEAK. Cosmic waves, face transformation, handshake.
                   Pace: Maximum. Densest cuts here.

6:26-7:22  ▓▓░    OUTRO: Transformation → cosmic journey → fade.
                   Pace: Gradual deceleration. Each cut in the last 45s gets slower.
                   Final frame: Fade to black, 3 seconds. Silence.
```

### Verification Questions
- Does the Bridge (4:22-4:36) genuinely feel like a BREATH? Or does it pass too quickly?
- Does the Ultimate (5:37-6:25) genuinely feel like the PEAK? Or is it indistinguishable from the Reprise?
- Does the Outro (6:37-7:22) genuinely FADE? Or does it end abruptly?
- Does the 81-second intro hold attention? Is a new image every ~5 seconds enough?

---

## PHASE 10: EXPORT & QA

### Export Settings

| Setting | Value |
|---------|-------|
| **Resolution** | 4K (3840×2160) |
| **Frame Rate** | 24fps |
| **Codec** | H.265 (HEVC) |
| **Bitrate** | 35-60 Mbps |
| **Format** | MP4 |
| **Watermark** | None (CapCut Pro) |

**Output:** `episode-01/06_edit/ep01_final_v01.mp4`

### QA Checklist

- [ ] **16 re-shot clips** placed at correct timestamps
- [ ] S72: old 2 clips replaced by single Mode B clip
- [ ] Total timeline duration = 442s (±1s)
- [ ] No gaps anywhere on the timeline
- [ ] All 25 beat sync points verified (especially ⚡ re-shot clips)
- [ ] 3 Light Leaks at correct chorus entries (S24→25, S41→42, S54→55)
- [ ] Cross Dissolves only at location transitions
- [ ] Fade to Black only on final frame (S78, 3s)
- [ ] Kodachrome LUT applied
- [ ] Color Match reference: S14 (amber staff)
- [ ] Film Grain: 10-15%
- [ ] Vignette: 15-25%
- [ ] Letterbox: 2.35:1
- [ ] NO Chromatic Aberration (EP01 = Phase 1, no damage)
- [ ] NO forbidden effects or transitions
- [ ] Energy curve feels correct (intro breathes, bridge breathes, outro fades)
- [ ] **Full preview watched** — 7:22 uninterrupted, 1× speed

### The Final Question
> **"Would a stranger watching this for the first time say: I want to see what comes next?"**

If yes: Export. 🎬

---

*"The edit is where the vision meets the frame. Every cut is a breath, every transition a heartbeat. Make it invisible — the best edit is the one the viewer never notices."*
