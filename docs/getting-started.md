# Getting Started with ROBOTIKO v2.0 Pipeline
> **Version:** 1.0 | **Status:** Draft — To be completed at EP10 open source release.

---

## What is This?

ROBOTIKO v2.0 is a 10-episode CyberAnatolian concept album + video series, built entirely by one human and Claude + AI Tools. This repository contains not just the creative assets, but the **entire production pipeline** — so others can replicate it for their own projects.

---

## Prerequisites

Before you begin, you need:

- [ ] **Claude Code** — [Install guide](https://docs.anthropic.com)
- [ ] **VSCode** — With Claude Code extension
- [ ] **GitHub account** — For version control
- [ ] **Google Drive** — For binary asset storage (via custom MCP server in `_tools/mcp-gdrive/`)
- [ ] **Suno AI** — For music generation
- [ ] **Nano Banana Pro** — For image generation
- [ ] **Kling / Veo / Seedance 1.0** — For video generation
- [ ] **CapCut** — For final editing

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/fibuladev/robotiko-v2.git
cd robotiko-v2
```

### 2. Read the Master document
```
_management/master.md
```
This is the Universe Bible. Read it entirely before doing anything else.

### 3. Open in VSCode with Claude Code
```bash
code .
```
Claude Code will automatically read `CLAUDE.md` and understand the project context.

### 4. Create a new episode
```bash
python scripts/create_episode.py {episode_number}
```

### 5. Follow the pipeline
See `_management/pipeline_rules.md` for the full step-by-step workflow.

---

## Repository Structure

See `_management/architecture.md` for the full structure explanation.

---

## Key Documents

| Document | Purpose |
|---|---|
| `_management/master.md` | Universe Bible — source of truth |
| `_management/pipeline_rules.md` | Production workflow |
| `_management/naming_convention.md` | File naming standards |
| `_management/architecture.md` | Technical stack |
| `CLAUDE.md` | Claude Code context |
| `_memory/lessons.md` | Claude self-improvement rules |

---

*Full documentation coming at EP10 open source release.*