"""
Robotiko v2.0 — Universe Configuration (the single source for validator constants).

Forking? Change your universe's constants HERE and only here — the gate stays green
because fixtures derive from this module too.

WHY THIS FILE EXISTS
--------------------
The validator suite enforces universe-SPECIFIC rules: every visual prompt must end
with ROBOTIKO's mandatory style suffix, every motion prompt with the video suffix,
certain aesthetics are forbidden, and every motion prompt must carry an anti-spawn
guard. Before this module, those strings were hardcoded inside
visual_prompt_validator.py and motion_script_validator.py. A forker who followed
CONTRIBUTING §3 step 4 ("set your own mandatory suffix in CLAUDE.md") got a RED gate
on their first `run_all`: the skills read CLAUDE.md, but the validators still demanded
the ROBOTIKO suffix from a string the forker never saw. This module is the one place a
forker edits to re-point the gate at their own universe.

Defaults below are the current ROBOTIKO values, verbatim. Changing a value here
changes both the validator AND the meta-test fixtures that derive from it (the
meta-tests import these names rather than re-typing the strings), so the gate follows
your universe instead of fighting it.

WHAT LIVES HERE vs. WHAT DELIBERATELY DOES NOT
----------------------------------------------
IN (universe-specific — a different universe would legitimately change these):
  * VISUAL_SUFFIX / VIDEO_SUFFIX — the mandatory style/motion suffixes.
  * FORBIDDEN_AESTHETICS — aesthetics ROBOTIKO's art direction bans.
  * ANTI_SPAWN_GUARD / ANTI_SPAWN_ALTERNATIVES — the canonical anti-spawn phrase and
    its recognized paraphrases.
  * PHOTOREAL_MODIFIER — the ROBOTIKO-specific alternate render aesthetic (EP07+
    art-house short films open with "Photorealistic, not a painting"). This is a
    universe styling choice: a forker whose base look is, say, cel-shaded anime would
    have a different — or no — sanctioned variant modifier, so it belongs here.

OUT (deliberately NOT hoisted — these are not universe styling):
  * The eye-glow keyword lists (GLOW_WORDS / EYE_WORDS / BODY_GLOW_NOUNS in
    visual_prompt_validator.py). These encode GENERATION PHYSICS, not universe style:
    glow keywords adjacent to eye/lens words empirically break image generation
    regardless of which universe you author (three failed formulations documented in
    lessons.md). A forker inherits the same generator constraint, so the list stays
    with the check that owns it.
  * STYLE_MODE_MARKER ("style mode") stays in the validator. It is the generic
    MECHANISM — "declare your variant in the file header" — not a universe aesthetic.
    Only the modifier string a header sanctions (PHOTOREAL_MODIFIER) is
    universe-specific; the "declare it in the header" convention is universal, so the
    variant family is split along that seam on purpose.
"""

# ─────────────────────────────────────────────
# MANDATORY SUFFIXES
# ─────────────────────────────────────────────

# Appended to every visual prompt (visual_prompt_validator.check_suffix).
VISUAL_SUFFIX = (
    "hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets "
    "Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, "
    "volumetric fog, 8k resolution, masterpiece."
)

# Appended to every motion prompt (motion_script_validator video-suffix check).
VIDEO_SUFFIX = (
    "Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, "
    "heavy film grain, shallow depth of field."
)

# ─────────────────────────────────────────────
# PROTAGONIST BINDING (visual_prompt_validator character-phase / ref-integrity)
# The visual-prompt checks that enforce "the protagonist renders in the phase-correct
# body state" need to know (a) which top-level key in character_profiles.json is the
# protagonist, and (b) the identifier strings that mark a scene as featuring them.
# A fork with a different lead re-points these two names; the checks then either
# enforce the fork's own phase machine or, if the key is absent, degrade to no-ops
# (they never crash on a foreign cast). Defaults are the ROBOTIKO values.
# ─────────────────────────────────────────────

PROTAGONIST_KEY = "robotiko"
PROTAGONIST_IDENTIFIERS = ["robotiko", "chrome android"]

# ─────────────────────────────────────────────
# FORBIDDEN AESTHETICS (visual_prompt_validator.check_forbidden_aesthetics)
# ─────────────────────────────────────────────

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

# ─────────────────────────────────────────────
# ANTI-SPAWN GUARD (motion_script_validator)
# The canonical phrase plus the recognized paraphrases a motion prompt may use.
# ─────────────────────────────────────────────

ANTI_SPAWN_GUARD = "Do not add extra characters. Keep everything as pictured."
ANTI_SPAWN_ALTERNATIVES = [
    "No third figure",
    "Exactly two instances",
    "no additional characters",
    "no other figures",
]

# ─────────────────────────────────────────────
# STYLE-SUFFIX VARIANT FAMILY (ADR-0009)
# The base suffix (VISUAL_SUFFIX) is always required. EP07+ art-house short films may
# ALSO open the prompt with this photoreal modifier, but only when the file declares a
# STYLE MODE in its header (the marker convention lives in the validator). See the
# module docstring for why only the modifier — not the marker — is universe-specific.
# ─────────────────────────────────────────────

PHOTOREAL_MODIFIER = "photorealistic, not a painting"
