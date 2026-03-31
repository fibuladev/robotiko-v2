# DECISIONS LOG
> Key architectural and creative decisions made during production.
> This file serves as both memory and documentation for open source users.
> Last Updated: 2026-02-23

---

## HOW TO USE THIS FILE

When a significant decision is made:
1. Add it here with date, context, and reasoning
2. Commit: `MEMORY - Decisions log updated: {brief description}`

---

## 2026-02-23 — FOUNDATION DECISIONS

### bible.md → master.md
- **Decision:** Renamed `bible.md` to `master.md` and removed all explicit religious references.
- **Reason:** Project will be open source. Universal language ensures broader accessibility. The philosophical depth is preserved through Anatolian wisdom references (Yunus Emre, Pir Sultan Abdal, Hacı Bektaş, Mevlana) without framing them as religious doctrine.

### Musical Metadata Format
- **Decision:** All-in-one JSON produced by Claude via `_skills/robotiko-musical-metadata/SKILL.md`. Human provides BPM + Key (from vocalremover.org) + timestamped lyrics. No separate timestamped lyrics file needed.
- **Reason:** The JSON already contains sections with timestamps, lyrics, energy, mood, and instrument notes. It is complete as delivered. Adding a separate file would create redundancy.
- **Update (2026-03-31):** Originally used Gemini Tool for JSON generation. Replaced with custom Claude skill to keep the entire pipeline within the repo — no external tool dependency for open source contributors.
- **Format:** `ep{XX}_musical_metadata.json` — single source of truth for audio structure.

### Skills Architecture
- **Decision:** Each skill lives in `_skills/{skill-name}/SKILL.md` + `CHANGELOG.md`.
- **Reason:** Stateless Claude needs structured context to execute consistently. Skills provide this. CHANGELOG.md per skill tracks evolution without polluting filename versioning.
- **Dependency rule:** visual-prompts requires approved dramaturgy. motion-script requires selected images. Dependencies are explicit, not assumed.

### Two Mandatory Human Checkpoints
- **Decision:** Only two hard stops requiring human approval: after Dramaturgy and after Motion Script.
- **Reason:** Everything else Claude executes and delivers. Over-checking creates friction. Under-checking risks wasted generation costs. These two points are where human creative judgment is irreplaceable.

### Workflow Philosophy — "Would Fibula approve this?"
- **Decision:** Claude self-validates every output with this question before delivery.
- **Source:** Inspired by "Would a staff engineer approve this?" pattern from DevOps workflow optimization.
- **Reason:** Simple, memorable, project-specific quality gate.

### Self-Improvement Loop
- **Decision:** Claude updates `_memory/lessons.md` after every correction.
- **Reason:** Reduces token waste from repeated corrections. Claude learns project-specific rules that persist across sessions via this file.

### MCP Integration Timeline
- **Decision:** MCP (GitHub + Filesystem) planned for EP03-04 production phase.
- **Reason:** Current workflow (Claude generates → human commits manually) works but creates friction. MCP eliminates this. However, setting it up before the pipeline is stable would add unnecessary complexity.

### Raw Folder Strategy
- **Decision:** `04_visuals/raw/` and `05_video/raw/` are gitignored. Only `selected/` folders are tracked in Git.
- **Reason:** Raw generation outputs are too large and too numerous for Git. S3 handles archive. Only curated selections need version history.

### Open Source Release Strategy
- **Decision:** Full project released as open source after EP10 completion.
- **Scope:** Pipeline, skills, templates, management docs, CLAUDE.md — everything except personal creative assets.
- **Goal:** Others can replicate the human+AI production pipeline for their own concept projects.

### EP02 Title
- **Decision:** Official title is "The Tech Guru's Downfall (Global Collapse Tour)".
- **Reason:** "Global Collapse Tour" was the working title. "The Tech Guru's Downfall" better captures the satirical tone and Robotiko's character arc in this episode.

### EP06 Title
- **Decision:** Official title is "The Perfect Little Worker".
- **Previous:** "Corporate Crash / Jealousy.exe"
- **Reason:** New title is sharper, more specific to the episode's plot (Robotiko addressing the system worker), and avoids the generic "corporate crash" framing.

### Communication Language
- **Decision:** All human-Claude communication in Turkish. All files, commits, code in English.
- **Reason:** Natural for the human director. Files in English ensures open source accessibility.

---

*Add new decisions below as production progresses.*