"""
Robotiko v2.0 — Character Profiles Structural Validator
Validates character_profiles.json against required structure from schema.json.

This is a lightweight stdlib-only structural check. Full JSON Schema draft-2020-12
validation is deferred per the stdlib-only constraint (no jsonschema dependency).

Usage:
    python tests/character_profiles_validator.py

Status: IMPLEMENTED v1.0
"""

import os
import sys
import json
import importlib.util

PROFILES_PATH = "_assets/cast/character_profiles.json"
SCHEMA_PATH = "_assets/cast/character_profiles.schema.json"

# Reuse the single-source eye-glow detector from the visual-prompt validator, so the
# JSON prompt fields and the Text Prompt blockquotes are judged by identical rules
# (ADR-0010). character_profiles.json is a LIVE production input (it feeds EP10 and
# any re-gen), so an eye-glow leak here is FAIL, not the WARN legacy tier.
_VPV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visual_prompt_validator.py")
_vpv_spec = importlib.util.spec_from_file_location("visual_prompt_validator", _VPV_PATH)
_vpv = importlib.util.module_from_spec(_vpv_spec)
_vpv_spec.loader.exec_module(_vpv)

# Keys whose string values are MODEL-FACING prompt fragments (fed to the generator).
PROMPT_BEARING_KEYS = {"base_visual_prompt", "visual_prompt_addition"}


def _iter_prompt_strings(node, path=""):
    """Yield (json_path, string) for every prompt-bearing field, recursively. A
    visual_prompt_addition may be a plain string or a dict of per-episode strings."""
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else key
            if key in PROMPT_BEARING_KEYS:
                if isinstance(value, str):
                    yield child, value
                elif isinstance(value, dict):
                    for sub, sv in value.items():
                        if isinstance(sv, str):
                            yield f"{child}.{sub}", sv
            else:
                yield from _iter_prompt_strings(value, child)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from _iter_prompt_strings(item, f"{path}[{i}]")


def scan_eye_glow(data) -> list:
    """FAIL findings for any glow-family keyword near an eye/lens word in a
    prompt-bearing field. Kintsugi body gold-glow is allowlisted by the detector."""
    findings = []
    for json_path, text in _iter_prompt_strings(data):
        for snippet in _vpv.eye_glow_hits(text):
            findings.append((
                "FAIL",
                f"Eye-glow in model-facing field '{json_path}': '...{snippet}...'. "
                f"Use the material-lens idiom (ADR-0010); glow keywords break generation."
            ))
    return findings


def validate() -> list:
    findings = []

    if not os.path.isfile(PROFILES_PATH):
        return [("ERROR", f"File not found: {PROFILES_PATH}")]
    if not os.path.isfile(SCHEMA_PATH):
        return [("WARN", f"Schema not found: {SCHEMA_PATH} — structural check only")]

    with open(PROFILES_PATH, encoding="utf-8") as f:
        data = json.load(f)
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        schema = json.load(f)

    if not isinstance(data, dict):
        return [("FAIL", "Top-level value must be an object")]

    # Content-layer guard: model-facing prompt fields must use the material-lens eye
    # idiom, not glow keywords (ADR-0010). Structural checks continue below.
    findings.extend(scan_eye_glow(data))

    top_required = schema.get("required", [])
    for key in top_required:
        if key not in data:
            findings.append(("FAIL", f"Missing required top-level key: '{key}'"))

    schema_props = schema.get("properties", {})

    for char_name, char_data in data.items():
        if not isinstance(char_data, dict):
            findings.append(("FAIL", f"'{char_name}' must be an object"))
            continue

        char_schema = schema_props.get(char_name, {})
        char_required = char_schema.get("required", [])
        for field in char_required:
            if field not in char_data:
                findings.append(("FAIL", f"'{char_name}' missing required field: '{field}'"))

        if char_name in schema_props and "reference_images" in char_required:
            ref_images = char_data.get("reference_images", {})
            if isinstance(ref_images, dict):
                for phase, ref in ref_images.items():
                    if not isinstance(ref, dict):
                        findings.append(("FAIL", f"'{char_name}.reference_images.{phase}' must be an object"))
                        continue
                    for req in ["path", "alt_angles", "description"]:
                        if req not in ref:
                            findings.append(("FAIL", f"'{char_name}.reference_images.{phase}' missing '{req}'"))

        if char_name in schema_props and "phase_reference_map" in char_required:
            phase_map = char_data.get("phase_reference_map", {})
            if isinstance(phase_map, dict):
                default = phase_map.get("default_by_phase", {})
                if isinstance(default, dict):
                    for phase in ["1", "2", "3"]:
                        if phase not in default:
                            findings.append(("FAIL", f"'{char_name}.phase_reference_map.default_by_phase' missing phase '{phase}'"))

    return findings


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — Character Profiles Structural Validator")
    print("=" * 50)

    findings = validate()
    for sev, msg in findings:
        print(f"  {sev}: {msg}")

    fails = [f for f in findings if f[0] in ("FAIL", "ERROR")]
    if fails:
        print(f"\n  CHARACTER PROFILES VALIDATION FAILED — {len(fails)} issue(s).")
        sys.exit(1)
    print("\n  CHARACTER PROFILES VALIDATION PASSED.")
    sys.exit(0)


if __name__ == "__main__":
    main()
