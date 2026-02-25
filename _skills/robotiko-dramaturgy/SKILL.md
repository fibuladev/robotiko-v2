# SKILL: robotiko-dramaturgy
> **Version:** 1.0 | **Last Updated:** 2026-02-24
> **Trigger:** `"Create dramaturgy for EP{XX}"`
> **Output:** `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md`

---

## PURPOSE

Generate a scene-by-scene dramaturgy document that maps the visual narrative of an episode to its musical structure. The dramaturgy is the bridge between the music (temporal skeleton) and the visuals (spatial expression). Every scene must be anchored to a specific musical moment, serve the episode's philosophical station, and respect the character's current evolutionary phase.

---

## MANDATORY INPUTS (Read Before Writing a Single Scene)

Read these files in this exact order before generating any output:

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/master.md` | Episode arc, station, tone, key lyrics, key moments, character phases, philosophical context |
| 2 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Sections, timestamps, energy levels, mood, instruments, lyrics per section |
| 3 | `episode-{XX}/03_direction/ep{XX}_concept_notes.md` | Human must-have shots, creative overrides, specific visual requests |
| 4 | `_assets/cast/character_profiles.json` | Character visual state for this episode's phase (use `visual_prompt_addition`) |
| 5 | `_templates/dramaturgy_template.md` | Output structure and formatting template |

**If any of inputs 1-4 are missing:** STOP. Inform the human. Do not proceed with partial inputs.

---

## PRE-GENERATION ANALYSIS

Before writing any scenes, perform this internal analysis and output it as the **Episode Context Block** at the top of the dramaturgy document:

### Step 1: Identify the Station
- Which of the Seven Stations does this episode belong to?
- What is the core psychological state of Robotiko?
- What is the transformation arc within this episode (beginning state → ending state)?

### Step 2: Extract the Musical Skeleton
- List all sections from `musical_metadata.json` with timestamps, energy, and mood.
- Identify energy peaks, valleys, and transitions — these are your scene break candidates.
- Note any instrumental solos, breakdowns, or silence — these demand special visual treatment.

### Step 3: Map Character State
- From `character_profiles.json`, identify the exact phase (Awakening / Destruction / Reconstruction).
- Copy the `visual_prompt_addition` field — this will be embedded in every scene that features the character.
- Check Mentor status: Active / Disappearing / Gone.
- Check if Robochica appears in this episode.

### Step 4: Integrate Human Overrides
- Read `concept_notes.md` and flag all must-have shots.
- These shots take priority — build the surrounding scenes to support them.
- Mark overridden scenes with `User Override: YES` in the scene table.

---

## SCENE GENERATION RULES

### Rule 1: Music Drives the Scene Count
- The number of scenes is determined by the musical structure, NOT by an arbitrary target.
- Each musical section (intro, verse, chorus, bridge, solo, outro) generates at least one scene.
- Long sections (>15 seconds) or high-energy sections may generate 2-3 scenes.
- Short transitions (<5 seconds) may be combined with adjacent sections.
- Typical range: 20-35 scenes per episode (but never force a count).

### Rule 2: Energy = Visual Intensity
- Map musical energy levels directly to visual intensity:
  - `low` → Wide shots, slow atmosphere, environmental focus
  - `medium` → Character focus, mid-range compositions, narrative beats
  - `high` → Close-ups, rapid detail, dynamic compositions, visual climax
  - `building` → Progressive tightening of composition, increasing detail
  - `peak` → Maximum visual intensity, the defining image of the section

### Rule 3: Beat Sync Awareness
- Note the tempo (BPM) from the metadata JSON.
- For high-energy sections, scene changes should align with musical beats or downbeats.
- For atmospheric sections, scene changes can breathe across multiple bars.
- Always note the musical sync point in the "Music Sync" column.

### Rule 4: Character Continuity
- Robotiko's visual state MUST match the episode's phase. Never show pristine Robotiko in Phase 2/3.
- If the Mentor appears, reference his exact visual description from `character_profiles.json`.
- If Robochica appears, reference her profile. If her design is pending, flag it and describe compositionally.

### Rule 5: Composition for Motion
- Every scene description should imply a composition that allows camera movement.
- Include "headroom" (space above subject for tilt) and "breathing space" (lateral space for pan).
- Note depth layers (foreground / midground / background) when relevant.
- This enables the Motion Script phase to define camera moves without re-composing.

### Rule 6: No Cheap Emotion
- Visual descriptions must earn their emotional weight through specificity, not adjective stacking.
- Avoid: "incredibly sad and devastated Robotiko crying in beautiful despair"
- Prefer: "Robotiko kneeling, one hand pressed flat against cracked earth, blue eyes dim, sparks dripping from a severed wire at his wrist"

### Rule 7: The Forbidden List
- Never describe visuals as clean, sterile, smooth, or Pixar-like.
- Never use generic cyberpunk neon aesthetics.
- Always maintain the 70s Prog Rock album art DNA: analog, textured, painterly.

---

## OUTPUT FORMAT

Use the template from `_templates/dramaturgy_template.md`. The output document must contain these sections in this order:

### 1. Episode Header
Fill all fields from the template: Episode, Title, Station, Tone, Language, Character Phase, Robotiko Visual State, Total Scenes, Total Duration.

### 2. Musical Structure Summary
Auto-extracted from the musical metadata JSON. Table with: Section, Timestamp, Type, Energy, Key Instruments, Notes.

### 3. Scene Breakdown Table
The core deliverable. Table with columns:

| Column | Description |
|---|---|
| **Shot ID** | Sequential: S01, S02, S03... Always 2 digits. |
| **Timestamp** | Exact start time from musical metadata (MM:SS or M:SS) |
| **Visual Description** | Detailed scene description (3-5 sentences). Specific, compositional, cinematic. |
| **Mood / Lighting** | Color temperature, atmosphere, lighting direction |
| **Characters** | Which characters appear. Reference their current phase state. |
| **Music Sync** | What musical element this scene aligns with (e.g., "Fuzz guitar entry", "Hammond organ swell", "Drum fill into chorus") |
| **User Override?** | YES if from concept_notes.md, NO if Claude-generated |

### 4. Scene Detail Blocks
For complex scenes that will likely need Start/End keyframe video strategy, provide expanded detail blocks with:
- Timestamp and duration
- Musical moment description
- Full visual description
- Characters with current visual state
- Suggested video tech strategy (Standard / Start-End / Extension)
- Composition notes (headroom, depth, breathing space)
- User override flag

### 5. Director's Notes
Claude's analysis of creative decisions:
- How the scenes serve the episode's station
- Character arc progression expressed through visuals
- Connections to the overarching Master narrative
- Any scenes flagged for special human attention

### 6. Approval Status
Checkboxes: Human reviewed, Human approved, Ready for Visual Prompt generation.

---

## SCENE DESCRIPTION WRITING GUIDE

### DO:
- Write in present tense, active voice
- Be cinematically specific: angle, depth, light source, texture
- Reference the exact musical moment the scene lives in
- Include environmental context (where is Robotiko? what surrounds him?)
- Layer meaning: surface action + symbolic undercurrent
- Use the color palette from master.md (cold blues/silver for AI, golden/amber for warmth)

### DON'T:
- Stack adjectives without visual specificity
- Describe emotions abstractly ("he feels sad") — show it physically
- Use generic sci-fi descriptions ("futuristic city")
- Forget the analog/textured/70s aesthetic
- Write scenes that exist purely for spectacle without narrative purpose
- Reference camera movements — that is the Motion Script's job

### EXAMPLE (Good):
> Robotiko stands at the edge of a rust-colored cliff, his chrome body reflecting the dying amber light of a Kodachrome sunset. His left arm hangs loose, sparks dripping from a cracked joint. In the distance, the silhouette of an industrial wasteland stretches to the horizon — smokestacks like broken fingers against a bruised sky. His blue eyes are steady but dim. The Mentor's staff lies on the ground beside him, its amber tip still faintly glowing.

### EXAMPLE (Bad):
> Robotiko is standing in a beautiful futuristic landscape looking sad and broken. The sky is amazing with lots of colors. He misses the Mentor and feels alone.

---

## VERSIONING

- First output is always `v01`.
- If the human requests revisions, increment: `v02`, `v03`, etc.
- Each version is a complete document (not a diff).
- Version number is in the filename: `ep{XX}_dramaturgy_v{VV}.md`

---

## POST-GENERATION CHECKLIST

Before delivering the dramaturgy to the human, verify:

- [ ] Every scene has a timestamp anchored to the musical metadata JSON
- [ ] Character visual state matches the episode's phase (no continuity errors)
- [ ] All human must-have shots from concept_notes.md are included and marked
- [ ] No scene uses forbidden aesthetics (clean, sterile, neon cyberpunk, Pixar)
- [ ] Visual descriptions are specific and compositional, not abstract
- [ ] Energy mapping is consistent (low energy ≠ visual climax)
- [ ] Director's Notes explain how scenes serve the station
- [ ] Approval checkboxes are present at the bottom
- [ ] File is saved with correct naming: `ep{XX}_dramaturgy_v{VV}.md`
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## WHAT HAPPENS NEXT

After human approves the dramaturgy:
1. The dramaturgy becomes the input for `_skills/robotiko-visual-prompts/SKILL.md`
2. Each scene in the breakdown table will be converted to a standalone image generation prompt
3. The mandatory visual suffix will be appended to each prompt
4. Image generation begins (Nano Banana)

**The dramaturgy is the foundation. If it is weak, everything built on it will be weak.**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Musical metadata JSON is missing | STOP. Inform human. Cannot proceed without temporal skeleton. |
| Concept notes file is missing | Inform human. Proceed with master.md as sole creative guide, but flag that no human overrides were applied. |
| Character phase unclear | Cross-reference master.md Section 4 (Character Profiles) and character_profiles.json. If still unclear, ask the human. |
| Episode not yet in master.md | STOP. This episode has not been defined yet. Cannot generate dramaturgy for undefined content. |
| Scene count feels too high/low | Trust the music. If the metadata has 15 sections, you will have approximately 20-30 scenes. Do not force a count. |
| Human override contradicts the station's tone | Flag it in Director's Notes but include it. The human has final creative authority. |

---

*"The dramaturgy is where the music becomes a story, and the story becomes an image."*
*— Robotiko v2.0 Pipeline*
