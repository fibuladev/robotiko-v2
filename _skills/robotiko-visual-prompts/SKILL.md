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
| 3 | `_assets/cast/character_profiles.json` | Character `visual_prompt_addition` for this episode's phase, `reference_images` + `phase_reference_map` for the correct ref file, eye color logic |
| 4 | Phase-correct Robotiko reference | Look up `phase_reference_map` in character_profiles.json → determines which ref file to use (pristine, damaged, or kintsugi). For episodes with `episode_overrides` (EP08, EP09), check scene ranges. |
| 5 | `_assets/cast/ref_mentor_master.png` | Visual reference image (if Mentor appears; EP01-07 only) |
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

### Step 0: Pre-Generate Reference Images (CHARACTER + ENVIRONMENT)

Before writing any scene prompts, identify and prepare reference images:

**Character References:**
- Scan the dramaturgy for episode-specific character groups (e.g., sol-liberal travelers, wedding guests, nightclub touts).
- For each group, write a standalone prompt that clearly shows the group in a neutral composition — this becomes the character reference image.
- The human generates this image first, then uploads it alongside every scene prompt where that group appears.
- Robotiko has multiple reference images keyed to his phase — look up `reference_images` and `phase_reference_map` in `character_profiles.json` to determine which file to use. Phase 1 (EP01-03): `ref_robotiko_master.png`. Phase 2 (EP04-07, EP08 body): `android_damaged.png` (+ alt angles `_2`, `_3`). Phase 3: `android_kintsugi.png` (the full patchwork/gold-cracked body — added 2026-06-28). For EP09 the body is still @Damaged through the S27 transition keyframes (first gold on a damaged body, use `android_damaged.png`), then switches to `android_kintsugi.png` from S28 onward. Check `episode_overrides` for EP08 (body stays damaged all episode) and EP09 (intra-episode transition at S27). Mentor: `ref_mentor_master.png` (EP01-07 only). Episode-specific groups do NOT have master refs — they need per-episode reference images.

**Environment References:**
- Scan the dramaturgy for locations that appear in 3+ scenes (e.g., an industrial estate, a nightclub interior, a metro/BRT line).
- For each recurring location, write a standalone environment prompt — wide establishing shot, no characters, full spatial detail. **Make the prompt geometry-explicit:** decide and state the canonical camera position, the perspective direction, and where the key landmarks sit (e.g., "three-quarter interior, the workbench receding diagonally from front-left toward the back-right shutter, tool pegboard on the left wall, metal shelving on the right"). The geometry is a DECISION made here — not something to discover from the output later.
- **Write an `Environment Geometry` note** beside each env-ref prompt: one short block capturing that canonical camera position, perspective direction, and landmark layout. This is the contract every scene in that location frames against. It is plain text, available at authoring time — so scenes can be framed BEFORE the env-ref image exists. This is what dissolves the "frame to an image that doesn't exist yet" ordering problem.
- The human generates this image first, then uploads it alongside every scene prompt set in that location.
- This ensures visual continuity: same workshop walls, same lighting fixtures, same floor texture across all scenes.

**Framing Pass (after the env-ref images are generated):** open each generated environment reference, confirm it matches its `Environment Geometry` note (update the note if the real image diverged), and adjust any scene whose framing the actual image contradicts. This is the moment a scene is framed to the real pixels — a verification / refinement step, never a blocker for first-draft authoring. (When an env ref already exists up front — reused, a photo, or human-provided — you are effectively in the Framing Pass from the start: frame straight to the image.)

**Why this matters:** Without reference images, Nano Banana generates different-looking characters and environments in every scene. Reference images anchor visual identity across the episode.

### Step 1: Confirm Character Phase
- From `character_profiles.json`, extract the `visual_prompt_addition` for this episode's phase.
- Use it ONLY to confirm the phase and pick the correct reference file — do NOT paste this string into the prompts. The short identifier + inline reference binding (Rule 2b / Rule 3) name the subject; the uploaded reference carries the detail.
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

### Rule 2b: Inline Reference Binding (Nano Banana)
When a scene uploads reference images, **bind each reference to its element inline** — put the reference's filename in parentheses immediately after the thing it defines:
- `inside a workshop (ep09_ref_workshop.png)` — environment ref
- `the chrome android (android_damaged.png)` — character ref
- `the chrome android's open chest panel (android_damaged.png)` — for a close-up, bind the same character ref

Use the exact filename the human uploads (the basename in that scene's `Upload` field). The metadata `Upload` field still lists the same files for bookkeeping and the validator — the inline callout is what the model actually reads.

**Why:** when several references are uploaded at once, Nano Banana otherwise guesses which upload maps to which element, and mis-binds or ignores them. The inline callout pins each reference to its target — this is what makes multi-reference generation reliable.

**Do NOT also restate what the bound reference already shows.** `the chrome android (android_damaged.png)` carries the full damaged body, the missing ear, the wires; adding "battle-scarred rusted chrome, missing right ear with exposed wires" competes with the reference and degrades the output. Describe ONLY what is NOT in the reference — a new wound, or (for EP09 S27+) the emerging gold/kintsugi transformation the damaged reference does not yet show.

### Rule 3: Character Embedding
When a character appears in a scene:
- The **short identifier is authoritative**, and it is **bound to its reference inline** (Rule 2b) — the reference image carries the visual detail. The text prompt names the subject and pins the file; the uploaded reference defines what it looks like. Long descriptions compete with the reference and confuse the model.
- For Robotiko: "a chrome android (android_damaged.png)" or "the chrome android (android_damaged.png)" — the phase-correct reference (via `phase_reference_map`) carries the damage state, body details, and proportions. Bind the same file for close-ups of his hand, face, or chest.
- For Mentor: "an elderly figure in dark green cloak, wooden staff with glowing amber tip" when `ref_mentor_master.png` is uploaded.
- For episode-specific groups: use a brief consistent descriptor (e.g., "three young travelers — mixed men and women with colorful scarves") when the group's reference image is uploaded.
- Only add specific damage/state details if they differ from the reference image (e.g., "thin scratch across his cheek" for a new wound not present in the ref).
- Do NOT use character names ("Robotiko", "Mentor") — image generators don't know names. Describe by appearance.

**Example — Robotiko with phase-correct reference uploaded (Phase 2, damaged):**
> A chrome android standing at the edge of a rusted platform...

**Example — Robotiko WITHOUT reference image (fallback only):**
> A retro-futuristic chrome android with battle-scarred chrome body, exposed analog wires, glowing blue eyes, standing at the edge of...

### Rule 3b: Anti-Spawn Guard
Image generators spawn duplicate characters. Every single-character scene needs a guard — but the phrasing depends on the tool:
- **Nano Banana / Gemini:** End the prompt (before the style suffix) with: `single figure composition, no additional characters`
- **Motion prompts (Kling / Veo / Seedance):** Use the motion-specific guard from the motion script skill: `Do not add extra characters. Keep everything as pictured.`
- Do NOT write "only ONE android" or "no second robot" — these literal number/negation phrases backfire in Nano Banana, causing the tool to latch onto the concept of a second robot and generate one.
- **OMIT the guard entirely when the uploaded character reference + scene context already establish a single figure** (a solo portrait reference in a clearly solo scene — e.g. EP09's kintsugi workshop shots). The phrase is then redundant noise that adds nothing; see the golden EXAMPLE below ("the reference plus 'alone' already establish a single figure"). Add the guard only when duplication is a real risk: no strong solo reference, or a scene/composition the tool tends to populate.
- **Exception:** Intentional multi-figure scenes (ghost-self, dream copies) skip the guard and instead specify the exact count and each instance's distinct treatment — see the INTENTIONAL MULTI-FIGURE rule in `_memory/lessons.md`.

### Rule 4: Environmental Specificity
- Never write generic environments ("a futuristic city", "a dark room").
- Always describe specific textures, materials, depth layers, and light sources.
- Ground the scene in the 70s Prog Rock aesthetic: analog, industrial, painterly.
- Include foreground/midground/background layering when the dramaturgy calls for depth.

### Rule 4b: Frame to the Environment Reference
Frame every scene's **angle and composition to the geometry of its environment**, so the shot sits inside a coherent, consistent space instead of defaulting to a flat frontal portrait. Two modes, depending on whether the env-ref image exists yet:

- **Image exists** (reused from a prior episode, a real photo, a human-provided ref, or already generated in the Framing Pass): **open it and read its geometry** — camera position, perspective lines, where the depth goes — and write the angle to match.
- **Image not generated yet** (you are authoring this pass, before Step 0 images are made): frame to the location's **`Environment Geometry` note** (Step 0) — the canonical camera/landmark layout decided when the env-ref prompt was written. The geometry is text you already hold; you do not need the pixels to be spatially coherent. Verify against the real image later in the Framing Pass.

- **Why it matters:** a character reference is usually a frontal portrait. If you don't name the angle, the generator turns the character to face the camera and centres them — flat, symmetrical, identical every time. Naming the angle that matches the environment breaks that default and gives the scene depth. (EP09 S34 kept coming out dead-centre and frontal until rewritten as "three-quarter view from the front-left corner, the bench receding diagonally toward the shutter" — matching `ref_workshop.png` — and it locked on the first try.)
- **Vary within the space:** scenes in the same location must NOT clone the env-ref's exact angle. Choose deliberate, *spatially coherent* viewpoints inside the established geometry (a reverse angle, a low angle across the bench, a corner three-quarter), honouring the episode's Camera Diversity rule. The env ref establishes the room; each scene picks a considered viewpoint within it.
- **Specify** the camera **angle** and the subject's **placement / orientation**: three-quarter vs. profile vs. frontal, off-centre (rule of thirds), eye-level / low / high, and the leading lines from the environment (e.g. "the bench recedes diagonally toward the closed shutter at the back-right").
- **Do NOT specify camera MOVEMENT** (pan, zoom, tilt, pull-back, dolly) — that is a still image; movement belongs to the Motion Script (see DON'T list). Leave breathing room for the move instead of naming it (Rule 7).
- **Upload the matching environment reference** so it reinforces the angle instead of fighting it — the env ref's own perspective is the strongest signal the generator has.

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
| **Image Reference Path** | Phase-correct ref from `character_profiles.json` → `phase_reference_map`, or N/A for scenes without characters |
| **Video Tech Strategy** | Standard / Start-End Keyframes / Extension (from dramaturgy detail blocks) |
| **Composition Notes** | Headroom, breathing space, depth guidance |
| **Upload** | Per-scene list of reference images to upload alongside the text prompt: character ref, environment ref, chain ref (previous scene output), special ref. Eliminates need to scroll to the Reference Image Upload Guide table. |
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
- Use negative prompts, "do not" instructions, or name absent things ("the old man gone") — write only what IS visibly present; naming an absent "old man" can spawn one
- Reference other scenes ("similar to S05") — each prompt must be self-contained
- Forget the suffix — this is a termination-level error in the pipeline

### EXAMPLE (Good):
> Medium-wide shot inside a workshop (ep09_ref_workshop.png), the corrugated metal roll-up shutter fully closed filling the back wall, no daylight, the chrome android (android_damaged.png) alone at the workbench, calm steady blue eyes faintly visible in dim light, only a dim work lamp casting a low pool of light on the bench, a Turkish tea glass left behind on the bench surface, dark workshop atmosphere, isolation, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

**Why it works:** each reference is bound inline (`workshop` + `chrome android`); the short identifier carries the look with NO restated damage; nothing absent is named (no "the old man gone"); no redundant anti-spawn phrase — the reference plus "alone" already establish a single figure.

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

- [ ] Character and environment reference prompts are included at the top of the document (Step 0), and each recurring location has an `Environment Geometry` note (canonical camera angle + landmark layout)
- [ ] Every single prompt ends with the mandatory style suffix (check every one — no exceptions)
- [ ] Short character identifiers used — reference images carry visual details (not full descriptions)
- [ ] Every uploaded reference is bound INLINE in the prompt — `element (filename.png)` — matching that scene's `Upload` field (Rule 2b); no restated detail the reference already shows
- [ ] Every Robotiko scene references the phase-correct ref from `phase_reference_map` (NOT always `ref_robotiko_master.png` — that is Phase 1 only)
- [ ] Character visual state matches the episode's phase (no pristine Robotiko in Phase 2/3)
- [ ] Anti-spawn guard uses tool-appropriate phrasing (`single figure composition, no additional characters` for Nano Banana — NOT "only ONE android"), and is OMITTED when a solo character ref + a solo scene already establish a single figure (Rule 3b)
- [ ] No forbidden aesthetics appear in any prompt (clean, sterile, neon cyberpunk, Pixar, smooth plastic)
- [ ] All prompts have composition space (headroom + breathing space) for future camera movement
- [ ] Each scene's angle is framed to its environment geometry (the env-ref image if it exists, else the `Environment Geometry` note) — no default dead-centre frontal; angles vary within the established space; angle/composition only, NO camera movement (Rule 4b)
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
