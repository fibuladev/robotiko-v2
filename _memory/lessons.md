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

## CATEGORY: PIPELINE & FILES

- **RULE:** Musical metadata JSON is all-in-one — produced by Gemini Tool. Never ask the human to add more data to it. It is complete as delivered.
- **RULE:** Never reference `video_strategy_rules.md` — it does not exist. All strategy rules are in `_management/pipeline_rules.md`.
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

*Add new lessons below as they emerge during production.*