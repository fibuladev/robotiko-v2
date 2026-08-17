# VISUAL PROMPT TEMPLATE (NANO BANANA) — Two-Phase
> **Version:** 2.0 (two-phase) | Skill: `_skills/robotiko-visual-prompts/SKILL.md`
> This template is auto-populated by Claude. Do not fill manually.
> One template, both phases, gate divider + sentinel pre-placed — isomorphic to the SKILL.

---

## HOW TO USE THIS TEMPLATE (read once)

The visual-prompts stage is **two phases separated by a hard human gate** (docs/two-phase-visual-prompts.md):

```
PREREQUISITE (dramaturgy approved)
    -> PHASE 1 — REFERENCE AUTHORING (v01: refs + locks + coverage map + sentinel; ZERO scenes)
    -> HARD STOP: REFERENCE GATE (gate 1R — human generates + approves the ref images)
    -> PHASE 2 — SCENE AUTHORING AGAINST REAL PIXELS (v02: scenes framed to approved pixels)
```

- **`ep{XX}_visual_prompts_v01.md` = the complete PHASE-1 deliverable.** Everything from the top of
  this template down to and including the Phase-1 sentinel. Zero scene prompts by design.
- **`ep{XX}_visual_prompts_v02.md` = the complete PHASE-1+2 document.** The v01 reference blocks
  carried forward (Environment Geometry notes rewritten to the approved pixels), plus the Camera
  Ledger and all scene prompts. **The sentinel is removed in v02.**

Fill every `[bracketed placeholder]`. Delete the instructional `> notes` in your finished document.

---

## PRE-GENERATION CHECKLIST (Claude reads these before writing a single prompt)

- [ ] `_management/master.md` — Visual DNA (Sec. 3), color palette, forbidden list, mandatory suffix
- [ ] `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` — APPROVED scene breakdown (its **location
      labels** are the ceiling for decomposition and the source of truth for the completeness check)
- [ ] `_assets/cast/character_profiles.json` — `visual_prompt_addition` for this phase,
      `reference_images` + `phase_reference_map` for the correct body-state ref, eye-canon logic
- [ ] Phase-correct Robotiko reference (via `phase_reference_map`; check `episode_overrides` for EP08/EP09)
- [ ] `_assets/cast/ref_mentor_master.png` — only if the Mentor appears (EP01-07)
- [ ] `_assets/style/visual_dna.md` — the look contract + reference-image-first doctrine

> WARNING: Dramaturgy must be human-APPROVED before this file is generated. If not approved, STOP.

---

## EPISODE HEADER

| Field | Value |
|---|---|
| **Episode** | EP{XX} |
| **Title** | [Episode Title, from dramaturgy] |
| **Station** | [The X Self] |
| **Character Phase** | [Phase 1 / 2 / 3] |
| **Robotiko Visual State** | [Exact `visual_prompt_addition` from character_profiles.json] |
| **Camera Personality** | [Episode camera character, from the ART DIRECTION LOCKS] |
| **Reference (body)** | [Phase-correct ref file, e.g. `_assets/cast/android_kintsugi.png`] |
| **Total Scenes** | [N scenes from the approved dramaturgy] |
| **Total Prompts** | [scene prompts + reference prompts; scene count must match the dramaturgy] |

> **Version note.** v01 = Phase-1 deliverable (this header down to the sentinel; zero scenes).
> v02 = Phase-1+2 document (refs carried forward + Camera Ledger + all scenes; sentinel removed).

---

## MANDATORY STYLE SUFFIX
> This suffix is appended verbatim to the end of EVERY prompt — reference AND scene. No exceptions.

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## FORBIDDEN AESTHETICS REMINDER
- Clean, sterile, or Apple-style design
- Pixar / cartoon / anime rendering
- Generic cyberpunk neon glow
- Smooth plastic textures
- Modern UI elements (unless satirically intended and noted in dramaturgy)
- Cheap melodrama or ornamental excess

---

# ============================================================
# PHASE 1 — REFERENCE AUTHORING  (delivered as v01)
# ============================================================

> Phase 1 authors every reference PROMPT, locks the cross-scene art direction, and publishes the
> coverage map. It contains ZERO scene prompts. The gate is only as good as what sits at it — so
> everything the director needs to validate ref coverage against the story lives in this document.

---

## ART DIRECTION LOCKS (mandatory Phase-1 section)
> The cross-scene working memory Phase 2 resumes from — the shared brain that keeps every scene
> coherent. Fill each lock; delete none of the headings.

- **Color-journey scene-bands:** [which scene ranges sit in which color state, as one continuous arc
  — e.g. "his gold distinct in pre-dawn grey (S01-S03) -> grass-gold and seam-gold converge (S13-S18)
  -> one warmth by the meadow (S30+)"]
- **Per-episode budgets:** [scarce effects with a hard count and where spent — e.g. "the single Amber
  Pulse, S10 only; embers are orange-red, never amber". Name the budget and the exact scene.]
- **Camera personality + gaze discipline:** [the episode's camera character (e.g. THE COMPANION
  CAMERA — alongside never above, beside-space kept open) AND the gaze rules (e.g. the only direct
  look into the lens is S34a; elsewhere the gaze stays below/beside the lens)]
- **Body-state locks:** [what the body does and does NOT do this episode — e.g. "full kintsugi from
  frame one, stable, no transformation beats; the mouthless-face guard"]
- **What is NOT shown:** [explicit exclusion list — e.g. "no monument framing of the infinity stone,
  no Mentor embodied, no screen-world, no invented mouth"]

---

## CHARACTER / GROUP REFERENCES (enumerate every NEW reference)
> Reference-first is not just environments (ADR-0007's original scar was a CHARACTER ref — the
> kintsugi body). List EVERY new body-state and group ref the episode needs; each is gated at 1R
> alongside the environments; loop-back in Phase 2 covers a missing character ref exactly as a space.

- **Body-state references:** [any Robotiko phase/state not already on disk. Look up `reference_images`
  + `phase_reference_map`. If the path is null/missing, it is a Phase-1 deliverable — author a REF
  block for it below. Shared cast refs already on disk (e.g. `_assets/cast/android_kintsugi.png`)
  are named, not re-authored.]
- **Group references:** [every episode-specific group that RECURS or REACTS needs a neutral-composition
  ref so it stays the same group. A one-off anonymous ensemble that never recurs and never reacts does
  NOT — note that honestly here (as EP10 did for its Dawn Workers: "no dedicated ref required").]
- **Mentor:** [`_assets/cast/ref_mentor_master.png` — EP01-07 only. After EP07 only his objects (the
  staff) may appear.]

> New character/group refs are authored with the SAME REF block schema below. Their Text Prompts
> contain a character, so the validator pseudo-scene-lints them (eye-canon / phase keywords) — write
> them to the eye-canon idiom and the correct phase.

---

## ENVIRONMENT REFERENCE BLOCKS
> One REF block per distinct camera-space from the decomposition (SKILL 1.1: the site-map +
> landmark-consistency test, NOT the old "3+ scenes" heuristic; alarm band ~1 ref per 3 scenes;
> spaces under ~2 scenes extend a neighbor ref or chain via Rule 4c). Sibling refs of ONE dramaturgy
> location must declare shared through-anchors (SKILL 1.2) and pass "no cross-ref typology clash
> (roofs, materials, horizon)". The block is the reference's whole contract.

### REF {letter}: {Name} ({scene span, e.g. S03-S08, S11-S12})

- **Design Brief:** [What the space IS and what it must never become — its identity, its mood, its
  hard "NOT" clauses (no monument framing, no light from within the stone, no invented mouth). Prose.]
- **Environment Geometry:** [*Phase 1 — the generation spec.* A DECISION, not a discovery: the
  canonical camera position, the perspective direction, and where the key landmarks sit ("eye-level;
  the two stone loops lie across the mid-ground, near loop toward camera; monolith mountains in the
  background; low horizon, big warm sky"). This is what the ref image is generated to hit.]
  > POST-APPROVAL (start of Phase 2) this field is MANDATORY-rewritten in place to describe the
  > ACTUAL approved pixels, in the "Framing Pass note" format (see the example under the gate below).
  > A scene frames to THIS rewritten note — the real image — never to the stale generation spec.
- **Narrative anchors:** [The story obligations the space must preserve, carried from the dramaturgy
  — the content that must NOT be demoted away when the geometry is rewritten. Examples that live in
  the dramaturgy: *the beside-space stays open (his right side)*; *the street runs toward the town =
  the direction of desire*; *reserved sky room for a walking figure and a crossing flock without
  touching the celestial bodies*. Geometry says where the camera sits; narrative anchors say what the
  frame owes the story.]
- **Reference Image Path:** `episode-{XX}/04_visuals/raw/ep{XX}_ref_{name}.png`
  > Canonical form. Environment refs and per-episode body/group refs both follow it; shared cast refs
  > (e.g. `android_kintsugi.png`) live in `_assets/cast/`. The `raw/` segment is canonical.
- **Through-anchors (sibling refs of one location only):** [shared palette journey; single
  light-direction / time contract; >=1 co-visible landmark (e.g. the distant monolith silhouettes).
  Omit this line for a standalone location with no siblings.]

**Text Prompt:**
> [Wide establishing shot, no characters, full spatial detail, the geometry named above, plain ASCII
> only (no em-dash)]. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### REF {letter}: {Name} ({scene span})

- **Design Brief:** [...]
- **Environment Geometry:** [generation spec; rewritten to real pixels post-approval]
- **Narrative anchors:** [...]
- **Reference Image Path:** `episode-{XX}/04_visuals/raw/ep{XX}_ref_{name}.png`
- **Through-anchors (if a sibling of the REF above):** [...]

**Text Prompt:**
> [...]. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

*(Repeat one REF block per camera-space and per new character/group reference.)*

---

## SCENE-TO-SPACE COVERAGE MAP (mandatory, delivered AT the gate)
> The artifact that converts the gate from a false "done" sticker into a real one. Authored BEFORE any
> image is generated, so the director validates ref coverage against the whole story on cheap text.
> **Every dramaturgy scene appears exactly once.** Ref-less scenes (macro, fourth-wall close-ups,
> tracks-only) are listed with `ref-less` in the camera-space column — never omitted; they carry the
> emotional payload and must be visible at the gate. This map also names which scenes to re-verify if
> a reference is ever edited late (the GAP-B backstop; input to the Phase-2 backstop rule).

| scene-id | camera-space | one-line narrative role |
|---|---|---|
| S01 | [REF letter / ref name, or `ref-less`] | [what the scene does in the story, one line] |
| S02a | [...] | [...] |
| S02b | [...] | [...] |
| ... | ... | ... |

---

## HARD STOP: REFERENCE GATE (Gate 1R)
> **Mandatory human checkpoint. Phase 2 does not begin until it clears. Never skip it.**

Deliver the complete `ep{XX}_visual_prompts_v01.md` (references + locks + coverage map + sentinel) and
hand off with this message:

1. **Generate the reference images** listed above into `episode-{XX}/04_visuals/raw/` as
   `ep{XX}_ref_{name}.png` (environments, body states, groups).
2. **Iterate freely.** Regenerate, reframe, edit — this is the cheap place to get the world right
   (a roof clash, a drifted castle, a glowing amber tip get caught here, on the pixels).
3. **Approve.** When every reference image is right, the human approves the reference SET.
4. **On approval, gate 1R is recorded as data** — an entry in `_management/approvals.json`
   (`gate: "1R"`, `artifact:` the v01 path, `sha256`, `date`, `note`), sha-pinned to the frozen v01
   bytes. From this point v01 is frozen; a later edit fires the existing sha-drift WARN (the honest
   late-ref-edit signal). `project_metadata.json` `production.visuals` moves to `"refs_approved"`.

**Honest limit.** 1R records that a human approved the reference PROMPTS and signed off the reference
IMAGES they generated. The images live in gitignored `raw/` and are not machine-verifiable — the gate
is preventive at the SKILL layer, detective at CI. Same posture as gates 1 and 2.

**Optional escape valve.** Only if the director asks it to judge a contested reference: ONE throwaway,
explicitly non-binding exemplar scene prompt per contested ref. Rewritten from scratch in Phase 2.
Cap it hard — never a back door into writing the scene set early.

### The Phase-1 sentinel — closes the v01 document

The block below is already placed live, where the scene section will later be written. It tells the
validator this is an intentional Phase-1 file (partial pass), not a refs-only false green. Carry it
**verbatim** into v01 — do not paraphrase or re-case it. It is REMOVED in v02.

## SCENES — PENDING (PHASE 2)

> STATUS: this is a valid, designed Phase 1 deliverable, not an unfinished draft.
> Reference prompts above are authored and human-approved; scene prompts are intentionally
> not written yet. They are authored in Phase 2, framed against the REAL reference images
> once a human has generated and approved them. Why: docs/two-phase-visual-prompts.md
>
> SCENES_STATUS: PENDING_PHASE_2

> v01 ENDS HERE. Everything below is authored in Phase 2 (v02), after gate 1R clears.

---

# ============================================================
# PHASE 2 — SCENE AUTHORING AGAINST REAL PIXELS  (delivered as v02)
# ============================================================

> Runs in a SEPARATE session after gate 1R. Inputs: the approved ref PNGs in `raw/`, the frozen v01,
> the approved dramaturgy. Opening move = batch verification pass (SKILL 2.1): read every approved
> ref PNG, walk ALL scenes against the pixels + coverage map, collect every gap into ONE loop-back
> batch BEFORE writing any prompt. Rewrite each REF block's Environment Geometry note to the approved
> pixels. Re-read the dramaturgy + ART DIRECTION LOCKS first (SKILL 2.2). In v02: carry the reference
> blocks forward (with rewritten geometry notes) and REMOVE the sentinel.

---

## PER-SPACE CAMERA LEDGER
> One row per scene per space (SKILL 2.4). Makes cross-scene geography contradictions visible on one
> screen: if two scenes in the same space put the same landmark on opposite screen-sides for no story
> reason, the ledger shows it. Also where you confirm the Camera Diversity rule — same space,
> deliberately different, spatially coherent viewpoints, never the ref's exact angle cloned.

| space | ref | scene | camera position & heading | landmark screen-side |
|---|---|---|---|---|
| [market edge] | [`ep{XX}_ref_market.png`] | [S11] | [eye-level, facing the vendors, road receding right] | [oven back-left] |
| [market edge] | [`ep{XX}_ref_market.png`] | [S12] | [tracking-height among the crowd, facing down-lane] | [oven back-left] |
| ... | ... | ... | ... | ... |

---

## GENERATED SCENE PROMPTS (grouped by musical section)
> Prompts grouped under section headers matching the dramaturgy's musical structure. One scene = one
> self-contained prompt (Rule 1). Bind each reference inline `element (filename.png)` (Rule 2b);
> use the short character identifier and do NOT restate what the reference already shows (Rule 3).

### SECTION: [Section Name from Dramaturgy — e.g. "INTRO & AWAKENING (0:00 - 0:42)"]

---

#### Scene S{XX} — [Scene Title]
- **Timestamp:** [MM:SS]
- **Dramaturgy Reference:** [CITED pointer to the dramaturgy Shot ID — not a fresh paraphrase written
  from the image (SKILL 2.2). e.g. "Shot S12 (dramaturgy: 'Among Them') — walks through the market at
  their pace, unremarkable and belonging."]
- **Characters Present:** [List with phase-appropriate visual state noted]
- **Image Reference Path:** [Phase-correct ref from `phase_reference_map`, or N/A for no characters]
- **Video Tech Strategy:** [Standard / Start-End Keyframes — from dramaturgy detail blocks]
- **Composition Notes:** [Headroom, breathing space, depth; AND name the ART DIRECTION LOCKS rules that
  bind this scene where they apply (SKILL 2.2) — gaze discipline, beside-space, active color band,
  spent/unspent budget, mouthless-face guard. Frame the angle to the ref geometry (Rule 4b); vary
  within the space, never clone the ref's exact angle.]
- **Upload:** [Per-scene ref images matching the inline bindings: char ref + env ref + `chain: S{XX}
  output` or `base: {frame}` + special ref]

**Text Prompt:**
> [Full self-contained scene description, angle framed to the environment reference, character bound
> inline `the chrome android (android_kintsugi.png)`, eye-canon idiom for any lens, anti-spawn guard
> only if needed, plain ASCII only (no em-dash)]. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

#### Scene S{XX} — [Scene Title]  *(ref-less example — macro / fourth-wall / tracks-only)*
- **Timestamp:** [MM:SS]
- **Dramaturgy Reference:** [Cited Shot-ID pointer]
- **Characters Present:** [e.g. None (macro), or Robotiko (fourth-wall close)]
- **Image Reference Path:** [N/A (macro) or the phase-correct char ref for a close-up]
- **Video Tech Strategy:** [Standard / match-cut / ...]
- **Composition Notes:** [REF-LESS SCENE (SKILL 2.3): cannot be framed to pixels — signed off against
  its dramaturgy GRAMMAR obligations by name (the gaze rule, the beside-space, the match-cut angle
  contract, the mouthless guard, the budget). List the grammar check here so the completeness approver
  can see it.]
- **Upload:** [- (macro, no ref) or char ref for a close-up]

**Text Prompt:**
> [Self-contained macro / close-up description, plain ASCII only (no em-dash)]. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

---

### SECTION: [Next Section Name]

*(Continue the pattern for every scene in the approved dramaturgy. Total scene-prompt count must match
the dramaturgy scene count; Start/End scenes get two prompts, S{XX}a / S{XX}b.)*

---

## QUALITY CHECKLIST (Claude self-validates before delivery — covers BOTH phases)
> Phase 1 (v01): items 1-9 apply to the reference document. Phase 2 (v02): all 13 apply.

- [ ] **1. Mandatory suffix present** — every prompt (reference AND scene) ends with the exact style
      suffix; no modification, no omission.
- [ ] **2. 16:9** — every Text Prompt carries `16:9 widescreen composition`.
- [ ] **3. ASCII / no em-dash (ADR-0006)** — every Text Prompt blockquote is plain-English ASCII; no
      em-dash, no non-ASCII punctuation inside a prompt.
- [ ] **4. Reference-first (ADR-0007)** — every new reference (environment AND body-state AND group)
      authored and gated before any scene is written; scenes frame to refs that already exist.
- [ ] **5. Decomposition test applied** — the site-map + landmark-consistency test (SKILL 1.1), not
      the old "3+ scenes" heuristic; alarm band (~1 ref/3 scenes) checked; <2-scene spaces extended or
      chained (Rule 4c).
- [ ] **6. Through-anchors declared** — sibling refs of one location share a palette journey, a single
      light-direction/time contract, and >=1 co-visible landmark; "no cross-ref typology clash (roofs,
      materials, horizon)" (SKILL 1.2).
- [ ] **7. Narrative anchors present** — each REF block records the story obligations the space must
      preserve (beside-space, direction of desire, reserved sky room), not just geometry (SKILL 1.4).
- [ ] **8. Coverage map complete** — every dramaturgy scene mapped exactly once; ref-less scenes
      listed as `ref-less`, never omitted (SKILL 1.6).
- [ ] **9. Sentinel state correct** — the Phase-1 sentinel block is PRESENT and verbatim in v01;
      ABSENT from v02 (a v02 with the sentinel is a stale-sentinel FAIL) (SKILL 1.7 / 2.7).
- [ ] **10. Camera ledger consistent** — present in v02, one row per scene per space; no unexplained
      landmark screen-side flips; angles vary within each space (SKILL 2.4).
- [ ] **11. Ref-less scenes signed off** — each checked against its dramaturgy grammar obligations by
      name, against the story not an image (SKILL 2.3).
- [ ] **12. Character phase correct** — every Robotiko scene references the phase-correct ref from
      `phase_reference_map`; visual state matches the episode phase; no pristine after EP01.
- [ ] **13. Eye-canon idiom (ADR-0010)** — material-lens idiom only ("calm steady blue optical lenses
      set into chrome sockets, like polished sapphires"); never "glow" within reach of an eye/lens
      word (kintsugi body gold-glow is allowlisted; eyes never).
- [ ] Ask yourself: **"Would Fibula approve this?"**
