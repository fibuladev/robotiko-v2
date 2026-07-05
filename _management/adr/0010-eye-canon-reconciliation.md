# ADR 0010 - Eye-canon reconciliation: appearance vs. prompt language

- **Status:** Accepted (2026-07-05)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** Canon/style enforcement bundle (A2.1)

## Context

Two of our own rules contradicted each other - the panel's most-repeated finding:

- **lessons.md rule #2 (Character Design, 2026-03-23/31)** bans ALL glow keywords for
  EYES in model-facing prompts. Three formulations failed generation ("amber eyes",
  "warm glow radiating around eyes", "no glow / no luminescence" - the last produced
  cyan glowing eyeballs). The tested, working formula is material-lens language:
  Robochica's *"dark amber glass lenses set into chrome sockets, like polished
  gemstones"*.
- **`character_profiles.json` (a LIVE production input) and `master.md`** described
  Robotiko's eyes with glow language: `base_visual_prompt` said "glowing blue eyes",
  the per-phase `visual_prompt_addition` fields said "glowing steady blue eyes",
  master.md Sec 3.3 said "Neon Blue" and Sec 4.1 "Glowing blue eyes". These strings
  would feed EP10 prompts (and any re-generation) directly.

On screen, Robotiko's eyes DO emit a steady blue light - that is real, intended
appearance. But the moment that appearance is written into a MODEL-FACING string, the
generator renders literal glowing eyeballs. The contradiction is only apparent.

## Decision

Apply the repo's own **scope-by-audience** principle (the ADR-0006 precedent) and
distinguish two layers:

- **Canonical APPEARANCE (canon layer).** master.md and the direction notes MAY
  describe Robotiko's eyes as emitting steady blue light - that is the on-screen truth
  and the philosophical core (blue = healthy/curious; red = error; glitch = fracture).
  Canon is not punished. master.md keeps its appearance language, with a one-line
  pointer that PROMPTS never say glow for eyes (this ADR).
- **PROMPT LANGUAGE (model-facing layer).** Any string a generator reads - the prompt
  fields in `character_profiles.json`, and the `Text Prompt` blockquotes in
  visual-prompt files - must use the tested material-lens idiom for eyes. Robotiko's
  formula parallels the proven Robochica one:
  *"steady blue optical lenses set into chrome sockets, like polished sapphires"*
  (flickering blue-red for the Phase-2 fracture; calm steady blue for Phase-3 kintsugi).

Machine guard (an eye-glow lint, both surfaces):

- `eye_glow_hits(text)` (in `tests/visual_prompt_validator.py`) is the single detector:
  a glow-family keyword (`glow/glowing/glows/glowed/luminous/luminescent/...`) within 3
  word-tokens of an eye/lens word (`eye/eyes/lens/lenses/optical/socket/ocular`).
- **Scope: model-facing strings only.** `check_eye_glow` reads the `Text Prompt`
  blockquotes; `character_profiles_validator.scan_eye_glow` reads the prompt-bearing
  JSON fields. Neither opens master.md or the direction notes - canon keeps its
  appearance language, exactly as ADR-0006 keeps the sanctioned Turkish out of the
  ASCII lint's reach.
- **Allowlist - kintsugi body gold-glow.** "cracks filled with glowing gold light" and
  "bioluminescent core" are canon and generation-safe (they describe the BODY, not the
  eyes). A glow keyword bound (+-1 token) to a body-gold noun is exempt; the eye-only
  proximity keeps "glowing amber-gold eyes" (eye colour) still caught.
- **Curation - "light" is not a glow keyword.** EP07's Dual Device uses canonical
  lens-PROJECTION language ("a pale light from his optical lenses"), which is
  generation-safe. Flagging "light" would punish it, so only emissive glow verbs count.
- **Severity.** FAIL for the live input (`character_profiles.json`) and for files whose
  header declares SKILL v2.0+; WARN for shipped, unstamped visual-prompt files (EP02-09
  era), which are measured legacy debt and are NOT retrofitted (see the EP02 legacy
  header notes). A full-tree sweep confirmed the only v2-would-be-FAIL hit is EP09 S31's
  "self-luminous" - a shipped prompt, correctly WARN'd, not rewritten.

## Consequences

- The eye rule graduates from a documented ⚪ Gap to 🟢 Machine in the Invariant
  Coverage Matrix - the last of the three original gaps (anti-spawn and motion
  video-suffix closed in the 2026-07-04 audit) to close.
- `character_profiles.json` and `master.md` now agree: appearance in canon, lenses in
  prompts.
- The guard is narrow by design. A future model-facing surface that carries eye
  descriptions must be added to the lint explicitly - silence is not coverage.
