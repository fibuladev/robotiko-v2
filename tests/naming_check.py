"""
Robotiko v2.0 — Naming Convention Validator
Checks all files in the repository against the naming convention defined in:
_management/naming_convention.md

Usage:
    python tests/naming_check.py
    python tests/naming_check.py --episode 02
    python tests/naming_check.py --full

Status: IMPLEMENTED v1.0
"""

import os
import re
import sys
import argparse

# ─────────────────────────────────────────────
# NAMING PATTERNS (from naming_convention.md)
# ─────────────────────────────────────────────

PATTERNS = {
    # Core pipeline deliverables
    "lyrics":           r"^ep\d{2}_lyrics(_v\d{2})?\.md$",  # _v## standard; unversioned accepted (EP01 legacy)
    "musical_metadata": r"^ep\d{2}_musical_metadata\.json$",
    "concept_notes":    r"^ep\d{2}_concept_notes\.md$",
    "dramaturgy":       r"^ep\d{2}_dramaturgy_v\d{2}\.md$",
    "visual_prompts":   r"^ep\d{2}_visual_prompts_v\d{2}\.md$",
    "motion_script":    r"^ep\d{2}_motion_script(_v\d{2})?\.md$",
    # Direction briefs (one-off planning docs, e.g. ep05_visual_prompt_generation_brief.md)
    "direction_brief":  r"^ep\d{2}_[a-z0-9_]+_brief\.md$",
    # Edit + packaging + social deliverables (produced by capcut-editor, youtube-packager, reels-atomizer, launch-orchestrator)
    "capcut_guide":     r"^ep\d{2}_capcut_guide_v\d{2}\.md$",
    "youtube_package":  r"^ep\d{2}_youtube_package\.md$",
    "social_atomization": r"^ep\d{2}_social_atomization\.md$",
    "launch_checklist": r"^ep\d{2}_launch_checklist\.md$",
    "walkthrough":      r"^ep\d{2}_walkthrough\.md$",
    "external_promotion": r"^ep\d{2}_external_promotion\.md$",
    # Assets
    "raw_image":        r"^ep\d{2}_s\d{2}_v\d{2}\.png$",
    "selected_image":   r"^ep\d{2}_s\d{2}_selected\.png$",
    "raw_video":        r"^ep\d{2}_s\d{2}_video_(kling|veo|seedance)\.mp4$",
    "selected_video":   r"^ep\d{2}_s\d{2}_selected\.mp4$",
    "audio":            r"^ep\d{2}_audio_v\d{2}\.mp3$",
    "final_edit":       r"^ep\d{2}_final_v\d{2}\.mp4$",
    # Exported documents (PDF exports of text deliverables)
    "pdf_export":       r"^ep\d{2}_(lyrics|visual_prompts|motion_script|dramaturgy)(_v\d{2})?\.pdf$",
}

# Files that are allowed with fixed names (not episode-prefixed)
ALLOWED_FIXED_NAMES = {
    "SKILL.md",
    "CHANGELOG.md",
    "MANIFEST.md",
    ".gitkeep",
}

# Folders to skip during validation
SKIP_DIRS = {"raw", ".git", "__pycache__", "node_modules", ".claude"}

# Root-level directories that are NOT episode folders (skip naming validation)
NON_EPISODE_DIRS = {
    "_management", "_assets", "_memory", "_skills", "_templates",
    "scripts", "tests", "docs", ".github",
}

# ─────────────────────────────────────────────
# VALIDATOR
# ─────────────────────────────────────────────

def validate_file(filename: str, folder_context: str = "") -> tuple[bool, str]:
    """
    Validate a single filename against all known patterns.
    Returns (is_valid, message).
    """
    # Allow fixed-name files
    if filename in ALLOWED_FIXED_NAMES:
        return True, f"  PASS (fixed name): {filename}"

    # Check against all patterns
    for pattern_name, pattern in PATTERNS.items():
        if re.match(pattern, filename):
            return True, f"  PASS ({pattern_name}): {filename}"

    return False, f"  FAIL: {filename} — does not match any known pattern"


def validate_episode_consistency(filename: str, expected_ep: str) -> tuple[bool, str]:
    """
    Check that a file's episode number matches its parent folder.
    """
    match = re.match(r"^ep(\d{2})_", filename)
    if match:
        file_ep = match.group(1)
        if file_ep != expected_ep:
            return False, f"  FAIL (wrong episode): {filename} is ep{file_ep} but lives in episode-{expected_ep}"
    return True, ""


def scan_episode(episode_number: str, repo_root: str = ".") -> list[dict]:
    """
    Scan a specific episode folder for naming violations.
    """
    results = []
    episode_folder = os.path.join(repo_root, f"episode-{episode_number}")

    if not os.path.exists(episode_folder):
        print(f"  Episode folder not found: {episode_folder}")
        return results

    for root, dirs, files in os.walk(episode_folder):
        # Skip raw folders and other excluded dirs
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for filename in files:
            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, repo_root)

            # Validate naming pattern
            is_valid, message = validate_file(filename, root)
            results.append({
                "file": rel_path,
                "valid": is_valid,
                "message": message,
            })

            # Validate episode consistency
            if is_valid:
                ep_valid, ep_message = validate_episode_consistency(filename, episode_number)
                if not ep_valid:
                    results.append({
                        "file": rel_path,
                        "valid": False,
                        "message": ep_message,
                    })

    return results


def scan_full_repo(repo_root: str = ".") -> list[dict]:
    """
    Scan all episode folders in the repository.
    """
    results = []

    for item in sorted(os.listdir(repo_root)):
        if item.startswith("episode-") and os.path.isdir(os.path.join(repo_root, item)):
            ep_num = item.replace("episode-", "")
            results.extend(scan_episode(ep_num, repo_root))

    return results


# ─────────────────────────────────────────────
# REPORT
# ─────────────────────────────────────────────

def print_report(results: list[dict]) -> int:
    """
    Print validation report. Returns exit code (0 = pass, 1 = failures found).
    """
    if not results:
        print("\n  No files found to validate.")
        return 0

    failures = [r for r in results if not r["valid"]]
    passes = [r for r in results if r["valid"]]

    print(f"\n  Results: {len(passes)} passed, {len(failures)} failed, {len(results)} total")
    print("-" * 50)

    if failures:
        print("\n  FAILURES:")
        for f in failures:
            print(f"  {f['message']}")

    if passes:
        print(f"\n  PASSED: {len(passes)} files")

    print("-" * 50)

    if failures:
        print(f"\n  NAMING CHECK FAILED — {len(failures)} violation(s) found.")
        return 1
    else:
        print("\n  NAMING CHECK PASSED — All files comply.")
        return 0


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Robotiko Naming Convention Validator")
    parser.add_argument("--episode", type=str, help="Episode number to validate (e.g., 02)")
    parser.add_argument("--full", action="store_true", help="Scan all episode folders")
    args = parser.parse_args()

    # Determine repo root (script lives in tests/)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — Naming Convention Validator")
    print("=" * 50)

    if args.episode:
        ep = args.episode.zfill(2)
        print(f"  Scanning episode-{ep}...")
        results = scan_episode(ep)
    elif args.full:
        print("  Scanning all episode folders...")
        results = scan_full_repo()
    else:
        print("  Usage: python tests/naming_check.py --episode 02")
        print("         python tests/naming_check.py --full")
        sys.exit(0)

    exit_code = print_report(results)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
