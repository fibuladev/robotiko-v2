# PRODUCTION PIPELINE & QUALITY ASSURANCE

## THE GOLDEN RULE: CHAIN OF THOUGHT
Output of Step N = Input of Step N+1.
*Never skip a step. Never guess. Always refer to the Bible.*

## PHASE 1: NARRATIVE & AUDIO
### Step 1: Lyrics & Music
* **Input:** Bible Theme.
* **Output:** Audio File + Lyrics Text.

### Step 2: Dramaturgy (The Hybrid Director)
* **Input:** Lyrics + `concept_notes.md` (User Must-Haves).
* **Process:** LLM generates Scene Breakdown.
* **CRITICAL USER STEP:** User reviews and edits the script before visuals begin.

## PHASE 2: VISUAL PRODUCTION
### Step 3: Visual Prompting (Nano Banana)
* **Input:** Approved Dramaturgy + **Master Reference Images**.
* **Rule 1 (Consistency):** You MUST assign a Master Image Path (`_assets/cast/...`) if a character appears.
* **Rule 2 (Video-Ready):** Compose shots with "Headroom" and "Breath" to allow for camera movement later. Avoid tight crops that lock motion.

## PHASE 3: MOTION PRODUCTION
### Step 4: Motion Scripting (The Video Blueprint)
* **Input:** Selected Generated Images + Dramaturgy.
* **Action:** LLM generates `motion_script.md`.
* **CRITICAL USER STEP:** User reviews the "Camera Moves" and "Tech Strategy" (Start/End vs Standard).
* **Only approved motion prompts go to Kling/Veo.**

### Step 5: Video Generation Strategy
* **Mode A (Standard - 5s):** For atmospheric/simple shots. (Input: 1 Image)
* **Mode B (Start/End Keyframes - 5s/10s):** For transformation, morphing, or complex travel. (Input: 2 Images).
* **Mode C (Extension):** For continuous pans.

## PHASE 4: POST-PRODUCTION
### Step 6: Editing (CapCut)
* **Input:** Generated Video Clips + Final Music.
* **QA Checklist:** Sync to beat, Color Consistency (Grain/Warmth), 4K Export.