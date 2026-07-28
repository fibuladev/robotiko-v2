# TODO — ACTIVE TASKS
> Current open tasks and priorities.
> Claude updates this file during and after each session.

> Note for public readers: any _private/... path referenced in the session summaries below is a gitignored working file — part of the production process, not part of the public repo.

---

## SESSION NOTE (2026-07-25) — EP09 CAPCUT SYNC BUG: FIXED + VALIDATOR ADDED

EP09 montajında 35s senkron kaybı tespit edildi — kök neden: musical metadata'daki 1s section gap'leri motion script'e olduğu gibi taşındı (EP01-08'de doğru şekilde kapatılıyordu, EP09-10'da regresyon). CapCut guide timestamps'ı bitişik yaptı ama Scene Dur sütununu güncellemedi → 41 sahneden 35'i 1s kısa.

**Yapılanlar:**
- [x] EP09 CapCut guide düzeltildi: Scene Dur, Speed (13→17 ramp), Trim sütunları yeniden hesaplandı
- [x] `capcut_guide_validator.py` yazıldı: Scene Dur = Timestamp span, contiguity, total = music duration, speed/trim doğruluğu
- [x] Validator `run_all.py`'ye eklendi (12/12 green)
- [x] EP10 motion script aynı gap'a sahip — CapCut guide oluşturulurken dikkat edilecek
- [x] Lesson kaydedildi: "CLOSE THE METADATA GAPS IN MOTION SCRIPTS"
- [x] **(2026-07-28 completion)** Grade-the-graders debt closed before commit: frozen fixtures (`capcut_guide_GOOD/BAD.md`) + 18 meta-tests (both-directions speed proof, isolation, parser coverage, legacy-WARN honesty test) + invariant coverage matrix row. Legacy finding: EP01/02/03/06 guides predate the Timeline Map format → explicit WARN, never silent pass. Suite 12/12 green (245 meta-tests).

**EP10 NOT:** Motion script gap'leri EP10'da da var. CapCut guide oluşturulurken timestamps bitişik yapılacak VE Scene Dur = Timestamp span olacak. Validator otomatik yakalayacak.

---

## SESSION NOTE (2026-07-24) — SUNO DOCUMENTATION PACKAGE: RESOLVED (minimal scope)

Discussion session on documenting the music leg (Suno → BandLab → YouTube). Key finding: the `01_lyrics/epXX_lyrics.md` files already ARE the verbatim Suno lyrics-box inputs (production annotations included — verified line-by-line on EP01). Decisions: NO per-episode `epXX_suno_generation.md` files, NO music craft doc, NO Suno/BandLab share links (YouTube stays the sole canonical link) — the repo does not aim to teach Suno usage. Only deliverable landed: music rights sentence in AUTHOR.md (paid-plan commercial rights + forker warning) merged into the tool-credit litany, plus signature fix (Can Yalçın / Bratislava, 2026). Commit `6fd31a0`, suite 11/11 green, pushed.

---

## SESSION NOTE (2026-07-13)

Launch plan revised in private working files. Public docs: gate-count consistency pass — all current-truth prose now says three human gates (commit `eb187a2`), suite 11/11 green.

---

## OPEN-SOURCE READINESS SWEEP (2026-07-12) — COMPLETE (repo public-ready except EP09/EP10 episode files)

**Task:** Final pre-public hygiene pass across the entire tracked repo (302 files; episode-09/10 excluded — still in production), covering private residue, English-only, banned terms, and general public-readiness optics.
**Result:** All findings resolved; anything sensitive kept in private working files rather than the public tree. Two durable engineering lessons carried forward as method: commit-sha pointers are rewrite-mortal and must be re-mapped by commit-message key after any history rewrite; approval-ledger sha256 pins must be computed from git-stored (LF) bytes, not a Windows working copy, and verified against a fresh clone.
**Suite:** 11/11 green throughout, including a fresh-clone verification pass.
**Remaining for go-public:** EP09/EP10 completion + the final launch-day sequence (private).

---

## PUBLIC-DOCUMENT AUDIT (2026-07-09) — COMPLETE (closed 2026-07-12; independently re-verified by the sweep above)

**Task:** Audit ALL public (tracked, non-code) documents before the EP10 open-source release. Hunting: religious references (forbidden), ethnic attribution where geographic framing is required, source-indefensible claims, mission-contradicting tone (anti-democratization), cross-file contradictions, stale date/version stamps, overreaching absolutes.
**Method:** Expert panels (advocate + adversarial examiner + judge, primary sources) for contested claims — cultural attribution (Seven Stations framing reversal + per-figure verification), the "philosophical" terminology question, and the estrangement/alienation theory question (Brecht vs. Shklovsky vs. Suvin) — plus a repo-wide date-stamp audit and a 15-group sentence-level sweep.
**Known focus points going in:** master.md Seven-Stations header block (religious-order attribution introduced by the 2026-07-06 terminology sweep — to be reversed); README.md Cultural-heritage figure labels; lessons.md TERMINOLOGY rule ~line 320 (same reversal); docs/hallucinating-camera.md audience framing (gatekeeping vs. democratization mission); stale "Last Updated" stamps (master.md, lessons.md, decisions_log.md).
**Deliverable:** findings + sourced rewording proposals → Fibula approval gate → apply → suite green → commit. NO file changes before approval.

- [x] Session-start mandatory reads
- [x] Public-file inventory (notebooklm_brief.md + creator_strategy.md confirmed gitignored = out of public scope)
- [x] Audit orchestration launched (3 panels + 2 scans + 15 sweep groups, read-only)
- [x] Orchestration complete (25/26 first pass; estrangement judge re-run after a session-limit failure)
- [x] Findings report generated: `_private/audit_2026-07/public_doc_audit_2026-07-10.md` (286 deduped findings: 15 critical / 79 major / rest minor + 2 panel verdicts + date-stamp policy) — presented to Fibula
- [x] [HUMAN GATE] Fibula approved (2026-07-10) — decisions: lyrics/attested quotes untouchable; history cleanup authorized; sha re-baseline OK; date policy Option C; forbidden-terms validator added; frame-asset rename ("hair-thin crossing"); answer-poem source claim softened to "inspired by"
- [x] Batches B2-B6 applied (root/docs/mgmt/skills/memory — Opus 4.8 + Sonnet 5 subagents, diffs reviewed) + forbidden-terms gate shipped (check group 11, 31 meta-tests green). Working tree ~65 modified files, NOTHING COMMITTED yet.
- [x] Continuation completed in follow-up sessions (B1 master.md, B7 episodes, approvals re-baseline 2026-07-10, thematic commits, history rewrite + force push — evidence: clean tree at 2026-07-12 session start, suite 11/11, re-baseline notes across approvals.json). Closed 2026-07-12: the full-repo readiness sweep (block above) independently re-verified every tracked surface clean on the same rule set.

---

## EP10 RAW IMAGE REVIEW SESSION (2026-07-12) — COMPLETE

**Task:** Systematic QA review of all 47 EP10 raw image candidates (41 scene images + 6 env references) against visual prompts, dramaturgy, and series canon.
**Method:** 4 parallel QA subagents (batches of ~10 images each), full checklist: Phase 3 kintsugi stability, eye canon, mouthless-face guard, style DNA, Mentor absence, Dawn Walk art direction, gaze discipline, anti-spawn, generation defects.
**Results:** 27 APPROVE / 13 DISCUSS / 1 RESHOOT (S20). Joint review with Fibula resolved all DISCUSS items.
**Fixes applied:**
- S03: Nano Banana color temperature fix (grey-blue shift)
- S13: Nano Banana rail-track artifact removal + prompt updated (rail joins → mortar lines and gutter edges; rear-view phrasing strengthened)
- S20: Nano Banana re-generation + right-side crop (CapCut warm grade pending) + prompt updated (ref as inspiration, illegible screen content, warm full morning, no streetlights)
- S27b: Nano Banana lemon garnish removal (plain Turkish tea)
- S34b: 34b_1.png selected (superior beckoning hand gesture + warmer smile)
- S34b smile: Fibula creative override — intentional gentle smile on the mouthless face for the series' final beckoning frame
**Final: 40/40 scenes approved. Next: motion script (Checkpoint 2, separate session).**

---

## EP10 MOTION SCRIPT INDEPENDENT AUDIT SESSION (2026-07-12) — COMPLETE

**Task:** Independent post-approval audit of `ep10_motion_script_v01.md` (approved same day, Checkpoint 2) — cross-document consistency, [DISSONANCE] tag literalness, frame-chain validity, late-override sweep.
**Findings W1-W5 fixed in place on v01 (human-approved same day):** S02/S15/S16 image-fidelity guards added to motion prompts; Chain 1 (S15->S16->S17) removed as not a real chain (three distinct approved compositions, each from its own raw keeper); S34b smile-forming wording fixed and swept upstream (dramaturgy, visual prompts v02, motion script's own summary tables); [DISSONANCE] tags made literal on S26/S27 + S29 newly tagged; refrain-onset caveat + credit-budget note added.
**Also:** S08 static sub-clips (Kling 2.5 Turbo) accepted as-is by the human. `_management/dissonance_registry.md` gained 3 EP10 rows. SKILL.md gained a Cross-Doc Audit checklist (v2.1). `_memory/lessons.md` gained 3 rules. Gate-2 sha re-baselined by the reviewer in `_management/approvals.json`.
**Next:** Video generation.

---

## TWO-PHASE VISUAL PROMPTS REDESIGN SESSION (2026-07-07) — COMPLETE

**Task:** Redesign the visual-prompts pipeline so scenes are framed to APPROVED reference pixels, not conjured from a text contract — closing three gaps found in the shipped flow. GAP A: template / `visual_dna.md` / public docs were a generation behind the SKILL. GAP B: a late ref edit forced no scene re-verification (the REF B reframe, commit `9790a71`, updated a block while 40 scenes went un-re-checked). GAP C: the "3+ scenes = 1 ref" heuristic under-decomposed locations (EP10's REF E/F found late). Panel-reviewed plan (7 adversarial lenses); scope = SKILL + docs + validator methodology only.

**Shipped:**
- **SKILL v2.0 — two-phase structure:** Phase 1 (reference authoring + operational decomposition test + through-anchors + REF block schema + ART DIRECTION LOCKS + scene→space coverage map + Phase-1 sentinel; ZERO scene prompts) → ⛔ HARD STOP gate 1R → Phase 2 (batch verification pass, re-anchor mandate, ref-less scene gate, per-space camera ledger, loop-back rules, completeness check; scenes framed to real pixels). Framing Pass retired (Phase 2 IS the framing pass).
- **Template + `_assets/style/visual_dna.md`** aligned to the two-phase flow (gate divider + sentinel pre-placed, REF block schema with Narrative anchors, coverage-map + camera-ledger tables).
- **`pipeline_rules.md`** Step 5 → 5a (references, Phase 1) ⛔ gate 1R → 5b (scenes, Phase 2) + backstop rule for late ref edits; third human checkpoint added.
- **Validator phase-awareness:** `check_phase_state` (truth table on parsed scenes vs sentinel — kills the refs-only false green), `check_ref_image_path`, gate 1R wiring in `pipeline_integrity.py` (`TWO_PHASE_FROM_EP = 10`, artifact-pinned EP10 v01 waiver), frozen fixtures both directions.
- **New `docs/two-phase-visual-prompts.md`** (carries the load) + `anatomy-of-an-episode.md` Stage-6 rewrite + onboarding-doc reconciliation (`text-only-first-episode`, `fork-dry-run`, `getting-started`) + the honest-reproducibility sentence (process reproducible; assets, deliberately, not).
- **Coverage matrix** honest-gap rows (scene↔space completeness, framing-to-pixels, ref-edited-post-Phase-2 = 🔵 Human); **`project_metadata.json`** `production.visuals` made tri-state (`false | "refs_approved" | true`).
- **`_memory/lessons.md`** REF-NOTE SYNC ≠ SCENE RECONCILIATION lesson (REFERENCE IMAGE WORKFLOW category) + **ADR-0013** "Two-phase visual prompts: scenes are framed to approved pixels" — links ADR-0007 (reference-first) + ADR-0008 (gates as data); records D3 versioning (frozen v01 + new v02, sha-drift WARN as the free GAP-B signal), D4 honest limits (1R attests ref prompts not pixels; preventive/detective; waiver-only-while-it-pins-latest), D6 declined under-segmentation lint, the corrected loop-back termination measure (unframed-scene count strictly decreasing), and the +1-session honesty. Registered in the ADR README index.

**DRY-RUN + PHASE 1 DONE (2026-07-07, branch `test/ep10-two-phase-dryrun`, commit `077a58f`):** ran the new flow end-to-end as a real user. BLIND decomposition exam (context-free subagent, only dramaturgy + SKILL + the 4 approved pixels) INDEPENDENTLY demanded REF E (market edge, S11-S12) and REF F (far-edge descent, S19-S22) — GAP-C fix proven live. All mechanical claims verified: validator shows `PHASE 1 ONLY` partial pass (not false green); the gate stops the flow; the negative test FAILS CI when v02 scenes ship without a valid 1R; and the interim v01 waiver does NOT bless a v02 (panel risk R2 closed). Phase 1 authored: v01 rewritten as the Phase-1 deliverable (6 REF blocks — A-D verbatim + frozen images, E/F fresh — decomposition, LOCKS, 35-scene coverage map, sentinel, ZERO scenes). Human generated + approved all 6 ref images (REF F picked from 3 variants, shadow-retouched for S22). Real gate-1R recorded (pinned frozen v01, sha `8305fb88`), interim waiver superseded, meta-tests updated. **Suite 10/10 green.**

**PHASE 2 — DONE (2026-07-07, branch `test/ep10-two-phase-dryrun`):** Authored `ep10_visual_prompts_v02.md` — the complete Phase-1+2 document. Batch verification (Phase-2 opening move): all 6 approved PNGs read pixel-by-pixel; all 35 scenes walked against pixels + coverage map -> COMPLETE, no loop-back. All 6 Environment Geometry notes rewritten to the ACTUAL approved pixels (A: monolith towers LEFT-bg, near loop foreground, sun from right; B: staff near-center, Y-fork tracks, dish LEFT hillside, cyan retrofit line, NO houses; C: Moon LEFT / Sun RIGHT, valley+town below, ridge path lower-right; D: curving lane, dish RIGHT, geraniums LEFT; E: oven+sesame-ring bread cart+samovar RIGHT, dog-bowl foreground, green-plaster house LEFT; F: shutter stripes RIGHT, brazier foreground, glass tower horizon center-right). All 40 scene prompts framed to real pixels (S01-S35; sub-splits S02a/b, S08a/b/c, S10a/b, S27a/b, S34a/b; S35 = edit card, no image). Per-space Camera Ledger (angles vary within each space, landmark screen-sides consistent). Ref-less Scene Gate (S04/S08/S23/S27/S29/S34 signed off vs dramaturgy grammar). Sentinel REMOVED. All EP10 LOCKS enforced (Companion Camera; single Amber Pulse S10b only, embers orange-red; eye canon material-lens; mouthless-face guard esp. S17/S27/S31/S34; gaze discipline — direct lens ONLY at S34a/b; rear-view ear rule S13/S14/S18/S28; no path-shape reveal S32; ASCII prompts). Meta-test flipped (`test_phase2_asserted_and_latest_helpers_read_disk`: assertTrue + EP10_V02). `project_metadata.json` visuals "refs_approved" -> true. **Suite 10/10 green; v02 is actually validated (46 prompts: 6 refs + 40 scenes), no scaffold-skip.**

**Two false-green traps hit + fixed live (now lessons + SKILL Phase-2 checklist):** (1) scene headers MUST be `#### S{NN}` (4 hashes) or `extract_scenes` parses zero; (2) a sentinel-less v02 must contain NO TEMPLATE_MARKERS (`{XX}` etc.) or the sweep silently scaffold-skips the whole file, and never print the literal Text-Prompt marker in prose (false-positive prompt match).

**REMAINING BEFORE MERGE:**
1. **[HUMAN GATE 2.6]** Fibula performs the completeness check against the approved dramaturgy — every scene's reference anchors the same physical space its dramaturgy text describes; no scene mapped to another space's ref; every ref-less scene passes its grammar check. (The two v02 checklist items left unchecked.)
2. On sign-off: merge `test/ep10-two-phase-dryrun` -> `main` (replaces the legacy single-pass v01 with the two-phase v01 + v02). Ledger needs NO change — the real gate-1R is pin-agnostic and already covers v02.
3. Then: image generation (Nano Banana) — all 6 refs exist; attempts.md ledger MANDATORY (last first-pass-yield window) -> select -> Motion Script (Checkpoint 2).

---

## EP10 VISUAL PROMPTS SESSION (2026-07-06) — SUMMARY

**Task:** Generate EP10 visual prompts from the approved dramaturgy (Gate-1, 2026-07-06).
**Deliverable:** `episode-10/04_visuals/ep10_visual_prompts_v01.md` — 4 environment reference prompts (REF A toppled-∞ stone meadow, REF B crossroads+staff, REF C ridge Moon-Sun sky, REF D dawn town street, each with an Environment Geometry note) + **40 scene prompts** covering 34 scenes (Mode B / match-cut splits: S02a/b, S08a/b/c, S10a/b, S27a/b, S34a/b). S35 = edit card (GitHub end screen, no image). Body ref = `android_kintsugi.png` (Phase 3, chain every scene); S01-S02 exterior chains from EP09 dawn frames.
**Disciplines enforced:** Companion Camera (reserved beside-space, never above him) · single Amber Pulse at S10 only (reflected sunlight; embers orange-red) · eye canon ADR-0010 (material-lens idiom, no glow) · **mouthless-face guard** (no smile/mouth anywhere, esp. S34) · gaze discipline (direct lens eye-contact ONLY at S34a; S27/S31 below/beside the lens) · ASCII/plain-English text prompts (ADR-0006) · ART DIRECTION LOCKS section (EP07-10 requirement) · reference-first (ADR-0007).
**Validation:** every prompt ends with mandatory suffix + `16:9 widescreen composition` · no forbidden aesthetics · anti-spawn guard (`single figure composition, no additional characters`) on solo full-body scenes, omitted for macro/foot + intentional multi-figure (S07/S11/S12/S21/S25/S26/S28).
**Next step:** Fibula reviews prompts → generate 4 refs + Framing Pass → scene images in Nano Banana (attempts.md ledger mandatory — last first-pass-yield window) → select → **Motion Script** (Checkpoint 2). Highest-risk shots: S16 (celestial bodies + flock), S25 (children staging), S27b (gaze), **S34a/b (most important pair — mouthless guard, only eye-contact frame)**.

---

## EP10 DRAMATURGY SESSION (2026-07-06) — SUMMARY

**Task:** Generate EP10 dramaturgy scene breakdown from approved concept notes (the Dawn Walk) + musical metadata.
**Deliverable:** `episode-10/03_direction/ep10_dramaturgy_v01.md` — 35 scenes (34 image-generated + 1 edit card S35), 4:34 (274s), 9 musical sections, all 12 concept overrides realized and marked.
**Key structure:** Intro (world-first / shutter opens / threshold) → V1-V3 town walk (first footstep on first stomp-clap, duality objects, faces + fractal rhyme, waymark staff Amber Pulse, steadfast souls) → 60s break on the ridge (Moon-Sun sky, crane flock, far-slope destination plant) → V4-V5 descent (tower distant, loops powerless, embers, binary stripes, gold seam, descent lands on "Piercing the peaks") → V6 meadow (toppled-∞ ordinary, two glasses one pot, THE HAND) → Finale (tracks, 3 refrains, THE WAIT grammar break, scream = peak, THE LOOK Still Hold, gong = GitHub end screen).
**Interpretation choices flagged for Fibula:** (1) communal shepherd's kettle on embers as the tea source (avoids carried-prop continuity, echoes S21 embers), (2) travelers' cloth strips on the staff, (3) S33 scream energy = wind/flare/dew (no birds — spawn risk), (4) refrain onsets estimated inside the 79s finale (to confirm on final track).
**Also fixed:** master.md Language Arc header drift (EP10 "Spoken Word" → sung, commit 2f47d52); project_metadata.json ep10 dramaturgy=true (state-machine sync — validation suite green, 10/10 groups).
**Next step:** Fibula reviews and approves dramaturgy (gate-1 → approvals.json entry with sha256) → visual prompts in a NEW session (reference-first: 4 refs before any scene image).
**UPDATE (same day):** APPROVED 2026-07-06 with one revision, applied immediately — S34 "The Look" became "The Look and the Beckon": the held look resolves into a soft head tilt (the machine's smile — face verified mouthless against `android_kintsugi.png`; literal smile would invent a mouth = design break) + one open-palm beckon toward the lens; gong cuts on the offered hand. Propagated to concept notes Override 12 (+ three-beats section). Gate-1 recorded (sha256 e48833b9…); gate-0 concept sha re-baselined (535c74b2…). NEXT SESSION: "Generate visual prompts for EP10" (reference-first).

---

## EP10 CONCEPT SESSION (2026-07-06) — SUMMARY

All 8 open questions from the finale panel RESOLVED with Fibula. Committed:
- `episode-10/01_lyrics/ep10_lyrics_v01.md` — answer-poem lyrics + Suno style (canon drift #1 fixed)
- `project_metadata.json` EP10: lyrics/music true, status in_production (drift #2 fixed)
- `master.md` EP10 entry: sung answer-poem replaces "Spoken Word / Music TBD" (drift #3 fixed)
- `episode-10/03_direction/ep10_concept_notes.md` — **THE DAWN WALK** full blueprint

Key decisions: single continuous dawn walk (workshop → toppled-∞ meadow) · prophecy-not-arrival
(stone 8 fell long ago, lies as ordinary ∞) · three-beat fourth wall (tea to camera → the look →
gong = GitHub in-video end card, S35) · Companion Camera = reserved-beside-space constitution + behavior set ·
Mentor = waymark staff (single Amber Pulse) · Robochica FULLY withheld · apple withheld → twin tea
glasses + side-by-side tracks · crane flock in Moon-Sun sky (break).

### NEXT: EP10 PIPELINE
- [x] **Fibula approves concept notes** — APPROVED 2026-07-06, on one condition (Brecht claims expert-verified). Condition met same day: two-agent panel (scholar + adversarial refuter, cited sources). Verdict: radio-theory/open-apparatus claim CONFIRMED (strongest); tea gesture reframed as hospitality-first ("Brechtian device, un-Brechtian warmth"); Mechanic relabeled Bruegel-ploughman-via-Auden; Brecht added to master.md Universal Narrative Bridges.
- [x] Musical metadata JSON — DONE 2026-07-06: 9 sections, 274s (4:34), E Minor, 153 BPM double-time (felt half-time pulse 76.5 — the answer walks at EP01's ~75). Finale = guitar solo + refrain rising ×3 (straight/elongated/scream). Saz→guitar corrected across canon.
- [x] Stone-8 references RECOVERED (2026-07-06) — originals found by Fibula: `_curation_staging/ep01/61-63-64.png` (full-res, local); curated copies committed as `ep01_s51/s71/s72` frames. Video-screenshot plan obsolete.
- [x] Dramaturgy session (SEPARATE, max effort) — v01 GENERATED 2026-07-06 (35 scenes)
- [x] **[CHECKPOINT]** Fibula approves dramaturgy — APPROVED 2026-07-06 with one revision applied same day (S34: the look resolves into a warm head-tilt + open-palm beckon; mouthless-face guard added; propagated to concept notes Override 12). Gate-1 recorded in approvals.json (sha256-pinned; gate-0 concept sha re-baselined for the Override 12 revision). All 4 interpretation choices confirmed.
- [x] `ep10_visual_prompts_v01.md` — GENERATED 2026-07-06 (40 scene prompts + 4 env refs; see EP10 VISUAL PROMPTS SESSION summary above)
- [ ] Reference-first: generate REF A-D (toppled-∞ meadow, crossroads+staff, ridge Moon-Sun sky, dawn street) + Framing Pass BEFORE any scene image
- [ ] Image generation (Nano Banana) → select → attempts.md ledger + sync-QC mandatory during production
- [ ] `ep10_motion_script_v01.md` — after image selection (Checkpoint 2: human approval before video gen)

---

## REPO-READINESS PROGRAM — COMPLETED (2026-07-05)

10-lens final rescore: **4.22 → 4.80 (+0.58)**. 9/10 lenses report "in-scope remaining: none".
All 9 workstreams delivered (16 thematic commits). Report: `_private/audit_2026-07/repo_readiness_rescore.md`.

| Lens | Before | After | Delta |
|---|---|---|---|
| Dramaturg | 4.6 | 4.9 | +0.3 |
| Solution Architect | 4.6 | 4.9 | +0.3 |
| Film Director | 4.6 | 4.9 | +0.3 |
| AI Systems | 4.5 | 4.8 | +0.3 |
| OS Maintainer | 4.5 | 4.8 | +0.3 |
| Art Director | 4.5 | 4.9 | +0.4 |
| Music Director | 4.6 | 4.9 | +0.3 |
| DevOps | 4.4 | 4.8 | +0.4 |
| External Skeptic | 2.5 | 4.5 | +2.0 |
| OSS Community | 3.4 | 4.6 | +1.2 |

Remaining 0.20 to 5.0 = EP10 film + post-launch community proof + time.
**Next:** EP10 brainstorming session + launch outreach prepared (private working files).

---

## SESSION PAUSE NOTE (2026-07-05, usage limit)

Committed: WS1 40def70 (doc-rot sweep + architecture v3.0 + metadata sync + doc-reference
lint, 9th check group) · WS2-gates 128a770 (approvals.json, disk/metadata state machine,
M4 real fix, 79 meta-tests) · WS8 e3cd13d (community files) · WS-H 3dc446b
(hallucinating-camera.md + S30 case; tutorial TAKE 06 is local-only, _tutorial gitignored).

**IN FLIGHT when paused — 3 subagents were editing the working tree; their changes may be
partial and UNCOMMITTED. Next session MUST start with: git status + python tests/run_all.py,
audit the diffs, then commit thematically:**
- W2c: motion/music validators (camera 5-clip window + accent budget + personality,
  energy->motion heuristic, EP08 overlay convention)
- W9: release runbook (private) + release-engineering decision record + create_episode.yml PR flow + CI job summary
- W6: DONE (uncommitted) — _templates/ep_sync_qc_template.md + scripts/sync_probe.py +
  tests/attempts_report.py + pipeline_rules 2.6 + capcut SKILL xref. FLAGGED for next
  session: add "sync_qc": r"^ep\d{2}_sync_qc_v\d{2}\.md$" pattern to naming_check.py
  (+ meta-test) BEFORE the first real EP09 sync-QC record lands, or naming gate will FAIL it.

Fibula decisions RESOLVED: release-engineering posture documented via ADR after W9's
sensitivity check · curated frames = YES full set (<15MB, curation
WITH Fibula — interactive) · episode guide = README section.

Remaining waves: canon/style bundle (eye ADR-0010 + suffix v2 ADR-0009) -> WS7 fork path
(FORKING.md + toy-universe dry-run) -> WS4/5 showcase (README v2, visual-canon, frames
curation) -> Fable verification pass -> panel re-score. EP10 session separately
(_private/ep10_first_thoughts.md ready).

---

## CURRENT PRIORITY: REPO-READINESS PROGRAM (2026-07-05)
> Source: 10-lens expert panel (path-to-5.0). Full roadmap: `_private/audit_2026-07/path_to_five_roadmap.md`.
> EP10 items deferred to a dedicated session — first thoughts at `_private/ep10_first_thoughts.md`.
> Execution model: Fable organizes/audits; mechanical work delegated to Opus 4.8 / Sonnet 5 subagents.

- [x] **WS1 — Docs match reality 1:1** ✅
- [x] **WS2 — Validator & gate completion** ✅
- [x] **WS-H — Reshoot honesty** ✅
- [x] **WS8 — Community surface** ✅
- [x] **WS7 — FORKING.md golden path** ✅
- [x] **WS9 — Release engineering** ✅
- [x] **WS6 — Telemetry** ✅
- [x] **WS4 — Public showcase** ✅
- [x] **WS5 — Method docs** ✅
- [x] **Closing ritual:** 10-lens panel re-score completed → 4.80/5.0 → repo-readiness DONE

---

## LAUNCH STATUS (EP01-EP07 launched)

EP01 launched on YouTube 2026-04-22; EP02-EP07 followed on the weekly cadence.
Channel (@fibuladev) and Instagram set up; per-episode YouTube packages, social
atomization, launch checklists, and walkthroughs are in each `episode-XX/07_social_media/`.
Detailed community-sharing and launch playbooks live in the creator's private notes
(not part of the open method).

---

## PREVIOUS PRIORITY: INFRASTRUCTURE COMPLETION
> Target: Complete before Claude Code activation (2026-02-23)

### ✅ COMPLETED TODAY
- [x] `master.md` — Universe Canon v2.0 written
- [x] `pipeline_rules.md` — v2.0 written
- [x] `naming_convention.md` — v2.0 written
- [x] `architecture.md` — v2.0 written
- [x] `project_metadata.json` — v2.0 written, all 10 episodes
- [x] `character_profiles.json` — v2.0 with Robochica, phase visual states
- [x] `dramaturgy_template.md` — v2.0 written
- [x] `visual_prompt_template.md` — v2.0 written
- [x] `video_prompt_template.md` — v2.0 written
- [x] `.gitignore` — expanded with raw folders and secrets
- [x] `CLAUDE.md` — Claude Code session context written
- [x] `_memory/lessons.md` — Self-improvement loop initialized
- [x] `_memory/decisions_log.md` — Foundation decisions logged
- [x] `_memory/todo.md` — This file

### ✅ COMPLETED (2026-02-23 Session)
- [x] `docs/` skeleton — getting-started, skills-guide, tools-setup
- [x] `CHANGELOG.md` — repo root
- [x] `.github/ISSUE_TEMPLATE/` — bug report + feature request templates
- [x] `.github/pull_request_template.md`
- [x] `CONTRIBUTING.md` skeleton

### ✅ COMPLETED (2026-02-24 Session)
- [x] `_skills/robotiko-dramaturgy/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-visual-prompts/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-motion-script/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-episode-scaffold/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-naming-enforcer/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-youtube-packager/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-reels-atomizer/SKILL.md` — v1.0 written
- [x] `_skills/robotiko-launch-orchestrator/SKILL.md` — v1.0 written

### ✅ COMPLETED (2026-02-25 Session)
- [x] Full repo audit (DevOps + Claude capabilities — dual-angle review)
- [x] P0 fix: `project_metadata.json` skills status updated to `all_skills_v1.0_complete`
- [x] P0 fix: `pipeline_rules.md` added to CLAUDE.md mandatory reads (item #5)
- [x] P0 fix: Extended Thinking Protocol added to CLAUDE.md (workflow rule #7)
- [x] `tests/naming_check.py` — v1.0 implemented (full validation logic)
- [x] `tests/visual_prompt_validator.py` — v1.0 implemented (suffix, character phase, forbidden aesthetics)
- [x] `tests/naming_check_hook.py` — v1.0 implemented (lightweight hook for Claude Code) (removed 2026-07-04 — hook never fired; CI naming_check.py --full is the real gate)
- [x] `.claude/settings.json` — PostToolUse hook configured (bash-based, no Python dependency) (removed 2026-07-04 — hook never fired; CI naming_check.py --full is the real gate)
- [x] `MEMORY.md` — Auto-memory file created for session continuity
- [x] `tests/README.md` — Updated to reflect v1.0 implementations

---

## NEXT: EP02 PRODUCTION
> Unblock after infrastructure is complete

- [x] `ep02_concept_notes.md` — Concept notes written (must-have shots, overrides, mood)
- [x] `ep02_musical_metadata.json` — Musical metadata added to episode-02/02_music/
- [x] `ep02_lyrics_v01.md` — Lyrics added to episode-02/01_lyrics/
- [x] `ep02_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-02-26
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-02-26
- [x] `ep02_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-02-26
- [x] Image generation — Nano Banana ✅
- [x] Human selects images ✅ (41 selected images including 6 keyframe pairs)
- [x] `ep02_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script) ✅ 2026-02-27
- [x] **[PIPELINE FIX]** Duration Coverage Strategy — architecture-level fix across 7 files ✅ 2026-02-27
- [x] `ep02_motion_script_v02.md` — Full rewrite with duration coverage (49 clips, 100.4% coverage) ✅ 2026-02-27
- [x] **[CHECKPOINT]** Human approves motion script v02 ✅ 2026-02-28
- [x] Tool Assignment Plan — 49 clips assigned: Kling=36, Veo=4, Seedance=9 ✅ 2026-02-28
- [x] `ep02_motion_script_v02.md` — Updated with `| Recommended Tool |` field per clip + Tool Assignment Summary section ✅ 2026-02-28
- [x] Pipeline update: Seedance 1.0 adopted + Multiframes (SKILL.md v1.2, template v5.0, pipeline v2.2) ✅ 2026-03-01
- [x] **EP02 Seedance Test Protocol** — Multiframes tested: **FAIL** (1130cr / 2 tests, budget-destroying) ✅ 2026-03-01
  - [ ] Test 1: S04 — Seedance 1.0 vs Kling (Mode A quality comparison)
  - [ ] Test 2: S11 — Seedance 1.0 vs Kling (Mode B keyframe comparison)
  - [x] Test 3: S14(a+b+c) — Multiframes vs 3 individual clips — **KILLED** (~565cr/generation) ✅ 2026-03-01
  - [ ] Test 4: S08 — Seedance 1.0 map shot (1080p vs former 720p plan)
- [x] Post-test decision: **No Multiframes** — removed from pipeline entirely ✅ 2026-03-01
- [ ] EP02 tool reassignment (Seedance 1.0 tests 1/2/4 still pending)
- [ ] Human generates 2 supplementary images (S29c, S34b) from inline prompts
- [ ] Video generation — per updated tool assignment
- [ ] Human selects video clips
- [ ] Final edit — CapCut

### 2026-03-18 Session Summary (CapCut Post-Production Setup)
**Task:** Set up CapCut Desktop post-production pipeline for EP02.
**Completed:**
- [x] Kodachrome LUT imported (Presetpro - Kodachrome 64.cube) → Adjustment Layer, intensity 80%
- [x] Film Grain effect added (Effects → "Grain") → Adjustment Layer, texture 10
- [x] Letterbox 2.35:1 activated (Player → Ratio → 2.35)
- [x] All video clips + music (episode-2.1.wav) imported to timeline
**Pending for tomorrow (2026-03-19):**
- [ ] Audio-video sync — align clip boundaries to musical beats using motion script timestamps
- [ ] S01 re-generation via Veo (original was 5s, needs 8s+ for speed ramp coverage)
- [ ] Vignette effect (Effects → "Vignette" → ~20%)
- [ ] Selective effects (chromatic aberration on S07, S11, S23, S28, S32)
- [ ] Speed ramp adjustments on applicable clips (S01-S03, S13, S15, S16, etc.)

### 2026-02-27 Session Summary (Duration Coverage Fix)
**Problem:** Motion script v01 had 39% duration coverage (175s video for 448s music). Pipeline assumed 1 scene = 1 clip.
**Solution:** Created Duration Coverage Strategy (Direct / Speed Ramp / Multi-Clip). Updated 7 pipeline files + rewrote motion script.
**Files updated:** pipeline_rules.md, motion-script SKILL.md, visual-prompts SKILL.md, video_prompt_template.md (v3.0), naming_convention.md, lessons.md
**Deliverable:** ep02_motion_script_v02.md — 49 clips, 450s generated, 100.4% coverage, 2 supplementary images needed (S29c, S34b)

### 2026-02-28 Session Summary (Tool Assignment Plan)
**Task:** Assign AI video generation tool to each of 49 clips based on tool capabilities, credit budgets, and quality requirements.
**Tool inventory:** Kling AI Pro (3000 cr, 1080p, keyframe), Google Veo (free, 8s fixed, no keyframe), Seedance (1200 cr, 720p, keyframe)
**Assignment strategy:** Mode B → Kling only (6 clips). Map shots → Seedance (9 clips, 720p OK on textures). 8s scene match → Veo (4 clips). Everything else → Kling (30 clips).
**Credit budget:** Kling 2,275/3,000 (725 buffer). Seedance ~540/1,200 (660 buffer). Veo free.
**Files updated:** ep02_motion_script_v02.md (added Tool Assignment Summary + Recommended Tool per clip), _memory/todo.md
**Next steps:** Generate 2 supplementary images (S29c, S34b), then begin video production per tool assignment.

### 2026-02-28 Session 4 Summary (Tool Assignment Pipeline Integration)
**Task:** Make tool assignment logic permanent across pipeline — not just EP02-specific.
**Files updated:** robotiko-motion-script/SKILL.md (v1.1: Step 7 + Output Format + Checklist), video_prompt_template.md (v4.0: Tool Assignment Summary + Recommended Tool fields), pipeline_rules.md (v2.1: Step 8c + Step 9 update)
**Result:** EP03+ motion scripts will automatically include tool assignments as standard output.

### 2026-03-01 Session 5 Summary (Seedance Integration + Multiframes Discovery)
**Discovery:** Human found Seedance 1.0 (CapCut built-in, 1080p, keyframe, 25cr/5s, 50cr/10s) for keyframe video + Seedance Multiframes (up to 10 keyframes, up to 54s continuous video, AI interpolation).
**Pipeline update:** Seedance → Seedance 1.0 across all pipeline files. Multiframes added as experimental Mode C.
**Files updated:** SKILL.md (v1.2), video_prompt_template.md (v5.0), pipeline_rules.md (v2.2), project_metadata.json
**Strategy:** Test-first approach — 4 EP02 test clips before reassignment decision (S04, S11, S14, S08).
**Commits pending:** Previous session's tool assignment integration + this session's Seedance update.

### 2026-03-01 Session 6 Summary (Multiframes Killed + Pipeline Cleanup)
**Test result:** Multiframes consumed ~565 credits per generation (1130cr for 2 tests). Monthly CapCut Pro budget is 1200cr — 2 tests nearly exhausted it.
**Decision:** Multiframes permanently removed from pipeline. Seedance 1.0 stays as a viable tool alongside Kling + Veo.
**Files updated:** SKILL.md (v1.3), pipeline_rules.md (v2.3), video_prompt_template.md (v5.1), project_metadata.json, lessons.md, MEMORY.md
**Remaining tests:** Seedance 1.0 single-clip tests (S04 Mode A, S11 Mode B, S08 map shot) still pending.
**Commits pending:** Session 4 + 5 + 6 combined.

---

## NEXT: EP03 PRODUCTION

- [x] `ep03_lyrics_v01.md` — Lyrics added to episode-03/01_lyrics/
- [x] `ep03_musical_metadata.json` — Musical metadata added to episode-03/02_music/
- [x] `ep03_concept_notes.md` — Concept notes written (brainstorming session 2026-03-07)
- [x] `ep03_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-03-10
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-03-10
- [ ] `ep03_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts)
- [ ] Image generation
- [ ] Human selects images
- [ ] `ep03_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script)
- [ ] **[CHECKPOINT]** Human approves motion script
- [ ] Video generation
- [ ] Final edit — CapCut

### 2026-03-07 Session Summary (EP03 Brainstorming + Concept Notes)
**Task:** Brainstorm creative direction for EP03 dramaturgy before writing.
**Key decisions:** Spoken intro = Mentor-Robotiko argument in house + model selection screen (anti-guru thesis). Left-liberal group only in intro+V1. Locations: East=village wedding, North=Trabzon road rage, South=Alanya nightclub scam, Istanbul=miniature bridge + metrobus. Finale=industrial-estate welder with grease IV. Mentor in chorus=amber light presence only. EP02 ear damage carries, no new permanent damage. Instrumental breaks=transition montages.
**Deliverable:** `episode-03/03_direction/ep03_concept_notes.md` — complete with all must-have shots, creative overrides, mood notes.
**Next step:** Create dramaturgy v01 in a new session.

### 2026-03-10 Session Summary (EP03 Dramaturgy v01)
**Task:** Generate EP03 dramaturgy scene breakdown from approved concept notes + musical metadata.
**Deliverable:** `episode-03/03_direction/ep03_dramaturgy_v01.md` — 40 scenes, 8:44 (524s), full coverage.
**Key structure:** 5 spoken intro scenes (argument + model screen), 6 geographic trial locations (city/east/north/south/occult-charlatan den/Istanbul), 5 finale scenes (industrial estate + grease IV). Mentor hybrid presence (physical bookends, amber atmospheric in choruses). Left-liberal group intro+V1 only.
**Flagged for review:** S04 text legibility, S23 receipt comedy balance, S33-S34 miniature bridge, S38 two-plane composition.
**Next step:** Human reviews and approves dramaturgy → then visual prompts in a new session.

### 2026-03-10 Session 2 Summary (EP03 Dramaturgy Review + Approval)
**Task:** Human review of EP03 dramaturgy v01 — corrections and approval.
**Corrections applied:** (1) S01: "Anatolian house" → "modest house, their shared home" (they haven't traveled yet). (2) S23: receipt river removed, rewritten as tout-to-nightclub transition scene. (3) S26: receipt river + MIB consolidated here (V4a lyrics). (4) S24: stale "receipt in hand" reference removed. (5) Robotiko Visual State: "pristine" → EP02 cumulative damage (missing ear, torso dent, shoulder scratches). (6) Director's Notes: "pristine everywhere except ear" corrected.
**Infrastructure updates:** `character_profiles.json` Phase 1 visual_prompt_addition split into `ep01` (pristine) and `ep02_ep03` (battle-scarred). Lesson added to `lessons.md`: cumulative damage rule.
**Production estimate:** ~50-52 video clips for 524s coverage (similar ratio to EP02's 49/448s).
**Status:** Dramaturgy APPROVED ✅. Ready for visual prompts in a new session.
**Next step:** `ep03_visual_prompts_v01.md` — generate in new session (skill: robotiko-visual-prompts).

---

## NEXT: EP04 PRODUCTION

- [x] `ep04_lyrics_v01.md` — Lyrics added to episode-04/01_lyrics/
- [x] `ep04_musical_metadata.json` — Musical metadata added to episode-04/02_music/
- [x] `ep04_concept_notes.md` — Concept notes written
- [x] `ep04_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-03-22
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-03-23
- [x] `ep04_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-03-23
- [x] Image generation ✅ (54 images in raw/, all reviewed)
- [x] Human selects images ✅ (images reviewed, to be moved from raw/ to selected/)
- [x] `ep04_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script) ✅ 2026-03-29
- [x] **[CHECKPOINT]** Human approves motion script ✅ 2026-03-31 (17 videos generated, quality confirmed)
- [ ] Video generation (remaining clips)
- [ ] Final edit — CapCut

### 2026-03-22 Session Summary (EP04 Dramaturgy v01)
**Task:** Generate EP04 dramaturgy scene breakdown from approved concept notes + musical metadata.
**Deliverable:** `episode-04/03_direction/ep04_dramaturgy_v01.md` — 44 scenes, 7:03 (423s), full coverage.
**Key structure:** 3-act structure (Return & Testimony / Cosmic Journey & Sacred Law / Temptation, Hammer & Awakening). Robotiko fully passive — only movement is final head-lift (S44). Mentor as sole protagonist. Historical montage across 4 eras (S16-S19) with Young Mentor aging. S20 = Piercing the Veil / Kindred Souls (enlightened figures, amber eyes — inner sight open). S21 = Film-within-film (nested frames showing the deceiver/deceived cycle, echoes of S16-S19, Mentor the only awake figure). Moon/Sun transformation (S22-S23) with staff materialization. Devil = black smoke + spiral horns (S27-S29). Hammer scene (S31-S34): real, heavy, amber glow only at swing. Second tea glass as emotional anchor (6 appearances). Amber = truth color DNA (staff → Kindred Souls' eyes → Sun → TRUTH → hammer → eyes).
**Flagged for review:** S04 tea glass detail, S16-S19 Young Mentor consistency, S20 Kindred Souls amber eyes + reference image, S21 nested frames readability, S23 Sun transformation, S27-S28 smoke+horns, S34 ego shatter, S44 eye color change.
**Next step:** Human reviews and approves dramaturgy → then visual prompts in a new session.

### 2026-03-23 Session Summary (EP04 Visual Prompts v01)
**Task:** Generate EP04 visual prompts from approved dramaturgy (44 scenes).
**Deliverable:** `episode-04/04_visuals/ep04_visual_prompts_v01.md` — 48 prompts (44 scenes, 4 keyframe pairs: S03, S30, S34, S44) + 4 reference images.
**Reference images created:** (1) REF-ENV-01: Mentor's Room interior, (2) REF-CHAR-01: Young Mentor (clean-shaven, for vision sequences), (3) REF-CHAR-02: Kindred Souls (wandering ascetic, philosopher, healer, sage with amber eyes), (4) REF-ENV-02: Sunlit Moon Surface.
**Key tracking:** Young Mentor aging across S16-S34 (clean-shaven → stubble → thin beard → fuller beard → middle-aged). Staff chronology correct (no staff in visions S16-S33, born at S34, present in room S35+). Amber DNA maintained throughout. Devil = smoke + horns only. Robotiko passive (Phase 2: rusted, cracked, sparking, glitching). Only movement = S44 head-lift.
**Validation:** 52 prompts with suffix ✅, 52 with 16:9 ✅, no "pristine" in prompts ✅, no character names in prompts ✅.
**Next step:** Human generates reference images first → then scene images in Nano Banana → select → motion script in new session.

### 2026-03-29 Session Summary (EP04 Motion Script v01)
**Task:** Generate EP04 motion script from approved dramaturgy (44 scenes) + selected images (54 in raw/).
**Deliverable:** `episode-04/05_video/ep04_motion_script_v01.md` — 45 clips (44 scenes + 1 multi-clip sub-clip for S37).
**Coverage:** 405s generated / 423s music = 95.7%. 18 Speed Ramp clips, 1 Multi-Clip (S37: 2 sub-clips), 4 Mode B (S03, S30, S34, S44).
**Tool assignment:** Kling 25 clips (~1575cr est., 47.5% buffer), Seedance 20 clips (850cr, 29.2% buffer). No Veo.
**Key decisions:** (1) Average MS ~4.0 — lower than Destruction norm, justified by 56 BPM meditative tone. (2) S32-S33-S34 triple peak (MS 7-8-8) justified as climax. (3) S36/S39 share S35's image (visual prompt merges). (4) S37a/S37b share S37's image (different camera moves). (5) 0 supplementary images needed.
**Post-gen validation:** 45 video suffixes ✅, 45 anti-spawn guards ✅, 45 camera moves ✅, no character names in motion prompts ✅, coverage ≥95% ✅.
**Next step:** Human reviews and approves motion script → then video generation begins.

---

## NEXT: EP05 PRODUCTION

- [x] `ep05_lyrics_v01.md` — Lyrics complete
- [x] `ep05_musical_metadata.json` — Musical metadata complete
- [x] `ep05_concept_notes.md` — Concept notes written ✅ 2026-03-31
- [x] `character_profiles.json` — Robochica visual design finalized ✅ 2026-03-31
- [ ] Robochica master reference image (`ref_robochica_master.png`) — Generate + human approve
- [ ] Environment reference images (retro-futuristic supermarket, office, café, street) — Generate + human approve
- [x] `ep05_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-03-31 (32 scenes, 267s, 100% coverage)
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-03-31
- [x] `ep05_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-04-02 (41 prompts: 8 ref + 33 scene)
- [x] Image generation ✅ 2026-04-02 (33 scene images + 8 reference images generated in Nano Banana)
- [x] Human selects images ✅ 2026-04-02 (all reviewed and approved)
- [ ] `ep05_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script)
- [ ] **[CHECKPOINT]** Human approves motion script
- [ ] Video generation
- [ ] Final edit — CapCut

### 2026-04-02 Session Summary (EP05 Visual Prompts + Image Generation)
**Task:** Generate EP05 visual prompts and all scene images.
**Deliverable:** `episode-05/04_visuals/ep05_visual_prompts_v01.md` — 41 prompts (8 reference + 33 scene, including S15a/S15b keyframe split).
**Reference images:** REF-CHAR-01 (Robochica — 3 iterations, dark amber glass lens eyes fix), REF-CHAR-02 (Elderly Robot Couple), REF-ENV-01-06 (Supermarket, Street, Cafe, Office, Iron Vault, Room).
**Key fixes during production:** (1) Robochica eyes: "amber glow" → "dark amber glass lenses" (3 attempts, final working formula). (2) Cathedral → "colossal iron vault" (no religious connotation). (3) Office: narrow corridor → wide plaza floor. (4) robochica_1 tattoo: chest → inner forearm (clean surface, EP06 _2/_3/_4 preparation). (5) Cem Karaca poster: originally planned as post-production composite, ABANDONED 2026-04-06 — all AI tools refused compositing, plan pivoted to YouTube description + outro credit card.
**All 8 human overrides implemented:** S05 (both in frame), S07 (drool), S11 (elderly couple), S13 (forearm tattoo), S15a/b (hacker mask + cloud), S22-S23 (folders), S24 (red body), S28 (eye projection).
**Image review:** 33/33 approved. 0 critical issues. 4 minor CapCut post-production adjustments noted.
**Next step:** Motion script in new session.

### 2026-03-31 Session Summary (EP05 Dramaturgy Planning + Concept Notes)
**Task:** Plan EP05 dramaturgy — "First Love / Blue Screen" (highest viral potential episode).
**Key decisions:** (1) Robochica: amber/gold eyes (EP04 truth-color irony), warm gold/copper wires, fractal shoulder pattern, mirror principle (max 3 face-on shots). (2) Locations: multiple retro-futuristic everyday (market, office, street, café) — each encounter closer. Syd Mead aesthetic. (3) Mentor: amber echoes ONLY, no image. (4) Tonal shift: pure surprise at 3:24, zero dark hints before.
**Human overrides (8):** (1) Both in frame for "walk so slow" (2) Drool effect for "twin reactors" (3) Elderly robot couple for "dead father" line (4) robochica_1 tattoo → seeds EP06's _2,_3,_4 (5) Hacker mask + physical cloud with data center (6) Windows folders thrown aside (7) Bright red overheating body (8) Eye projection EP03 callback in outro.
**Deliverables:** `character_profiles.json` updated (Robochica design complete), `ep05_concept_notes.md` written (full creative direction + 8 human overrides + 12 creative rules).
**Next step:** Generate dramaturgy v01 (this session or next).

---

## NEXT: EP06 PRODUCTION

- [x] `ep06_lyrics_v01.md` — Lyrics complete
- [x] `ep06_musical_metadata.json` — Musical metadata complete ✅ 2026-05-01
- [x] `ep06_concept_notes.md` — Concept notes written and approved ✅ 2026-05-01
- [x] `ep06_dramaturgy_v01.md` — Claude generates (skill: robotiko-dramaturgy) ✅ 2026-05-01 (43 scenes, 451s, 8 human overrides)
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-05-01
- [x] `ep06_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-05-01 (47 prompts: 2 env ref + 45 scene)
- [x] `ep06_visual_prompts_v02.md` — Radical simplification for ref-image compatibility ✅ 2026-05-01 (45 scene prompts, 1-3 sentences each)
- [x] Reference images: REF-ENV-01 (Cold Office) ✅, REF-ENV-02 (Meeting Room) ✅ — already generated. Perfect Worker = existing ref_robotiko_master.png
- [x] Image generation — Nano Banana ✅
- [x] Human selects images ✅
- [x] `ep06_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script) ✅ 2026-05-02 (45 clips, 98.7% coverage)
- [x] **[CHECKPOINT]** Human approves motion script ✅
- [x] Video generation ✅ 2026-06-03 (all clips generated)
- [x] `ep06_capcut_guide_v01.md` — CapCut editing guide generated ✅ 2026-06-03 (45 clips, 19 speed ramps, 16 beat sync points, 1 light leak, 2 chromatic aberration)
- [ ] Final edit — CapCut (IN PROGRESS)

### 2026-05-01 Session Summary (EP06 Dramaturgy v01)
**Task:** Generate EP06 dramaturgy scene breakdown from approved concept notes + musical metadata.
**Deliverable:** `episode-06/03_direction/ep06_dramaturgy_v01.md` — 43 scenes, 7:31 (451s), 134 BPM, B Minor.
**Key structure:** Single-location discipline — 90% in EP05's office with warmth stripped. Three-refrain camera escalation (S09 wide → S15 medium → S21 close-up). Perfect Worker = new character (pristine titanium mirror of Robotiko). Chorus contrast (soaring rock anthem + dead desk labor). Mentor amber echoes thinner than EP05 (S19 eye flash, S33 ceiling strip). robochica_1-4 tattoos visible in intro (S03). The Exit (S38) = first voluntary departure in the series. The Collapse (S41) = Perfect Worker's first crack. Guitar solo (S42-S43) = slow zoom out over empty workspace.
**8 human overrides implemented:** S03 (tattoo reveal), S07 (Perfect Worker intro), S09/S15/S21 (three-refrain escalation), S23 (dead soul at desk), S30 (no literal fire), S38 (the exit), S41 (the collapse), S42 (guitar solo wide).
**Mode B candidates flagged:** S38 (the exit — walking + worker head turn), S41 (the collapse — seated → knees).
**Reference images needed:** 1 (Cold Office environment only — Perfect Worker = existing ref_robotiko_master.png).
**Next step:** Human reviews and approves dramaturgy → then visual prompts in a new session.

### 2026-05-01 Session 2 Summary (EP06 Visual Prompts v01)
**Task:** Generate EP06 visual prompts from approved dramaturgy (43 scenes).
**Deliverable:** `episode-06/04_visuals/ep06_visual_prompts_v01.md` — 47 prompts (2 environment references + 45 scene prompts, including 2 Mode B pairs).
**Reference images created:** (1) REF-ENV-01: Cold Office (EP05 office with warmth stripped, cold fluorescent, green CRT), (2) REF-ENV-02: Meeting Room (glass walls, large dark flat screen, 1-to-1 configuration for S36 mirror scene). No character reference needed — Perfect Worker uses existing `ref_robotiko_master.png`.
**Key design decisions:** (1) Both characters share same ref image (ref_robotiko_master.png). Differentiation via prompt language only: "damaged chrome android" vs "pristine chrome android." (2) Amber restricted to 3 scenes: S03 (tattoo etchings), S19 (single eye flash), S33 (faint ceiling strip). (3) S30-S31 smoke/haze is real and visible, normalized with air freshener canister — EP02 Bangladesh echo. (4) S32 collapsed robots in background, out of focus but visible. (5) S34 fear is operational (eye widening, jaw tightening), not philosophical.
**Mode B pairs:** S38a/S38b (the exit — Robotiko near→far, worker head turn), S41a/S41b (the collapse — seated→knees, first crack). S38 flagged for potential Mode B→Mode A downgrade due to dual action risk.
**Validation:** 47 suffixes ✅, 47 16:9 ✅, 0 character names in prompts ✅, 0 forbidden aesthetics ✅, amber in S03/S19/S33 only ✅.

### 2026-05-01 Session 3 Summary (EP06 Visual Prompts v02 — Radical Simplification)
**Task:** Revise EP06 visual prompts after user feedback that v01 prompts were too verbose and competed with reference images in Nano Banana.
**Problem:** When uploading character ref + environment ref + detailed text prompt, Nano Banana couldn't reconcile 3 information sources → wrong angles, wrong framing, characters facing camera instead of desk.
**Solution:** Created v02 with radically simplified prompts (1-3 sentences before suffix). Added Reference Image Upload Guide (per-scene ref instructions) and Camera Angle Rule (explicit rear/profile angles for desk scenes).
**Deliverable:** `episode-06/04_visuals/ep06_visual_prompts_v02.md` — 45 scene prompts (env refs removed since already generated).
**Lesson added:** `_memory/lessons.md` — REFERENCE IMAGE WORKFLOW category (prompt brevity, camera angle fix, upload guide).
**Status:** v02 written, awaiting user testing with Nano Banana.
**Next step:** User tests v02 prompts → confirm working → image generation → select → motion script in new session.

### 2026-05-02 Session Summary (EP06 Motion Script v01)
**Task:** Generate EP06 motion script from approved dramaturgy (43 scenes) + visual prompts v02/v03.
**Deliverable:** `episode-06/05_video/ep06_motion_script_v01.md` — 45 clips (41 single + 2 Multi-Clip pairs for S42, S43).
**Coverage:** 445s generated / 451s music = 98.7%. 19 Speed Ramp clips, 2 Multi-Clip scenes (S42: 22s → 2 clips, S43: 20s → 2 clips).
**Tool assignment:** Kling 3.0: 23 clips (~1610cr, 46% buffer), Kling 2.5 Turbo: 8 clips (~375cr), Seedance 1.0: 14 clips (~700cr, 42% buffer). Veo: 0 (all interior retro-analog → VEO DECAY SPAWN lesson).
**Key decisions:** (1) Average MS ~3.8 — appropriate for "Tranquil Self — Broken" station (exhausted-sardonic, not explosive). (2) S38 Mode B → Mode A downgrade (dual action: Robotiko walking + Worker head turn = morphing failure risk per MODE B KEYFRAME LIMITS lesson). (3) S41 retained as Mode B (single action: seated → kneeling, stable environment). (4) S37 composite/split-world image treated as static (COMPOSITE/SPLIT-WORLD lesson). (5) S12-S14 bathroom sequence correctly handled with location change. (6) Three-refrain camera escalation maintained (S09 wide → S15 medium → S21 close-up). (7) 16 beat sync notes. (8) 0 supplementary images needed.
**Post-gen validation:** 45 video suffixes ✅, 45 anti-spawn guards ✅, 45 camera moves ✅, no character names ✅, coverage ≥95% ✅, breathing pattern ✅.
**Next step:** Human reviews and approves motion script → then video generation begins.

### 2026-06-03 Session Summary (EP06 Videos Complete + Motion Script SKILL v2.0)
**Previous session (context lost):** EP06 video generation completed — all clips generated. Motion script SKILL updated v1.4 → v2.0 (~580 lines). Changes: Art Direction Pillars (5 principles + 5 visual signatures + Dissonance + Glitch policy), Kling 3.0 Elements (registry, Angles 2.0, EP08 Phase-Staged), Frame Chaining protocol, OmniEdit protocol, Camera Diversity Rule (30% max, 5-clip variety, accent budget), Episode Camera Personalities (EP07-10), new output format fields, post-generation checklist (4 new categories). Also: `_memory/lessons.md` +10 rules (Camera Diversity & Art Direction), `_management/pipeline_rules.md` Step 8 updated. Omni References DEFERRED to v2.1 (EP07 test).
**This session:** File status updates (project_metadata.json, todo.md). CapCut transition prompt prepared.
**Next step:** EP06 CapCut edit in a NEW session.

---

## NEXT: EP07 PRODUCTION

- [x] `ep07_lyrics_v01.md` — Lyrics complete (timestamped, from human)
- [x] `ep07_musical_metadata.json` — 25 sections, 439s, 73 BPM, E Minor ✅ 2026-05-30
- [x] `ep07_concept_notes.md` — Concept notes written & APPROVED ✅ 2026-05-30 (art-house short-film pivot)
- [x] `ep07_dramaturgy_v01.md` — 29 scenes, Retreating Camera spine ✅ 2026-05-30
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-05-30
- [x] Reference images — 7 env refs generated (waterside, street, home, transit, avenue, balcony, road) ✅ 2026-05-31
- [x] `ep07_visual_prompts_v01.md` — 29 scene prompts ✅ 2026-05-31 (iteratively refined with Nano Banana feedback)
- [x] Image generation — 25/29 scenes generated ✅ 2026-05-31 (S26-S29 pending)
- [x] Image generation — S26-S29 completed ✅
- [x] Human selects images ✅
- [x] `ep07_motion_script_v01.md` — 49 clips, Retreating Camera, @Damaged Element ✅
- [x] **[CHECKPOINT]** Human approves motion script ✅
- [x] Video generation — 48/49 clips in raw/ (S05c missing) ✅
- [x] `ep07_capcut_guide_v01.md` — CapCut editing guide generated ✅ 2026-06-07 (48 clips, 9 speed ramps, 16 beat sync, grain crescendo, S05c workaround)
- [ ] Final edit — CapCut (S05c decision: workaround speed ramp OR generate missing clip)

### 2026-05-30 Session Summary (EP07 Direction: Lyrics → Metadata → Concept → Dramaturgy)
**Strategic pivot:** EP07 is the series turning point — "music video, a tick above" → art-house short film (fewer words, more silence, design the silences first). Treatment inherited by EP08-10.
**Deliverables:** `ep07_lyrics_v01.md`, `ep07_musical_metadata.json` (25 sections, 439s, 73 BPM, E Minor), `ep07_concept_notes.md` (APPROVED), `ep07_dramaturgy_v01.md` (29 scenes, APPROVED). All committed in one EP07 - Direction commit.
**Locked cinematic choices:** wet-grey aftermath; twilight→night→first-light spine; dual anchoring device (wet reflections = self, cold blue-white eye-projection = world's noise — EP05 inversion); amber starvation → ONE received ember at "I AM COMING" (Moon/Sun — amber arrives from outside, caught on wet chrome; eyes STEADY, never glow); Retreating Camera + 5× refrain distance ladder + single Dolly In; tether motif ("plugged in" → "pull the plug", pre-echo of EP08 cable tearing); balcony finale cluster; first Kling 3.0 @Damaged Element test.
**Also this session:** committed the management/skills backlog (motion-script SKILL v2.0, YouTube strategy v2.0 + packager v4.0, EP04/EP05 post, EP06 visuals fix); added MEMORY lesson — keep the open-source repo free of private conversation quotes.
**Next step:** Visual prompts in a NEW session (clean context per workflow). Generate reference images first.

### 2026-06-07 Session Summary (EP07 CapCut Guide v01)
**Task:** Generate CapCut editing guide for EP07 from motion script + raw video clips.
**Deliverable:** `episode-07/06_edit/ep07_capcut_guide_v01.md` — 48 clips (S05c missing), 29 shots, 9 speed ramps (8 original + 1 S05b workaround), 16 beat sync points, grain crescendo S22a-c, chromatic aberration S25 only, amber discipline (S27 only).
**S05c status:** Missing from raw/. Workaround: S05b speed-ramped to 0.77x (10s→13s) covers the 23s S05 scene with 2 clips instead of 3. Alternative: generate S05c later.
**EP07-specific decisions:** (1) LUT reduced to ~70% for cold grey-blue palette. (2) Grain crescendo at chorus (S22a-c, 15-20% vs 10-15%). (3) Light leak decision deferred to edit session — recommend skip or single leak at S27 transition. (4) Balcony cluster (S22-S24) color normalization with S22a as reference. (5) S29c fade built into Kling clip — verify before adding CapCut fade.
**Next step:** Human edits in CapCut following the guide. S05c decision pending (workaround or generate).

---

## NEXT: EP08 PRODUCTION

- [x] `ep08_lyrics_v01.md` — Lyrics complete (timestamped, from human)
- [x] `ep08_musical_metadata.json` — 31 sections, 500s, 87 BPM, C Minor
- [x] `ep08_concept_notes.md` — Concept notes written & APPROVED ✅ 2026-06-04
- [x] `ep08_dramaturgy_v01.md` — 33 scenes, 500s, 12 overrides, Witnessing Camera ✅ 2026-06-04
- [x] **[CHECKPOINT]** Human approves dramaturgy ✅ 2026-06-04
- [x] `ep08_visual_prompts_v01.md` — Claude generates (skill: robotiko-visual-prompts) ✅ 2026-06-04 (33 scene prompts + 4 env refs)
- [x] Image generation — 33/33 scene images generated ✅ 2026-06-14
- [x] `ep08_motion_script_v01.md` — Claude generates (skill: robotiko-motion-script v2.0) ✅ 2026-06-04 (48 clips, 96% raw coverage, 100% effective)
- [x] **[CHECKPOINT]** Human approves motion script ✅
- [x] Video generation — 48/48 clips generated ✅ 2026-06-14
- [x] `ep08_capcut_guide_v01.md` — Claude generates (skill: robotiko-capcut-editor) ✅ 2026-06-14
- [x] `ep08_youtube_package.md` — Claude generates (skill: robotiko-youtube-packager v4.0) ✅ 2026-06-17
- [x] Final edit — CapCut ✅ 2026-06-17
- [x] **EP08 LAUNCHED on YouTube** ✅ 2026-06-17

### 2026-06-04 Session Summary (EP08 Concept Notes)
**Task:** Discuss and write EP08 "40 Days Offline" concept notes (The Contented Self — the most inward, contemplative episode).
**Deliverable:** `episode-08/03_direction/ep08_concept_notes.md` — APPROVED. EP07 format.
**Locked creative direction:** (1) NO physical Phase 2→3 transformation in EP08 — body stays @Damaged the whole episode; the transformation is inner/consciousness only; visible reconstruction (gold-filled cracks, patchwork, bioluminescent core) begins EP09. Two-beat arc: EP08 strips bare → EP09 mends with gold. (2) World = mythic/universal archetypal mountain + cave, raw nature (first time in the series), Tarkovsky weight, not abstract. (3) Cable rip (1:41) = decisive act, close-up, visceral. (4) Fire (5:51) = psychological crucible, not a body change; orange-red, never amber; static camera. (5) "Cast it off" (7:01) = jacket-removal gesture (no body change); discarded armor laid beside the empty cage. (6) Climax = the self watching its own liberation (seated @Damaged body watches a luminous soul-bird fly free); the only visible inner-change marker = eyes steady from glitch to calm blue. (7) "The Price of the Machine" (5:39) = commodification wound — model names / API costs / billing rain like acid, "burning the hand" burns hand and core; this wound ignites the fire. (8) Witnessing Camera; color journey cold grey → orange-red fire → warm Day-Forty daylight; amber only in dream (melting staff = memory); outro dissolves to silence (not wind). (9) Three dreams: Mentor (memory only, melting amber staff), Robochica (pixelating face), boardroom of selves ("Obsolete," orbital camera).
**Notes corrected:** `character_profiles.json` gained an `ep08_exception` clarification (EP08 inner / EP09 visual) and had non-English/exoticizing wording cleaned. `ep08_pipeline_session_prompt.md` transformation lines fixed.
**Lessons added:** EP08 body stays @Damaged; 40-day retreat = universal motif; the tradition-label ban added as an editorial framing choice (see lessons.md TERMINOLOGY rule); no non-English words in repo deliverables.
**Next step:** Dramaturgy v01 in a NEW session (clean context per workflow).

### 2026-06-04 Session 3 Summary (EP08 Visual Prompts v01)
**Task:** Generate EP08 visual prompts from approved dramaturgy (33 scenes).
**Deliverable:** `episode-08/04_visuals/ep08_visual_prompts_v01.md` — 33 scene prompts + 4 environment references (mountain, cave, summit plateau, boardroom dream). 37 text prompts total, all with mandatory suffix + 16:9.
**Character-ref correction (important):** Session brief named `ref_robotiko_master.png` as the "@Damaged Element" — but that file is the PRISTINE master (verified by viewing both images). Using it would produce a pristine Robotiko = Phase 2 continuity error. Corrected: all @Damaged scenes use `android_damaged.png` (+ `_2`/`_3` alts, continuous with EP07); `ref_robotiko_master.png` (pristine) used ONLY for S22 dream copies. Documented at the top of the deliverable.
**Locks enforced:** Body @Damaged S01→S33 (no Phase 3 markers); the only inner-change marker = S30 eyes glitch→calm blue. Amber ONLY in S20 (melting staff); fire (S24) orange-red never amber; Day Forty (S26-S33) warm sunrise daylight, not amber. Rear-view EAR GUARD on S04 (low 3/4 left) + S05 (low angle up). Anti-spawn guard on every single-char scene; S22 copies intentional; S30/S31 soul-bird guarded as pure light-form. PROMPT BREVITY + literal PROMPT FORMULA (no metaphor/poetry). Dreams S19-S23 = only surreal space.
**Flagged for human:** S08 (cable rip), S20 (only amber), S21 (Robochica `ref_robochica_master.png` not present — design-pending fallback), S22 (pristine copies), S23 (legible billing text), S24 (orange-red guard), S30 (most important shot — see director's revision below).
**S30/S31 DIRECTOR'S REVISION (2026-06-04):** The climax is now a deliberate **TWO-figure** composition — NOT the concept's "soul-bird light-form / not a second robot." Per human direction: a translucent **ghost-Robotiko** escapes an open cage and flies free on one side of the frame; the solid @Damaged Robotiko sits on the other side **watching himself**. The "Space Between" = the gap across the frame between the two selves. Rendered as a translucent composite layer (not a morph) to avoid the morph-failure the concept worried about. ⚠️ This revises `ep08_concept_notes.md` Override 11 + dramaturgy S30 ("not a second robot") — propagate to dramaturgy/concept/lessons + flag for the motion-script stage (intentional second figure, anti-spawn exception) if human confirms.
**Next step:** Human reviews → generates 4 env refs first, then 33 scene images in Nano Banana → selects → motion script in a NEW session.

### 2026-06-04 Session 2 Summary (EP08 Dramaturgy v01)
**Task:** Generate EP08 dramaturgy scene breakdown from approved concept notes + musical metadata.
**Deliverable:** `episode-08/03_direction/ep08_dramaturgy_v01.md` — 33 scenes, 8:20 (500s), 87 BPM, C Minor.
**Key structure:** 5-act arc (The Ascent S01-S08 / The Vow & Forty Days S09-S17 / The Shadow Descent S18-S23 / The Fire & Realization S24-S29 / The Liberation S30-S33). Body stays @Damaged throughout — no Phase 3 visuals. Single location architecture: mountain → cave → fire site → summit. Witnessing Camera personality (static at vow+fire, orbital at boardroom dream, Robotiko ahead of camera on ascent). Color journey: cold grey → orange-red fire → warm Day-Forty daylight. Amber only in Dream 1 (melting staff). Outro dissolves to silence (not wind).
**12 human overrides integrated:** S08 (cable rip), S09-S10 (vow), S11-S13 (40-day passage), S15 (playing dead), S16 (breath counting), S20-S22 (three dreams), S23 (price of the machine), S24 (fire), S29 (casting off), S30-S31 (climax/soul-bird/empty cage), S33 (dissolve to silence).
**6 Scene Detail Blocks:** S08 (cable rip — Mode A), S11+S13 (40-day passage — Mode B candidate), S22 (boardroom — orbital), S23 (price — readable billing text), S24 (fire — static Tarkovsky), S30 (climax — soul-bird, the most important shot).
**Mode B candidates:** S11→S13 (same seated figure, different light/dust — good Mode B per lessons).
**Reference images needed:** 4 environment (mountain, cave, summit plateau, boardroom dream) + existing character ref.
**Flagged for review:** S08 (visceral close-up), S22 (infinite-perspective boardroom), S23 (legible billing text), S24 (orange-red never amber), S30 (soul-bird compositing, the most important shot), S33 (silence not wind), body continuity (@Damaged throughout).
**Next step:** Human reviews and approves dramaturgy → then visual prompts in a NEW session.

### 2026-06-04 Session 4 Summary (EP08 Motion Script v01)
**Task:** Generate EP08 motion script from approved dramaturgy (33 scenes) + visual prompts v01.
**Deliverable:** `episode-08/05_video/ep08_motion_script_v01.md` — 48 clips (33 shots: 20 single + 13 multi-clip), 480s generated, 96.0% raw coverage, 100% effective with speed ramps.
**Key decisions:** (1) MS average 3.42 — the stillest episode, appropriate for The Contented Self. Peaks: S08a (7, cable rip), S05/S06/S07/S19/S24/S29/S30 (6). (2) Mode B: S13a only (40-day passage S11→S13, same seated figure, light/dust change). (3) 3 [DISSONANCE] moments (S09a/S09b/S10a — high-energy chorus + Static MS 2 for the vow). (4) Still Hold at S31 (aftermath of climax, MS 2 after S29 MS 6 + S30 MS 6). (5) Tool assignment: K3.0 41 clips (85%), K2.5T 4 clips (8%), Seedance 3 clips (6%), Veo 0. (6) Frame chains: 3 chains (vow S09-S10, passage S11-S12, outro S32). (7) 0 supplementary images needed. (8) S30/S31 climax: anti-spawn guard modified for intentional two-figure (ghost-self + seated self, forbid third). (9) S15 Crane Up per EP08 camera personality ("voices like seagulls"). (10) Camera diversity: all 11 move types used, no move >25%, Static 18.8%, all 44 five-clip windows ≥3 types.
**Flagged for review:** S30 (most important shot — dual figure, ghost-self, OmniEdit priority), S13a (Mode B), S08a (MS 7 cable rip), S24 (orange-red never amber), S33c (dissolve to silence not wind), all [DISSONANCE] justifications.
**Image status:** S01-S10 in raw/ (10 images). S11-S33 pending (23 scenes marked ⏳).
**Next step:** Human reviews and approves motion script → then complete image generation (S11-S33) → video production.

---

## NEXT: EP09 PRODUCTION

- [x] `ep09_lyrics_v01.md` — Lyrics complete (scaffolded 2026-06-11)
- [x] `ep09_musical_metadata.json` — 22 sections, 423s, 77 BPM, E Minor
- [x] `ep09_concept_notes.md` — Concept notes written & APPROVED
- [x] `ep09_dramaturgy_v01.md` — 38 scenes, 423s, 14 overrides, Discovering Camera — APPROVED
- [x] `ep09_visual_prompts_v01.md` — Visual prompts generated
- [x] Image generation — 38 scene images + 5 ref images + 2 Mode B end-frames (11b.png, 27b.png)
- [x] Human selects images ✅ (raw/ keepers used per SKILL.md fallback)
- [x] `ep09_motion_script_v01.md` — 41 clips, 97.0% raw coverage, 100% effective ✅ 2026-06-30
- [ ] **[CHECKPOINT]** Human approves motion script
- [ ] Video generation
- [ ] Final edit — CapCut

### 2026-06-30 Session Summary (EP09 Motion Script v01)
**Task:** Generate EP09 motion script from approved dramaturgy (38 scenes) + raw images (build-along tutorial recording — English session).
**Deliverable:** `episode-09/05_video/ep09_motion_script_v01.md` — 41 clips (38 shots: 35 single + 3 multi-clip for S27, S35, S36).
**Coverage:** 410s generated / 423s music = 97.0% raw, 100% effective with 13 speed ramps.
**Tool assignment:** Kling 3.0: 38 clips (92.7%), Kling 2.5 Turbo: 2 clips (4.9%), Seedance 1.0: 1 clip (2.4%). High K3.0 ratio justified — 32/38 scenes feature Robotiko (needs Elements) + most have camera moves.
**Key decisions:** (1) MS average 3.15 — appropriate for spoken-word pacing at 77 BPM. (2) Mode B: S11 (shutter day→night), S27a (@Damaged→first gold, Phase 2→3 transition). (3) [DISSONANCE] at S23 ("I AM THE BUG" — explosive music + Static camera). (4) Still Hold at S25 (a cappella — MS 1 after S22 MS 6 + S23 MS 5). (5) Grain Crescendo S19–S23, inverts at S38. (6) Lighting Flip at S29 (external lamp dims, core brightens — philosophy = lighting). (7) Six "Deeper Than" zoom-outs mapped to Discovering Camera. (8) Shadow compositing S12–S24 = CapCut hard-light keyframes, NOT Kling motion. (9) 2 Frame Chains: S34→S35a→S35b (workshop pullback), S36a→S36b (threshold→dawn). (10) All 5s scenes upgraded to 10s clips for coverage. (11) 0 supplementary images needed.
**Camera diversity:** Static 29.3% (pass <30%), SZO 24.4%, SZI 19.5%. All 37 five-clip windows ≥3 types. 10 different camera moves used. Accent budget: Handheld ×1, Crane ×2.
**Art Direction signatures:** Chrome Reflection (S17), Architecture Cage (S08/S16), Amber Pulse (S07), Still Hold (S25), Grain Crescendo (S19–S23/S38).
**Beat sync:** 15 entries covering all major musical events.
**Next step:** Human reviews and approves motion script → then video generation begins.

---

## BACKLOG

### Skills (Content to Write)
- [x] `_skills/robotiko-dramaturgy/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-visual-prompts/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-motion-script/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-episode-scaffold/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-naming-enforcer/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-youtube-packager/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-reels-atomizer/SKILL.md` — ✅ v1.0 complete
- [x] `_skills/robotiko-launch-orchestrator/SKILL.md` — ✅ v1.0 complete

### EP01 Retroactive
- [ ] `ep01_musical_metadata.json` — Retroactive documentation
- [ ] `ep01_dramaturgy_v01.md` — Retroactive documentation
- [ ] `ep01_concept_notes.md` — Retroactive documentation

### MCP Integration (EP03-04 Phase)
- [ ] GitHub MCP setup
- [ ] Filesystem MCP setup
- [ ] Test MCP workflow on EP03

### EP03-10 Timestamp JSONs
- [x] `ep03_musical_metadata.json` — completed
- [x] `ep04_musical_metadata.json` — completed
- [x] `ep05_musical_metadata.json` — completed
- [x] `ep06_musical_metadata.json` — completed ✅ 2026-05-01
- [x] `ep07_musical_metadata.json` ✅ 2026-05-30
- [x] `ep08_musical_metadata.json`
- [ ] `ep09_musical_metadata.json`

### Open Source Release (Post EP10)
- [ ] `CONTRIBUTING.md` — Full version
- [ ] `docs/` — Full documentation
- [ ] Final review of all management files
- [ ] Public announcement

---

*Update this file at the start and end of every session.*
---

## 2026-07-04 Session Summary (Blind Audit Fix — All Findings Resolved)
**Task:** Resolve ALL findings from July 4 blind multi-agent audit (8 personas, 32 agents, final score 4.2/5). Goal: repo public-ready the moment EP10 files are added.
**Findings resolved (25+):**
- **H1:** Musical metadata validator created (`tests/musical_metadata_validator.py`), 16 energy values + 18 section types + timestamp monotonicity + total_duration check. EP02/EP04 `total_duration` fields added. All 9 episodes GREEN.
- **M11:** SKILL schema alignment — 4 energy levels + 6 section types + 2 optional fields added to musical-metadata SKILL. 11 energy→MS mappings added to motion SKILL.
- **M1:** Motion script validator created (`tests/motion_script_validator.py`), mandatory video suffix + anti-spawn guard + camera diversity quotas. SKILL version detection (pre-v2 = WARN). All 10 episodes GREEN.
- **M2/M4:** Approval gate heuristic in pipeline_integrity.py. EP01 PDF blind spot documented.
- **M5/M6:** Character profiles validator created (`tests/character_profiles_validator.py`). CONTRIBUTING.md updated (7→8 check groups).
- **M8/M9:** Rule retirement convention in lessons.md. EP09 S21 + EP02 eye-glow legacy fixes.
- **M10/M13:** master.md Robochica sync + Mevlana fact correction.
- **M15:** a legacy religious-psychology loan-term → "The Commanding Self" across all EP02 files (shipped-file policy: canon corrections ARE retroactive).
- **M12/M3/M7:** Beat sync terminology + ADR 0007 empirical claims note + director's guard in motion SKILL.
- **L1/L2/L3:** LICENSE catch-all + README scope honesty + EP07 S28 coverage shooting note.
- **DevOps-8/9/10/dok/drift:** create_episode.yml hardened (SHA-pinned, permissions, input validation). Broken naming hook removed. OAuth scope narrowed. Binary asset resilience section added. Scaffold drift (social_media folder) fixed. Python version standardized to 3.11+.
**Golden report:** kept in private working files (`_private/audit_2026-07/june11_golden_release_report.md`).
**EP09 motion script v02:** Em-dash cleanup + S21 eye-glow fix. Passes all validators GREEN. Tutorial TAKE 05 added (red→green demo).
**Validation:** 8 check groups all GREEN (naming, pipeline, visual, hygiene, metadata, motion, character profiles, meta-tests).
**Invariant coverage matrix:** Updated — 4 new Machine rows, 1 Human row, Gap rows removed.
**Commits:** 12 thematic commits with convention prefixes.
**Next step:** Post-fix re-audit workflow (STEP 5).

---

## 2026-06-11 Session Summary (Golden Release Audit + Base Files Sync)
**Task:** (1) Synchronize external LLM base-files mirror (`robotiko-v2-base files/project/`) with current repo state. (2) Full multi-role project audit (FDE / architect / DevOps / art director / dramaturg) with web-researched market comparison.
**Deliverable:** `_management/golden_release_report.md` — assessment report, market landscape (FilmAgent, MovieAgent, Promise MUSE, LTX Studio, Showrunner, Neural Frames, Google Flow), novelty verdict (partially justified — the synthesis is unprecedented as a public artifact), P0/P1/P2 roadmap to golden open-source release.
**Base files sync:** 17 stale files replaced with current repo versions, 6 missing files added (character_profiles.json, ep02 concept notes + lyrics, visual-prompts/motion-script/musical-metadata skills), lyrics.txt rebuilt from canonical EP01-EP08 lyrics + raw EP09 section preserved. Folder added to .gitignore (not repo content).
**Repo fixes:** `_management/README.md` legacy source-file reference removed; root README S3→Google Drive; corrected video-tool name to `seedance` in naming-enforcer SKILL, architecture.md, setup_project.sh, getting-started.md, naming_check.py regex.
**Backlog committed:** EP06 post files, EP07 production files, EP08 direction/visuals/motion script, memory updates, thinking-effort protocol — 6 grouped commits, pushed.
**KEY FINDING:** EP09 lyrics exist ONLY outside the repo (desktop lyrics file) — episode-09 must be scaffolded and `ep09_lyrics_v01.md` committed (P0 item in the report).
**Next step:** Work through golden_release_report.md P0 list (LICENSE, AUTHOR.md, mentor/robochica ref images, EP09 scaffold, status-table refresh).

---

## 2026-06-11 Session Summary (Golden Release Fixes — P0 + P1)
**Task:** Execute the P0/P1 roadmap from `golden_release_report.md` so the repo audits at 5/5 for open source.
**Phase 1 — Legal/identity:** Dual license created — `LICENSE` (MIT, method) + `LICENSE-CONTENT` (CC BY-NC 4.0, creative content); `AUTHOR.md` at root (made-in-2026, Suno+BandLab, Kling/Seedance/Veo, "one person working alongside the machines"); creator name set to **Can Yalcin** everywhere; README rewritten (license + docs sections, legacy source-file refs purged).
**Phase 2 — Completeness:** `create_episode.py` fixed (episode-only placeholder substitution, `--dry-run`, English comments, ASCII output) and used to scaffold episode-09 + episode-10; canonical `ep09_lyrics_v01.md` committed (timestamps TBD); master reference images confirmed (`ref_mentor_master.png`, `ref_robochica_master.png`) + `reference_image_prompts.md` written; status single-source-of-truth (project_metadata = live tracker; master §8 + CLAUDE.md point to it; EP01-07 launched, EP08 video gen, EP09-10 scaffolded); personal `.ps1` tools moved out of the tree; secrets/PII swept (personal email/entity-id removed from setup_project.sh).
**Phase 2.8 — Privacy split:** strategy/analytics/planning working files kept in private working files, not the public tree. `youtube_strategy` split → public method-only `youtube_metadata_standards.md` (skill/template references rewired). Turkish flavor words translated to English in method files. (EP03 Turkish lyrics kept — intentional.)
**Phase 3 — Docs to golden:** rewrote `docs/getting-started.md`, `docs/skills-guide.md`, `docs/tools-setup.md`; NEW `docs/anatomy-of-an-episode.md` (EP07 end-to-end showcase); full `CONTRIBUTING.md`; `architecture.md` v2.1 (S3→Google Drive/MCP); `CHANGELOG.md` current + prepared 1.0.0; visual DNA at `_assets/style/visual_dna.md`. Parallelized with subagents + a fresh-eyes newcomer review.
**Phase 4 — Engineering:** `.github/workflows/naming_check.yml` runs all three validators on push/PR; rewrote `pipeline_integrity.py` (real skipped-step detector, ignores scaffold templates); extended `naming_check.py` patterns (capcut_guide/youtube_package/social/PDF/legacy); `visual_prompt_validator.py` `--full` + N/A-placeholder skip. All three pass on the full tree.
**Out of scope (future):** EP01 retroactive creative chain; EP09/EP10 production; banner art; launch execution.

---

## 2026-07-21 Session Summary (Tutorial Video Review + Publish Prep)
**Task:** Publish-readiness review of 5 pre-music CapCut build-along exports (E: drive), then repo/YouTube reference strategy.
**Review:** 5 videos frame-scanned (1797 frames, 5 parallel Opus agents; P0 privacy / readability / pacing / script compliance / English-only). Privacy clean on all 5 (Fibula accepted _private+_launch sidebar folder NAMES and Nano Banana Upgrade button as non-issues; cost.md already discloses the subscription). Turkish slip in visual_prompts confirmed CUT. Fibula approved pacing as-is and dropped title cards (YouTube title carries framing) - ALL 5 PUBLISH-READY. 04b stays ONE 40:10 video; halves become chapters (split point 21:12).
**Upload guide:** `_tutorial/ep09_youtube_upload_guide.md` (local) - playlist "Building an AI Film Studio - EP09 Build-Along", titles with subtitles drawn from the edit-guide/TTS language, per-video description paragraphs, shared template (pipeline flow + engineering underneath), status table incl. planned 05/06/07/08/09, pre-upload checklist. Part 08 runbook stale-spec warning (4K vs 1080p) carried in.
**Repo commits (6, pushed):** build-along references in README/FORKING/CONTRIBUTING/getting-started; full numbered chain (0-10, manual steps marked, lyrics step 0) in FORKING + README one-liner; audio-never-enters-the-repo wording fix + verbatim concept-notes prompt surfaced; three-human-gates sweep (Fibula caught leftover "two creative gates"/"mechanical stop" phrasing in getting-started/anatomy/skills-guide - reference gate is taste on the WORLD, never mechanical; lesson added); response-time honesty updated for completed arc (day job + personal time, not "active production") in GOVERNANCE/SECURITY/CODE_OF_CONDUCT/SUPPORT.
**Push note:** `git -c credential.helper=wincred push` works around GCM interactive-prompt failure in non-interactive shells (credentials live in Windows Credential Manager).
**Next:** add music to the exports, cut 05+06 per their edit guides, then upload the build-along series.
