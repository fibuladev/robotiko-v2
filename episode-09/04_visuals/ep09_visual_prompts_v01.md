# VISUAL PROMPT TEMPLATE (NANO BANANA)
> **Version:** 2.0 | Skill: `_skills/robotiko-visual-prompts/SKILL.md`
> This template is auto-populated by Claude. Do not fill manually.

---

## PRE-GENERATION CHECKLIST (Claude reads these before writing a single prompt)

- [ ] `_management/master.md` → Visual DNA, color palette, forbidden list, mandatory suffix
- [ ] `episode-09/03_direction/ep09_dramaturgy.md` → APPROVED scene breakdown
- [ ] `_assets/cast/character_profiles.json` → Character visual state + visual_prompt_addition for this phase
- [ ] `_assets/cast/ref_robotiko_master.png` → Visual reference (if Robotiko appears)
- [ ] `_assets/cast/ref_mentor_master.png` → Visual reference (if Mentor appears)

> ⚠️ Dramaturgy must be APPROVED before this file is generated.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP09 |
| **Title** | [Episode Title] |
| **Station** | [The X Self] |
| **Character Phase** | [Phase 1 / 2 / 3] |
| **Robotiko Visual State** | [Exact visual_prompt_addition from character_profiles.json] |
| **Total Prompts** | [Number] |

---

## MANDATORY STYLE SUFFIX
> ⛔ This suffix must be appended to EVERY prompt without exception. Do not modify.

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## FORBIDDEN AESTHETICS REMINDER
- ❌ Clean Apple design
- ❌ Pixar-style rendering
- ❌ Generic cyberpunk neon
- ❌ Smooth plastic textures
- ❌ Cheap melodrama or ornamental excess

---

## GENERATED PROMPTS

### SECTION: [Section Name from Dramaturgy — e.g., "INTRO & AWAKENING (0:00 - 0:42)"]

---

#### Scene S{XX} — [Scene Title]
- **Timestamp:** [MM:SS]
- **Dramaturgy Reference:** [Brief scene description from approved dramaturgy]
- **Characters Present:** [List — with phase-appropriate visual state noted]
- **Image Reference Path:** `_assets/cast/ref_{character}_master.png` *(or N/A if no characters)*
- **Video Tech Strategy:** [Standard / Start-End Keyframes / Extension]
- **Composition Notes:** [Headroom for camera movement, breathing space, depth — never tight crops]
- **Upload:** [Per-scene ref images: `char_ref.png` + `env_ref.png` + chain: S{XX} output + special: path]

**Text Prompt:**
> [Full scene description]. [Character visual state if present]. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S{XX} — [Scene Title]
- **Timestamp:** [MM:SS]
- **Dramaturgy Reference:** [...]
- **Characters Present:** [...]
- **Image Reference Path:** [...]
- **Video Tech Strategy:** [...]
- **Composition Notes:** [...]

**Text Prompt:**
> [...], hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: [Next Section Name]

*(Continue pattern for all scenes)*

---

## QUALITY CHECKLIST (Claude self-validates before delivery)

- [ ] Every prompt ends with the mandatory style suffix
- [ ] Every scene with a character references the correct master image path
- [ ] Character visual state matches the episode's phase (no pristine Robotiko in Phase 2)
- [ ] No forbidden aesthetics present in any prompt
- [ ] All prompts composed with headroom and breathing space
- [ ] Total prompt count matches approved dramaturgy scene count