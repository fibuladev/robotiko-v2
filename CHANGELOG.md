# CHANGELOG
> All notable changes to ROBOTIKO v2.0 are documented here.
> Format: [VERSION] — DATE — Description
> Note: 0.3.x point releases were assigned by scope, not chronology, so version order does not always track date order.

---

## [1.0.0] — TBD (target 2026-08-04) — Open Source Release (EP10 Release Day)

> **Status: PREPARED — not yet released.** The public release ships on EP10 release day,
> when the repository goes public.

A complete, reproducible, open-source methodology for LLM-directed music cinema — a ten-episode
closed arc produced by a git repository operating as a one-person film studio, with Claude as a
stage-gated production crew and the human retaining two irreplaceable roles: creative vision
(inputs) and taste (the three approval checkpoints).

### Ships in 1.0.0
- **The method is reproducible from the repo; the films are not — renders live outside the tree:**
  - `master.md` — Universe Canon (constitution / policy-as-code: golden rules, mandatory suffixes).
  - 10 production skills in `_skills/` — musical-metadata, dramaturgy, visual-prompts, motion-script,
    episode-scaffold, naming-enforcer, youtube-packager, reels-atomizer, launch-orchestrator, capcut-editor.
  - `_memory/lessons.md` — ~125 dated, tested generative-film-grammar rules (a self-improving knowledge base).
  - `_memory/decisions_log.md` — architectural decision records.
  - `character_profiles.json` + `project_metadata.json` — explicit multi-episode character state machine
    (cumulative damage tracked and enforced across all episodes).
  - `_templates/` — dramaturgy, visual-prompt, video-prompt templates.
- **Enforcement / CI layer:** `tests/naming_check.py`, `tests/pipeline_integrity.py`,
  `tests/visual_prompt_validator.py`, Claude Code PostToolUse naming hook (later removed 2026-07-04),
  GitHub Actions scaffold.
- **Tooling:** custom-built Google Drive MCP server (`_tools/mcp-gdrive/`, no third-party packages),
  Python episode-scaffold scripts.
- **Dual license:**
  - `LICENSE` — **MIT** for the method (pipeline, skills, scripts, templates, docs).
  - `LICENSE-CONTENT` — **CC BY-NC 4.0** for the creative content (lyrics, dramaturgy, visuals, audio).
- **Authorship & docs:** `AUTHOR.md` (creator Can Yalcin, channel Fibula), completed `docs/`
  (getting-started, skills-guide, tools-setup, anatomy-of-an-episode), CONTRIBUTING.md.
- **10 episodes** documented end-to-end; EP01–EP10 published on YouTube.

---

## [0.9.0] — 2026-06-11 — Open Source Readiness Pass (Golden Release Prep)

### Added
- `LICENSE` — MIT, covering the method (pipeline, skills, scripts, templates, docs).
- `LICENSE-CONTENT` — CC BY-NC 4.0, covering the creative content (lyrics, dramaturgy, visuals, audio).
- `AUTHOR.md` — repo root; creator identity (Can Yalcin) and channel (Fibula).
- `_management/golden_release_report.md` — multi-role golden-release audit (FDE / architect / DevOps /
  art director / dramaturg) with web-researched market comparison, novelty verdict, and P0/P1/P2 roadmap.
- `docs/anatomy-of-an-episode.md` — one episode traced end-to-end as the showcase artifact.
- `episode-09/` + `episode-10/` scaffolded; `ep09_lyrics_v01.md` committed (canonical creative input now in git).

### Changed
- **Status is now single-source-of-truth.** `project_metadata.json` is the authoritative status tracker;
  `master.md` and `CLAUDE.md` point to it instead of duplicating stale episode tables.
- `_management/architecture.md` — v2.1: AWS S3 → Google Drive + custom MCP; current toolchain
  (Kling 3.0 / Elements / Omni, Seedance 1.0); Claude Code hooks.
- Root `README.md` — golden pass; storage and tooling references corrected.
- Corrected the stale video-tool name to `Seedance` across naming-enforcer SKILL, `architecture.md`,
  setup script, `docs/getting-started.md`, and `tests/naming_check.py` regex.
- `_management/README.md` — removed a forbidden legacy source-file reference; file list brought current.

### Removed / Separated
- Private files separated from the public tree (local playbook and personal system-maintenance
  utilities gitignored); secrets/PII sweep across `_tools/` and committed JSON.

### Notes
- Planned for golden quality (P1): CI workflow running the naming + pipeline-integrity tests on push/PR.

---

## [0.8.0] — 2026-06-04 — EP08 Direction & Motion Script

### Added
- `episode-08/03_direction/ep08_concept_notes.md` — "40 Days Offline" (The Contented Self). APPROVED.
- `episode-08/03_direction/ep08_dramaturgy_v01.md` — 33 scenes, 500s, 87 BPM, C Minor, 12 human overrides,
  Witnessing Camera personality. APPROVED.
- `episode-08/04_visuals/ep08_visual_prompts_v01.md` — 33 scene prompts + 4 environment references.
- `episode-08/05_video/ep08_motion_script_v01.md` — 48 clips, 96% raw coverage, 100% effective.

### Notes
- Body stays @Damaged for the whole episode (inner/consciousness transformation only); visible
  reconstruction (gold-filled cracks) deferred to EP09 — a two-beat payoff structure.
- Pipeline caught a critical continuity error: the pristine master reference was corrected to the
  damaged-android set for all @Damaged scenes.

---

## [0.7.0] — 2026-05-30 — EP07 Direction & Production (Art-House Short-Film Pivot)

### Added
- `episode-07/` full direction: lyrics, musical metadata (25 sections, 439s, 73 BPM, E Minor),
  concept notes (APPROVED), dramaturgy (29 scenes, Retreating Camera spine, APPROVED).
- `episode-07/04_visuals/ep07_visual_prompts_v01.md` — 29 scene prompts.
- `episode-07/05_video/ep07_motion_script_v01.md` — 49 clips, Retreating Camera, first Kling 3.0
  @Damaged Element test.
- `episode-07/06_edit/ep07_capcut_guide_v01.md` — CapCut editing guide (48 clips, grain crescendo).

### Notes
- EP07 is the series turning point: "music video" → art-house short film treatment inherited by EP08–10.
- Locked cinematic choices: wet-grey aftermath, dual anchoring device (wet reflections vs. cold
  eye-projection), amber starvation with one received ember (Moon/Sun), 5× refrain distance ladder.

---

## [0.6.0] — 2026-06-03 — Motion Script SKILL v2.0 & EP06 Complete

### Added
- `_skills/robotiko-capcut-editor/SKILL.md` — CapCut editing-guide skill (10th and final skill).
- `_skills/robotiko-musical-metadata/SKILL.md` — custom Claude skill replacing the former Gemini tool
  (keeps the whole pipeline in-repo). **All 10 skills now complete.**
- `episode-06/` full production: dramaturgy (43 scenes, 451s, 134 BPM, B Minor), visual prompts (v01 + v02
  radical simplification for reference-image compatibility), motion script (45 clips, 98.7% coverage),
  CapCut guide.

### Changed
- `_skills/robotiko-motion-script/SKILL.md` — **v2.0**: Art Direction Pillars (5 principles + visual
  signatures), Kling 3.0 Elements (registry, Angles 2.0), Frame Chaining protocol, OmniEdit protocol,
  Camera Diversity Rule (no move type >30%, 5-clip variety, accent budget), Episode Camera Personalities
  (EP07 Retreating / EP08 Witnessing / EP09 Discovering / EP10 Companion).
- `_memory/lessons.md` — +10 camera-diversity and art-direction rules; 2.35:1 letterbox confirmed.
- `_management/pipeline_rules.md` — Step 8 updated for the v2.0 motion-script output.

---

## [0.5.0] — 2026-05-22 — YouTube Strategy v2.0

### Changed
- `_skills/robotiko-youtube-packager/SKILL.md` — **v4.0**: "Cinematic AI Series" title format,
  film-first tags, new description template, new hashtags. EP01–EP03 packages retrofitted.
- YouTube strategy overhaul: Film & Animation recategorization, no mixed playlists with competitors,
  film-first metadata standards across all episodes.

### Notes
- EP01–EP07 launched on YouTube (channel @fibuladev): EP01 (Apr 22), EP02 (May 1), EP03 (May 13),
  EP04 (May 19), EP05, EP06, EP07. (Launch dates recorded retroactively, through June 2026.)

---

## [0.4.0] — 2026-03-31 — EP03–EP05 Production & Robochica Design

### Added
- `episode-03/` production: concept notes, dramaturgy (40 scenes, 524s — the Anatolian Trials crucible).
- `episode-04/` production: dramaturgy (44 scenes, 423s), visual prompts (48 prompts + 4 reference images),
  motion script (45 clips, 95.7% coverage). Amber = truth-color DNA throughout.
- `episode-05/` production: concept notes, dramaturgy (32 scenes, 267s, 100% coverage), visual prompts
  (41 prompts), motion script (32 clips), CapCut guide. "First Love / Blue Screen."

### Changed
- `_assets/cast/character_profiles.json` — Robochica visual design finalized (dark amber glass lens eyes,
  gold/copper wires, fractal shoulder pattern); Phase 1 split into `ep01` (pristine) vs. `ep02_ep03`
  (cumulative battle damage).
- `robotiko-musical-metadata` — JSON generation migrated from the Gemini tool to the in-repo Claude skill.

### Notes
- Lesson confirmed: "amber glow" for eyes fails generation — use "dark amber glass lenses set into
  chrome sockets." Tattoo placement moved to inner forearm. "Cathedral" → "colossal iron vault."
- Cem Karaca in-scene poster easter egg abandoned (AI tools refuse real public figures);
  inspiration credit moved to YouTube description + optional outro credit card.

---

## [0.3.5] — 2026-04-22 — EP01 Launch & Social Infrastructure

### Added
- `episode-01/07_social_media/` — YouTube package, social atomization, launch checklist, walkthrough,
  external promotion strategy.
- Social infrastructure: YouTube + Instagram accounts (@fibuladev), banner, About section, playlist.
- Creator strategy defined (kept in the creator's private notes) — channel name Fibula,
  AUTHOR.md on EP10 release day, AI transparency from EP01, weekly release rhythm.

### Notes
- **EP01 launched on YouTube April 22, 2026.** First public episode of the series.
- Strategy pivot: pre-launch teaser campaign killed; Instagram repositioned as a post-launch Reels funnel.

---

## [0.3.2] — 2026-03-01 — Video Tooling: Seedance Migration & Duration Coverage

### Added
- **Duration Coverage Strategy** — architecture-level fix across 7 pipeline files. A scene is no longer
  assumed to be one clip; clips are generated via Direct / Speed Ramp / Multi-Clip modes to reach ~100%
  music coverage (EP02 motion script v02: 49 clips, 100.4% coverage for 448s of music).
- **Tool Assignment** — each clip is assigned a video tool (Kling / Veo / Seedance) by capability and
  credit budget; this is now standard motion-script output (EP03+).

### Changed
- Video generation tooling migrated to **Seedance 1.0** (CapCut built-in, 1080p, keyframe support)
  replacing the former 720p generator. Pipeline files, SKILL, and template updated accordingly.

### Removed
- **Multiframes mode killed** within one session of discovery — it consumed ~565 credits per generation
  against a 1200-credit monthly budget. Removed from the pipeline entirely; Kling + Veo + Seedance remain.

### Notes
- Binary asset storage migrated from AWS S3 to **Google Drive** (more accessible for open-source
  contributors); a custom-built Google Drive MCP server (`_tools/mcp-gdrive/`, no third-party packages)
  later handled binary archive.

---

## [0.3.0] — 2026-02-23 — Infrastructure Complete

### Added
- `_memory/lessons.md` — Claude self-improvement loop initialized
- `_memory/decisions_log.md` — Foundation decisions logged
- `_memory/todo.md` — Active task tracker
- `docs/getting-started.md` — Open source onboarding skeleton
- `docs/skills-guide.md` — Skills system documentation skeleton
- `docs/tools-setup.md` — Toolchain setup guide skeleton
- `tests/naming_check.py` — Naming convention validator skeleton
- `tests/pipeline_integrity.py` — Pipeline integrity checker skeleton
- `CLAUDE.md` — Claude Code session context
- `.gitignore` — Expanded with raw folders, secrets, and OS files
- Claude Code activated as the local LLM director (VSCode + Claude Code, active from 2026-02-23)

### Changed
- `_management/master.md` — Universe Canon v2.0 (full rewrite of the legacy universe file)
- `_management/pipeline_rules.md` — v2.0 with musical metadata step and skills system
- `_management/naming_convention.md` — v2.0 with new file types and commit convention
- `_management/architecture.md` — v2.0 with Claude Code, MCP roadmap, open source strategy
- `_management/project_metadata.json` — v2.0 with all 10 episodes and real production status
- `_assets/cast/character_profiles.json` — v2.0 with Robochica, phase visual states, Kintsugi detail
- `_templates/dramaturgy_template.md` — v2.0 with musical metadata input and approval checkboxes
- `_templates/visual_prompt_template.md` — v2.0 with quality checklist
- `_templates/video_prompt_template.md` — v2.0 with beat sync notes and fixed broken reference

### Removed
- The legacy universe file — replaced by `master.md`

---

## [0.2.0] — 2026-02-23 — EP02 Musical Metadata

### Added
- `episode-02/02_music/ep02_musical_metadata.json` — All-in-one musical metadata

---

## [0.1.0] — 2026-02-23 — Foundation Commit

### Added
- Full repository structure (95+ folders)
- All management documentation (initial versions)
- Asset library organized
- Templates ready
- Skills framework scaffolded (8 empty folders)
- Episode 01 partially migrated (lyrics, visual prompts, motion script)
- GitHub Actions workflow: `create_episode.yml`
- Python script: `scripts/create_episode.py`
- EP01 completed: video + visuals done

---

## Versioning Convention

| Version | Meaning |
|---|---|
| `0.X.0` | Infrastructure or management milestone |
| `0.0.X` | Episode production update |
| `1.0.0` | EP10 complete — open source release |
