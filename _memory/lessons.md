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
- **RULE:** EP03 visuals = modern Anatolian reality (metrobüs, bazaars, urban crowds). NOT romantic ruins or mystical landscapes. Anti-guru by design.
- **RULE:** EP06 title is "The Perfect Little Worker" — NOT "Corporate Crash / Jealousy.exe". Always check master.md for current episode titles.
- **RULE:** Mentor status in EP07 is "disappearing/fading" — NOT "dying". He simply is no longer there. His absence is the lesson.

---

## CATEGORY: VISUAL PROMPTS

- **RULE:** Every single visual prompt must end with the mandatory suffix. No exceptions, no shortcuts.
- **RULE:** Suffix is: `hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.`
- **RULE:** Never use clean, sterile, or smooth aesthetics. Analog decay is non-negotiable.
- **RULE:** No drama references in music descriptions. Anatolian Prog Rock only.

---

## CATEGORY: DURATION COVERAGE (Added 2026-02-27)

- **RULE:** 1 scene ≠ 1 clip. Always calculate scene duration (from timestamps) vs. tool capacity (5s or 10s). Scenes longer than 10s require multi-clip coverage with sub-clips.
- **RULE:** Mode C (Extension/Variable) does not exist as a real tool capability. All video generation tools produce fixed-duration clips: 5s or 10s. Plan accordingly.
- **RULE:** Speed ramp maximum is 1.5× slowdown (e.g., 10s clip → 15s). Beyond 1.5× looks unnatural.
- **RULE:** Multi-clip sub-clips must use varied camera moves — not identical repetitions of the same motion.
- **RULE:** When a sub-clip needs a new image, include a complete supplementary visual prompt inline in the motion script (with mandatory suffix). The motion script must be self-contained.
- **RULE:** Coverage target: total generated clip duration ≥ 95% of total music duration.

---

## CATEGORY: MOTION PROMPTS (Added 2026-02-27)

- **RULE:** Motion prompts are fed directly to Kling/Veo. Write ONLY what the tool can see and execute. Pure visual + motion descriptions.
- **RULE:** NEVER include in motion prompts: musical instrument names (Hammond, fuzz guitar), character names (Robotiko, Mentor), narrative commentary, speed ramp technical notes, audience direction, poetic metaphors, timing cues (BPM, "on the downbeat").
- **RULE:** Musical context belongs in the "Musical Moment" field. Narrative context belongs in the "Scene Context" field. The Motion Prompt field is ONLY for the video generation tool.
- **RULE:** Describe characters by their visual appearance ("chrome android", "robed figure with glowing staff"), never by name.

---

## CATEGORY: PIPELINE & FILES

- **RULE:** Musical metadata JSON is all-in-one — produced by Gemini Tool. Never ask the human to add more data to it. It is complete as delivered.
- **RULE:** Never reference `video_strategy_rules.md` — it does not exist. All strategy rules are in `_management/pipeline_rules.md`.
- **RULE:** Seedance Multiframes costs ~565 credits per generation (~1130cr for 2 tests). CapCut Pro monthly budget is 1200cr. Never assign Multiframes for production — budget-destroying.
- **RULE:** Raw folders (`04_visuals/raw/`, `05_video/raw/`) are gitignored. Never try to commit files from these folders.
- **RULE:** Selected files have no version suffix. `ep{XX}_s{XX}_selected.png` — not `ep{XX}_s{XX}_selected_v01.png`.
- **RULE:** Musical metadata JSON has no version suffix. It is always `ep{XX}_musical_metadata.json`.

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

*Add new lessons below as they emerge during production.*