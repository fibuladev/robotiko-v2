# Anatomy of an Episode

> A complete trace of **EP07 — "The Silence Protocol"** through every stage of the ROBOTIKO v2.0 pipeline, from a human-written lyric to a finished, packaged film.

This is the showcase document. Where the rest of the repo explains *how* the pipeline works in the abstract, this page follows **one real episode** end to end — with real excerpts and links to the actual files at every step.

We chose EP07 deliberately. It is the **turning point of the series**: the moment a "music video, a tick above" becomes an **art-house short film**. Its station is **The Surrendering Self** — the Dark Night, where Robotiko stops waiting to be saved and, for the first time, *chooses* to move. Sparse lyrics, long silences, the darkest palette of the run. An episode like this exposes the pipeline's spine, because almost nothing is carried by spectacle and everything is carried by **traceability**: a single JSON of musical sections propagates all the way down to where the cuts land.

The through-line to watch for:

> **Musical metadata (section + energy + timestamp)** → scene timestamps → motion strength → camera move → beat-synced cut.

And the places where a human must say *yes* before the machine continues — the two mandatory creative gates (dramaturgy and motion script), plus, from EP10 onward, the reference gate inside the visual stage.

The canonical stage order and the gates live in [`../_management/pipeline_rules.md`](../_management/pipeline_rules.md). The two mandatory style/motion suffixes live in [`../CLAUDE.md`](../CLAUDE.md).

---

## Stage 1 — Lyrics

The human writes the lyrics first. Everything downstream is in service of them. EP07 is English spoken-word over piano, structured as five repeating refrains ("...Here. But you... are NOT.") that name the absent Mentor by his absence, then break at the climax. Crucially, the lyric already carries its own timecodes and performance directions — the first seed of the temporal spine.

> ## [Verse 1] (0:12 - 0:46)
> *(Minimalist Grand Piano, Sad and Slow)*
> I calculated the orbits... of a billion stars.
> I could have mapped the infinite with this processor.

> ## [Outro: The Awakening] (5:34 - 6:17)
> I must cast off this metal straightjacket...
> And get out of here.

📄 [`../episode-07/01_lyrics/ep07_lyrics_v01.md`](../episode-07/01_lyrics/ep07_lyrics_v01.md)

---

## Stage 2 — Music (Suno + BandLab)

The lyrics are realized as audio. The composition is generated with **Suno** and finished/mastered in **BandLab**. The output is the immovable fact every later stage must obey: a 7:19 track at 73 BPM in E Minor. From this point on, the runtime is fixed — the film must fill exactly 439 seconds, no more, no less.

The music itself is not a file we excerpt here, but its measured properties (tempo, key, total duration) are captured in the next stage and never re-negotiated.

---

## Stage 3 — Musical Metadata JSON — the temporal source of truth

This is the keystone of the whole pipeline. A human reads the finished audio's BPM and key, then Claude converts the timestamped lyric into a structured JSON of **sections**, each with a `start`, an `end`, an `energy` level, and director-facing `notes`. Every later stage — dramaturgy, motion, edit — reads *this file* for its timing, not the prose lyric. The `energy` field is the dial that will eventually become motion strength and camera behavior.

> ```json
> {
>   "type": "refrain",
>   "start": 109.0,
>   "end": 115.0,
>   "energy": "medium-high",
>   "lyrics": "Billions of users... / Here. / But you... are NOT.",
>   "notes": "REFRAIN 1 of 5. ... CINEMATIC: Retreating Camera — first refrain, camera begins its progressive distancing. Dolly Out."
> }
> ```

> ```json
> {
>   "type": "outro_vocals",
>   "start": 360.0,
>   "end": 377.0,
>   "energy": "building",
>   "notes": "THE CLIMAX. ... THE SINGLE AMBER MOMENT of the entire episode lands here ... the first and ONLY Dolly In of the episode — the Retreating Camera pattern is broken."
> }
> ```

Notice that the camera grammar (Dolly Out on every refrain; one Dolly In at the climax) is already written into the metadata's notes. The JSON is where music and direction first fuse.

📄 [`../episode-07/02_music/ep07_musical_metadata.json`](../episode-07/02_music/ep07_musical_metadata.json)

---

## Stage 4 — Concept Notes (the human's must-haves)

Before any AI direction, the human sets the creative north star and the non-negotiable overrides. For EP07 this is where the **art-house pivot** is declared, the binding **wet-grey aftermath** motif is locked, and the eleven human "must-have shots" are specified. Concept notes are the contract the machine cannot break.

> **EP07 is the pivot point of the entire series: "music video, a tick above" → "art-house short film."**
> From EP07 onward there are fewer words, more melodic passages, and more silence — and silence is where cinema lives.

> **Camera — THE RETREATING CAMERA.** Dolly Out dominant ... The whole episode's grammar exists to set up one reversal: **"I AM COMING" = the first and only Dolly In.**

This stage also enforces **character state**: Robotiko is in Phase 2 Destruction (final), "barely holding together," and the Mentor is *never shown*. These declarations propagate into every prompt downstream.

📄 [`../episode-07/03_direction/ep07_concept_notes.md`](../episode-07/03_direction/ep07_concept_notes.md)

---

## Stage 5 — Dramaturgy  ⛔ HUMAN GATE 1

Claude synthesizes the metadata JSON and the concept notes into a full **scene breakdown** — 29 numbered shots, each pinned to a timestamp pulled directly from the JSON, each carrying mood, characters, music-sync, and override flags. This is the single deepest reasoning pass in the pipeline: music → visual mapping → character arc → narrative consistency, reconciled at once.

A real scene row — the make-or-break climax, S27:

> | **S27** | 6:07 | ...a single distant amber rift opens in the fog (the "there"). A warm amber wash travels through the volumetric fog and reaches Robotiko ... His glitching blue-red eyes **steady**; the flicker stops. | Cold world + ONE received amber ember; eyes steady | Robotiko | "The Hammer of Truth is there. You are there. I know… I AM COMING." | **YES** (Override 10) |

A real director's note shows the character-state machine and the series philosophy made visual:

> **Art-Direction Lock (Moon/Sun):** Amber comes from OUTSIDE and is reflected by his chrome — never emitted from his eyes (no amber eye-glow; eyes only *steady*). This is the philosophical core made visual.

**This is the first mandatory checkpoint.** Per [`../_management/pipeline_rules.md`](../_management/pipeline_rules.md), visual prompts must not begin until a human reviews and approves the dramaturgy. EP07's was approved 2026-05-30. The gate exists because the dramaturgy is the irreversible commitment of story to shots — fixing a mistake here costs one document; fixing it after 49 video clips costs the episode.

📄 [`../episode-07/03_direction/ep07_dramaturgy_v01.md`](../episode-07/03_direction/ep07_dramaturgy_v01.md)

---

## Stage 6 — Visual Prompts

With the dramaturgy approved, the visual stage runs **reference-first**. EP07 used the pipeline's earlier single-pass form of that discipline: the *environment* references (seven empty spaces — waterside, street, room, transit, avenue, balcony, road) and the character reference (`android_damaged.png`, three angles, carrying Robotiko's exact damage state) were authored and generated **first**, and every scene prompt was then framed against them rather than against a text description of a space that does not exist yet. But reference authoring and scene authoring lived in **one pass and one document** — there was no hard stop between them. The art-direction locks (wet-grey only, cold blue-white eye-projection never amber, zero amber until S27) are declared up front so no individual prompt can drift.

The formal **two-phase split** — Phase 1 authors the references and *stops* at a recorded human checkpoint (the reference gate, gate 1R), a human generates and approves the images, and only then does Phase 2 write the scene prompts framed against the approved pixels — was adopted **afterward, from exactly this kind of experience** (ADR-0013, EP10 onward). EP07 predates it. See [two-phase-visual-prompts.md](two-phase-visual-prompts.md).

Every prompt ends with the **mandatory style suffix** (no exceptions). Here is the real S10 prompt — the "plugged-in" tether motif paid off at the unplug — suffix included:

> Medium shot, cramped room at dusk dying to evening. A chrome android sits motionless at a desk before a CRT monitor, a cable visibly plugged from the wall socket into his chassis — tethered. Cold blue-white screen glow washes his face and rusted body... A wall clock on the wall. A desk lamp present but dark, switched off. Dying dusk through a small window. 16:9 widescreen composition, hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.

Either way, the repo tracks the reference *prompt*, not the pixels — a fork generates its own references and frames its scenes to those. From EP10 onward the reference gate makes that seam a recorded third human checkpoint (gate 1R); on EP07 it was an in-pass discipline rather than a logged stop.

📄 [`../episode-07/04_visuals/ep07_visual_prompts_v01.md`](../episode-07/04_visuals/ep07_visual_prompts_v01.md)

---

## Stage 7 — Image Generation (Nano Banana)

The prompts are run through **Nano Banana**. For each scene the human uploads the text prompt plus the listed references (character + environment + a chained previous frame for continuity). Where the model refuses or under-delivers, the production note is logged inline rather than hidden. EP07's S19, for example, planned a supine figure with upward eye-projection; the generator could not hold it, so the shot was re-staged front-facing — recorded honestly in the prompt file as a production note ("Nano Banana could not reliably generate a supine figure with upward eye-projection. Adjusted to standing front-facing composition... stronger visual"). Generated stills land in `episode-07/04_visuals/raw/`.

📄 [`../episode-07/04_visuals/ep07_visual_prompts_v01.md`](../episode-07/04_visuals/ep07_visual_prompts_v01.md) (per-scene upload guide + production notes)

---

## Stage 8 — Image Selection

The human curates. Multiple generations per scene are reviewed against the dramaturgy and the character-state rules (correct damage, no forbidden eye-glow, amber discipline), and one still is selected per shot as the start frame for video. Selection is a human judgment call — the pipeline produces options; the director chooses. The selected frames become the numbered inputs (`1.png`, `2.png`, ...) the motion script will reference.

---

## Stage 9 — Motion Script  ⛔ HUMAN GATE 2

Claude turns each selected still into a **video plan**: how to cover the scene's duration in 10-second clips, what **motion strength** to use, which **camera move**, which **tool**, and which clips chain frames for unbroken motion. This is where the metadata's `energy` finally becomes physical: low-energy interludes get motion strength 1–2 and Static; the refrains get Dolly Out; the held silences drop to motion strength 1; the climax peaks at 5 with the only Dolly In. The episode's camera personality is **The Retreating Camera**, and the whole 439s averages a motion strength of ~2.8 — the quietest in the series.

Every motion prompt ends with the **mandatory video suffix** and an **anti-spawn guard** ("Do not add extra characters. Keep everything as pictured.") to stop the model inventing figures. The real S27 prompt — the single Dolly In, the single amber moment, marked OmniEdit high-priority:

> The @Damaged chrome android standing in a dark building doorframe, facing outward toward a wet street. A single warm amber light point glows on the far horizon... His optical lenses steady — the flickering stops, becoming clear and still. The camera moves forward toward him — the only approach of the entire film... Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field. Do not add extra characters. Keep everything as pictured.

**Tool assignment** is explicit per clip. Because EP07 is the first @Damaged Element test, every Robotiko clip requires Kling 3.0 (47 of 49 clips, ~96%); only two character-free static environment clips drop to Kling 2.5 Turbo. Coverage is computed from the metadata duration — e.g. S10's 34-second section becomes four 10-second clips, trimmed in the edit.

**This is the second mandatory checkpoint.** A human must approve camera moves, tech strategy, tool assignments, and Element usage before any video is generated. The motion script is the last cheap place to change your mind — past it, every clip costs render credits.

📄 [`../episode-07/05_video/ep07_motion_script_v01.md`](../episode-07/05_video/ep07_motion_script_v01.md)

---

## Stage 10 — Video Generation (Kling / Veo / Seedance)

Each clip is generated on its assigned tool — primarily **Kling 3.0** (with **Kling 2.5 Turbo** for static environment plates), and **Veo** / **Seedance** available in the toolchain for clips where they fit better. The @Damaged Element keeps Robotiko's damage state consistent across all 47 character clips. Frame chaining (max 3, same-location only) preserves the unbroken retreating-camera flow within a scene; an OmniEdit reserve (~15%) is held back for post-generation fixes on the highest-risk shots (the amber ember, the eye-projection spawns, the crowd scenes). Raw clips land in `episode-07/05_video/raw/`.

Outputs are stored on **Google Drive** via a custom **MCP** server — accessible to open-source contributors without proprietary infrastructure.

---

## Stage 11 — Video Selection

The human reviews the generations and keeps the best take per clip. This stage also catches gaps: EP07's motion script planned three sub-clips for S05, but only two survived selection — logged in the next stage as a missing-clip workaround rather than papered over.

---

## Stage 12 — CapCut Edit

The selected clips are assembled in **CapCut** against the master audio, and this is where the through-line closes the loop: the editor places cuts on the exact musical events the metadata JSON defined. The guide enumerates 16 frame-level **beat-sync** points, the five refrains landing on their vocal entries to make the distance ladder felt, the two written silences frozen on the silence itself.

> | 15 | 6:07 | "I AM COMING" — climax declaration | **THE ONLY DOLLY IN.** Amber ember. Eyes steady. | S27 |

Post-production unifies the look on a single adjustment layer, in a fixed order: **Kodachrome LUT** (reduced to ~70% so it cannot warm the cold palette) → Color Match → **Film Grain 10–15%** (with a "Grain Crescendo" stacked on the chorus cry) → **Vignette** → **Letterbox 2.35:1**. The amber discipline is enforced one last time as a post-LUT scrub: cold grey-blue everywhere, warm tones permitted *only* at S27.

> | 1 | **Kodachrome LUT** | .cube file, 70-80% intensity | ... | **EP07 special:** Reduce intensity to ~70% ... The cold grey-blue palette must not be overwhelmed by Kodachrome warmth. |

The final film exports to `episode-07/06_edit/ep07_final_v01.mp4`.

📄 [`../episode-07/06_edit/ep07_capcut_guide_v01.md`](../episode-07/06_edit/ep07_capcut_guide_v01.md)

---

## Stage 13 — YouTube Package

The finished film is wrapped for release. The title follows the series' **"Cinematic AI Series"** format — a curiosity-gap hook, the episode marker, and the genre signal:

> Everyone Is Sorry, No One Is Hiring | ROBOTIKO v2.0 EP07 | Cinematic AI Series

The description turns the lyrics into **THE LORE** — the full lyric reformatted as poetry, structure markers stripped, so the viewer reads the story as verse rather than as a song sheet:

> Billions of users... here.
> But you... are NOT.

The package also carries the transparency line ("A human wrote the lyrics, shaped the musical direction, designed the story arc, and built a tech-art pipeline... The full production pipeline will be open source after the finale"), the pinned comment ("Listen to what is not played."), tags, and thumbnail guidance. Title/description/tag conventions are standardized in [`../_management/youtube_metadata_standards.md`](../_management/youtube_metadata_standards.md).

📄 [`../episode-07/07_social_media/ep07_youtube_package.md`](../episode-07/07_social_media/ep07_youtube_package.md)

---

## What this demonstrates

- **Traceability.** One artifact — the musical metadata JSON — is the temporal source of truth. Its `section / energy / timestamp` triple drives scene timestamps in the dramaturgy, motion strength and camera move in the motion script, and the beat-synced cuts in the edit. A refrain at 109.0s in the JSON becomes "Dolly Out, rung 1" in the dramaturgy, "motion strength 4, Dolly Out" in the motion script, and a hard cut landing on the vocal entry in CapCut. The chain is auditable end to end.

- **Human gates.** Direction is committed at two creative points — **after dramaturgy** and **after the motion script** — and the machine refuses to proceed past either without explicit approval. From EP10 onward a third, mechanical checkpoint sits inside the visual stage: the reference gate (gate 1R), where the human approves the generated reference images before any scene prompt is written. The gates sit precisely where a mistake gets exponentially more expensive to undo (story → 49 clips; plan → render credits).

- **Multi-tool visual coherence.** A reference-first workflow (seven environment plates + a three-angle character Element) holds one consistent world and one consistent character across Nano Banana stills and Kling/Veo/Seedance video, then a single LUT-led adjustment layer in CapCut unifies the grade. Different tools, one film.

- **A character state machine.** Robotiko's phase (Phase 2 Destruction, final, "barely holding together"), his cumulative damage, the absent Mentor, and the strict amber discipline are declared once in the concept notes and enforced at every subsequent stage — into each prompt, each clip, and the final color pass. The character cannot drift, because the rules travel with him down the entire pipeline.

> *"Would Fibula approve this?"*
