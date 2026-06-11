# Skills Guide

> How ROBOTIKO v2.0 turns a repository into a film studio.

This repo is a **studio, not just a folder**. The crew is Claude, working inside Claude Code. The crew's
job descriptions live in `_skills/` — ten `SKILL.md` files, each a precise runbook for one stage of the
pipeline. Read this guide to understand what a skill is, how one is built, what each of the ten does, and
how a single trigger phrase walks an episode from music to a stage-gated, reviewable deliverable.

Related reading: [`../_skills/README.md`](../_skills/README.md) for the short index,
[`../_management/pipeline_rules.md`](../_management/pipeline_rules.md) for the full pipeline and the two
human gates, and [`../CLAUDE.md`](../CLAUDE.md) for the trigger-phrase table the crew obeys at session start.

---

## 1. What a Skill Is

A skill is a **declarative runbook** — a single `SKILL.md` file that Claude reads *before* it does any work.
It is not code that runs. It is a contract the crew agrees to follow, written in plain Markdown so a human
can audit it as easily as the model can execute it.

Each skill answers four questions before a single line of output is written:

- **Trigger** — the exact phrase a human types to start the stage (e.g. `"Create dramaturgy for EP05"`).
- **Mandatory inputs** — the files that must be read, in order, before generating anything. No guessing,
  no improvising from memory.
- **STOP / gate conditions** — the conditions under which the crew must halt and ask the human, rather than
  proceed on partial or unapproved inputs.
- **Post-generation checklist** — the self-review the crew runs against its own output before declaring the
  stage done.

Because every stage is pinned to a written runbook, the pipeline becomes **deterministic and reviewable**.
The same trigger produces the same shape of output every time, anchored to the same source files, halted by
the same gates. A reviewer never has to wonder *how* a deliverable was made — the SKILL.md is the method,
checked into git alongside the result.

> A skill makes the crew's judgment legible. The story stays human; the execution becomes repeatable.

---

## 2. Anatomy of a SKILL.md

Every skill follows the same skeleton. Below, each section is illustrated with real excerpts from
[`../_skills/robotiko-dramaturgy/SKILL.md`](../_skills/robotiko-dramaturgy/SKILL.md), the heart of the
direction phase.

### Header — Version / Trigger / Output

The first four lines pin the skill's identity. The trigger is the activation phrase; the output line names
the exact file the stage must produce.

```
# SKILL: robotiko-dramaturgy
> Version: 1.0 | Last Updated: 2026-02-24
> Trigger: "Create dramaturgy for EP{XX}"
> Output: episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md
```

### Purpose

A short paragraph stating the stage's reason to exist and where it sits between neighbours. Dramaturgy
defines itself as the bridge between two worlds:

> Generate a scene-by-scene dramaturgy document that maps the visual narrative of an episode to its musical
> structure. The dramaturgy is the bridge between the music (temporal skeleton) and the visuals (spatial
> expression).

### Prerequisite / STOP conditions

The hard line the crew cannot cross. Dramaturgy's mandatory-inputs block ends with an explicit halt:

> If any of inputs 1-4 are missing: STOP. Inform the human. Do not proceed with partial inputs.

Other skills gate on *approval* rather than mere presence — visual-prompts will not run until the dramaturgy
is human-approved, motion-script requires both an approved dramaturgy and selected images, and the
distribution skills require a finished final edit. The STOP is what keeps the pipeline honest.

### Mandatory Inputs table

A numbered table of every file to read, in order, and what to extract from each. This is the stage's
dependency graph made explicit:

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/master.md` | Episode arc, station, tone, key lyrics, character phases, philosophical context |
| 2 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Sections, timestamps, energy levels, mood, instruments, lyrics |
| 3 | `episode-{XX}/03_direction/ep{XX}_concept_notes.md` | Human must-have shots, creative overrides, specific requests |
| 4 | `_assets/cast/character_profiles.json` | Character visual state for this episode's phase |
| 5 | `_templates/dramaturgy_template.md` | Output structure and formatting template |

### Output Structure

The exact shape of the deliverable — for dramaturgy, an ordered document: Episode Header, Musical Structure
Summary, the core **Scene Breakdown Table** (Shot ID, Timestamp, Visual Description, Mood / Lighting,
Characters, Music Sync, User Override?), Scene Detail Blocks, Director's Notes, and an Approval Status block
of checkboxes. The structure is fixed so downstream skills can read it without surprises.

### Post-Generation Checklist

The crew's self-review before handing off. Dramaturgy's checklist closes the loop:

> - [ ] Every scene has a timestamp anchored to the musical metadata JSON
> - [ ] Character visual state matches the episode's phase (no continuity errors)
> - [ ] All human must-have shots from concept_notes.md are included and marked
> - [ ] No scene uses forbidden aesthetics (clean, sterile, neon cyberpunk, Pixar)
> - [ ] Approval checkboxes are present at the bottom
> - [ ] Ask yourself: "Would Fibula approve this?"

Most skills also carry an **Error Handling** table and a **Versioning** rule (first output is always `v01`;
revisions increment to `v02`, `v03`; each version is a complete document, never a diff).

---

## 3. The Ten Skills

The full crew, in pipeline order. Triggers and outputs are taken verbatim from each
[`../_skills/`](../_skills/) `SKILL.md` header.

| Skill | Trigger phrase | Key inputs | Output |
|---|---|---|---|
| [`robotiko-musical-metadata`](../_skills/robotiko-musical-metadata/SKILL.md) | `"Create musical metadata for EP{XX}"` | Human-provided BPM, key, timestamped lyrics; `master.md` for inference | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` |
| [`robotiko-dramaturgy`](../_skills/robotiko-dramaturgy/SKILL.md) | `"Create dramaturgy for EP{XX}"` | `master.md`, `musical_metadata.json`, `concept_notes.md`, `character_profiles.json` | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` |
| [`robotiko-visual-prompts`](../_skills/robotiko-visual-prompts/SKILL.md) | `"Generate visual prompts for EP{XX}"` | Approved dramaturgy, `master.md`, `character_profiles.json`, master reference images | `episode-{XX}/04_visuals/ep{XX}_visual_prompts_v{VV}.md` |
| [`robotiko-motion-script`](../_skills/robotiko-motion-script/SKILL.md) | `"Generate motion script for EP{XX}"` | Approved dramaturgy, `musical_metadata.json`, selected images, `master.md` | `episode-{XX}/05_video/ep{XX}_motion_script_v{VV}.md` |
| [`robotiko-episode-scaffold`](../_skills/robotiko-episode-scaffold/SKILL.md) | `"Scaffold EP{XX}"` | `architecture.md`, `naming_convention.md`, `project_metadata.json` | Full folder structure under `episode-{XX}/` |
| [`robotiko-naming-enforcer`](../_skills/robotiko-naming-enforcer/SKILL.md) | `"Validate file names"` (or `"Validate file names for EP{XX}"`) | `naming_convention.md` | Compliance report (printed to chat) |
| [`robotiko-youtube-packager`](../_skills/robotiko-youtube-packager/SKILL.md) | `"Package EP{XX} for YouTube"` | `youtube_metadata_standards.md`, `master.md`, `musical_metadata.json`, dramaturgy | `episode-{XX}/07_social_media/ep{XX}_youtube_package.md` |
| [`robotiko-reels-atomizer`](../_skills/robotiko-reels-atomizer/SKILL.md) | `"Atomize EP{XX} for social"` | Dramaturgy, `musical_metadata.json`, `master.md`, motion script | `episode-{XX}/07_social_media/ep{XX}_social_atomization.md` |
| [`robotiko-launch-orchestrator`](../_skills/robotiko-launch-orchestrator/SKILL.md) | `"Orchestrate EP{XX} launch"` | YouTube package, social atomization, `project_metadata.json`, `master.md` | `episode-{XX}/07_social_media/ep{XX}_launch_checklist.md` |
| [`robotiko-capcut-editor`](../_skills/robotiko-capcut-editor/SKILL.md) | `"Edit EP{XX} in CapCut"` | Approved motion script, `musical_metadata.json`, selected video clips, `master.md`, `pipeline_rules.md` | `episode-{XX}/06_edit/ep{XX}_capcut_guide_v{VV}.md` |

A few notes the table can't carry:

- **Storage.** Audio and rendered media are gitignored; large assets live on **Google Drive**, reached
  through the repo's custom Drive MCP. The text deliverables above are what land in git.
- **Image and video tools.** Visual prompts target **Nano Banana**; motion scripts assign per-clip video
  tools (Kling / Veo / Seedance) inside the script itself. The skills produce the *instructions*; the human
  runs the generators.
- **Mechanical vs. creative.** Scaffold and naming-enforcer are mechanical gates run at low effort.
  Dramaturgy and motion-script are single-shot deep syntheses run at maximum effort. The skill files say so;
  the crew obeys.

---

## 4. Worked Example, End to End: `robotiko-dramaturgy`

One stage, start to finish, to show how trigger, inputs, gate, and deliverable fit together.

**1. The human types the trigger.**

```
Create dramaturgy for EP05
```

**2. The crew reads the runbook, then the inputs — in order.**

Claude opens [`../_skills/robotiko-dramaturgy/SKILL.md`](../_skills/robotiko-dramaturgy/SKILL.md) first,
then reads its mandatory inputs exactly as listed:

1. [`../_management/master.md`](../_management/master.md) — the episode's station, arc, tone, character phase.
2. `episode-05/02_music/ep05_musical_metadata.json` — the temporal skeleton: every section, timestamp,
   and energy level the scenes will hang from.
3. `episode-05/03_direction/ep05_concept_notes.md` — the human's must-have shots and overrides.
4. [`../_assets/cast/character_profiles.json`](../_assets/cast/character_profiles.json) — Robotiko's exact
   visual state for this episode's phase, copied into every scene that features him.
5. `_templates/dramaturgy_template.md` — the output shape.

**3. The STOP gate is enforced.**

> If any of inputs 1-4 are missing: STOP. Inform the human. Do not proceed with partial inputs.

If the musical metadata JSON does not exist, the crew halts here — there is no temporal skeleton to anchor
scenes to, so there is nothing honest to generate.

**4. The deliverable is produced.**

The crew writes:

```
episode-05/03_direction/ep05_dramaturgy_v01.md
```

A complete document: Episode Header, Musical Structure Summary, the Scene Breakdown Table (each row anchored
to a timestamp from the metadata JSON), Scene Detail Blocks for the complex shots, Director's Notes, and an
Approval Status block. Before handing it over, the crew runs the post-generation checklist against its own
work and asks the project's standing question: *"Would Fibula approve this?"*

**5. The human-approval gate follows.**

Dramaturgy is one of the two mandatory checkpoints. The document is delivered with its approval checkboxes
*unticked*. Nothing downstream moves until a human reviews the scene breakdown and approves it. Only then
does the approved dramaturgy become the primary input to
[`../_skills/robotiko-visual-prompts/SKILL.md`](../_skills/robotiko-visual-prompts/SKILL.md), which converts
each scene row into a standalone Nano Banana image prompt.

> The dramaturgy is the foundation. If it is weak, everything built on it will be weak.

---

## 5. The Two Gates and the Two Suffixes

### Two mandatory human gates

Two stages — and only two — require explicit human approval before the pipeline may continue. Everything
else the crew executes and delivers autonomously. Per
[`../_management/pipeline_rules.md`](../_management/pipeline_rules.md):

1. **After Dramaturgy** — the human reviews and approves the scene breakdown before any visual work begins.
2. **After Motion Script** — the human reviews camera moves, tool assignments, and video strategy before any
   video is generated.

These gates are where human authorship is asserted. The crew can propose an entire episode's direction in
one pass, but it cannot greenlight itself.

### Two mandatory suffixes

Every creative skill enforces a fixed style suffix so output stays visually coherent across hundreds of
prompts and ten episodes. They are appended verbatim — no edits, no omissions.

**Visual suffix** (appended to every image prompt):

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

**Video suffix** (appended to every motion prompt):

```
Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.
```

The gates protect the story. The suffixes protect the look. Together they are why a repository full of
Markdown can behave like a studio with a house style — and why every frame, however it was generated, still
belongs to the same film.
