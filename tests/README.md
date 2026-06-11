# Tests
> **Status:** v1.0 — Naming and visual prompt validators implemented.

---

## Available Tests

| Script | Purpose | Status |
|---|---|---|
| `naming_check.py` | Validates file names against `naming_convention.md` | v1.0 Implemented |
| `visual_prompt_validator.py` | Validates visual prompt content (suffix, character phase, forbidden aesthetics) | v1.0 Implemented |
| `pipeline_integrity.py` | Ensures no pipeline steps were skipped | Skeleton |
| `naming_check_hook.py` | Lightweight hook script for Claude Code PostToolUse | v1.0 Implemented |

---

## Usage

```bash
# Validate naming convention for a specific episode
python tests/naming_check.py --episode 02

# Validate naming convention for all episodes
python tests/naming_check.py --full

# Validate visual prompt content for a specific episode
python tests/visual_prompt_validator.py --episode 02

# Validate visual prompt content for a specific file
python tests/visual_prompt_validator.py --file episode-02/04_visuals/ep02_visual_prompts_v01.md

# Check pipeline integrity for an episode
python tests/pipeline_integrity.py --episode 02
```

---

## Claude Code Hook Integration

The naming convention hook is configured in `.claude/settings.json` and runs automatically after every Write tool call. It checks if files written inside `episode-XX/` folders follow the naming convention.

**Note:** The hook uses pure bash (no Python dependency) for maximum compatibility.

---

## What Each Validator Checks

### naming_check.py
- File name matches one of 12 known patterns (lyrics, metadata, dramaturgy, etc.)
- Episode number consistency (file ep02_* lives in episode-02/)
- Skips raw folders and non-episode directories

### visual_prompt_validator.py
- Every prompt contains the mandatory visual suffix
- No forbidden aesthetics (Pixar, clean Apple design, generic cyberpunk neon, etc.)
- Character phase consistency (pristine Robotiko in Phase 1, damaged in Phase 2, etc.)

### pipeline_integrity.py
- Checks each pipeline step has its required output file
- Flags missing steps and mandatory checkpoints

---

## GitHub Actions Integration

All three validators run automatically on every push and pull request via
[`.github/workflows/naming_check.yml`](../.github/workflows/naming_check.yml):

```
python tests/naming_check.py --full
python tests/pipeline_integrity.py --full
python tests/visual_prompt_validator.py --full
```

Run them locally the same way before opening a PR.