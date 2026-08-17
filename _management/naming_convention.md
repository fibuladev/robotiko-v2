# FILE NAMING CONVENTION
> **Version:** 2.1
> All files in this project must follow this convention without exception.
> The `robotiko-naming-enforcer` skill validates compliance automatically.

---

## GENERAL FORMAT

```
ep{EPISODE_NUMBER}_{TYPE}_v{VERSION}.{EXTENSION}
```

For scene-specific files:
```
ep{EPISODE_NUMBER}_s{SCENE_NUMBER}_{TYPE}_v{VERSION}.{EXTENSION}
```

---

## DEFINITIONS

| Field | Format | Examples |
|---|---|---|
| `EPISODE_NUMBER` | Always 2 digits | `01`, `02`, `10` |
| `SCENE_NUMBER` | Always 2 digits | `01`, `12`, `35` |
| `VERSION` | Always 2 digits, prefixed with `v` | `v01`, `v02`, `v03` |
| `TYPE` | Lowercase, descriptive | See table below |
| `EXTENSION` | Lowercase | `.md`, `.json`, `.png`, `.mp4`, `.mp3` |

---

## FILE TYPE REFERENCE

| File Type | Naming Pattern | Example |
|---|---|---|
| Lyrics | `ep{XX}_lyrics_v{XX}.md` | `ep03_lyrics_v01.md` |
| Musical Metadata JSON | `ep{XX}_musical_metadata.json` | `ep02_musical_metadata.json` |
| Concept Notes | `ep{XX}_concept_notes.md` | `ep03_concept_notes.md` |
| Dramaturgy | `ep{XX}_dramaturgy_v{XX}.md` | `ep03_dramaturgy_v02.md` |
| Visual Prompts | `ep{XX}_visual_prompts_v{XX}.md` | `ep03_visual_prompts_v01.md` |
| Motion Script | `ep{XX}_motion_script_v{XX}.md` | `ep03_motion_script_v01.md` |
| Raw Image | `ep{XX}_s{XX}_v{XX}.png` | `ep03_s01_v04.png` |
| Selected Image | `ep{XX}_s{XX}_selected.png` | `ep03_s01_selected.png` |
| Reference Image (per-episode env/body, two-phase) | `ep{XX}_ref_{name}.png` | `ep10_ref_market_edge.png` |
| Raw Video | `ep{XX}_s{XX}_video_{tool}.mp4` | `ep03_s01_video_kling.mp4` |
| Raw Video (sub-clip) | `ep{XX}_s{XX}{a\|b\|c\|d}_video_{tool}.mp4` | `ep02_s29c_video_kling.mp4` |
| Selected Video | `ep{XX}_s{XX}_selected.mp4` | `ep03_s01_selected.mp4` |
| Selected Video (sub-clip) | `ep{XX}_s{XX}{a\|b\|c\|d}_selected.mp4` | `ep02_s29c_selected.mp4` |
| Supplementary Image | `ep{XX}_s{XX}{a\|b\|c\|d}_selected.png` | `ep02_s29c_selected.png` |
| Audio File | `ep{XX}_audio_v{XX}.mp3` | `ep02_audio_v01.mp3` |
| Final Edit | `ep{XX}_final_v{XX}.mp4` | `ep02_final_v01.mp4` |
| PDF Export (of a text deliverable) | `ep{XX}_{lyrics\|visual_prompts\|motion_script\|dramaturgy}_v{XX}.pdf` (the `_v{XX}` is optional) | `ep01_visual_prompts_v01.pdf` |
| Episode Manifest (fixed name) | `MANIFEST.md` | `episode-01/MANIFEST.md` |

### Edit, packaging & social deliverables (`06_edit/`, `07_social_media/`)

| File Type | Naming Pattern | Example |
|---|---|---|
| CapCut Guide | `ep{XX}_capcut_guide_v{XX}.md` | `ep07_capcut_guide_v01.md` |
| Sync-QC Record | `ep{XX}_sync_qc_v{XX}.md` | `ep09_sync_qc_v01.md` |
| YouTube Package | `ep{XX}_youtube_package.md` | `ep07_youtube_package.md` |
| Social Atomization | `ep{XX}_social_atomization.md` | `ep02_social_atomization.md` |
| Launch Checklist | `ep{XX}_launch_checklist.md` | `ep01_launch_checklist.md` |
| Walkthrough | `ep{XX}_walkthrough.md` | `ep01_walkthrough.md` |
| External Promotion | `ep{XX}_external_promotion.md` | `ep09_external_promotion.md` |
| Direction Brief (one-off) | `ep{XX}_{topic}_brief.md` | `ep05_visual_prompt_generation_brief.md` |

> **Legacy note:** EP01 (the first episode) predates strict versioning and uses a
> few unversioned forms (`ep01_lyrics.md`). These are accepted by the validator for
> backward compatibility; all new files use the versioned forms above. EP01's original
> pre-pipeline working documents were personal PDFs, kept private (not in the public repo).

> **Two-phase reference images (EP10 onward):** Per-episode environment and
> body-state reference images live in `episode-{XX}/04_visuals/raw/` as
> `ep{XX}_ref_{name}.png` (e.g. `episode-10/04_visuals/raw/ep10_ref_lane.png`).
> These are the Phase-1 reference set the human generates and approves at gate 1R,
> before any scene prompt is written (see `_skills/robotiko-visual-prompts/SKILL.md`
> and `pipeline_rules.md` Step 5a). Shared cast **master** refs instead use
> `_assets/cast/ref_{character}_master.png` (see Asset Files below).
>
> **Enforcement is limited, and honestly so:** `raw/` is gitignored and is never
> walked by `naming_check.py`, so these on-disk filenames are not CI-checked. The
> only CI-visible guard is the Reference-Image-Path field lint (`check_ref_image_path`
> in `tests/visual_prompt_validator.py`) on the tracked
> `ep{XX}_visual_prompts_v{XX}.md`, which requires each `### REF` block's declared
> path to match `episode-{XX}/04_visuals/[raw/]ep{XX}_ref_{name}.png` with the path's
> episode number matching the folder.

---

## MANAGEMENT FILES (Fixed Names — No Versioning in Filename)

These files live in `_management/` and are versioned via Git, not filename:

| File | Purpose |
|---|---|
| `README.md` | Folder guide — what each canon file is for |
| `master.md` | Universe Canon — absolute source of truth |
| `pipeline_rules.md` | Production workflow |
| `naming_convention.md` | This document |
| `architecture.md` | Technical stack & data flow |
| `project_metadata.json` | Episode status tracker |
| `approvals.json` | Human-approval ledger for the pipeline gates (1, 1R, 2) |
| `cost.md` | Full production cost disclosure |
| `dissonance_registry.md` | Ledger of sanctioned visual-vs-music DISSONANCE moments |
| `invariant_coverage_matrix.md` | What the machine guarantees vs. what a human still checks |
| `case_study_validation_backbone.md` | Case study — how the EP09 bug became the validation backbone |
| `youtube_metadata_standards.md` | Upload standard: category, title, description, thumbnail |
| `adr/` | Architecture Decision Records (`NNNN-slug.md`, plus `README.md`) |

---

## SKILL FILES (Fixed Names)

Each skill lives in its own folder under `_skills/`:
```
_skills/{skill-name}/SKILL.md
_skills/{skill-name}/CHANGELOG.md
```

Example:
```
_skills/robotiko-dramaturgy/SKILL.md
_skills/robotiko-dramaturgy/CHANGELOG.md
```

---

## ASSET FILES

```
_assets/cast/ref_{character}_master.png
_assets/cast/character_profiles.json
_assets/style/visual_dna.md
```

Examples:
```
_assets/cast/ref_robotiko_master.png
_assets/cast/ref_mentor_master.png
```

### Curated frames library

Hand-picked stills from finished episodes, used as visual documentation and in
the public-facing docs:

```
_assets/style/frames/ep{XX}/ep{XX}_s{XX}_{slug}.jpg
```

Example: `_assets/style/frames/ep09/ep09_s27_glitch_is_scripture.jpg`

> **Honest note:** `_assets/` is listed in `NON_EPISODE_DIRS` in
> [`tests/naming_check.py`](../tests/naming_check.py), so the validator never walks
> it. This convention — including the `{slug}` — is held by hand, not by CI.

---

## MEMORY FILES

```
_memory/decisions_log.md
```

---

## RULES & ENFORCEMENT

1. **Always two digits** for episode and scene numbers. `ep1` is invalid. `ep01` is correct.
2. **Always two digits** for version numbers. `v1` is invalid. `v01` is correct.
3. **No spaces** in filenames. Use underscores only.
4. **No uppercase** in filenames except the fixed names `SKILL.md`, `CHANGELOG.md` and `MANIFEST.md` (`ALLOWED_FIXED_NAMES` in [`tests/naming_check.py`](../tests/naming_check.py), together with `.gitkeep`).
5. **Tool name in video files:** Always specify the generation tool (`kling`, `veo`, `seedance` — the list is hardcoded in [`tests/naming_check.py`](../tests/naming_check.py); adding a tool means editing that pattern).
6. **Musical metadata has no version suffix** — it is always the single source of truth per episode. If it needs updating, overwrite and commit with a descriptive message.
7. **Selected files have no version suffix** — selection is a curation decision, not an iteration.
8. **Sub-clip suffix** uses lowercase letters (a, b, c, d) appended directly to the scene number. This pattern is used for: keyframe pairs (start/end), multi-clip sub-clips, and supplementary images. Example: `ep02_s07a` (keyframe start), `ep02_s29c` (third sub-clip of scene 29).

---

## VALIDATION

Run the naming enforcer before any commit:

```
Trigger phrase: "Validate file names for EP{XX}"
Skill: _skills/robotiko-naming-enforcer/SKILL.md
```

GitHub Actions also runs the naming check — together with the pipeline-integrity, visual-prompt, and grade-the-graders meta-test suites — on every push and pull request, through the single entrypoint `tests/run_all.py`. See [`.github/workflows/validation_suite.yml`](../.github/workflows/validation_suite.yml).

---

## COMMIT MESSAGE CONVENTION

```
EP{XX} - {Stage} - {Brief Description}
```

| Stage | When |
|---|---|
| `Scaffold` | New episode folder structure created |
| `Lyrics` | Lyrics file added or updated |
| `Metadata` | Musical metadata JSON added or updated |
| `Concept` | Concept notes added or updated |
| `Dramaturgy` | Scene breakdown created or revised |
| `Visuals` | Visual prompts or images added |
| `Motion` | Motion script created or revised |
| `Video` | Video clips added |
| `Edit` | Final edit committed |
| `Retroactive` | EP01 retroactive documentation |
| `MASTER` | Master.md updated |
| `PIPELINE` | Pipeline rules updated |
| `ARCH` | Architecture updated |
| `MEMORY` | `_memory/` files updated (lessons, todo, decisions log) |

**Examples:**
```
EP02 - Metadata - Musical metadata JSON complete
EP02 - Dramaturgy - Scene breakdown v01, 24 scenes
EP03 - Scaffold - Episode folder structure created
MASTER - v2.0 - Full rewrite with station mapping
```