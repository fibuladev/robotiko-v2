# SKILL: robotiko-visual-prompts
> **Version:** 2.0
> **Trigger:** `"Generate visual prompts for EP{XX}"`
> **Output (Phase 1):** `episode-{XX}/04_visuals/ep{XX}_visual_prompts_v01.md` — complete Phase-1 document (references + locks + coverage map + sentinel; zero scenes)
> **Output (Phase 2):** `episode-{XX}/04_visuals/ep{XX}_visual_prompts_v02.md` — complete Phase-1+2 document (references carried forward + scenes framed to real pixels; sentinel removed)

---

## PURPOSE

Convert an approved dramaturgy document into standalone image generation prompts for Nano Banana — in **two phases separated by a hard human gate.**

- **Phase 1 — Reference Authoring.** Decompose the episode's locations, enumerate every new reference (environments, body states, groups), author the reference PROMPTS, lock the cross-scene art direction, and publish a scene→space coverage map. The human then generates and approves the reference IMAGES. **No scene prompt is written yet.**
- **Phase 2 — Scene Authoring Against Real Pixels.** With the approved reference images in hand, verify every scene against the actual pixels, then write each scene prompt framed to the reference that already exists.

Each scene prompt is a single, self-contained text prompt an image model can execute without any additional context. It must encode the full visual intent: scene composition, character state, lighting, texture, and the mandatory style suffix.

---

## THE TWO-PHASE ARCHITECTURE (Read This First)

The old skill wrote reference prompts and ALL scene prompts in one pass, against a text contract, and generated the reference images afterward. A "Framing Pass" was supposed to reconcile scenes to the real pixels — but it was explicitly "never a blocker," so in practice it was skipped (see the REF B reframe, 2026-07-07 / commit `60cabd2`: the REF block was updated, and 40 scenes were never re-checked against it). Reference-first was a principle (ADR-0007) that nothing structurally enforced.

The two-phase split makes reference-first structural:

```
PREREQUISITE (dramaturgy approved)
    → PHASE 1 — REFERENCE AUTHORING (v01: refs + locks + coverage map + sentinel)
    → ⛔ HARD STOP: REFERENCE GATE (gate 1R — human generates + approves the ref images)
    → PHASE 2 — SCENE AUTHORING AGAINST REAL PIXELS (v02: scenes framed to approved pixels)
```

**The honest cost.** This flow costs **+1 formalized session** versus the old single pass. That +1 is not new overhead — it is the Framing Pass debt finally being paid on the table instead of skipped. In exchange it buys back the ADR-0007 reshoot tax: EP09 paid 8-10x regenerations on scenes conjured from text against the wrong reference. One deliberate gate is cheaper than a hundred reshoots. Spend the session.

---

## PREREQUISITE

> **The dramaturgy for this episode MUST be human-approved before this skill executes.**
> If the dramaturgy has not been approved, STOP. Do not generate references or scene breakdowns from unapproved dramaturgy.

---

## MANDATORY INPUTS (Read Before Writing a Single Prompt)

Read these files in this exact order:

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/master.md` | Visual DNA (Section 3), color palette, forbidden aesthetics, mandatory suffix |
| 2 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Approved scene breakdown — this is your primary input; its **location labels** are the ceiling for decomposition (Phase 1) and the source of truth for the completeness check (Phase 2) |
| 3 | `_assets/cast/character_profiles.json` | Character `visual_prompt_addition` for this episode's phase, `reference_images` + `phase_reference_map` for the correct ref file, eye color logic |
| 4 | Phase-correct Robotiko reference | Look up `phase_reference_map` in character_profiles.json → determines which ref file to use (pristine, damaged, or kintsugi). For episodes with `episode_overrides` (EP08, EP09), check scene ranges. |
| 5 | `_assets/cast/ref_mentor_master.png` | Visual reference image (if Mentor appears; EP01-07 only) |
| 6 | `_templates/visual_prompt_template.md` | Output structure and formatting template (both phases; gate divider + sentinel pre-placed) |

**If the approved dramaturgy file is missing:** STOP. The pipeline requires human-approved dramaturgy before visual prompts can be generated.

---

## THE MANDATORY VISUAL SUFFIX

This exact string is appended to the end of every single prompt — reference prompts AND scene prompts. No exceptions. No modifications. No omissions.

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

# PHASE 1 — REFERENCE AUTHORING

Phase 1 produces `ep{XX}_visual_prompts_v01.md`: a **complete, designed Phase-1 deliverable** — not a half-written draft. It contains every reference prompt, the ART DIRECTION LOCKS, the scene→space coverage map, and the Phase-1 sentinel. It contains **zero scene prompts** by design. The gate is only as good as what sits at it, so everything the director needs to validate ref coverage against the story lives in this document.

---

## 1.1 — Location Decomposition (The Operational Test)

Before naming a single reference, decide **how many distinct camera-spaces the episode actually has.** This replaces the old "a location that appears in 3+ scenes gets one ref" heuristic — that rule under-decomposes (a "town" is not one space) and it was exactly how EP09 and EP10's town lost references and paid for them late.

**The operational test.** Two scenes share ONE environment reference **if and only if** both of these hold:

- **(a) Single site-map test** — both cameras can sit as viewpoints on ONE drawable floor-plan / site-map. If you cannot draw both shots as camera positions on the same little map, they are not the same space.
- **(b) Landmark-consistency test** — every landmark named in BOTH scenes keeps the same relative position (the shutter stays back-right, the tower stays on the horizon to the left). If a landmark has to move between the two shots, they are not the same space.

**Either test fails → separate spaces → separate references.**

**The ceiling and the alarm band.**
- **Never segment finer than the dramaturgy's own location labels.** The dramaturgy is the ceiling; if it calls a place one location, do not shatter it into five refs for their own sake.
- **Alarm band: roughly 1 reference per 3 scenes.** If a single ref is carrying many more scenes than that, run the operational test again — it is probably hiding two spaces (this is the smell that flagged the EP10 town below). This is a smell, not a hard limit; a genuinely wide-but-coherent space (one meadow shot from many viewpoints) can legitimately carry a long span.
- **Spaces under ~2 scenes do not earn a standalone ref.** Either extend a neighboring ref to cover them, or chain from an adjacent frame (Rule 4c). Do not mint a reference for a place the camera visits once.

**Worked example — the EP10 town.** The dramaturgy's "town" is really **three** camera-spaces under the operational test:
1. the **residential lane** (waking street corners, the threshold, the first footsteps),
2. the **market edge** (the vendors, the crowd, "Among Them"), and
3. the **far edge on the descent** (the descending road with the distant glass tower on the horizon).

The market crowd and the far-edge tower cannot sit on one site-map, and the tower is a landmark that would have to move — both tests fail. **Honest note:** the shipped EP10 v01 mapped all three sub-spaces to a single reference (REF D, "Dawn Town Street") and paid for it — the missing market-edge and far-edge references (REF E / REF F) were discovered late, by luck, not by the pipeline. Phase 1 exists so that decomposition happens on cheap text at the gate, not expensively mid-production.

---

## 1.2 — Through-Anchor Requirement (Sibling References of One Location)

When one dramaturgy location legitimately decomposes into sibling references (lane / market / far-edge; workshop interior / exterior), the siblings must not drift into three unrelated worlds. Each set of sibling refs of one location MUST declare, in the REF blocks:

- **A shared palette journey** — the color band each sibling sits in, on one continuous arc (EP10: grey-blue dawn → full sunrise → full morning), so the town reads as one town waking, not three towns in three weathers.
- **A single light-direction / time contract** — one sun, one time-of-day progression across the siblings; no sibling lit from a contradictory angle or hour.
- **At least one co-visible through-anchor landmark** — a feature visible across the siblings that stitches them into one place (EP10: the distant monolith silhouettes on the horizon; a workshop's chimney; the ridge line).

**Checklist line every sibling set must pass:** *"no cross-ref typology clash (roofs, materials, horizon)."*

**Worked failure — the REF B / REF D roof clash.** In EP10 the crossroads ref (REF B) came back with **flat roofs** while the town ref (REF D) established **tile roofs** — a roof-typology clash that would have read as two different places one cut apart. It was caught and resolved at the image stage by removing the houses from REF B entirely, reframing it as the village *exit* onto open highland (REF B reframe, 2026-07-07 / commit `60cabd2`). The through-anchor check exists to catch this on text, before the pixels, not after.

---

## 1.3 — Enumerate Every New Reference (Environments AND Characters/Groups)

Reference-first is not just about environments. **ADR-0007's original driver was a CHARACTER reference** — EP09's kintsugi body did not exist, so every gold-body scene was conjured from long text on the wrong (damaged) reference, and that fight *was* the 8-10x reshoot tax. Phase 1 must therefore list EVERY new reference the episode needs:

- **Environment references** — one per distinct camera-space from the decomposition (1.1).
- **Body-state references** — any Robotiko phase/state not already on disk. Look up `reference_images` + `phase_reference_map` in `character_profiles.json`. If the episode needs a body state whose reference path is null or missing on disk, that reference is a Phase-1 deliverable, not a Phase-2 discovery. (Phase 1 (EP01-03): `ref_robotiko_master.png`. Phase 2 (EP04-07, EP08 body): `android_damaged.png`. Phase 3: `android_kintsugi.png`. Check `episode_overrides` for EP08/EP09 intra-episode transitions.)
- **Group references** — every episode-specific group that recurs or reacts (travelers, wedding guests, onlookers). A group that recurs across scenes needs a neutral-composition reference so it stays the same group; a one-off anonymous ensemble that never recurs and never reacts does not (note that honestly in the REF section, as EP10 did for its Dawn Workers).
- **Mentor:** `ref_mentor_master.png` (EP01-07 only). After EP07 the Mentor is gone; only his objects (the staff) may appear.

Every reference on this list is gated at 1R alongside the environments. Loop-back in Phase 2 (2.5) covers a **missing character reference** exactly as it covers a missing space.

---

## 1.4 — REF Block Schema

Every reference in the Phase-1 document is authored as a block with these fields, in this order. The block is the reference's whole contract.

**`### REF {letter}: {Name} ({scene span})`**

- **Design Brief:** What the space/subject IS and what it must never become — its identity, its mood, its hard "NOT" clauses (no monument framing, no light from within the stone, no invented mouth). Prose.
- **Environment Geometry:** This field has **two lives**:
  - *Phase 1 — the generation spec.* A DECISION, not a discovery: the canonical camera position, the perspective direction, and where the key landmarks sit ("eye-level; the two stone loops lie across the mid-ground, near loop toward camera; monolith mountains in the background; low horizon, big warm sky"). This is what the ref image is generated to hit.
  - *Post-approval — MANDATORY rewrite to the actual pixels.* The moment the reference image is approved (start of Phase 2), this field is **rewritten in place to describe the ACTUAL approved pixels**, modeled on EP10's REF B "Framing Pass note" format (`Framing Pass note (2026-07-07): Locked. Gen 1 drifted...; final edit removed the background houses...; landscape anchor = distant peaks + highland scrub`). This rewrite is **not optional** — it is the structural replacement for the old skipped Framing Pass. A scene in Phase 2 frames to THIS updated note, i.e. to the real image, never to the stale generation spec.
- **Narrative anchors:** The story obligations the space must preserve, carried from the dramaturgy — the content that must NOT be demoted away when the geometry gets rewritten. Examples that verifiably live in the EP10 notes today: *the beside-space stays open (his right side)*; *the street runs toward the town = the direction of desire*; *reserved sky room for a walking figure and a crossing flock without touching the celestial bodies*. Geometry says where the camera sits; narrative anchors say what the frame owes the story.
- **Reference Image Path:** Canonical form `episode-{XX}/04_visuals/raw/ep{XX}_ref_{name}.png`. (Environment refs and per-episode body/group refs both follow this; shared cast refs like `android_kintsugi.png` live in `_assets/cast/`. The `raw/` segment is canonical — EP10 v01's raw-less paths are tolerated legacy, not the pattern to copy.)
- **Text Prompt:** The full standalone reference prompt — wide establishing shot, no characters (for environments), full spatial detail, ending with the mandatory suffix. **The marker MUST stay exactly `**Text Prompt:**`.** Do not rename, restyle, or re-case it. The ADR-0006 prompt-hygiene lint scopes REF prompts by that exact marker; renaming it silently drops every reference prompt out of hygiene enforcement (ASCII/no-em-dash, forbidden aesthetics, suffix presence).

---

## 1.5 — ART DIRECTION LOCKS (Mandatory Phase-1 Section)

Promoted from an EP10 nicety to a mandatory Phase-1 section. This is the cross-scene working memory Phase 2 resumes from — the shared brain that keeps 40 scenes coherent. It captures, at minimum:

- **Color-journey scene-bands** — which scene ranges sit in which color state, as one arc (EP10: his gold distinct in pre-dawn grey → grass-gold and seam-gold converge → one warmth by the meadow).
- **Per-episode budgets** — scarce effects with a hard count (EP10: **the single Amber Pulse, S10 only**; embers are orange-red, never amber). Name the budget and where it is spent.
- **Camera personality + gaze discipline** — the episode's camera character (EP10: THE COMPANION CAMERA, alongside never above, beside-space kept open) and the gaze rules (EP10: the only direct look into the lens is S34a; elsewhere the gaze stays below/beside the lens).
- **Body-state locks** — what the body does and does not do this episode (EP10: full kintsugi from frame one, stable, no transformation beats; the mouthless-face guard).
- **"What is NOT shown"** — the explicit exclusion list (no monument framing of the ∞ stone, no Mentor embodied, no screen-world, no invented mouth).

---

## 1.6 — Scene→Space Coverage Map (Mandatory, Delivered AT the Gate)

The single artifact that converts the gate from a false "done" sticker into a real one. A table, authored **before** any image is generated, that lets the director validate reference coverage against the whole story on cheap text — before spending days generating.

| Field | Content |
|---|---|
| **scene-id** | S01, S02a, S02b, ... — every scene in the approved dramaturgy |
| **camera-space** | the reference (or `ref-less`) this scene will frame to |
| **one-line narrative role** | what the scene does in the story (one line) |

Every dramaturgy scene appears exactly once. Ref-less scenes (macro, fourth-wall close-ups, tracks-only) are listed with `ref-less` in the camera-space column — they are NOT omitted; they are the scenes most likely to carry the emotional payload and must be visible at the gate. This map also names, for free, **which scenes to re-verify if a reference is ever edited late** (the GAP-B backstop, and the input to the Phase-2 backstop rule 2.8).

---

## 1.7 — The Phase-1 Sentinel (Closes the Document)

The Phase-1 document ends with this block, **verbatim**, placed where the scene section will later be written:

```
## SCENES — PENDING (PHASE 2)

> STATUS: this is a valid, designed Phase 1 deliverable, not an unfinished draft.
> Reference prompts above are authored and human-approved; scene prompts are intentionally
> not written yet. They are authored in Phase 2, framed against the REAL reference images
> once a human has generated and approved them. Why: docs/two-phase-visual-prompts.md
>
> SCENES_STATUS: PENDING_PHASE_2
```

The machine token `SCENES_STATUS: PENDING_PHASE_2` tells the validator this is an intentional Phase-1 file (partial pass — ref prompts validated, scenes correctly absent) rather than a refs-only false green. It is removed in Phase 2. Do not paraphrase or re-case it.

---

## ⛔ HARD STOP: REFERENCE GATE (Gate 1R)

> **This is a mandatory human checkpoint. Phase 2 does not begin until it clears. Never skip it.**

Deliver the complete `ep{XX}_visual_prompts_v01.md` (references + locks + coverage map + sentinel) and hand off with this message:

1. **Generate the reference images** listed above into `episode-{XX}/04_visuals/raw/` as `ep{XX}_ref_{name}.png` (environments, body states, groups).
2. **Iterate freely.** Regenerate, reframe, edit — this is the cheap place to get the world right. (This is also where the honest divergences get caught: a roof clash, a drifted castle, a glowing amber tip.)
3. **Approve.** When every reference image is right, the human approves the reference SET.
4. **On approval, gate 1R is recorded as data** — an entry in `_management/approvals.json` (`gate: "1R"`, `artifact:` the v01 path, `sha256`, `date`, `note`), **sha-pinned to the frozen v01 bytes.** From this point v01 is frozen; a later edit to it fires the existing sha-drift WARN, which is the honest late-ref-edit signal. `project_metadata.json` `production.visuals` moves to the half-state `"refs_approved"`.

**Honest limit.** 1R records that a human approved the reference PROMPTS and signed off the reference IMAGES they generated. The images live in gitignored `raw/` and are not machine-verifiable — the gate is preventive at this SKILL layer, detective at CI. Same posture as gates 1 and 2.

**Optional escape valve.** If, and only if, the director asks for it to judge a contested reference, you may write **ONE throwaway exemplar scene prompt per contested ref** — explicitly labeled non-binding, a judgment aid to see the space with a figure in it. It is **rewritten from scratch in Phase 2** against the real pixels and carries no authority. Cap it hard: one per contested ref, never a back door into writing the scene set early.

---

# PHASE 2 — SCENE AUTHORING AGAINST REAL PIXELS

Phase 2 runs in a **separate session** after gate 1R clears. Its inputs are the approved reference IMAGES in `raw/`, the frozen v01, and the approved dramaturgy. Its output is `ep{XX}_visual_prompts_v02.md`. Every scene is born framed to a reference that already exists — there is no "frame to an image that doesn't exist yet" problem left to solve.

---

## 2.1 — Opening Move: Batch Verification Pass (Before Writing Any Prompt)

Do NOT start writing scene prompts. First:

1. **Read every approved reference PNG** in `raw/` (actually open the pixels — Read the image files).
2. **Walk ALL scenes against the pixels + the coverage map** — every scene, checking that the reference it is mapped to truly holds that scene's space, body state, and group.
3. **Collect EVERY gap into ONE loop-back batch** — a missing space the decomposition now reveals, a missing character/body-state ref, a decomposition split a real image exposes. Surface the whole batch at once.

No mid-authoring interruptions: you do not want to be forty scenes deep and discover a missing market-edge reference. One batch, resolved up front (2.5), then write.

**Rewrite the Environment Geometry notes to the pixels.** As part of this pass, perform the mandatory post-approval rewrite (1.4): each reference's Environment Geometry note is updated in the carried-forward REF block to describe the ACTUAL approved image, in the REF B Framing-Pass-note format. Scenes frame to these updated notes.

---

## 2.2 — Re-Anchor Mandate (Story First, Then Pixels)

Before writing scene prompts, **re-read the approved dramaturgy and the ART DIRECTION LOCKS.** The pixels tell you where the camera can sit; the dramaturgy tells you why the shot exists. Do not let the image overwrite the story.

- **Dramaturgy Reference = a cited pointer, not a fresh paraphrase.** Each scene's Dramaturgy Reference field cites the dramaturgy Shot ID and points to its text — it is not a new description improvised from staring at the reference image. The story is authored once, in the dramaturgy; Phase 2 points back to it.
- **Name the episode-wide rules where they bind.** In each scene's Composition Notes, name the LOCKS rules that constrain that scene — gaze discipline, beside-space, the active color band, the mouthless-face guard, the spent/unspent budget. The LOCKS are the working memory; Composition Notes are where they touch each scene.

---

## 2.3 — Ref-less Scene Gate (Closes the Fourth-Wall Hole)

Scenes with **no environment reference** — macro shots (leaf veins, frost, a forearm seam), tracks-only frames, fourth-wall close-ups (EP10's S34a/b, S27, S31, S08, S23) — cannot be "framed to pixels." They are structurally exempt from the frame-to-reference check, and they are frequently the scenes carrying the emotional payload. They get their own gate:

> **Every ref-less scene is checked, explicitly, against its dramaturgy grammar obligations** — the gaze rule, the beside-space, the match-cut angle contract, the mouthless guard, the budget. It is signed off against the STORY, not against an image. A ref-less scene that quietly violates a LOCKS rule is exactly the failure this gate exists to catch.

List the ref-less scenes and their grammar checks explicitly in the Phase-2 output so the completeness approver (2.6) can see them.

---

## 2.4 — Per-Space Camera Ledger (In the Output)

Phase 2 emits a Camera Ledger — the artifact that finally makes Rule 4b's "vary within the space" and cross-scene geography contradictions visible on one screen:

| space | ref | scene | camera position & heading | landmark screen-side |
|---|---|---|---|---|
| market edge | `ep10_ref_market.png` | S11 | eye-level, facing the vendors, road receding right | oven back-left |
| market edge | `ep10_ref_market.png` | S12 | tracking-height among the crowd, facing down-lane | oven back-left |

One row per scene per space. If two scenes in the same space put the same landmark on opposite screen-sides for no story reason, the ledger shows the contradiction at a glance. It is also where you confirm the Camera Diversity rule is honored: same space, deliberately different, spatially coherent viewpoints — never the ref's exact angle cloned.

---

## 2.5 — Loop-Back Rules (Mini-Phase-1 for a Discovered Gap)

When the batch verification pass (2.1) reveals a missing reference, loop back — a compressed Phase 1 for that one reference:

1. **Author the reference prompt** → the human generates it → approves it → record a dated 1R-note or ledger note for it.
2. **The new reference must carry its parent location's through-anchors AND narrative anchors** (1.2, 1.4) and be **checked against the dramaturgy's location text.** A loop-back reference **may add a sub-space** of a place the dramaturgy already names; it **may NOT invent a new place** the dramaturgy does not have. *(Cautionary case: a loop-back or regeneration that drifts into a "European castle" the story never had — REF B's first-generation drift, 2026-07-07 / commit `60cabd2` — is a reject, corrected back to the village exit the dramaturgy calls for.)*
3. **Termination.** The measure is the **count of not-yet-framed scenes**, which strictly decreases with each loop-back; the bound is the total scene count. Decomposition may SPLIT a space and thereby GROW the reference set — so the space count is NOT a valid termination measure — but every loop-back frames at least one previously-unframed scene, and the unframed-scene set only shrinks. The loop terminates.

---

## 2.6 — Completeness Check (Human-Gated, Named Judge)

Performed by **the Gate-1 (dramaturgy) approver, against the approved dramaturgy** — not by the author, and not against the images. The judge confirms:

- Every scene's reference anchors the **same physical space its dramaturgy text describes.**
- **No scene is mapped to another space's reference** (a market scene framed to the lane ref, a far-edge scene framed to the market ref).
- **Every ref-less scene passes its grammar check** (2.3).

This is the check that the coverage is not just complete-looking but story-true.

---

## 2.7 — Output: v02

- Filename `ep{XX}_visual_prompts_v02.md` — the **complete Phase-1+2 document**: the REF blocks carried forward (with Environment Geometry notes rewritten to the approved pixels), the LOCKS, the coverage map, the Camera Ledger, and all scene prompts.
- **The sentinel is removed.** A v02 that still contains `SCENES_STATUS: PENDING_PHASE_2` is a stale-sentinel FAIL (scenes present + sentinel present).
- Geometry notes are updated wherever the real image diverged from the generation spec.

---

## 2.8 — Backstop Rule (Late Reference Edits)

> **If a reference image is edited AFTER Phase 2 has begun, every scene bound to that reference in the coverage map MUST be re-verified against the new pixels before delivery.**

This is the structural fix for the exact failure that motivated the redesign (a REF block updated, dependent scenes never re-checked). The coverage map (1.6) names the affected scenes; the backstop rule makes re-verifying them non-optional. Also lives in `pipeline_rules.md`.

---

# PROMPT GENERATION RULES

These rules govern the actual writing of prompts. Rules 4b and 4c are the core of Phase-2 framing; all rules apply to both reference prompts (where relevant) and scene prompts. **Phase 2 re-references this whole section** — nothing here is superseded by the two-phase split; the split changes WHEN scenes are written (against real pixels), not HOW.

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

**Do NOT also restate what the bound reference already shows.** `the chrome android (android_damaged.png)` carries the full damaged body, the missing ear, the wires; adding "battle-scarred rusted chrome, missing right ear with exposed wires" competes with the reference and degrades the output. Describe ONLY what is NOT in the reference — a new wound, or the emerging gold/kintsugi transformation the damaged reference does not yet show.

### Rule 3: Character Embedding
When a character appears in a scene:
- The **short identifier is authoritative**, and it is **bound to its reference inline** (Rule 2b) — the reference image carries the visual detail. The text prompt names the subject and pins the file; the uploaded reference defines what it looks like. Long descriptions compete with the reference and confuse the model.
- For Robotiko: "a chrome android (android_damaged.png)" or "the chrome android (android_kintsugi.png)" — the phase-correct reference (via `phase_reference_map`) carries the damage/kintsugi state, body details, and proportions. Bind the same file for close-ups of his hand, face, or chest.
- For Mentor: "an elderly figure in dark green cloak, wooden staff with glowing amber tip" when `ref_mentor_master.png` is uploaded (EP01-07 only).
- For episode-specific groups: use a brief consistent descriptor (e.g., "three young travelers — mixed men and women with colorful scarves") when the group's reference image is uploaded.
- Only add specific damage/state details if they differ from the reference image (e.g., "thin scratch across his cheek" for a new wound not present in the ref).
- Do NOT use character names ("Robotiko", "Mentor") — image generators don't know names. Describe by appearance.

**Example — Robotiko with phase-correct reference uploaded (Phase 2, damaged):**
> A chrome android standing at the edge of a rusted platform...

**Example — Robotiko WITHOUT reference image (fallback only):**
> A retro-futuristic chrome android with battle-scarred chrome body, exposed analog wires, steady blue optical lenses set into chrome sockets like polished sapphires, standing at the edge of...

> See `_memory/lessons.md` CHARACTER DESIGN (ADR-0010) — never write "glowing [color] eyes" in a model-facing string; the eye-glow lint FAILs on it.

### Rule 3b: Anti-Spawn Guard
Image generators spawn duplicate characters. Every single-character scene needs a guard — but the phrasing depends on the tool:
- **Nano Banana / Gemini:** End the prompt (before the style suffix) with: `single figure composition, no additional characters`
- **Motion prompts (Kling / Veo / Seedance):** Use the motion-specific guard from the motion script skill: `Do not add extra characters. Keep everything as pictured.`
- Do NOT write "only ONE android" or "no second robot" — these literal number/negation phrases backfire in Nano Banana, causing the tool to latch onto the concept of a second robot and generate one.
- **OMIT the guard entirely when the uploaded character reference + scene context already establish a single figure** (a solo portrait reference in a clearly solo scene). The phrase is then redundant noise; see the golden EXAMPLE below ("the reference plus 'alone' already establish a single figure"). Add the guard only when duplication is a real risk: no strong solo reference, or a scene/composition the tool tends to populate.
- **Exception:** Intentional multi-figure scenes (ghost-self, dream copies, a crowd Robotiko walks through) skip the guard and instead specify the exact count and each instance's distinct treatment — see the INTENTIONAL MULTI-FIGURE rule in `_memory/lessons.md`.

### Rule 4: Environmental Specificity
- Never write generic environments ("a futuristic city", "a dark room").
- Always describe specific textures, materials, depth layers, and light sources.
- Ground the scene in the 70s Prog Rock aesthetic: analog, industrial, painterly.
- Include foreground/midground/background layering when the dramaturgy calls for depth.

### Rule 4b: Frame to the Environment Reference
Frame every scene's **angle and composition to the geometry of its environment**, so the shot sits inside a coherent, consistent space instead of defaulting to a flat frontal portrait.

In the two-phase flow, **the reference image always exists by the time you write the scene** (that is the whole point of the gate). So the mode is always: **open the approved reference image and read its geometry** — camera position, perspective lines, where the depth goes, where the landmarks sit — and write the angle to match its rewritten Environment Geometry note (the one describing the real pixels, 1.4 / 2.1). You are never framing to a note for an image that does not exist yet.

- **Why it matters:** a character reference is usually a frontal portrait. If you don't name the angle, the generator turns the character to face the camera and centres them — flat, symmetrical, identical every time. Naming the angle that matches the environment breaks that default and gives the scene depth. (EP09 S34 kept coming out dead-centre and frontal until rewritten as "three-quarter view from the front-left corner, the bench receding diagonally toward the shutter" — matching `ref_workshop.png` — and it locked on the first try.)
- **Vary within the space:** scenes in the same location must NOT clone the env-ref's exact angle. Choose deliberate, *spatially coherent* viewpoints inside the established geometry (a reverse angle, a low angle across the bench, a corner three-quarter), honouring the episode's Camera Diversity rule. The Camera Ledger (2.4) is where this is verified.
- **Specify** the camera **angle** and the subject's **placement / orientation**: three-quarter vs. profile vs. frontal, off-centre (rule of thirds), eye-level / low / high, and the leading lines from the environment.
- **Do NOT specify camera MOVEMENT** (pan, zoom, tilt, pull-back, dolly) — that is a still image; movement belongs to the Motion Script (see DON'T list). Leave breathing room for the move instead of naming it (Rule 7).
- **Upload the matching environment reference** so it reinforces the angle instead of fighting it — the env ref's own perspective is the strongest signal the generator has.

### Rule 4c: Base Image — lock a composition or chain a pull
When an earlier generated frame already holds what a scene needs — a fixed composition (a threshold layout, a camera position) OR an established WORLD that must stay consistent as the camera moves — declare it as the **base image** ("Use 5.png as the base image") and describe ONLY what changes. The base carries the entire frame, so do NOT re-describe what it already shows. Two uses:

- **Lock a static frame:** reuse a prior frame's exact composition and change only the light/state (EP09 S36: `5.png` as base locked the dawn-threshold on a one-line change; re-describing the exterior had made it drift).
- **Chain a zoom-out / extra-wide pull:** use the PREVIOUS (tighter) frame as the base for the next (wider) one, then just widen the framing ("Ultra-wide shot... in the lower-centre third"). The world stays identical as the camera pulls back. EP09's dawn pull chains this way: `5.png` → S36 (base `5.png`) → S37 → S38 (base `37.png`).
- Also the tool for the **<2-scene spaces** the decomposition (1.1) declined to give a standalone ref: chain them from an adjacent frame instead of minting a reference.
- Stronger than an environment reference for continuity (it pins the FULL frame — camera + interior + exterior — not just the look) and keeps the prompt short. Record it in the scene's `Upload` field as `base: <frame>`.

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
- Color temperature should flow with the musical energy arc (cold → warm or vice versa) — tracked in the ART DIRECTION LOCKS color-journey bands (1.5).
- Recurring elements (Mentor's staff, Robotiko's exposed wires) must be described identically each time.

---

## OUTPUT FORMAT

Use the template from `_templates/visual_prompt_template.md` (one template, both phases, gate divider + sentinel pre-placed). The v02 document contains:

### 1. Episode Header
| Field | Value |
|---|---|
| Episode | EP{XX} |
| Title | [from dramaturgy] |
| Station | [from dramaturgy] |
| Character Phase | [Phase 1 / 2 / 3] |
| Robotiko Visual State | [exact `visual_prompt_addition`] |
| Camera Personality | [episode camera character, from the LOCKS] |
| Total Prompts | [scene prompts + reference prompts; scene count must match dramaturgy] |

### 2. Mandatory Style Suffix
Displayed once at the top as a reference block.

### 3. Forbidden Aesthetics Reminder
Quick reference of what must never appear.

### 4. ART DIRECTION LOCKS
The mandatory section from Phase 1 (1.5), carried forward.

### 5. Reference Blocks
The REF blocks from Phase 1 (1.4), carried forward, with Environment Geometry notes rewritten to the approved pixels.

### 6. Scene→Space Coverage Map + Camera Ledger
The coverage map (1.6) and the per-space Camera Ledger (2.4).

### 7. Generated Prompts (Grouped by Musical Section)
Prompts are grouped under section headers matching the dramaturgy's musical structure (e.g., "INTRO & AWAKENING (0:00 - 0:42)").

Each prompt block contains:

| Field | Description |
|---|---|
| **Scene ID** | S{XX} — matches dramaturgy Shot ID |
| **Timestamp** | From dramaturgy |
| **Dramaturgy Reference** | Cited pointer to the dramaturgy Shot ID (2.2) — not a fresh paraphrase from the image |
| **Characters Present** | List with phase-appropriate visual state noted |
| **Image Reference Path** | Phase-correct ref from `character_profiles.json` → `phase_reference_map`, or N/A for scenes without characters |
| **Video Tech Strategy** | Standard / Start-End Keyframes (from dramaturgy detail blocks; the former Extension mode is deprecated — long scenes are handled by the motion script's Duration Coverage Strategy) |
| **Composition Notes** | Headroom, breathing space, depth guidance; the LOCKS rules that bind this scene (gaze, beside-space, color band, budget) named where they apply (2.2) |
| **Upload** | Per-scene list of reference images: character ref, environment ref, chain/base ref, special ref — matching the inline bindings (Rule 2b) |
| **Text Prompt** | The full image generation prompt ending with the mandatory suffix |

### 8. Quality Checklist
The post-generation checklist at the bottom of the document.

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
- Use an em-dash or non-ASCII punctuation INSIDE a Text Prompt blockquote (ADR-0006 hygiene) — plain ASCII only in prompts

### EXAMPLE (Good):
> Medium-wide shot inside a workshop (ep09_ref_workshop.png), the corrugated metal roll-up shutter fully closed filling the back wall, no daylight, the chrome android (android_damaged.png) alone at the workbench, calm steady blue optical lenses set into chrome sockets, faintly catching the dim light, only a dim work lamp casting a low pool of light on the bench, a Turkish tea glass left behind on the bench surface, dark workshop atmosphere, isolation, 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

**Why it works:** each reference is bound inline (`workshop` + `chrome android`); the short identifier carries the look with NO restated damage; nothing absent is named (no "the old man gone"); no redundant anti-spawn phrase — the reference plus "alone" already establish a single figure.

### EXAMPLE (Bad):
> Robotiko standing in a desert looking cool and futuristic. The lighting is dramatic and moody. He looks amazing and powerful. 8k masterpiece.

---

## HANDLING SPECIAL CASES

### Scenes Without Characters (Environmental / Atmospheric)
- These prompts focus entirely on environment, texture, and mood.
- Describe the space as if it is a character: give it material, history, decay.
- Still apply the mandatory suffix; still compose with headroom and breathing space.
- If truly ref-less (macro, tracks-only), they pass through the ref-less scene gate (2.3) — checked against dramaturgy grammar, not framed to an image.

### Scenes With Multiple Characters
- Describe spatial relationship between characters (distance, relative position, eye contact or avoidance).
- Each character is bound to its phase-correct reference (Rule 2b/3).
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

- **v01 = the complete Phase-1 document** — references + ART DIRECTION LOCKS + coverage map + sentinel; zero scenes. Frozen at gate 1R and sha-pinned in `approvals.json`.
- **v02 = the complete Phase-1+2 document** — the v01 references (geometry notes rewritten to pixels) carried forward + all scene prompts + Camera Ledger; sentinel removed.
- If the human requests revisions after reviewing v02, increment: `v03`, `v04`, etc.
- **Each version is a complete document, not a diff** — this invariant is preserved; the two-phase split just makes v01 a complete *Phase-1* document rather than a partial scene set.
- Version number in the filename: `ep{XX}_visual_prompts_v{VV}.md`

> **Framing Pass — retired.** The old standalone "Framing Pass" step (reconcile scenes to real pixels, "never a blocker") no longer exists as a separate optional step. **Superseded: Phase 2 IS the framing pass — scenes are born framed to approved pixels.** What was an optional, skippable reconciliation is now the structural body of Phase 2.

---

## POST-GENERATION CHECKLIST

Before delivering **Phase 1 (v01)**, verify:

- [ ] Location decomposition applied — the operational site-map + landmark-consistency test (1.1), not the old "3+ scenes" heuristic; alarm band (~1 ref/3 scenes) checked; <2-scene spaces extended or chained (Rule 4c)
- [ ] Every new reference enumerated and gated — environments AND body-state AND group refs (1.3, ADR-0007)
- [ ] Sibling refs of one location declare through-anchors (shared palette journey, single light-direction, ≥1 co-visible landmark) and pass the "no cross-ref typology clash" line (1.2)
- [ ] Each REF block carries Design Brief + Environment Geometry (generation spec) + Narrative anchors + canonical Reference Image Path + a `**Text Prompt:**` marker spelled exactly (1.4)
- [ ] ART DIRECTION LOCKS section present (color bands, budgets, camera personality + gaze, body-state locks, "what is NOT shown") (1.5)
- [ ] Scene→space coverage map complete — every dramaturgy scene mapped, ref-less scenes listed as `ref-less` (1.6)
- [ ] Phase-1 sentinel block present, verbatim (1.7)
- [ ] Every reference Text Prompt ends with the mandatory suffix and is plain ASCII (no em-dash)

Before delivering **Phase 2 (v02)**, verify all Phase-1 items carried forward, plus:

- [ ] Batch verification pass done — all ref PNGs read, all scenes walked against pixels + coverage map, all gaps resolved in one loop-back batch (2.1)
- [ ] Environment Geometry notes rewritten to the ACTUAL approved pixels (mandatory post-approval rewrite, 1.4 / 2.1)
- [ ] Every scene's Dramaturgy Reference is a cited Shot-ID pointer, not a fresh paraphrase from the image (2.2); binding LOCKS rules named in Composition Notes
- [ ] Ref-less scenes signed off against their dramaturgy grammar obligations (2.3)
- [ ] Per-space Camera Ledger present and internally consistent — no unexplained landmark screen-side flips; angles vary within each space (2.4)
- [ ] Loop-back references (if any) carry parent through-anchors + narrative anchors, add sub-spaces only, never invent a place (2.5)
- [ ] Completeness check performed by the Gate-1 approver against the approved dramaturgy (2.6)
- [ ] Sentinel ABSENT from v02 (2.7)
- [ ] **Scene headers are `#### S{NN}` (FOUR hashes), NOT `###`** — `extract_scenes` requires `####\s*(?:Scene\s+)?S\d{2}`; three-hash headers parse to ZERO scenes, tripping the scenes-XOR-sentinel meta-test (and, in other contexts, a false green). Two-digit scene number + optional a/b suffix (`#### S02a`).
- [ ] **No TEMPLATE_MARKERS anywhere in v02** (`{XX}`, `auto-populated by Claude`, `Do not fill manually`, `[Claude generates`, `Shot X: ...`) — once the sentinel is removed, ANY such marker makes the validator silently scaffold-skip the whole file (every scene goes unvalidated = false green). Write concrete filenames (`ep10_s01_selected.png`), never `{XX}`. Also: do NOT print the literal `**Text Prompt:**` marker in prose/checklists — the prompt-extractor matches it as a real (suffix-less) prompt; write "the Text-Prompt marker" without asterisks.
- [ ] Every single prompt ends with the mandatory style suffix (check every one)
- [ ] Short character identifiers used, bound inline `element (filename.png)` matching the `Upload` field; no restated detail the reference already shows (Rule 2b/3)
- [ ] Every Robotiko scene references the phase-correct ref from `phase_reference_map`
- [ ] Anti-spawn guard uses tool-appropriate phrasing and is OMITTED when a solo ref + solo scene already establish a single figure (Rule 3b)
- [ ] No forbidden aesthetics in any prompt (Rule 6)
- [ ] All prompts have composition space (headroom + breathing space) for camera movement (Rule 7)
- [ ] Each scene's angle framed to its environment reference — no default dead-centre frontal; angle/composition only, NO camera movement (Rule 4b)
- [ ] Total scene-prompt count matches the approved dramaturgy scene count; Start/End scenes have two prompts (S{XX}a/S{XX}b)
- [ ] Lighting direction specified in every prompt; no prompt references another prompt
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## WHAT HAPPENS NEXT

After the v02 visual prompts are delivered:
1. Human feeds each scene prompt to Nano Banana for image generation (references already exist from Phase 1)
2. Multiple variants are generated per scene → stored in `04_visuals/raw/`; attempts logged in `raw/attempts.md` (EP10 onward — first-pass-yield telemetry, ADR-0007 note)
3. Human selects the best variant per scene → stored in `04_visuals/selected/` as `ep{XX}_s{XX}_selected.png`
4. Selected images become input for `_skills/robotiko-motion-script/SKILL.md`

**Every weak prompt produces a weak image. Every weak image produces a weak video. Precision here cascades forward through the entire pipeline — and framing to real pixels instead of text is the single biggest lever on first-pass yield.**

---

## SUPPLEMENTARY VISUAL PROMPTS (Motion Script Feedback Loop)

The motion script skill (`robotiko-motion-script`) may discover that some scenes require additional images to cover their full music duration. When this happens, the motion script includes **inline supplementary visual prompts** — complete, ready-to-use prompts embedded directly in the motion script document.

### How This Works

1. The motion script identifies scenes where a single video clip cannot cover the music duration.
2. These scenes are split into sub-clips (e.g., S29a, S29b, S29c, S29d).
3. Sub-clips that need a different composition than the existing selected image get an inline supplementary visual prompt.
4. The human generates the image from this prompt in Nano Banana, selects it, and saves it with the filename specified in the motion script.

### Quality Rules for Supplementary Prompts

Supplementary prompts generated by the motion script skill **must follow all rules of this visual prompts skill** — and, because the references already exist by then, they frame straight to the approved pixels (Rule 4b):

- [x] Must end with the mandatory visual suffix — no exceptions
- [x] Must respect the episode's character phase (from `character_profiles.json`)
- [x] Must not include any forbidden aesthetics
- [x] Must be fully self-contained (no cross-references to other prompts)
- [x] Must include composition space (headroom + breathing space) for camera movement
- [x] Must frame to the scene's approved environment reference and bind it inline (Rule 2b/4b)

The motion script skill generates these prompts, but they are subject to the same quality gates as primary visual prompts.

### Naming Convention

Supplementary images follow the sub-clip naming pattern:
- `ep{XX}_s{XX}{a|b|c|d}_selected.png`
- Example: `ep02_s29c_selected.png` (third sub-clip of scene 29)

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Dramaturgy not approved | STOP. Cannot generate references or scenes from unapproved dramaturgy. |
| Dramaturgy file missing | STOP. Inform human. The pipeline requires dramaturgy before visual prompts. |
| Asked to write scenes before gate 1R | STOP. Phase 2 does not begin until the reference gate clears. Deliver Phase 1 (v01) and request ref generation + approval. (Exception: the capped, non-binding escape-valve exemplar, 1R section.) |
| Reference image missing at Phase 2 start | Loop-back (2.5): author the ref prompt, human generates + approves, then frame the dependent scenes. Do not conjure the scene from text. |
| Reference edited after Phase 2 began | Backstop rule (2.8): re-verify every coverage-map scene bound to that ref before delivery. |
| Character design pending (e.g., Robochica) | It is a Phase-1 reference deliverable — enumerate and gate it (1.3). Do not defer it into scene prompts. |
| Dramaturgy scene has no visual description | Do not invent. Ask the human to update the dramaturgy or provide guidance. |
| Suffix accidentally omitted | This is a critical pipeline error. Re-check every prompt before delivery. |
| Scene count mismatch with dramaturgy | Investigate. The counts must match exactly. If a scene was split (Start/End), document the S{XX}a/S{XX}b convention. |
| Sentinel still present in v02 | FAIL. Remove the `SCENES_STATUS: PENDING_PHASE_2` block before delivering the scene document. |

---

*"The prompt is the blueprint. The image is the brick. Build with precision or the wall will fall."*
*"Author the world first. Then frame the story to the world you actually got."*
*— Robotiko v2.0 Pipeline*
