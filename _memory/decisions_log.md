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
- **Reason:** Project will be open source. Universal language ensures broader accessibility. The philosophical depth is preserved through the Turkish wisdom tradition (Yunus Emre, Pir Sultan Abdal, Hacı Bektaş, Mevlana) without framing them as religious doctrine.

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
- **Reason:** Raw generation outputs are too large and too numerous for Git. Google Drive handles the binary archive (via the custom MCP server). Only curated selections need version history.

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

## 2026-03-25 — CREATOR IDENTITY & CHANNEL STRATEGY

### Creator Strategy Finalized
- **Decision:** Creator identity, channel architecture, open source rollout, social media strategy, and inspiration credits strategy approved and documented in `_management/creator_strategy.md`.
- **Key decisions:**
  - Channel name: **Fibula** (creator identity, not project name — allows future projects)
  - AUTHOR.md approved — appears only on EP10 release day when repo goes public
  - No timestamps in YouTube descriptions (cinematic integrity — "do not skip")
  - No end screens except EP10 GitHub link (silence after music is sacred)
  - Repository goes public on EP10 release day — no delay
  - AI transparency from EP01 — no hiding, no phased reveal
  - Inspiration credits at episode level, not project level (Cem Karaca → EP05, Korkmazgil → EP06)
  - Pinned comments serve as breadcrumbs, never duplicate description content
  - Social media: YouTube + Instagram + TikTok. No X/Twitter. No face reveal, ever.
  - Release rhythm: weekly (not day-locked). EP01 launch: April 22, 2026
  - Pre-launch: 4 weeks starting March 25
  - Post-series: gradual fade-out over 6-7 weeks, then silence
  - Banner evolves every 2-3 episodes to reflect Robotiko's arc
  - About section has 4 progressive phases revealing more over time
  - #aiart hashtag used from EP01
  - Social content derived from episode material via reels-atomizer skill

### EP05 — Cem Karaca Inspiration Credit
- **Original plan (2026-03-31):** Worn vintage Cem Karaca "Delikanlı Sevdası" concert poster composited onto the wall of Robotiko's room in S26-S27 as a discoverable easter egg honoring the song that inspired EP05.
- **Revision (2026-04-06):** Poster plan dropped. Inspiration credit moved to (1) YouTube description — explicit "Inspired by Cem Karaca — Delikanlı Sevdası" line, (2) optional outro credit card at end of episode showing song title and artist name. In-scene poster abandoned.
- **Reason for revision:** Nano Banana / Gemini 2.5 Flash Image refused both generation and compositing of real public figures — policy blocks editing workflows too, not just generation. Manual Photoshop perspective warp attempted but did not achieve the required lighting/grain integration across S26-S29. Flux Kontext via fal.ai was identified as a technical alternative but requires learning curve and cost not justified by the reach of a peripheral easter egg (~5% of audience would notice).
- **Why the new plan is stronger:** YouTube description + outro credit reaches 100% of viewers. It transforms the reference from a hidden easter egg into an honest, visible act of gratitude — which better matches the intent (the song is an inspirational debt, not a hidden wink). Cem Karaca's legacy is honored openly rather than secretly.
- **Pattern for future episodes:** Any real-figure easter egg must be validated against current AI tool capabilities BEFORE being written into visual prompts. Default to outro credits unless a proven compositing workflow exists.

### EP06 — Korkmazgil Easter Egg (Future)
- **Decision:** Korkmazgil portrait visible OUTSIDE the sterile workspace — corridor or street wall as Robotiko exits.
- **Reason:** EP06 inspired by "Bir Ornek Insan Portresi." Poet exists outside the machine. To be integrated during EP06 dramaturgy.

---

*Add new decisions below as production progresses.*