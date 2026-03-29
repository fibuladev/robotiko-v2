# LESSONS LEARNED
> Claude updates this file after every correction from the human.
> Read this at every session start before any task.
> Last Updated: 2026-02-23

---

## HOW TO USE THIS FILE

After any correction from the human:
1. Identify the mistake pattern
2. Write a clear rule that prevents it
3. Add it here under the relevant category
4. Commit: `MEMORY - Lessons updated: {brief description}`

---

## CATEGORY: CREATIVE & NARRATIVE

- **RULE:** Never reference `bible.md` — the source of truth is `master.md`. bible.md no longer exists.
- **RULE:** Always check character phase before writing any visual prompt. Pristine Robotiko in EP07 is a continuity error.
- **RULE:** Robotiko's damage is CUMULATIVE across episodes. EP01 = pristine. EP02+ = battle scars carry forward (missing ear, torso dent, shoulder scratches). Never write "pristine" for any episode after EP01. Always reference `character_profiles.json` episode-specific visual_prompt_addition. (Added 2026-03-10)
- **RULE:** EP03 visuals = modern Anatolian reality (metrobüs, bazaars, urban crowds). NOT romantic ruins or mystical landscapes. Anti-guru by design.
- **RULE:** EP06 title is "The Perfect Little Worker" — NOT "Corporate Crash / Jealousy.exe". Always check master.md for current episode titles.
- **RULE:** Mentor status in EP07 is "disappearing/fading" — NOT "dying". He simply is no longer there. His absence is the lesson.

---

## CATEGORY: VISUAL PROMPTS

- **RULE:** Every single visual prompt must end with the mandatory suffix. No exceptions, no shortcuts.
- **RULE:** Suffix is: `hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.`
- **RULE:** Never use clean, sterile, or smooth aesthetics. Analog decay is non-negotiable.
- **RULE:** No drama references in music descriptions. Anatolian Prog Rock only.
- **RULE:** Always specify `16:9 widescreen composition` in visual prompts. Without this, Nano Banana defaults to 1:1 square. All production images must be 16:9. (Added 2026-03-07)
- **RULE:** Visual prompts must be CLEAN and TOOL-FRIENDLY. Image generators cannot process narrative metaphors, emotional states, character psychology, or dramaturgical commentary. Write only what is visually renderable: setting, character positions, objects, lighting, colors, composition. "Posture aggressive like a stubborn teenager who knows everything" = useless. "Leaning forward, one arm raised, chin up" = actionable. (Added 2026-03-10)
- **RULE:** When a reference image is provided to the image generator (e.g., Robotiko reference), do NOT repeat the character's full physical description in the prompt. Use a short identifier ("the chrome android") and let the reference image carry the visual details. Long descriptions compete with the reference image and confuse the model. (Added 2026-03-10)
- **RULE:** CHARACTER REFERENCE IMAGES FIRST. Before generating scene images, generate a standalone reference image for each episode-specific character group (e.g., sol-liberal group, wedding guests). Upload this reference image alongside the text prompt for every scene where that group appears. Without this, Nano Banana generates different-looking characters in every scene — breaking visual continuity. (Added 2026-03-13)
- **RULE:** ENVIRONMENT REFERENCE IMAGES FIRST. For locations that appear in multiple scenes (e.g., sanayi sitesi in S40-S44), generate a standalone environment reference image first. Upload this environment image alongside the text prompt for every scene set in that location. Without this, Nano Banana generates inconsistent environments across scenes sharing the same location. (Added 2026-03-13)

---

## CATEGORY: DURATION COVERAGE (Added 2026-02-27)

- **RULE:** 1 scene ≠ 1 clip. Always calculate scene duration (from timestamps) vs. tool capacity (5s or 10s). Scenes longer than 10s require multi-clip coverage with sub-clips.
- **RULE:** Mode C (Extension/Variable) does not exist as a real tool capability. All video generation tools produce fixed-duration clips: 5s or 10s. Plan accordingly.
- **RULE:** Speed ramp maximum is 1.5× slowdown (e.g., 10s clip → 15s). Beyond 1.5× looks unnatural.
- **RULE:** Multi-clip sub-clips must use varied camera moves — not identical repetitions of the same motion.
- **RULE:** When a sub-clip needs a new image, include a complete supplementary visual prompt inline in the motion script (with mandatory suffix). The motion script must be self-contained.
- **RULE:** Coverage target: total generated clip duration ≥ 95% of total music duration.
- **RULE:** Kling 3.0 Multi-Shot: Use for multi-clip shots where sub-clips share the same source image AND are all Kling 3.0. Produces one continuous video (max 15s), smoother transitions, lower credit cost. Segments can be 5-8s each. Mark as `Multi-Shot` (not `Multi-Clip`) in motion script. If sub-clips use different tools or different source images → standard Multi-Clip (separate generations). (Added 2026-03-08, tested on EP02 S34b+c)

---

## CATEGORY: MOTION PROMPTS (Added 2026-02-27)

- **RULE:** Motion prompts are fed directly to Kling/Veo. Write ONLY what the tool can see and execute. Pure visual + motion descriptions.
- **RULE:** NEVER include in motion prompts: musical instrument names (Hammond, fuzz guitar), character names (Robotiko, Mentor), narrative commentary, speed ramp technical notes, audience direction, poetic metaphors, timing cues (BPM, "on the downbeat").
- **RULE:** Musical context belongs in the "Musical Moment" field. Narrative context belongs in the "Scene Context" field. The Motion Prompt field is ONLY for the video generation tool.
- **RULE:** Describe characters by their visual appearance ("chrome android", "robed figure with glowing staff"), never by name.
- **RULE:** NEVER use split-screen / multi-panel compositions in motion prompts. Video generators cannot handle "zoom into left panel", "right panel slides off-frame", or any panel-based movement. If the source image is a split-screen, treat it as a single flat image and describe only simple camera movement + atmospheric motion (dust, smoke, light shifts). (Added 2026-03-07)
- **RULE:** Keep motion prompts SIMPLE. One primary action only. No complex choreography (character A does X while character B does Y while camera does Z). Video generators produce best results with: 1 camera move + 1-2 atmospheric elements (dust, smoke, light). If a scene requires complex action, simplify to the aftermath or a single key moment. (Added 2026-03-07)
- **RULE:** Motion prompts must be SHORT — max 2-3 sentences before the video suffix. Describe atmosphere + main action with strong keywords, NOT micro-level visual details. Video tools respond to mood words (glowing, hypnotic, charred, decay) better than literal descriptions (halftone dots large as coins, paper fibers visible as individual strands). Over-detailed prompts confuse the model. (Added 2026-03-09, EP02 S29 lesson)
- **RULE:** CHARACTER MOVEMENT DIRECTION must be EXPLICIT. "Steps through the doorway" is ambiguous — the video generator may move the character in the wrong direction. Instead, describe the full action sequence: "walks away from the table, exits the room through the doorway into daylight." Specify what the character moves AWAY FROM and TOWARD, not just the destination. Also specify where the camera stays: "the camera stays inside" prevents it from following the character out. (Added 2026-03-13, EP03 S03 lesson)
- **RULE:** ANTI-SPAWN GUARD — Every motion prompt MUST end with "Do not add extra characters. Keep everything as pictured." after the video suffix. Video generators (Kling, Veo, Seedance) spawn phantom characters in backgrounds — flickering, glitching figures that waste credits on retakes. This guard line prevents the tool from adding elements not present in the source image. Apply to ALL prompts, not just crowd scenes. (Added 2026-03-14, EP03 S22 lesson)
- **RULE:** CROWD SCENE MICRO-MOTION — In scenes with multiple characters, NEVER use plural group descriptions ("smiling touts", "beckoning men") or broad gestures ("leaning in", "gesturing warmly"). Instead: (1) specify exact character count and appearance ("four men in black vests"), (2) state "remain in their exact positions", (3) limit movement to micro-actions only (subtle head nods, slow head pan, slight tilt), (4) add environmental motion for liveliness (neon flicker, smoke drift) instead of character movement. Plural descriptions + broad gestures cause AI to spawn duplicate characters and distort limbs. (Added 2026-03-17, EP03 S22 lesson)

---

## CATEGORY: PIPELINE & FILES

- **RULE:** Musical metadata JSON is all-in-one — produced by Gemini Tool. Never ask the human to add more data to it. It is complete as delivered.
- **RULE:** Never reference `video_strategy_rules.md` — it does not exist. All strategy rules are in `_management/pipeline_rules.md`.
- **RULE:** Seedance Multiframes costs ~565 credits per generation (~1130cr for 2 tests). CapCut Pro monthly budget is 1200cr. Never assign Multiframes for production — budget-destroying.
- **RULE:** Raw folders (`04_visuals/raw/`, `05_video/raw/`) are gitignored. Never try to commit files from these folders.
- **RULE:** Seedance 1.0 performs well on character/figure scenes (Robotiko, people) but POORLY on abstract/texture content (maps, macro surfaces, paper textures). For map/texture shots, prefer Kling 2.5 Turbo (static camera) or Kling 3.0 (camera movement). Reserve Seedance for character-focused scenes where its budget advantage matters. (Added 2026-03-09, EP02 S29 lesson)
- **RULE:** Selected files have no version suffix. `ep{XX}_s{XX}_selected.png` — not `ep{XX}_s{XX}_selected_v01.png`.
- **RULE:** Musical metadata JSON has no version suffix. It is always `ep{XX}_musical_metadata.json`.
- **RULE:** Never use generic "Kling AI Pro" in motion scripts. Always specify the exact model: **Kling 2.5 Turbo** for Static camera shots, **Kling 3.0** for shots with camera movement (zoom, dolly, tilt, crane, pan). Mode B (keyframe) shots always have camera movement → always Kling 3.0. (Added 2026-03-29, EP04 motion script correction)

---

## CATEGORY: COMMUNICATION

- **RULE:** Always communicate with the human in Turkish. All files and commits in English.
- **RULE:** Do not over-explain decisions. Deliver first, explain briefly after.
- **RULE:** Do not ask unnecessary clarifying questions for clear tasks. Execute and deliver.
- **RULE:** When providing file content, use artifacts — do not paste raw markdown in chat.

---

## CATEGORY: WORKFLOW

- **RULE:** Two mandatory checkpoints exist. Never skip them:
  1. Dramaturgy must be human-approved before visual prompts begin.
  2. Motion script must be human-approved before video generation begins.
- **RULE:** Always ask "Would Fibula approve this?" before delivering any output.
- **RULE:** If a task goes wrong mid-execution: STOP, re-plan, inform human, then continue.

---

## CATEGORY: IMAGE FIDELITY & REPRESENTATION (Added 2026-03-01)

- **RULE:** Video generators will attempt to "clarify" ambiguous visual elements (silhouettes → realistic people, blurred shapes → detailed objects). Motion prompts must explicitly protect abstract/intentional elements with preservation language: "maintain as featureless dark shapes, do not resolve into detailed figures."
- **RULE:** Source images are production-ready. Video generators must animate them faithfully — not reinterpret, enhance, or "improve" visual elements. If a background has abstract silhouettes, the video must keep them abstract.
- **RULE:** All crowd, audience, mob, and group scenes must include mixed gender representation. Never write "suited figures" or "strikers" without specifying "mixed men and women." This applies to both visual prompts and motion prompts.
- **RULE:** Background crowds in Davos scenes, protest scenes, mine scenes, and any public setting must reflect realistic demographics — not uniform rows of identical male figures.

---

## CATEGORY: ASPECT RATIO & VIDEO SUFFIX (Added 2026-03-01)

- **RULE:** "vintage anamorphic lens" in the video suffix was pushing video generators toward 2.35:1 or 2.39:1 aspect ratios instead of 16:9. Replaced with "cinematic 16:9 framing" across all pipeline files.
- **RULE:** The mandatory video suffix is now: `Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.`
- **RULE:** Veo (and similar models) tends to maintain the source image's original aspect ratio. If the source image is 1:1, the output will be 1:1 — not automatically 16:9. Pre-process reference images to 16:9 before uploading, OR set 16:9 in the tool's aspect ratio settings.
- **RULE:** When in doubt about aspect ratio, add "16:9 aspect ratio, widescreen format" at the beginning of the motion prompt as an explicit override.

---

## CATEGORY: CHARACTER DESIGN (Added 2026-03-23)

- **RULE:** Never write "amber eyes" or "glowing [color] eyes" in visual prompts. Image generators render literal glowing eyeballs = alien/creepy, not wise/benevolent. Instead, use "amber waves radiating around their eyes" or "soft golden light rippling outward from their gaze." The symbolic meaning (wisdom, truth, inner sight) is conveyed through aura/emanation around the eyes, not by changing the eye color itself. (Added 2026-03-23, EP04 Kindred Souls lesson)

---

*Add new lessons below as they emerge during production.*