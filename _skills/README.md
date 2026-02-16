# 🤖 CLAUDE SKILLS

Skills are operational instructions for Claude AI to execute specific workflows.

## Available Skills

1. **robotiko-dramaturgy** - Generate scene-by-scene breakdowns
2. **robotiko-visual-prompts** - Create Nano Banana image prompts
3. **robotiko-motion-script** - Generate Kling/Veo video prompts
4. **robotiko-episode-scaffold** - Auto-create episode folder structure
5. **robotiko-naming-enforcer** - Validate file naming conventions
6. **robotiko-youtube-packager** - Generate YouTube metadata
7. **robotiko-reels-atomizer** - Extract social media clips
8. **robotiko-launch-orchestrator** - Master launch coordinator

## Model Recommendations

- **Creative Skills** (dramaturgy, visuals, motion): Sonnet 4.5 + Extended Thinking ON
- **Mechanical Skills** (scaffolding, naming): Haiku 4.5 + Extended Thinking OFF

## Usage

In Claude Code/Chat:
```
"Read robotiko-dramaturgy skill and create dramaturgy for ep03"
```

Claude will:
1. Read the SKILL.md file
2. Read necessary project files (_management/bible.md, etc.)
3. Execute the workflow
4. Output files to appropriate folders
