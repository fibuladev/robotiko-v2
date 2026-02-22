# PRODUCTION PIPELINE & QUALITY ASSURANCE
> **Version:** 2.0 | **Last Updated:** 2026-02-23
> Always refer to `_management/master.md` as the absolute source of truth.

---

## THE GOLDEN RULE: CHAIN OF THOUGHT
Output of Step N = Input of Step N+1.
**Never skip a step. Never guess. Always refer to the Master.**

---

## MANDATORY CHECKPOINTS (Human Approval Required)
Two steps require explicit human approval before proceeding. Everything else Claude executes and delivers:

1. **After Dramaturgy** → Human reviews and approves scene breakdown before visuals begin.
2. **After Motion Script** → Human reviews camera moves and tech strategy before video generation.

---

## PHASE 0: PREPARATION

### Step 0: Episode Scaffolding
- **Trigger:** `python scripts/create_episode.py {episode_number}`
- **Or via:** GitHub Actions → `create_episode.yml` workflow
- **Output:** Full folder structure created under `episode-{XX}/`
- **Skill:** `_skills/robotiko-episode-scaffold/SKILL.md`

---

## PHASE 1: NARRATIVE & AUDIO

### Step 1: Lyrics & Music
- **Input:** `_management/master.md` (episode theme, station, tone)
- **Tool:** Human writes lyrics → Suno AI generates audio
- **Output:**
  - `episode-{XX}/01_lyrics/ep{XX}_lyrics_v01.md`
  - `episode-{XX}/02_music/ep{XX}_audio_v01.wav` (stored in S3/Git LFS)

### Step 2: Musical Metadata JSON
- **Input:** Audio file + Lyrics
- **Tool:** Human listens to audio → Gemini Tool generates structured JSON
- **Output:** `episode-{XX}/02_music/ep{XX}_musical_metadata.json`
- **Format:** All-in-one JSON containing:
  - `tempo`, `key`, `time_signature`, `mood[]`, `instruments[]`
  - `sections[]` with `type`, `start`, `end`, `energy`, `lyrics`, `notes`
- **Note:** This JSON is the temporal skeleton of the entire episode. Every scene, visual, and camera move will be anchored to it. Do not proceed without it.

---

## PHASE 2: DIRECTION

### Step 3: Concept Notes (Human Must-Haves)
- **Input:** Human's creative vision, override requests, must-have shots
- **Output:** `episode-{XX}/03_direction/ep{XX}_concept_notes.md`
- **Note:** If no overrides exist, this file can be minimal. But it must exist.

### Step 4: Dramaturgy Generation
- **Input:**
  - `_management/master.md` (episode arc, station, tone, character state)
  - `episode-{XX}/02_music/ep{XX}_musical_metadata.json`
  - `episode-{XX}/03_direction/ep{XX}_concept_notes.md`
  - `_assets/cast/character_profiles.json` (character visual state for this episode)
- **Tool:** Claude executes `_skills/robotiko-dramaturgy/SKILL.md`
- **Output:** `episode-{XX}/03_direction/ep{XX}_dramaturgy.md`
- **Format:** Scene-by-scene table with: Shot ID, Timestamp, Visual Description, Mood/Lighting, Characters, User Override flag
- **⛔ MANDATORY CHECKPOINT:** Human reviews and approves before Phase 3 begins.

---

## PHASE 3: VISUAL PRODUCTION

### Step 5: Visual Prompt Generation
- **Input:**
  - Approved `ep{XX}_dramaturgy.md`
  - `_assets/cast/character_profiles.json` (mandatory — character state tracking)
  - `_management/master.md` (visual suffix, color palette)
- **Tool:** Claude executes `_skills/robotiko-visual-prompts/SKILL.md`
- **Output:** `episode-{XX}/04_visuals/ep{XX}_visual_prompts.md`
- **Rules:**
  - Every prompt MUST reference character master image path if a character appears
  - Every prompt MUST end with the mandatory visual suffix (no exceptions)
  - Compose with "Headroom" and "Breath" for camera movement space
  - Skill:** `_skills/robotiko-visual-prompts/SKILL.md`

### Step 6: Image Generation
- **Tool:** Nano Banana Pro (using prompts from Step 5)
- **Output:** `episode-{XX}/04_visuals/raw/ep{XX}_s{XX}_v{XX}.png`

### Step 7: Image Selection
- **Tool:** Human curates best outputs
- **Output:** `episode-{XX}/04_visuals/selected/ep{XX}_s{XX}_selected.png`

---

## PHASE 4: MOTION PRODUCTION

### Step 8: Motion Script Generation
- **Input:**
  - Selected images from `04_visuals/selected/`
  - Approved `ep{XX}_dramaturgy.md`
  - `ep{XX}_musical_metadata.json` (for beat sync)
- **Tool:** Claude executes `_skills/robotiko-motion-script/SKILL.md`
- **Output:** `episode-{XX}/05_video/ep{XX}_motion_script_v01.md`
- **⛔ MANDATORY CHECKPOINT:** Human reviews camera moves and tech strategy before video generation.

### Step 9: Video Generation
- **Tool:** Seedream, Kling or Veo
- **Strategy Options:**
  - **Mode A — Standard (5s):** Atmospheric/simple movement. Input: 1 image.
  - **Mode B — Start/End Keyframes (5s or 10s):** Transformations, morphing, complex travel. Input: 2 images.
  - **Mode C — Extension:** Continuous long takes, pans.
- **Output:** `episode-{XX}/05_video/raw/ep{XX}_s{XX}_video_{tool}.mp4`

### Step 10: Video Selection
- **Tool:** Human curates final clips
- **Output:** `episode-{XX}/05_video/selected/ep{XX}_s{XX}_selected.mp4`

---

## PHASE 5: POST-PRODUCTION

### Step 11: Editing
- **Tool:** CapCut
- **Input:** Selected video clips + Final audio
- **Output:** `episode-{XX}/06_edit/ep{XX}_final_v01.mp4`
- **QA Checklist:**
  - [ ] Beat sync verified
  - [ ] Color consistency (Kodachrome warmth, film grain)
  - [ ] 4K export confirmed
  - [ ] No clean/sterile aesthetics — analog decay preserved

---

## PHASE 6: DISTRIBUTION (Post-Completion)

### Step 12: YouTube Packaging
- **Tool:** Claude executes `_skills/robotiko-youtube-packager/SKILL.md`
- **Output:** Title, description, timestamps, tags

### Step 13: Social Media Atomization
- **Tool:** Claude executes `_skills/robotiko-reels-atomizer/SKILL.md`
- **Output:** Platform-specific clips under `episode-{XX}/07_social_media/`

---

## SKILLS SYSTEM

All Claude workflows are defined in `_skills/`. Each skill is a `SKILL.md` file.
Claude reads the relevant SKILL.md before executing any workflow.

| Skill | Trigger Phrase | Output |
|---|---|---|
| `robotiko-dramaturgy` | "Create dramaturgy for EP{XX}" | `ep{XX}_dramaturgy.md` |
| `robotiko-visual-prompts` | "Generate visual prompts for EP{XX}" | `ep{XX}_visual_prompts.md` |
| `robotiko-motion-script` | "Generate motion script for EP{XX}" | `ep{XX}_motion_script.md` |
| `robotiko-episode-scaffold` | "Scaffold EP{XX}" | Full folder structure |
| `robotiko-naming-enforcer` | "Validate file names" | Compliance report |
| `robotiko-youtube-packager` | "Package EP{XX} for YouTube" | Metadata file |
| `robotiko-reels-atomizer` | "Atomize EP{XX} for social" | Clip list |
| `robotiko-launch-orchestrator` | "Orchestrate EP{XX} launch" | Launch checklist |

---

## PIPELINE SUMMARY (Quick Reference)

```
SCAFFOLD → LYRICS → MUSIC → METADATA JSON → CONCEPT NOTES
    → DRAMATURGY [✋ CHECKPOINT] → VISUAL PROMPTS → IMAGE GEN → IMAGE SELECT
    → MOTION SCRIPT [✋ CHECKPOINT] → VIDEO GEN → VIDEO SELECT
    → EDIT → YOUTUBE + SOCIAL
```