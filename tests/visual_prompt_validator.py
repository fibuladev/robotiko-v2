"""
Robotiko v2.0 — Visual Prompt Content Validator
Validates visual prompt files for:
  1. Mandatory suffix presence in every prompt
  2. Character phase consistency (Robotiko visual state matches episode phase)
  3. Forbidden aesthetics detection
  4. Reference image integrity (phase-correct character reference per scene)
  5. Phase state (ADR-0013): a Phase-1 deliverable (reference prompts only, scenes
     pending behind the human ref gate) is recognized via its scene-pending sentinel
     and partial-passed; a refs-only file with NO sentinel is caught as a false green.
     Two-phase REF blocks also get a Reference-Image-Path lint + pseudo-scene linting.

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

# universe_config lives beside this file — the single source for universe-specific
# validator constants (suffix, forbidden aesthetics, ...). Insert its directory so the
# import resolves whether we run as a script (tests/ is sys.path[0]), as a subprocess
# from the repo root, or loaded by path in the meta-tests (repo root is sys.path[0]).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import universe_config

# ─────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────
# Universe-specific values come from universe_config (fork there, not here). The
# module-level aliases below keep the existing references — and the meta-tests'
# vpv.MANDATORY_SUFFIX / vpv.FORBIDDEN_AESTHETICS — pointing at the single source.

MANDATORY_SUFFIX = universe_config.VISUAL_SUFFIX

FORBIDDEN_AESTHETICS = universe_config.FORBIDDEN_AESTHETICS

# Which character_profiles.json key is the protagonist, and the scene-identifier
# strings that mark a scene as featuring them. Forked in universe_config; defaults are
# the ROBOTIKO values. Absent key -> the phase/ref checks degrade to no-ops (never crash).
PROTAGONIST_KEY = universe_config.PROTAGONIST_KEY
PROTAGONIST_IDENTIFIERS = universe_config.PROTAGONIST_IDENTIFIERS

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
# EYE-GLOW LINT (ADR-0010) — the two-layer eye doctrine.
#
# CANON (master.md) may describe Robotiko's eyes as emitting steady blue light —
# that is on-screen APPEARANCE. But any MODEL-FACING string (Text Prompt blockquotes
# here; prompt fields in character_profiles.json) must use the tested material-lens
# idiom, because glow keywords near eyes empirically break generation (three failed
# formulations documented in lessons.md — "amber eyes", "warm glow", "no glow").
#
# The check is deliberately narrow: a glow-family keyword within EYE_PROXIMITY word
# tokens of an eye/lens word. Curation choices, honest by design:
#   * "light" is NOT a glow keyword — canonical lens-PROJECTION language ("a pale
#     light from his optical lenses", EP07's Dual Device) is generation-safe and
#     must not be flagged. Only emissive glow verbs/adjectives count.
#   * kintsugi BODY gold-glow ("cracks filled with glowing gold light",
#     "bioluminescent core") is canon and generation-safe: a glow keyword bound to a
#     body-gold noun is allowlisted, and "bioluminescent" is not itself a glow token.
# ─────────────────────────────────────────────

GLOW_WORDS = {
    "glow", "glowing", "glows", "glowed", "aglow",
    "luminous", "luminescent", "luminescence", "luminesce",
    "incandescent", "radiant",
}
EYE_WORDS = {
    "eye", "eyes", "lens", "lenses", "optical", "socket", "sockets", "ocular",
}
# A glow keyword immediately adjacent to one of these is kintsugi body-glow, not
# eye-glow — canon and generation-safe. Narrow ±1 window so "glowing amber-gold
# eyes" (color of the eyes) is NOT swallowed by the "gold" of "amber-gold".
BODY_GLOW_NOUNS = {
    "gold", "golden", "core", "cracks", "crack", "seam", "seams", "vein", "veins",
    "kintsugi",
}
EYE_PROXIMITY = 3   # eye word must be within this many tokens of the glow keyword

# Severity mirrors the motion-script model: a file whose header declares SKILL v2.0+
# is FAIL-enforced; files with no version stamp (every shipped visual-prompt file,
# authored before this rule) are WARN-only measured legacy debt and are NOT
# retrofitted. The live input (character_profiles.json) is always FAIL — enforced in
# character_profiles_validator.py.

# ─────────────────────────────────────────────
# STYLE-SUFFIX VARIANT FAMILY (ADR-0009)
#
# The base suffix (check_suffix, MANDATORY_SUFFIX) is required on every prompt,
# always. EP07+ art-house short films ALSO open the prompt with a photoreal modifier
# ("Photorealistic, not a painting") that co-exists with the base suffix — a
# sanctioned variant. It is only legitimate when the file DECLARES its style mode in
# the header (a "STYLE MODE" note citing ADR-0009). An undeclared photoreal modifier
# is a silent contradiction with "70s album art style": WARN legacy / FAIL v2+.
# ─────────────────────────────────────────────

# PHOTOREAL_MODIFIER is universe-specific (fork it in universe_config). STYLE_MODE_MARKER
# is the generic "declare your variant in the header" mechanism and stays local.
PHOTOREAL_MODIFIER = universe_config.PHOTOREAL_MODIFIER
STYLE_MODE_MARKER = "style mode"

# ─────────────────────────────────────────────
# TWO-PHASE PHASE-1 SENTINEL (ADR-0013 / two-phase visual prompts)
#
# A Phase-1 deliverable authors the reference prompts + locks + coverage map and
# INTENTIONALLY leaves the scene section pending behind the human ref-approval gate.
# Such a file has REF Text Prompts (so extract_prompts finds >0) but ZERO parsed
# scenes. Without a marker that is indistinguishable from a refs-only FALSE GREEN
# (someone forgot to write the scenes). The sentinel below is the machine token that
# says "this refs-only state is designed, not unfinished".
#
# Detection is line-anchored AND applied only AFTER fenced code blocks are stripped,
# so a doc / template / changelog that QUOTES the token inside a ``` fence never
# false-positives. ASCII, underscores; contains no is_unfilled_template marker and no
# pipeline_integrity.TEMPLATE_MARKERS token by construction.
# ─────────────────────────────────────────────

SCENES_PENDING_SENTINEL = "SCENES_STATUS: PENDING_PHASE_2"
# Line-anchored; tolerates a leading markdown blockquote marker ('> ') because the
# live sentinel sits inside the human-facing PENDING block's blockquote (D1). Applied
# only after strip_code_fences() so a fenced QUOTE of the token never false-positives.
_SENTINEL_RE = re.compile(r"(?m)^\s*>?\s*SCENES_STATUS:\s*PENDING_PHASE_2\s*$")
_FENCE_RE = re.compile(r"(?ms)^[ \t]*```.*?^[ \t]*```[ \t]*$")


def strip_code_fences(content: str) -> str:
    """Remove fenced code blocks (```...```) so a sentinel QUOTED inside a fence —
    docs, the template, a changelog — never trips the Phase-1 detector. Only the live
    document body is considered."""
    return _FENCE_RE.sub("", content)


def has_phase1_sentinel(content: str) -> bool:
    """True if the Phase-1 scene-pending sentinel appears in the LIVE body (outside any
    fenced code block). This is the single source for 'is this a Phase-1 deliverable'."""
    return bool(_SENTINEL_RE.search(strip_code_fences(content)))


def is_skill_v2(content: str) -> bool:
    """True if the file's header declares SKILL v2.0+ (mirrors the motion-script
    severity model). Version-stamped files are FAIL-enforced for the eye-glow and
    style-mode rules; unstamped shipped files are WARN-only legacy debt."""
    for line in content.splitlines()[:15]:
        if "SKILL.md" in line and ("v2" in line or "v3" in line):
            return True
    return False


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


# The canonical two-phase REFERENCE-block header: "### REF A: ...", "### REF 3: ...".
# Deliberately NARROW — a whitespace after "REF" is required, so the older
# "### REF-ENV-01 —" format (EP04/EP05, pre-two-phase) is NOT matched and stays out of
# scope of the two-phase ref-path lint / pseudo-scene lint (those files pass today).
_REF_BLOCK_RE = re.compile(
    r"(?ms)^###\s+REF\s+([A-Za-z0-9]+)\b[^\n]*\n(.*?)(?=^###\s|^##\s|\Z)"
)
_REF_PATH_FIELD_RE = re.compile(
    r"\*\*Reference\s+Image\s+Path:?\s*\*\*:?\s*(.*?)(?:\n|\Z)", re.IGNORECASE
)
_REF_TEXT_RE = re.compile(
    r"\*\*(?:Text\s+)?Prompt:?\s*\*\*:?\s*\n?>?\s*(.*?)(?=\n###|\n##|\n---|\Z)",
    re.DOTALL | re.IGNORECASE,
)


def _extract_ref_path(field_value: str) -> str:
    """Pull the reference image path out of a Reference-Image-Path field value.
    Prefers the FIRST backtick-quoted token (paths are quoted) so a trailing
    annotation — e.g. `...ref_exterior.png` (generate from `5.png`) — does not leak
    into the path. Falls back to the first whitespace-delimited token."""
    m = re.search(r"`([^`]+)`", field_value)
    if m:
        return m.group(1).strip()
    field_value = field_value.strip()
    return field_value.split()[0] if field_value else ""


def extract_ref_blocks(content: str) -> list[dict]:
    """
    Extract the two-phase ENVIRONMENT/CHARACTER reference blocks (`### REF <id>: ...`)
    with their Reference Image Path and Text Prompt. These are the Phase-1
    deliverables the gate approves; scene blocks (`#### Scene S..`) are parsed
    separately by extract_scenes(). Returns [] for pre-two-phase files that use the
    older `### REF-ENV-01 —` header (deliberately not matched)."""
    blocks = []
    for m in _REF_BLOCK_RE.finditer(content):
        ref_id = m.group(1)
        body = m.group(2)
        block = {"ref_id": ref_id, "label": f"REF {ref_id}", "ref_path": "", "text": ""}
        pm = _REF_PATH_FIELD_RE.search(body)
        if pm:
            block["ref_path"] = _extract_ref_path(pm.group(1))
        tm = _REF_TEXT_RE.search(body)
        if tm:
            block["text"] = tm.group(1).strip()
        blocks.append(block)
    return blocks


def load_profiles(repo_root: str = ".") -> dict:
    """Load character_profiles.json from the repo root."""
    path = os.path.join(repo_root, "_assets", "cast", "character_profiles.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_phase_for_episode(episode: int, profiles: dict) -> int:
    """Determine which phase an episode belongs to from the evolution data. Returns 0
    (phase unknown) when the protagonist entry or its evolution block is absent — a
    foreign-universe cast must not crash this helper."""
    evolution = profiles.get(PROTAGONIST_KEY, {}).get("evolution")
    if not isinstance(evolution, dict):
        return 0
    for phase_key, phase_data in evolution.items():
        if episode in (phase_data.get("episodes", []) if isinstance(phase_data, dict) else []):
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
    protagonist = profiles.get(PROTAGONIST_KEY, {})
    ref_map = protagonist.get("phase_reference_map")
    ref_images = protagonist.get("reference_images")
    if not isinstance(ref_map, dict) or not isinstance(ref_images, dict):
        return None, [], []

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

    if "phase_reference_map" not in profiles.get(PROTAGONIST_KEY, {}):
        return ["  WARN [Ref Integrity] character_profiles.json missing phase_reference_map — skipping ref check."]

    protagonist_identifiers = PROTAGONIST_IDENTIFIERS

    for scene in scenes:
        chars_lower = scene["characters"].lower()
        if not any(ident in chars_lower for ident in protagonist_identifiers):
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
                ref_images = profiles[PROTAGONIST_KEY]["reference_images"]
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
    wl = profiles.get(PROTAGONIST_KEY, {}).get("phase_keyword_whitelist", {})
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
        return [
            f"  WARN: Episode {episode_number} not mapped to any phase — character-state "
            f"keywords not checked. Add the episode to EPISODE_FORBIDDEN in "
            f"tests/visual_prompt_validator.py; a fork defines its own phase map there."
        ]

    phase = get_phase_for_episode(episode_number, load_profiles()) if os.path.exists(
        os.path.join(".", "_assets", "cast", "character_profiles.json")
    ) else 0
    label = PHASE_LABELS.get(phase, f"EP{episode_number:02d}")

    if whitelist is None:
        whitelist = load_phase_whitelist(episode_number)

    protagonist_identifiers = PROTAGONIST_IDENTIFIERS
    errors = []

    for scene in scenes:
        haystack = f"{scene.get('characters', '')} {scene.get('text', '')}".lower()
        if not any(ident in haystack for ident in protagonist_identifiers):
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

    protagonist = profiles.get(PROTAGONIST_KEY, {})
    ref_images = protagonist.get("reference_images", {})
    if not ref_images or "phase_reference_map" not in protagonist:
        return ["  WARN [Reference-First] character_profiles.json missing reference_images / phase_reference_map."]

    identifiers = PROTAGONIST_IDENTIFIERS
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


def eye_glow_hits(text: str) -> list[str]:
    """
    Core eye-glow detector, reusable for any model-facing string (Text Prompt
    blockquotes here, prompt fields in character_profiles.json). Returns a list of
    offending snippets (empty == clean). A hit is a glow-family keyword within
    EYE_PROXIMITY tokens of an eye/lens word, EXCEPT when the glow keyword is bound
    to kintsugi body-gold (allowlisted).
    """
    words = re.findall(r"[a-z0-9]+", text.lower())
    hits = []
    for i, w in enumerate(words):
        if w not in GLOW_WORDS:
            continue
        # Allowlist: kintsugi body gold-glow — glow keyword adjacent (+-1) to a
        # body-gold noun ("glowing gold light"). Narrow so "glowing amber-gold eyes"
        # (eye colour) is NOT exempted by the incidental "gold".
        neighbours = words[max(0, i - 1):i + 2]
        if any(n in BODY_GLOW_NOUNS for n in neighbours if n != w):
            continue
        window = words[max(0, i - EYE_PROXIMITY):i + EYE_PROXIMITY + 1]
        if any(n in EYE_WORDS for n in window):
            snippet = " ".join(words[max(0, i - EYE_PROXIMITY):i + EYE_PROXIMITY + 1])
            hits.append(snippet)
    return hits


def check_eye_glow(scenes: list[dict], severity: str = "WARN") -> list[tuple]:
    """
    Scan each scene's Text Prompt blockquote (scene["text"]) for eye-glow: a glow
    keyword next to an eye/lens word in a MODEL-FACING string (ADR-0010). Returns
    (severity, message) tuples. ASCII output only.
    """
    findings = []
    for scene in scenes:
        for snippet in eye_glow_hits(scene.get("text", "")):
            label = scene.get("label", f"S{scene.get('scene_number', 0):02d}")
            findings.append((
                severity,
                f"  {severity} [Eye Glow] Scene {label}: glow keyword near eyes in the "
                f"Text Prompt ('...{snippet}...'). Model-facing eye descriptions must use "
                f"the material-lens idiom (ADR-0010); glow keywords break generation."
            ))
    return findings


def check_style_mode(content: str, prompts: list[dict], severity: str = "WARN") -> list[tuple]:
    """
    Style-suffix variant family (ADR-0009). The base suffix stays required
    (check_suffix). The photoreal modifier is allowed ONLY when the file declares its
    STYLE MODE in the header; an undeclared modifier is a silent contradiction with
    the base "70s album art style". Returns (severity, message) tuples. ASCII only.
    """
    if STYLE_MODE_MARKER in content.lower():
        return []
    findings = []
    for prompt in prompts:
        if PHOTOREAL_MODIFIER in prompt["text"].lower():
            findings.append((
                severity,
                f"  {severity} [Style Mode] Prompt #{prompt['index']}: uses the photoreal "
                f"modifier ('{PHOTOREAL_MODIFIER}') but the file declares no STYLE MODE "
                f"header. The variant is sanctioned only when declared (ADR-0009)."
            ))
    return findings


def check_phase_state(content: str, scenes: list[dict]) -> list[tuple]:
    """
    Phase-aware gate (ADR-0013 / two-phase visual prompts). Kills the refs-only FALSE
    GREEN: a file with REF Text Prompts but zero SCENE prompts used to sail through
    every text check while checking nothing scene-level. Keyed on extract_scenes()
    (NOT extract_prompts) because REF blocks carry **Text Prompt:** markers too — only
    a parsed SCENE count discriminates a Phase-1 deliverable from a full document.

    Returns (severity, message) tuples. Severities:
      * "INFO" — legitimate Phase-1 deliverable (sentinel present, 0 scenes). The
        caller runs prompt-level + pseudo-scene checks over the REF prompts and SKIPS
        the scene-level checks. Not a failure.
      * "FAIL" — a blocking state (stale sentinel, or refs-only false green).

    Truth table (sentinel = present outside fenced code blocks):

      | sentinel | scenes | outcome                                               |
      |----------|--------|-------------------------------------------------------|
      | yes      | 0      | INFO  — PHASE 1 ONLY partial pass                      |
      | yes      | >0     | FAIL  — stale Phase-1 sentinel (scenes present)        |
      | no       | 0      | FAIL  — refs-only false green (no scenes, no sentinel) |
      | no       | >0     | (empty) — normal full validation, unchanged           |
    """
    has_sentinel = has_phase1_sentinel(content)
    n = len(scenes)

    if has_sentinel and n == 0:
        return [(
            "INFO",
            "  PHASE 1 ONLY - Phase-1 deliverable: reference prompts validated, "
            "0 scenes (pending Phase 2). Scene-level checks skipped by design "
            "(scenes are framed to approved reference pixels in Phase 2)."
        )]
    if has_sentinel and n > 0:
        return [(
            "FAIL",
            f"  FAIL [Phase State] Stale Phase-1 sentinel: {n} scene(s) are present but "
            f"the '{SCENES_PENDING_SENTINEL}' token is still in the file. Remove the "
            f"sentinel - this is a Phase-2 (or full) document, not a Phase-1 deliverable."
        )]
    if not has_sentinel and n == 0:
        return [(
            "FAIL",
            "  FAIL [Phase State] No scenes parsed and no Phase-1 sentinel - a refs-only "
            "file would pass silently (false green). Either write the scenes, or declare "
            f"a Phase-1 deliverable with the '{SCENES_PENDING_SENTINEL}' token."
        )]
    return []


# Canonical Reference-Image-Path form (D6): episode-XX/04_visuals/[raw/]epXX_ref_<name>.png
# with the path's episode number matching the folder episode. The optional raw/ segment
# tolerates EP10 v01's raw-less committed paths; canonical form includes raw/.
_REF_IMAGE_PATH_RE = re.compile(
    r"^episode-(\d{2})/04_visuals/(?:raw/)?ep\1_ref_[a-z0-9_]+\.png$"
)


def check_ref_image_path(ref_blocks: list[dict], episode_number: int,
                         severity: str = "FAIL") -> list[tuple]:
    """
    Reference-Image-Path field lint (D6) on the two-phase REF blocks. The one cheap,
    machine-visible guard the panel kept after declining a full under-segmentation
    lint: a REF block's declared image path must be well-formed AND belong to this
    episode's folder, so a mis-pointed or malformed ref path is caught on cheap text
    before generation. Returns (severity, message) tuples. ASCII output only."""
    findings = []
    for b in ref_blocks:
        path = (b.get("ref_path") or "").strip().strip("`").replace("\\", "/")
        label = b.get("label", "REF")
        if not path:
            findings.append((
                severity,
                f"  {severity} [Ref Path] {label}: missing Reference Image Path field."
            ))
            continue
        m = _REF_IMAGE_PATH_RE.match(path)
        if not m:
            findings.append((
                severity,
                f"  {severity} [Ref Path] {label}: path '{path}' does not match "
                f"episode-XX/04_visuals/[raw/]epXX_ref_<name>.png (lowercase name, .png)."
            ))
            continue
        if int(m.group(1)) != episode_number:
            findings.append((
                severity,
                f"  {severity} [Ref Path] {label}: path episode number {m.group(1)} "
                f"!= folder episode {episode_number:02d} ('{path}')."
            ))
    return findings


def ref_pseudo_scenes(ref_blocks: list[dict]) -> list[dict]:
    """Turn CHARACTER/GROUP reference blocks (a REF whose Text Prompt names the
    protagonist) into pseudo-scenes so the eye-glow (ADR-0010) and character-phase
    lints reach them in a Phase-1 deliverable — where there are no real scenes yet but
    the kintsugi/body-state refs (ADR-0007's original driver) still must be clean.
    Environment-only refs (no character in the prompt) are skipped."""
    idents = PROTAGONIST_IDENTIFIERS
    pseudo = []
    for b in ref_blocks:
        text = b.get("text", "")
        if any(ident in text.lower() for ident in idents):
            pseudo.append({
                "scene_number": 0,
                "label": b.get("label", "REF"),
                "characters": b.get("label", "REF"),
                "text": text,
                "ref_path": b.get("ref_path", ""),
                "upload": "",
            })
    return pseudo


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

    def route(sev, msg):
        (results["errors"] if sev in ("FAIL", "ERROR") else results["warnings"]).append(msg)

    # Extract prompts, scenes and two-phase REF blocks up front — check_phase_state
    # needs the SCENE count to discriminate a Phase-1 deliverable from a false green.
    prompts = extract_prompts(content)
    scenes = extract_scenes(content)
    ref_blocks = extract_ref_blocks(content)
    results["prompt_count"] = len(prompts)

    # Phase-state gate (ADR-0013): BEFORE the empty-prompts guard, so a legitimate
    # Phase-1 file is recognized and a refs-only false green is caught. INFO ->
    # warnings (visible "PHASE 1 ONLY" partial pass); FAIL -> errors (blocks).
    phase_findings = check_phase_state(content, scenes)
    phase1_only = any(sev == "INFO" for sev, _ in phase_findings)
    for sev, msg in phase_findings:
        route(sev, msg)

    if not prompts:
        # No REF prompts AND no scene prompts: a malformed file. (check_phase_state has
        # already flagged the no-scenes dimension; this is the explicit prompts==[] FAIL.)
        results["errors"].append(
            "  FAIL: No prompts found in file (expected **Text Prompt:** or **Prompt:** "
            "markers) - malformed visual prompts file."
        )
        return results

    # Prompt-level checks run over ALL prompts (incl. REF Text Prompts) in BOTH phases,
    # so a Phase-1 file's reference prompts are still suffix/forbidden/style checked.
    results["errors"].extend(check_suffix(prompts))
    results["errors"].extend(check_forbidden_aesthetics(prompts))

    # Style-suffix + eye-glow severity mirrors the motion-script model: version-
    # stamped files FAIL, unstamped shipped files WARN (measured legacy debt).
    style_severity = "FAIL" if is_skill_v2(content) else "WARN"

    # Style-suffix variant family (ADR-0009): severity-routed (FAIL -> errors, WARN
    # -> warnings) so a legacy/undeclared modifier surfaces without blocking.
    for sev, msg in check_style_mode(content, prompts, style_severity):
        route(sev, msg)

    if episode_number > 0:
        # An episode outside this universe's phase map — a fork's own episode, a freshly
        # scaffolded folder — cannot be character-phase checked. That is a gap in the map,
        # not a defect in the file, so it WARNs instead of blocking the gate. All ten
        # ROBOTIKO episodes are mapped, so this never downgrades a real finding here.
        phase_bucket = "errors" if episode_number in EPISODE_FORBIDDEN else "warnings"

        # Reference-Image-Path field lint (D6) on the two-phase REF blocks — both phases.
        for sev, msg in check_ref_image_path(ref_blocks, episode_number):
            route(sev, msg)

        if phase1_only:
            # Phase-1 deliverable: scenes intentionally pending, so scene-level checks
            # are skipped. The character/group REF prompts still get pseudo-scene
            # linting (D7.4) so eye-glow and phase keywords bind to the body-state refs.
            pseudo = ref_pseudo_scenes(ref_blocks)
            results[phase_bucket].extend(check_character_phase(pseudo, episode_number))
            for sev, msg in check_eye_glow(pseudo, style_severity):
                route(sev, msg)
        else:
            results[phase_bucket].extend(check_character_phase(scenes, episode_number))
            results["errors"].extend(check_ref_integrity(scenes, episode_number))
            results["errors"].extend(check_reference_first(scenes, episode_number))

            # Eye-glow lint (ADR-0010): severity-routed. FAIL for version-stamped files;
            # WARN for shipped, unstamped files (not retrofitted; see EP02 legacy note).
            for sev, msg in check_eye_glow(scenes, style_severity):
                route(sev, msg)

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


def find_pdf_visuals(visuals_dir: str) -> list[str]:
    """
    Recursively find PDF visual-prompt files anywhere under an episode's 04_visuals
    directory — including the selected/ and raw/ subfolders.

    This is the M4 real fix. The prior code called os.listdir(visuals_dir) (one level
    only), so EP01's PDF — which lives at episode-01/04_visuals/selected/ep01_visual_
    prompts_v01.pdf — was NEVER seen: the branch could not fire and EP01 was skipped
    silently, with no output line at all. os.walk sees the whole subtree, so the
    PDF-only skip actually triggers and becomes visible.
    """
    pdfs = []
    for root, _dirs, files in os.walk(visuals_dir):
        for name in files:
            if name.lower().endswith(".pdf") and "visual_prompts" in name.lower():
                pdfs.append(os.path.join(root, name))
    return sorted(pdfs)


def pdf_skip_message(ep_dir: str, pdf_path: str) -> str:
    """The VISIBLE skip line for a PDF-only (pre-method) episode. Asserted verbatim
    by a meta-test so it can never silently vanish again (the M4 regression)."""
    rel = pdf_path.replace("\\", "/")
    return (
        f"  Skipping {ep_dir}: PDF-only visuals ({rel}) - pre-method episode, "
        f"declared Human-tier in the coverage matrix; not machine-parseable."
    )


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
            # Search the whole 04_visuals subtree (selected/ + raw/), not just the top
            # level — this is what makes EP01's PDF-only skip actually fire and print.
            pdf_files = find_pdf_visuals(visuals_dir)
            if pdf_files:
                print("\n" + pdf_skip_message(ep_dir, pdf_files[0]))
            continue
        filepath = os.path.join(visuals_dir, candidates[0])
        # Sentinel check BEFORE the unfilled-template skip (D2): a Phase-1 deliverable
        # (scene-pending sentinel present) must ALWAYS be validated, never silently
        # routed into the scaffold-skip path — even if a scaffold marker lingers.
        try:
            with open(filepath, encoding="utf-8", errors="ignore") as fh:
                _head = fh.read()
        except OSError:
            _head = ""
        if not has_phase1_sentinel(_head) and is_unfilled_template(filepath):
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
