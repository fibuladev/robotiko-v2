# Skills Guide
> **Version:** 1.0 | **Status:** Draft — To be completed at EP10 open source release.

---

## What are Skills?

Skills are Claude's operational instructions. Each skill is a `SKILL.md` file that defines exactly how Claude should execute a specific workflow. When you give Claude a trigger phrase, it reads the relevant SKILL.md and follows its instructions precisely.

This eliminates the need to explain the same workflow repeatedly — Claude learns it once from the skill file and executes consistently across all episodes.

---

## Available Skills

| Skill | Trigger Phrase | Output |
|---|---|---|
| `robotiko-dramaturgy` | "Create dramaturgy for EP{XX}" | `ep{XX}_dramaturgy.md` |
| `robotiko-visual-prompts` | "Generate visual prompts for EP{XX}" | `ep{XX}_visual_prompts.md` |
| `robotiko-motion-script` | "Generate motion script for EP{XX}" | `ep{XX}_motion_script.md` |
| `robotiko-episode-scaffold` | "Scaffold EP{XX}" | Full folder structure |
| `robotiko-naming-enforcer` | "Validate file names" | Compliance report |
| `robotiko-youtube-packager` | "Package EP{XX} for YouTube" | Metadata file |
| `robotiko-reels-atomizer` | "Atomize EP{XX} for social" | Clip list |
| `robotiko-launch-orchestrator` | "Orchestrate EP{XX} launch" | Launch checklist |

---

## How Skills Work

1. Human gives trigger phrase
2. Claude reads `_skills/{skill-name}/SKILL.md`
3. Claude reads all prerequisite files listed in the skill
4. Claude executes the workflow
5. Claude delivers the output
6. Human reviews (mandatory checkpoints: Dramaturgy + Motion Script)

---

## Skill Dependencies

```
episode-scaffold
    → lyrics (human)
    → musical-metadata (human + Gemini)
    → concept-notes (human)
    → dramaturgy [✋ CHECKPOINT]
    → visual-prompts
    → (image generation — Nano Banana)
    → motion-script [✋ CHECKPOINT]
    → (video generation — Kling/Veo)
    → youtube-packager
    → reels-atomizer
    → launch-orchestrator
```

---

## Adapting Skills for Your Own Project

Each SKILL.md is designed to be readable and modifiable. To adapt for your own project:

1. Fork this repository
2. Update `_management/master.md` with your own universe bible
3. Update `_assets/cast/character_profiles.json` with your characters
4. Modify skill files to match your aesthetic and narrative rules
5. Update `CLAUDE.md` with your project context

---

*Full skills documentation coming at EP10 open source release.*