# SYSTEM ARCHITECTURE
> **Version:** 2.0 | **Last Updated:** 2026-02-23

---

## 1. TECHNICAL STACK

| Layer | Tool | Role |
|---|---|---|
| **Version Control** | GitHub | The Brain — all decisions, all files, all history |
| **Storage** | AWS S3 | Long-term archive for heavy video/audio assets |
| **Automation** | GitHub Actions + Python Scripts | Episode scaffolding, naming validation, status tracking |
| **LLM Director** | Claude (Opus) via Claude Code + VSCode | Dramaturgy, visual prompts, motion scripts, skill execution |
| **Local IDE** | VSCode + Claude Code | Primary development environment (active from 2026-02-23) |
| **Music Generation** | Suno AI | Audio production |
| **Metadata Generation** | Claude (robotiko-musical-metadata skill) | Musical metadata JSON from human-provided BPM, Key, timestamped lyrics |
| **Image Generation** | Nano Banana Pro | Visual prompt execution |
| **Video Generation** | Kling / Veo / Seedance 1.0 | Motion production |
| **Editing** | CapCut | Final assembly |

---

## 2. DATA FLOW

### Full Pipeline
```
Human (Lyrics + Vision)
    → Suno AI (Audio)
    → Claude (Musical Metadata JSON — from human BPM/Key/timestamps)
    → Claude / master.md / concept_notes (Dramaturgy) [✋ CHECKPOINT]
    → Claude (Visual Prompts)
    → Nano Banana Pro (Images)
    → Human (Image Selection)
    → Claude (Motion Script) [✋ CHECKPOINT]
    → Kling / Veo / Seedance 1.0 (Video)
    → Human (Video Selection)
    → CapCut (Final Edit)
    → YouTube + Social Media
```

### Musical Metadata Flow (Critical)
```
Human listens to audio + runs vocalremover.org (BPM/Key)
    → Claude (robotiko-musical-metadata skill)
    → ep{XX}_musical_metadata.json (all-in-one)
        ├── tempo, key, time_signature
        ├── mood[], instruments[]
        └── sections[] {type, start, end, energy, lyrics, notes}
    → This JSON is the temporal skeleton for Dramaturgy
```

---

## 3. REPOSITORY STRUCTURE

```
robotiko-v2/
│
├── CLAUDE.md                    # Claude's role & project context (auto-read by Claude Code)
│
├── _management/                 # Source of truth documentation
│   ├── master.md                # Universe Master File — THE LAW
│   ├── pipeline_rules.md        # Production workflow
│   ├── naming_convention.md     # File naming standards
│   ├── architecture.md          # This document
│   └── project_metadata.json    # Episode status tracker
│
├── _assets/                     # Reusable creative assets
│   ├── cast/
│   │   ├── character_profiles.json
│   │   ├── ref_robotiko_master.png
│   │   └── ref_mentor_master.png
│   └── style/
│       └── visual_dna.md
│
├── _templates/                  # Episode scaffolding templates
│   ├── dramaturgy_template.md
│   ├── visual_prompt_template.md
│   └── video_prompt_template.md
│
├── _skills/                     # Claude operational workflows
│   ├── README.md
│   ├── robotiko-dramaturgy/
│   │   ├── SKILL.md
│   │   └── CHANGELOG.md
│   ├── robotiko-visual-prompts/
│   │   ├── SKILL.md
│   │   └── CHANGELOG.md
│   ├── robotiko-motion-script/
│   │   ├── SKILL.md
│   │   └── CHANGELOG.md
│   ├── robotiko-episode-scaffold/
│   │   ├── SKILL.md
│   │   └── CHANGELOG.md
│   ├── robotiko-naming-enforcer/
│   │   ├── SKILL.md
│   │   └── CHANGELOG.md
│   ├── robotiko-youtube-packager/
│   │   ├── SKILL.md
│   │   └── CHANGELOG.md
│   ├── robotiko-reels-atomizer/
│   │   ├── SKILL.md
│   │   └── CHANGELOG.md
│   └── robotiko-launch-orchestrator/
│       ├── SKILL.md
│       └── CHANGELOG.md
│
├── _memory/
│   └── decisions_log.md         # Key decisions log (memory across sessions)
│
├── scripts/
│   └── create_episode.py        # Episode scaffolding script
│
├── .github/workflows/
│   ├── create_episode.yml       # Episode scaffold trigger
│   └── naming_check.yml         # Naming convention validator (planned)
│
├── episode-01/ through episode-10/
│   ├── 01_lyrics/
│   │   └── ep{XX}_lyrics_v01.md
│   ├── 02_music/
│   │   ├── ep{XX}_audio_v01.wav       # Stored in S3 / Git LFS
│   │   └── ep{XX}_musical_metadata.json
│   ├── 03_direction/
│   │   ├── ep{XX}_concept_notes.md
│   │   └── ep{XX}_dramaturgy_v01.md
│   ├── 04_visuals/
│   │   ├── ep{XX}_visual_prompts_v01.md
│   │   ├── raw/
│   │   └── selected/
│   ├── 05_video/
│   │   ├── ep{XX}_motion_script_v01.md
│   │   ├── raw/
│   │   └── selected/
│   ├── 06_edit/
│   └── 07_social_media/
│       ├── stills/
│       └── reels/
```

---

## 4. FOLDER MIRRORING (S3 Backup)

All generated binary assets (audio, images, video) are stored exclusively on AWS S3 — never in Git:
```
Local:  episode-{XX}/02_music/         ==  S3: robotiko-bucket/episode-{XX}/02_music/
Local:  episode-{XX}/04_visuals/raw/   ==  S3: robotiko-bucket/episode-{XX}/04_visuals/raw/
Local:  episode-{XX}/04_visuals/selected/  ==  S3: robotiko-bucket/episode-{XX}/04_visuals/selected/
Local:  episode-{XX}/05_video/raw/     ==  S3: robotiko-bucket/episode-{XX}/05_video/raw/
Local:  episode-{XX}/05_video/selected/    ==  S3: robotiko-bucket/episode-{XX}/05_video/selected/
```
Git tracks only text files: lyrics, metadata JSON, dramaturgy, visual prompts, motion scripts, management docs.

Sync trigger: Automatic when episode is tagged as `completed` (planned via GitHub Actions).

---

## 5. CLAUDE CODE INTEGRATION

### How Claude Code Works in This Project
- Claude Code runs in VSCode's integrated terminal
- `CLAUDE.md` in repo root is auto-read on every session — Claude knows the project immediately
- Skill execution: Human says trigger phrase → Claude reads `_skills/{skill}/SKILL.md` → Executes → Commits output
- File operations: Claude reads, writes, and commits files directly (no manual copy-paste)

### CLAUDE.md Purpose
The `CLAUDE.md` file in the repo root gives Claude Code instant context:
- Project identity and role
- Which management files to read first
- Skill system overview
- Key rules (no revenge, no cheap melodrama, no gratuitous melancholy, no ornamental excess, visual suffix, etc.)

---

## 6. MCP INTEGRATION (Planned — EP03-04 Phase)

MCP (Model Context Protocol) servers will extend Claude's capabilities:

| MCP Server | Capability | Impact |
|---|---|---|
| **GitHub MCP** | Direct commit, PR, branch management | Claude commits without manual git commands |
| **Filesystem MCP** | Read/write files natively | Claude manages files autonomously |

**Current workaround:** Claude generates files → Human commits manually.
**After MCP:** Claude generates files → Claude commits directly → Human reviews PR.

---

## 7. AUTOMATION ROADMAP

| Automation | Status | Trigger |
|---|---|---|
| Episode scaffolding | ✅ Active | `create_episode.yml` GitHub Action |
| Naming convention check | 📋 Planned | Pre-commit hook + GitHub Action on push |
| Episode status auto-update | 📋 Planned | `project_metadata.json` auto-patch on file commit |
| S3 sync on completion | 📋 Planned | GitHub Action on episode `completed` tag |
| MCP GitHub integration | 📋 Planned | EP03-04 phase |

---

## 8. OPEN SOURCE STRATEGY

The full project — pipeline, skills, templates, management docs — will be released as open source after EP10 completion.

**What others will get:**
- A complete AI-assisted video production pipeline
- All skill definitions (reusable for any concept album/video series)
- `CLAUDE.md` and management docs as templates
- The proof of concept: one human + Claude = 10-episode series

**Key files for open source release:**
- `CLAUDE.md` — instant onboarding for Claude Code users
- `_skills/` — reusable workflow definitions
- `_management/` — adaptable templates
- `CONTRIBUTING.md` — to be written at EP10