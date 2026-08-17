# Channel Banner — Spec (series-wide)

> Generation spec for the YouTube channel banner.
> Human generates using Nano Banana or equivalent image generation tool.

---

## DIMENSIONS

| Platform | Size | Notes |
|----------|------|-------|
| YouTube Banner | 2560 x 1440 px | Safe area: center 1546 x 423 px (visible on ALL devices) |

Other platforms are out of scope — distribution is YouTube-only.

**Critical:** The YouTube safe area (1546x423px center rectangle) must work as a standalone composition. Everything outside this zone may be cropped on mobile.

The shipped asset (`_assets/banner.png`) is 2752 x 1371 — generated wider than the spec target and uploaded as-is; the safe-area rule is what actually governs.

---

## COMPOSITION

> Channel art sits outside the episode state machine: the banner is the series' front door, not a frame from it, so Phase-1 pristine is deliberate here.

### Layout
- **Right third:** Robotiko Phase 1 — pristine chrome android, three-quarter or profile view facing left. Clean, unscratched, factory-fresh. Blue optical sensors. No damage, no rust, no cracks. This is the beginning.
- **Left two-thirds:** Deep negative space. Subtle circuit-board trace pattern fading into darkness — barely visible, like a watermark. This emptiness is intentional: the journey hasn't begun yet.
- **No text.** The channel name "Fibula" handles identity. The banner is pure visual.

### Subject Details (Robotiko Phase 1)
- Chrome/silver metallic body, highly reflective
- Blue optical sensors (NOT glowing — describe as: "steady blue optical lenses set into chrome sockets, like polished sapphires, reflecting ambient light")
- Smooth, undamaged surface — no battle scars, no rust, no patina
- Slight rim lighting from behind (cool blue) to separate from dark background
- Posture: still, composed, perhaps slightly upward gaze — the arrogance of certainty

### Background & Atmosphere
- Deep blue-black gradient (#0A0F1A to #141B2D)
- Faint circuit-board traces in the darkness (20% opacity max)
- Subtle volumetric fog at the bottom edge
- Warm amber accent light from the far left (Kodachrome warmth — #D4A574 at low intensity)
- This warm light hints at what's coming but doesn't dominate

### Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Deep background | #0A0F1A | Primary background |
| Mid background | #141B2D | Gradient mid-tone |
| Chrome body | #C0C0C0 | Robotiko's surface |
| Chrome highlight | #E8E8E8 | Specular reflections |
| Blue sensors | #4A90D9 | Robotiko's eyes/sensors |
| Kodachrome amber | #D4A574 | Subtle warm accent |
| Circuit traces | #1A2744 | Background pattern (subtle) |

---

## STYLE REQUIREMENTS

- 70s progressive rock album art aesthetic
- Film grain texture overlay (subtle, not heavy — this is a banner, not a scene)
- Kodachrome color rendering feel
- Cinematic lighting with strong contrast
- Frank Frazetta meets Syd Mead aesthetic language
- NO text, NO logos, NO watermarks

---

## IMAGE GENERATION PROMPT

Use this as a starting point (adjust for your tool):

```
Wide cinematic banner composition, 2560x1440 aspect ratio. Right side: a pristine chrome android in three-quarter view facing left, highly reflective silver-chrome body, pale blue glass lenses set into chrome sockets like polished sapphires, smooth undamaged surface, cool blue rim lighting from behind. Left side: deep blue-black negative space with barely visible circuit-board trace patterns fading into darkness. Bottom edge: subtle volumetric fog. Faint warm amber accent light from far left. Deep blue-black gradient background. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

**Post-generation check — what the generated image must satisfy:**
- Safe area (center 1546x423) works standalone
- Robotiko is pristine (no damage, no cracks)
- No text or logos in the image
- Blue eyes are NOT glowing/alien — they look like glass lenses
- Circuit traces are subtle (barely visible)
- Overall mood: still, confident, pre-journey

---

## BANNER EVOLUTION REFERENCE

This spec was originally designed as Banner v1 of a five-stage evolving arc:

| Phase | Episodes | Banner Change |
|-------|----------|---------------|
| v1 | EP01-03 | Pristine chrome, blue eyes, clean |
| v2 | EP04-05 | Subtle cracks visible on chrome surface |
| v3 | EP06-07 | Near-monochrome, fragmenting, mixed eye colors |
| v4 | EP08-09 | Dark with golden light seeping through cracks |
| v5 | EP10 (release day onward) | Full Kintsugi — cracked but whole, gold light from within |

**Decision (2026-08-12): single banner, series-wide.** This composition is the one
banner the channel runs for all ten episodes — see `_memory/decisions_log.md`
(2026-08-12 entry) for the full reasoning: YouTube's all-device safe area crops the
banner down to a wide horizontal strip, and what survives that crop here is the head
and eyes of the figure on the right, which still reads as a composition. The v2-v5
variants above were never produced. The table stays as the designed mechanism,
available to forks that want an evolving banner.

---

*"Would Fibula approve this?"*
