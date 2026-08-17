# CHARACTER REFERENCE IMAGE PROMPTS

> Generation prompts for the master character reference images used as the
> consistency anchors across all episodes (uploaded alongside scene prompts in
> Nano Banana / Omni References).
>
> **Status:** The reference images already exist in this folder — four character
> masters (`ref_robotiko_master.png`, `ref_mentor_master.png`,
> `ref_robochica_master.png`, `ref_mechanic.png`) plus Robotiko's body-state
> references (`android_damaged.png` with its `_2` / `_3` alt angles, and
> `android_kintsugi.png`).
>
> **Scope:** This file records TWO of those prompts — the Mentor and Robochica
> masters. They are the recorded examples of how a master reference is specified,
> kept so the images can be regenerated and so anyone forking the method can see
> exactly what a reference prompt has to carry. The remaining masters were
> generated before this file existed and their prompts were never written down —
> an honest gap, not a hidden one.
>
> Each prompt follows the PROMPT FORMULA and the eye-material rule from
> `_memory/lessons.md` + [ADR 0010](../../_management/adr/0010-eye-canon-reconciliation.md)
> (never write "glowing eyes"; describe eyes as a physical material). Every prompt
> ends with the mandatory visual suffix.

---

## THE MANDATORY VISUAL SUFFIX

Append to every prompt, no exceptions:

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## 1. THE COSMIC MENTOR — `ref_mentor_master.png`

**Profile:** `character_profiles.json` → `mentor`. Warm/organic counterpoint to
Robotiko's cold chrome. The amber staff tip is his single light source — his face
stays shadowed beneath the hood (do not describe glowing eyes).

```
Full-body character reference, centered, front view, full figure head to boots. A tall figure in a weathered dark green hooded cloak over a worn brown leather tunic and a wide leather belt, one gloved hand gripping a tall gnarled wooden staff topped with a raw amber crystal that glows warm gold. Standing still and grounded, a fellow traveler who has crossed the wasteland. Storm-grey mountain wasteland behind him, distant lightning, drifting dust. Dusk light and volumetric fog, the warm amber glow of the staff the only warm key against the cold storm tones. Face mostly shadowed beneath the hood — weathered, bearded, calm, eyes in shadow. One figure only, no other characters. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## 2. ROBOCHICA — `ref_robochica_master.png`

**Profile:** `character_profiles.json` → `robochica`. Same aesthetic universe as
Robotiko but feminine; warm gold/copper wires vs. his blue/red. Eyes use the
tested glass-lens material formula (never "amber glow"). One visual signature:
the fractal/mandala shoulder etching.

```
Full-body character reference, centered, front view, full figure head to feet. An elegant retro-futuristic chrome female android, 70s sci-fi feminine form with smooth curved chrome plating and an art-deco-influenced, slightly elongated head. The eyes are dark amber glass lenses set into chrome sockets, like polished gemstones — warm brown-gold, reflective, catching the environment light, not a light source. Exposed warm-toned analog wires in gold and copper at the joints. A fractal mandala pattern etched into the left shoulder plate, readable even in silhouette. Subtle scratches and minor wear marks on the chrome — she carries her own history, not pristine. Standing still in a neutral pose, arms relaxed at her sides. Warm amber-lit retro-futuristic workshop behind her, soft industrial haze. Warm Kodachrome key light tracing the chrome curves. Only one chrome android, no second robot. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## NOTES

- **Robotiko** (`ref_robotiko_master.png`) is the pristine Phase-1 master. For
  Phase-2 damaged scenes use `android_damaged.png` (+ `_2` / `_3` variants), not
  this pristine master — see `_memory/lessons.md` (cumulative damage rule).
- Upload the relevant master alongside the scene prompt; do **not** repeat the
  character's full physical description in scene prompts — the reference image
  carries the detail (see the Reference Image Workflow rules in `lessons.md`).
