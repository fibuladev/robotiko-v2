# TODO — ACTIVE TASKS
> Current open tasks and priorities.
> Claude updates this file during and after each session.
> Last Updated: 2026-03-01 (Session 6: Multiframes Killed + Pipeline Cleanup)

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
- [ ] `ep03_musical_metadata.json`
- [ ] `ep04_musical_metadata.json`
- [ ] `ep05_musical_metadata.json`
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