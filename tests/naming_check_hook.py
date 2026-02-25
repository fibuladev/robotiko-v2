"""
Robotiko v2.0 — Naming Convention Hook
Lightweight validation triggered by Claude Code hooks after Write tool calls.
Checks if the written file's name follows the naming convention.

This is a fast, single-file check — not a full repo scan.
For full validation, use: python tests/naming_check.py --full
"""

import os
import re
import sys

PATTERNS = {
    "lyrics":           r"^ep\d{2}_lyrics_v\d{2}\.md$",
    "musical_metadata": r"^ep\d{2}_musical_metadata\.json$",
    "concept_notes":    r"^ep\d{2}_concept_notes\.md$",
    "dramaturgy":       r"^ep\d{2}_dramaturgy_v\d{2}\.md$",
    "visual_prompts":   r"^ep\d{2}_visual_prompts_v\d{2}\.md$",
    "motion_script":    r"^ep\d{2}_motion_script_v\d{2}\.md$",
    "raw_image":        r"^ep\d{2}_s\d{2}_v\d{2}\.png$",
    "selected_image":   r"^ep\d{2}_s\d{2}_selected\.png$",
    "raw_video":        r"^ep\d{2}_s\d{2}_video_(kling|veo)\.mp4$",
    "selected_video":   r"^ep\d{2}_s\d{2}_selected\.mp4$",
    "audio":            r"^ep\d{2}_audio_v\d{2}\.mp3$",
    "final_edit":       r"^ep\d{2}_final_v\d{2}\.mp4$",
}

ALLOWED_FIXED = {
    "SKILL.md", "CHANGELOG.md", "MANIFEST.md", ".gitkeep",
    "settings.json", "MEMORY.md",
}

# Only validate files inside episode folders
EPISODE_DIR_PATTERN = re.compile(r"episode-\d{2}")


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    filepath = sys.argv[1]
    if not filepath:
        sys.exit(0)

    # Only check files inside episode-XX folders
    normalized = filepath.replace("\\", "/")
    if not EPISODE_DIR_PATTERN.search(normalized):
        sys.exit(0)

    filename = os.path.basename(filepath)

    # Skip allowed fixed names
    if filename in ALLOWED_FIXED:
        sys.exit(0)

    # Check against patterns
    for pattern_name, pattern in PATTERNS.items():
        if re.match(pattern, filename):
            sys.exit(0)

    # If we got here, the filename doesn't match
    print(f"[NAMING HOOK] WARNING: '{filename}' does not match naming convention.")
    print(f"[NAMING HOOK] See: _management/naming_convention.md")
    # Exit 0 — warn but don't block (non-blocking hook)
    sys.exit(0)


if __name__ == "__main__":
    main()
