"""
Robotiko v2.0 — Visual Prompt Content Validator
Validates visual prompt files for:
  1. Mandatory suffix presence in every prompt
  2. Character phase consistency (Robotiko visual state matches episode phase)
  3. Forbidden aesthetics detection
  4. Reference image integrity (phase-correct character reference per scene)

Usage:
    python tests/visual_prompt_validator.py --file episode-02/04_visuals/ep02_visual_prompts_v01.md
    python tests/visual_prompt_validator.py --episode 02

Status: IMPLEMENTED v2.0
"""

import os
import re
import sys
import json
import argparse

# ─────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────

MANDATORY_SUFFIX = "hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece."

FORBIDDEN_AESTHETICS = [
    "clean apple design",
    "pixar",
    "generic cyberpunk neon",
    "smooth plastic",
    "sleek modern",
    "cartoonish",
    "anime style",
    "3d render",
    "unreal engine",
]

# Robotiko visual state per phase. The forbidden set is per-EPISODE, not per-phase,
# because Phase 1 is NOT uniform: EP01 is pristine, but canon (character_profiles
# evolution.phase_1_awakening) says EP02-EP03 already carry battle damage — missing
# ear, torso dent, cracked sensor panels. So "cracked"/"rusted" are CORRECT for
# EP02-EP03, not violations. Phase-3 markers (translucent body, gold-filled cracks,
# bioluminescent core) stay forbidden until the body actually reaches Phase 3.
PHASE_LABELS = {
    1: "Phase 1: Pristine Chrome (Awakening)",
    2: "Phase 2: Damaged Chrome (Destruction)",
    3: "Phase 3: Reconstructed (Kintsugi)",
}

PHASE3_MARKERS = ["translucent", "patched", "bioluminescent", "kintsugi"]

# Forbidden Robotiko body-state keywords, per episode.
EPISODE_FORBIDDEN = {
    1: ["rusted", "cracked"] + PHASE3_MARKERS,   # EP01: pristine — no damage at all
    2: PHASE3_MARKERS,                            # EP02-03: damage is canon; no Phase-3 yet
    3: PHASE3_MARKERS,
    4: ["pristine"] + PHASE3_MARKERS,            # EP04-07: damaged; pristine + Phase-3 forbidden
    5: ["pristine"] + PHASE3_MARKERS,
    6: ["pristine"] + PHASE3_MARKERS,
    7: ["pristine"] + PHASE3_MARKERS,
    8: ["pristine"],                              # EP08-10: Phase 3 — only pristine is wrong
    9: ["pristine"],
    10: ["pristine"],
}

# A forbidden keyword is judged ONLY when it describes Robotiko. When it is bound to
# scenery or an effect (a "cracked" wall, a "translucent" data hologram, "pristine"
# shelves), it is not a character-state violation. These nouns, appearing within a few
# words of the keyword, neutralize it. Body words (chest, plate, chassis, panel, hand)
# are deliberately ABSENT — those keep the keyword pointed at Robotiko.
NON_ROBOTIKO_NOUNS = {
    "wall", "walls", "shelf", "shelves", "glass", "data", "visualization",
    "hologram", "sky", "snow", "floor", "ground", "screen", "mirror", "window",
    "windows", "skylight", "skylights", "curtain", "curtains", "ceiling",
    "building", "buildings", "room", "corridor", "vault", "tiles", "tile",
    "wallpaper", "fog", "cloud", "clouds", "world",
}


# ─────────────────────────────────────────────
# VALIDATORS
# ─────────────────────────────────────────────

def extract_prompts(content: str) -> list[dict]:
    """
    Extract individual visual prompts from a visual prompts markdown file.
    Looks for text between **Text Prompt:** or **Prompt:** markers.
    """
    prompts = []

    # Pattern: find scene headers and their associated prompts
    # Flexible matching for different formatting styles
    scene_pattern = re.compile(
        r"(?:###?\s*(?:Scene\s+)?S?(\d{1,2}).*?\n)"
        r"(.*?)(?=(?:###?\s*(?:Scene\s+)?S?\d{1,2})|$)",
        re.DOTALL | re.IGNORECASE
    )

    prompt_pattern = re.compile(
        r"(?:\*\*(?:Text\s+)?Prompt[:\s]*\*\*[:\s]*)(.*?)(?=\n\*\*|\n###|\n---|\Z)",
        re.DOTALL | re.IGNORECASE
    )

    # Try to find prompts by marker
    matches = prompt_pattern.findall(content)

    if matches:
        for i, match in enumerate(matches, 1):
            text = match.strip()
            # Skip explicit "no prompt" placeholders (a scene whose environment
            # reference image IS the scene image — no new prompt is generated).
            probe = text.lstrip("> ").strip().lower()
            if probe.startswith("n/a") or "env ref serves" in probe or probe.startswith("no prompt"):
                continue
            prompts.append({
                "index": i,
                "text": text,
            })
    else:
        # Fallback: split by scene headers
        scene_matches = scene_pattern.findall(content)
        for scene_num, scene_content in scene_matches:
            prompts.append({
                "index": int(scene_num),
                "text": scene_content.strip(),
            })

    return prompts


def extract_scenes(content: str) -> list[dict]:
    """
    Extract full scene metadata blocks from a visual prompts file.
    Parses Characters Present, Image Reference Path, Upload and the text prompt —
    the fields the ref-integrity and character-phase checks need.

    Handles BOTH header conventions:
      - "#### Scene S03a — Title"  (EP02, EP04, EP05, EP07-09)
      - "#### S11 — Title"          (EP06)
    The "Scene" word is optional. The a/b sub-scene suffix (Mode B keyframe pairs)
    is preserved as a label so S03a and S03b read as the two distinct frames they
    are — not as a duplicate "S03".
    """
    scenes = []

    scene_block_pattern = re.compile(
        r"####\s*(?:Scene\s+)?S(\d{2})(\w*)\s*[^\n]*\n"
        r"(.*?)(?=\n####\s*(?:Scene\s+)?S\d{2}|\n---\s*\n##\s|\Z)",
        re.DOTALL
    )

    field_patterns = {
        "characters": re.compile(
            r"\*\*Characters?\s+Present:?\s*\*\*:?\s*(.*?)(?:\n\s*-\s*\*\*|\Z)", re.DOTALL | re.IGNORECASE
        ),
        "ref_path": re.compile(
            r"\*\*Image\s+Reference\s+Path:?\s*\*\*:?\s*(.*?)(?:\n\s*-\s*\*\*|\Z)", re.DOTALL | re.IGNORECASE
        ),
        "upload": re.compile(
            r"\*\*Upload:?\s*\*\*:?\s*(.*?)(?:\n\s*-?\s*\*\*|\n\n|\Z)", re.DOTALL | re.IGNORECASE
        ),
    }

    # The text prompt body — a markdown blockquote after the **Text Prompt:** marker.
    text_pattern = re.compile(
        r"\*\*(?:Text\s+)?Prompt:?\s*\*\*:?\s*\n?>?\s*(.*?)(?=\n####|\n---|\Z)",
        re.DOTALL | re.IGNORECASE
    )

    for scene_match in scene_block_pattern.finditer(content):
        scene_num = int(scene_match.group(1))
        suffix = scene_match.group(2) or ""
        block = scene_match.group(3)

        scene = {
            "scene_number": scene_num,
            "label": f"S{scene_num:02d}{suffix}",
            "characters": "",
            "ref_path": "",
            "upload": "",
            "text": "",
        }

        for field, pattern in field_patterns.items():
            m = pattern.search(block)
            if m:
                scene[field] = m.group(1).strip().split("\n")[0].strip()

        tm = text_pattern.search(block)
        if tm:
            scene["text"] = tm.group(1).strip()

        scenes.append(scene)

    return scenes


def load_profiles(repo_root: str = ".") -> dict:
    """Load character_profiles.json from the repo root."""
    path = os.path.join(repo_root, "_assets", "cast", "character_profiles.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_phase_for_episode(episode: int, profiles: dict) -> int:
    """Determine which phase an episode belongs to from the evolution data."""
    evolution = profiles["robotiko"]["evolution"]
    for phase_key, phase_data in evolution.items():
        if episode in phase_data["episodes"]:
            if "phase_1" in phase_key:
                return 1
            elif "phase_2" in phase_key:
                return 2
            elif "phase_3" in phase_key:
                return 3
    return 0


def get_expected_ref(episode: int, scene: int, profiles: dict) -> tuple:
    """
    Given an episode and scene number, return (ref_id, allowed_paths, forbidden_paths).
    Uses phase_reference_map from character_profiles.json.
    """
    robotiko = profiles["robotiko"]
    ref_map = robotiko["phase_reference_map"]
    ref_images = robotiko["reference_images"]

    ep_str = str(episode)
    ref_id = None

    if ep_str in ref_map.get("episode_overrides", {}):
        override = ref_map["episode_overrides"][ep_str]
        if "scene_ranges" in override:
            for r in override["scene_ranges"]:
                if r["start"] <= scene <= r["end"]:
                    ref_id = r["ref"]
                    break
        else:
            ref_id = override.get("ref")

    if ref_id is None:
        phase = get_phase_for_episode(episode, profiles)
        ref_id = ref_map["default_by_phase"].get(str(phase))

    if not ref_id or ref_id not in ref_images:
        return ref_id, [], []

    entry = ref_images[ref_id]
    allowed = []
    if entry["path"]:
        allowed.append(entry["path"])
        allowed.extend(entry.get("alt_angles", []))

    forbidden = []
    for other_id, other_entry in ref_images.items():
        if other_id == ref_id:
            continue
        if not other_entry["path"]:
            continue
        if ref_id == "kintsugi" and other_id == "damaged":
            allowed.append(other_entry["path"])
            allowed.extend(other_entry.get("alt_angles", []))
            continue
        forbidden.append(other_entry["path"])
        forbidden.extend(other_entry.get("alt_angles", []))

    return ref_id, allowed, forbidden


def check_ref_integrity(scenes: list[dict], episode_number: int) -> list[str]:
    """
    Check that every Robotiko scene uses the phase-correct reference image.
    Reads the phase_reference_map from character_profiles.json to determine
    which reference file is expected, then compares against the actual
    Image Reference Path and Upload fields.
    """
    errors = []

    try:
        profiles = load_profiles()
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return ["  WARN [Ref Integrity] Could not load character_profiles.json or missing phase_reference_map."]

    if "phase_reference_map" not in profiles.get("robotiko", {}):
        return ["  WARN [Ref Integrity] character_profiles.json missing phase_reference_map — skipping ref check."]

    robotiko_identifiers = ["robotiko", "chrome android"]

    for scene in scenes:
        chars_lower = scene["characters"].lower()
        if not any(ident in chars_lower for ident in robotiko_identifiers):
            continue

        ref_id, allowed, forbidden = get_expected_ref(episode_number, scene["scene_number"], profiles)

        if not ref_id:
            continue

        ref_path = scene["ref_path"]
        upload = scene["upload"]
        combined = f"{ref_path} {upload}".lower()

        has_allowed = any(os.path.basename(a).lower() in combined for a in allowed) if allowed else False

        for f_path in forbidden:
            f_basename = os.path.basename(f_path).lower()
            if f_basename in combined and not has_allowed:
                ref_images = profiles["robotiko"]["reference_images"]
                expected_entry = ref_images.get(ref_id, {})
                expected_path = expected_entry.get("path")
                expected_name = os.path.basename(expected_path) if expected_path else "text-only base / chain refs (no file)"
                label = scene.get("label", f"S{scene['scene_number']:02d}")
                errors.append(
                    f"  FAIL [Ref Integrity] Scene {label}: "
                    f"Uses '{os.path.basename(f_path)}' but phase requires '{ref_id}' "
                    f"(expected: {expected_name}). "
                    f"Rule: {ref_id} ref must be used for EP{episode_number:02d} {label}."
                )
                break

    return errors


def check_suffix(prompts: list[dict]) -> list[str]:
    """Check that every prompt ends with the mandatory suffix."""
    errors = []
    suffix_normalized = MANDATORY_SUFFIX.lower().strip().rstrip(".")

    for prompt in prompts:
        text_normalized = prompt["text"].lower().strip().rstrip(".")
        if suffix_normalized not in text_normalized:
            errors.append(
                f"  FAIL [Suffix Missing] Prompt #{prompt['index']}: "
                f"Does not contain mandatory visual suffix."
            )

    return errors


def check_forbidden_aesthetics(prompts: list[dict]) -> list[str]:
    """Check for forbidden aesthetic references."""
    errors = []

    for prompt in prompts:
        text_lower = prompt["text"].lower()
        for forbidden in FORBIDDEN_AESTHETICS:
            if forbidden.lower() in text_lower:
                errors.append(
                    f"  FAIL [Forbidden Aesthetic] Prompt #{prompt['index']}: "
                    f"Contains forbidden term: '{forbidden}'"
                )

    return errors


def keyword_targets_robotiko(text_lower: str, keyword: str) -> bool:
    """
    Decide whether a forbidden keyword actually describes Robotiko, or whether it
    is bound to scenery / an effect (a 'cracked' wall, a 'translucent' data
    hologram, 'pristine' shelves). Returns True only if at least one occurrence is
    Robotiko-pointed: not negated ("not pristine"), and not within a few words of a
    non-Robotiko noun. This is what lets the check judge Robotiko, not the set.
    """
    words = re.findall(r"[a-z0-9]+", text_lower)
    for i, w in enumerate(words):
        if w != keyword:
            continue
        if i > 0 and words[i - 1] == "not":          # "not pristine"
            continue
        window = words[max(0, i - 3):i + 4]
        if any(n in NON_ROBOTIKO_NOUNS for n in window if n != keyword):
            continue
        return True
    return False


def load_phase_whitelist(episode_number: int, profiles: dict = None) -> list:
    """
    Scene-pinned exceptions where a forbidden keyword legitimately describes a
    NON-Robotiko subject (e.g. EP08 S22's pristine dream copies, EP06's pristine
    conformist foil android). Narrow by design: pinned to specific scenes + keywords
    so a new pristine-Robotiko error anywhere else still fires.
    """
    if profiles is None:
        try:
            profiles = load_profiles()
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return []
    wl = profiles.get("robotiko", {}).get("phase_keyword_whitelist", {})
    return wl.get(str(episode_number), [])


def _is_whitelisted(entries: list, scene_number: int, keyword: str) -> bool:
    for e in entries:
        if scene_number in e.get("scenes", []) and keyword in e.get("keywords", []):
            return True
    return False


def check_character_phase(scenes: list[dict], episode_number: int, whitelist: list = None) -> list[str]:
    """
    Check that Robotiko's visual state matches the episode's phase. Scene-based, so
    it knows the scene id (for honest labels and scene-pinned whitelisting) and only
    judges words that describe Robotiko (subject-guard), not the scenery.
    """
    forbidden = EPISODE_FORBIDDEN.get(episode_number)
    if forbidden is None:
        return [f"  WARN: Episode {episode_number} not mapped to any phase."]

    phase = get_phase_for_episode(episode_number, load_profiles()) if os.path.exists(
        os.path.join(".", "_assets", "cast", "character_profiles.json")
    ) else 0
    label = PHASE_LABELS.get(phase, f"EP{episode_number:02d}")

    if whitelist is None:
        whitelist = load_phase_whitelist(episode_number)

    robotiko_identifiers = ["robotiko", "chrome android"]
    errors = []

    for scene in scenes:
        haystack = f"{scene.get('characters', '')} {scene.get('text', '')}".lower()
        if not any(ident in haystack for ident in robotiko_identifiers):
            continue

        text_lower = scene.get("text", "").lower()
        scene_label = scene.get("label", f"S{scene.get('scene_number', 0):02d}")

        for kw in forbidden:
            if kw not in text_lower:
                continue
            if not keyword_targets_robotiko(text_lower, kw):
                continue  # describes scenery/effect, not Robotiko
            if _is_whitelisted(whitelist, scene.get("scene_number", -1), kw):
                continue  # intentional, documented non-Robotiko subject
            errors.append(
                f"  FAIL [Character Phase] Scene {scene_label}: "
                f"Contains '{kw}' describing Robotiko, which is forbidden in {label}."
            )

    return errors


def check_reference_first(scenes: list[dict], episode_number: int, profiles: dict = None) -> list[str]:
    """
    Reference-first guard — the EP09 root-cause class.

    If the episode has Robotiko scenes in a phase whose DEDICATED reference image
    is missing (path is null, or the file is not on disk), flag it. Authoring or
    generating scenes for a body state that has no reference forces the generator
    to conjure that state from text on the wrong base image — the 8-10x reshoot
    tax EP09 paid for the kintsugi body before `android_kintsugi.png` existed.
    The rule: generate the reference FIRST, then frame scenes to it.
    """
    if profiles is None:
        try:
            profiles = load_profiles()
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return ["  WARN [Reference-First] Could not load character_profiles.json."]

    robotiko = profiles.get("robotiko", {})
    ref_images = robotiko.get("reference_images", {})
    if not ref_images or "phase_reference_map" not in robotiko:
        return ["  WARN [Reference-First] character_profiles.json missing reference_images / phase_reference_map."]

    identifiers = ["robotiko", "chrome android"]
    used_ref_ids = []
    for scene in scenes:
        haystack = f"{scene.get('characters', '')} {scene.get('text', '')}".lower()
        if not any(i in haystack for i in identifiers):
            continue
        ref_id, _allowed, _forbidden = get_expected_ref(episode_number, scene["scene_number"], profiles)
        if ref_id and ref_id not in used_ref_ids:
            used_ref_ids.append(ref_id)

    errors = []
    for ref_id in used_ref_ids:
        entry = ref_images.get(ref_id, {})
        path = entry.get("path")
        if not path:
            errors.append(
                f"  FAIL [Reference-First] EP{episode_number:02d} has '{ref_id}'-phase Robotiko scenes "
                f"but reference_images['{ref_id}'].path is null — generate the dedicated reference image "
                f"BEFORE authoring/generating these scenes. Conjuring a body state from text on the wrong "
                f"base is the EP09 kintsugi root-cause class (heavy reshoots)."
            )
        elif not os.path.exists(path):
            errors.append(
                f"  FAIL [Reference-First] EP{episode_number:02d} '{ref_id}' reference is declared "
                f"('{path}') but the file is missing on disk — generate it before generating these scenes."
            )
    return errors


def validate_file(filepath: str) -> dict:
    """
    Run all validations on a visual prompts file.
    Returns a results dict.
    """
    results = {
        "file": filepath,
        "errors": [],
        "warnings": [],
        "prompt_count": 0,
    }

    if not os.path.exists(filepath):
        results["errors"].append(f"  FAIL: File not found: {filepath}")
        return results

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract episode number from filename
    ep_match = re.search(r"ep(\d{2})", os.path.basename(filepath))
    episode_number = int(ep_match.group(1)) if ep_match else 0

    # Extract prompts
    prompts = extract_prompts(content)
    results["prompt_count"] = len(prompts)

    if not prompts:
        results["warnings"].append(
            "  WARN: No prompts found in file. Check formatting — "
            "expected **Text Prompt:** or **Prompt:** markers."
        )
        return results

    # Run all checks
    results["errors"].extend(check_suffix(prompts))
    results["errors"].extend(check_forbidden_aesthetics(prompts))

    if episode_number > 0:
        scenes = extract_scenes(content)
        results["errors"].extend(check_character_phase(scenes, episode_number))
        results["errors"].extend(check_ref_integrity(scenes, episode_number))
        results["errors"].extend(check_reference_first(scenes, episode_number))

    return results


# ─────────────────────────────────────────────
# REPORT
# ─────────────────────────────────────────────

def print_report(results: dict) -> int:
    """Print validation report. Returns exit code."""
    print(f"\n  File: {results['file']}")
    print(f"  Prompts found: {results['prompt_count']}")
    print("-" * 50)

    if results["warnings"]:
        print("\n  WARNINGS:")
        for w in results["warnings"]:
            print(f"  {w}")

    if results["errors"]:
        print("\n  ERRORS:")
        for e in results["errors"]:
            print(f"  {e}")
        print(f"\n  VISUAL PROMPT VALIDATION FAILED — {len(results['errors'])} error(s).")
        return 1
    else:
        print("\n  VISUAL PROMPT VALIDATION PASSED — All checks clear.")
        return 0


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

TEMPLATE_MARKERS = ("auto-populated by Claude", "Do not fill manually", "[Claude generates", "{XX}")


def is_unfilled_template(filepath: str) -> bool:
    try:
        with open(filepath, encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except OSError:
        return False
    return any(m in text for m in TEMPLATE_MARKERS)


def run_full() -> int:
    """Validate the latest visual prompts file of every episode, skipping unfilled scaffolds."""
    exit_code = 0
    for ep_dir in sorted(d for d in os.listdir(".") if d.startswith("episode-") and os.path.isdir(d)):
        visuals_dir = os.path.join(ep_dir, "04_visuals")
        if not os.path.isdir(visuals_dir):
            continue
        candidates = sorted(
            (f for f in os.listdir(visuals_dir) if re.match(r"ep\d{2}_visual_prompts_v\d{2}\.md$", f)),
            reverse=True,
        )
        if not candidates:
            continue
        filepath = os.path.join(visuals_dir, candidates[0])
        if is_unfilled_template(filepath):
            print(f"\n  Skipping (unfilled scaffold template): {filepath}")
            continue
        results = validate_file(filepath)
        if print_report(results) != 0:
            exit_code = 1
    return exit_code


def main():
    parser = argparse.ArgumentParser(description="Robotiko Visual Prompt Content Validator")
    parser.add_argument("--file", type=str, help="Path to visual prompts file")
    parser.add_argument("--episode", type=str, help="Episode number (finds file automatically)")
    parser.add_argument("--full", action="store_true", help="Validate every episode's visual prompts")
    args = parser.parse_args()

    # Determine repo root
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — Visual Prompt Content Validator")
    print("=" * 50)

    if args.full:
        sys.exit(run_full())
    elif args.file:
        filepath = args.file
    elif args.episode:
        ep = args.episode.zfill(2)
        # Find the latest version of visual prompts
        visuals_dir = f"episode-{ep}/04_visuals"
        if os.path.exists(visuals_dir):
            candidates = sorted([
                f for f in os.listdir(visuals_dir)
                if re.match(rf"ep{ep}_visual_prompts_v\d{{2}}\.md$", f)
            ], reverse=True)
            if candidates:
                filepath = os.path.join(visuals_dir, candidates[0])
            else:
                print(f"  No visual prompt files found in {visuals_dir}")
                sys.exit(1)
        else:
            print(f"  Directory not found: {visuals_dir}")
            sys.exit(1)
    else:
        print("  Usage: python tests/visual_prompt_validator.py --file <path>")
        print("         python tests/visual_prompt_validator.py --episode 02")
        sys.exit(0)

    results = validate_file(filepath)
    exit_code = print_report(results)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
