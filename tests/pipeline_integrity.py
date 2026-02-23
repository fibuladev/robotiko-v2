"""
Robotiko v2.0 — Pipeline Integrity Checker
Validates that no steps were skipped in the production pipeline.
Checks: Lyrics → Metadata → Concept Notes → Dramaturgy → Visuals → Video

Usage:
    python tests/pipeline_integrity_check.py --episode 02

Status: SKELETON — To be fully implemented during EP03 production phase.
"""

import os
import json
import argparse

# ─────────────────────────────────────────────
# PIPELINE STEPS (from pipeline_rules.md)
# ─────────────────────────────────────────────

PIPELINE_STEPS = [
    {
        "step": 1,
        "name": "Lyrics",
        "required_file": "01_lyrics/ep{EP}_lyrics_v01.md",
        "blocking": True,
    },
    {
        "step": 2,
        "name": "Musical Metadata JSON",
        "required_file": "02_music/ep{EP}_musical_metadata.json",
        "blocking": True,
    },
    {
        "step": 3,
        "name": "Concept Notes",
        "required_file": "03_direction/ep{EP}_concept_notes.md",
        "blocking": True,
    },
    {
        "step": 4,
        "name": "Dramaturgy",
        "required_file": "03_direction/ep{EP}_dramaturgy_v01.md",
        "blocking": True,
        "checkpoint": "Human approval required before proceeding.",
    },
    {
        "step": 5,
        "name": "Visual Prompts",
        "required_file": "04_visuals/ep{EP}_visual_prompts_v01.md",
        "blocking": False,
    },
    {
        "step": 6,
        "name": "Motion Script",
        "required_file": "05_video/ep{EP}_motion_script_v01.md",
        "blocking": True,
        "checkpoint": "Human approval required before proceeding.",
    },
    {
        "step": 7,
        "name": "Final Edit",
        "required_file": "06_edit/ep{EP}_final_v01.mp4",
        "blocking": False,
    },
]


# ─────────────────────────────────────────────
# CHECKER
# ─────────────────────────────────────────────

def check_episode_pipeline(episode_number: str) -> None:
    """
    Check pipeline integrity for a specific episode.
    """
    ep = f"ep{episode_number}"
    episode_folder = f"episode-{episode_number}"

    print(f"\n🔍 Checking pipeline for: {episode_folder}")
    print("=" * 50)

    if not os.path.exists(episode_folder):
        print(f"❌ Episode folder not found: {episode_folder}")
        return

    last_completed_step = 0

    for step in PIPELINE_STEPS:
        filepath = os.path.join(
            episode_folder,
            step["required_file"].replace("{EP}", ep)
        )
        exists = os.path.exists(filepath)

        if exists:
            print(f"✅ Step {step['step']}: {step['name']}")
            last_completed_step = step["step"]
        else:
            print(f"⏳ Step {step['step']}: {step['name']} — PENDING")
            if step.get("checkpoint"):
                print(f"   ⛔ CHECKPOINT: {step['checkpoint']}")

    print(f"\n📍 Last completed step: {last_completed_step}/{len(PIPELINE_STEPS)}")


def main():
    parser = argparse.ArgumentParser(description="Robotiko Pipeline Integrity Checker")
    parser.add_argument("--episode", type=str, required=True, help="Episode number (e.g., 02)")
    args = parser.parse_args()

    print("🔍 Robotiko v2.0 — Pipeline Integrity Checker")
    print("⚠️  SKELETON — Full implementation pending (EP03 phase)")

    check_episode_pipeline(args.episode.zfill(2))


if __name__ == "__main__":
    main()