# SKILL: robotiko-motion-script
> **Version:** 1.0 | **Last Updated:** 2026-02-24
> **Trigger:** `"Generate motion script for EP{XX}"`
> **Output:** `episode-{XX}/05_video/ep{XX}_motion_script_v{VV}.md`

---

## PURPOSE

Generate a shot-by-shot motion script that defines camera movements, video generation strategy, motion intensity, and beat sync instructions for each scene of an episode. The motion script translates still images (selected visuals) into cinematic motion by telling the video generation tool (Seedream / Kling / Veo) exactly how each frame should come alive.

This is the final creative document before video generation begins. Precision here determines whether the final video breathes with the music or fights against it.

---

## PREREQUISITE

> **Two conditions must be met before this skill executes:**
> 1. The dramaturgy for this episode must be **human-approved**.
> 2. Selected images must exist in `episode-{XX}/04_visuals/selected/`.
>
> If either condition is not met, STOP. Inform the human.

---

## MANDATORY INPUTS (Read Before Writing a Single Shot)

Read these files in this exact order:

| # | File | What to Extract |
|---|---|---|
| 1 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Approved scene breakdown, scene descriptions, mood/lighting, characters, music sync column |
| 2 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Tempo (BPM), sections with timestamps, energy levels, instruments, mood per section |
| 3 | `episode-{XX}/04_visuals/selected/` | Verify which selected images exist (file listing) |
| 4 | `_management/master.md` | Episode tone, station, character phase, narrative arc |

**If the musical metadata JSON is missing:** STOP. Beat sync is impossible without temporal data.
**If selected images are missing:** STOP. The motion script references specific image files as input assets.

---

## PRE-GENERATION ANALYSIS

### Step 1: Extract the Temporal Grid
- From `musical_metadata.json`, build the complete section map:
  - Section type (intro, verse, chorus, bridge, solo, outro)
  - Start and end timestamps
  - Energy level per section
  - BPM (constant or variable)
- This grid is the backbone of all timing decisions.

### Step 2: Map Energy to Motion
- Energy levels from the musical metadata directly inform motion intensity:
  - `low` energy → Motion strength 1-3 (subtle breathing, slow drift)
  - `medium` energy → Motion strength 4-5 (steady cinematic movement)
  - `high` energy → Motion strength 6-8 (dynamic, purposeful movement)
  - `peak` energy → Motion strength 8-10 (maximum intensity, controlled chaos)
  - `building` energy → Motion strength ramps progressively within the section

### Step 3: Identify Beat Sync Critical Points
- Scan the musical metadata for:
  - Chorus entries (high impact — visual cuts or reveals should land here)
  - Drum fills and drops (natural cut points)
  - Instrumental solos (extended single-shot opportunities)
  - Silence or breakdowns (freeze or minimal motion)
  - Energy transitions (ramp up/down in motion strength)
- These become entries in the Beat Sync Notes table.

### Step 4: Match Selected Images to Scenes
- List all files in `04_visuals/selected/`.
- Map each `ep{XX}_s{XX}_selected.png` to its corresponding scene in the dramaturgy.
- If a scene has no selected image, flag it — the shot cannot be generated without an asset.
- If a scene was flagged for Start/End keyframes in the dramaturgy, confirm that both `s{XX}a` and `s{XX}b` selected images exist (or that two separate scene images are available for the transformation).

### Step 5: Determine Tech Strategy Per Shot
Assign one of three video generation modes to each shot:

| Mode | When to Use | Input | Duration | Motion Strength Range |
|---|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, single subject, no transformation | 1 selected image | 5s | 1-6 |
| **B — Start/End Keyframes** | Transformations, morphing, character state changes, location transitions, complex travel | 2 selected images | 5s or 10s | 3-8 |
| **C — Extension** | Continuous long takes, sustained atmosphere, slow reveals, scenes that need to breathe longer | 1 image + previous clip output | Variable | 1-5 |

Decision logic:
- Does the scene involve transformation or travel? → **Mode B**
- Does the scene need to sustain beyond 5 seconds for musical reasons? → **Mode C**
- Is it a single atmospheric moment or character portrait? → **Mode A**

---

## CAMERA MOVE VOCABULARY

Use only these approved camera moves. Do not invent custom terms.

| Camera Move | Description | Best For |
|---|---|---|
| **Static** | No camera movement. The frame breathes but does not travel. | Portraits, tension, still moments |
| **Slow Zoom In** | Gradual push toward subject. Builds intimacy or tension. | Emotional beats, revelations, close-ups |
| **Slow Zoom Out** | Gradual pull away from subject. Reveals context or isolation. | Establishing scale, loneliness, aftermath |
| **Pan Left** | Horizontal sweep left. Reveals environment or follows movement. | Location scanning, following action |
| **Pan Right** | Horizontal sweep right. Same as Pan Left but opposite direction. | Location scanning, following action |
| **Tilt Up** | Vertical sweep upward. Reveals height, scale, or ascension. | Buildings, mountains, cosmic reveals |
| **Tilt Down** | Vertical sweep downward. Reveals depth or descent. | Chasms, fallen subjects, grounding |
| **Crane Up** | Rising movement combining tilt and zoom out. Cinematic departure. | End of sections, epic reveals, departures |
| **Crane Down** | Descending movement combining tilt and zoom in. Cinematic arrival. | Introductions, landings, discoveries |
| **Handheld** | Subtle organic shake. Adds documentary urgency or instability. | Crisis, chaos, raw moments, EP02 satire |
| **Dolly In** | Steady forward push on a horizontal plane. More grounded than zoom. | Walking toward, approaching, confrontation |
| **Dolly Out** | Steady backward pull on a horizontal plane. | Retreat, separation, aftermath |
| **Orbital** | Slow circular movement around the subject. | Ritualistic moments, 360 reveals, EP08-09 |

### Camera Move Rules:
- **One camera move per shot.** Never combine "Pan Left + Zoom In" in a single shot — that creates conflicting instructions for the video model.
- **Motion direction should follow musical energy.** Zoom in during builds, zoom out during releases.
- **Static is not lazy.** A well-composed static shot with subtle atmospheric breathing (fog, sparks, light flicker) is often more powerful than an unmotivated camera move.
- **Match the station's emotional weight.** EP01-02 (Awakening) can be more dynamic. EP07-08 (Dark Night / Silence) should be restrained. EP09-10 (Integration) can be contemplative.

---

## MOTION STRENGTH SCALE

A 1-10 scale defining how much movement exists in the frame:

| Level | Description | Example |
|---|---|---|
| 1 | Almost still. Barely perceptible breathing. | Fog drifting, single light flicker |
| 2 | Gentle atmospheric motion. | Dust motes floating, fabric swaying |
| 3 | Subtle character or environmental movement. | Robotiko's wires shifting, ember glow pulsing |
| 4 | Clear but restrained motion. Standard cinematic feel. | Slow walk, steady head turn |
| 5 | Full cinematic motion. The frame is alive. | Deliberate camera move with environmental motion |
| 6 | Energetic. Purpose-driven movement. | Fast walk, sparks flying, wind gusts |
| 7 | High intensity. Multiple elements in motion. | Running, explosions beginning, storm approaching |
| 8 | Very high. Controlled chaos. | Battle damage, systems failing, crowd panic |
| 9 | Near maximum. Rapid, overwhelming. | Full system meltdown, visual overload |
| 10 | Maximum chaos. Disintegration. Use sparingly. | EP06-07 crisis peaks only |

### Motion Strength Rules:
- Never use 9-10 for more than 1-2 shots per episode. These are the visual equivalent of a scream — overuse kills impact.
- The average motion strength for an episode should align with the station's energy:
  - EP01-03 (Awakening): avg 4-5
  - EP04-07 (Destruction): avg 5-7, peaks at 8-9
  - EP08-10 (Reconstruction): avg 2-4, with occasional 5-6

---

## MOTION PROMPT WRITING GUIDE

The Motion Prompt field is a director's note describing what should feel alive in the frame. It is NOT a repeat of the visual prompt — the image already exists. This describes the **movement layer** added on top.

### DO:
- Describe what moves, how fast, and in what direction
- Reference the musical moment ("as the fuzz guitar enters, sparks begin cascading")
- Specify atmospheric motion: fog, dust, light flickers, wire sway, ember drift
- Note the emotional intent of the movement ("the zoom tightens like a closing fist")
- Keep it concise — 2-4 sentences maximum
- Describe the feeling of time within the shot (slow, suspended, urgent, relentless)

### DON'T:
- Repeat the visual description from the dramaturgy or visual prompt
- Describe what the image looks like — describe what MOVES
- Write prose paragraphs — this is a technical instruction
- Request impossible physics (an AI video model cannot rotate a subject 360 degrees from a single still image)
- Ignore the musical moment — every motion prompt must acknowledge what the music is doing

### EXAMPLE (Good):
> Slow zoom in toward Robotiko's face as the Hammond organ swell builds. His blue eyes flicker imperceptibly — not a full glitch, just a tremor. Wisps of volumetric fog drift left to right across the lower third of the frame. The amber light from the Mentor's staff pulses once, slowly, like a heartbeat.

### EXAMPLE (Bad):
> Camera moves in. Robotiko is standing there looking broken. Make it look cinematic and epic. The atmosphere should feel emotional.

---

## OUTPUT FORMAT

Use the template from `_templates/video_prompt_template.md`. The output document contains:

### 1. Episode Header
| Field | Value |
|---|---|
| Episode | EP{XX} |
| Title | [from dramaturgy] |
| Station | [from dramaturgy] |
| Dominant Energy | [overall energy character of this episode] |
| Total Shots | [must match scene count] |
| Total Duration | [MM:SS from musical metadata] |

### 2. Video Strategy Reference
Quick reference table for Mode A / B / C with usage criteria.

### 3. Motion Script (Shot by Shot)
Each shot block contains:

| Field | Description |
|---|---|
| **Shot ID** | S{XX} — matches dramaturgy and visual prompt scene ID |
| **Shot Title** | Brief descriptive title |
| **Timestamp** | From musical metadata |
| **Musical Moment** | What is happening in the music at this exact moment |
| **Scene Context** | 1-sentence reference to the approved dramaturgy |
| **Tech Strategy** | Mode A / Mode B / Mode C |
| **Duration** | 5s / 10s / Variable |
| **Motion Strength** | 1-10 |
| **Assets Required** | Start Frame path (and End Frame path if Mode B) |
| **Camera Move** | One move from the approved vocabulary |
| **Motion Prompt** | Director's note on movement, atmosphere, and musical sync |

### 4. Beat Sync Notes
Critical musical moments requiring precise visual synchronization:

| Timestamp | Musical Event | Required Visual Action |
|---|---|---|
| MM:SS | [specific musical event] | [specific visual response] |

### 5. Approval Status
Checkboxes: Human reviewed camera moves, Human reviewed tech strategy, Human approved, Ready for video generation.

---

## SHOT SEQUENCING PRINCIPLES

### Rhythm and Flow
- Alternate between movement and stillness. Three dynamic shots in a row exhausts the viewer.
- After a high-intensity sequence (motion 7-9), follow with a breath (motion 1-3).
- Match the musical phrasing: verse = steady rhythm, chorus = peak energy, bridge = transition.

### Visual Grammar
- **Zoom In** followed by **Zoom Out** creates a pulse. Use sparingly and intentionally.
- **Pan sequences** (Left, Left, Right) create a scanning rhythm. Use for location tours (EP02).
- **Static → Zoom In** is a revelation pattern. The stillness makes the movement meaningful.
- **Crane Up** at section endings = departure/transcendence.
- **Crane Down** at section openings = arrival/grounding.

### Continuity
- If two consecutive shots share the same location, consider Mode C (Extension) for seamless flow.
- If two consecutive shots are radically different environments, a hard cut (Mode A → Mode A) is correct.
- Camera direction should not jump randomly: don't Pan Left in S05 then Pan Left in S06 — the viewer needs directional logic.

---

## VERSIONING

- First output is always `v01`.
- If the human requests revisions, increment: `v02`, `v03`, etc.
- Each version is a complete document, not a diff.
- Version number in the filename: `ep{XX}_motion_script_v{VV}.md`

---

## POST-GENERATION CHECKLIST

Before delivering the motion script to the human, verify:

- [ ] Every shot references an existing selected image file path
- [ ] Every shot has exactly one camera move from the approved vocabulary
- [ ] Motion strength values align with the musical energy arc (no motion 9 during a quiet bridge)
- [ ] Tech strategy (A/B/C) is appropriate for each shot's requirements
- [ ] Beat Sync Notes table includes all critical musical moments (chorus entries, drops, solos, silence)
- [ ] No shot combines multiple camera moves (one move per shot — strict)
- [ ] Motion prompts describe movement, not visual appearance
- [ ] Motion prompts reference the musical moment they live in
- [ ] Shot sequence follows rhythm principles (no three consecutive high-intensity shots without a breath)
- [ ] Average motion strength matches the episode's station energy
- [ ] Approval checkboxes are present at the bottom
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## WHAT HAPPENS NEXT

After human approves the motion script:
1. Human feeds each shot to the video generation tool (Seedream / Kling / Veo) with:
   - The selected image(s) as input
   - The camera move instruction
   - The motion prompt as descriptive guidance
   - The motion strength as intensity parameter
2. Generated clips are stored in `05_video/raw/`
3. Human selects the best take per shot → stored in `05_video/selected/`
4. Selected clips go to CapCut for final editing (Phase 5: Post-Production)

**The motion script is the last creative decision before execution. After this, it is craft — not vision.**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Dramaturgy not approved | STOP. Cannot generate motion script without approved scene breakdown. |
| Selected images missing | STOP. List which scenes lack selected images. Inform human. |
| Musical metadata missing | STOP. Beat sync is impossible without temporal data. |
| Scene has no clear motion intent | Default to Mode A, Static, Motion Strength 3. Flag for human review. |
| BPM changes mid-song | Note the tempo change in the Beat Sync Notes and adjust motion strength at the transition point. |
| Scene requires transformation but only one image exists | Flag it. Suggest either generating a second image or switching to Mode A with Slow Zoom In as a simpler alternative. |
| Motion strength exceeds station norms | Flag in Director's Notes. If EP08 has a motion 8 shot, explain why it is justified. |
| Two consecutive shots have conflicting camera directions | Review and adjust. Camera direction should have spatial logic across sequences. |

---

*"Motion is the breath between the frames. Without it, the image is a photograph. With it, the image is alive."*
*— Robotiko v2.0 Pipeline*
