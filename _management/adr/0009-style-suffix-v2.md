# ADR 0009 - Style-suffix variant family (photoreal short-film modifier)

- **Status:** Accepted (2026-07-05)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** Canon/style enforcement bundle (A2.8)

## Context

The mandatory visual suffix (`hyper-realistic, 70s progressive rock album art style,
Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic
lighting, volumetric fog, 8k resolution, masterpiece.`) is applied verbatim on every
prompt across the series, and `check_suffix` enforces it as an exact substring.

Starting with EP07, the series adopted an art-house short-film treatment (the "EP07+
pivot"). Every prompt in EP07 (8 prompts carry the modifier) and EP08 (24 prompts)
opens with **"Photorealistic, not a painting"** while STILL ending with the base
suffix. Read literally, "Photorealistic, not a painting" contradicts "70s progressive
rock album art style" - yet these prompts shipped and produced the intended look. The
contradiction is only apparent: the two strings steer different axes of the render.

A naive "the suffix must be the only style directive" stance would flag 32 shipped,
working prompts. Doing nothing leaves an undocumented, unpoliced contradiction that a
future contributor would either "fix" (breaking the look) or cargo-cult blindly.

## Decision

Canonize a small **variant family** of sanctioned style strings, documented in
`_assets/style/visual_dna.md`:

- **(a) base** - the classic mandatory suffix. Required on EVERY prompt, always.
  First used: EP01. Enforced by `check_suffix`.
- **(b) photoreal-shortfilm** - the base suffix PLUS the leading modifier
  "Photorealistic, not a painting". Use for the EP07+ art-house short-film treatment,
  where a literal painterly render is not wanted but the Kodachrome/grain/Frazetta-Mead
  DNA still must hold. First used: EP07 (S-level, waterside/embankment establishing
  prompts onward). The base suffix is never dropped - the modifier is additive.
- **Daylight / fog honesty note (no variant (c)).** We checked whether EP07's alpine /
  first-light and EP08's Day-Forty daylight scenes replaced "volumetric fog" with a
  daylight token. They did not - the base suffix (fog included) is applied verbatim
  even in daylight scenes. Rather than invent an unused "daylight variant", we record
  the honest finding: **"volumetric fog" is a known cargo-token in daylight prompts** -
  carried for consistency, not always literally rendered. Honesty over completeness; if
  a real daylight variant is ever authored, it gets its own ADR and fixture first.

Machine enforcement (`check_style_mode` in `tests/visual_prompt_validator.py`):

- The base suffix stays mandatory (`check_suffix`, unchanged).
- The photoreal modifier is **allowed (not flagged)** when the file DECLARES its style
  mode: a `## STYLE MODE` header note citing this ADR. EP07 and EP08 now carry that
  note.
- An **undeclared** photoreal modifier (present in a prompt, no STYLE MODE header) is a
  silent contradiction: **WARN** for legacy/unstamped files, **FAIL** for files whose
  header declares SKILL v2.0+ (the same severity model the motion-script validator
  uses). Fixtures prove both directions.

## Consequences

- The 32 shipped EP07/EP08 prompts are correct-by-declaration, not exceptions: their
  files now say WHY the modifier is there.
- A future file that sneaks in "Photorealistic, not a painting" without declaring STYLE
  MODE is caught (WARN, or FAIL once version-stamped) - the variant cannot spread
  silently.
- The suffix row in the Invariant Coverage Matrix becomes variant-aware.
- The doctrine lives in `visual_dna.md` (the style home) with a one-line pointer +
  ADR link in `master.md` Section 3.2.
