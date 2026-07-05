# SKILL: robotiko-motion-script
> **Version:** 2.1 | **Last Updated:** 2026-06-30
> **Trigger:** `"Generate motion script for EP{XX}"`
> **Output:** `episode-{XX}/05_video/ep{XX}_motion_script_v{VV}.md`

---

## PURPOSE

Generate a shot-by-shot motion script that defines camera movements, video generation strategy, motion intensity, and beat sync instructions for each scene of an episode. The motion script translates still images (selected visuals) into cinematic motion by telling the video generation tool (Kling / Veo / Seedance) exactly how each frame should come alive.

This is the final creative document before video generation begins. Precision here determines whether the final video breathes with the music or fights against it.

---

## ART DIRECTION PILLARS

> These principles govern ALL creative decisions in the motion script. They are non-negotiable artistic commitments — not suggestions, not nice-to-haves.

### 5 Artistic Pillars (Project DNA)

| # | Pillar | Meaning | How It Shapes Motion Scripts |
|---|---|---|---|
| 1 | **Restraint Over Spectacle** | Emotional impact over visual impact. Emptiness is a tool. | Default to lower MS. A static shot with fog > a dynamic shot with no purpose. Never add motion "because it looks cool." |
| 2 | **Single-Location Discipline** | Stay in one space; let emotional evolution carry visual interest. | Camera moves within the same frame rather than cutting to new angles. Environment breathing > environment changing. |
| 3 | **Cumulative Character Damage** | Body tells the story of ALL previous episodes. | Motion prompts reference current damage state. Element tags must match episode phase. |
| 4 | **Musical Dissonance as Choice** | Sometimes visual REFUSES to match music's energy. Dissonance = art. | Mark intentional mismatches as `[DISSONANCE]` in the musical moment field. Do not "fix" them. |
| 5 | **Camera Has Memory** | Camera moves carry meaning across scenes. Patterns establish expectations that can be broken. | Track dominant camera move per episode. Breaking the pattern = dramatic climax. |

### 5 Visual Signatures (Recognizable Identity)

| # | Signature | What It Is | Implementation in Motion Script |
|---|---|---|---|
| 1 | **Chrome Reflection** | Action shown THROUGH reflective surfaces. Character's body as mirror. | Motion prompt: "reflected in the chrome surface of [body part/object]." Camera focuses on reflection, not direct action. |
| 2 | **Architecture Cage** | Rigid geometry (desks, corridors, fluorescents) frames/traps character. | Frame composition note: character occupies <30% of frame. Environment dominates. Motion: environment breathes (lights flicker, dust drifts), character is still. |
| 3 | **Amber Pulse** | ONE warm color moment per episode in cold world. Mentor's trace / inner light. | Flag the single amber moment in Director's Notes. Motion prompt includes "warm amber light pulses once" or similar. Max 1 per episode. |
| 4 | **Still Hold** | At emotional peak, camera STOPS completely. Stillness after motion = punch. | Assign Static + MS 1-2 at the most emotionally loaded moment. Preceding shots should be MS 4+ to create contrast. |
| 5 | **Grain Crescendo** | Film grain thickens with emotional intensity. Texture as emotion. | Add grain intensity note to motion prompt at high-emotion scenes: "heavy film grain" → "extremely heavy, visible film grain." |

### Musical Dissonance Decision Criteria

When should visual REFUSE to match music?

| Music Energy | Visual Choice | Use When |
|---|---|---|
| High/Peak | Static, MS 1-2 | Character is emotionally dead while world rages. The body has given up. |
| Low/Quiet | MS 5-6, dynamic camera | Internal turmoil despite external silence. Mind racing while body is still. |
| Rising build | Camera retreats (Dolly Out) | World is offering energy but character cannot receive it. Rejection of hope. |

Mark these moments with `[DISSONANCE]` tag in the Musical Moment field. Include a 1-line justification.

Every tagged shot is logged in [`_management/dissonance_registry.md`](../../_management/dissonance_registry.md) — the human-readable ledger behind the machine exemption in `tests/energy_motion_check.py` (an exemption without a ledger is a loophole).

### Glitch Production Policy

"Glitch is Scripture" = NARRATIVE METAPHOR. In production:
- AI artifacts are DEFECTS, not art. Fix with OmniEdit or re-generate.
- Visual quality target: maximum achievable fidelity.
- "Glitch" lives in the story, not in the output quality.

---

## PREREQUISITE

> **Two conditions must be met before this skill executes:**
> 1. The dramaturgy for this episode must be **human-approved**.
> 2. Generated scene images must exist — **either** the convention-named copies in
>    `episode-{XX}/04_visuals/selected/` **or** the scene-numbered keepers in
>    `episode-{XX}/04_visuals/raw/` (`1.png`, `2.png`, …). `selected/` is the preferred, tidy input;
>    if it is empty, fall back to the numbered `raw/` keepers. Only STOP if **both** are empty.
>    (EP05 and EP07 ran straight from `raw/` — running `select_images.py` first is optional, not required.)
>
> If either condition is not met, STOP. Inform the human.

---

## MANDATORY INPUTS (Read Before Writing a Single Shot)

Read these files in this exact order:

| # | File | What to Extract |
|---|---|---|
| 1 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Approved scene breakdown, scene descriptions, mood/lighting, characters, music sync column |
| 2 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Tempo (BPM), sections with timestamps, energy levels, instruments, mood per section |
| 3 | `episode-{XX}/04_visuals/selected/` (preferred) **or** `04_visuals/raw/` (fallback) | Verify which **scene** images exist (file listing). Prefer `selected/`; if empty, use the scene-numbered `raw/` keepers (`1.png`, `2.png`, …). **Never treat reference images as scenes** — ignore any `ref_*.png` / `ep{XX}_ref_*.png` (e.g. `ref_workshop.png`, `ref_exterior.png`, `ref_onlookers.png`); they are generation references, not shots. |
| 4 | `_management/master.md` | Episode tone, station, character phase, narrative arc |
| 5 | `_templates/video_prompt_template.md` | Output structure and formatting template |

**If the musical metadata JSON is missing:** STOP. Beat sync is impossible without temporal data.
**If neither `selected/` nor the numbered `raw/` keepers exist:** STOP. The motion script references specific image files as input assets. (Reference images — `ref_*.png` — do not count; they are not scenes.)

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

**Terminology note:** "Beat sync" in this pipeline means section-level and phrase-level synchronization — aligning camera cuts, motion intensity, and visual transitions to musical section boundaries and phrase transitions. It does NOT mean frame-accurate beat-grid quantization (BPM-locked cuts on every downbeat). The musical metadata JSON provides section timestamps, not individual beat positions.

- Energy levels from the musical metadata directly inform motion intensity:
  - `low` energy → Motion strength 1-3 (subtle breathing, slow drift)
  - `medium` energy → Motion strength 4-5 (steady cinematic movement)
  - `high` energy → Motion strength 6-8 (dynamic, purposeful movement)
  - `peak` energy → Motion strength 8-10 (maximum intensity, controlled chaos)
  - `building` energy → Motion strength ramps progressively within the section
  - `medium-low` energy → Motion strength 2-3 (gentle drift, slow atmospheric movement)
  - `medium-high` energy → Motion strength 5-6 (rising intensity, fuller cinematic movement)
  - `explosive` energy → Motion strength 9-10 (maximum blast, climax-only)
  - `theatrical` energy → Motion strength 5-7 (dramatic delivery, measured grandeur)
  - `epic` energy → Motion strength 6-8 (sweeping dynamics, orchestral weight)
  - `rising` energy → Motion strength ramps progressively (similar to building)
  - `chaotic` energy → Motion strength 8-10 (unstructured intensity)
  - `fading` energy → Motion strength ramps down progressively within the section
  - `still` energy → Motion strength 1-2 (near-frozen, spoken word ambience)
  - `minimal` energy → Motion strength 1 (whisper, near-silence)
  - `slowing` energy → Motion strength ramps down with tempo deceleration

### Step 3: Identify Beat Sync Critical Points
- Scan the musical metadata for:
  - Chorus entries (high impact — visual cuts or reveals should land here)
  - Drum fills and drops (natural cut points)
  - Instrumental solos (extended single-shot opportunities)
  - Silence or breakdowns (freeze or minimal motion)
  - Energy transitions (ramp up/down in motion strength)
- These become entries in the Beat Sync Notes table.

### Step 4: Match Scene Images to Scenes
- List all files in `04_visuals/selected/`. **If `selected/` is empty, list `04_visuals/raw/` instead** and
  use the scene-numbered keepers (`1.png`, `2.png`, …).
- **Exclude reference images.** Only files whose name is a scene number (`{XX}.png`, optionally with an
  `a`–`d` sub-clip letter like `11b.png`) are shots. Skip anything else — especially `ref_*.png` /
  `ep{XX}_ref_*.png` (`ref_workshop.png`, `ref_exterior.png`, `ref_onlookers.png`, etc.). Reference images
  describe the character/environment for the generator; they are **never** a scene and must not get a shot block.
- Map each scene image to its corresponding scene in the dramaturgy (`ep{XX}_s{XX}_selected.png` → scene XX,
  or `{XX}.png` → scene XX).
- If a scene has no image in either folder, flag it — the shot cannot be generated without an asset.
- If a scene was flagged for Start/End keyframes in the dramaturgy, confirm that both `s{XX}a`/`s{XX}b`
  (or `{XX}a.png`/`{XX}b.png`) images exist (or that two separate scene images are available for the transformation).
- In each shot's **Assets Required** field, write the path of whichever folder you actually used
  (`selected/…` or `raw/…`) so the human knows exactly which file feeds the clip.

### Step 5: Determine Tech Strategy Per Shot
Assign one of two video generation modes to each shot:

| Mode | When to Use | Input | Duration | Motion Strength Range |
|---|---|---|---|---|
| **A — Standard** | Atmospheric shots, simple movement, single subject, no transformation | 1 selected image | 5s or 10s (tool-dependent) | 1-8 |
| **B — Start/End Keyframes** | Transformations, morphing, character state changes, location transitions, complex travel | 2 selected images | 5s or 10s | 3-8 |

Decision logic:
- Does the scene involve transformation or before/after change? → **Mode B**
- Is it a single atmospheric moment, character portrait, or environmental shot? → **Mode A**

> **Field note — wide-reveal moves invite hallucination (S30 rescue pattern):** A
> wide-reveal move (Slow Zoom Out, Crane Up, Dolly Out) from a **single start frame**
> asks the model to fill area beyond the source borders — and it fills it by
> *inventing* content (set dressing, structures, props) that is not in the universe.
> When the reveal itself matters, do NOT trust Mode A: prefer **Mode B** with an
> existing wide frame from the episode's own `raw/` set as the **end frame**, so the
> pull-back interpolates toward a real destination instead of extrapolating into
> invention. EP09 S30 "Full Kintsugi" failed four Mode-A reshoots this way, then
> succeeded first-try once an existing exterior keeper was pinned as the end frame.
> Full case + before/after prompts: `docs/hallucinating-camera.md`.

> **Note:** Mode C (Extension) has been deprecated. Video generation tools produce fixed-duration clips (5s or 10s) with no chaining capability. Scenes longer than 10s are handled through the Duration Coverage Strategy (Step 6).

### Step 6: Duration Coverage Analysis (CRITICAL)

**This step prevents the duration gap problem.** Calculate coverage for every shot:

1. For each shot, compute: `scene_duration = timestamp_end - timestamp_start`
2. Apply the Duration Coverage Strategy:

| Scene Duration | Strategy | Clip Count | Notes |
|---|---|---|---|
| ≤ 5s | **Direct** | 1 × 5s | Trim excess in CapCut |
| 6–10s | **Direct** | 1 × 10s | Trim in CapCut. If tool is 5s-only: 1 × 5s + speed ramp |
| 11–15s | **Speed Ramp** | 1 × 10s + slow-mo (max 1.5×) | If tool is 5s-only: 2 × 5s |
| 16–30s | **Multi-Clip** | ⌈duration / 10⌉ × 10s clips | Each sub-clip gets own camera move + motion prompt |
| 30s+ | **Multi-Clip** | ⌈duration / 10⌉ × 10s clips | May need supplementary images |

3. For Multi-Clip shots, define sub-clips (labeled a, b, c, d...):
   - Each sub-clip gets its own camera move and motion prompt
   - Sub-clips should create visual variety (different camera moves, not identical repetitions)
   - Determine which sub-clips can reuse the existing selected image and which need new images

4. For sub-clips requiring new images, include an inline **Supplementary Visual Prompt**:
   - Must follow all visual prompt rules (mandatory suffix, character phase, forbidden aesthetics)
   - Include the expected selected image filename
   - The human generates the image from this prompt before video generation

5. Calculate totals:
   - Total generated clip duration must be ≥ 95% of total music duration
   - Document the coverage ratio in the Coverage Summary section

### Step 7: Tool Assignment Analysis

After determining coverage strategy (Step 6), assign an AI video generation tool to each clip based on capabilities, budget, and quality requirements.

#### Tool Inventory

| Tool | Keyframe Support | Resolution | Duration | Camera Movement | Cost Model | Elements Support |
|---|---|---|---|---|---|---|
| **Kling 3.0** | Start + End | 1080p | 5s or 10s | Full vocabulary | Credits (paid) | ✅ Yes |
| **Kling 2.5 Turbo** | Start + End | 1080p | 5s or 10s | Static only | Credits (paid) | ❌ No |
| **Seedance 1.0 (CapCut)** | Start + End | 1080p | 5s or 10s | Limited | 25cr/5s, 50cr/10s | ❌ No |
| **Google Veo** | None | ~1080p | 8s fixed | Limited | Free (daily limit) | ❌ No |

> Tool inventory may change between episodes. Always check `_management/project_metadata.json` for current tool availability and credit budgets before assigning.

#### Assignment Rules (Priority Order)

1. **Mode B → Kling 3.0** — Transformation shots need maximum visual quality + camera movement. Kling 3.0 is the only tool that combines keyframe support with full camera vocabulary.
2. **Element-tagged shots → Kling 3.0 only** — Elements is a Kling 3.0 exclusive feature. No other tool supports @Name references.
3. **Camera movement shots → Kling 3.0** — Any shot requiring zoom, dolly, tilt, crane, pan, or orbital.
4. **Static camera + simple shot → Kling 2.5 Turbo** — Budget-efficient for atmospheric/still shots.
5. **Map/texture shots → Kling 2.5 Turbo or Kling 3.0** — Seedance performs poorly on abstract/texture content.
6. **Character close-ups → Kling 3.0** — Chrome detail, eye color, wire textures are resolution-sensitive and benefit from Elements consistency.
7. **Standalone detail shots (no camera move, no Element) → Seedance 1.0** — Budget diversification for simple character-focused scenes.
8. **Veo → diminished role** — Free daily limit useful for test renders or non-critical atmospheric shots only.

#### EP07+ Tool Distribution Target

| Tool | Target % | Role |
|---|---|---|
| Kling 3.0 | 70-80% | Primary. Camera moves, Mode B, Elements. |
| Kling 2.5 Turbo | 5-10% | Static budget shots only. |
| Seedance 1.0 | 10-20% | Standalone detail, character-only, no camera move. |
| Veo | 0-5% | Test renders, non-critical atmospherics. |

#### Budget Tracking

For each tool, calculate:
- Total credits consumed by all assigned clips
- Remaining buffer (for retakes + OmniEdit reserve)
- Aim for ≥15% buffer per paid tool
- Reserve 10-15% of Kling credits for OmniEdit fixes

#### Output Requirements

- Add `| **Recommended Tool** |` field to every clip's table (after Motion Strength)
- Format: `{Tool Name} ({Mode}, {resolution}) — {brief rationale}`
- Add a **Tool Assignment Summary** section between Video Strategy Reference and Motion Script sections
- Summary must include: tool distribution table, assignment rules applied, clips-by-tool list, credit budget

---

## KLING 3.0 FEATURES

> EP07+ uses Kling 3.0 as the dominant generation tool. These features are Kling 3.0 exclusive.

### Elements (Character Consistency)

Elements are named persistent character references. Upload reference images, tag with @Name in prompts, and Kling 3.0 maintains visual consistency across all clips using that Element.

#### Element Registry Template

Before the shot-by-shot section, define ALL Elements used in this episode:

```
## Element Registry

| Element Name | Description | Reference Images | Episodes Active |
|---|---|---|---|
| @Damaged | Robotiko EP07 state (missing ear, torso dent, forearm tattoos) | android_damaged.png, android_damaged_2.png, android_damaged_3.png | EP07 |
| @Crane | Turna (crane bird) companion | crane_ref_01.png, crane_ref_02.png | EP10 |
```

#### Angles 2.0 Protocol

For each Element, generate 12 reference angles from the master reference photo:
1. Upload master ref to Kling 3.0 Elements → "Generate Angles"
2. System produces 12 auto-generated angle variations
3. Review: reject any that deviate from character design (wrong damage state, incorrect eye rendering)
4. Approved angles become the Element's reference set

#### Element Usage Rules

1. **Kling 3.0 only** — Elements do NOT work in Kling 2.5 Turbo, Seedance, or Veo. If a clip uses Elements, it MUST be assigned to Kling 3.0.
2. **Max 2 Elements per clip** — Kling 3.0 supports up to 2 named Elements in a single generation.
3. **Tag format in motion prompt** — Reference by @Name: "The @Damaged chrome android walks through rain..."
4. **Element state must match episode phase** — Do NOT use @Pristine references for EP07+. Check `character_profiles.json` for current phase.
5. **Test with single Element first** — EP07 uses only @Damaged (single character, single state). Multi-Element (EP10: @Damaged + @Crane) requires separate testing.

#### Progressive Transformation (EP08+)

For episodes where character appearance evolves across the episode (EP08: 40 days of weathering):

**Strategy: Phase-Staged Elements** (to be tested in EP08 production)
- Create 2-3 Element variants per episode: @Phase1, @Phase2, @Phase3
- Assign phase boundaries at specific timestamps in the episode
- Switch Element tag at phase transitions
- This creates gradual visual evolution without per-clip inconsistency

> ⚠️ This strategy is PLANNED but UNTESTED. Test during EP08 production. If results are poor, fall back to single Element + descriptive prompts for evolution.

### Generation Mode Field

Each clip must specify its generation mode:

| Generation Mode | Description | When to Use |
|---|---|---|
| **Standard** | Single image input, standard generation | Default for most clips |
| **Mode B** | Start + End keyframe pair | Transformations, morphs |
| **Multi-shot** | Up to 6 segments, 15s max, single continuous video | DISABLED for primary strategy (retake fallback only) |

> **Multi-shot constraint:** Cannot combine with Mode B. Use only when sub-clips share the same source image AND are all Kling 3.0 AND smooth transitions are more important than individual retake capability.

---

### Frame Chaining

Frame Chaining creates visual continuity between consecutive clips by using the last frame of one clip as the start frame of the next.

#### Protocol

1. Generate the upstream clip (Clip A)
2. Export/download the last frame of Clip A
3. Upload that frame as the Start Frame for Clip B
4. Generate Clip B — it begins exactly where Clip A ended

#### Rules

| Rule | Detail |
|---|---|
| **Max chain length** | 3 clips. Beyond 3, quality degrades and error compounds. |
| **Location breaks chain** | If the next clip is a different location, start fresh. Do not chain across locations. |
| **Dependency warning** | Upstream failure = entire chain must restart. If Clip A fails, Clip B and C are invalid. |
| **Notation in motion script** | Mark chained clips: `| Frame Chain | ← S{XX}a (last frame) |` |
| **When to use** | Same-location multi-clip shots where camera continuity matters (walking sequences, slow reveals, extended solos). |
| **When NOT to use** | Different locations, different camera angles, hard cuts, different Elements. |

#### Frame Chain Map (Output Section)

After the Beat Sync Notes, include a Frame Chain Map showing all chains:

```
## Frame Chain Map

| Chain | Clips | Location | Notes |
|---|---|---|---|
| Chain 1 | S12a → S12b → S12c | Office corridor | Walking sequence, dolly follows |
| Chain 2 | S28a → S28b | Mountain path | Ascent continues |
```

---

### OmniEdit Protocol

OmniEdit is Kling 3.0's post-generation editing tool. It fixes specific issues in already-generated clips without full re-generation.

#### When to Use OmniEdit vs Re-Generate

| Issue | Action | Reason |
|---|---|---|
| Phantom character spawned in background | OmniEdit: remove | Cheaper than full re-gen; composition is otherwise good |
| Wrong texture on one element | OmniEdit: fix | Targeted fix preserves the good parts |
| Character face distorted | Re-generate | Face issues are too fundamental for edit |
| Wrong camera direction entirely | Re-generate | Composition failure = start over |
| Color/lighting inconsistency | OmniEdit: adjust | Quick atmospheric fix |
| Motion too fast/slow | Re-generate with adjusted MS | OmniEdit cannot change motion parameters |
| Limb distortion (extra fingers, bent arm) | OmniEdit: fix | If composition is otherwise strong; re-gen if severe |

#### Budget

- Reserve 10-15% of total Kling credits for OmniEdit
- Priority scenes for OmniEdit investment:
  - Dual-character scenes (highest spawn risk)
  - Mode B clips (hardest to re-generate cleanly)
  - Atmospheric/environmental shots (easiest to fix with targeted edits)
  - Visual signature moments (Chrome Reflection, Amber Pulse)

#### Decision Tree

```
Clip generated → Review quality:
├── Acceptable as-is → DONE
├── Minor fixable issue (spawn, texture, color) → OmniEdit
├── Major structural issue (face, motion, composition) → Re-generate
└── Multiple issues → Re-generate (OmniEdit for 1-2 issues max)
```

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

### Camera Move Diversity Rule (v2.0)

> Camera monotony kills cinematic quality. EP06 had 42% Slow Zoom In — never again.

| Rule | Threshold | Enforcement |
|---|---|---|
| **No single move dominates** | No camera move >30% of total clips | If exceeded: redistribute to secondary moves |
| **Local variety** | Every 5 consecutive clips must use ≥3 different moves | If violated: swap middle clip to a different move |
| **Accent moves are special** | Orbital, Handheld, Crane (Up/Down) — max 2-3 uses per episode | Reserve for emotional peaks only |
| **Static has weight** | Static ≥15% of clips minimum | Stillness is a choice, not filler — but it must be present |
| **Episode personality honored** | Dominant move must match the Episode Camera Personality table | See below |

> **Machine-checked** by `tests/motion_script_validator.py` (via `tests/run_all.py`):
> the 30% / 15% quotas, the 5-clip local window, one-move-per-clip, and the accent
> budget (2-3 is the soft zone; **>3 uses of any single accent move is the violation**)
> all FAIL a SKILL-v2 script. Personality is WARN-only — artistic judgement stays human.
> The energy→motion mapping (Step 2) is cross-checked as an advisory tier by
> `tests/energy_motion_check.py`: `[DISSONANCE]`-tagged shots are exempt, ramp
> energies get a ±1 wider band, and its warnings never block.

#### Camera Diversity Report (Output Section)

After the Coverage Summary, include:

```
## Camera Diversity Report

| Camera Move | Count | % of Total | Limit | Status |
|---|---|---|---|---|
| Dolly Out | 12 | 27% | 30% max | ✅ |
| Static | 10 | 22% | 15% min | ✅ |
| Slow Zoom In | 8 | 18% | 30% max | ✅ |
| ... | ... | ... | ... | ... |

Local variety check: ✅ All 5-clip windows contain ≥3 different moves.
Accent move budget: Orbital ×2, Crane Up ×1 — within limits.
```

**Director's guard:** Camera diversity quotas are a floor, not a ceiling — and never a substitute for motivation. Every camera move must first be justified by the moment it serves: what the narrative demands, what the music suggests, what the frame composition allows. A move that satisfies the quota but serves no dramatic purpose is worse than a quota violation with a justified `[DISSONANCE]` tag. The quotas prevent the monotony trap (EP06's 42% zoom-in); the director's eye prevents the checkbox trap.

---

### Episode Camera Personalities (EP07-10)

Each episode has a **camera personality** — a dominant emotional strategy expressed through camera moves. This is not just "use more X" — it's "this episode's camera FEELS like Y."

#### EP07: "The Silence Protocol" — THE RETREATING CAMERA

| Aspect | Detail |
|---|---|
| **Primary move** | Dolly Out (25-30%) — world pushes Robotiko away, he shrinks |
| **Secondary move** | Static (20-25%) — emptiness between retreats |
| **Pattern** | 5× "HERE/NOT" refrains = camera progressively MORE distant each time |
| **Climax reversal** | "I AM COMING" = first Dolly In of entire episode. Pattern broken. |
| **Unifying motif** | Rain across ALL locations (wet, grey, same feeling everywhere) |
| **Piano interludes** | Character ABSENT. Environment only. Architecture Cage pure. |
| **MS average** | ~3.0 (lowest of series). Chorus peaks: MS 6-7. |
| **Tone** | Modern human condition — unemployment, alienation, purposelessness. RELATABLE-dark. |

#### EP08: "40 Days Offline" — THE WITNESSING CAMERA

| Aspect | Detail |
|---|---|
| **Mountain ascent** | Dolly alongside → Crane Up. Robotiko AHEAD of camera for first time. |
| **Fire / Burn the Database** | STATIC. Camera witnesses, doesn't participate. (Tarkovsky influence) |
| **Jung "Obsolete"** | Orbital — circling still figure, shadow grows |
| **Voices like seagulls** | Crane Up/overhead — character below, particles/light above |
| **Nature** | Realistic, raw (rocks, wind, earth). NOT abstract/minimal. |
| **40 days passage** | Light + body + texture evolve together (gradual, imperceptible) |
| **MS average** | ~3.5-4.5. Peaks at ritual/fire moments. |

#### EP09: "Shadow Debugging" — THE DISCOVERING CAMERA

| Aspect | Detail |
|---|---|
| **Philosophy** | Parça → Bütün (close-up broken → zoom out reveals gold-filled) |
| **Camera = scientist** | Cold, observing, documentary. But observation reveals beauty. |
| **Primary move** | Slow Zoom Out — NOT retreat (that's EP07). Here it means "understanding widens." |
| **Climax Still Hold** | "Glitch is Scripture" line = camera stops. Long Static. Words carry. |
| **MS average** | ~3.0-3.5. Spoken word pacing — slower, more contemplative. |

#### EP10: "The Glitch Scripture" — THE COMPANION CAMERA

| Aspect | Detail |
|---|---|
| **Turna (Crane bird)** | Arrives mid-episode. Robotiko mounts turna, flies to world locations. |
| **Pre-turna** | Camera alongside on ground (walking WITH, not observing FROM) |
| **With turna** | Aerial sequences, location transitions, flight. |
| **Camera = fellow traveler** | Not observing FROM outside — existing WITH the character. |
| **8→∞ moment** | Crane Up (camera rises) while world OPENS (character doesn't shrink) |
| **Final frame** | Camera stops. Robotiko continues. Open ending = infinite. |
| **Elements** | @Robotiko + @Crane as named Elements. |
| **MS average** | ~4-5. Flowing, confident, unhurried. |

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
- **EP07 exception:** MS average ~3.0 despite being in Destruction arc. The darkness is quiet, not loud.

---

## MOTION PROMPT WRITING GUIDE

The Motion Prompt is fed directly to the video generation tool (Kling / Veo / Seedance). It must contain ONLY what the tool can see and execute — pure visual and motion descriptions. The tool does not know our characters, our music, or our story.

Musical context belongs in the **Musical Moment** field. Narrative context belongs in the **Scene Context** field. The Motion Prompt is ONLY for the video generation tool.

### DO:
- Describe what moves, how fast, and in what direction
- Specify atmospheric motion: fog, dust, light flickers, wire sway, ember drift
- Describe characters by their visual appearance ("chrome android", "robed figure with glowing staff")
- **Keep it SHORT — max 2-3 sentences before the video suffix.** Video tools respond to atmosphere + mood keywords (glowing, hypnotic, charred, decay) far better than literal micro-descriptions (halftone dots large as coins, paper fibers visible as individual strands). Over-detailed prompts confuse the model.
- Use strong evocative adjectives rather than precise physical measurements
- Describe visible light changes, color shifts, particle effects
- When using Elements: reference by @Name tag ("The @Damaged chrome android...")

### DON'T:
- Use character names (Robotiko, Mentor) — the tool doesn't know them (but @Name Element tags ARE allowed)
- Reference musical instruments (Hammond organ, fuzz guitar, bass drop) — the tool doesn't hear music
- Include narrative commentary ("the only honest light in EP02", "this is Tuesday")
- Add speed ramp technical notes ("0.71× slowdown will make...") — that's post-production info
- Include audience/viewer direction ("the audience needs time to read")
- Write poetic metaphors the tool cannot render ("approaching the sermon", "a congregation drawn to the preacher")
- Add timing cues (BPM, "on the downbeat", "at ~1:31") — the tool doesn't know the timeline
- Repeat the visual description from the dramaturgy or visual prompt
- Request impossible physics (an AI video model cannot rotate a subject 360° from a single still image)

### Mandatory Video Style Suffix

Append this to the end of every motion prompt — no exceptions:

> Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.

This is the video equivalent of the visual prompt suffix. It ensures consistent 70s analog aesthetic across all video generation tools (Kling, Veo, Seedance 1.0).

### Mandatory Anti-Spawn Guard

Append this AFTER the video style suffix on every motion prompt — no exceptions:

> Do not add extra characters. Keep everything as pictured.

Video generators (Kling, Veo, Seedance) spawn phantom characters in backgrounds — flickering, glitching figures that waste credits on retakes. This guard line prevents the tool from adding elements not present in the source image. Apply to ALL prompts, not just crowd scenes.

### Crowd Scene Micro-Motion Protocol

In scenes with multiple characters (2+ people), follow these rules strictly:

1. **Specify exact count and appearance** — "four men in black vests", NOT "smiling touts" or "a group of men"
2. **Lock positions** — Include "remain in their exact positions" in the prompt
3. **Micro-actions only** — Limit character movement to: subtle head nods, slow head pan, slight head tilt. NEVER use broad gestures (beckoning, leaning in, gesturing warmly, waving)
4. **Environmental motion for liveliness** — Use neon sign flicker, smoke drift, light reflections instead of character movement to make the scene feel alive
5. **Static background** — Add "Background remains static" for scenes with background crowds

**Why:** Plural group descriptions + broad gestures cause video generators to spawn duplicate characters and distort limbs. Specifying count, locking positions, and limiting to micro-motion prevents this.

### Image Fidelity & Representation Rules

- **Source images are production-ready.** Video generators must animate them faithfully — not reinterpret, enhance, or "improve" visual elements.
- **Protect abstract elements:** When the source image contains silhouettes, blurred figures, abstract textures, or intentionally undefined elements, the motion prompt MUST include explicit preservation language: "maintain as featureless dark shapes, do not resolve into detailed figures."
- **Gender diversity:** All crowd, audience, mob, and group references MUST specify "mixed men and women." Never leave group descriptions as implicitly all-male.
- **Video generators will "clarify" ambiguity** — they turn silhouettes into photorealistic faces, blurred shapes into detailed objects. The motion prompt must actively prevent this.

### EXAMPLE (Good — character scene with Element):
> The @Damaged chrome android stands in pouring rain, water streaming down chrome surfaces. Slow head tilt downward. Fog drifts at knee level, neon reflections shimmer on wet pavement. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

### EXAMPLE (Good — texture/map scene):
> Extreme close-up on a glowing red light marker on a charred, burnt map. The red light pulses slowly and hypnotically. The surrounding paper is heavily textured with ashes and decay. Cinematic 35mm film style, heavy film grain, shallow depth of field, Kodachrome colors, 16:9. Do not add extra characters. Keep everything as pictured.

### EXAMPLE (Bad — narrative/musical contamination):
> Slow zoom in toward Robotiko's face as the Hammond organ swell builds. The slowdown to 0.71× will make the approach feel reverential — a congregation drawn to the preacher in suspended time.

### EXAMPLE (Bad — vague and empty):
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
| Camera Personality | [from Episode Camera Personalities table — e.g., "THE RETREATING CAMERA"] |
| Dominant Energy | [overall energy character of this episode] |
| Total Shots | [must match scene count] |
| Total Duration | [MM:SS from musical metadata] |

### 2. Element Registry
Define all Elements used in this episode (see Element Registry Template above). If no Elements used, state "None — pre-Element episode."

### 3. Video Strategy Reference
Quick reference table for Mode A / B with usage criteria.

### 4. Tool Assignment Summary
Tool distribution table, assignment rules applied, clips-by-tool list, credit budget.

### 5. Motion Script (Shot by Shot)
Each shot block contains:

| Field | Description |
|---|---|
| **Shot ID** | S{XX} — matches dramaturgy and visual prompt scene ID |
| **Shot Title** | Brief descriptive title |
| **Timestamp** | From musical metadata |
| **Scene Duration** | Calculated duration in seconds |
| **Coverage Strategy** | Direct / Speed Ramp (with ratio) / Multi-Clip (with count) |
| **Musical Moment** | What is happening in the music at this exact moment. Add `[DISSONANCE]` tag if intentional mismatch. |
| **Scene Context** | 1-sentence reference to the approved dramaturgy |
| **Tech Strategy** | Mode A / Mode B |
| **Generation Mode** | Standard / Multi-shot / Mode B |
| **Element Tags** | @Name1 / @Name1 + @Name2 / None |

**For Direct and Speed Ramp shots (single clip):**

| Field | Description |
|---|---|
| **Clip Duration** | 5s / 10s |
| **Motion Strength** | 1-10 |
| **Recommended Tool** | Tool name, mode, resolution, brief rationale |
| **Assets Required** | Start Frame path (and End Frame path if Mode B) |
| **Camera Move** | One move from the approved vocabulary |
| **Motion Prompt** | Pure visual/motion description for the video generation tool (no character names, no music references) |
| **Speed Ramp** | (Speed Ramp only) Target playback ratio, e.g., "0.7× (10s → 14s)" |
| **Frame Chain** | (If chained) `← S{XX}[a|b|c] (last frame)` or `None` |

**For Multi-Clip shots (multiple sub-clips):**

Each sub-clip (Clip A, Clip B, etc.) contains:

| Field | Description |
|---|---|
| **Sub-clip ID** | S{XX}a / S{XX}b / S{XX}c / etc. |
| **Clip Duration** | 5s / 10s |
| **Motion Strength** | 1-10 |
| **Recommended Tool** | Tool name, mode, resolution, brief rationale |
| **Generation Mode** | Standard / Multi-shot / Mode B |
| **Element Tags** | @Name1 / @Name1 + @Name2 / None |
| **Assets Required** | Image path. If new image needed: `⚠️ NEW IMAGE REQUIRED` + inline supplementary visual prompt |
| **Camera Move** | One move from the approved vocabulary |
| **Motion Prompt** | Pure visual/motion description for this sub-clip (no character names, no music references) |
| **Frame Chain** | (If chained) `← S{XX}[a|b|c] (last frame)` or `None` |

### 6. Beat Sync Notes
Critical musical moments requiring precise visual synchronization:

| Timestamp | Musical Event | Required Visual Action |
|---|---|---|
| MM:SS | [specific musical event] | [specific visual response] |

### 7. Frame Chain Map
All frame chains in the episode (see Frame Chaining section above).

### 8. Coverage Summary

| Metric | Value |
|---|---|
| Total music duration | [seconds] |
| Total generated clip duration | [seconds] |
| Coverage ratio | [percentage] |
| Total clips | [number] (single clips + sub-clips) |
| Clips from existing images | [number] |
| Clips needing new images | [number] |

### 9. Camera Diversity Report
Camera move distribution and diversity checks (see Camera Move Diversity Rule section above).

### 10. Director's Notes
- MS average for this episode vs target
- Visual signature moments flagged (which shots use Chrome Reflection, Amber Pulse, Still Hold, Grain Crescendo)
- Any `[DISSONANCE]` moments and their justification
- Camera personality pattern compliance
- OmniEdit priority scenes flagged

### 11. Approval Status
Checkboxes: Human reviewed camera moves, Human reviewed tech strategy, Human reviewed coverage, Human reviewed camera diversity, Human reviewed Element assignments, Human approved, Ready for video generation.

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
- **Dolly Out → Dolly Out → Dolly In** = the EP07 pattern. Retreat, retreat, APPROACH (climax reversal).

### Continuity
- If two consecutive shots share the same location, consider Frame Chaining for seamless flow.
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

**Core Requirements:**
- [ ] **Duration coverage:** Total generated clip duration ≥ 95% of total music duration
- [ ] Every clip (including sub-clips) references an existing selected image or has a flagged supplementary visual prompt
- [ ] Every clip has exactly one camera move from the approved vocabulary
- [ ] Motion strength values align with the musical energy arc (no motion 9 during a quiet bridge)
- [ ] Tech strategy (A/B) is appropriate for each shot's requirements
- [ ] Beat Sync Notes table includes all critical musical moments (chorus entries, drops, solos, silence)
- [ ] No clip combines multiple camera moves (one move per clip — strict)
- [ ] Motion prompts describe movement, not visual appearance
- [ ] Shot sequence follows rhythm principles (no three consecutive high-intensity shots without a breath)
- [ ] Sub-clips within a shot use varied camera moves (not identical repetitions)
- [ ] Average motion strength matches the episode's station energy
- [ ] Supplementary visual prompts include the mandatory suffix and respect character phase
- [ ] Coverage Summary section is present and accurate

**Tool Assignment:**
- [ ] Every clip has a Recommended Tool assignment
- [ ] All Mode B shots assigned to Kling 3.0
- [ ] All Element-tagged shots assigned to Kling 3.0
- [ ] No Speed Ramp shots assigned to fixed-duration tools without verifying slowdown limit
- [ ] Total credits per paid tool ≤ budget (with ≥15% buffer for retakes)
- [ ] 10-15% of Kling credits reserved for OmniEdit
- [ ] No character close-ups assigned to low-resolution tools
- [ ] Tool Assignment Summary section is present and accurate

**Camera Diversity (v2.0):**
- [ ] No single camera move exceeds 30% of total clips
- [ ] Every 5 consecutive clips use ≥3 different moves
- [ ] Accent moves (Orbital, Handheld, Crane) ≤3 uses each
- [ ] Static ≥15% of clips
- [ ] Episode Camera Personality dominant move is honored
- [ ] Camera Diversity Report section is present and accurate

**Kling 3.0 Features (v2.0):**
- [ ] Element Registry is defined (or marked "None")
- [ ] All Element-tagged clips specify correct @Name for episode phase
- [ ] Generation Mode field present for every clip
- [ ] Frame Chain Map is present (or marked "No chains")
- [ ] Frame chains do not exceed 3 clips
- [ ] Frame chains do not cross location boundaries

**Art Direction (v2.0):**
- [ ] At least one Still Hold moment at emotional peak (Static + MS 1-2 after MS 4+ sequence)
- [ ] Maximum one Amber Pulse moment flagged in Director's Notes
- [ ] Any `[DISSONANCE]` moments are justified
- [ ] Director's Notes section identifies visual signature moments
- [ ] Approval checkboxes are present at the bottom

**Final:**
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## WHAT HAPPENS NEXT

After human approves the motion script:
1. Human creates Elements in Kling 3.0 (upload refs, generate Angles 2.0, approve)
2. Human feeds each shot to its **Recommended Tool** (per the Tool Assignment Summary) with:
   - The selected image(s) as input
   - The Element @Name tag (if applicable)
   - The camera move instruction
   - The motion prompt as descriptive guidance
   - The motion strength as intensity parameter
3. Generated clips are stored in `05_video/raw/`
4. Human reviews: Accept / OmniEdit fix / Re-generate
5. Human selects the best take per shot → stored in `05_video/selected/`
6. Selected clips go to CapCut for final editing (Phase 5: Post-Production)

**The motion script is the last creative decision before execution. After this, it is craft — not vision.**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Dramaturgy not approved | STOP. Cannot generate motion script without approved scene breakdown. |
| Scene images missing (both `selected/` and numbered `raw/` empty) | STOP. List which scenes lack an image in either folder. Reference images (`ref_*.png`) do not count. Inform human. |
| Musical metadata missing | STOP. Beat sync is impossible without temporal data. |
| Scene has no clear motion intent | Default to Mode A, Static, Motion Strength 3. Flag for human review. |
| BPM changes mid-song | Note the tempo change in the Beat Sync Notes and adjust motion strength at the transition point. |
| Scene requires transformation but only one image exists | Flag it. Suggest either generating a second image or switching to Mode A with Slow Zoom In as a simpler alternative. |
| Motion strength exceeds station norms | Flag in Director's Notes. If EP08 has a motion 8 shot, explain why it is justified. |
| Two consecutive shots have conflicting camera directions | Review and adjust. Camera direction should have spatial logic across sequences. |
| Camera diversity threshold exceeded | Redistribute: swap overused move for secondary options. Document in Director's Notes. |
| Element not available for episode | STOP. Elements must be created in Kling 3.0 before generation. Inform human. |
| Frame chain upstream clip fails | Entire chain invalidated. Re-generate from chain start. |
| OmniEdit budget exhausted | Switch to re-generation only. Flag remaining priority scenes. |

---

*"Motion is the breath between the frames. Without it, the image is a photograph. With it, the image is alive."*
*— Robotiko v2.0 Pipeline*
