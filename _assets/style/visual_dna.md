# VISUAL DNA — ROBOTIKO v2.0

> The visual contract every image and video must obey. The source of truth for
> story and character is `_management/master.md`; this file distills the *look*.
> This doctrine is **shown, not just asserted**, in [docs/visual-canon.md](../../docs/visual-canon.md) — 67 curated frames that prove each rule below on disk.

---

## THE LOOK

70s progressive-rock album art: **Frank Frazetta meets Syd Mead**. Hyper-real,
hand-painted weight, analog warmth — never clean, never sterile, never digital-slick.
Kodachrome film stock, heavy grain, volumetric fog, cinematic lighting.

- **Aspect ratio:** 16:9 (always specify in image prompts — Nano Banana defaults to 1:1 otherwise).
- **Letterbox:** final edits are masked to 2.35:1 in CapCut.
- **Grain is non-negotiable.** Analog decay over digital polish, always.

---

## MANDATORY VISUAL SUFFIX

Every image prompt ends with this, verbatim, no exceptions:

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

### Style-suffix variant family (ADR-0009)

The suffix above is the **base** variant, required on every prompt, always. There is a
small sanctioned family of style strings - use only these, and declare the non-base one:

- **(a) base** - the classic suffix above. First used EP01. Enforced by `check_suffix`.
- **(b) photoreal-shortfilm** - the base suffix PLUS a leading modifier
  `Photorealistic, not a painting`. This is the EP07+ art-house short-film treatment:
  the base suffix keeps the Kodachrome / grain / Frazetta-meets-Syd-Mead album-art DNA,
  while the modifier steers the render away from a literal painterly look. First used
  EP07 (8 prompts), continued EP08 (24 prompts). The base suffix is never dropped - the
  modifier is additive. A file using it MUST carry a `## STYLE MODE` header note citing
  ADR-0009, or `check_style_mode` flags it (WARN legacy / FAIL version-stamped).
- **daylight + fog (honest cargo-token, not a variant).** Alpine / first-light and
  Day-Forty daylight scenes still ship the base suffix verbatim - "volumetric fog" is
  carried even in daylight, a known cargo-token kept for consistency, not always
  literally rendered. No unused "daylight variant" was invented (honesty over
  completeness). Full reasoning: [ADR 0009](../../_management/adr/0009-style-suffix-v2.md).

## MANDATORY VIDEO SUFFIX

Every motion prompt ends with this, verbatim:

```
Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.
```

---

## FORBIDDEN AESTHETICS

No generic cyberpunk neon. No Pixar / cartoon / anime. No smooth plastic, sleek
modern, "clean Apple design". No obvious 3D-render / Unreal-Engine look. The
naming/visual validators (`tests/visual_prompt_validator.py`) enforce this list.

---

## EYES (the most-tested rule)

Never write "glowing eyes", "amber glow", "aura around eyes", or any negative glow
phrase ("no glow") — image generators render any of these as literal glowing
eyeballs. Describe eyes as a **physical material** instead:

> dark amber glass lenses set into chrome sockets, like polished gemstones — warm
> brown-gold tone, reflective, catching the environment light on their smooth
> curved surface.

Robotiko's healthy eyes are steady blue (read as material/light, not a glow):
*"steady blue optical lenses set into chrome sockets, like polished sapphires"* -
the blue parallel of Robochica's amber glass lenses. On screen his eyes DO emit steady
blue light (canonical appearance); PROMPTS never say glow for eyes (two-layer doctrine,
[ADR 0010](../../_management/adr/0010-eye-canon-reconciliation.md)). This is now
machine-enforced on both model-facing surfaces (`character_profiles.json` prompt fields
and Text Prompt blockquotes). See `_memory/lessons.md` (Character Design).

---

## COLOR & CHARACTER STATE

- **Amber** is the colour of truth and the Mentor's trace. Use sparingly — at most
  one warm amber moment per episode (the "Amber Pulse"). Forced amber is worse than none.
- **Character state is a machine, not a mood.** Robotiko's damage is cumulative and
  phase-bound — always copy the episode-correct `visual_prompt_addition` from
  `_assets/cast/character_profiles.json` (Phase 1 pristine → Phase 2 damaged →
  Phase 3 kintsugi). "Pristine" is a continuity error after EP01.
- **Per-episode palette journeys** keep the single suffix from reading as monotony
  (e.g. EP07 wet grey-blue, EP08 cold grey → fire orange-red → warm Day-Forty daylight).

---

## REFERENCE-IMAGE-FIRST

Generate a master/episode reference image before scene images and upload it
alongside each prompt (`_assets/cast/reference_image_prompts.md`). When a reference
is provided, do NOT repeat the character's physical description in the prompt — the
reference carries it; describing it again causes over-interpretation.

---

*Glitch is metaphor only. In production, AI artifacts are defects to fix — maximum
quality is always the target.*
