# CAPCUT EDIT GUIDE — EP09 "Shadow Debugging"
> **Version:** v01 | Skill: `_skills/robotiko-capcut-editor/SKILL.md` v1.0
> Generated from: `ep09_motion_script_v02.md` (APPROVED) + `ep09_musical_metadata.json`
> Camera Personality: **The Discovering Camera** — Slow Zoom Out = understanding widens (not retreat)
> Phase Transition: **@Damaged → @Kintsugi at S27 (4:09)**

---

## ⚠️ PRE-FLIGHT — READ FIRST

This guide is the **blueprint you execute across the CapCut edit session**. Two source clips are
not yet rendered at guide-generation time — the guide is complete, but **do not export until
both are in `05_video/raw/`:**

| Missing Clip | Shot | Status |
|---|---|---|
| `37.mp4` | **S37** — The Dawn (exterior crane up) | Video-gen queue (episode is at 37/38 scenes rendered) |
| `36b.mp4` | **S36b** — Dawn Breaks (Chain-2 second sub-clip) | Chained clip — generate from S36a's exported last frame |

**Clip source:** clips are read from `episode-09/05_video/raw/` (numeric keepers — `selected/` is empty
by project convention; the motion script points here). **Audio** is the episode WAV from Google Drive
(fibuladev account) — only the metadata JSON is local.

---

## 1. EPISODE HEADER

| Field | Value |
|---|---|
| Episode | EP09 |
| Title | Shadow Debugging |
| Station | The Integrated Self (Kintsugi — making peace with flaws) |
| Total Shots | 38 |
| Total Clips | 41 (3 multi-clip scenes: S27, S35, S36) |
| Music Duration | 7:03 (423s) |
| BPM | 77 (1 beat ≈ 0.779s) |
| Key | E Minor |
| Frame Rate | 24fps |
| Delivery | 1080p (1920×1080), H.265 |

---

## 2. CLIP IMPORT CHECKLIST

Import all clips from `episode-09/05_video/raw/`. Tool in parentheses (from motion script assignment).

```
- [ ] 1.mp4    S01  (Kling 3.0)
- [ ] 2.mp4    S02  (Kling 3.0)
- [ ] 3.mp4    S03  (Kling 3.0)
- [ ] 4.mp4    S04  (Kling 2.5 Turbo)
- [ ] 5.mp4    S05  (Kling 3.0)
- [ ] 6.mp4    S06  (Kling 3.0)
- [ ] 7.mp4    S07  (Kling 3.0)
- [ ] 8.mp4    S08  (Kling 3.0)
- [ ] 9.mp4    S09  (Kling 2.5 Turbo)
- [ ] 10.mp4   S10  (Kling 3.0)
- [ ] 11.mp4   S11  (Kling 3.0 — Mode B)
- [ ] 12.mp4   S12  (Kling 3.0)
- [ ] 13.mp4   S13  (Kling 3.0)
- [ ] 14.mp4   S14  (Kling 3.0)
- [ ] 15.mp4   S15  (Kling 3.0)
- [ ] 16.mp4   S16  (Kling 3.0)
- [ ] 17.mp4   S17  (Kling 3.0)
- [ ] 18.mp4   S18  (Kling 3.0)
- [ ] 19.mp4   S19  (Kling 3.0)
- [ ] 20.mp4   S20  (Kling 3.0)
- [ ] 21.mp4   S21  (Kling 3.0)
- [ ] 22.mp4   S22  (Kling 3.0)
- [ ] 23.mp4   S23  (Kling 3.0)
- [ ] 24.mp4   S24  (Kling 3.0)
- [ ] 25.mp4   S25  (Kling 3.0)
- [ ] 26.mp4   S26  (Kling 3.0)
- [ ] 27.mp4   S27a (Kling 3.0 — Mode B)
- [ ] 27b.mp4  S27b (Kling 3.0)
- [ ] 28.mp4   S28  (Kling 3.0)
- [ ] 29.mp4   S29  (Kling 3.0)
- [ ] 30.mp4   S30  (Kling 3.0)
- [ ] 31.mp4   S31  (Kling 3.0)
- [ ] 32.mp4   S32  (Kling 3.0)
- [ ] 33.mp4   S33  (Kling 3.0)
- [ ] 34.mp4   S34  (Kling 3.0 — Chain 1 start)
- [ ] 35.mp4   S35a (Kling 3.0 — Chain 1)
- [ ] 35b.mp4  S35b (Kling 3.0 — Chain 1 end)
- [ ] 36.mp4   S36a (Kling 3.0 — Chain 2 start)
- [ ] ⚠️ 36b.mp4  S36b (Kling 3.0 — Chain 2 end) — NOT YET RENDERED
- [ ] ⚠️ 37.mp4   S37  (Kling 3.0) — NOT YET RENDERED
- [ ] 38.mp4   S38  (Seedance 1.0)
```

**Present: 39 / 41.** The two ⚠️ clips must be rendered and imported before final assembly is complete.

---

## 3. TIMELINE MAP

Placement is contiguous — every second of the 423s audio is covered (the small display gaps in the
motion-script timestamps are cosmetic; butt every clip against the previous one).

| Shot | Timestamp | Clip File | Scene Dur | Clip Dur | Speed | Trim |
|------|-----------|-----------|-----------|----------|-------|------|
| S01 | 0:00–0:14 | 1.mp4 | 14s | 10s | 0.71× | — |
| S02 | 0:14–0:26 | 2.mp4 | 11s | 10s | 0.91× | — |
| S03 | 0:26–0:39 | 3.mp4 | 12s | 10s | 0.83× | — |
| S04 | 0:39–0:49 | 4.mp4 | 9s | 10s | — | trim 1s |
| S05 | 0:49–0:59 | 5.mp4 | 9s | 10s | — | trim 1s |
| S06 | 0:59–1:05 | 6.mp4 | 5s | 10s | — | trim 5s |
| S07 | 1:05–1:12 | 7.mp4 | 6s | 10s | — | trim 4s |
| S08 | 1:12–1:23 | 8.mp4 | 10s | 10s | — | — |
| S09 | 1:23–1:28 | 9.mp4 | 5s | 10s | — | trim 5s |
| S10 | 1:28–1:34 | 10.mp4 | 6s | 10s | — | trim 4s |
| S11 | 1:34–1:40 | 11.mp4 | 5s | 10s | — | trim 5s (Mode B) |
| S12 | 1:40–1:50 | 12.mp4 | 9s | 10s | — | trim 1s |
| S13 | 1:50–1:56 | 13.mp4 | 5s | 10s | — | trim 5s |
| S14 | 1:56–2:05 | 14.mp4 | 8s | 10s | — | trim 2s |
| S15 | 2:05–2:11 | 15.mp4 | 5s | 10s | — | trim 5s |
| S16 | 2:11–2:21 | 16.mp4 | 9s | 10s | — | trim 1s |
| S17 | 2:21–2:31 | 17.mp4 | 9s | 10s | — | trim 1s |
| S18 | 2:31–2:41 | 18.mp4 | 9s | 10s | — | trim 1s |
| S19 | 2:41–2:52 | 19.mp4 | 10s | 10s | — | — |
| S20 | 2:52–3:02 | 20.mp4 | 9s | 10s | — | trim 1s |
| S21 | 3:02–3:12 | 21.mp4 | 9s | 10s | — | trim 1s |
| S22 | 3:12–3:18 | 22.mp4 | 5s | 10s | — | trim 5s |
| S23 | 3:18–3:30 | 23.mp4 | 11s | 10s | 0.91× | — |
| S24 | 3:30–3:43 | 24.mp4 | 12s | 10s | 0.83× | — |
| S25 | 3:43–3:57 | 25.mp4 | 13s | 10s | 0.77× | — |
| S26 | 3:57–4:08 | 26.mp4 | 10s | 10s | — | — |
| S27a | 4:08–4:18 | 27.mp4 | 10s | 10s | — | (Mode B) |
| S27b | 4:18–4:28 | 27b.mp4 | 9s | 10s | — | trim 1s |
| S28 | 4:28–4:39 | 28.mp4 | 10s | 10s | — | — |
| S29 | 4:39–4:52 | 29.mp4 | 12s | 10s | 0.83× | — |
| S30 | 4:52–5:04 | 30.mp4 | 11s | 10s | 0.91× | — |
| S31 | 5:04–5:17 | 31.mp4 | 12s | 10s | 0.83× | — |
| S32 | 5:17–5:31 | 32.mp4 | 13s | 10s | 0.77× | — |
| S33 | 5:31–5:45 | 33.mp4 | 13s | 10s | 0.77× | — |
| S34 | 5:45–6:00 | 34.mp4 | 14s | 10s | 0.71× | Chain 1 START |
| S35a | 6:00–6:10 | 35.mp4 | 10s | 10s | — | Chain 1 |
| S35b | 6:10–6:20 | 35b.mp4 | 9s | 10s | — | trim 1s / Chain 1 END |
| S36a | 6:20–6:30 | 36.mp4 | 10s | 10s | — | Chain 2 START |
| S36b | 6:30–6:40 | ⚠️ 36b.mp4 | 9s | 10s | — | trim 1s / Chain 2 END |
| S37 | 6:40–6:55 | ⚠️ 37.mp4 | 14s | 10s | 0.71× | — |
| S38 | 6:55–7:03 | 38.mp4 | 7s | 10s | — | trim 3s |

> **Total timeline = 423s = music duration.** ✅ No gaps.

---

## 4. SPEED RAMP TABLE

Only the 13 clips needing a speed curve. Apply via **Speed → Curve** (smooth, not linear stutter).
All ramps are within the 1.5× slowdown limit.

| Clip | Shot | Native | Playback Speed | Target Dur | Notes |
|------|------|--------|----------------|------------|-------|
| 1.mp4 | S01 | 10s | 0.71× | 14s | The Myth — slow descent |
| 2.mp4 | S02 | 10s | 0.91× | 11s | The Puncture |
| 3.mp4 | S03 | 10s | 0.83× | 12s | Held silence |
| 23.mp4 | S23 | 10s | 0.91× | 11s | "I AM THE BUG" apex |
| 24.mp4 | S24 | 10s | 0.83× | 12s | The Collapse |
| 25.mp4 | S25 | 10s | 0.77× | 13s | **Still Hold** — deepest ramp |
| 29.mp4 | S29 | 10s | 0.83× | 12s | Lighting flip |
| 30.mp4 | S30 | 10s | 0.91× | 11s | Full Kintsugi |
| 31.mp4 | S31 | 10s | 0.83× | 12s | Frame that glows |
| 32.mp4 | S32 | 10s | 0.77× | 13s | It holds me |
| 33.mp4 | S33 | 10s | 0.77× | 13s | "I—" suspended |
| 34.mp4 | S34 | 10s | 0.71× | 14s | Dawn pull begins |
| ⚠️ 37.mp4 | S37 | 10s | 0.71× | 14s | The Dawn (pending render) |

---

## 5. BEAT SYNC CHECKLIST

BPM 77 → beat ≈ 0.779s. **On-beat = |delta| ≤ 150ms.** These 15 points from the motion script
are the mandatory frame-level verifications. After export, log the measured deltas in the sync-QC record.

| # | Timestamp | Musical Event | Visual Action | Clip |
|---|-----------|---------------|---------------|------|
| 1 | 0:26 | "Nothing comes out" — held vocal silence | Face hold, mouth opens, nothing | S03 |
| 2 | 1:05 | Saz sustain peak | Amber flicker on wrench tip — one pulse | S07 |
| 3 | 1:34 | Creeping fuzz + heartbeat pulse enters | Shutter begins closing (Mode B) | S11 |
| 4 | 1:40 | Tense heartbeat drum | Self-surgery begins — hand enters chest | S12 |
| 5 | 1:56 | Heavy fuzz rock chorus entry | Shadow starts leading — Dolly Out | S14 |
| 6 | 2:11 | Single dark drone — heavy silence | Aftermath: stillness, dust settling | S16 |
| 7 | 2:41 | First tribal drum hit | Doom frame vibration — dust lifts | S19 |
| 8 | 3:12 | Rising tribal drums + dark saz | Reboot — lamp strobing, Handheld | S22 |
| 9 | 3:18 | Massive doom — "I AM THE BUG" | Static, frame blazes [DISSONANCE] | S23 |
| 10 | 3:43 | Pure silence — a cappella | **STILL HOLD** — Static, MS 1 | S25 |
| 11 | 4:08 | "Glitch is scripture" — warm spoken word | Camera stops — first gold (Mode B) | S27a |
| 12 | 4:39 | Chorus 3 — massive fuzz wall | Lighting flip — lamp dims, core brightens | S29 |
| 13 | 4:52 | Pounding tribal drums + wailing saz | Full kintsugi reveal — widest zoom-out | S30 |
| 14 | 5:31 | "I—" unfinished | Face hold, 0.77× suspension | S33 |
| 15 | 5:45 | Fuzz guitar solo begins | Dawn pull starts — Slow Zoom Out, Chain 1 | S34 |

**Priority sync anchors:** #9 (I AM THE BUG downbeat), #10 (silence → Still Hold — visual stillness
must begin *exactly* as instruments drop), #11 (phase transition — gold must start on the warm-word
beat), #13 (kintsugi reveal on the chorus-3 drum).

---

## 6. TRANSITION MAP

**Default = hard cut everywhere.** Multi-clip sub-clips (S27a→S27b, S35a→S35b, S36a→S36b) are hard
cuts — continuous coverage, not separate scenes. Frame-chained clips already share continuity from the
last-frame handoff; a hard cut is invisible there.

| Between | Transition | Duration | Notes |
|---------|------------|----------|-------|
| S37 → S38 → (end) | **Fade to Black** | 2–3s | Final shot only — grain lightens into dawn, then black |

**Light Leak count: 0 — deliberate.** The skill permits up to 3 warm-amber light-leak transitions on
chorus entries, but EP09 is governed by the **Amber Pulse discipline: exactly ONE amber moment per
episode (S07, which fails).** Warmth after S27 returns as **gold, achieved in-clip** (core-glow), never
as a transition effect. Adding amber leaks would break the single-amber signature and cheapen the gold
turn. Chorus entries (S14, S23, S29) therefore land on **hard cuts** — the cut itself is the punctuation.

**FORBIDDEN:** glitch, zoom, spin, slide, wipe, swipe, shape presets. None used.

---

## 7. EFFECT SETTINGS (Adjustment Layer, full timeline)

Apply in this exact order — order matters.

| # | Effect | Value | CapCut Path |
|---|--------|-------|-------------|
| 1 | Kodachrome LUT | `Kodachrome 64.cube` @ 80–100% | Filters → Custom → Import |
| 2 | Color Match | Reference = **S07 (7.mp4)** | Select ref clip → Match (see §9 caveat) |
| 3 | Film Grain | **10–15%** (push toward 15% in the Grain Crescendo, S19–S23) | Filters → Vintage → Film Grain |
| 4 | Vignette | Subtle **15–25%** | Effects → Vignette |
| 5 | Letterbox 2.35:1 | Custom ratio | Player → Ratio → Customized → 2.35:1 |

> **Rationale:** LUT sets the color base → Color Match unifies tool differences on top → Grain adds
> texture over color → Vignette pulls spatial focus → Letterbox is the final framing crop.

---

## 8. SELECTIVE EFFECTS MAP (per-clip only, NOT global)

| Clip | Shot | Effect | Setting | Timing |
|------|------|--------|---------|--------|
| 22.mp4 | S22 | Chromatic Aberration | Subtle "Shift Channels" RGB split | On reboot strobe, 1–2s |
| 23.mp4 | S23 | Chromatic Aberration | Subtle RGB split | On "I AM THE BUG" blaze, 1–2s |
| 14.mp4 | S14 | Chromatic Aberration (light) | Very subtle | On shadow-inversion beat, ~1s |

**Manual grain crescendo (S19→S23):** ramp the per-clip grain slightly *above* the 15% baseline across
these five shots, then **invert at S38** — lighten grain to near-clean as the dawn opens (motion-script
signature). This is a hand-keyed override on top of the global grain, not a preset.

**Shadow compositing (S12–S24):** the shadow's autonomous behaviour (leading in S14–S15, thrashing in
S22–S23, deflating in S24) is **hard-light keyframe compositing in CapCut**, per the motion script's
Shadow Compositing Protocol — it is NOT in the source clips. Build it on a separate overlay layer.

**FORBIDDEN selective:** neon glow, digital glitch, motion-blur presets, speed-zoom, full-clip VHS.

---

## 9. COLOR REFERENCE

- **Reference clip: S07 (7.mp4)** — the mechanic under the warm amber work lamp against oil-dark walls.
  It carries the truest Kodachrome warmth (warm amber highlights + rich shadow) without being fully gold.
- **⚠️ Preserve the color journey — do NOT flatten it.** EP09's palette deliberately travels
  **cold grey (S01–S05 exterior / S08 command-bridge blue) → warm workshop → gold kintsugi (S27+).**
  Use Color Match to unify *tool-to-tool* inconsistency, but do **not** let it warm the cold exterior and
  flashback scenes into the workshop palette. Match loosely on S01–S05 and S08; match fully from S06 on.
- **Tool-specific corrections:**
  - Kling clips run slightly cool → nudge warmth via HSL (orange/amber +5–10%) where the scene is warm.
  - Seedance clip (S38) usually sits well on the LUT alone — check the dawn sky isn't over-saturated.

---

## 10. EXPORT SETTINGS

> **Do not export until `36b.mp4` and `37.mp4` are rendered and placed.**

| Setting | Value |
|---------|-------|
| Resolution | 1080p (1920×1080) |
| Frame Rate | 24fps |
| Codec | H.265 (HEVC) |
| Bitrate | 35–60 Mbps |
| Format | MP4 |
| Watermark | None (CapCut Pro) |
| Output | `episode-09/06_edit/ep09_final_v01.mp4` |

**Incremental saves:** save the CapCut project after Phase 2 (assembly), after Phase 6 (global effects),
and before export.

---

## 11. QA CHECKLIST (pre-export)

- [ ] Both pending clips rendered & placed (36b.mp4, 37.mp4)
- [ ] Every shot has its clip on the timeline (41 total)
- [ ] No timeline gaps — total = 423s (±1s)
- [ ] All 13 speed ramps match the table exactly
- [ ] All 15 beat-sync anchors verified frame-level
- [ ] Transitions: hard cut default + one fade-to-black (S38 only); zero light leaks (Amber discipline)
- [ ] Chromatic aberration on S22 / S23 / S14 only
- [ ] Effect order: LUT → Color Match → Film Grain → Vignette → Letterbox
- [ ] Film grain 10–15% (crescendo S19–S23, invert to near-clean S38)
- [ ] Letterbox 2.35:1 applied
- [ ] Color journey preserved (cold → warm → gold NOT flattened)
- [ ] Shadow compositing built on overlay layer (S12–S24)
- [ ] Amber Pulse intact at S07 only; no other warm-amber moment
- [ ] Eye canon: calm steady blue lenses (S03, S25, S33) — not glowing eyeballs
- [ ] Phase transition reads clean at S27 (@Damaged → @Kintsugi)
- [ ] Export: 1080p, H.265, 35–60 Mbps, 24fps
- [ ] No forbidden effects anywhere
- [ ] **Sync-QC record filled** → `ep09_sync_qc_v01.md` (min 5 timestamped spot-checks) after export
- [ ] "Would Fibula approve this?"

---

## POST-EXPORT — MANDATORY SYNC-QC RECORD

From EP09 onward the edit is **not "done"** without a committed sync-QC record. After the render exists:

1. Copy `_templates/ep_sync_qc_template.md` → `episode-09/06_edit/ep09_sync_qc_v01.md`.
2. Fill **≥ 5 timestamped spot-checks** sourced from §5 above (recommend #9, #10, #11, #13, #15).
3. For each: compare target timestamp to the actual cut, verdict **ON-BEAT** (|Δ| ≤ 150ms),
   **OFF by N ms**, or **ACCEPTED-DEVIATION** (deliberate offset + one-line reason).
4. `scripts/sync_probe.py` is an optional local helper that prints measured cut-vs-boundary numbers.

The final render is gitignored (Drive), so this committed record is the beat-sync evidence CI cannot produce.

---

*"The edit is where the vision meets the frame. Every cut is a breath, every transition a heartbeat.
Make it invisible — the best edit is the one the viewer never notices."*
*— Robotiko v2.0 Pipeline*
