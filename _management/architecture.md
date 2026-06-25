# SYSTEM ARCHITECTURE
> **Version:** 2.1 | **Last Updated:** 2026-06-11
>
> **v2.1 changelog:** Binary storage moved from the earlier S3 plan to **local disk + Google Drive via the custom MCP server** (`_tools/mcp-gdrive/`). Toolchain refreshed (Suno + BandLab, Nano Banana, Kling / Veo / Seedance 1.0, CapCut). Enforcement layer documented as a first-class subsystem: `tests/` validators + Claude Code PostToolUse naming hook + naming convention + GitHub Actions. The two human approval gates are now first-class architectural elements.

This is a **repo-as-studio**: a single git repository that operates as a complete film-production company for one person. Claude (via Claude Code) acts as a stage-gated production crew; the human keeps exactly two irreplaceable powers — creative vision (the inputs) and taste (two approval gates). Every stage is traceable: **Output of Step N = Input of Step N+1.**

---

## 1. TECHNICAL STACK

| Layer | Tool | Role |
|---|---|---|
| **Version Control** | GitHub | The brain — text, decisions, and full history of every creative choice |
| **Binary Storage** | Local disk + Google Drive (custom MCP server) | Heavy assets (PNG, MP4, WAV) live locally and are archived to Google Drive via `_tools/mcp-gdrive/`. Git never stores raw binaries. |
| **Automation** | GitHub Actions + Python scripts | Episode scaffolding, naming validation, pipeline integrity |
| **Enforcement** | `tests/` validators + Claude Code PostToolUse hook | Naming, visual-prompt, and pipeline-integrity checks |
| **LLM Director / Crew** | Claude (Opus) via Claude Code + VSCode | Dramaturgy, visual prompts, motion scripts, packaging, skill execution |
| **Music Generation** | Suno (generation) + BandLab (mastering) | Audio production |
| **Musical Metadata** | Claude (`robotiko-musical-metadata` skill) | Metadata JSON from human-provided BPM, key, and timestamped lyrics |
| **Image Generation** | Nano Banana | Visual-prompt execution |
| **Video Generation** | Kling (2.5 Turbo / 3.0 Elements / Omni), Veo, Seedance 1.0 | Motion production |
| **Editing** | CapCut | Final assembly (LUT + grain + 2.35:1 letterbox unification protocol) |

---

## 2. DATA FLOW (THE PIPELINE DAG)

```
   [ HUMAN: Lyrics + Vision ]
              │
              ▼
   LYRICS  ──►  MUSIC                     (Suno generation + BandLab mastering)
                  │
                  ▼
        MUSICAL METADATA JSON             (Claude · robotiko-musical-metadata)
        ── temporal source of truth ──    tempo · key · sections[] {start,end,energy,lyrics}
                  │
                  ▼
        CONCEPT NOTES                      (human must-haves / overrides)
                  │
                  ▼
        DRAMATURGY ════════════════════►  ✋ HUMAN GATE 1  (approve scene breakdown)
                  │                            (Claude · robotiko-dramaturgy)
                  ▼
        VISUAL PROMPTS                     (Claude · robotiko-visual-prompts + mandatory suffix)
                  │
                  ▼
        IMAGE GEN                          (Nano Banana → 04_visuals/raw/)
                  │
                  ▼
        IMAGE SELECT                       (human curates → 04_visuals/selected/)
                  │
                  ▼
        MOTION SCRIPT ══════════════════►  ✋ HUMAN GATE 2  (approve camera + tool assignment)
                  │                            (Claude · robotiko-motion-script)
                  ▼
        VIDEO GEN                          (Kling / Veo / Seedance 1.0 → 05_video/raw/)
                  │
                  ▼
        VIDEO SELECT                       (human curates → 05_video/selected/)
                  │
                  ▼
        CAPCUT EDIT                        (Claude · robotiko-capcut-editor guide → 06_edit/)
                  │
                  ▼
        YOUTUBE PACKAGE                    (Claude · robotiko-youtube-packager
                  │                          per youtube_metadata_standards.md)
                  ▼
        LAUNCH                             (Claude · robotiko-launch-orchestrator)
                  │
                  ▼
        SOCIAL                             (Claude · robotiko-reels-atomizer → 07_social_media/)
```

### The Musical Metadata JSON is the temporal source of truth

```
Human listens to audio + finds BPM/Key (vocalremover.org) + timestamps lyrics
    → Claude (robotiko-musical-metadata skill)
    → ep{XX}_musical_metadata.json
        ├── tempo, key, time_signature
        ├── mood[], instruments[]
        └── sections[] { type, start, end, energy, lyrics, notes }
```

Every scene, every visual, and every camera move is anchored to this JSON's timeline. The pipeline does not advance past metadata without it.

### The Two Human Gates (first-class architecture)

The DAG has exactly two blocking edges. Everything else Claude executes and delivers autonomously.

| Gate | Position | Human reviews | Why it is irreplaceable |
|---|---|---|---|
| **GATE 1** | After Dramaturgy, before Visual Prompts | Scene breakdown, tone, station fidelity | Taste on narrative structure cannot be delegated |
| **GATE 2** | After Motion Script, before Video Gen | Camera moves, tech strategy, tool/Element assignment | Video generation is the most expensive stage — approve before spend |

---

## 3. REPOSITORY STRUCTURE

```
robotiko-v2/
│
├── CLAUDE.md                       # Claude's role & context (auto-read every session)
├── README.md  AUTHOR.md  CONTRIBUTING.md
├── LICENSE  LICENSE-CONTENT        # MIT (method) + CC BY-NC 4.0 (creative content)
│
├── _management/                    # CONSTITUTION — source of truth
│   ├── master.md                   # Universe Canon — THE LAW
│   ├── pipeline_rules.md           # Production workflow + quality gates
│   ├── naming_convention.md        # File naming standards (the pipeline's foreign keys)
│   ├── architecture.md             # This document
│   ├── youtube_metadata_standards.md
│   └── project_metadata.json       # State — episode status + toolchain + MCP config
│
├── _assets/                        # STATE — reusable creative assets
│   ├── cast/
│   │   ├── character_profiles.json # Character visual state machine (per-phase)
│   │   ├── ref_robotiko_master.png
│   │   └── ref_mentor_master.png
│   └── style/visual_dna.md
│
├── _templates/                     # Episode scaffolding templates
│   ├── dramaturgy_template.md
│   ├── visual_prompt_template.md
│   └── video_prompt_template.md
│
├── _skills/                        # WORKFLOWS — 10 SKILL.md runbooks (the crew)
│   ├── robotiko-musical-metadata/
│   ├── robotiko-dramaturgy/
│   ├── robotiko-visual-prompts/
│   ├── robotiko-motion-script/
│   ├── robotiko-episode-scaffold/
│   ├── robotiko-naming-enforcer/
│   ├── robotiko-youtube-packager/
│   ├── robotiko-reels-atomizer/
│   ├── robotiko-launch-orchestrator/
│   └── robotiko-capcut-editor/     # (each: SKILL.md + CHANGELOG.md)
│
├── _memory/                        # MEMORY — cross-session continuity
│   ├── lessons.md                  # Tested, self-improvement rules
│   ├── decisions_log.md            # Architectural decision record
│   └── todo.md                     # Open tasks + session summaries
│
├── _tools/
│   └── mcp-gdrive/                 # Custom Google Drive MCP server (binary archive)
│       ├── src/index.js            # ~300 lines, 2 deps (googleapis, MCP SDK)
│       └── README.md
│
├── docs/                           # Public onboarding
│   ├── getting-started.md
│   ├── skills-guide.md
│   ├── tools-setup.md
│   └── anatomy-of-an-episode.md
│
├── scripts/
│   └── create_episode.py           # Episode scaffolding
│
├── tests/                          # ENFORCEMENT — CI / QA validators
│   ├── naming_check.py
│   ├── pipeline_integrity.py
│   ├── visual_prompt_validator.py
│   ├── naming_check_hook.py        # Lightweight PostToolUse hook helper
│   └── README.md
│
├── .claude/
│   └── settings.json               # PostToolUse naming hook (Write matcher)
│
├── .github/
│   ├── workflows/create_episode.yml
│   ├── ISSUE_TEMPLATE/  pull_request_template.md
│
└── episode-01/ … episode-10/
    ├── 01_lyrics/      ep{XX}_lyrics_v{VV}.md
    ├── 02_music/       ep{XX}_musical_metadata.json   (+ *.wav → gitignored, Drive)
    ├── 03_direction/   ep{XX}_concept_notes.md  ep{XX}_dramaturgy_v{VV}.md
    ├── 04_visuals/     ep{XX}_visual_prompts_v{VV}.md  raw/  selected/   (raw+selected gitignored)
    ├── 05_video/       ep{XX}_motion_script_v{VV}.md   raw/  selected/   (raw+selected gitignored)
    ├── 06_edit/        ep{XX}_capcut_guide_v{VV}.md    (+ *.mp4 → gitignored, Drive)
    └── 07_social_media/ stills/  reels/
```

---

## 4. BINARY / TEXT SEPARATION (replaces the earlier S3 plan)

Git is the **text brain**; Google Drive is the **binary archive**. There is no S3 in this architecture.

```
   TEXT (tracked in Git)                       BINARY (local + Google Drive)
   ─────────────────────                       ─────────────────────────────
   lyrics, metadata JSON,                       *.wav audio
   concept notes, dramaturgy,           ◄──►    raw images (all variants)
   visual prompts, motion scripts,              selected images (curated)
   capcut guides, management docs,              raw + selected video clips
   skills, tests, scripts                       final episode MP4
```

- **Tracked:** all text, plus curated *selections* are referenced by name (the naming convention is the foreign key linking a tracked motion script to its Drive-stored clip).
- **Gitignored raw folders:** `episode-*/04_visuals/raw/`, `episode-*/04_visuals/selected/`, `episode-*/05_video/raw/`, `episode-*/05_video/selected/`, and `episode-*/02_music/*.wav|*.mp3`, plus `*.mp4 *.mov *.png(4k/8k) *.psd`.
- **Archive path:** binaries are uploaded to Google Drive through the custom MCP server. Drive layout mirrors the repo: `robotiko-v2/ep{XX}/{raw,selected,audio,video}/`.

### The Google Drive MCP server (`_tools/mcp-gdrive/`)

Custom, no third-party MCP packages. Configured via `.mcp.json` at project root. OAuth credentials/tokens live in `~/.config/` (never in the repo).

| MCP Tool | Capability |
|---|---|
| `gdrive_list_folder` | Browse Drive folder contents |
| `gdrive_search` | Find files by name / MIME type |
| `gdrive_create_folder` | Create folders |
| `gdrive_upload` | Upload local PNG / MP4 / WAV |
| `gdrive_move` | Move files between folders |

---

## 5. THE FIVE SUBSYSTEMS

The repo is one machine with five cooperating subsystems. Each maps to a directory.

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. CONSTITUTION   _management/master.md + golden rules + mandatory suffixes│
│    The law. Read first, every session. Defines tone, character arc,        │
│    cultural attribution, and the two non-negotiable visual/video suffixes. │
├─────────────────────────────────────────────────────────────────────────┤
│ 2. WORKFLOWS      _skills/  — 10 SKILL.md runbooks                          │
│    The crew. Each skill is a deterministic runbook Claude reads before     │
│    acting: musical-metadata, dramaturgy, visual-prompts, motion-script,    │
│    episode-scaffold, naming-enforcer, youtube-packager, reels-atomizer,    │
│    launch-orchestrator, capcut-editor.                                     │
├─────────────────────────────────────────────────────────────────────────┤
│ 3. MEMORY         _memory/lessons.md + decisions_log.md + todo.md          │
│    Continuity across sessions. lessons.md = tested rules that prevent      │
│    repeat mistakes; decisions_log = architecture decisions; todo = tasks.  │
├─────────────────────────────────────────────────────────────────────────┤
│ 4. STATE          _assets/cast/character_profiles.json +                   │
│                   _management/project_metadata.json                        │
│    character_profiles.json = the character visual state machine (which     │
│    phase/damage applies to a given episode). project_metadata.json =       │
│    episode status, toolchain, MCP config, global render settings.          │
├─────────────────────────────────────────────────────────────────────────┤
│ 5. ENFORCEMENT    tests/ + Claude Code PostToolUse hook + naming           │
│                   convention + GitHub Actions                              │
│    Guards correctness: naming_check.py, visual_prompt_validator.py,        │
│    pipeline_integrity.py; the .claude/settings.json PostToolUse hook warns │
│    on non-conforming filenames at write time; create_episode.yml scaffolds │
│    in CI. naming_convention.md is the contract all of these enforce.       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. ENFORCEMENT LAYER (detail)

Three layers catch errors at different moments:

| When | Mechanism | Checks |
|---|---|---|
| **At write time** | Claude Code PostToolUse hook (`.claude/settings.json`, Write matcher) | Warns immediately if a file written under `episode-XX/` breaks the naming convention |
| **On demand / pre-publish** | `tests/run_all.py` (one command) | `naming_check.py` (filename patterns + episode-number consistency); `visual_prompt_validator.py` (mandatory suffix, forbidden aesthetics, per-episode character-phase with subject-guard + whitelist, and metadata-based **reference integrity**); `pipeline_integrity.py` (no skipped steps / missing gate outputs); `test_validators.py` (grade-the-graders meta-tests) |
| **In CI** | GitHub Actions (`.github/workflows/`) | `create_episode.yml` scaffolds episodes on dispatch; `validation_suite.yml` runs the single gate `tests/run_all.py` on every push and pull request, blocking on failure (Python + action SHAs pinned) |

The contract is `_management/naming_convention.md` (naming) and the
[`adr/`](adr/) + [`invariant_coverage_matrix.md`](invariant_coverage_matrix.md)
records (validation backbone).

---

## 7. CLAUDE CODE INTEGRATION

- Claude Code runs in VSCode's integrated terminal. `CLAUDE.md` is auto-read every session, so Claude has full project context immediately.
- **Skill execution:** human says a trigger phrase → Claude reads `_skills/{skill}/SKILL.md` → executes → commits output.
- **File operations:** Claude reads, writes, and commits directly — no manual copy-paste.
- **Binary archive:** Claude uploads curated assets to Google Drive through the MCP server.
- **Guardrails:** the PostToolUse naming hook fires on every Write; the golden rules and mandatory suffixes in `CLAUDE.md` / `master.md` constrain every creative output.

---

## 8. OPEN SOURCE

The full method — pipeline, skills, templates, tests, MCP server, management docs — is open source.

- **Software & method** (skills, scripts, tests, MCP server, templates, process docs): **MIT** (`LICENSE`).
- **Creative content** (lyrics, dramaturgy, the ROBOTIKO universe, character designs): **CC BY-NC 4.0** (`LICENSE-CONTENT`).

**What a fork inherits:** a complete, traceable AI-assisted production pipeline; 10 reusable skill definitions; `CLAUDE.md` + management docs as templates; the enforcement layer; the proof of concept — one human plus a crew of machines producing a 10-episode series. Take the method, build your own universe.
