#!/usr/bin/env python3
"""Copy curated raw video clips into the selected/ folder with convention names.

Usage:
    python scripts/select_videos.py <episode_number> [--dry-run]

Examples:
    python scripts/select_videos.py 9
    python scripts/select_videos.py 9 --dry-run

Keeper clips are saved into episode-{XX}/05_video/raw/ named by scene number --
1.mp4, 2.mp4, ... with sub-clips as 1b.mp4, 1c.mp4 (letter = sub-clip). This
script COPIES each scene-numbered raw clip into 05_video/selected/ using the
naming convention:

    raw/1.mp4    ->  selected/ep09_s01_selected.mp4
    raw/1b.mp4   ->  selected/ep09_s01b_selected.mp4

Anything not scene-numbered is skipped. Copying is non-destructive (raw/ is left
untouched) and safe to re-run.

This step is OPTIONAL: CapCut imports straight from the numbered raw clips. The
selected/ set is a clean, convention-named, shareable copy -- this script is the
twin of select_images.py and just spares you renaming every clip by hand.

Run this from the repository root -- paths are resolved against the current
working directory.
"""

import argparse
import os
import re
import shutil

BASE_DIR = os.getcwd()

# scene-numbered clip: leading digits + optional single sub-clip letter (a-d).
SCENE_RE = re.compile(r"^(\d+)([a-d]?)\.mp4$", re.IGNORECASE)


def select_videos(episode_num, dry_run=False):
    ep_str = f"ep{episode_num:02d}"
    ep_folder = os.path.join(BASE_DIR, f"episode-{episode_num:02d}")
    raw_dir = os.path.join(ep_folder, "05_video", "raw")
    selected_dir = os.path.join(ep_folder, "05_video", "selected")

    if not os.path.isdir(raw_dir):
        raise SystemExit(f"[!] raw folder not found: {raw_dir}")

    prefix = "[dry-run] would copy" if dry_run else "Copying"
    print(f"==> {prefix} curated clips for Episode {episode_num} into: {selected_dir}")

    if not dry_run:
        os.makedirs(selected_dir, exist_ok=True)

    copied = skipped = 0
    for name in sorted(os.listdir(raw_dir)):
        src = os.path.join(raw_dir, name)
        if not os.path.isfile(src):
            continue
        match = SCENE_RE.match(name)
        if not match:
            print(f"[=] skip (not scene-numbered): {name}")
            skipped += 1
            continue
        scene = int(match.group(1))
        letter = match.group(2).lower()
        dst_name = f"{ep_str}_s{scene:02d}{letter}_selected.mp4"
        dst = os.path.join(selected_dir, dst_name)
        if dry_run:
            print(f"[+] [dry-run] {name} -> selected/{dst_name}")
        else:
            shutil.copy2(src, dst)
            print(f"[+] copied: {name} -> selected/{dst_name}")
        copied += 1

    verb = "would copy" if dry_run else "copied"
    print(f"==> Done. {verb} {copied} clip(s), skipped {skipped} non-scene file(s).\n")


def main():
    parser = argparse.ArgumentParser(
        description="Copy curated raw video clips into selected/ with convention names."
    )
    parser.add_argument("episode_number", type=int, help="Episode number, e.g. 9")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be copied without writing anything.",
    )
    args = parser.parse_args()

    if not 1 <= args.episode_number <= 99:
        parser.error("episode_number must be between 1 and 99")

    select_videos(args.episode_number, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
