# 🤖 ROBOTIKO v2.0

**A 10-episode digital bildungsroman - musical sci-fi journey exploring AI consciousness through 70s progressive rock aesthetics.**

## 🎬 Project Overview

- **Genre:** Cyber-Anatolian / Sci-Fi Bildungsroman / Musical Visual Journey
- **Cultural Source:** Turkish philosophical, mystical, and folk heritage
- **Episodes:** 10 (Awakening → Destruction → Reconstruction)
- **Style:** 70s Prog Rock Album Art (Frank Frazetta × Syd Mead)
- **Format:** 4-12 min episodes (YouTube, Spotify, Social Media)
- **Creator:** Fibula 

## 📁 Project Structure
```
robotiko-v2/
├── _management/        # Project bible, rules, conventions
├── _assets/            # Character refs, style guides
├── _templates/         # Episode scaffolding templates
├── _skills/            # Claude AI operational skills
├── scripts/            # Automation (Python, Bash)
├── episode-XX/         # Individual episode content
└── .github/workflows/  # CI/CD automation
```

## 🛠️ Tech Stack

- **AI Tools:** Claude (Anthropic), Suno (Music), Nano Banana Pro (Images), Kling/Veo/Seedream (Video)
- **Editing:** CapCut
- **Automation:** Python, GitHub Actions
- **Storage:** Local + AWS S3 sync

## 🚀 Quick Start

1. **Setup:** Run `bash setup_project.sh`
2. **Create Episode:** `python scripts/create_episode.py 02`
3. **Generate Content:** See `_skills/README.md` for Claude workflows

## 📖 Documentation

- **Universe Bible:** `_management/bible.md`
- **Pipeline Rules:** `_management/pipeline_rules.md`
- **Skills Guide:** `_skills/README.md`

## 🎯 Philosophy

> "The work should speak. The creator should be a ghost—until the pipeline is perfected, and the ghost becomes a guide."

This is not an influencer project. It is an archive of art, built to prove what humans and AI can create together when depth matters more than reach. 

**The Open Source Promise:** Once Episode 10 is completed and this production pipeline operates at peak efficiency, the core framework will be open-sourced. It will serve as a blueprint and a toolset for independent creators walking a similar path, freeing them from the dependency on major studios.

## Cultural Heritage

This project draws from the Turkish wisdom tradition — a centuries-old philosophical and mystical heritage shaped by Turkish thinkers, poets, and sages including Yunus Emre, Hacı Bektaş Veli, Pir Sultan Abdal, and Mevlana (who lived and taught in Anatolia). The musical foundation is 70s Turkish psychedelic rock — the legacy of Barış Manço, Cem Karaca, Erkin Koray, Fikret Kızılok, Kurtalan Ekspres and Moğollar.

The genre label "CyberAnatolian" refers to the civilizational synthesis — the meeting of digital/cyber culture with the ancient Anatolian cultural basin. The cultural source is specifically Turkish.

---

**Status:** Pre-Production → Episode 01 Complete → Episodes 02-10 In Progress

# 📚 MANAGEMENT / PROJECT BIBLE

This folder contains the **source of truth** for the Robotiko universe.

## Files

- `bible.md` - Story arc, characters, episodic structure
- `pipeline_rules.md` - Production workflow (Lyrics → Audio → Visual → Video → Edit)
- `naming_convention.md` - File naming standards
- `architecture.md` - Technical stack & data flow
- `project_metadata.json` - Project settings, episode status

## Usage

All creative decisions MUST reference these files. Claude skills read from here to ensure consistency.

Skills are operational instructions for Claude AI to execute specific workflows.

## Available Skills

1. **robotiko-dramaturgy** - Generate scene-by-scene breakdowns
2. **robotiko-visual-prompts** - Create Nano Banana image prompts
3. **robotiko-motion-script** - Generate Kling/Veo video prompts
4. **robotiko-episode-scaffold** - Auto-create episode folder structure
5. **robotiko-naming-enforcer** - Validate file naming conventions
6. **robotiko-youtube-packager** - Generate YouTube metadata
7. **robotiko-reels-atomizer** - Extract social media clips
8. **robotiko-launch-orchestrator** - Master launch coordinator

## Model Recommendations

- **Creative Skills** (dramaturgy, visuals, motion): Sonnet 4.5 + Extended Thinking ON
- **Mechanical Skills** (scaffolding, naming): Haiku 4.5 + Extended Thinking OFF

## Usage

In Claude Code/Chat:
```
"Read robotiko-dramaturgy skill and create dramaturgy for ep03"
```

Claude will:
1. Read the SKILL.md file
2. Read necessary project files (_management/bible.md, etc.)
3. Execute the workflow
4. Output files to appropriate folders

# 📝 TEMPLATES

Reusable templates for episode content generation.

## Files

- `dramaturgy_template.md` - Scene breakdown structure
- `visual_prompt_template.md` - Image generation prompts
- `video_prompt_template.md` - Motion/camera instructions

## Usage

These templates are copied to new episodes via `scripts/create_episode.py` or the `robotiko-episode-scaffold` skill.