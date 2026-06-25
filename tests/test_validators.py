"""
Robotiko v2.0 — Meta-tests: grade the graders.

A checker with no proof it works is just a more confident way to be wrong.
These tests assert the validator suite FAILS on a frozen broken fixture and
PASSES on its corrected counterpart — and, crucially, that the broken fixture
fails ONLY on ref-integrity, which is the exact green-over-bug we shipped: every
text-based check passed while the wrong reference image sat in the metadata.

Run:
    python -m unittest tests.test_validators            # from repo root
    python tests/test_validators.py                     # direct
"""

import os
import sys
import unittest
import importlib.util

# ─────────────────────────────────────────────
# Locate repo + load the validator by path (no package assumptions)
# ─────────────────────────────────────────────

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(TESTS_DIR)
FIXTURES = os.path.join(TESTS_DIR, "fixtures")

BROKEN = os.path.join(FIXTURES, "ep09_visual_prompts_BROKEN.md")
GOOD = os.path.join(FIXTURES, "ep09_visual_prompts_GOOD.md")

_spec = importlib.util.spec_from_file_location(
    "visual_prompt_validator", os.path.join(TESTS_DIR, "visual_prompt_validator.py")
)
vpv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vpv)


def setUpModule():
    # check_ref_integrity loads _assets/cast/character_profiles.json relative to
    # cwd — the source of truth must resolve from the repo root, same as in prod.
    os.chdir(REPO_ROOT)


def ref_integrity_errors(errors):
    return [e for e in errors if "[Ref Integrity]" in e]


def non_ref_errors(errors):
    return [e for e in errors if "[Ref Integrity]" not in e]


# ─────────────────────────────────────────────
# The spine: frozen fixtures, both directions
# ─────────────────────────────────────────────

class TestFrozenFixtures(unittest.TestCase):
    """The regression pair. If either direction flips, a grader has rotted."""

    def test_broken_fixture_fails(self):
        results = vpv.validate_file(BROKEN)
        self.assertTrue(
            results["errors"],
            "BROKEN fixture must not validate clean — it carries the real ref bug.",
        )

    def test_broken_fixture_fails_on_ref_integrity(self):
        results = vpv.validate_file(BROKEN)
        ri = ref_integrity_errors(results["errors"])
        self.assertTrue(
            ri,
            "The ref-integrity check must fire on the BROKEN fixture (pristine "
            "ref on a damaged/kintsugi body episode).",
        )
        # Every Robotiko scene in the fixture is mis-referenced -> S01, S02, S27.
        self.assertGreaterEqual(len(ri), 3, f"Expected >=3 ref-integrity hits, got: {ri}")

    def test_broken_fixture_fails_ONLY_on_ref_integrity(self):
        """This is the green-over-bug, pinned: the text-based graders are blind
        to it. Suffix, forbidden-aesthetics and character-phase must all stay
        silent — only ref-integrity catches the wrong reference image."""
        results = vpv.validate_file(BROKEN)
        leaked = non_ref_errors(results["errors"])
        self.assertEqual(
            leaked, [],
            "Only ref-integrity should fire on BROKEN. The text checks passing is "
            f"the whole reason the bug shipped green. Unexpected: {leaked}",
        )

    def test_good_fixture_passes(self):
        results = vpv.validate_file(GOOD)
        self.assertEqual(
            results["errors"], [],
            f"GOOD fixture must pass every check. Errors: {results['errors']}",
        )

    def test_good_fixture_has_prompts(self):
        # Guard against the fixture silently parsing to zero prompts (a green
        # that means "nothing checked", not "everything passed").
        results = vpv.validate_file(GOOD)
        self.assertGreaterEqual(results["prompt_count"], 3)


# ─────────────────────────────────────────────
# Grade each grader in isolation: it must fire when it should,
# and stay silent when it shouldn't.
# ─────────────────────────────────────────────

SUFFIX = vpv.MANDATORY_SUFFIX


class TestRefIntegrityGrader(unittest.TestCase):
    def setUp(self):
        self.profiles = vpv.load_profiles(REPO_ROOT)

    def test_pristine_ref_forbidden_in_damaged_range(self):
        scenes = [{
            "scene_number": 1, "characters": "Robotiko (@Damaged)",
            "ref_path": "`_assets/cast/ref_robotiko_master.png`",
            "upload": "char: `ref_robotiko_master.png`",
        }]
        errs = vpv.check_ref_integrity(scenes, 9)
        self.assertTrue(errs, "Pristine ref on EP09 damaged-range scene must fail.")

    def test_damaged_ref_allowed_in_damaged_range(self):
        scenes = [{
            "scene_number": 1, "characters": "Robotiko (@Damaged)",
            "ref_path": "`_assets/cast/android_damaged.png`",
            "upload": "char: `android_damaged.png`",
        }]
        self.assertEqual(vpv.check_ref_integrity(scenes, 9), [])

    def test_damaged_ref_allowed_as_base_in_kintsugi_range(self):
        # No dedicated Phase 3 ref exists yet; damaged-as-base is the approved
        # kintsugi base. This must NOT be flagged.
        scenes = [{
            "scene_number": 27, "characters": "Robotiko (@Damaged to first gold)",
            "ref_path": "`_assets/cast/android_damaged.png`",
            "upload": "char: `android_damaged.png`",
        }]
        self.assertEqual(vpv.check_ref_integrity(scenes, 9), [])

    def test_pristine_ref_forbidden_in_kintsugi_range(self):
        scenes = [{
            "scene_number": 27, "characters": "Robotiko",
            "ref_path": "`_assets/cast/ref_robotiko_master.png`",
            "upload": "char: `ref_robotiko_master.png`",
        }]
        self.assertTrue(vpv.check_ref_integrity(scenes, 9))

    def test_non_robotiko_scene_ignored(self):
        # The Mechanic alone in frame — no Robotiko reference to police.
        scenes = [{
            "scene_number": 6, "characters": "The Mechanic",
            "ref_path": "`_assets/cast/ref_mechanic.png`",
            "upload": "char: `ref_mechanic.png`",
        }]
        self.assertEqual(vpv.check_ref_integrity(scenes, 9), [])


class TestTextGraders(unittest.TestCase):
    def test_suffix_grader_catches_missing(self):
        bad = [{"index": 1, "text": "a chrome android on a grey path, no suffix here"}]
        self.assertTrue(vpv.check_suffix(bad))

    def test_suffix_grader_passes_present(self):
        ok = [{"index": 1, "text": f"a chrome android on a grey path, {SUFFIX}"}]
        self.assertEqual(vpv.check_suffix(ok), [])

    def test_forbidden_aesthetics_grader_catches(self):
        bad = [{"index": 1, "text": f"a chrome android, pixar style render, {SUFFIX}"}]
        self.assertTrue(vpv.check_forbidden_aesthetics(bad))

    def test_forbidden_aesthetics_grader_passes_clean(self):
        ok = [{"index": 1, "text": f"a chrome android, gritty industrial, {SUFFIX}"}]
        self.assertEqual(vpv.check_forbidden_aesthetics(ok), [])

    def test_character_phase_grader_catches_pristine_in_phase3(self):
        # EP09 is Phase 3 — "pristine" is forbidden in the prompt text.
        bad = [{"index": 1, "text": f"a pristine chrome android, {SUFFIX}"}]
        self.assertTrue(vpv.check_character_phase(bad, 9))

    def test_character_phase_grader_passes_correct_phase3(self):
        ok = [{"index": 1, "text": f"a battle-scarred chrome android, gold in the cracks, {SUFFIX}"}]
        self.assertEqual(vpv.check_character_phase(ok, 9), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
