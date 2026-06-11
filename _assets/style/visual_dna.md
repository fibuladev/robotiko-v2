# VISUAL DNA — ROBOTIKO v2.0

> The visual contract every image and video must obey. The source of truth for
> story and character is `_management/master.md`; this file distills the *look*.

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

Robotiko's healthy eyes are steady blue (read as material/light, not a glow).
Robochica's are amber glass lenses. See `_memory/lessons.md` (Character Design).

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
