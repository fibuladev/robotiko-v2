# SYSTEM ARCHITECTURE
> **Version:** 3.0 | **Last Updated:** 2026-07-05
>
> **v3.0 (2026-07-05):** document matches repository reality 1:1; dead hook references removed. Enforcement is now described as its actual two-layer reality — a local one-gate command `python tests/run_all.py` and the CI workflow `.github/workflows/validation_suite.yml`, both running the identical entrypoint. A write-time Claude Code PostToolUse naming hook (`tests/naming_check_hook.py` + a `.claude/settings.json` Write matcher) existed and was removed 2026-07-04 after proving inert — it never fired — so enforcement is consolidated in CI.
> **v2.1 (2026-06-11):** Binary storage moved from the earlier S3 plan to **local disk + Google Drive via the custom MCP server** (`_tools/mcp-gdrive/`). Toolchain refreshed (Suno + BandLab, Nano Banana, Kling / Veo / Seedance 1.0, CapCut). Enforcement layer documented as a first-class subsystem. The two human approval gates are now first-class architectural elements.

This is a **repo-as-studio**: a single git repository that operates as a complete film-production company for one person. Claude (via Claude Code) acts as a stage-gated production crew; the human keeps exactly two irreplaceable powers — creative vision (the inputs) and taste (two approval gates). Every stage is traceable: **Output of Step N = Input of Step N+1.**

---

## 1. TECHNICAL STACK

| Layer | Tool | Role |
|---|---|---|
| **Version Control** | GitHub | The brain — text, decisions, and full history of every creative choice |
| **Binary Storage** | Local disk + Google Drive (custom MCP server) | Heavy assets (PNG, MP4, WAV) live locally and are archived to Google Drive via `_tools/mcp-gdrive/`. Git never stores raw binaries. |
| **Automation** | GitHub Actions + Python scripts | Episode scaffolding, naming validation, pipeline integrity |
| **Enforcement** | `tests/` validators behind one gate (`python tests/run_all.py`), run in CI by `validation_suite.yml` | Naming, visual-prompt, pipeline-integrity, hygiene, metadata, motion, character, and meta-test checks |
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

### Pipeline state (episode lifecycle)

An episode advances through a fixed sequence of stages, each producing the input for the next:

```
scaffold → lyrics / music → concept notes → dramaturgy [HUMAN GATE 1]
   → visual prompts → images → motion script [HUMAN GATE 2]
   → video → edit → launch → social
```

The two human gates are **gated by design, not gaps**: they are deliberate points where a person applies taste, not missing automation. Today the gate crossing is a human act of approval that Claude honors procedurally (per `pipeline_rules.md`) rather than a machine-recorded token — the invariant-coverage matrix lists both checkpoints under "gated by design." Machine linkage of approvals (a recorded, checkable approval artifact per gate) is on the roadmap, not yet built.

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
│   ├── invariant_coverage_matrix.md # What is Machine / Heuristic / Human / Gap enforced
│   ├── case_study_validation_backbone.md
│   ├── adr/                        # Architecture Decision Records (0001–0007 + README)
│   ├── README.md
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
│   ├── create_episode.py           # Episode scaffolding
│   ├── select_images.py            # Curate raw → selected (visuals)
│   └── select_videos.py            # Curate raw → selected (video)
│
├── tests/                          # ENFORCEMENT — CI / QA validators (stdlib only)
│   ├── run_all.py                  # THE ONE GATE — runs all 9 check groups, non-zero on any fail
│   ├── naming_check.py             # Filename patterns + episode-number consistency
│   ├── pipeline_integrity.py       # No silently-skipped pipeline steps
│   ├── visual_prompt_validator.py  # Suffix · forbidden aesthetics · character phase · ref integrity
│   ├── prompt_hygiene_lint.py      # Scoped — model-facing prompt strings must be plain-English ASCII
│   ├── musical_metadata_validator.py # JSON structure · vocabulary · timestamps · total_duration
│   ├── motion_script_validator.py  # Video suffix · anti-spawn guard · camera diversity quotas
│   ├── character_profiles_validator.py # Structural validation against character_profiles.schema.json
│   ├── test_validators.py          # 41 grade-the-graders meta-tests
│   ├── fixtures/                   # Frozen BROKEN/GOOD regression pair + README.md
│   └── README.md
│
├── .claude/
│   └── settings.json               # Session config (model). No hook — removed 2026-07-04 (never fired)
│
├── .github/
│   ├── workflows/
│   │   ├── validation_suite.yml    # CI gate: runs `python tests/run_all.py` on every push / PR
│   │   └── create_episode.yml      # Episode scaffolding on workflow_dispatch
│   ├── ISSUE_TEMPLATE/             # bug_report.md  feature_request.md
│   └── pull_request_template.md
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
│ 5. ENFORCEMENT    tests/ (one gate) + naming convention + GitHub Actions   │
│    Guards correctness. `python tests/run_all.py` runs 9 check groups        │
│    (naming, pipeline integrity, visual prompts, prompt hygiene, musical     │
│    metadata, motion script, character profiles, meta-tests). CI runs the    │
│    identical command via validation_suite.yml and blocks the merge on red;  │
│    create_episode.yml scaffolds episodes on dispatch. naming_convention.md  │
│    is the contract these enforce. (A write-time naming hook was removed     │
│    2026-07-04 after proving inert — enforcement lives in CI.)               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. ENFORCEMENT LAYER (detail)

Enforcement is **two layers running one identical entrypoint** — the local pre-push
check and CI are the same command, so a green terminal predicts a green pipeline:

| When | Mechanism | Checks |
|---|---|---|
| **Locally, before you push** | `python tests/run_all.py` (one gate) | Runs all 9 check groups below in sequence; exits non-zero if any fails. Standard-library only — no `pip install`. |
| **In CI** | GitHub Actions — [`.github/workflows/validation_suite.yml`](../.github/workflows/validation_suite.yml) | Runs the identical `python tests/run_all.py` on every push and pull request, blocking the merge on failure (Python + action SHAs pinned). [`create_episode.yml`](../.github/workflows/create_episode.yml) scaffolds episodes on `workflow_dispatch`. |

**Historical note:** a write-time Claude Code PostToolUse naming hook
(`tests/naming_check_hook.py` wired through a `.claude/settings.json` Write matcher) <!-- doc-ref: ignore -->
once formed a third, earlier layer. It was removed 2026-07-04 after proving inert —
it never fired — and enforcement was consolidated into the single CI gate. The doc no
longer describes it as live.

### The validation backbone

`tests/run_all.py` is the whole gate. It runs **9 check groups**:

1. **Naming convention** — `naming_check.py --full` (filename patterns + episode-number consistency; 85 checks)
2. **Pipeline integrity** — `pipeline_integrity.py --full` (no silently-skipped steps / missing gate outputs)
3. **Visual prompt sweep** — `visual_prompt_validator.py --full` (mandatory suffix, forbidden aesthetics, per-episode character-phase with subject-guard + whitelist, and metadata-based **reference integrity**)
4. **Prompt hygiene** — `prompt_hygiene_lint.py --full` (scoped: model-facing prompt strings must be plain-English ASCII; deliberately never reads canon)
5. **Musical metadata** — `musical_metadata_validator.py --full` (JSON structure, energy/type vocabulary, timestamp monotonicity, total_duration match)
6. **Motion script** — `motion_script_validator.py --full` (video suffix, anti-spawn guard, camera diversity quotas)
7. **Character profiles** — `character_profiles_validator.py --full` (structural validation against `_assets/cast/character_profiles.schema.json`)
8. **Validator meta-tests** — `test_validators.py` — **55 grade-the-graders tests**: the suite must FAIL the frozen BROKEN fixture and PASS the GOOD one, every loosening proven in both directions, plus a parser-coverage guard against the zero-scene false-green
9. **Doc reference integrity** — `doc_reference_check.py` (backtick-quoted repo paths in load-bearing docs must exist on disk; present-tense claims about removed components fail; coverage matrix stays in sync with the `check_` functions that exist)

A green run certifies only the machine-checked invariants. The
[`invariant_coverage_matrix.md`](invariant_coverage_matrix.md) is the honesty ledger,
tiering every invariant as **Machine** (mechanically checked, CI blocks),
**Heuristic** (advisory, can over/under-fire), **Human** (gated at a checkpoint), or
**Gap** (cared about, no automated check yet). The reasoning behind the backbone lives
in the [`adr/`](adr/) records (0001–0007).

The contract is `_management/naming_convention.md` (naming) and the
[`adr/`](adr/) + [`invariant_coverage_matrix.md`](invariant_coverage_matrix.md)
records (validation backbone).

---

## 7. CLAUDE CODE INTEGRATION

- Claude Code runs in VSCode's integrated terminal. `CLAUDE.md` is auto-read every session, so Claude has full project context immediately.
- **Skill execution:** human says a trigger phrase → Claude reads `_skills/{skill}/SKILL.md` → executes → commits output.
- **File operations:** Claude reads, writes, and commits directly — no manual copy-paste.
- **Binary archive:** Claude uploads curated assets to Google Drive through the MCP server.
- **Guardrails:** `python tests/run_all.py` is the pre-push gate (and the identical CI gate); the golden rules and mandatory suffixes in `CLAUDE.md` / `master.md` constrain every creative output.

---

## 8. OPEN SOURCE

The full method — pipeline, skills, templates, tests, MCP server, management docs — is open source.

- **Software & method** (skills, scripts, tests, MCP server, templates, process docs): **MIT** (`LICENSE`).
- **Creative content** (lyrics, dramaturgy, the ROBOTIKO universe, character designs): **CC BY-NC 4.0** (`LICENSE-CONTENT`).

**What a fork inherits:** a complete, traceable AI-assisted production pipeline; 10 reusable skill definitions; `CLAUDE.md` + management docs as templates; the enforcement layer; the proof of concept — one human plus a crew of machines producing a 10-episode series. Take the method, build your own universe.

---

## Binary Asset Resilience

Rendered assets (images, video clips, audio files, final edits) are gitignored — they live on Google Drive via the MCP server, not in the repository. Binary backup and disaster recovery is the operator's responsibility, not the pipeline's scope.

The project maintainer runs a 3-copy / 2-media / 2-account setup (production Drive + personal Drive mirror on a separate Google account + portable physical disk). Fork operators should establish their own equivalent. The pipeline produces recipes and paper trails; the operator stores the renders.
