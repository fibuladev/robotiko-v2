# Tools Setup Guide
> **Version:** 1.0 | **Status:** Draft — To be completed at EP10 open source release.

---

## Overview

ROBOTIKO v2.0 uses a specific toolchain. Each tool handles a distinct stage of the pipeline.

| Tool | Stage | Purpose |
|---|---|---|
| Claude Code + VSCode | Direction | Dramaturgy, visual prompts, motion scripts |
| Suno AI | Music | Audio generation from lyrics |
| Gemini | Metadata | Musical metadata JSON generation |
| Nano Banana | Visuals | Image generation from prompts |
| Kling / Veo | Video | Motion generation from images |
| CapCut | Edit | Final assembly |
| GitHub | Version Control | All files, all history |
| AWS S3 | Storage | Heavy assets archive |

---

## Claude Code Setup

*Detailed setup instructions coming at EP10 open source release.*

Quick start:
1. Install Claude Code
2. Open VSCode
3. Clone the repository
4. Claude Code reads `CLAUDE.md` automatically on session start

---

## Suno AI Setup

*Coming at EP10 open source release.*

---

## Gemini Musical Metadata Setup

*Coming at EP10 open source release.*

Key output format: `ep{XX}_musical_metadata.json`
All-in-one JSON with sections, timestamps, energy, mood, lyrics, instruments.

---

## Nano Banana Pro Setup

*Coming at EP10 open source release.*

---

## Kling / Veo Setup

*Coming at EP10 open source release.*

Video strategy modes:
- Mode A: Standard (5s) — atmospheric shots
- Mode B: Start/End Keyframes (5s/10s) — transformations
- Mode C: Extension — continuous pans

---

## AWS S3 Setup

*Coming at EP10 open source release.*

Folder mirroring structure:
```
Local: episode-{XX}/04_visuals/raw/  ==  S3: robotiko-bucket/episode-{XX}/04_visuals/raw/
Local: episode-{XX}/05_video/raw/    ==  S3: robotiko-bucket/episode-{XX}/05_video/raw/
```

---

*Full tools documentation coming at EP10 open source release.*