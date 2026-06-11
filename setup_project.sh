#!/bin/bash

# ============================================================================
# ROBOTIKO v2.0 - PROJECT STRUCTURE SETUP SCRIPT
# ============================================================================
# Architect : Fibula
# Studio    : Fibula
# ============================================================================
#
# Creates the standard folder structure (idempotent: safe to re-run; existing
# files are never overwritten). It does NOT touch README/management/skill files
# and does NOT initialise or commit to git. After cloning the repo you normally
# do not need to run this at all - the structure already exists. Use it when
# forking the method to bootstrap a fresh tree.
# ============================================================================

set -e

echo "========================================================"
echo "  ROBOTIKO v2.0 - Initializing project structure"
echo "  [ A CYBER-ANATOLIAN PRODUCTION BY FIBULA ]"
echo "========================================================"
echo ""

# ------------------------------------------------------------
# Core directories
# ------------------------------------------------------------
echo "Creating core directories..."

mkdir -p _management
mkdir -p _assets/cast
mkdir -p _assets/style
mkdir -p _assets/banners
mkdir -p _templates
mkdir -p _tools
mkdir -p scripts
mkdir -p tests
mkdir -p docs
mkdir -p .github/workflows

# Skills (10 operational runbooks)
for skill in \
  robotiko-musical-metadata \
  robotiko-dramaturgy \
  robotiko-visual-prompts \
  robotiko-motion-script \
  robotiko-episode-scaffold \
  robotiko-naming-enforcer \
  robotiko-youtube-packager \
  robotiko-reels-atomizer \
  robotiko-launch-orchestrator \
  robotiko-capcut-editor; do
  mkdir -p "_skills/${skill}"
done

# ------------------------------------------------------------
# Episode folders (10 episodes, full per-episode structure)
# ------------------------------------------------------------
for i in $(seq 1 10); do
  ep_num=$(printf "%02d" "$i")
  echo "  episode-${ep_num}"
  mkdir -p "episode-${ep_num}/01_lyrics"
  mkdir -p "episode-${ep_num}/02_music"
  mkdir -p "episode-${ep_num}/03_direction"
  mkdir -p "episode-${ep_num}/04_visuals/raw"
  mkdir -p "episode-${ep_num}/04_visuals/selected"
  mkdir -p "episode-${ep_num}/05_video/raw"
  mkdir -p "episode-${ep_num}/05_video/selected"
  mkdir -p "episode-${ep_num}/06_edit"
  mkdir -p "episode-${ep_num}/07_social_media"
done

echo ""
echo "Done. Folder structure is ready."
echo ""
echo "Next steps:"
echo "  - Scaffold an episode's working files:  python scripts/create_episode.py 02"
echo "  - Read docs/getting-started.md for the full walkthrough."
echo "========================================================"
