"""
Robotiko v2.0 — Naming Convention Validator
Checks all files in the repository against the naming convention defined in:
_management/naming_convention.md

Usage:
    python tests/naming_check.py
    python tests/naming_check.py --episode 02

Status: SKELETON — To be fully implemented during EP03 production phase.
"""

import os
import re
import sys
import argparse

# ─────────────────────────────────────────────
# NAMING PATTERNS (from naming_convention.md)
# ─────────────────────────────────────────────

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

ALLOWED_FIXED_NAMES = [
    "SKILL.md",
    "CHANGELOG.md",
    "MANIFEST.md",
    "concept_notes.md",  # before episode prefix applied
]

# ─────────────────────────────────────────────
# VALIDATOR
# ─────────────────────────────────────────────

def validate_file(filename: str) -> tuple[bool, str]:
    """
    Validate a single filename against all known patterns.
    Returns (is_valid, message).
    """
    # TODO: Implement full validation logic
    # For now, skeleton only
    for pattern_name, pattern in PATTERNS.items():
        if re.match(pattern, filename):
            return True, f"✅ Valid ({pattern_name}): {filename}"
    return False, f"❌ Invalid: {filename}"


def scan_episode(episode_number: str) -> list[dict]:
    """
    Scan a specific episode folder for naming violations.
    """
    # TODO: Implement episode folder scanning
    results = []
    episode_folder = f"episode-{episode_number}"

    if not os.path.exists(episode_folder):
        print(f"⚠️  Episode folder not found: {episode_folder}")
        return results

    for root, dirs, files in os.walk(episode_folder):
        # Skip raw folders (gitignored, not validated)
        dirs[:] = [d for d in dirs if d != "raw"]
        for filename in files:
            is_valid, message = validate_file(filename)
            results.append({
                "file": os.path.join(root, filename),
                "valid": is_valid,
                "message": message
            })

    return results


def main():
    parser = argparse.ArgumentParser(description="Robotiko Naming Convention Validator")
    parser.add_argument("--episode", type=str, help="Episode number to validate (e.g., 02)")
    args = parser.parse_args()

    print("🔍 Robotiko v2.0 — Naming Convention Validator")
    print("=" * 50)

    # TODO: Full implementation
    print("⚠️  SKELETON — Full implementation pending (EP03 phase)")
    print("Refer to: _management/naming_convention.md")


if __name__ == "__main__":
    main()