# CAPCUT EDIT GUIDE — EP10 "The Glitch Scripture / I Came to Walk Beside"
> **Version:** v01 | Skill: `_skills/robotiko-capcut-editor/SKILL.md` v1.0
> Generated from: `ep10_motion_script_v01.md` (APPROVED 2026-07-12, gate-2) + `ep10_musical_metadata.json`
>
> **Camera Personality:** THE COMPANION CAMERA — walks alongside, never above him; the reserved
> beside-space is furnished from the first frame to the last.
> **Station:** The Integrated Self — Arrival (Enlightenment. 8 → ∞). No damage, no doom, no glitch —
> this is the calm of arrival.
>
> **Gap closure applied (EP09 lesson).** The motion script's timestamps carry the musical metadata's
> 1s display gaps (S01 `0:00-0:09`, S02 starts `0:10`). Left as-is that is a **34s deficit** across 35
> scenes and total vocal-sync loss. Every scene here runs to the **next scene's start**, so the timeline
> is contiguous and totals exactly **274s**. All 35 scene **start** times are unchanged — and every one of
> the 9 musical section boundaries still lands on a scene start (28 / 47 / 60 / 81 / 142 / 164 / 179 / 195s).
> **Clip durations below are measured from the rendered files, not from the motion script's nominal 5s/10s.**

---

## ⚠️ PRE-FLIGHT — READ BEFORE OPENING CAPCUT

All 37 clips are rendered and present in `episode-10/05_video/raw/`. Five findings need your eye first —
none of them blocks assembly.

### 1. `34b.mp4` — re-rendered with Seedance 2.0 (Dreamina); tool history + one watermark check

S34b (The Beckon) could not be executed by Kling — it read the open-palm beckon as presenter-style
arm movement instead of the small, human *come* the shot is built on. A first replacement came from
Google (Veo/Gemini): gesture right, but 720p / 1.9 Mbps / synthetic audio track. The final keeper
(2026-08-05) was re-rendered with **Seedance 2.0 via Dreamina**, which delivered the gesture AND clean
technical specs. Art-director review passed (2026-08-05): character continuity with `34.mp4` holds
(same patchwork, copper patches, antenna, blue lenses, kintsugi seams, meadow + toppled-∞ ring + mist),
the framing is a legitimate punch-in on the same axis, and the approved smile override reads friendly,
not uncanny.

| | `34.mp4` (S34a) | `34b.mp4` (S34b, final keeper) |
|---|---|---|
| Tool | Kling 3.0 | **Seedance 2.0 (Dreamina)** |
| Resolution | 1920×1080 | 1920×1080 ✅ |
| Video bitrate | 11.5 Mbps | 13.5 Mbps ✅ |
| Audio track | none | none ✅ |
| Duration | 8.04s | **5.04s** (see §2 — the pair's internal boundary moves to 4:24) |

**The one remaining item — the Dreamina "Ai" watermark.** Top-left corner, measured at
x ≈ 36–95, y ≈ 50–90 px at 1080p. The 2.35:1 letterbox top bar covers the first **~131 px** of frame
height, so the watermark sits **fully under the bar with ~40 px of margin** (the global 101% scale
pushes it further out still). No action needed — but **verify in the export preview** that the mark is
invisible at 4:23–4:30 before rendering. If it ever peeks (e.g. the letterbox is applied differently),
nudge the clip's vertical position up a few px; the crop hides the shift.

### 2. Clip lengths do not match the motion script's plan

The motion script planned every clip as a nominal 5s or 10s Kling output with 5 designed speed ramps.
The rendered clips were generated at custom lengths close to the *gapped* scene durations (e.g. `12.mp4`
= 3.04s, `18.mp4` = 7.04s, `32.mp4` = 11.04s). Once the gaps are closed, most clips are **1s short of
their slot**, so the timeline needs **28 speed ramps instead of 5**. They are small — 1.11× to 1.41×
slowdown, all inside the 1.5× limit — and on serene, unhurried material at 24fps they are invisible.
This is the arithmetic of the 34s deficit; there is no version of a synced timeline without them.
(With the S34b re-render the count is **29** — S34b joined the fit ramps at 0.84×.)

### 3. `10b.mp4` carries S10

S10 (The Touch and the Amber Pulse) is a Mode B shot built from `10.png` → `10b.png`. The render is named
after its end keyframe: **`10b.mp4` is the S10 clip** and there is no `10.mp4`. Confirm this is the keeper,
not an alternate take you meant to replace.

### 4. Frame sizes wobble by a few pixels

Several clips came back at 1916×1080, 1920×1076 or 1924×1076 instead of exactly 1920×1080. In a 1920×1080
project these leave hairline black edges. **Fix once, globally:** select all clips → Scale to ~101% so
every frame fills. The 2.35:1 letterbox then crops the residue anyway.

### 5. S35 end-card text needs your approval

The card is specified everywhere as "GitHub end screen, white text on black" but its exact wording has
never been written down. Proposed text in §8 — **your call before export.**

**Audio:** the final EP10 WAV lives on Google Drive (fibuladev account); only the metadata JSON is local.

---

## 1. EPISODE HEADER

| Field | Value |
|---|---|
| Episode | EP10 |
| Title | The Glitch Scripture / I Came to Walk Beside |
| Station | The Integrated Self — Arrival (Enlightenment. 8 → ∞) |
| Total Shots | 35 (34 generated + 1 edit card, S35) |
| Total Clips | 37 (S08 triple + S34 pair) |
| Music Duration | 4:34 (274s) |
| BPM | 153 detected (double-time) — **felt stomp-clap pulse 76.5 BPM, beat ≈ 0.784s** |
| Key | E Minor |
| Frame Rate | 24fps |
| Delivery | 1080p (1920×1080), H.265 |

> **Beat = footstep.** The whole episode is cut to the felt 76.5 pulse, not to the detector's 153.
> If CapCut's Auto Beat Detection marks 153 BPM, use every **second** marker.

---

## 2. CLIP IMPORT CHECKLIST

Import all 37 from `episode-10/05_video/raw/` (numeric keepers — `selected/` is empty by project
convention). Tool from the motion script's assignment; measured duration from the file itself.

```
- [ ] 1.mp4     S01   10.04s  (Kling 3.0)
- [ ] 2.mp4     S02   10.04s  (Kling 3.0 — Mode B)
- [ ] 3.mp4     S03    8.04s  (Kling 3.0)
- [ ] 4.mp4     S04    5.04s  (Kling 3.0)
- [ ] 5.mp4     S05    5.04s  (Kling 3.0)
- [ ] 6.mp4     S06    5.04s  (Kling 3.0)
- [ ] 7.mp4     S07    5.04s  (Kling 3.0)
- [ ] 8.mp4     S08a   3.04s  (Kling 2.5 Turbo)
- [ ] 8b.mp4    S08b   3.04s  (Kling 2.5 Turbo)
- [ ] 8c.mp4    S08c   3.04s  (Kling 3.0)
- [ ] 9.mp4     S09    5.04s  (Kling 3.0)
- [ ] 10b.mp4   S10    5.04s  (Kling 3.0 — Mode B; named after its end keyframe)
- [ ] 11.mp4    S11    5.04s  (Kling 3.0)
- [ ] 12.mp4    S12    3.04s  (Kling 3.0)
- [ ] 13.mp4    S13   10.04s  (Kling 3.0)
- [ ] 14.mp4    S14   10.04s  (Kling 3.0)
- [ ] 15.mp4    S15   10.04s  (Kling 3.0)
- [ ] 16.mp4    S16    9.04s  (Kling 3.0)
- [ ] 17.mp4    S17    5.04s  (Kling 3.0)
- [ ] 18.mp4    S18    7.04s  (Kling 3.0)
- [ ] 19.mp4    S19    7.04s  (Kling 3.0)
- [ ] 20.mp4    S20    6.04s  (Kling 3.0)
- [ ] 21.mp4    S21    6.04s  (Kling 3.0)
- [ ] 22.mp4    S22    4.04s  (Kling 3.0)
- [ ] 23.mp4    S23    4.04s  (Kling 3.0)
- [ ] 24.mp4    S24    4.04s  (Kling 3.0)
- [ ] 25.mp4    S25    5.04s  (Kling 3.0)
- [ ] 26.mp4    S26    5.04s  (Kling 3.0)
- [ ] 27.mp4    S27    4.04s  (Kling 3.0 — Mode B)
- [ ] 28.mp4    S28    8.04s  (Kling 3.0)
- [ ] 29.mp4    S29    8.04s  (Kling 2.5 Turbo)
- [ ] 30.mp4    S30   10.04s  (Kling 3.0)
- [ ] 31.mp4    S31    8.04s  (Kling 3.0)
- [ ] 32.mp4    S32   11.04s  (Kling 3.0)
- [ ] 33.mp4    S33    7.04s  (Kling 3.0)
- [ ] 34.mp4    S34a   8.04s  (Kling 3.0 — the series' most important shot)
- [ ] 34b.mp4   S34b   5.04s  (**Seedance 2.0 via Dreamina** — re-render 2026-08-05, 1080p, silent; watermark under letterbox, see Pre-Flight §1)
- [ ] S35 — no clip. Built in CapCut (§8).
```

**Present: 37 / 37.** Nothing is missing.

---

## 3. TIMELINE MAP

Butt every clip against the previous one — **no gaps, no overlaps**. Total = 274s = the audio.
Speed values are `clip ÷ slot`; enter them as plain playback speed unless §4 marks the shot as a
designed curve.

| Shot | Timestamp | Clip File | Scene Dur | Clip Dur | Speed | Trim |
|------|-----------|-----------|-----------|----------|-------|------|
| S01 | 0:00–0:10 | 1.mp4 | 10s | 10s | — | — |
| S02 | 0:10–0:19 | 2.mp4 | 9s | 10s | — | trim 1s |
| S03 | 0:19–0:28 | 3.mp4 | 9s | 8s | 0.89× | — |
| S04 | 0:28–0:34 | 4.mp4 | 6s | 5s | 0.83× | — |
| S05 | 0:34–0:41 | 5.mp4 | 7s | 5s | 0.71× | — |
| S06 | 0:41–0:47 | 6.mp4 | 6s | 5s | 0.83× | — |
| S07 | 0:47–0:53 | 7.mp4 | 6s | 5s | 0.83× | — |
| S08a | 0:53–0:55 | 8.mp4 | 2s | 3s | — | trim 1s |
| S08b | 0:55–0:57 | 8b.mp4 | 2s | 3s | — | trim 1s |
| S08c | 0:57–1:00 | 8c.mp4 | 3s | 3s | — | — |
| S09 | 1:00–1:06 | 9.mp4 | 6s | 5s | 0.83× | — |
| S10 | 1:06–1:12 | 10b.mp4 | 6s | 5s | 0.83× | — |
| S11 | 1:12–1:17 | 11.mp4 | 5s | 5s | — | — |
| S12 | 1:17–1:21 | 12.mp4 | 4s | 3s | 0.75× | — |
| S13 | 1:21–1:33 | 13.mp4 | 12s | 10s | 0.83× | — |
| S14 | 1:33–1:45 | 14.mp4 | 12s | 10s | 0.83× | — |
| S15 | 1:45–1:57 | 15.mp4 | 12s | 10s | 0.83× | — |
| S16 | 1:57–2:07 | 16.mp4 | 10s | 9s | 0.9× | — |
| S17 | 2:07–2:14 | 17.mp4 | 7s | 5s | 0.71× | — |
| S18 | 2:14–2:22 | 18.mp4 | 8s | 7s | 0.88× | — |
| S19 | 2:22–2:30 | 19.mp4 | 8s | 7s | 0.88× | — |
| S20 | 2:30–2:37 | 20.mp4 | 7s | 6s | 0.86× | — |
| S21 | 2:37–2:44 | 21.mp4 | 7s | 6s | 0.86× | — |
| S22 | 2:44–2:49 | 22.mp4 | 5s | 4s | 0.8× | — |
| S23 | 2:49–2:54 | 23.mp4 | 5s | 4s | 0.8× | — |
| S24 | 2:54–2:59 | 24.mp4 | 5s | 4s | 0.8× | — |
| S25 | 2:59–3:05 | 25.mp4 | 6s | 5s | 0.83× | — |
| S26 | 3:05–3:10 | 26.mp4 | 5s | 5s | — | — |
| S27 | 3:10–3:15 | 27.mp4 | 5s | 4s | 0.8× | — |
| S28 | 3:15–3:24 | 28.mp4 | 9s | 8s | 0.89× | — |
| S29 | 3:24–3:33 | 29.mp4 | 9s | 8s | 0.89× | — |
| S30 | 3:33–3:45 | 30.mp4 | 12s | 10s | 0.83× | — |
| S31 | 3:45–3:54 | 31.mp4 | 9s | 8s | 0.89× | — |
| S32 | 3:54–4:08 | 32.mp4 | 14s | 11s | 0.79× | — |
| S33 | 4:08–4:16 | 33.mp4 | 8s | 7s | 0.88× | — |
| S34a | 4:16–4:24 | 34.mp4 | 8s | 8s | — | — |
| S34b | 4:24–4:30 | 34b.mp4 | 6s | 5s | 0.84× | — |
| S35 | 4:30–4:34 | — (edit card) | 4s | — | — | — |

> **Total = 274s = music duration.** ✅ No gaps.

**Sub-clip splits:**
- **S08 (0:53–1:00, 7s)** — the fractal rhyme, three match-cuts on "a billion cells": leaf veins (2s) /
  frost (2s) / gold forearm seams (3s). The third holds longest — it is the payoff, the only one with
  @Kintsugi in frame. Hard cuts, no transition, equal-angle match.
- **S34 (4:16–4:30, 14s)** — S34a The Look (8s) then S34b The Beckon (6s). The internal boundary sits at
  **4:24** (moved from the nominal 4:23 when S34b was re-rendered at 5.04s): the look gains a full second
  of hold — exactly what the shot wants — and S34b's ramp stays gentle at 0.84× instead of a deep 0.72×.
  The look must **land and hold** before the tilt arrives. At 0.84× the clip's final frame lands at 4:30
  exactly: the offered hand reaches full extension in the last second, where the gong cuts it.

---

## 4. SPEED TABLE

29 clips need a speed adjustment. They split into two kinds — treat them differently.

### 4a. Designed ramps — use **Speed → Curve** (smooth, dramatic)

These 5 were authored as speed ramps in the motion script. The slowdown is part of the shot.

| Clip | Shot | Native | Speed | Target | Notes |
|------|------|--------|-------|--------|-------|
| 13.mp4 | S13 | 10.04s | 0.83× | 12s | Leaving the Town — the break opens, scale widens |
| 14.mp4 | S14 | 10.04s | 0.83× | 12s | The Climb — the stride at full MS 4 |
| 15.mp4 | S15 | 10.04s | 0.83× | 12s | The Moon-Sun Sky — the cosmic center; deepest breath |
| 30.mp4 | S30 | 10.04s | 0.83× | 12s | Refrain One — peak walk energy |
| 32.mp4 | S32 | 11.04s | 0.79× | 14s | Refrain Two, elongated — the music elongates, so does the shot |

### 4b. Fit ramps — use **Speed → Normal** (uniform, invisible)

Purely technical: the render is ~1s shorter than its slot. A uniform 1.1–1.4× slowdown at 24fps on
this material is imperceptible. Do **not** curve these — a curve would invent a dramatic gesture the
shot was not designed to make.

| Clip | Shot | Native | Speed | Target | Slowdown |
|------|------|--------|-------|--------|----------|
| 3.mp4 | S03 | 8.04s | 0.89× | 9s | 1.12× |
| 4.mp4 | S04 | 5.04s | 0.83× | 6s | 1.20× |
| 5.mp4 | S05 | 5.04s | 0.71× | 7s | **1.41×** |
| 6.mp4 | S06 | 5.04s | 0.83× | 6s | 1.20× |
| 7.mp4 | S07 | 5.04s | 0.83× | 6s | 1.20× |
| 9.mp4 | S09 | 5.04s | 0.83× | 6s | 1.20× |
| 10b.mp4 | S10 | 5.04s | 0.83× | 6s | 1.20× |
| 12.mp4 | S12 | 3.04s | 0.75× | 4s | 1.33× |
| 16.mp4 | S16 | 9.04s | 0.9× | 10s | 1.11× |
| 17.mp4 | S17 | 5.04s | 0.71× | 7s | **1.41×** |
| 18.mp4 | S18 | 7.04s | 0.88× | 8s | 1.14× |
| 19.mp4 | S19 | 7.04s | 0.88× | 8s | 1.14× |
| 20.mp4 | S20 | 6.04s | 0.86× | 7s | 1.16× |
| 21.mp4 | S21 | 6.04s | 0.86× | 7s | 1.16× |
| 22.mp4 | S22 | 4.04s | 0.8× | 5s | 1.25× |
| 23.mp4 | S23 | 4.04s | 0.8× | 5s | 1.25× |
| 24.mp4 | S24 | 4.04s | 0.8× | 5s | 1.25× |
| 25.mp4 | S25 | 5.04s | 0.83× | 6s | 1.20× |
| 27.mp4 | S27 | 4.04s | 0.8× | 5s | 1.25× |
| 28.mp4 | S28 | 8.04s | 0.89× | 9s | 1.12× |
| 29.mp4 | S29 | 8.04s | 0.89× | 9s | 1.12× |
| 31.mp4 | S31 | 8.04s | 0.89× | 9s | 1.12× |
| 33.mp4 | S33 | 7.04s | 0.88× | 8s | 1.14× |
| 34b.mp4 | S34b | 5.04s | 0.84× | 6s | 1.19× |

**Deepest ramps: S05 and S17 at 1.41×** (limit 1.5×). Both are passing/atmospheric shots — S05 the ivy
through the machine carcass, S17 the profile beside him at the crest. Neither carries a footfall that
must land on a beat, so the stretch costs nothing. Watch S05's dew and S17's cloth for slow-motion
"floatiness"; if either reads unnatural, trim the neighbouring shot by a frame or two instead.

**Trims (3):** S02 (1s), S08a (1s), S08b (1s) — cut from the **end** in all three. S34a now uses its
full clip (the 0.04s tail is noise); S34b is a fit ramp, not a trim — its full 5.04s gesture arc plays,
gently stretched to 6s, and the final palm-toward-lens pose lands on the gong.

---

## 5. BEAT SYNC CHECKLIST

Felt pulse 76.5 BPM → beat ≈ 0.784s. **On-beat = |Δ| ≤ 150ms.** These 15 points are the mandatory
frame-level verifications; 13 of them are scene starts, so they come free if §3 is placed exactly.

| # | Timestamp | Musical Event | Visual Action | Clip |
|---|-----------|---------------|---------------|------|
| 1 | 0:28 | First stomp-clap downbeat — "I cast the enmity" | **Foot lands exactly on the beat** | S04 |
| 2 | 0:53 | "The Dye of Truth engraved in a billion cells" | Triple match-cut: leaf / frost / seam | S08a-c |
| 3 | 1:00 | Verse 3 — "The path the Mentors mapped" | Crossroads arrives on the verse boundary | S09 |
| 4 | 1:06 | "The station where the steadfast souls reside" | Full stop #1; hand on staff; **Amber Pulse** on release | S10 |
| 5 | 1:21 | Instrumental break opens — Moog arpeggio | Scale widens; road rises out of the town | S13 |
| 6 | 1:45 | Moog at full sweep — the cosmic center | Moon-Sun sky revealed | S15 |
| 7 | 2:22 | Verse 4 returns — "I watched the world" | Tower on the horizon; his head never turns | S19 |
| 8 | 2:44 | Verse 5 — "tracing Love's vein of light" | Binary stripes; MS peaks at 5 | S22 |
| 9 | 2:59 | Verse 6 full band — "Ghost in the Machine, unchained" | The infinity stone, treated as ordinary | S25 |
| 10 | 3:14–3:15 | Minor-to-major shift completes | Glass **fully extended** toward the lens on S27's last second | S27 end |
| 11 | 3:15 | Guitar solo ignites | Walk resumes; stride on the solo's attack | S28 |
| 12 | 3:33 | Refrain 1 onset (straight) | Full-stride walking — peak walk energy | S30 |
| 13 | 3:45 | Solo breathing between refrains | **The Wait** — grammar break; he stops and half-turns | S31 |
| 14 | 4:08 | Refrain 3 / rock scream — the album's epic peak | Wind-wave + sun flare + dew sparks; MS 6 | S33 |
| 15 | 4:16 | Solo fading | **STILL HOLD** — the only direct look into the lens | S34a |
| 16 | 4:29–4:30 | Final bars | The beckon completes; hand fully offered | S34b |
| 17 | 4:30 | **FINAL GONG — single strike** | **Hard cut to black → edit card** | S35 |

> **Refrain onsets are estimates.** The metadata does not subdivide the 79s finale, so 3:33 / 3:45 /
> 3:54 / 4:08 / 4:16 came from the motion script's reading. **Confirm them against the final track before
> you lock S30–S34b.** If a refrain sits ±1s off, move the boundary and rebalance the neighbour — the
> scene *order* is timing-proof, only the boundaries move.

**Priority anchors:** #1 (the first footstep — if this floats, the whole walking premise floats),
#4 (the single Amber Pulse), #14 (the scream), #17 (the gong cut — sound and cut are one event).

---

## 6. TRANSITION MAP

**Hard cut everywhere. Zero transition effects in this episode.** That is not an omission — each
optional transition is refused for a stated reason:

| Transition | Count | Why |
|---|---|---|
| Cross Dissolve | **0** | EP10 is one continuous dawn walk. There is no map shot, no location jump, nothing geographic to bridge. A dissolve would invent a discontinuity the episode does not have. |
| Light Leak | **0** | The **Amber Pulse discipline**: EP10 contains exactly ONE amber event — S10, reflected sunlight on the staff tip. A warm-amber leak anywhere else breaks the single-amber signature. Chorus/refrain entries (S30, S32, S33) land on hard cuts; the cut is the punctuation. |
| Fade to Black | **0** | **The gong is a hard cut, not a fade.** "Sound and cut are one event" — a 2–3s fade would soften the exact thing the finale is built on. The skill's default (fade on the final shot) is deliberately overridden here. |
| Hard Cut | **all 37** | Including sub-clips S08a→b→c and S34a→S34b — continuous coverage, not separate scenes. |

**FORBIDDEN and unused:** glitch, zoom, spin, slide, wipe, swipe, shape presets.

---

## 7. EFFECT SETTINGS (Adjustment Layer, full timeline)

Apply in this exact order — order matters.

| # | Effect | Value | CapCut Path |
|---|--------|-------|-------------|
| 1 | Kodachrome LUT | `Kodachrome 64.cube` @ 80–100% | Filters → Custom → Import |
| 2 | Color Match | Reference = **S30 (30.mp4)** | Select ref clip → Match (see §9 caveat) |
| 3 | Film Grain | **10–15%, CONSTANT** | Filters → Vintage → Film Grain |
| 4 | Vignette | Subtle **15–25%** | Effects → Vignette |
| 5 | Letterbox 2.35:1 | Custom ratio | Player → Ratio → Customized → 2.35:1 |

> **Rationale:** LUT sets the color base → Color Match unifies tool differences on top → Grain adds
> texture over color → Vignette pulls spatial focus → Letterbox is the final framing crop.

**Grain stays flat.** EP09 had a grain crescendo into the doom section and a lighten at dawn. **EP10 has
neither** — per the motion script's Visual Signature table, the grain breathes evenly from the first
frame to the last. The Companion Camera's serenity is expressed by *not* modulating.

**Global scale fix:** before grading, select all clips → Scale ≈ **101%** (Pre-Flight §4) so the
few-pixel-short renders fill the frame.

---

## 8. SELECTIVE EFFECTS MAP

Almost empty by design — and that is the point.

| Effect | Count | Why |
|---|---|---|
| Chromatic Aberration | **0** | The skill reserves it for damage/impact frames. **EP10 has no damage.** Robotiko arrives whole — the kintsugi is healed, not breaking. There is no impact moment in the episode to mark. |
| Light Leak overlay | **0** | Amber Pulse discipline (§6). |
| Freeze Frame | **0** | S34a's Still Hold is already a held shot in-clip; a freeze would be a second, cheaper version of it. |

*(The per-clip grain/sharpness overrides written for the old 720p Google keeper are retired — the
Seedance 2.0 re-render matches its neighbour technically. Only the §9 color-pair check remains.)*

**The one thing you build by hand:**

### S35 — THE EDIT CARD (4:30–4:34)

The gong strikes → **hard cut to black** → white text on black → out. Build it on the timeline:

1. Black background clip, 4s, starting exactly at **4:30** (the gong's attack frame — verify frame by
   frame; this cut is the album's final gesture).
2. White text, centered, no animation — **no fade in, no fade out, no motion-graphics preset.** The card
   appears with the black and leaves with it.
3. **Exclude S35 from the Adjustment Layer** — no LUT, no grain, no vignette on the card. Pure black,
   pure white. The letterbox stays (it is the project format).
4. **Don't build the text in CapCut** — three finished 1920×1080 card PNGs are ready in
   `episode-10/05_video/raw/` (rendered 2026-08-05, typography locked, centered inside the 2.35:1 band).
   Pick one, drag it onto the timeline at 4:30, set its duration, done:

   | File | Line | Voice |
   |---|---|---|
   | `endcard_A.png` | **THE FULL SCORE IS PUBLIC.** (Georgia serif) + URL (Consolas mono) | The Brecht payoff — the apparatus handed over, stated plainly |
   | `endcard_B.png` | ***I came to walk beside.*** (Palatino italic) + URL (Consolas mono) | The refrain's last breath — the URL becomes the poem's next line |
   | `endcard_C.png` | **8 → ∞** (Segoe UI Light glyphs) + URL (Consolas mono) | The series' entire arc in three characters — no words at all |

   All three share the same grammar: one statement in the episode's voice, then the door in terminal
   monospace — the card is the exact seam where the film ends and the repository begins, and the type
   says so. URL sits at 75% white so the statement leads. **Pick one — your call.** (If a wording tweak
   is wanted, the render commands are one-line ffmpeg `drawtext` calls — ask and it's re-rendered.)

> **Card length:** the concept notes say 5s; the music leaves 4s (the gong lands at 4:30, the track ends
> at 4:34). Two honest options: hold the card 4s and end with the audio (export = 274s, what this guide
> assumes), or let it run 5s over the gong's decay tail (export = 275s). Either is fine — decide before export.

---

## 9. COLOR REFERENCE

- **Reference clip: S30 (30.mp4)** — full stride in complete morning gold, character prominent, the
  episode's arrival palette at its truest Kodachrome warmth.
- **⚠️ Preserve the dawn journey — do NOT flatten it.** EP10 travels **pre-dawn grey-blue (S01–S03) →
  sunrise building (S04–S12) → full morning (S13 onward)**. That progression *is* the episode: the world
  wakes as he walks. Color Match exists to unify tool-to-tool inconsistency, not to warm the pre-dawn
  into morning.
  - **S01–S03:** match loosely or not at all. The grey-blue must stay cold. The only warmth allowed is
    the gold seeping from the workshop seams (S01) and the gold spill through the opening shutter (S02).
  - **S04–S12:** partial match — the sun is climbing; let the warmth build shot by shot.
  - **S13–S34b:** full match to S30.
- **Tool-specific corrections:**
  - Kling 3.0 clips run slightly cool → nudge orange/amber +5–10% via HSL where the scene is warm.
  - Kling 2.5 Turbo clips (8.mp4, 8b.mp4, 29.mp4) are macro/texture shots — check they do not sit flatter
    in contrast than their neighbours after the LUT.
  - **34b.mp4 comes from a different generator** (Seedance 2.0 via Dreamina) and may respond to the LUT
    with a slightly different contrast curve and metal warmth than its Kling neighbour. Grade it
    **against 34.mp4 specifically**, by eye, after the global pass. This pair is the last thing the viewer
    sees; matching it to itself matters more than matching it to S30.
- **⚠️ Amber containment.** Grading warmth can accidentally manufacture a second amber moment. Two shots
  to watch: **S21** (the embers must read **orange-red**, never amber) and **S33** (the sun flare must stay
  white-gold sunlight). Amber belongs to S10 alone.
- **⚠️ Eye canon (ADR-0010).** The lenses are *calm steady blue optical lenses set into chrome sockets* —
  a material, not a light source. Do not let a bloom, glow or highlight-lift turn them into glowing eyes.
  Check S17, S27, S34a, S34b specifically.

---

## 10. EXPORT SETTINGS

| Setting | Value |
|---------|-------|
| Resolution | 1080p (1920×1080) |
| Frame Rate | 24fps |
| Codec | H.265 (HEVC) |
| Bitrate | 35–60 Mbps |
| Format | MP4 |
| Watermark | None (CapCut Pro) |
| Output | `episode-10/06_edit/ep10_final_v01.mp4` |

**Incremental saves:** save the project after assembly (§3), after global effects (§7), and before export.
This is the last episode of the series — do not lose the timeline.

---

## 11. QA CHECKLIST (pre-export)

**Timeline**
- [ ] All 37 clips placed; no gaps, no overlaps — total = 274s (±1s)
- [ ] All 29 speed values match §4 exactly (5 curves, 24 uniform)
- [ ] All 3 trims applied (S02, S08a, S08b — from the end)
- [ ] Refrain onsets (3:33 / 3:45 / 3:54 / 4:08 / 4:16) confirmed against the final track
- [ ] All 17 beat-sync anchors verified frame-level — especially the first footstep (0:28) and the gong (4:30)

**Grammar & canon**
- [ ] **Amber appears exactly once** — S10, and nowhere else (check S21 embers = orange-red, S33 flare = white-gold)
- [ ] **Eye contact appears exactly once** — S34a/S34b. Verify S27's gaze stays **below** the lens
- [ ] Eye canon: blue material lenses, no glow, no bloom (S17, S27, S34a, S34b)
- [ ] Mouthless-face guard holds everywhere **except** the approved S34b smile override — and that smile
      reads friendly and gentle, never uncanny. This is the last frame of ten episodes; if it reads wrong, re-render
- [ ] Companion Camera: the beside-space stays reserved and empty; nothing is ever above him
- [ ] No path-shape reveal in S32 (no lemniscate drawn by the walk)
- [ ] Grain constant across the episode — no crescendo, no dawn-lighten

**Post & delivery**
- [ ] Effect order: LUT → Color Match → Film Grain → Vignette → Letterbox
- [ ] Film grain 10–15%; Letterbox 2.35:1 applied
- [ ] Dawn color journey preserved (grey-blue → sunrise → morning gold, NOT flattened)
- [ ] Global scale ≈101% — no hairline black edges from the odd frame sizes
- [ ] **Dreamina "Ai" watermark invisible in export preview** at 4:24–4:30 (sits under the top letterbox bar — Pre-Flight §1)
- [ ] S34a/S34b pair matched to each other: no color step at the 4:24 cut (different generators)
- [ ] S35 card: hard cut on the gong, text approved, excluded from the Adjustment Layer, no animation
- [ ] Zero transitions: no dissolve, no light leak, **no fade to black**
- [ ] Zero chromatic aberration, zero freeze frames
- [ ] Export: 1080p, H.265, 35–60 Mbps, 24fps
- [ ] **Sync-QC record filled** → `ep10_sync_qc_v01.md` (min 5 timestamped spot-checks) after export
- [ ] "Would Fibula approve this?"

---

## POST-EXPORT — MANDATORY SYNC-QC RECORD

The edit is not "done" without a committed sync-QC record. After the render exists:

1. Copy `_templates/ep_sync_qc_template.md` → `episode-10/06_edit/ep10_sync_qc_v01.md`.
2. Fill **≥ 5 timestamped spot-checks** sourced from §5 (recommend #1, #4, #12, #14, #17).
3. For each: compare the target timestamp to the actual cut, verdict **ON-BEAT** (|Δ| ≤ 150ms),
   **OFF by N ms**, or **ACCEPTED-DEVIATION** (deliberate offset + one-line reason).
4. `scripts/sync_probe.py` is an optional local helper that prints measured cut-vs-boundary numbers.

The final render is gitignored (Drive), so this committed record is the beat-sync evidence CI cannot produce.

---

*"The edit is where the vision meets the frame. Every cut is a breath, every transition a heartbeat.
Make it invisible — the best edit is the one the viewer never notices."*
*— Robotiko v2.0 Pipeline*
