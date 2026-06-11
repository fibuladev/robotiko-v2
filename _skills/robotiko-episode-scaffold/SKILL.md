# SKILL: robotiko-episode-scaffold
> **Version:** 1.0 | **Last Updated:** 2026-02-24
> **Trigger:** `"Scaffold EP{XX}"`
> **Output:** Full folder structure under `episode-{XX}/`

---

## PURPOSE

Create the complete folder structure and placeholder files for a new episode. The scaffold ensures every episode starts with a consistent, pipeline-ready directory layout — no missing folders, no ad-hoc structure, no naming errors.

---

## MANDATORY INPUTS

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/architecture.md` | Repository structure (Section 3) — the canonical folder layout |
| 2 | `_management/naming_convention.md` | File naming rules — all placeholders must comply |
| 3 | `_management/project_metadata.json` | Verify episode does not already exist |

---

## PRE-EXECUTION CHECKS

Before creating any files:

1. **Episode number validation:** Must be 01-10. Reject anything outside this range.
2. **Duplicate check:** Verify `episode-{XX}/` does not already exist. If it does, STOP and inform the human.
3. **Master reference:** Confirm the episode is defined in `_management/master.md`. If undefined, warn the human but allow scaffolding (the episode may be in early planning).

---

## FOLDER STRUCTURE TO CREATE

```
episode-{XX}/
├── 01_lyrics/
│   └── ep{XX}_lyrics_v01.md          (placeholder — "Lyrics pending")
├── 02_music/
│   └── .gitkeep                       (audio files are gitignored, stored on Google Drive)
├── 03_direction/
│   ├── ep{XX}_concept_notes.md        (placeholder — "Concept notes pending")
│   └── .gitkeep
├── 04_visuals/
│   ├── raw/
│   │   └── .gitkeep
│   └── selected/
│       └── .gitkeep
├── 05_video/
│   ├── raw/
│   │   └── .gitkeep
│   └── selected/
│       └── .gitkeep
├── 06_edit/
│   └── .gitkeep
└── 07_social_media/
    ├── stills/
    │   └── .gitkeep
    └── reels/
        └── .gitkeep
```

---

## PLACEHOLDER FILE CONTENTS

### `ep{XX}_lyrics_v01.md`
```markdown
# EP{XX} — Lyrics
> Status: Pending
> Episode Title: [from master.md or "TBD"]

---

Lyrics will be added here when available.
```

### `ep{XX}_concept_notes.md`
```markdown
# EP{XX} — Concept Notes
> Status: Pending
> Episode Title: [from master.md or "TBD"]

---

## Human Must-Have Shots
*(Add specific visual requests, overrides, and creative directions here)*

## Notes
*(Any additional context for this episode's direction)*
```

### `.gitkeep`
Empty file. Exists solely to preserve the folder in Git (Git does not track empty directories).

---

## POST-SCAFFOLD ACTIONS

After creating the folder structure:

1. **Update `project_metadata.json`:** Set the episode status to `"scaffolded"` if it was previously undefined. Do not overwrite existing status if the episode is already in production.
2. **Verify naming compliance:** Run a quick check that all created files match the naming convention.
3. **Report to human:** List all created folders and files.

---

## EXECUTION METHOD

This skill can be executed in two ways:

### Method A: Claude Code Direct
Claude creates folders and files directly using file system tools.

### Method B: Python Script
```
python scripts/create_episode.py {episode_number}
```
Or via GitHub Actions: `create_episode.yml` workflow.

If the Python script exists and is functional, prefer Method B for consistency. If it does not exist or fails, fall back to Method A.

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Episode folder already exists | STOP. Inform human. Do not overwrite. |
| Episode number out of range (not 01-10) | STOP. Invalid episode number. |
| Episode not defined in master.md | Warn but proceed. Scaffold is structural, not creative. |
| Python script missing or broken | Fall back to direct file creation (Method A). |
| Permission error on directory creation | STOP. Report the error. Likely a filesystem issue. |

---

## POST-GENERATION CHECKLIST

- [ ] All 7 top-level subfolders exist (01_lyrics through 07_social_media)
- [ ] All `raw/` and `selected/` subfolders exist with `.gitkeep`
- [ ] Placeholder files follow naming convention (2-digit episode number, correct prefixes)
- [ ] `project_metadata.json` updated if needed
- [ ] No duplicate folders created
- [ ] Report delivered to human with full file listing

---

*"A clean scaffold is a clean mind. The structure serves the story."*
*— Robotiko v2.0 Pipeline*
