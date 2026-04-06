# TODO — ACTIVE TASKS
> Current open tasks and priorities.
> Claude updates this file during and after each session.
> Last Updated: 2026-03-31 (EP05 Dramaturgy Planning + Concept Notes)

---

## CURRENT PRIORITY: INFRASTRUCTURE COMPLETION
> Target: Complete before Claude Code activation (2026-02-23)

### ✅ COMPLETED TODAY
- [x] `master.md` — Universe Bible v2.0 written
- [x] `pipeline_rules.md` — v2.0 written
- [x] `naming_convention.md` — v2.0 written
- [x] `architecture.md` — v2.0 written
- [x] `project_metadata.json` — v2.0 written, all 10 episodes
- [x] `character_profiles.json` — v2.0 with Robochica, phase visual states
- [x] `dramaturgy_template.md` — v2.0 written
- [x] `visual_prompt_template.md` — v2.0 written
- [x] `video_prompt_template.md` — v2.0 written
- [x] `.gitignore` — expanded with raw folders and secrets
- [x] `CLAUDE.md` — Claude Code session context written
- [x] `_memory/lessons.md` — Self-improvement loop initialized
- [x] `_memory/decisions_log.md` — Foundation decisions logged
- [x] `_memory/todo.md` — This file

### ✅ COMPLETED (2026-02-23 Session)
- [x] `docs/` skeleton — getting-started, skills-guide, tools-setup
- [x] `CHANGELOG.md` — repo root
- [x] `.github/ISSUE_TEMPLATE/` — bug report + feature request templates
- [x] `.github/pull_request_template.md`
- [x] `CONTRIBUTING.md` skeleton

### ✅ COMPLETED (2026-02-24 Session)
- [x] `_skills/robotiko-dramaturgy/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-visual-prompts/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-motion-script/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-episode-scaffold/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-naming-enforcer/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-youtube-packager/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-reels-atomizer/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-launch-orchestrator/SKILL.md` — v1.0 written

### ✅ COMPLETED (2026-02-25 Session)
- [x] Full repo audit (DevOps + Claude capabilities — dual-angle review)
- [x] P0 fix: `project_metadata.json` skills status updated to `all_skills_v1.0_complete`
- [x] P0 fix: `pipeline_rules.md` added to CLAUDE.md mandatory reads (item #5)
- [x] P0 fix: Extended Thinking Protocol added to CLAUDE.md (workflow rule #7)
- [x] `tests/naming_check.py` — v1.0 implemented (full validation logic)
- [x] `tests/visual_prompt_validator.py` — v1.0 implemented (suffix, character phase, forbidden aesthetics)
- [x] `tests/naming_check_hook.py` — v1.0 implemented (lightweight hook for Claude Code)
- [x] `.claude/settings.json` — PostToolUse hook configured (bash-based, no Python dependency)
- [x] `MEMORY.md` — Auto-memory file created for session continuity
- [x] `tests/README.md` — Updated to reflect v1.0 implementations

---

## NEXT: EP02 PRODUCTION
> Unblock after infrastructure is complete

- [x] `ep02_concept_notes.md` — Concept notes written (must-have shots, overrides, mood)
- [x] `ep02_musical_metadata.json` — Musical metadata added to episode-02/02_music/
- [x] `ep02_lyrics_v01.md` — Lyrics added to episode-02/01_lyrics/
- [x] `ep02_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-02-26
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-02-26
- [x] `ep02_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-02-26
- [x] Image generation — Nano Banana ✅
- [x] Human selects images ✅ (41 selected images including 6 keyframe pairs)
- [x] `ep02_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script) ✅ 2026-02-27
- [x] **[PIPELINE FIX]** Duration Coverage Strategy — architecture-level fix across 7 files ✅ 2026-02-27
- [x] `ep02_motion_script_v02.md` — Full rewrite with duration coverage (49 clips, 100.4% coverage) ✅ 2026-02-27
- [x] **[CHECKPOINT]** Human approves motion script v02 ✅ 2026-02-28
- [x] Tool Assignment Plan — 49 clips assigned: Kling=36, Veo=4, Seedream=9 ✅ 2026-02-28
- [x] `ep02_motion_script_v02.md` — Updated with `| Recommended Tool |` field per clip + Tool Assignment Summary section ✅ 2026-02-28
- [x] Pipeline update: Seedream → Seedance 1.0 + Multiframes (SKILL.md v1.2, template v5.0, pipeline v2.2) ✅ 2026-03-01
- [x] **EP02 Seedance Test Protocol** — Multiframes tested: **FAIL** (1130cr / 2 tests, budget-destroying) ✅ 2026-03-01
  - [ ] Test 1: S04 — Seedance 1.0 vs Kling (Mode A quality comparison)
  - [ ] Test 2: S11 — Seedance 1.0 vs Kling (Mode B keyframe comparison)
  - [x] Test 3: S14(a+b+c) — Multiframes vs 3 individual clips — **KILLED** (~565cr/generation) ✅ 2026-03-01
  - [ ] Test 4: S08 — Seedance 1.0 map shot (1080p vs former 720p plan)
- [x] Post-test decision: **No Multiframes** — removed from pipeline entirely ✅ 2026-03-01
- [ ] EP02 tool reassignment (Seedance 1.0 tests 1/2/4 still pending)
- [ ] Human generates 2 supplementary images (S29c, S34b) from inline prompts
- [ ] Video generation — per updated tool assignment
- [ ] Human selects video clips
- [ ] Final edit — CapCut

### 2026-03-18 Session Summary (CapCut Post-Production Setup)
**Task:** Set up CapCut Desktop post-production pipeline for EP02.
**Completed:**
- [x] Kodachrome LUT imported (Presetpro - Kodachrome 64.cube) → Adjustment Layer, intensity 80%
- [x] Film Grain effect added (Effects → "Grain") → Adjustment Layer, texture 10
- [x] Letterbox 2.35:1 activated (Player → Ratio → 2.35)
- [x] All video clips + music (episode-2.1.wav) imported to timeline
**Pending for tomorrow (2026-03-19):**
- [ ] Audio-video sync — align clip boundaries to musical beats using motion script timestamps
- [ ] S01 re-generation via Veo (original was 5s, needs 8s+ for speed ramp coverage)
- [ ] Vignette effect (Effects → "Vignette" → ~20%)
- [ ] Selective effects (chromatic aberration on S07, S11, S23, S28, S32)
- [ ] Speed ramp adjustments on applicable clips (S01-S03, S13, S15, S16, etc.)

### 2026-02-27 Session Summary (Duration Coverage Fix)
**Problem:** Motion script v01 had 39% duration coverage (175s video for 448s music). Pipeline assumed 1 scene = 1 clip.
**Solution:** Created Duration Coverage Strategy (Direct / Speed Ramp / Multi-Clip). Updated 7 pipeline files + rewrote motion script.
**Files updated:** pipeline_rules.md, motion-script SKILL.md, visual-prompts SKILL.md, video_prompt_template.md (v3.0), naming_convention.md, lessons.md
**Deliverable:** ep02_motion_script_v02.md — 49 clips, 450s generated, 100.4% coverage, 2 supplementary images needed (S29c, S34b)

### 2026-02-28 Session Summary (Tool Assignment Plan)
**Task:** Assign AI video generation tool to each of 49 clips based on tool capabilities, credit budgets, and quality requirements.
**Tool inventory:** Kling AI Pro (3000 cr, 1080p, keyframe), Google Veo (free, 8s fixed, no keyframe), Seedream 1.5 Pro (1200 cr, 720p, keyframe)
**Assignment strategy:** Mode B → Kling only (6 clips). Map shots → Seedream (9 clips, 720p OK on textures). 8s scene match → Veo (4 clips). Everything else → Kling (30 clips).
**Credit budget:** Kling 2,275/3,000 (725 buffer). Seedream ~540/1,200 (660 buffer). Veo free.
**Files updated:** ep02_motion_script_v02.md (added Tool Assignment Summary + Recommended Tool per clip), _memory/todo.md
**Next steps:** Generate 2 supplementary images (S29c, S34b), then begin video production per tool assignment.

### 2026-02-28 Session 4 Summary (Tool Assignment Pipeline Integration)
**Task:** Make tool assignment logic permanent across pipeline — not just EP02-specific.
**Files updated:** robotiko-motion-script/SKILL.md (v1.1: Step 7 + Output Format + Checklist), video_prompt_template.md (v4.0: Tool Assignment Summary + Recommended Tool fields), pipeline_rules.md (v2.1: Step 8c + Step 9 update)
**Result:** EP03+ motion scripts will automatically include tool assignments as standard output.

### 2026-03-01 Session 5 Summary (Seedance Integration + Multiframes Discovery)
**Discovery:** Human found Seedance 1.0 (CapCut built-in, 1080p, keyframe, 25cr/5s, 50cr/10s) as Seedream 1.5 Pro replacement + Seedance Multiframes (up to 10 keyframes, up to 54s continuous video, AI interpolation).
**Pipeline update:** Seedream → Seedance 1.0 across all pipeline files. Multiframes added as experimental Mode C.
**Files updated:** SKILL.md (v1.2), video_prompt_template.md (v5.0), pipeline_rules.md (v2.2), project_metadata.json
**Strategy:** Test-first approach — 4 EP02 test clips before reassignment decision (S04, S11, S14, S08).
**Commits pending:** Previous session's tool assignment integration + this session's Seedance update.

### 2026-03-01 Session 6 Summary (Multiframes Killed + Pipeline Cleanup)
**Test result:** Multiframes consumed ~565 credits per generation (1130cr for 2 tests). Monthly CapCut Pro budget is 1200cr — 2 tests nearly exhausted it.
**Decision:** Multiframes permanently removed from pipeline. Seedance 1.0 stays as a viable tool alongside Kling + Veo.
**Files updated:** SKILL.md (v1.3), pipeline_rules.md (v2.3), video_prompt_template.md (v5.1), project_metadata.json, lessons.md, MEMORY.md
**Remaining tests:** Seedance 1.0 single-clip tests (S04 Mode A, S11 Mode B, S08 map shot) still pending.
**Commits pending:** Session 4 + 5 + 6 combined.

---

## NEXT: EP03 PRODUCTION

- [x] `ep03_lyrics_v01.md` — Lyrics added to episode-03/01_lyrics/
- [x] `ep03_musical_metadata.json` — Musical metadata added to episode-03/02_music/
- [x] `ep03_concept_notes.md` — Concept notes written (brainstorming session 2026-03-07)
- [x] `ep03_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-03-10
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-03-10
- [ ] `ep03_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts)
- [ ] Image generation
- [ ] Human selects images
- [ ] `ep03_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script)
- [ ] **[CHECKPOINT]** Human approves motion script
- [ ] Video generation
- [ ] Final edit — CapCut

### 2026-03-07 Session Summary (EP03 Brainstorming + Concept Notes)
**Task:** Brainstorm creative direction for EP03 dramaturgy before writing.
**Key decisions:** Spoken intro = Mentor-Robotiko argument in house + model selection screen (anti-guru thesis). Sol-liberal group only in intro+V1. Locations: East=village wedding, North=Trabzon road rage, South=Alanya nightclub scam, Istanbul=miniature bridge + metrobus. Finale=sanayi sitesi kaynakci with grease IV. Mentor in chorus=amber light presence only. EP02 ear damage carries, no new permanent damage. Instrumental breaks=transition montages.
**Deliverable:** `episode-03/03_direction/ep03_concept_notes.md` — complete with all must-have shots, creative overrides, mood notes.
**Next step:** Create dramaturgy v01 in a new session.

### 2026-03-10 Session Summary (EP03 Dramaturgy v01)
**Task:** Generate EP03 dramaturgy scene breakdown from approved concept notes + musical metadata.
**Deliverable:** `episode-03/03_direction/ep03_dramaturgy_v01.md` — 40 scenes, 8:44 (524s), full coverage.
**Key structure:** 5 spoken intro scenes (argument + model screen), 6 geographic trial locations (city/east/north/south/cinci hoca/Istanbul), 5 finale scenes (sanayi sitesi + grease IV). Mentor hybrid presence (physical bookends, amber atmospheric in choruses). Sol-liberal group intro+V1 only.
**Flagged for review:** S04 text legibility, S23 receipt comedy balance, S33-S34 miniature bridge, S38 two-plane composition.
**Next step:** Human reviews and approves dramaturgy → then visual prompts in a new session.

### 2026-03-10 Session 2 Summary (EP03 Dramaturgy Review + Approval)
**Task:** Human review of EP03 dramaturgy v01 — corrections and approval.
**Corrections applied:** (1) S01: "Anatolian house" → "modest house, their shared home" (they haven't traveled yet). (2) S23: receipt river removed, rewritten as tout-to-nightclub transition scene. (3) S26: receipt river + MIB consolidated here (V4a lyrics). (4) S24: stale "receipt in hand" reference removed. (5) Robotiko Visual State: "pristine" → EP02 cumulative damage (missing ear, torso dent, shoulder scratches). (6) Director's Notes: "pristine everywhere except ear" corrected.
**Infrastructure updates:** `character_profiles.json` Phase 1 visual_prompt_addition split into `ep01` (pristine) and `ep02_ep03` (battle-scarred). Lesson added to `lessons.md`: cumulative damage rule.
**Production estimate:** ~50-52 video clips for 524s coverage (similar ratio to EP02's 49/448s).
**Status:** Dramaturgy APPROVED ✅. Ready for visual prompts in a new session.
**Next step:** `ep03_visual_prompts_v01.md` — generate in new session (skill: robotiko-visual-prompts).

---

## NEXT: EP04 PRODUCTION

- [x] `ep04_lyrics_v01.md` — Lyrics added to episode-04/01_lyrics/
- [x] `ep04_musical_metadata.json` — Musical metadata added to episode-04/02_music/
- [x] `ep04_concept_notes.md` — Concept notes written
- [x] `ep04_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-03-22
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-03-23
- [x] `ep04_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-03-23
- [x] Image generation ✅ (54 images in raw/, all reviewed)
- [x] Human selects images ✅ (images reviewed, to be moved from raw/ to selected/)
- [x] `ep04_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script) ✅ 2026-03-29
- [x] **[CHECKPOINT]** Human approves motion script ✅ 2026-03-31 (17 videos generated, quality confirmed)
- [ ] Video generation (remaining clips)
- [ ] Final edit — CapCut

### 2026-03-22 Session Summary (EP04 Dramaturgy v01)
**Task:** Generate EP04 dramaturgy scene breakdown from approved concept notes + musical metadata.
**Deliverable:** `episode-04/03_direction/ep04_dramaturgy_v01.md` — 44 scenes, 7:03 (423s), full coverage.
**Key structure:** 3-act structure (Return & Testimony / Cosmic Journey & Sacred Law / Temptation, Hammer & Awakening). Robotiko fully passive — only movement is final head-lift (S44). Mentor as sole protagonist. Historical montage across 4 eras (S16-S19) with Young Mentor aging. S20 = Piercing the Veil / Kindred Souls (aydınlanmış figürler, amber gözler — gönül gözü açık). S21 = Film-within-film (iç içe çerçevelerde aldatan/aldatılan döngüsü, S16-S19 yankıları, Mentor tek uyanık figür). Moon/Sun transformation (S22-S23) with staff materialization. Devil = black smoke + spiral horns (S27-S29). Hammer scene (S31-S34): real, heavy, amber glow only at swing. Second tea glass as emotional anchor (6 appearances). Amber = truth color DNA (staff → Kindred Souls' eyes → Sun → TRUTH → hammer → eyes).
**Flagged for review:** S04 tea glass detail, S16-S19 Young Mentor consistency, S20 Kindred Souls amber eyes + reference image, S21 nested frames readability, S23 Sun transformation, S27-S28 smoke+horns, S34 ego shatter, S44 eye color change.
**Next step:** Human reviews and approves dramaturgy → then visual prompts in a new session.

### 2026-03-23 Session Summary (EP04 Visual Prompts v01)
**Task:** Generate EP04 visual prompts from approved dramaturgy (44 scenes).
**Deliverable:** `episode-04/04_visuals/ep04_visual_prompts_v01.md` — 48 prompts (44 scenes, 4 keyframe pairs: S03, S30, S34, S44) + 4 reference images.
**Reference images created:** (1) REF-ENV-01: Mentor's Room interior, (2) REF-CHAR-01: Young Mentor (clean-shaven, for vision sequences), (3) REF-CHAR-02: Kindred Souls (dervish, philosopher, healer, sage with amber eyes), (4) REF-ENV-02: Sunlit Moon Surface.
**Key tracking:** Young Mentor aging across S16-S34 (clean-shaven → stubble → thin beard → fuller beard → middle-aged). Staff chronology correct (no staff in visions S16-S33, born at S34, present in room S35+). Amber DNA maintained throughout. Devil = smoke + horns only. Robotiko passive (Phase 2: rusted, cracked, sparking, glitching). Only movement = S44 head-lift.
**Validation:** 52 prompts with suffix ✅, 52 with 16:9 ✅, no "pristine" in prompts ✅, no character names in prompts ✅.
**Next step:** Human generates reference images first → then scene images in Nano Banana → select → motion script in new session.

### 2026-03-29 Session Summary (EP04 Motion Script v01)
**Task:** Generate EP04 motion script from approved dramaturgy (44 scenes) + selected images (54 in raw/).
**Deliverable:** `episode-04/05_video/ep04_motion_script_v01.md` — 45 clips (44 scenes + 1 multi-clip sub-clip for S37).
**Coverage:** 405s generated / 423s music = 95.7%. 18 Speed Ramp clips, 1 Multi-Clip (S37: 2 sub-clips), 4 Mode B (S03, S30, S34, S44).
**Tool assignment:** Kling 25 clips (~1575cr est., 47.5% buffer), Seedance 20 clips (850cr, 29.2% buffer). No Veo.
**Key decisions:** (1) Average MS ~4.0 — lower than Destruction norm, justified by 56 BPM meditative tone. (2) S32-S33-S34 triple peak (MS 7-8-8) justified as climax. (3) S36/S39 share S35's image (visual prompt merges). (4) S37a/S37b share S37's image (different camera moves). (5) 0 supplementary images needed.
**Post-gen validation:** 45 video suffixes ✅, 45 anti-spawn guards ✅, 45 camera moves ✅, no character names in motion prompts ✅, coverage ≥95% ✅.
**Next step:** Human reviews and approves motion script → then video generation begins.

---

## NEXT: EP05 PRODUCTION

- [x] `ep05_lyrics_v01.md` — Lyrics complete
- [x] `ep05_musical_metadata.json` — Musical metadata complete
- [x] `ep05_concept_notes.md` — Concept notes written ✅ 2026-03-31
- [x] `character_profiles.json` — Robochica visual design finalized ✅ 2026-03-31
- [ ] Robochica master reference image (`ref_robochica_master.png`) — Generate + human approve
- [ ] Environment reference images (retro-futuristic supermarket, office, café, street) — Generate + human approve
- [x] `ep05_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-03-31 (32 scenes, 267s, 100% coverage)
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-03-31
- [x] `ep05_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-04-02 (41 prompts: 8 ref + 33 scene)
- [x] Image generation ✅ 2026-04-02 (33 scene images + 8 reference images generated in Nano Banana)
- [x] Human selects images ✅ 2026-04-02 (all reviewed and approved)
- [ ] `ep05_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script)
- [ ] **[CHECKPOINT]** Human approves motion script
- [ ] Video generation
- [ ] Final edit — CapCut

### 2026-04-02 Session Summary (EP05 Visual Prompts + Image Generation)
**Task:** Generate EP05 visual prompts and all scene images.
**Deliverable:** `episode-05/04_visuals/ep05_visual_prompts_v01.md` — 41 prompts (8 reference + 33 scene, including S15a/S15b keyframe split).
**Reference images:** REF-CHAR-01 (Robochica — 3 iterations, dark amber glass lens eyes fix), REF-CHAR-02 (Elderly Robot Couple), REF-ENV-01-06 (Supermarket, Street, Cafe, Office, Iron Vault, Room).
**Key fixes during production:** (1) Robochica eyes: "amber glow" → "dark amber glass lenses" (3 attempts, final working formula). (2) Cathedral → "colossal iron vault" (no religious connotation). (3) Office: narrow corridor → wide plaza floor. (4) robochica_1 tattoo: chest → inner forearm (clean surface, EP06 _2/_3/_4 preparation). (5) Cem Karaca poster: originally planned as post-production composite, ABANDONED 2026-04-06 — all AI tools refused compositing, plan pivoted to YouTube description + outro credit card.
**All 8 human overrides implemented:** S05 (both in frame), S07 (drool), S11 (elderly couple), S13 (forearm tattoo), S15a/b (hacker mask + cloud), S22-S23 (folders), S24 (red body), S28 (eye projection).
**Image review:** 33/33 approved. 0 critical issues. 4 minor CapCut post-production adjustments noted.
**Next step:** Motion script in new session.

### 2026-03-31 Session Summary (EP05 Dramaturgy Planning + Concept Notes)
**Task:** Plan EP05 dramaturgy — "First Love / Blue Screen" (highest viral potential episode).
**Key decisions:** (1) Robochica: amber/gold eyes (EP04 truth-color irony), warm gold/copper wires, fractal shoulder pattern, mirror principle (max 3 face-on shots). (2) Locations: multiple retro-futuristic everyday (market, office, street, café) — each encounter closer. Syd Mead aesthetic. (3) Mentor: amber echoes ONLY, no image. (4) Tonal shift: pure surprise at 3:24, zero dark hints before.
**Human overrides (8):** (1) Both in frame for "walk so slow" (2) Drool effect for "twin reactors" (3) Elderly robot couple for "dead father" line (4) robochica_1 tattoo → seeds EP06's _2,_3,_4 (5) Hacker mask + physical cloud with data center (6) Windows folders thrown aside (7) Bright red overheating body (8) Eye projection EP03 callback in outro.
**Deliverables:** `character_profiles.json` updated (Robochica design complete), `ep05_concept_notes.md` written (full creative direction + 8 human overrides + 12 creative rules).
**Next step:** Generate dramaturgy v01 (this session or next).

---

## BACKLOG

### Skills (Content to Write)
- [x] `_skills/robotiko-dramaturgy/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-visual-prompts/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-motion-script/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-episode-scaffold/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-naming-enforcer/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-youtube-packager/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-reels-atomizer/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-launch-orchestrator/SKILL.md` — ✅ v1.0 complete

### EP01 Retroactive
- [ ] `ep01_musical_metadata.json` — Retroactive documentation
- [ ] `ep01_dramaturgy_v01.md` — Retroactive documentation
- [ ] `ep01_concept_notes.md` — Retroactive documentation

### MCP Integration (EP03-04 Phase)
- [ ] GitHub MCP setup
- [ ] Filesystem MCP setup
- [ ] Test MCP workflow on EP03

### EP03-10 Timestamp JSONs
- [x] `ep03_musical_metadata.json` — completed
- [x] `ep04_musical_metadata.json` — completed
- [x] `ep05_musical_metadata.json` — completed
- [ ] `ep06_musical_metadata.json`
- [ ] `ep07_musical_metadata.json`
- [ ] `ep08_musical_metadata.json`
- [ ] `ep09_musical_metadata.json`

### Open Source Release (Post EP10)
- [ ] `CONTRIBUTING.md` — Full version
- [ ] `docs/` — Full documentation
- [ ] Final review of all management files
- [ ] Public announcement

---

*Update this file at the start and end of every session.*