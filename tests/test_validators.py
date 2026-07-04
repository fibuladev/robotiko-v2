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

_hspec = importlib.util.spec_from_file_location(
    "prompt_hygiene_lint", os.path.join(TESTS_DIR, "prompt_hygiene_lint.py")
)
phl = importlib.util.module_from_spec(_hspec)
_hspec.loader.exec_module(phl)

_dspec = importlib.util.spec_from_file_location(
    "doc_reference_check", os.path.join(TESTS_DIR, "doc_reference_check.py")
)
drc = importlib.util.module_from_spec(_dspec)
_dspec.loader.exec_module(drc)

_pspec = importlib.util.spec_from_file_location(
    "pipeline_integrity", os.path.join(TESTS_DIR, "pipeline_integrity.py")
)
pi = importlib.util.module_from_spec(_pspec)
_pspec.loader.exec_module(pi)

DOC_REF_BAD = os.path.join(FIXTURES, "doc_ref_BAD.md")
DOC_REF_GOOD = os.path.join(FIXTURES, "doc_ref_GOOD.md")

# M4 fixture: a PDF that lives in a selected/ SUBDIR (exactly where EP01's real PDF
# sits) — the case the old one-level os.listdir could never see.
PDF_SUBDIR_VISUALS = os.path.join(FIXTURES, "pdf_only_visuals", "04_visuals")


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
        # EP09 is Phase 3 — "pristine" describing Robotiko is forbidden.
        bad = [_scene(f"a pristine chrome android, {SUFFIX}")]
        self.assertTrue(vpv.check_character_phase(bad, 9, whitelist=[]))

    def test_character_phase_grader_passes_correct_phase3(self):
        ok = [_scene(f"a battle-scarred chrome android, gold in the cracks, {SUFFIX}")]
        self.assertEqual(vpv.check_character_phase(ok, 9, whitelist=[]), [])


# ─────────────────────────────────────────────
# Each loosening, proven both directions: still CATCHES a real Robotiko bug,
# and correctly IGNORES the intended case. No check is loosened without this.
# ─────────────────────────────────────────────

def _scene(text, characters="Robotiko (@Damaged)", number=1, label=None):
    return {
        "scene_number": number,
        "label": label or f"S{number:02d}",
        "characters": characters,
        "text": text,
        "ref_path": "",
        "upload": "",
    }


class TestSubjectGuardRefinement(unittest.TestCase):
    """REFINE A — judge Robotiko, not the scenery."""

    def test_ignores_pristine_scenery(self):
        # EP05 S10 real text: "pristine shelves" is the supermarket, not Robotiko.
        s = _scene("his cracked chassis contrasts with the pristine shelves around him")
        self.assertEqual(vpv.check_character_phase([s], 5, whitelist=[]), [])

    def test_ignores_translucent_effects_and_walls(self):
        # EP05 S22 (data viz) and S30 (iron walls dissolving) — environment/effect.
        s1 = _scene("a translucent visualization of data flows around his head")
        s2 = _scene("the colossal iron walls becoming translucent and ghostly")
        self.assertEqual(vpv.check_character_phase([s1], 5, whitelist=[]), [])
        self.assertEqual(vpv.check_character_phase([s2], 5, whitelist=[]), [])

    def test_ignores_negated_pristine(self):
        s = _scene("subtle wear marks, the chrome android is not pristine, he carries history")
        self.assertEqual(vpv.check_character_phase([s], 5, whitelist=[]), [])

    def test_still_catches_pristine_robotiko_body(self):
        # The real bug the guard must NOT mask: Robotiko himself described pristine.
        s = _scene("the chrome android's pristine chest plate, clean and sealed")
        self.assertTrue(vpv.check_character_phase([s], 5, whitelist=[]))


class TestPhaseGranularityRefinement(unittest.TestCase):
    """REFINE B — EP01 is pristine, but EP02/EP03 are canon-damaged."""

    def test_ep01_still_forbids_cracked_robotiko(self):
        s = _scene("the chrome android with a cracked dented chest plate")
        self.assertTrue(vpv.check_character_phase([s], 1, whitelist=[]))

    def test_ep02_allows_canon_damage(self):
        s = _scene("the chrome android, cracked sensor panels, missing right ear, torso dent")
        self.assertEqual(vpv.check_character_phase([s], 2, whitelist=[]), [])

    def test_ep03_allows_canon_damage(self):
        s = _scene("the chrome android with cracked back panels and rusted joints")
        self.assertEqual(vpv.check_character_phase([s], 3, whitelist=[]), [])

    def test_ep02_still_catches_phase3_marker_leak(self):
        # Damage is fine in EP02; a Phase-3 marker (translucent body) is not.
        s = _scene("the chrome android with translucent digital skin over a glowing core")
        self.assertTrue(vpv.check_character_phase([s], 2, whitelist=[]))


class TestWhitelistNarrowness(unittest.TestCase):
    """The whitelist (loaded from character_profiles.json) is scene-pinned: it
    silences the intended case WITHOUT silencing the same keyword elsewhere."""

    def test_ep08_s22_dream_copies_ignored(self):
        s = _scene(
            "every seat occupied by an identical pristine undamaged chrome android",
            characters="Robotiko (damaged, center); hundreds of pristine copies",
            number=22,
        )
        self.assertEqual(vpv.check_character_phase([s], 8), [])

    def test_ep08_pristine_robotiko_elsewhere_still_fires(self):
        s = _scene("the pristine chrome android at the center, undamaged", number=10)
        self.assertTrue(vpv.check_character_phase([s], 8))

    def test_ep06_foil_scene_ignored(self):
        s = _scene("two chrome android faces side by side, pristine on the right",
                   characters="", number=21)
        self.assertEqual(vpv.check_character_phase([s], 6), [])

    def test_ep06_pristine_robotiko_in_unlisted_scene_still_fires(self):
        s = _scene("the chrome android, pristine and undamaged chrome body", number=99)
        self.assertTrue(vpv.check_character_phase([s], 6))


class TestReferenceFirstGuard(unittest.TestCase):
    """The EP09 root-cause guard: scenes in a phase whose dedicated reference image
    is missing must FAIL — generate the reference first, then frame to it."""

    def setUp(self):
        self.profiles = vpv.load_profiles(REPO_ROOT)

    def _kintsugi_scene(self):
        # EP09 S30 is in the kintsugi scene-range (S27+).
        return {"scene_number": 30, "label": "S30", "characters": "Robotiko (Phase 3)",
                "text": "a chrome android", "ref_path": "", "upload": ""}

    def test_passes_when_dedicated_ref_exists(self):
        # Current state: android_kintsugi.png is registered and on disk.
        self.assertEqual(vpv.check_reference_first([self._kintsugi_scene()], 9, self.profiles), [])

    def test_catches_null_phase_ref(self):
        # The exact EP09 root cause: kintsugi scenes but no kintsugi reference.
        import copy
        p = copy.deepcopy(self.profiles)
        p["robotiko"]["reference_images"]["kintsugi"]["path"] = None
        self.assertTrue(vpv.check_reference_first([self._kintsugi_scene()], 9, p))

    def test_catches_declared_but_missing_file(self):
        import copy
        p = copy.deepcopy(self.profiles)
        p["robotiko"]["reference_images"]["kintsugi"]["path"] = "_assets/cast/does_not_exist.png"
        self.assertTrue(vpv.check_reference_first([self._kintsugi_scene()], 9, p))

    def test_ignores_scene_without_robotiko(self):
        # A non-Robotiko scene must not trip the guard even if a phase ref is null.
        import copy
        p = copy.deepcopy(self.profiles)
        p["robotiko"]["reference_images"]["kintsugi"]["path"] = None
        mech = {"scene_number": 6, "label": "S06", "characters": "The Mechanic",
                "text": "an old man at a bench", "ref_path": "", "upload": ""}
        self.assertEqual(vpv.check_reference_first([mech], 9, p), [])


class TestParserCoverage(unittest.TestCase):
    """The false-green that started TAKE 05: a scene parser that silently matches
    zero blocks reports PASS over an unchecked file. Guard it forever."""

    SHIPPED = [
        "episode-02/04_visuals/ep02_visual_prompts_v01.md",
        "episode-04/04_visuals/ep04_visual_prompts_v01.md",
        "episode-05/04_visuals/ep05_visual_prompts_v01.md",
        "episode-06/04_visuals/ep06_visual_prompts_v03.md",  # the "#### S11" format
        "episode-08/04_visuals/ep08_visual_prompts_v01.md",
        "episode-09/04_visuals/ep09_visual_prompts_v01.md",
    ]

    def _read(self, rel):
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as f:
            return f.read()

    def test_every_shipped_episode_parses_scenes(self):
        for rel in self.SHIPPED:
            scenes = vpv.extract_scenes(self._read(rel))
            self.assertGreater(
                len(scenes), 0,
                f"{rel} parsed ZERO scenes — ref-integrity would silently pass over nothing.",
            )

    def test_ep06_alternate_header_format_is_parsed(self):
        # EP06 uses "#### S11 —", not "#### Scene S11 —". Regression guard.
        content = self._read("episode-06/04_visuals/ep06_visual_prompts_v03.md")
        self.assertGreaterEqual(len(vpv.extract_scenes(content)), 30)

    def test_keyframe_pairs_get_distinct_labels(self):
        # S03a and S03b must not collapse to a single "S03".
        content = self._read("episode-04/04_visuals/ep04_visual_prompts_v01.md")
        labels = [s["label"] for s in vpv.extract_scenes(content)]
        self.assertIn("S03a", labels)
        self.assertIn("S03b", labels)


class TestPromptHygieneLint(unittest.TestCase):
    """The attribution lint, proven both ways: it catches a tradition label or a
    non-ASCII char leaking into an actual model-facing prompt string, and it leaves
    the canon (master.md, direction notes, the Dramaturgy Reference lines in the
    same file) untouched — out of scope by design, so the canon is never punished."""

    # A scene block whose CANON lines carry sanctioned Turkish + a tradition label,
    # but whose model-facing Text Prompt is clean plain-English ASCII.
    CLEAN_PROMPT_DIRTY_CANON = (
        "#### Scene S01 - Title\n"
        "- **Dramaturgy Reference:** A glass of çay; the Turkish wisdom tradition "
        "of Hacı Bektaş Veli. Canonical and required.\n"
        "- **Composition Notes:** dolmuş interior.\n"
        "\n"
        "**Text Prompt:**\n"
        "> a chrome android in a minibus interior, plain english, masterpiece.\n"
    )

    def test_catches_nonascii_in_prompt(self):
        content = (
            "**Text Prompt:**\n"
            "> a chrome android with a Hacı Bektaş engraving, masterpiece.\n"
        )
        findings = phl.lint_content(content, "Text Prompt")
        self.assertTrue(any(k == "non-ascii" for _, k, _ in findings))

    def test_catches_tradition_label_in_prompt(self):
        content = (
            "**Text Prompt:**\n"
            "> a chrome android beneath a banner reading the Turkish wisdom tradition, masterpiece.\n"
        )
        findings = phl.lint_content(content, "Text Prompt")
        self.assertTrue(any(k == "tradition-label" for _, k, _ in findings))

    def test_ignores_canon_outside_the_prompt_block(self):
        # The label + Turkish live in Dramaturgy/Composition lines, NOT the prompt.
        self.assertEqual(phl.lint_content(self.CLEAN_PROMPT_DIRTY_CANON, "Text Prompt"), [])

    def test_fix_is_scoped_and_idempotent(self):
        leak = (
            "- **Dramaturgy Reference:** çay, the Turkish wisdom tradition.\n"
            "\n"
            "**Text Prompt:**\n"
            "> a chrome android, Hacı engraving — masterpiece.\n"
        )
        once = phl.fix_content(leak, "Text Prompt")
        twice = phl.fix_content(once, "Text Prompt")
        self.assertEqual(once, twice, "fix must be idempotent")
        self.assertEqual(phl.lint_content(once, "Text Prompt"), [], "prompt must be ASCII after fix")
        self.assertIn("çay", once, "the out-of-scope Dramaturgy line must be left untouched")

    def test_scope_excludes_master_and_direction_notes(self):
        files = phl.in_scope_files(REPO_ROOT)
        self.assertTrue(files, "lint should resolve some in-scope files")
        for f in files:
            low = f.replace("\\", "/").lower()
            self.assertTrue(("/04_visuals/" in low) or ("/05_video/" in low),
                            f"in-scope file outside the two prompt dirs: {f}")
            for forbidden in ("master.md", "/03_direction/", "/02_music/",
                              "_concept_notes", "_dramaturgy", "_musical_metadata"):
                self.assertNotIn(forbidden, low, f"canon file leaked into scope: {f}")
        # Prove the exclusion is real, not vacuous: master.md exists but is not in scope.
        master = os.path.join(REPO_ROOT, "_management", "master.md")
        self.assertTrue(os.path.exists(master))
        self.assertNotIn(os.path.abspath(master), [os.path.abspath(x) for x in files])

    def test_all_shipped_prompts_are_ascii_clean(self):
        # Regression guard: every in-scope file stays clean after the normalization.
        for path in phl.in_scope_files(REPO_ROOT):
            self.assertEqual(phl.lint_file(path), [], f"{path} has prompt-hygiene issues")


class TestDocReferenceExistence(unittest.TestCase):
    """The doc-rot guard, proven both directions: a frozen doc with a dead
    backtick path must FAIL; a clean doc (with a tolerated historical hook
    mention, a _private/ path, a gitignored render output, and an inline-
    suppressed anti-example) must PASS with zero findings."""

    def _fails(self, findings):
        return [m for s, m in findings if s == "FAIL"]

    def test_bad_fixture_fails_on_missing_path(self):
        findings = drc.lint_doc_file("tests/fixtures/doc_ref_BAD.md", REPO_ROOT)
        fails = self._fails(findings)
        self.assertTrue(fails, "BAD fixture must fail: it names a nonexistent path.")
        self.assertTrue(
            any("does_not_exist_xyz.py" in m for m in fails),
            f"the dead path must be the reported failure. Got: {fails}",
        )

    def test_bad_fixture_real_path_is_not_the_failure(self):
        # tests/run_all.py in the same fixture must not be flagged.
        findings = drc.lint_doc_file("tests/fixtures/doc_ref_BAD.md", REPO_ROOT)
        self.assertFalse(any("run_all.py" in m for _, m in findings))

    def test_good_fixture_passes_clean(self):
        findings = drc.lint_doc_file("tests/fixtures/doc_ref_GOOD.md", REPO_ROOT)
        self.assertEqual(
            findings, [],
            f"GOOD fixture must pass with zero findings. Got: {findings}",
        )

    def test_private_and_render_paths_tolerated(self):
        # Isolate the two gitignored-by-design cases from the whole-file pass.
        toks = drc.extract_path_tokens(
            "see `_private/audit/x.md` and `episode-07/06_edit/final.mp4` "
            "and `episode-07/05_video/raw/`"
        )
        self.assertEqual(toks, [], f"gitignored-by-design paths must be dropped: {toks}")

    def test_dotpaths_survive_extraction(self):
        # Regression: the leading dot of .github / .claude must not be stripped.
        toks = drc.extract_path_tokens(
            "CI is `.github/workflows/validation_suite.yml` and `.claude/settings.json`."
        )
        self.assertIn(".github/workflows/validation_suite.yml", toks)
        self.assertIn(".claude/settings.json", toks)

    def test_current_tree_is_clean(self):
        # The curated docs on disk must stay green (this is what CI enforces).
        self.assertEqual(drc.scan_all_docs(REPO_ROOT), [])


class TestHookRotGuard(unittest.TestCase):
    """A present-tense claim about the removed naming hook must fire; a historical
    mention (with a nearby removed/was/once cue) or a suppressed line must not."""

    def test_catches_present_tense_hook_claim(self):
        lines = ["The `naming_check_hook.py` PostToolUse hook fires on every Write."]
        self.assertTrue(drc.scan_hook_claims(lines))

    def test_ignores_historical_mention_same_line(self):
        lines = ["The PostToolUse naming_check_hook was removed 2026-07-04."]
        self.assertEqual(drc.scan_hook_claims(lines), [])

    def test_ignores_historical_cue_on_adjacent_line(self):
        # The real wrap case: trigger on one line, the 'removed' cue on the next.
        lines = [
            "A Claude Code PostToolUse hook (`naming_check_hook.py`) once",
            "auto-checked naming. It was removed 2026-07-04.",
        ]
        self.assertEqual(drc.scan_hook_claims(lines), [])

    def test_suppression_marker_silences(self):
        lines = ["The naming_check_hook PostToolUse hook runs now. <!-- doc-ref: ignore -->"]
        self.assertEqual(drc.scan_hook_claims(lines), [])


class TestMatrixSync(unittest.TestCase):
    """Every enforcement check_ function must be represented in the coverage matrix
    or admitted as an internal helper; a new check with neither must be reported."""

    def test_current_tree_is_synced(self):
        self.assertEqual(drc.verify_matrix_sync(REPO_ROOT), [])

    def test_allowlisted_helper_is_internal_only(self):
        # check_episode is a genuine internal driver, not a standalone invariant.
        self.assertIn("check_episode", drc.ALLOWLIST)

    def test_named_checks_are_actually_in_the_matrix(self):
        with open(os.path.join(REPO_ROOT, drc.MATRIX_PATH), encoding="utf-8") as f:
            matrix = f.read()
        for name in ("check_ref_integrity", "check_reference_first", "check_suffix",
                     "check_forbidden_aesthetics", "check_character_phase"):
            self.assertIn(name, matrix, f"{name} must have a matrix row")

    def test_unrepresented_check_is_reported(self):
        # Inject a bogus check_ function absent from matrix + allowlist -> must FAIL.
        original = drc.collect_check_functions
        drc.collect_check_functions = lambda root: {
            "check_totally_unlisted_xyz": "tests/fake.py"
        }
        try:
            findings = drc.verify_matrix_sync(REPO_ROOT)
        finally:
            drc.collect_check_functions = original
        self.assertTrue(
            any("check_totally_unlisted_xyz" in m for _, m in findings),
            "an enforcement check with no matrix row and no allowlist entry must fail.",
        )


# ─────────────────────────────────────────────
# M4 real fix: the EP01 PDF-only skip is now VISIBLE (was inert).
# ─────────────────────────────────────────────

class TestPdfOnlySkipVisible(unittest.TestCase):
    """The audit found EP01 was silently skipped: its PDF lives in 04_visuals/selected/
    but the detector only listed the top level, so the skip branch never fired and no
    line printed at all. Lock BOTH: the recursive detector finds a subdir PDF, and the
    exact skip-message text so it can never silently vanish again."""

    def test_finds_pdf_in_selected_subdir_fixture(self):
        found = vpv.find_pdf_visuals(PDF_SUBDIR_VISUALS)
        self.assertTrue(found, "recursive detector must find the PDF in selected/.")
        self.assertTrue(found[0].endswith("ep01_visual_prompts_v01.pdf"))

    def test_finds_ep01_real_pdf_in_repo_tree(self):
        # The real regression: episode-01/04_visuals/selected/ep01_visual_prompts_v01.pdf
        found = vpv.find_pdf_visuals(os.path.join(REPO_ROOT, "episode-01", "04_visuals"))
        self.assertTrue(found, "EP01's real PDF (in selected/) must be found.")
        self.assertTrue(any("ep01_visual_prompts_v01.pdf" in p for p in found))

    def test_top_level_only_would_have_missed_it(self):
        # Prove the subdir is why the old code failed: nothing matches at the top level.
        top = [f for f in os.listdir(PDF_SUBDIR_VISUALS) if f.lower().endswith(".pdf")]
        self.assertEqual(top, [], "fixture must keep the PDF in a subdir, not top level.")

    def test_skip_message_text_is_stable_and_ascii(self):
        msg = vpv.pdf_skip_message("episode-01", "episode-01/04_visuals/selected/x.pdf")
        self.assertIn("Skipping episode-01", msg)
        self.assertIn("PDF-only visuals", msg)
        self.assertIn("pre-method episode", msg)
        self.assertEqual(msg, msg.encode("ascii", "ignore").decode(),
                         "skip line must be ASCII (no em-dash regression).")


# ─────────────────────────────────────────────
# Pipeline state machine + gates: grade the grader, both directions.
# The synthetic-input idiom keeps these hermetic (no fake episode on disk needed).
# ─────────────────────────────────────────────

REAL_EPISODES = [f"{n:02d}" for n in range(1, 11)]

# A real committed artifact + its true sha, for the sha-drift proofs.
EP02_DRAMA = "episode-02/03_direction/ep02_dramaturgy_v01.md"
EP02_DRAMA_SHA = "626619ac4159398f8969b395b7d7d9ee4d631fb7bac759a3482f755f3f24a9ee"


def _sev(findings, sev):
    return [m for s, m in findings if s == sev]


class TestNonSequentialSkipDetection(unittest.TestCase):
    """The EP01 shape: an empty non-blocking step (Visual Prompts) before a present
    later step (Motion Script) IS a skip — the old blocking-only check let it pass."""

    def test_detects_ep01_shape(self):
        # [lyrics, music, concept, dramaturgy, VISUALS-empty, motion, edit-empty]
        status = [True, True, True, True, False, True, False]
        self.assertEqual(pi.nonsequential_skips(status), [4])

    def test_contiguous_prefix_is_not_a_skip(self):
        # A fresh scaffold / in-progress episode: contiguous done prefix, no skip.
        self.assertEqual(pi.nonsequential_skips([True, True, True, False, False, False, False]), [])

    def test_empty_episode_is_not_a_skip(self):
        self.assertEqual(pi.nonsequential_skips([False] * 7), [])


class TestWaiverAwareness(unittest.TestCase):
    """EP01's skip passes ONLY because a waiver record exists; the same shape in a new
    episode with no waiver FAILS. Both directions, driven by a synthetic ledger."""

    EP01_SHAPE = [True, True, True, True, False, True, False]

    def test_real_ledger_has_ep01_waiver(self):
        ledger = pi.load_approvals(REPO_ROOT)
        self.assertTrue(ledger, "approvals ledger must load.")
        self.assertIsNotNone(pi.episode_waiver(ledger, "01"),
                             "EP01 must carry a waiver record in the ledger.")

    def test_new_episode_without_waiver_fails_on_same_shape(self):
        # Same disk shape as EP01 but a ledger with NO waiver for ep77 -> FAIL.
        ledger = [{"episode": "77", "gate": 1, "artifact": EP02_DRAMA,
                   "sha256": EP02_DRAMA_SHA, "date": "2026-01-01",
                   "note": "approved"}]
        _status, findings = _fake_check("77", self.EP01_SHAPE, ledger, {"video": True})
        skip_fails = [m for m in _sev(findings, "FAIL") if "skipped step" in m]
        self.assertTrue(skip_fails, f"unwaivered skip must FAIL. Got: {findings}")

    def test_same_shape_with_waiver_is_warn_not_fail(self):
        ledger = [{"episode": "77", "gate": 1, "artifact": EP02_DRAMA,
                   "sha256": EP02_DRAMA_SHA, "date": "2026-01-01",
                   "note": "visual prompts stage waived - legacy"}]
        _status, findings = _fake_check("77", self.EP01_SHAPE, ledger, {"video": True})
        skip_fails = [m for m in _sev(findings, "FAIL") if "skipped step" in m]
        self.assertEqual(skip_fails, [], f"waivered skip must not FAIL. Got: {findings}")
        self.assertTrue([m for m in _sev(findings, "WARN") if "skipped step" in m])


def _fake_check(ep, status, ledger, production):
    """Drive the per-episode finding assembly with a synthetic disk status, bypassing
    episode_status() so no fake episode folder is needed on disk. Mirrors check_episode."""
    findings = []
    waiver = pi.episode_waiver(ledger, ep)
    for i in pi.nonsequential_skips(status):
        step = pi.PIPELINE_STEPS[i]
        later = next((pi.PIPELINE_STEPS[j]["name"] for j in range(i + 1, len(status)) if status[j]), "later")
        detail = f"step {step['step']} ({step['name']}) is empty but a later step ({later}) is present -> skipped step"
        if waiver is not None:
            findings.append(("WARN", detail + " WAIVERED"))
        else:
            findings.append(("FAIL", detail + " no waiver"))
    findings.extend(pi.disk_declared_conflicts(status, production))
    findings.extend(pi.gate_findings(ep, status, ledger, production, REPO_ROOT))
    return status, findings


class TestDiskDeclaredStateMachine(unittest.TestCase):
    """Disk-ahead-of-declared is the provable contradiction; declared-ahead (gitignored
    renders / in-progress) is deliberately tolerated."""

    def test_disk_ahead_of_declared_fails(self):
        # Motion script present on disk, but metadata declares video not done.
        status = [True, True, True, True, True, True, False]
        findings = pi.disk_declared_conflicts(status, {"video": False, "visuals": True,
                                                        "dramaturgy": True, "timestamp_json": True,
                                                        "lyrics": True})
        fails = _sev(findings, "FAIL")
        self.assertTrue(any("production.video" in m for m in fails),
                        f"disk-ahead video must FAIL. Got: {findings}")

    def test_consistent_disk_and_declared_is_clean(self):
        status = [True, True, True, True, True, True, False]
        prod = {"lyrics": True, "timestamp_json": True, "dramaturgy": True,
                "visuals": True, "video": True}
        self.assertEqual(pi.disk_declared_conflicts(status, prod), [])

    def test_declared_ahead_is_tolerated(self):
        # Metadata says visuals done but disk has none yet (e.g. gitignored/in-progress).
        status = [True, True, True, True, False, False, False]
        prod = {"lyrics": True, "timestamp_json": True, "dramaturgy": True,
                "visuals": True, "video": True}
        self.assertEqual(pi.disk_declared_conflicts(status, prod), [])

    def test_in_progress_flag_counts_as_started(self):
        self.assertTrue(pi._truthy("in_progress"))
        self.assertTrue(pi._truthy("retroactive"))
        self.assertFalse(pi._truthy(False))
        self.assertFalse(pi._truthy(""))


class TestGateRecordsAsData(unittest.TestCase):
    """Artifacts beyond a gate demand a ledger record (FAIL if absent); a stale sha is
    a WARN, not a FAIL (post-approval em-dash cleanups are legitimate)."""

    # visuals+motion on disk, video in progress -> both gates are 'beyond'.
    FULL_STATUS = [True, True, True, True, True, True, False]
    PROD = {"lyrics": True, "timestamp_json": True, "dramaturgy": True,
            "visuals": True, "video": True}

    def test_missing_gate1_record_fails(self):
        findings = pi.gate_findings("77", self.FULL_STATUS, [], self.PROD, REPO_ROOT)
        self.assertTrue(any("gate-1" in m for m in _sev(findings, "FAIL")))

    def test_missing_gate2_record_fails(self):
        ledger = [{"episode": "77", "gate": 1, "artifact": EP02_DRAMA,
                   "sha256": EP02_DRAMA_SHA, "date": "2026-01-01", "note": "ok"}]
        findings = pi.gate_findings("77", self.FULL_STATUS, ledger, self.PROD, REPO_ROOT)
        self.assertTrue(any("gate-2" in m for m in _sev(findings, "FAIL")))

    def test_both_records_present_no_fail(self):
        ledger = [
            {"episode": "77", "gate": 1, "artifact": EP02_DRAMA,
             "sha256": EP02_DRAMA_SHA, "date": "2026-01-01", "note": "ok"},
            {"episode": "77", "gate": 2, "artifact": EP02_DRAMA,
             "sha256": EP02_DRAMA_SHA, "date": "2026-01-01", "note": "ok"},
        ]
        findings = pi.gate_findings("77", self.FULL_STATUS, ledger, self.PROD, REPO_ROOT)
        self.assertEqual(_sev(findings, "FAIL"), [])

    def test_sha_mismatch_is_warn_not_fail(self):
        ledger = [
            {"episode": "77", "gate": 1, "artifact": EP02_DRAMA,
             "sha256": "deadbeef" * 8, "date": "2026-01-01", "note": "ok"},
            {"episode": "77", "gate": 2, "artifact": EP02_DRAMA,
             "sha256": EP02_DRAMA_SHA, "date": "2026-01-01", "note": "ok"},
        ]
        findings = pi.gate_findings("77", self.FULL_STATUS, ledger, self.PROD, REPO_ROOT)
        self.assertEqual(_sev(findings, "FAIL"), [], "sha drift must not FAIL.")
        self.assertTrue(any("stale approval" in m for m in _sev(findings, "WARN")))

    def test_no_artifacts_beyond_gate_needs_no_record(self):
        # A scaffold-stage episode (nothing past dramaturgy) needs no ledger record.
        scaffold = [True, True, True, False, False, False, False]
        prod = {"lyrics": True, "timestamp_json": True}
        self.assertEqual(pi.gate_findings("77", scaffold, [], prod, REPO_ROOT), [])


class TestRealTreeStaysGreen(unittest.TestCase):
    """The whole point: today's real tree passes with the honest checks live. No
    episode may produce a FAIL against the committed ledger + metadata."""

    def test_no_episode_fails(self):
        ledger = pi.load_approvals(REPO_ROOT)
        metadata = pi.load_metadata(REPO_ROOT)
        for ep in REAL_EPISODES:
            status, findings = pi.check_episode(ep, ledger, metadata, REPO_ROOT)
            if status is None:
                continue
            fails = _sev(findings, "FAIL")
            self.assertEqual(fails, [], f"episode-{ep} must not FAIL. Got: {fails}")

    def test_ep01_is_the_one_waivered_skip(self):
        ledger = pi.load_approvals(REPO_ROOT)
        metadata = pi.load_metadata(REPO_ROOT)
        _status, findings = pi.check_episode("01", ledger, metadata, REPO_ROOT)
        waivered = [m for m in _sev(findings, "WARN") if "WAIVERED" in m]
        self.assertTrue(waivered, "EP01's PDF-only skip must appear as a waivered WARN.")

    def test_every_progressed_episode_has_both_gate_records(self):
        # EP01-EP09 all have artifacts past both gates -> both records must resolve.
        ledger = pi.load_approvals(REPO_ROOT)
        for ep in [f"{n:02d}" for n in range(1, 10)]:
            self.assertIsNotNone(pi.gate_record(ledger, ep, 1), f"EP{ep} missing gate-1 record")
            self.assertIsNotNone(pi.gate_record(ledger, ep, 2), f"EP{ep} missing gate-2 record")

    def test_ep10_has_no_ledger_records(self):
        # EP10 is a scaffold; it must NOT have been given approval records.
        ledger = pi.load_approvals(REPO_ROOT)
        self.assertEqual(pi.approvals_for(ledger, "10"), [])

    def test_ledger_sha_matches_disk_for_all_records(self):
        # Snapshot integrity: every recorded sha matches the artifact on disk today.
        ledger = pi.load_approvals(REPO_ROOT)
        for e in ledger:
            path = os.path.join(REPO_ROOT, e["artifact"])
            self.assertTrue(os.path.isfile(path), f"ledger artifact missing: {e['artifact']}")
            self.assertEqual(pi.sha256_file(path), e["sha256"],
                             f"ledger sha != disk sha for {e['artifact']}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
