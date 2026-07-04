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

PROFILES_PATH = "_assets/cast/character_profiles.json"
SCHEMA_PATH = "_assets/cast/character_profiles.schema.json"


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
