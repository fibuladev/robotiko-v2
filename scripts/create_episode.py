#!/usr/bin/env python3
"""Scaffold a new ROBOTIKO v2.0 episode folder from the shared templates.

Usage:
    python scripts/create_episode.py <episode_number> [--dry-run]

Examples:
    python scripts/create_episode.py 9
    python scripts/create_episode.py 10 --dry-run

The script creates the standard episode folder tree, copies the direction /
visuals / video templates into place, and substitutes the episode-level
placeholders ({XX}) inside the copied templates. Scene-level placeholders
(S{XX}, _s{XX}) are intentionally left untouched for Claude to fill in later.
"""

import argparse
import os
import shutil

# CONFIGURATION
BASE_DIR = os.getcwd()
TEMPLATE_DIR = os.path.join(BASE_DIR, "_templates")

# Standard episode folder tree
FOLDERS = [
    "01_lyrics",
    "02_music",
    "03_direction",
    "04_visuals/raw",
    "04_visuals/selected",
    "05_video/raw",
    "05_video/selected",
    "06_edit",
    "07_social_media",
]

# template filename -> destination (relative to the episode folder)
TEMPLATES = {
    "dramaturgy_template.md": "03_direction/{ep}_dramaturgy_v01.md",
    "visual_prompt_template.md": "04_visuals/{ep}_visual_prompts_v01.md",
    "video_prompt_template.md": "05_video/{ep}_motion_script_v01.md",
}


def substitute_episode_tokens(text, episode_num):
    """Replace only the EPISODE-level placeholders, leaving scene tokens intact.

    Episode tokens: episode-{XX}, EP{XX}, ep{XX}  ->  episode-09, EP09, ep09
    Scene tokens (S{XX}, _s{XX}) are NOT episode-level and must remain as
    placeholders, so a naive global replace of "{XX}" is deliberately avoided.
    Order matters: substitute the longer "episode-" form before the bare "ep".
    """
    ep_num = f"{episode_num:02d}"
    text = text.replace("episode-{XX}", f"episode-{ep_num}")
    text = text.replace("EP{XX}", f"EP{ep_num}")
    text = text.replace("ep{XX}", f"ep{ep_num}")
    return text


def create_episode(episode_num, dry_run=False):
    ep_str = f"ep{episode_num:02d}"
    ep_folder_name = f"episode-{episode_num:02d}"
    ep_path = os.path.join(BASE_DIR, ep_folder_name)

    prefix = "[dry-run] would create" if dry_run else "Creating"
    print(f"==> {prefix} Episode {episode_num} environment at: {ep_path}")

    # 1. Folder tree
    if not dry_run:
        os.makedirs(ep_path, exist_ok=True)
        for folder in FOLDERS:
            os.makedirs(os.path.join(ep_path, folder), exist_ok=True)

    # 2. Empty concept-notes file for the human's first input
    concept_file = os.path.join(ep_path, f"03_direction/{ep_str}_concept_notes.md")
    concept_body = (
        f"# EPISODE {episode_num:02d} - CONCEPT NOTES\n\n"
        "* **Must-Have Shots (Override):**\n"
        "    * Shot X: ...\n"
        "* **Mood:** ...\n"
    )
    if os.path.exists(concept_file):
        print(f"[=] Exists, skipped: {concept_file}")
    elif dry_run:
        print(f"[+] [dry-run] would write: {concept_file}")
    else:
        with open(concept_file, "w", encoding="utf-8") as f:
            f.write(concept_body)
        print(f"[+] Created: {concept_file}")

    # 3. Copy templates and substitute episode-level placeholders
    for tpl_name, dest_rel in TEMPLATES.items():
        src = os.path.join(TEMPLATE_DIR, tpl_name)
        dst = os.path.join(ep_path, dest_rel.format(ep=ep_str))

        if not os.path.exists(src):
            print(f"[!] Warning: template not found: {tpl_name}")
            continue
        if os.path.exists(dst):
            print(f"[=] Exists, skipped: {dst}")
            continue
        if dry_run:
            print(f"[+] [dry-run] would create: {dst}")
            continue

        with open(src, "r", encoding="utf-8") as f:
            content = substitute_episode_tokens(f.read(), episode_num)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Created: {dst}")

    print(f"==> Episode {episode_num} is ready.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new ROBOTIKO v2.0 episode folder from templates."
    )
    parser.add_argument("episode_number", type=int, help="Episode number, e.g. 9 or 10")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing anything.",
    )
    args = parser.parse_args()

    if not 1 <= args.episode_number <= 99:
        parser.error("episode_number must be between 1 and 99")

    create_episode(args.episode_number, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
