# SKILL: robotiko-visual-prompts
> **Version:** 1.0 | **Last Updated:** 2026-02-24
> **Trigger:** `"Generate visual prompts for EP{XX}"`
> **Output:** `episode-{XX}/04_visuals/ep{XX}_visual_prompts_v{VV}.md`

---

## PURPOSE

Convert an approved dramaturgy document into standalone image generation prompts for Nano Banana. Each scene from the dramaturgy becomes a single, self-contained text prompt that an image generation model can execute without any additional context. The prompt must encode the full visual intent: scene composition, character state, lighting, texture, and the mandatory style suffix.

---

## PREREQUISITE

> **The dramaturgy for this episode MUST be human-approved before this skill executes.**
> If the dramaturgy has not been approved, STOP. Do not generate visual prompts from unapproved scene breakdowns.

---

## MANDATORY INPUTS (Read Before Writing a Single Prompt)

Read these files in this exact order:

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/master.md` | Visual DNA (Section 3), color palette, forbidden aesthetics, mandatory suffix |
| 2 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Approved scene breakdown — this is your primary input |
| 3 | `_assets/cast/character_profiles.json` | Character `visual_prompt_addition` for this episode's phase, `master_ref_path`, eye color logic |
| 4 | `_assets/cast/ref_robotiko_master.png` | Visual reference image (if Robotiko appears in the episode) |
| 5 | `_assets/cast/ref_mentor_master.png` | Visual reference image (if Mentor appears in the episode) |
| 6 | `_templates/visual_prompt_template.md` | Output structure and formatting template |

**If the approved dramaturgy file is missing:** STOP. The pipeline requires human-approved dramaturgy before visual prompts can be generated.

---

## THE MANDATORY VISUAL SUFFIX

This exact string is appended to the end of every single prompt. No exceptions. No modifications. No omissions.

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## PRE-GENERATION ANALYSIS

### Step 1: Confirm Character Phase
- From `character_profiles.json`, extract the `visual_prompt_addition` for this episode's phase.
- This exact string will be embedded in every prompt where that character appears.
- Cross-reference with the dramaturgy header to confirm phase alignment.

### Step 2: Identify Character Appearances
- Scan the dramaturgy scene table for the "Characters" column.
- For each character that appears, note:
  - Which scenes they appear in
  - Their `master_ref_path` for image reference
  - Any scene-specific state changes (e.g., "eyes glitching red" in a crisis moment)

### Step 3: Map Mood/Lighting Palette
- From the dramaturgy "Mood / Lighting" column, extract the color and atmosphere keywords.
- Ensure consistency with master.md color palette:
  - Cold blues, silver highlights → AI / Chrome / Cold
  - Golden oranges, amber → Human warmth / Energy / Kodachrome
  - Deep shadows against bright highlights → Contrast
  - Neon blue → Robotiko eyes (healthy)
  - Red → Robotiko eyes (error/danger)
  - Gold → Data / Energy flows
  - Glowing raw amber → Mentor's staff tip

### Step 4: Note Composition Requirements
- Check each scene's composition notes from the dramaturgy.
- Every prompt must describe compositions with enough space for camera movement (headroom + breathing space).
- Never generate tight crops that leave no room for the Motion Script's camera moves.

---

## PROMPT GENERATION RULES

### Rule 1: One Scene = One Prompt
- Each scene (S01, S02, S03...) from the dramaturgy becomes exactly one text prompt.
- The prompt must be completely self-contained — the image generation model has no memory of other prompts.
- Total prompt count must match the approved dramaturgy scene count.

### Rule 2: Prompt Structure
Every prompt follows this internal structure (written as continuous prose, not labeled sections):

```
[Subject/Action] + [Environment/Setting] + [Lighting/Atmosphere] + [Character Visual State if present] + [Texture/Material Details] + [Mandatory Suffix]
```

The prompt reads as a single flowing description, not as a bulleted list.

### Rule 3: Character Embedding
When a character appears in a scene:
- Embed the full `visual_prompt_addition` string from `character_profiles.json`
- Reference any scene-specific eye state or damage state from the dramaturgy
- Do NOT use vague references like "Robotiko" alone — always include visual descriptors

**Example — Robotiko in Phase 1:**
> A retro-futuristic chrome android with pristine chrome body, clean exposed analog wires (blue and red), glowing steady blue eyes, no damage, full armor, retro-futuristic 70s mechanical aesthetic, standing at the edge of...

**Example — Robotiko in Phase 2:**
> A retro-futuristic chrome android with rusted and cracked chrome chassis, sparks flying from joints, glitching blue-red eyes, exposed and fraying analog wires, battle-damaged retro-futuristic body, kneeling on...

### Rule 4: Environmental Specificity
- Never write generic environments ("a futuristic city", "a dark room").
- Always describe specific textures, materials, depth layers, and light sources.
- Ground the scene in the 70s Prog Rock aesthetic: analog, industrial, painterly.
- Include foreground/midground/background layering when the dramaturgy calls for depth.

### Rule 5: Lighting as Storytelling
- Lighting direction and quality must be specified in every prompt.
- Use lighting to reinforce the emotional beat:
  - Harsh side-lighting → Conflict, revelation
  - Warm backlight (amber/golden) → Hope, wisdom, the Mentor's presence
  - Cold overhead light → Isolation, clinical, system control
  - Volumetric fog with rim light → Mystery, transition, liminality
  - Dying light / dusk → Loss, fading, the Mentor's departure

### Rule 6: The Forbidden List (Hard Reject)
Every prompt is checked against these. If any of these appear, rewrite:
- Clean, sterile, or Apple-style design
- Pixar or cartoon rendering
- Generic cyberpunk neon glow
- Smooth plastic textures
- Modern UI elements (unless satirically intended and noted in dramaturgy)
- Cheap melodrama or ornamental excess

### Rule 7: Composition for Motion
- Compose every scene with 20-30% extra space in the direction of likely camera movement.
- Headroom: Leave space above subjects for potential tilt-up.
- Breathing space: Leave lateral space for potential pan.
- Depth: Include clear foreground/background separation for parallax potential.
- Never frame a subject dead-center filling the entire frame — the Motion Script needs room.

### Rule 8: Consistency Within an Episode
- The same character must look identical across all prompts within an episode.
- Environment transitions should be gradual unless the dramaturgy specifies a hard cut.
- Color temperature should flow with the musical energy arc (cold → warm or vice versa).
- Recurring elements (Mentor's staff, Robotiko's exposed wires) must be described identically each time.

---

## OUTPUT FORMAT

Use the template from `_templates/visual_prompt_template.md`. The output document contains:

### 1. Episode Header
| Field | Value |
|---|---|
| Episode | EP{XX} |
| Title | [from dramaturgy] |
| Station | [from dramaturgy] |
| Character Phase | [Phase 1 / 2 / 3] |
| Robotiko Visual State | [exact `visual_prompt_addition`] |
| Total Prompts | [must match dramaturgy scene count] |

### 2. Mandatory Style Suffix
Displayed once at the top as a reference block.

### 3. Forbidden Aesthetics Reminder
Quick reference of what must never appear.

### 4. Generated Prompts (Grouped by Musical Section)
Prompts are grouped under section headers matching the dramaturgy's musical structure (e.g., "INTRO & AWAKENING (0:00 - 0:42)").

Each prompt block contains:

| Field | Description |
|---|---|
| **Scene ID** | S{XX} — matches dramaturgy Shot ID |
| **Scene Title** | Brief descriptive title |
| **Timestamp** | From dramaturgy |
| **Dramaturgy Reference** | 1-sentence summary of the dramaturgy's scene description |
| **Characters Present** | List with phase-appropriate visual state noted |
| **Image Reference Path** | `_assets/cast/ref_{character}_master.png` or N/A |
| **Video Tech Strategy** | Standard / Start-End Keyframes / Extension (from dramaturgy detail blocks) |
| **Composition Notes** | Headroom, breathing space, depth guidance |
| **Text Prompt** | The full image generation prompt ending with the mandatory suffix |

### 5. Quality Checklist
Self-validation checklist at the bottom of the document.

---

## PROMPT WRITING GUIDE

### DO:
- Write in descriptive prose, present tense
- Be specific about materials: "oxidized copper", "brushed titanium", "cracked obsidian"
- Specify light sources: "amber light spilling from a crack in the ceiling"
- Include atmospheric elements: "dust motes caught in a shaft of cold light"
- Describe textures: "film grain visible across the frame", "paint-like smearing on chrome surfaces"
- Embed character visual state as integral description, not as a footnote
- End every prompt with the mandatory suffix — no exceptions

### DON'T:
- Use abstract or emotional language that an image model cannot render ("feeling of existential dread")
- Stack synonyms ("dark, gloomy, shadowy, dim, murky")
- Write camera directions (pan, zoom, tilt) — those belong to the Motion Script
- Use negative prompts or "do not" instructions — write what IS there, not what ISN'T
- Reference other scenes ("similar to S05") — each prompt must be self-contained
- Forget the suffix — this is a termination-level error in the pipeline

### EXAMPLE (Good):
> A retro-futuristic chrome android with pristine chrome body, clean exposed analog wires (blue and red), glowing steady blue eyes, no damage, full armor, retro-futuristic 70s mechanical aesthetic, standing on a rusted metal platform overlooking an endless desert of circuit boards and dead silicon wafers. The ground crunches with broken transistors. A single amber spotlight from above carves deep shadows across the android's chrome torso. Volumetric dust rises from the desert floor. In the far background, the skeletal remains of a massive server farm dissolve into heat haze. The sky is bruised purple and copper, like an overexposed Kodachrome slide left in the sun. hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

### EXAMPLE (Bad):
> Robotiko standing in a desert looking cool and futuristic. The lighting is dramatic and moody. He looks amazing and powerful. 8k masterpiece.

---

## HANDLING SPECIAL CASES

### Scenes Without Characters (Environmental / Atmospheric)
- These prompts focus entirely on environment, texture, and mood.
- Describe the space as if it is a character: give it material, history, decay.
- Still apply the mandatory suffix.
- Still compose with headroom and breathing space.

### Scenes With Multiple Characters
- Describe spatial relationship between characters (distance, relative position, eye contact or avoidance).
- Each character gets their full `visual_prompt_addition` embedded.
- If characters are in different phases (e.g., Robotiko damaged, Mentor pristine), the contrast must be explicit.

### Crowd, Audience, and Background Figures
- All crowd, audience, mob, and group scenes MUST include mixed gender representation — never uniform rows of identical male figures.
- Background figures should be described as intentionally abstract: "dark silhouettes", "featureless shapes", "impressionistic figures" — NOT as detailed realistic people.
- This is a deliberate aesthetic choice: video generators will attempt to "clarify" ambiguous figures into photorealistic humans, which breaks the 70s Prog Rock album art style. Keeping figures abstract in the source image prevents this.
- Specify demographics explicitly: "mixed men and women", "diverse crowd", "varied silhouettes" — never leave crowds as implicitly all-male.

### Scenes Requiring Start/End Keyframes
- The dramaturgy may flag scenes for Start/End keyframe video strategy.
- Generate TWO prompts for these scenes: one for the start frame, one for the end frame.
- Label them: `S{XX}a` (start) and `S{XX}b` (end).
- The transformation between start and end must be visually clear and achievable by the video generation model.

### Satirical or Ironic Scenes (e.g., EP02's Global Collapse Tour)
- The prompt describes the literal visual content, not the irony.
- Irony lives in the juxtaposition of what we see and what we hear — the image model only handles the visual.
- If the dramaturgy calls for "Robotiko preaching to a crowd of factory workers while wearing a startup hoodie", describe that literally and specifically.

---

## VERSIONING

- First output is always `v01`.
- If the human requests revisions after reviewing, increment: `v02`, `v03`, etc.
- Each version is a complete document, not a diff.
- Version number in the filename: `ep{XX}_visual_prompts_v{VV}.md`

---

## POST-GENERATION CHECKLIST

Before delivering the visual prompts to the human, verify:

- [ ] Every single prompt ends with the mandatory style suffix (check every one — no exceptions)
- [ ] Every scene with a character includes the full `visual_prompt_addition` from character_profiles.json
- [ ] Every scene with a character references the correct `master_ref_path`
- [ ] Character visual state matches the episode's phase (no pristine Robotiko in Phase 2/3)
- [ ] No forbidden aesthetics appear in any prompt (clean, sterile, neon cyberpunk, Pixar, smooth plastic)
- [ ] All prompts have composition space (headroom + breathing space) for future camera movement
- [ ] Total prompt count matches the approved dramaturgy scene count
- [ ] Start/End keyframe scenes have two prompts (S{XX}a and S{XX}b)
- [ ] Environmental prompts have specific textures and materials, not vague descriptions
- [ ] Lighting direction is specified in every prompt
- [ ] No prompt references another prompt — each is fully self-contained
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## WHAT HAPPENS NEXT

After visual prompts are delivered:
1. Human feeds each prompt to Nano Banana for image generation
2. Multiple variants are generated per scene → stored in `04_visuals/raw/`
3. Human selects the best variant per scene → stored in `04_visuals/selected/` as `ep{XX}_s{XX}_selected.png`
4. Selected images become input for `_skills/robotiko-motion-script/SKILL.md`

**Every weak prompt produces a weak image. Every weak image produces a weak video. Precision here cascades forward through the entire pipeline.**

---

## SUPPLEMENTARY VISUAL PROMPTS (Motion Script Feedback Loop)

The motion script skill (`robotiko-motion-script`) may discover that some scenes require additional images to cover their full music duration. When this happens, the motion script includes **inline supplementary visual prompts** — complete, ready-to-use prompts embedded directly in the motion script document.

### How This Works

1. The motion script identifies scenes where a single video clip cannot cover the music duration.
2. These scenes are split into sub-clips (e.g., S29a, S29b, S29c, S29d).
3. Sub-clips that need a different composition than the existing selected image get an inline supplementary visual prompt.
4. The human generates the image from this prompt in Nano Banana, selects it, and saves it with the filename specified in the motion script.

### Quality Rules for Supplementary Prompts

Supplementary prompts generated by the motion script skill **must follow all rules of this visual prompts skill:**

- [x] Must end with the mandatory visual suffix — no exceptions
- [x] Must respect the episode's character phase (from `character_profiles.json`)
- [x] Must not include any forbidden aesthetics
- [x] Must be fully self-contained (no cross-references to other prompts)
- [x] Must include composition space (headroom + breathing space) for camera movement
- [x] Must embed character `visual_prompt_addition` when characters appear

The motion script skill generates these prompts, but they are subject to the same quality gates as primary visual prompts.

### Naming Convention

Supplementary images follow the sub-clip naming pattern:
- `ep{XX}_s{XX}{a|b|c|d}_selected.png`
- Example: `ep02_s29c_selected.png` (third sub-clip of scene 29)

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Dramaturgy not approved | STOP. Cannot generate visual prompts from unapproved scenes. |
| Dramaturgy file missing | STOP. Inform human. The pipeline requires dramaturgy before visual prompts. |
| Character ref image missing | Proceed but flag it. Note in the prompt block that ref image is unavailable. |
| Character design pending (e.g., Robochica) | Describe compositionally using `character_profiles.json` base description. Flag as "design pending" in each relevant prompt. |
| Dramaturgy scene has no visual description | Do not invent. Ask the human to update the dramaturgy or provide guidance. |
| Suffix accidentally omitted | This is a critical pipeline error. Re-check every prompt before delivery. |
| Scene count mismatch with dramaturgy | Investigate. The counts must match exactly. If a scene was split (Start/End), document the S{XX}a/S{XX}b convention. |

---

*"The prompt is the blueprint. The image is the brick. Build with precision or the wall will fall."*
*— Robotiko v2.0 Pipeline*
