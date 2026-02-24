# SKILL: robotiko-naming-enforcer
> **Version:** 1.0 | **Last Updated:** 2026-02-24
> **Trigger:** `"Validate file names"` or `"Validate file names for EP{XX}"`
> **Output:** Compliance report (printed to console / chat)

---

## PURPOSE

Scan episode folders (or the entire repository) and validate that every file follows the naming convention defined in `_management/naming_convention.md`. Report violations with the exact file path, the violation type, and the corrected name.

This skill is a quality gate. It catches naming errors before they propagate through the pipeline and cause broken references in dramaturgy, visual prompts, or motion scripts.

---

## MANDATORY INPUTS

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/naming_convention.md` | All naming rules, patterns, and exceptions |

---

## SCOPE

### Full Scan (No episode specified)
Trigger: `"Validate file names"`
Scope: All `episode-{XX}/` folders + `_management/` + `_assets/` + `_skills/` + `_templates/`

### Episode Scan
Trigger: `"Validate file names for EP{XX}"`
Scope: Only `episode-{XX}/` and its subfolders.

---

## VALIDATION RULES

### Rule 1: Episode Number Format
- Must be exactly 2 digits: `01`, `02`, `10`
- Violation: `ep1_`, `ep002_`, `EP01_`
- Pattern: `/ep\d{2}_/`

### Rule 2: Scene Number Format
- Must be exactly 2 digits: `s01`, `s12`, `s35`
- Violation: `s1_`, `s001_`, `S01_`
- Pattern: `/s\d{2}_/` or `/s\d{2}\./`

### Rule 3: Version Number Format
- Must be `v` + exactly 2 digits: `v01`, `v02`
- Violation: `v1`, `v001`, `V01`
- Exception: Files that have no version suffix by design (see Rule 7)
- Pattern: `/v\d{2}\./`

### Rule 4: Lowercase Enforcement
- All filenames must be lowercase
- Exception: `SKILL.md`, `CHANGELOG.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`
- Violation: `Ep02_Lyrics_v01.md`, `EP02_dramaturgy.md`

### Rule 5: No Spaces
- Filenames must use underscores, never spaces
- Violation: `ep02 lyrics v01.md`

### Rule 6: Tool Name in Video Files
- Raw video files must include the generation tool name
- Pattern: `ep{XX}_s{XX}_video_{tool}.mp4` where `{tool}` is `kling`, `veo`, or `seedream`
- Violation: `ep02_s01_video.mp4` (missing tool name)

### Rule 7: No Version Suffix Exceptions
These file types must NOT have a version suffix:
- `ep{XX}_musical_metadata.json` — single source of truth
- `ep{XX}_s{XX}_selected.png` — curation result, not iteration
- `ep{XX}_s{XX}_selected.mp4` — curation result, not iteration
- `ep{XX}_concept_notes.md` — single document, Git-versioned
- Violation: `ep02_musical_metadata_v01.json`, `ep02_s01_selected_v02.png`

### Rule 8: Folder Structure Compliance
- Episode folders must follow the canonical structure from `architecture.md`
- Required subfolders: `01_lyrics/`, `02_music/`, `03_direction/`, `04_visuals/`, `05_video/`, `06_edit/`, `07_social_media/`
- `04_visuals/` must contain `raw/` and `selected/`
- `05_video/` must contain `raw/` and `selected/`
- `07_social_media/` must contain `stills/` and `reels/`

### Rule 9: Management Files (Fixed Names)
- `_management/` files have fixed names, no episode prefix, no version suffix
- Valid: `master.md`, `pipeline_rules.md`, `naming_convention.md`, `architecture.md`, `project_metadata.json`
- Violation: `master_v02.md`, `pipeline_rules_2.md`

### Rule 10: Asset Files
- Character references: `ref_{character}_master.png`
- Profiles: `character_profiles.json`
- Violation: `robotiko_ref.png`, `characters.json`

---

## OUTPUT FORMAT

### Summary Block
```
NAMING CONVENTION VALIDATION REPORT
Scope: [Full Scan / EP{XX}]
Date: [YYYY-MM-DD]
Files Scanned: [N]
Violations Found: [N]
Status: [PASS ✅ / FAIL ❌]
```

### Violation Table (if any)
| # | File Path | Violation | Expected Name |
|---|---|---|---|
| 1 | `episode-02/01_lyrics/ep2_lyrics_v1.md` | Episode number not 2 digits, version not 2 digits | `ep02_lyrics_v01.md` |
| 2 | `episode-03/04_visuals/raw/Ep03_s1_v01.png` | Uppercase, scene number not 2 digits | `ep03_s01_v01.png` |

### Missing Structure (if any)
| Episode | Missing Folder/File |
|---|---|
| EP03 | `07_social_media/reels/` not found |

---

## EXECUTION METHOD

### Method A: Claude Code Manual Scan
Claude uses Glob and file listing to scan all files, then applies the rules above.

### Method B: Automated Script (Planned)
```
python scripts/naming_check.py [--episode XX]
```
Or via GitHub Actions: `naming_check.yml` on every push.

If the script exists, prefer Method B. Otherwise, execute Method A.

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Episode folder does not exist | Report as missing. Not a naming violation — the episode may not be scaffolded yet. |
| Gitignored folders (raw/) are empty | Not a violation. Raw folders are gitignored by design. |
| `.gitkeep` files | Skip these. They are structural placeholders, not content files. |
| Unknown file types | Flag but do not auto-correct. Ask the human if they belong. |

---

## POST-VALIDATION ACTIONS

- If violations are found: Present the report. Ask the human if they want Claude to auto-rename the files.
- If no violations: Report PASS with file count.
- Never auto-rename without human confirmation — renaming can break references in other documents.

---

*"A misnamed file is a broken link in the chain. The pipeline is only as strong as its naming."*
*— Robotiko v2.0 Pipeline*
