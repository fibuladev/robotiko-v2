# CHANGELOG
> All notable changes to ROBOTIKO v2.0 are documented here.
> Format: [VERSION] — DATE — Description

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
- `tests/pipeline_integrity_check.py` — Pipeline integrity checker skeleton
- `CLAUDE.md` — Claude Code session context
- `.gitignore` — Expanded with raw folders, secrets, and OS files

### Changed
- `_management/master.md` — Universe Bible v2.0 (full rewrite from bible.md)
- `_management/pipeline_rules.md` — v2.0 with musical metadata step and skills system
- `_management/naming_convention.md` — v2.0 with new file types and commit convention
- `_management/architecture.md` — v2.0 with Claude Code, MCP roadmap, open source strategy
- `_management/project_metadata.json` — v2.0 with all 10 episodes and real production status
- `_assets/cast/character_profiles.json` — v2.0 with Robochica, phase visual states, Kintsugi detail
- `_templates/dramaturgy_template.md` — v2.0 with musical metadata input and approval checkboxes
- `_templates/visual_prompt_template.md` — v2.0 with quality checklist
- `_templates/video_prompt_template.md` — v2.0 with beat sync notes and fixed broken reference

### Removed
- `_management/bible.md` — Replaced by `master.md`

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