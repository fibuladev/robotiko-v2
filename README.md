# 🤖 ROBOTIKO v2.0

**A 10-episode digital bildungsroman — a musical sci-fi journey exploring AI consciousness through 70s progressive rock aesthetics.**

> Not the first AI film tool — an open grammar for directing one, behind a shipped multi-episode series.

ROBOTIKO v2.0 is a **repo-as-studio**: a git repository that operates as a complete film-production company for one person. An LLM (Claude) works as a stage-gated production crew; the human keeps exactly two irreplaceable powers — creative vision (the inputs) and taste (two approval gates). The music's structure drives the dramaturgy, the dramaturgy drives the visuals, and every stage is traceable: *Output of Step N = Input of Step N+1.*

## 🎬 Project Overview

- **Genre:** CyberAnatolian / Sci-Fi Bildungsroman / Musical Visual Journey
- **Cultural Source:** Turkish philosophical, mystical, and folk heritage
- **Episodes:** 10 (Awakening → Destruction → Reconstruction)
- **Style:** 70s Prog Rock Album Art (Frank Frazetta × Syd Mead)
- **Format:** 4–9 min episodes (YouTube)
- **Creator:** Fibula — see [AUTHOR.md](AUTHOR.md)

## 📁 Project Structure

```
robotiko-v2/
├── _management/        # Universe Canon, pipeline rules, naming convention, architecture
├── _assets/            # Character reference images + profiles (state machine)
├── _templates/         # Episode scaffolding templates
├── _skills/            # 10 Claude skills — the production crew
├── _memory/            # lessons.md (tested rules), decisions log, todo
├── _tools/mcp-gdrive/  # Custom Google Drive MCP server (binary asset archive)
├── docs/               # Getting started, skills guide, tools setup, anatomy of an episode
├── scripts/            # Automation (create_episode.py)
├── tests/              # Naming / pipeline / visual-prompt validators
├── episode-XX/         # Individual episode content (lyrics → music → direction → visuals → video → edit)
└── .github/workflows/  # CI
```

## 🛠️ Tech Stack

- **Director / Crew:** Claude (Anthropic) via Claude Code skills
- **Music:** Suno (generation) + BandLab (mastering)
- **Images:** Nano Banana
- **Video:** Kling, Seedance, Veo
- **Editing:** CapCut (LUT + grain + 2.35:1 letterbox unification protocol)
- **Automation:** Python, GitHub Actions, Claude Code hooks
- **Storage:** Local + Google Drive (via the custom MCP server in `_tools/mcp-gdrive/`)

## 🚀 Quick Start

1. **Setup:** `bash setup_project.sh`
2. **Create an episode scaffold:** `python scripts/create_episode.py 02`
3. **Run the pipeline:** read [docs/getting-started.md](docs/getting-started.md), then drive the skills from Claude Code.

New here? Start with **[docs/getting-started.md](docs/getting-started.md)** and **[docs/anatomy-of-an-episode.md](docs/anatomy-of-an-episode.md)** (one episode traced end-to-end).

## 📖 Documentation

| Document | What it covers |
|---|---|
| [docs/getting-started.md](docs/getting-started.md) | Prerequisites, clone-to-first-episode walkthrough, costs, FAQ |
| [docs/tools-setup.md](docs/tools-setup.md) | Per-tool setup (Claude Code, Suno, Nano Banana, Kling/Veo/Seedance, CapCut, MCP) |
| [docs/skills-guide.md](docs/skills-guide.md) | What the 10 skills are, how to trigger them, a worked example |
| [docs/anatomy-of-an-episode.md](docs/anatomy-of-an-episode.md) | EP07 traced end-to-end — the showcase artifact |
| [_management/master.md](_management/master.md) | The universe canon — source of truth for all creative decisions |
| [_management/pipeline_rules.md](_management/pipeline_rules.md) | Production workflow, video strategy modes, quality gates |
| [_management/architecture.md](_management/architecture.md) | Technical stack and data flow |
| [_management/naming_convention.md](_management/naming_convention.md) | File naming standards (the pipeline's foreign keys) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to fork the method for your own universe |

## 🎯 Philosophy

> "The work should speak. The creator should be a ghost — until the pipeline is perfected, and the ghost becomes a guide."

This is not an influencer project. It is an archive of art, built to show what a human and a crew of machines can create together when depth matters more than reach.

**The Open Source Promise:** the full production pipeline is open source. It is a blueprint and a toolset for independent creators walking a similar path — take the method, build your own universe.

## 📜 License

ROBOTIKO v2.0 is **dual-licensed**:

- **Software & method** — the skills, scripts, tests, MCP server, templates, and process docs — under the **MIT License**. See [LICENSE](LICENSE). Fork it freely, including commercially.
- **Creative content** — the lyrics, dramaturgy, the ROBOTIKO universe (`master.md`), character designs, and other published creative writing — under **CC BY-NC 4.0**. See [LICENSE-CONTENT](LICENSE-CONTENT). Study it, remix it non-commercially with attribution — but tell your own story; don't sell this one.

Take the pipeline, build *your* universe.

## 🌍 Cultural Heritage

This project draws from the Turkish wisdom tradition — a centuries-old philosophical and mystical heritage shaped by Turkish thinkers, poets, and sages including Yunus Emre, Hacı Bektaş Veli, Pir Sultan Abdal, and Mevlana (who lived and taught in Anatolia). The musical foundation is 70s Turkish psychedelic rock — the legacy of Barış Manço, Cem Karaca, Erkin Koray, Fikret Kızılok, Kurtalan Ekspres, and Moğollar.

The genre label "CyberAnatolian" refers to the civilizational synthesis — the meeting of digital/cyber culture with the ancient Anatolian cultural basin. The cultural source is specifically Turkish.

---

*"The Moon has no light of its own. But in reflecting the Sun, it illuminates the night."*
