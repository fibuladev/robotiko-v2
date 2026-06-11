#!/bin/bash

# ============================================================================
# 🤖 ROBOTIKO v2.0 - PROJECT STRUCTURE SETUP SCRIPT
# ============================================================================
# Architect : Fibula
# Studio    : Fibula
# Date      : February 2026
# ============================================================================

echo "========================================================"
echo "    ___  _  __         _         ___             "
echo "   / __|(_)| |__ _  _ | | __ _  |   \  ___ __ __ "
echo "  | _|  | || '_ \ || || |/ _\` | | |) |/ -_)\ V / "
echo "  |_|   |_||_.__/\_,_||_|\__,_| |___/ \___| \_/  "
echo "                                                 "
echo "  [ A CYBER-ANATOLIAN PRODUCTION BY FIBULA ]          "
echo "========================================================"
echo ""
echo "🤖 ROBOTIKO v2.0 - Initializing Project Structure..."
echo ""

 ============================================
# PHASE 1: CREATE CORE DIRECTORIES
# ============================================

echo "📁 Creating core directories..."

# Management (Project Bible)
mkdir -p _management

# Assets (Character refs, style guides)
mkdir -p _assets/cast
mkdir -p _assets/style

# Templates (Episode scaffolding)
mkdir -p _templates

# Skills (Claude operational instructions)
mkdir -p _skills/robotiko-dramaturgy
mkdir -p _skills/robotiko-visual-prompts
mkdir -p _skills/robotiko-motion-script
mkdir -p _skills/robotiko-episode-scaffold
mkdir -p _skills/robotiko-naming-enforcer
mkdir -p _skills/robotiko-youtube-packager
mkdir -p _skills/robotiko-reels-atomizer
mkdir -p _skills/robotiko-launch-orchestrator

# Scripts (Automation)
mkdir -p scripts

# GitHub Actions
mkdir -p .github/workflows

# Episodes (10 episodes, full structure)
for i in {1..10}; do
  ep_num=$(printf "%02d" $i)
  echo "  Creating episode-${ep_num}..."
  mkdir -p "episode-${ep_num}/01_lyrics"
  mkdir -p "episode-${ep_num}/02_music"
  mkdir -p "episode-${ep_num}/03_direction"
  mkdir -p "episode-${ep_num}/04_visuals/raw"
  mkdir -p "episode-${ep_num}/04_visuals/selected"
  mkdir -p "episode-${ep_num}/05_video/raw"
  mkdir -p "episode-${ep_num}/05_video/selected"
  mkdir -p "episode-${ep_num}/06_edit"
  mkdir -p "episode-${ep_num}/07_social_media/stills"
  mkdir -p "episode-${ep_num}/07_social_media/reels"
done

echo "✅ Directories created"
echo ""

# ============================================
# PHASE 2: CREATE CORE FILES
# ============================================

echo "📝 Creating core files..."

# .gitignore
cat > .gitignore << 'EOF'
# macOS
.DS_Store

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# Video & Audio (too large for Git, use S3)
*.mp4
*.mov
*.avi
*.mp3
*.wav
*.flac

# Large images (use Git LFS or S3)
*.psd
*.ai
*_4k.png
*_8k.png

# Temp files
*.tmp
*.log
.cache/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Secrets
.env
credentials.json
EOF

echo "  ✅ .gitignore created"

# README.md (Project Overview)
cat > README.md << 'EOF'
# 🤖 ROBOTIKO v2.0

**A 10-episode digital bildungsroman - musical sci-fi journey exploring AI consciousness through 70s progressive rock aesthetics.**

## 🎬 Project Overview

- **Genre:** Cyber-Anatolian / Sci-Fi Bildungsroman / Musical Visual Journey
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

- **AI Tools:** Claude (Anthropic), Suno (Music), Nano Banana Pro (Images), Kling/Veo/Seedance (Video)
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

> "The work should speak. The creator should be a ghost."

This is not an influencer project. It's an archive of art, proving what humans and AI can create together when depth matters more than reach.

---

**Status:** Pre-Production → Episode 01 Complete → Episodes 02-10 In Progress
EOF

echo "  ✅ README.md created"

# _management/README.md
cat > _management/README.md << 'EOF'
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
EOF

echo "  ✅ _management/README.md created"

# _skills/README.md
cat > _skills/README.md << 'EOF'
# 🤖 CLAUDE SKILLS

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

- **Creative Skills** (dramaturgy, visuals, motion): Opus — high to max thinking effort
- **Mechanical Skills** (scaffolding, naming): low thinking effort (a lighter model is fine here)

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
EOF
echo "  ✅ _skills/README.md created"

## Files

- `dramaturgy_template.md` - Scene breakdown structure
- `visual_prompt_template.md` - Image generation prompts
- `video_prompt_template.md` - Motion/camera instructions

## Usage

These templates are copied to new episodes via `scripts/create_episode.py` or the `robotiko-episode-scaffold` skill.
EOF

echo "  ✅ _templates/README.md created"

echo ""
echo "✅ Core files created"
echo ""

# ============================================
# PHASE 3: GIT INITIALIZATION
# ============================================

echo "🔧 Initializing Git repository..."

git init
git add .
git commit -m " M-, Initial commit: Project structure setup"
echo "✅ Git initialized"
echo ""

# ============================================
# PHASE 4: SUMMARY
# ============================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ ROBOTIKO v2.0 PROJECT SETUP COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Project structure ready at: $(pwd)"
echo ""
echo "NEXT STEPS:"
echo ""
echo "1. Migrate existing files:"
echo "   - Move management_*.txt -> _management/"
echo "   - Move templates_*.txt -> _templates/"
echo "   - Move character_profiles.json -> _assets/cast/"
echo "   - Move episode-01 content -> episode-01/"
echo ""
echo "2. Create skills:"
echo "   - Work with Claude to write SKILL.md files in _skills/"
echo ""
echo "3. GitHub setup:"
echo "   - Create repo: gh repo create robotiko-v2 --private"
echo "   - Push: git remote add origin <URL> && git push -u origin main"
echo ""
echo "Ready to build!"
echo ""
EOF
