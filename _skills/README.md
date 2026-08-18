# 🤖 CLAUDE SKILLS

Skills are operational instructions for Claude AI to execute specific workflows.

## Available Skills (10)

1. **robotiko-musical-metadata** - Build the temporal metadata JSON from BPM, key, and timestamped lyrics
2. **robotiko-dramaturgy** - Generate scene-by-scene breakdowns [HUMAN GATE 1]
3. **robotiko-visual-prompts** - Two-phase Nano Banana image prompts: reference sheet first, scene prompts after [HUMAN GATE 1R]
4. **robotiko-motion-script** - Generate Kling/Veo/Seedance video prompts [HUMAN GATE 2]
5. **robotiko-episode-scaffold** - Auto-create episode folder structure
6. **robotiko-naming-enforcer** - Validate file naming conventions
7. **robotiko-youtube-packager** - Generate YouTube metadata
8. **robotiko-reels-atomizer** - Extract social media clips
9. **robotiko-launch-orchestrator** - Master launch coordinator
10. **robotiko-capcut-editor** - CapCut post-production edit guide

> Full guide with triggers, inputs, outputs, and a worked example: [`docs/skills-guide.md`](../docs/skills-guide.md).

## Model Recommendations

- **Creative Skills** (dramaturgy, visuals, motion): Opus — high to max thinking effort
- **Mechanical Skills** (scaffolding, naming): low thinking effort (a lighter model is fine here)

## Human Gates

Three approval gates are mandatory and pinned by sha256 in `_management/approvals.json`:

| Gate | Where | What the human approves |
|---|---|---|
| **GATE 1** | after `robotiko-dramaturgy` | the scene breakdown, before any prompt is written |
| **GATE 1R** | inside `robotiko-visual-prompts`, between Phase 1 and Phase 2 | the reference images, before scene prompts are generated |
| **GATE 2** | after `robotiko-motion-script` | the motion script, before any video is generated |

## Usage

In Claude Code/Chat:
```
"Read robotiko-dramaturgy skill and create dramaturgy for ep03"
```

Claude will:
1. Read the SKILL.md file
2. Read necessary project files (_management/master.md, etc.)
3. Execute the workflow
4. Output files to appropriate folders
