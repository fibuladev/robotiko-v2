# PRODUCTION PIPELINE & QUALITY ASSURANCE
> **Version:** 2.7
> Always refer to `_management/master.md` as the absolute source of truth.

---

## THE GOLDEN RULE: CHAIN OF THOUGHT
Output of Step N = Input of Step N+1.
**Never skip a step. Never guess. Always refer to the Master.**

---

## MANDATORY CHECKPOINTS (Human Approval Required)
Three steps require explicit human approval before proceeding. Everything else Claude executes and delivers:

1. **After Dramaturgy (gate 1)** → Human reviews and approves the scene breakdown before visuals begin.
2. **After Reference Authoring (gate 1R)** → Human generates and approves the episode's reference IMAGES before any scene prompt is written (the two-phase visual-prompts split; see Step 5a → 5b).
3. **After Motion Script (gate 2)** → Human reviews camera moves and tech strategy before video generation.

Each gate is recorded **as data** in `_management/approvals.json` — one entry per gate (`episode`, `gate`, `artifact`, `sha256`, `date`, `note`). The ledger certifies that a human approved a specific artifact on a date; the `sha256` pins WHICH bytes were approved, so post-approval drift is visible. `pipeline_integrity.py` consumes the file: an artifact beyond a gate with no record = FAIL.

- **Honest limit of gate 1R:** it attests the human approved the reference PROMPTS and signed off the reference IMAGES generated from them. Those images live in gitignored `raw/` and are NOT machine-verifiable — preventive at the skill layer, detective at CI, the same posture as gates 1 and 2.
- **Scope of gate 1R:** **EP10 onward** (`TWO_PHASE_FROM_EP = 10` in `tests/pipeline_integrity.py`). EP01-09 predate the two-phase split and are exempt; EP10's legacy v01 (authored pre-split) carries an artifact-pinned 1R waiver until the two-phase v02 run records the real gate. The code enforces the cutover — this note is a summary, not the rule.

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
  - `episode-{XX}/02_music/ep{XX}_audio_v01.wav` (stored on Google Drive)

### Step 2: Musical Metadata JSON
- **Input:** Audio file + Lyrics
- **Tool:** Human provides BPM + Key (from [vocalremover.org](https://vocalremover.org/key-bpm-finder)) + timestamped lyrics → Claude executes `_skills/robotiko-musical-metadata/SKILL.md`
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
- **Output:** `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md`
- **Format:** Scene-by-scene table with: Shot ID, Timestamp, Visual Description, Mood/Lighting, Characters, User Override flag
- **⛔ MANDATORY CHECKPOINT:** Human reviews and approves before Phase 3 begins.

---

## PHASE 3: VISUAL PRODUCTION

Visual prompts are generated in **two phases separated by a hard human gate** (the Reference Gate, 1R). The old single-pass flow wrote reference prompts and ALL scene prompts at once against a text contract, then generated the reference images afterward — a reconciliation "Framing Pass" was "never a blocker" and in practice was skipped (REF B reframe, commit `a98acbc`: the REF block was updated, 40 scenes never re-checked). The two-phase split makes reference-first (ADR-0007) structural: refs are authored and approved as real pixels BEFORE any scene is framed to them.

### Step 5a: Reference Authoring (Phase 1)
- **Input:**
  - Approved `ep{XX}_dramaturgy_v{VV}.md` (its **location labels** are the ceiling for decomposition)
  - `_assets/cast/character_profiles.json` (mandatory — character state, `phase_reference_map`)
  - `_management/master.md` (visual suffix, color palette, forbidden aesthetics)
- **Tool:** Claude executes `_skills/robotiko-visual-prompts/SKILL.md` (Phase 1)
- **Output:** `episode-{XX}/04_visuals/ep{XX}_visual_prompts_v01.md` — a **complete Phase-1 document**: reference prompts (environments + body states + groups) + ART DIRECTION LOCKS + scene→space coverage map + Phase-1 sentinel. **Zero scene prompts, by design.**
- **Method:**
  - **Step 0 — Location decomposition.** Split each dramaturgy location into its distinct camera-spaces using the operational site-map + landmark-consistency test — replacing the old "a location in 3+ scenes gets one ref" heuristic that under-decomposed the EP09/EP10 town and cost the late REF E/REF F reshoots.
  - **Enumerate every new reference** — environments AND body-state AND group refs. ADR-0007's original driver was a CHARACTER ref (the EP09 kintsugi body), so character/group refs are gated at 1R alongside environments.
  - **Scene→space coverage map** — a table mapping every dramaturgy scene to the reference (or `ref-less`) it will frame to. This is the artifact the director validates ref coverage against the story on cheap text, AT the gate, before spending days generating. It is also the index of **which scenes to re-verify if a reference is ever edited late** (see the B-Residue Backstop below).
  - **Rationale:** `_management/adr/0007-reference-first-or-pay-the-reshoot-tax.md` — reference-first buys back the 8-10x reshoot tax EP09 paid conjuring scenes from text against the wrong reference. Phase 1 makes it structural rather than a skippable Framing Pass.
- **Skill:** `_skills/robotiko-visual-prompts/SKILL.md`

### ⛔ MANDATORY CHECKPOINT: THE REFERENCE GATE (gate 1R)
Between Phase 1 and Phase 2. **Phase 2 does not begin until it clears. Never skip it.** The human generates every reference image listed in the v01 document into `episode-{XX}/04_visuals/raw/` as `ep{XX}_ref_{name}.png`, iterates freely (this is the cheap place to catch a roof clash, a drifted castle, a glowing amber tip), and approves the reference SET **before any scene prompt is written.**

- On approval, **gate 1R is recorded as data** in `_management/approvals.json` (`gate: "1R"`, `artifact:` the v01 path, `sha256`, `date`, `note`), **sha-pinned to the frozen v01 bytes.** From this point v01 is frozen; a later edit to it fires the existing sha-drift WARN — the honest late-ref-edit signal. `project_metadata.json` `production.visuals` moves to the half-state `"refs_approved"`. This mirrors gates 1 (dramaturgy) and 2 (motion script).
- **Honest limit.** 1R attests the human approved the reference PROMPTS and signed off the reference IMAGES generated from them. The images live in gitignored `raw/` and are NOT machine-verifiable — preventive at the skill layer, detective at CI, same posture as gates 1/2.
- **Scope.** EP10 onward (`TWO_PHASE_FROM_EP = 10`). EP01-09 are exempt (pre-split legacy); EP10's v01 carries an artifact-pinned 1R waiver until the two-phase v02 run records the real gate. The code (`tests/pipeline_integrity.py`) enforces the cutover.

### Step 5b: Scene Authoring Against Real Pixels (Phase 2)
- **Runs in a separate session, after gate 1R clears.**
- **Input:**
  - Approved reference IMAGES in `episode-{XX}/04_visuals/raw/`
  - Frozen `ep{XX}_visual_prompts_v01.md` (references + LOCKS + coverage map)
  - Approved `ep{XX}_dramaturgy_v{VV}.md`
- **Tool:** Claude executes `_skills/robotiko-visual-prompts/SKILL.md` (Phase 2)
- **Output:** `episode-{XX}/04_visuals/ep{XX}_visual_prompts_v02.md` — the complete Phase-1+2 document: references carried forward (Environment Geometry notes rewritten to the approved pixels) + all scene prompts framed to real pixels + per-space Camera Ledger. **Sentinel removed.**
- **Method:**
  - **Opening move = batch verification pass.** Read every approved ref PNG, walk ALL scenes against the pixels + coverage map, and collect every gap (missing space, missing character ref, decomposition split) into ONE loop-back batch before writing a single prompt. No forty-scenes-deep surprises.
  - Every scene is born framed to a reference that already exists — the "frame to an image that does not exist yet" problem is gone.
- **Rules:**
  - Every prompt MUST bind its character/environment reference inline and MUST end with the mandatory visual suffix (no exceptions)
  - Compose with "Headroom" and "Breath" for camera movement space
  - **Skill:** `_skills/robotiko-visual-prompts/SKILL.md`

### Production Rule: B-Residue Backstop (Late Reference Edits)
> **If any environment reference is edited AFTER Phase 2 has begun, every scene mapped to that reference's space in the scene→space coverage map MUST be re-verified against the new pixels before delivery.**

This is the structural fix for the exact failure that motivated the two-phase redesign: a REF block was reframed (REF B, commit `a98acbc`) and the 40 dependent scenes were never re-checked against it. The scene→space coverage map (Step 5a) is the "which scenes" index — it names precisely which scenes a given ref edit invalidates. This rule is **human-gated**: confirming that new pixels still satisfy each scene's intent is semantic, not machine-lintable; CI can only surface the v01 sha-drift WARN as a partial signal. Also lives in `_skills/robotiko-visual-prompts/SKILL.md` (section 2.8).

### Step 6: Image Generation
- **Tool:** Nano Banana (using scene prompts from Step 5b)
- **Output:** `episode-{XX}/04_visuals/raw/ep{XX}_s{XX}_v{XX}.png`

### Step 7: Image Selection
- **Tool:** Human curates best outputs
- **Output:** `episode-{XX}/04_visuals/selected/ep{XX}_s{XX}_selected.png`

### Production Telemetry: Attempts Ledger

During image generation (Step 6), log every generated scene asset in
`episode-{XX}/04_visuals/raw/attempts.md` — **filled DURING generation, not
reconstructed afterward** (reconstruction would be fabricated telemetry, exactly
what this ledger exists to prevent). One row per scene:

| scene_id | attempts | first_pass (y/n) | fail_reason (one phrase) |
|---|---|---|---|
| s01 | 1 | y | — |
| s27 | 9 | n | no kintsugi reference (see ADR-0007) |

- **attempts** = how many generations it took to land a keeper for that scene.
- **first_pass** = did the very first generation land the keeper (y) or not (n).
- **fail_reason** = one short phrase when first_pass is n; leave `—` when y.
- **Mandatory from EP10 onward** — the last unproduced episode, and therefore the
  only remaining window to measure first-pass yield for real. EP01-EP09 were
  generated before this convention and get no retroactive ledger.
- This is the first *instrumented* data behind the "65-70% image first-pass / ~80%
  video first-pass" figures, which until now are experiential estimates from the
  director's production notes. See
  `_management/adr/0007-reference-first-or-pay-the-reshoot-tax.md` (Note on empirical
  claims) — after EP10 that claim gets its first measured data point.
- `attempts.md` lives inside `raw/` (a naming-check skip folder) and is summarized by
  the standalone reporter `tests/attempts_report.py`, which is NOT part of the CI gate.

---

## PHASE 4: MOTION PRODUCTION

### Step 8: Motion Script Generation
- **Input:**
  - Selected images from `04_visuals/selected/`
  - Approved `ep{XX}_dramaturgy_v{VV}.md`
  - `ep{XX}_musical_metadata.json` (for beat sync)
- **Tool:** Claude executes `_skills/robotiko-motion-script/SKILL.md` (v2.0)
- **Output:** `episode-{XX}/05_video/ep{XX}_motion_script_v01.md`
  - Output includes: **Tool Assignment Summary**, **Element Registry**, **Camera Diversity Report**, **Frame Chain Map**, per-clip `| Recommended Tool |`, `| Generation Mode |`, `| Element Tags |` fields
- **EP07+ additions:** Kling 3.0 Elements (character consistency via @Name tags), Frame Chaining (last-frame → start-frame continuity), OmniEdit budget reserve (10-15% of Kling credits)
- **Beat sync terminology note:** "Beat sync" in this pipeline means section-level and phrase-level synchronization — aligning camera cuts, motion intensity, and visual transitions to musical section boundaries and phrase transitions. It does NOT mean frame-accurate beat-grid quantization (BPM-locked cuts on every downbeat). The musical metadata JSON provides section timestamps, not individual beat positions.
- **⛔ MANDATORY CHECKPOINT:** Human reviews camera moves, tech strategy, tool assignments, camera diversity, and Element assignments before video generation.

### Step 8b: Supplementary Image Generation (If Required)
- **Trigger:** Motion script flags sub-clips with `⚠️ NEW IMAGE REQUIRED`
- **Input:** Inline supplementary visual prompts from the motion script
- **Tool:** Nano Banana (same as Step 6)
- **Output:** Additional images in `04_visuals/selected/` with sub-clip naming (e.g., `ep{XX}_s{XX}c_selected.png`)
- **Note:** This step only runs if the motion script identifies scenes where existing images cannot cover the full duration. The motion script contains ready-to-use visual prompts for these supplementary images.

### Step 8c: Tool Assignment (Built into Motion Script)
- **Purpose:** The motion script includes per-clip tool recommendations based on current tool capabilities and credit budgets.
- **Input:** Tool capabilities from `_management/project_metadata.json` (resolution, keyframe support, duration, cost)
- **Assignment Logic:** Mode B → highest-quality keyframe tool (Kling or Seedance 1.0). Map/texture → Seedance 1.0 (budget-efficient). Fixed-duration match → natural fit. Character close-ups → highest resolution.
- **Output:** `| Recommended Tool |` field in every clip + Tool Assignment Summary section in the motion script
- **Note:** Tool assignments are recommendations. The human makes the final decision during video generation. Credit budgets and tool availability may change between sessions.

### Step 9: Video Generation
- **Tool:** Per clip's `| Recommended Tool |` from the approved motion script. Tools include Kling, Veo, Seedance 1.0 (or others as added to toolchain).
- **Strategy Options:**
  - **Mode A — Standard (5s or 10s):** Atmospheric/simple movement. Input: 1 image. Duration depends on tool capability.
  - **Mode B — Start/End Keyframes (5s or 10s):** Transformations, morphing, complex travel. Input: 2 images.
- **Output:** `episode-{XX}/05_video/raw/ep{XX}_s{XX}_video_{tool}.mp4` (or `ep{XX}_s{XX}{a|b|c|d}_video_{tool}.mp4` for sub-clips)

### Duration Coverage Strategy (Step 8 Rule)

Video generation tools produce fixed-duration clips (5s or 10s). Music sections have arbitrary duration (5s–36s+). The motion script must ensure **full duration coverage** — every second of music must have corresponding video content.

| Scene Duration | Strategy | Clip Count | Notes |
|---|---|---|---|
| ≤ 5s | **Direct** | 1 × 5s | Trim excess in CapCut |
| 6–10s | **Direct** | 1 × 10s | Trim in CapCut. If tool is 5s-only: 1 × 5s + speed ramp |
| 11–15s | **Speed Ramp** | 1 × 10s + slow-mo (max 1.5×) | If tool is 5s-only: 2 × 5s |
| 16–30s | **Multi-Clip** | ⌈duration / 10⌉ × 10s clips | Each sub-clip gets own camera move + motion prompt |
| 30s+ | **Multi-Clip** | ⌈duration / 10⌉ × 10s clips | May need supplementary images (Step 8b) |

**Sub-clip naming:** `s{XX}a`, `s{XX}b`, `s{XX}c`, `s{XX}d` — consistent with existing keyframe pair naming.

**Speed ramp limit:** Maximum 1.5× slowdown (e.g., 10s clip → 15s at most). Beyond 1.5× looks unnatural.

**Coverage target:** ≥ 95% of total music duration covered by generated clip time (before speed ramp adjustments)

### Step 10: Video Selection
- **Tool:** Human curates final clips
- **Output:** `episode-{XX}/05_video/selected/ep{XX}_s{XX}_selected.mp4`

---

## PHASE 5: POST-PRODUCTION

### Step 11: Editing + Post-Production Unification
- **Tool:** CapCut Pro
- **Skill:** Claude executes `_skills/robotiko-capcut-editor/SKILL.md` to generate episode-specific edit guide
- **Input:** Selected video clips + Final audio + Approved motion script
- **Output:**
  - Edit guide: `episode-{XX}/06_edit/ep{XX}_capcut_guide_v{VV}.md`
  - Final video: `episode-{XX}/06_edit/ep{XX}_final_v{VV}.mp4`
  - Sync-QC record: `episode-{XX}/06_edit/ep{XX}_sync_qc_v01.md`

#### CapCut Post-Production Protocol

Apply these to ALL clips before editing, to unify output from multiple AI tools (Kling, Veo, Seedance 1.0):

1. **Film Grain:** 10-15% overlay on every clip. Breaks AI smoothness, creates organic analog texture.
2. **Color Match:** Select the best reference clip (best Kodachrome warmth) → match all other clips to it using CapCut's Match Color feature.
3. **Letterbox 2.35:1:** Add cinematic black bars (top + bottom). Hides edge artifacts, reinforces cinematic format.
4. **Kodachrome LUT:** If available, apply a warm Kodachrome color grading preset for unified look across all clips.

#### QA Checklist
  - [ ] Film grain applied to all clips (10-15%)
  - [ ] Color matched across all clips (single reference)
  - [ ] Letterbox 2.35:1 applied
  - [ ] Beat sync verified
  - [ ] Color consistency (Kodachrome warmth preserved)
  - [ ] 1080p export confirmed (project standard — source material is AI-generated at 1080p max)
  - [ ] No clean/sterile aesthetics — analog decay preserved

#### Sync-QC Record (Mandatory Evidence)

The "Beat sync verified" checkbox above is a claim until it is measured. Every
episode's edit produces a committed sync-QC record from the template:

- **Output:** `episode-{XX}/06_edit/ep{XX}_sync_qc_v01.md`, copied from
  `_templates/ep_sync_qc_template.md` and filled by the human once the render exists.
- **Minimum 5 timestamped spot-checks**, sourced from the motion script's Beat Sync
  Notes table. Each spot-check compares the target timestamp to the actual cut
  timestamp and returns a verdict: ON-BEAT (|delta| <= 150 ms), OFF by N ms, or
  ACCEPTED-DEVIATION (deliberate artistic offset, one-line reason). Artistic
  deviations are legitimate; hiding them is not.
- **Why it lives here and not in CI:** the final render is gitignored (Drive /
  portable disk), so CI can validate the score but never the mix. This record is the
  evidence CI cannot produce. `scripts/sync_probe.py` is an optional LOCAL helper
  that prints measured cut-vs-boundary numbers for the table — it is not part of the
  CI gate.
- **Scope:**
  - **EP01-EP07 — legacy (pre-QC-convention).** No retroactive obligation.
  - **EP08 — optional retro record** when the render is at hand.
  - **EP09 onward — mandatory.** The edit is not "done" without the record.

---

## PHASE 6: DISTRIBUTION (Post-Completion)

### Step 12: YouTube Packaging
- **Tool:** Claude executes `_skills/robotiko-youtube-packager/SKILL.md`
- **Output:** Title, description, thumbnail guidance, cross-links

### Step 12.5: YouTube Metadata Review
- **Reference:** `_management/youtube_metadata_standards.md`
- **Verify before upload:**
  - [ ] Title follows `[Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series` format (max 80 chars)
  - [ ] Description first 3 lines = hook + series descriptor + series entry point
  - [ ] Category: Film & Animation
  - [ ] Cross-links: previous + next episode + playlist in description
  - [ ] Pinned comment matches youtube_metadata_standards.md (Section 9) exactly

### Step 13: Social Media Atomization
- **Tool:** Claude executes `_skills/robotiko-reels-atomizer/SKILL.md`
- **Output:** Platform-specific clips under `episode-{XX}/07_social_media/`

---

## SKILLS SYSTEM

All Claude workflows are defined in `_skills/`. Each skill is a `SKILL.md` file.
Claude reads the relevant SKILL.md before executing any workflow.

| Skill | Trigger Phrase | Output |
|---|---|---|
| `robotiko-musical-metadata` | "Create musical metadata for EP{XX}" | `ep{XX}_musical_metadata.json` |
| `robotiko-dramaturgy` | "Create dramaturgy for EP{XX}" | `ep{XX}_dramaturgy_v01.md` |
| `robotiko-visual-prompts` | "Generate visual prompts for EP{XX}" | `ep{XX}_visual_prompts_v01.md` (Phase 1: refs) → `_v02.md` (Phase 2: scenes) |
| `robotiko-motion-script` | "Generate motion script for EP{XX}" | `ep{XX}_motion_script_v01.md` |
| `robotiko-episode-scaffold` | "Scaffold EP{XX}" | Full folder structure |
| `robotiko-naming-enforcer` | "Validate file names" | Compliance report |
| `robotiko-youtube-packager` | "Package EP{XX} for YouTube" | `ep{XX}_youtube_package.md` (per youtube_metadata_standards.md) |
| `robotiko-reels-atomizer` | "Atomize EP{XX} for social" | Clip list |
| `robotiko-launch-orchestrator` | "Orchestrate EP{XX} launch" | Launch checklist |
| `robotiko-capcut-editor` | "Edit EP{XX} in CapCut" | `ep{XX}_capcut_guide_v01.md` |

---

## PIPELINE SUMMARY (Quick Reference)

```
SCAFFOLD → LYRICS → MUSIC → METADATA JSON → CONCEPT NOTES
    → DRAMATURGY [✋ CHECKPOINT] → REF AUTHORING / Phase 1 [✋ REFERENCE GATE 1R]
    → SCENE AUTHORING / Phase 2 → IMAGE GEN → IMAGE SELECT
    → MOTION SCRIPT [✋ CHECKPOINT] → VIDEO GEN → VIDEO SELECT
    → CAPCUT GUIDE → EDIT → YOUTUBE + METADATA REVIEW + SOCIAL

Three human checkpoints: ✋ Dramaturgy (gate 1) · ✋ Reference Gate (gate 1R, EP10 onward) · ✋ Motion Script (gate 2).
```

---

## SHIPPED FILE POLICY

Shipped episode files (episodes launched on YouTube) are not retroactively edited for cosmetic changes. However, **canon terminology corrections** (e.g., station name standardization) ARE applied retroactively to maintain a single source of truth. The pipeline enforces current rules on all files.