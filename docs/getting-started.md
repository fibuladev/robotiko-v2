# Getting Started with ROBOTIKO v2.0

> A complete, first-run walkthrough — from cloning the repo to delivering your first episode.
> If you read only one document before touching the pipeline, read this one.

---

## What This Is

ROBOTIKO v2.0 is a **repo-as-studio**: a single git repository that operates as a complete film-production company for one person. The human keeps exactly two irreplaceable powers — creative vision (the inputs) and taste (two approval gates). Everything between is run by Claude through [Claude Code](https://docs.claude.com/en/docs/claude-code), acting as a stage-gated production crew. The crew is defined as a set of **skills** (`_skills/`), each a small instruction file Claude reads before it works.

The spine of the whole system is the music. Once an episode's audio exists, its structure is captured in a **musical metadata JSON** (`ep{XX}_musical_metadata.json`) — sections, timestamps, energy, mood, lyrics, instruments. That file is the *temporal source of truth*: every scene, every visual, every camera move is anchored to a timestamp in it. Nothing downstream invents its own clock.

From there the work flows as a directed acyclic graph, where the output of each step is the input of the next:

```
lyrics → music → metadata JSON → dramaturgy → visual prompts → images
       → motion script → video → edit → package
```

There are **two human gates** in that flow, and only two. The first is **after dramaturgy** — you approve the scene-by-scene breakdown before any visuals are made. The second is **after the motion script** — you approve camera moves, tool assignments, and tech strategy before any video is generated. Everything else, Claude executes and delivers. The rest of this guide walks you from an empty machine to your first finished episode.

---

## Prerequisites

You need a few accounts and a little local setup. The table below is the short version; per-tool sign-up and configuration lives in **[tools-setup.md](tools-setup.md)** — read it alongside this guide.

**Local environment**

- **A git client** — any recent [Git](https://git-scm.com/downloads) install. The whole studio is a git repository.
- **Python 3.11+** — [python.org/downloads](https://www.python.org/downloads/). Used by the scaffolding script and the validator tests. No third-party packages required for scaffolding.
- **Claude Code** (Anthropic) — the director and crew. Install and sign-in instructions: [docs.claude.com/en/docs/claude-code](https://docs.claude.com/en/docs/claude-code). It reads `CLAUDE.md` automatically on session start.

**Creative tool accounts** (each handles one pipeline stage)

- **[Suno](https://suno.com)** — music generation from your lyrics.
- **[BandLab](https://www.bandlab.com)** — mastering of the Suno output.
- **Nano Banana** — image generation from visual prompts.
- **Kling**, **Veo**, and/or **Seedance** — video generation from selected images. You do not need all three; see the FAQ.
- **[CapCut](https://www.capcut.com)** — final edit, grading, grain, and the 2.35:1 letterbox unification protocol.

**Optional**

- **A Google account** — only if you want to use the Google Drive MCP archive (`_tools/mcp-gdrive/`) to store the large binary assets (PNG, MP4, WAV) that are deliberately kept out of git. See the FAQ for where big files live.

> For where to sign up, how to authorize the MCP server, and per-tool notes, go to **[tools-setup.md](tools-setup.md)**.

---

## Clone to First Episode

The following takes you from nothing to an episode scaffold with the pipeline running. Steps 1–3 are mechanical. Step 4 is where the crew goes to work.

### 1. Clone the repository

```bash
git clone https://github.com/fibuladev/robotiko-v2.git
cd robotiko-v2
```

### 2. Run the setup script

```bash
bash setup_project.sh
```

This lays down the core directory tree (`_management/`, `_assets/`, `_skills/`, the ten `episode-XX/` folders, and so on). If you cloned a populated repo the directories already exist; the script is idempotent and safe to run.

### 3. Scaffold an episode

```bash
python scripts/create_episode.py 02
```

This creates `episode-02/` with the full folder tree, drops in an empty concept-notes file for your first creative input, and copies the direction / visuals / video templates with the episode number substituted in. Want to see what it would do without writing anything first? Use the dry run:

```bash
python scripts/create_episode.py 02 --dry-run
```

The episode number is always two digits in the filenames the script produces (`ep02_…`), regardless of how you type it on the command line.

### 4. Run the pipeline, stage by stage

Open the repo in your editor with Claude Code and drive the stages with the trigger phrases below. Each phrase tells Claude which skill to read first; it then reads the required project files and executes. Run each stage in its own clean Claude Code session — the pipeline is designed for that.

The full per-stage rules, inputs, and outputs live in **[../\_management/pipeline_rules.md](../_management/pipeline_rules.md)**. The order, with the two gates marked:

| # | Trigger phrase | What it produces |
|---|---|---|
| 1 | *Create musical metadata for EP02* | `ep02_musical_metadata.json` (the temporal source of truth) |
| — | *(you write the concept notes)* | `ep02_concept_notes.md` — overrides and must-have shots |
| 2 | **Create dramaturgy for EP02** | `ep02_dramaturgy.md` — scene-by-scene breakdown |
| | **⛔ STOP — HUMAN GATE 1.** Review and approve the dramaturgy before continuing. | |
| 3 | *Generate visual prompts for EP02* | `ep02_visual_prompts.md` — Phase 1: reference prompts, art-direction locks, scene→space coverage map (scenes intentionally pending) |
| | **⛔ STOP — REFERENCE GATE.** Generate the reference images, approve them, and record the approval (gate "1R") before any scene prompt is written. Phase 2 then writes the scenes against your approved images. See [two-phase-visual-prompts.md](two-phase-visual-prompts.md). | |
| — | *(you generate scene images in Nano Banana against the approved references, then curate the keepers)* | selected PNGs |
| 4 | **Generate motion script for EP02** | `ep02_motion_script.md` — camera moves, tool assignments, beat sync |
| | **⛔ STOP — HUMAN GATE 2.** Review camera moves and tool assignments before any video is generated. | |
| — | *(you generate video per the script, then curate the keepers)* | selected MP4s |
| 5 | *Edit EP02 in CapCut* | `ep02_capcut_guide_v01.md` — the edit guide you follow in CapCut |
| 6 | *Package EP02 for YouTube* | title, description, tags (per the metadata standards) |
| 7 | *Atomize EP02 for social* | platform-specific short clips |
| 8 | *Orchestrate EP02 launch* | launch checklist |

Before lyrics and music, an episode also needs its words and its audio: you write the lyrics, Suno generates the track, and you master it in BandLab. The metadata JSON in step 1 is built from that finished audio plus the BPM and key you read off it.

The stops are not optional and never skipped. They are the entire point of the arrangement: the machine does the labor; the human keeps the taste. The two creative gates (dramaturgy, motion script) approve *direction*; the reference gate approves the *world* the scenes will be framed against.

> New to the skills themselves? **[skills-guide.md](skills-guide.md)** explains what each one does and walks a worked example. The full trigger table also lives in **[../CLAUDE.md](../CLAUDE.md)**.

---

## What the Pipeline Does *Not* Do

Set your expectations honestly before your first episode. This pipeline is a huge multiplier on time and cost — one person runs a stage-gated film crew that would otherwise take a team — but it is **not copy-paste-and-done**. The stills and clips do not fall out perfect on demand, and no amount of prompt discipline makes the generators obedient.

The realistic number, from this project's own production across nine episodes, is that roughly **75-85% of shots land on the first generation** when their reference images already exist. That figure is an experiential observation from the edit bay, not instrumented telemetry — treat it as a planning heuristic, not a guarantee. The remaining shots need a reshoot or **live prompt surgery**: you catch a failure at generation time and rewrite the shot on the spot. Budget credits, and a little patience, for that tail.

The canonical example is **EP09's S30 "Full Kintsugi" shot**, where a Slow Zoom Out on a single frame made the model invent set dressing that does not exist in the universe — it failed four times before a live switch to a two-frame (start + end) setup, anchored to an existing wide frame from the episode's own set, fixed it on the first retry. The full before/after prompts and the general rule they produced are written up in **[hallucinating-camera.md](hallucinating-camera.md)** — read it before your first video-generation session so the failures are expected, not alarming.

The mindset that keeps this sane: discovering at generation time that a shot needs a better reference or a rewritten prompt is a **normal, healthy part of the flow**, not a sign something went wrong. The pipeline gets you 80% of the way in a fraction of the time; the last stretch is craft, and craft is iterative.

One more expectation to set straight: the pipeline does not reproduce *images*. The repo tracks the ref PROMPT + geometry note — the reproducible spec. It does not track the pixels. Your fork generates its own refs from the same prompt; they will differ; Phase 2 frames to YOURS. Process reproducible; assets, deliberately, not.

---

## Expected Costs

This is an honest, approximate picture. Tool pricing changes often, so where a number isn't verifiable from inside this repo, treat it as "check the tool's site" rather than gospel. None of these are sponsorships; they are simply the tools the pipeline was built against.

| Tool | Stage | Rough cost | Notes |
|---|---|---|---|
| Claude Code (Anthropic) | Direction / crew | Subscription **or** API usage | A Claude subscription covers Claude Code; heavy API use is billed per token. Pricing varies — check Anthropic's site. |
| Suno | Music | Subscription | Tiered monthly plans. Pricing varies — check Suno's site. |
| BandLab | Mastering | Free tier exists | Mastering is available without a paid plan at time of writing. |
| Nano Banana | Images | Credit / usage based | Pricing varies — check the tool's site. |
| Kling | Video | Credit based | You spend credits per generation; keyframe and longer clips cost more. Pricing varies — check Kling's site. |
| Veo | Video | Free tier exists | A free tier exists; quality tiers and quotas vary — check Google's site. |
| Seedance | Video | Runs **inside CapCut** | Consumes CapCut credits rather than a separate bill (see below). |
| CapCut Pro | Edit + some video gen | **~1200 credits / month** on the Pro plan | Verified from this project's own production notes (`_memory/lessons.md`). A single Seedance multi-frame generation can cost ~565 credits, so the monthly budget is real and worth planning. |

A practical reading: the two recurring subscriptions you'll actually feel are **Claude** (the crew) and **CapCut Pro** (the edit, which also hosts Seedance video). Image and video credits are consumed in bursts per episode rather than as a flat monthly cost. The minimum viable setup is cheaper than the full kit — see the first FAQ.

---

## FAQ

**Do I need all the paid tools?**
No. The non-negotiable pieces are Claude Code (it drives everything) and a way to make music, images, and video. You can run a lean version with Claude + Suno + Nano Banana + one video tool + the free tier of an editor. The full toolchain (multiple video generators, CapCut Pro) buys you more range and quality, not a different pipeline.

**Can I swap a tool?**
Yes — the pipeline cares about *stages*, not brands. Any image generator can stand in for Nano Banana, any of Kling / Veo / Seedance can cover video, and the motion script's tool assignments are recommendations the human can override. If you swap something, update the toolchain notes in `_management/project_metadata.json` and adjust the relevant skill so its prompts suit the new tool.

**What are the two human gates?**
Exactly two approvals are required, and Claude will stop and wait at each. **Gate 1 is after dramaturgy** — you sign off on the scene breakdown before any visuals are made. **Gate 2 is after the motion script** — you sign off on camera moves, tool assignments, and tech strategy before any video is generated. Everything else runs without hand-holding.

**Where do the big binary files live?**
Not in git. The raw and selected image/video folders, plus audio, are gitignored on purpose — they're far too large for version control. The repository tracks the *recipe* (prompts, scripts, metadata, edit guides), not the renders. The binary archive lives on **Google Drive**, reached through the project's own custom MCP server in **[../\_tools/mcp-gdrive/](../_tools/mcp-gdrive/)** — a small, self-contained server with no third-party storage SDK. (There is no AWS or external bucket; any older note saying otherwise is stale.)

**Why are all the files English-only?**
The human and the studio speak two languages by design: creative conversation happens in the author's native language, but **every file, commit, and piece of code is written in English**. That keeps the repository legible to anyone in the world who forks it — the whole reason this is open source.

**Can I fork this for my own universe?**
That's the intent. The software and method are MIT-licensed; take the skills, scripts, tests, MCP server, and templates and build your own story. Start by replacing `_management/master.md` with your own canon and `_assets/cast/character_profiles.json` with your own characters, then adjust the skills to your aesthetic. Your universe's gate constants — the mandatory suffixes, forbidden aesthetics, and anti-spawn guard — live in one place, `tests/universe_config.py`; re-point them there so the validation gate follows your fork instead of demanding the ROBOTIKO defaults. The how-to-fork details are in **[../CONTRIBUTING.md](../CONTRIBUTING.md)**.

**One more — how is YouTube metadata supposed to look?**
The packager skill follows a fixed house style: title format, description signal lines, tag strategy, and category. The standard is documented in **[../\_management/youtube_metadata_standards.md](../_management/youtube_metadata_standards.md)**; review it before any upload.

---

*The Moon has no light of its own. But in reflecting the Sun, it illuminates the night.*
