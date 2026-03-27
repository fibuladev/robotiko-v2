# CAPCUT EDITING GUIDE — EP02: THE TECH GURU'S DOWNFALL
> **Version:** v01 | **Skill:** robotiko-capcut-editor
> **Generated:** 2026-03-10
> **Based on:** ep02_motion_script_v02.md (approved)

---

## 1. EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP02 |
| **Title** | The Tech Guru's Downfall |
| **Total Shots** | 35 |
| **Total Clips** | 46 (physical files — adjusted from 49: S14c cancelled, S34b+c combined as Multi-Shot) |
| **Music Duration** | 7:28 (448s) |
| **BPM** | 104 (constant until War Zone tempo slow at 5:48) |
| **Frame Rate** | 24fps |
| **Resolution** | 4K (3840×2160) |

### Production Changes from Motion Script v02

| Change | Original | Actual | Impact |
|--------|----------|--------|--------|
| **S14c cancelled** | 3 × 5s clips | S14a (8s) + S14b (7s) | 15s total, covers 14s scene — trim 1s |
| **S34b+c → Multi-Shot** | S34b (10s) + S34c (10s) | S34bc (15s single clip) | Smoother transition, 15s continuous |
| **S07 (Start/End)** | S07a + S07b keyframes | Single 10s clip | No sub-clip split needed |
| **S20** | S20a (10s) + S20b (10s) | ⚠️ Single file (ep02_s20_selected.mp4) | See note below |

> ⚠️ **S20 FLAG:** Motion script requires 20s (2 × 10s sub-clips with different camera moves). Only one file exists. Verify clip duration before placing on timeline. If 10s: need speed ramp 0.5× (too slow) or second clip generation. If 20s: trim to 20s and place as continuous.

---

## 2. CLIP IMPORT CHECKLIST

Import all files from `episode-02/05_video/selected/`:

### Single Clips (27 files)
- [ ] ep02_s01_selected.mp4 (Kling 3.0)
- [ ] ep02_s02_selected.mp4 (Kling 3.0)
- [ ] ep02_s03_selected.mp4 (Kling 3.0)
- [ ] ep02_s04_selected.mp4 (Kling 3.0)
- [ ] ep02_s05_selected.mp4 (Kling 3.0)
- [ ] ep02_s06_selected.mp4 (Veo)
- [ ] ep02_s07_selected.mp4 (Kling 2.5 Turbo — Mode B Start/End)
- [ ] ep02_s08_selected.mp4 (Seedance 1.0)
- [ ] ep02_s09_selected.mp4 (Kling 3.0)
- [ ] ep02_s10_selected.mp4 (Kling 3.0)
- [ ] ep02_s11_selected.mp4 (Kling 3.0 — Mode B Start/End)
- [ ] ep02_s12_selected.mp4 (Kling 3.0)
- [ ] ep02_s13_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s15_selected.mp4 (Kling 3.0)
- [ ] ep02_s16_selected.mp4 (Seedance 1.0)
- [ ] ep02_s17_selected.mp4 (Veo)
- [ ] ep02_s18_selected.mp4 (Veo)
- [ ] ep02_s19_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s20_selected.mp4 (Kling 3.0) ⚠️ Check duration
- [ ] ep02_s21_selected.mp4 (Seedance 1.0)
- [ ] ep02_s22_selected.mp4 (Kling 3.0)
- [ ] ep02_s23_selected.mp4 (Kling 2.5 Turbo — Mode B Start/End)
- [ ] ep02_s26_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s27_selected.mp4 (Veo)
- [ ] ep02_s28_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s31_selected.mp4 (Kling 3.0)
- [ ] ep02_s32_selected.mp4 (Kling 3.0)

### Sub-Clips (17 files)
- [ ] ep02_s14a_selected.mp4 (Kling 3.0)
- [ ] ep02_s14b_selected.mp4 (Kling 3.0)
- [ ] ep02_s24a_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s24b_selected.mp4 (Kling 3.0)
- [ ] ep02_s24c_selected.mp4 (Kling 3.0)
- [ ] ep02_s25a_selected.mp4 (Seedance 1.0)
- [ ] ep02_s25b_selected.mp4 (Seedance 1.0)
- [ ] ep02_s29a_selected.mp4 (Seedance 1.0)
- [ ] ep02_s29b_selected.mp4 (Seedance 1.0)
- [ ] ep02_s29c_selected.mp4 (Seedance 1.0)
- [ ] ep02_s29d_selected.mp4 (Seedance 1.0)
- [ ] ep02_s30a_selected.mp4 (Kling 3.0)
- [ ] ep02_s30b_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s33a_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s33b_selected.mp4 (Kling 3.0)
- [ ] ep02_s35a_selected.mp4 (Kling 2.5 Turbo)
- [ ] ep02_s35b_selected.mp4 (Kling 2.5 Turbo)

### Multi-Shot / Combined (2 files)
- [ ] ep02_s34a_selected.mp4 (Kling 3.0)
- [ ] ep02_s34bc_selected.mp4 (Kling 3.0 Multi-Shot — 15s)

**Total: 46 files**

---

## 3. TIMELINE MAP

Place clips on the video track in this exact order. Match each clip's start position to its timestamp.

| # | Shot | Timestamp | Clip File | Scene Dur | Clip Dur | Speed | Action |
|---|------|-----------|-----------|-----------|----------|-------|--------|
| 1 | S01 | 0:00–0:14 | ep02_s01_selected.mp4 | 14s | 10s | 0.71× | Speed Ramp |
| 2 | S02 | 0:14–0:28 | ep02_s02_selected.mp4 | 14s | 10s | 0.71× | Speed Ramp |
| 3 | S03 | 0:28–0:42 | ep02_s03_selected.mp4 | 14s | 10s | 0.71× | Speed Ramp |
| 4 | S04 | 0:43–0:52 | ep02_s04_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 5 | S05 | 0:52–1:01 | ep02_s05_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 6 | S06 | 1:02–1:10 | ep02_s06_selected.mp4 | 8s | 10s | 1× | Trim 2s from end |
| 7 | S07 | 1:10–1:19 | ep02_s07_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 8 | S08 | 1:19–1:20 | ep02_s08_selected.mp4 | 1s | 5s | 1× | Trim 4s — 1s beat flash |
| 9 | S09 | 1:20–1:25 | ep02_s09_selected.mp4 | 5s | 5s | 1× | Perfect match |
| 10 | S10 | 1:25–1:30 | ep02_s10_selected.mp4 | 5s | 5s | 1× | Perfect match |
| 11 | S11 | 1:30–1:34 | ep02_s11_selected.mp4 | 4s | 5s | 1× | Trim 1s from end |
| 12 | S12 | 1:34–1:39 | ep02_s12_selected.mp4 | 5s | 5s | 1× | Perfect match |
| 13 | S13 | 1:39–1:52 | ep02_s13_selected.mp4 | 13s | 10s | 0.77× | Speed Ramp |
| 14 | S14a | 1:52–2:00 | ep02_s14a_selected.mp4 | 8s | 8s | 1× | Perfect match |
| 15 | S14b | 2:00–2:06 | ep02_s14b_selected.mp4 | 6s | 7s | 1× | Trim 1s from end |
| 16 | S15 | 2:06–2:20 | ep02_s15_selected.mp4 | 14s | 10s | 0.71× | Speed Ramp |
| 17 | S16 | 2:20–2:34 | ep02_s16_selected.mp4 | 14s | 10s | 0.71× | Speed Ramp |
| 18 | S17 | 2:34–2:42 | ep02_s17_selected.mp4 | 8s | 10s | 1× | Trim 2s from end |
| 19 | S18 | 2:42–2:51 | ep02_s18_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 20 | S19 | 2:52–3:04 | ep02_s19_selected.mp4 | 12s | 10s | 0.83× | Speed Ramp |
| 21 | S20 | 3:04–3:24 | ep02_s20_selected.mp4 | 20s | ⚠️ | — | ⚠️ Verify clip duration — see S20 Flag |
| 22 | S21 | 3:24–3:38 | ep02_s21_selected.mp4 | 14s | 10s | 0.71× | Speed Ramp |
| 23 | S22 | 3:38–3:48 | ep02_s22_selected.mp4 | 10s | 10s | 1× | Perfect match |
| 24 | S23 | 3:48–3:57 | ep02_s23_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 25 | S24a | 3:57–4:07 | ep02_s24a_selected.mp4 | 10s | 10s | 1× | — |
| 26 | S24b | 4:07–4:16 | ep02_s24b_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 27 | S24c | 4:16–4:25 | ep02_s24c_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 28 | S25a | 4:25–4:34 | ep02_s25a_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 29 | S25b | 4:34–4:42 | ep02_s25b_selected.mp4 | 8s | 10s | 1× | Trim 2s from end |
| 30 | S26 | 4:42–4:52 | ep02_s26_selected.mp4 | 10s | 10s | 1× | Perfect match |
| 31 | S27 | 4:52–5:01 | ep02_s27_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 32 | S28 | 5:02–5:12 | ep02_s28_selected.mp4 | 10s | 10s | 1× | Perfect match |
| 33 | S29a | 5:12–5:21 | ep02_s29a_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 34 | S29b | 5:21–5:30 | ep02_s29b_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 35 | S29c | 5:30–5:39 | ep02_s29c_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 36 | S29d | 5:39–5:48 | ep02_s29d_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 37 | S30a | 5:48–5:58 | ep02_s30a_selected.mp4 | 10s | 10s | 1× | — |
| 38 | S30b | 5:58–6:07 | ep02_s30b_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 39 | S31 | 6:07–6:17 | ep02_s31_selected.mp4 | 10s | 10s | 1× | Perfect match |
| 40 | S32 | 6:17–6:25 | ep02_s32_selected.mp4 | 8s | 10s | 1× | Use 8s. Hold extra 2s for emphasis if desired |
| 41 | S33a | 6:26–6:35 | ep02_s33a_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 42 | S33b | 6:35–6:44 | ep02_s33b_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 43 | S34a | 6:44–6:53 | ep02_s34a_selected.mp4 | 9s | 10s | 1× | Trim 1s from end |
| 44 | S34bc | 6:53–7:08 | ep02_s34bc_selected.mp4 | 15s | 15s | 1× | Perfect match (Multi-Shot) |
| 45 | S35a | 7:08–7:18 | ep02_s35a_selected.mp4 | 10s | 10s | 1× | — |
| 46 | S35b | 7:18–7:28 | ep02_s35b_selected.mp4 | 10s | 10s | 1× | — + Fade to Black |

**Timeline verification:** Total scene durations = 448s = Music duration ✓

---

## 4. SPEED RAMP TABLE

Only clips requiring speed adjustment. Apply via CapCut Speed → Curve.

| # | Clip | Native Dur | Playback Speed | Target Dur | Notes |
|---|------|-----------|----------------|------------|-------|
| 1 | S01 | 10s | 0.71× | 14s | Intro — dreamy slow zoom. Smooth curve. |
| 2 | S02 | 10s | 0.71× | 14s | Hammond swell — cathedral grandeur. Smooth curve. |
| 3 | S03 | 10s | 0.71× | 14s | Intro climax — chrome close-up. Smooth curve. |
| 4 | S13 | 10s | 0.77× | 13s | Chorus 1 — split screen energy. Smooth curve. |
| 5 | S15 | 10s | 0.71× | 14s | Guitar solo — salt flat contemplation. Smooth curve. |
| 6 | S16 | 10s | 0.71× | 14s | Hammond transition — map push. Smooth curve. |
| 7 | S19 | 10s | 0.83× | 12s | Verse 6 — aftermath stillness. Smooth curve. |
| 8 | S21 | 10s | 0.71× | 14s | Solo fade — map deterioration. Smooth curve. |

**How to apply in CapCut:**
1. Select the clip on timeline
2. Go to **Speed** panel → **Curve**
3. Choose **Custom** → drag the curve line down to the target speed
4. For uniform slowdown: keep the curve flat at the target speed
5. Verify the clip's new duration matches the Target Duration

---

## 5. BEAT SYNC CHECKLIST

BPM: 104 (one beat = 0.577s). Enable **Auto Beat Detection** on the audio track first.

Critical sync points — verify each one at frame level:

| # | Timestamp | Musical Event | Visual Action | Clip | Priority |
|---|-----------|---------------|---------------|------|----------|
| 1 | 0:00 | Opening guitar riff — first note | S01: Zoom begins, first route pulse | S01 | HIGH |
| 2 | 0:14 | Hammond organ sustain | Cut to podium — Robotiko revealed | S02 | HIGH |
| 3 | 0:43 | Verse 1 — guitar riff | S04: Pan begins — steps sync to BPM | S04 | MEDIUM |
| 4 | ~1:12 | "He blew a gasket in the hall" | S07: Eruption on exact downbeat | S07 | **CRITICAL** |
| 5 | 1:19 | Hammond swirl accent | S08: Map flash — 1s hold | S08 | HIGH |
| 6 | ~1:31 | "Junkie grabbed his metal leg" — bass drop | S11: Leg grab syncs to bass | S11 | HIGH |
| 7 | 1:34 | Energy dip — breath | S12: Cut to egg vendor warmth | S12 | MEDIUM |
| 8 | 1:39 | Chorus 1 — choir entry | S13: Split-screen locks + Light Leak | S13 | **CRITICAL** |
| 9 | 1:52 | Post-chorus fuzz riff | S14a: Montage begins | S14a | HIGH |
| 10 | 2:06 | Instrumental solo begins | S15: Cut to salt flat — visual exhale | S15 | MEDIUM |
| 11 | ~2:52 | "Boss scraps off his shoulder steel!" | S19: Scraping rhythm syncs to drums | S19 | MEDIUM |
| 12 | ~3:50 | "A Heavy Press gave a sudden skip" | S23: Press slam on drum fill | S23 | **CRITICAL** |
| 13 | 3:57 | Chorus 2 — choir re-entry | S24a: Escalated split-screen + Light Leak | S24a | **CRITICAL** |
| 14 | 4:42 | Bridge — "Hallucination Mode" | S26: Paris split engages | S26 | HIGH |
| 15 | ~5:02 | "Smashed the sensors" — drums | S28: First mob impact on drum accent | S28 | HIGH |
| 16 | 5:48 | Tempo slows — sparse guitar | S30a: Cut to war zone — stillness | S30a | HIGH |
| 17 | ~6:20 | "Shrapnel took away his ear" | S32: Impact on "took away" — then silence | S32 | **CRITICAL** |
| 18 | 6:26 | Chorus 3 DETONATION | S33a: Hard cut to hero shot + Light Leak | S33a | **CRITICAL** |
| 19 | 6:44 | Instruments dropping out | S34a: Pullback begins | S34a | HIGH |
| 20 | ~7:25 | Final harmonic decays to silence | S35b: Red eye last light → black | S35b | HIGH |

**Verification method:** Play each sync point at 0.25× speed. The visual action must land within ±2 frames of the beat marker.

---

## 6. TRANSITION MAP

Default transition is **hard cut** (not listed). Only non-default transitions below:

| # | Between | Transition | Duration | Reason |
|---|---------|------------|----------|--------|
| 1 | S08 → S09 | **Cross Dissolve** | 0.5s | Map → Location (Davos → San Francisco) |
| 2 | S12 → S13 | **Light Leak** | 0.5s | Chorus 1 entry — warm amber |
| 3 | S16 → S17 | **Cross Dissolve** | 0.5s | Map → Location (Map → Congo) |
| 4 | S21 → S22 | **Cross Dissolve** | 0.5s | Map → Location (Map → Bangladesh) |
| 5 | S23 → S24a | **Light Leak** | 0.5s | Chorus 2 entry — warm amber |
| 6 | S25b → S26 | **Cross Dissolve** | 0.5s | Map → Location (Map → Paris) |
| 7 | S32 → S33a | **Light Leak** | 0.5s | Chorus 3 DETONATION — warm amber |
| 8 | S35b end | **Fade to Black** | 3s | Final shot — episode end |

**Light Leak count: 3** (maximum allowed per episode) ✓

**IMPORTANT — Multi-clip scenes use hard cuts between sub-clips:**
- S14a → S14b: Hard cut
- S24a → S24b → S24c: Hard cuts
- S25a → S25b: Hard cut
- S29a → S29b → S29c → S29d: Hard cuts
- S30a → S30b: Hard cut
- S33a → S33b: Hard cut
- S34a → S34bc: Hard cut
- S35a → S35b: Hard cut

**FORBIDDEN:** Glitch, zoom, spin, slide, wipe, swipe, shape, or any "trendy" preset.

---

## 7. EFFECT SETTINGS — GLOBAL (Adjustment Layer)

Create one Adjustment Layer spanning the full timeline. Apply effects in this exact order:

| # | Effect | Value | CapCut Path | Notes |
|---|--------|-------|-------------|-------|
| 1 | **Kodachrome LUT** | 80-100% intensity | Filters → Custom → Import (.cube file) | Sets warm amber base palette. See LUT Guide below. |
| 2 | **Color Match** | Reference: S12 | Adjust → Color Match → Select reference | Unifies clips from Kling, Veo, Seedance |
| 3 | **Film Grain** | 12% | Filters → Vintage → Film Grain | Breaks AI smoothness. Adjust with Filter Parameter slider. |
| 4 | **Vignette** | 20% | Effects → Vignette | Subtle edge darkening. Pulls focus to center. |
| 5 | **Letterbox 2.35:1** | Custom ratio | Player panel → Ratio → Customized → 2.35:1 | Cinematic black bars. Hides edge artifacts. |

**Effect order rationale:** LUT (color base) → Color Match (unify tool differences) → Film Grain (texture) → Vignette (spatial focus) → Letterbox (final crop).

### Kodachrome LUT Guide

CapCut Pro supports .cube LUT import. Look for **Kodachrome 64** emulation:
- **FilterGrade** — Free Kodachrome Film Emulation pack (.cube)
- **Lutify.me** — Free Kodachrome 64 emulation
- **SmallHD** — Free Cinema LUT pack (warm film stocks)

**How to apply:**
1. Filters tab → Custom → Import → select .cube file
2. Adjust intensity with Filter Parameter slider (start at 80-100%)
3. Fine-tune warmth with HSL if needed

**Verification:** Image should have warm amber highlights, saturated reds/oranges, vintage film quality. If too cold or too modern → try different LUT or boost amber/orange in HSL.

---

## 8. SELECTIVE EFFECTS MAP

Per-clip special effects — NOT on the adjustment layer.

### Chromatic Aberration (Damage/Impact Moments)

Apply CapCut's **"Shift Channels"** effect — subtle RGB split, 1-2s duration.

| # | Clip | Timing | Damage Event | Intensity |
|---|------|--------|-------------|-----------|
| 1 | S07 | On eruption frame (~1:12) | Gasket blows — steam + sparks | Subtle — comedic, not destructive |
| 2 | S11 | On leg grab (~1:31) | Leg theft — sparks from joint | Medium — sudden violence |
| 3 | S23 | On press impact (~3:50) | Press slam — torso dent | Medium — industrial impact |
| 4 | S28 | On mob attack (~5:02) | Sensor smash — back cracked | Medium-high — mob rage |
| 5 | S32 | On ear reveal (~6:20) | Shrapnel — ear gone | **Maximum** — EP02 turning point |

**How to apply:**
1. Select the specific clip
2. Effects → search "Shift Channels" or "RGB Split"
3. Set duration: Start 0.5s before impact frame, end 1s after
4. Keep subtle — this is analog aberration, not digital glitch
5. S32 can be slightly stronger than others (climactic moment)

### Light Leak Overlays (Chorus Entries)

| # | Position | Timing | Opacity | Color |
|---|----------|--------|---------|-------|
| 1 | S12 → S13 | 1:39 (Chorus 1 entry) | 60% | Warm amber |
| 2 | S23 → S24a | 3:57 (Chorus 2 entry) | 60% | Warm amber |
| 3 | S32 → S33a | 6:26 (Chorus 3 entry) | 70% | Warm amber |

**How to apply:**
1. Effects → search "Light Leak"
2. Place on overlay track at the transition point
3. Duration: 0.5-1s
4. Adjust opacity (60-70%)
5. **Warm amber tone ONLY** — no cool or neon light leaks

**FORBIDDEN:** Neon glow, digital glitch, motion blur presets, speed zoom, VHS full-clip.

---

## 9. COLOR REFERENCE & TOOL-SPECIFIC CORRECTIONS

### Reference Clip
- **S12 (Egg Vendor)** — Warm golden light from egg cart heat lamp. Best Kodachrome warmth candidate. Intimate, saturated amber tones.
- Apply Color Match using S12 as the reference for all other clips.

### Tool-Specific Adjustments (After Global LUT + Color Match)

| Tool | Clips | Known Tendency | Correction |
|------|-------|----------------|------------|
| **Kling 3.0** | S01-S05, S09-S12, S15, S22, S24b/c, S30a, S31-S32, S33b, S34a/bc | Slightly cool | HSL: Orange/Amber +5-10%. Boost warmth. |
| **Kling 2.5 Turbo** | S07, S13, S19, S23, S24a, S26, S28, S30b, S33a, S35a/b | Slightly cool | Same as 3.0: HSL Orange/Amber +5-10% |
| **Veo** | S06, S17, S18, S27 | Inconsistent saturation | Normalize via Curves. Check mid-tone warmth. |
| **Seedance 1.0** | S08, S16, S21, S25a/b, S29a-d | Usually matches LUT well | Minimal correction needed. Verify grain consistency. |

### Color Verification
Scrub through the full timeline after corrections. At every cut point:
- Color temperature should feel continuous (no jarring warm-to-cool shifts)
- Pay extra attention to transitions between different tools (e.g., S12 Kling → S13 Kling 2.5T, S21 Seedance → S22 Kling)

---

## 10. EXPORT SETTINGS

| Setting | Value |
|---------|-------|
| **Resolution** | 4K (3840×2160) |
| **Frame Rate** | 24fps |
| **Codec** | H.265 (HEVC) |
| **Bitrate** | 50 Mbps (high — complex scenes with grain) |
| **Format** | MP4 |
| **Watermark** | None (CapCut Pro) |
| **Output Path** | `episode-02/06_edit/ep02_final_v01.mp4` |

---

## 11. QA CHECKLIST

### Pre-Export Verification

**Timeline Integrity:**
- [ ] All 46 clips placed in correct order (S01 → S35b)
- [ ] No timeline gaps — every second of audio has video
- [ ] Total timeline = 448s (±1s)
- [ ] S20 situation resolved (duration verified)

**Speed Ramps:**
- [ ] S01: 0.71× → 14s ✓
- [ ] S02: 0.71× → 14s ✓
- [ ] S03: 0.71× → 14s ✓
- [ ] S13: 0.77× → 13s ✓
- [ ] S15: 0.71× → 14s ✓
- [ ] S16: 0.71× → 14s ✓
- [ ] S19: 0.83× → 12s ✓
- [ ] S21: 0.71× → 14s ✓

**Beat Sync (Critical Points Only):**
- [ ] ~1:12 — S07 gasket eruption on downbeat
- [ ] 1:39 — S13 Chorus 1 choir entry
- [ ] ~3:50 — S23 press slam on drum fill
- [ ] 3:57 — S24a Chorus 2 choir re-entry
- [ ] ~6:20 — S32 ear reveal on "took away"
- [ ] 6:26 — S33a Chorus 3 detonation

**Transitions:**
- [ ] Only approved types used (hard cut, cross dissolve, light leak, fade to black)
- [ ] Light leak count = 3 (S12→S13, S23→S24a, S32→S33a)
- [ ] Cross dissolve only on map→location transitions (4 instances)
- [ ] Fade to black on S35b only
- [ ] No forbidden transitions anywhere

**Global Effects (Adjustment Layer):**
- [ ] Kodachrome LUT applied (80-100%)
- [ ] Color Match applied (reference: S12)
- [ ] Film Grain at 10-15%
- [ ] Vignette at 15-25%
- [ ] Letterbox 2.35:1

**Selective Effects:**
- [ ] Chromatic Aberration on S07, S11, S23, S28, S32 only
- [ ] Light Leaks on chorus entries only (warm amber)
- [ ] No forbidden effects anywhere

**Color:**
- [ ] Color continuous across all cut points
- [ ] Tool-specific HSL corrections applied (Kling warmth boost, Veo curves)
- [ ] Kodachrome warmth preserved throughout
- [ ] No clean/sterile aesthetics — analog decay present

**Final:**
- [ ] Full preview at 1× speed with audio — no issues
- [ ] 4K H.265 export confirmed
- [ ] No watermark

---

## 9-PHASE ASSEMBLY WALKTHROUGH

### Phase 1: Project Setup
1. Create new CapCut project: **4K (3840×2160), 24fps, 16:9**
2. Import `ep02_audio_v01.wav` (or .mp3) to the main audio timeline
3. Import all 46 video clips from `05_video/selected/`
4. Run **Auto Beat Detection** on the audio track → beat markers appear
5. Create a dedicated **Adjustment Layer** track (for global effects in Phase 6)
6. **Save project** as `EP02_v01`

### Phase 2: Timeline Assembly
1. Place clips on video track in order: S01 → S35b (follow Timeline Map table above)
2. Match each clip's start to its timestamp
3. Multi-clip scenes: place sub-clips sequentially (S14a → S14b, S24a → S24b → S24c, etc.)
4. Leave no gaps
5. Rough-cut each clip to approximate scene duration
6. **Save project** as `EP02_v02_rough`

### Phase 3: Trim & Speed Ramp
1. Apply speed ramps to 8 clips (see Speed Ramp Table)
2. Trim direct clips to exact scene durations (cut from end unless noted)
3. Resolve S20 duration situation
4. Verify: total timeline = 448s (±1s)
5. **Save project** as `EP02_v03_trimmed`

### Phase 4: Beat Sync Verification
1. Enable beat marker visibility
2. Walk through all 20 sync points (see Beat Sync Checklist)
3. Adjust clip boundaries by frames where needed
4. Pay special attention to 6 CRITICAL sync points
5. **Save project** as `EP02_v04_synced`

### Phase 5: Transitions
1. Apply 4 × Cross Dissolve (map → location transitions, 0.5s each)
2. Apply 3 × Light Leak (chorus entries, 0.5s each, warm amber)
3. Apply Fade to Black on S35b (3s)
4. Verify no forbidden transitions
5. **Save project** as `EP02_v05_transitions`

### Phase 6: Global Effects (Adjustment Layer)
1. Import Kodachrome LUT (.cube) → apply to adjustment layer (80-100%)
2. Set Color Match reference to S12 → match all clips
3. Apply Film Grain (12%) to adjustment layer
4. Apply Vignette (20%) to adjustment layer
5. Set Letterbox 2.35:1 (Player → Ratio → Customized)
6. **Save project** as `EP02_v06_graded`

### Phase 7: Color Unification
1. Scrub timeline — check color at every cut point
2. Apply tool-specific HSL corrections (Kling: amber +5-10%, Veo: curves)
3. Verify Kodachrome warmth continuous throughout
4. **Save project** as `EP02_v07_color`

### Phase 8: Selective Effects
1. Apply Chromatic Aberration to 5 damage clips (see Selective Effects Map)
2. Place Light Leak overlays at 3 chorus entries (overlay track, 60-70% opacity)
3. Optional: Freeze Frame at high-impact moments (S07 eruption, S32 ear) — 0.25-0.5s max
4. **Save project** as `EP02_v08_effects`

### Phase 9: Export & QA
1. Full preview at 1× speed with audio — note any issues
2. Run QA Checklist (Section 11)
3. Fix any issues found
4. Export: 4K, H.265, 50 Mbps, 24fps, MP4, no watermark
5. Output: `episode-02/06_edit/ep02_final_v01.mp4`
6. **Save final project** as `EP02_FINAL_v01`

---

*"The edit is where the vision meets the frame. Every cut is a breath, every transition a heartbeat. Make it invisible — the best edit is the one the viewer never notices."*

*Would Fibula approve this?*
