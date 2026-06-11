# Tools Setup Guide
> **Version:** 2.0 | **Status:** Golden — open-source release.
>
> ROBOTIKO v2.0 is a one-person, LLM-directed film-production pipeline. This guide explains
> each tool in the chain: what it does, when to use it, how to set it up, and the
> hard-won rules that keep its output consistent. Read it alongside
> **[getting-started.md](getting-started.md)** and **[skills-guide.md](skills-guide.md)**.

---

## Overview

Each tool owns one stage of the pipeline. The director (Claude Code) orchestrates the
sequence; the human approves at two checkpoints (after dramaturgy, after motion script).

| Tool | Stage | Purpose |
|---|---|---|
| **Claude Code** + VSCode | Direction | Reads `CLAUDE.md`, runs skills: dramaturgy, visual prompts, motion scripts |
| **Suno** | Music | Audio generation from human lyrics |
| **BandLab** | Mastering | Loudness / polish pass on the Suno output |
| **Nano Banana** | Visuals | Image generation from prompts (reference-image-first) |
| **Kling / Veo / Seedance** | Video | Motion generation from selected images |
| **CapCut** | Edit | Unification, beat sync, final 4K export |
| **GitHub** | Version Control | All text files, all history |
| **Google Drive** (custom MCP) | Binary archive | PNG, MP4, WAV via `_tools/mcp-gdrive/` |

> **Pricing note:** tool plans change often. Where this guide does not cite a concrete figure
> from a project file, pricing varies — check the tool's site. The only verified figure here is
> the Seedance Multiframes cost (see the video section).

---

## 1. Claude Code — the Director

Claude Code is the brain of the pipeline. It reads the project, runs the skills, validates
file names, and drives every creative stage from lyrics-metadata through CapCut guides.

**Install:** https://docs.claude.com/en/docs/claude-code

### Auto-read project context
On every session start, Claude Code automatically reads **[../CLAUDE.md](../CLAUDE.md)** at the
project root. That file defines the director's role, the mandatory suffixes, the golden rules,
the skill trigger table, and the file-naming convention. You do not paste it in — opening the
project is enough.

### Naming-convention hook
A hook is configured in `.claude/settings.json` as a **PostToolUse** action on the **Write**
tool. After any file write, it validates the new file name against the project naming convention
(`ep{XX}_..._v{VV}` form, two-digit episode/scene numbers, `v01` never `v1`). This catches a
mis-named output the moment it is created, before it ever reaches a commit.

### Reasoning-effort guidance
Match the per-session reasoning effort to the task (per `CLAUDE.md`, "Thinking Effort Protocol"):

| Task | Effort | Why |
|---|---|---|
| Dramaturgy, motion script | **High / Max** | Single-shot deep synthesis — music + arc + camera reconciled in one irreversible pass |
| Concept notes, creative discussion | **High** | Iterative; depth comes from back-and-forth |
| Standard visual prompts | Low / Medium | Template-driven |
| YouTube packaging, naming validation, file ops | **Low** | Mechanical |

Budget priority when constrained: **Dramaturgy > Motion Script > Visual Prompts.**

---

## 2. Suno (music) + BandLab (mastering)

The audio stage. The human writes the lyrics; the tools produce and polish the track.

### Suno — generation
Suno generates the song audio from the human-written lyrics and a style prompt
(Anatolian Prog Rock — never "drama"). Output is the episode's raw track.

**Setup:** create a Suno account at the tool's site. Pricing varies — check the tool's site.

### BandLab — mastering
BandLab runs a loudness/polish pass on the Suno output so levels sit right for YouTube.

**Setup:** create a free BandLab account; use its mastering tool on the exported track.

### What feeds the pipeline
After the track is finalized, the human measures and supplies three things, which feed the
**musical-metadata** skill (`"Create musical metadata for EP{XX}"`):

1. **BPM** and **Key** — from [vocalremover.org/key-bpm-finder](https://vocalremover.org/key-bpm-finder)
2. **Timestamped lyrics** — line-by-line timings

Claude turns these into `ep{XX}_musical_metadata.json` — the all-in-one temporal skeleton
(sections, timestamps, energy, mood, instruments, lyrics) that every later stage anchors to.
This JSON has no version suffix and is complete as delivered; never ask the human to add to it.

---

## 3. Nano Banana — Image Generation

Nano Banana turns approved visual prompts into the still frames that become video source images.
Output: `episode-{XX}/04_visuals/raw/ep{XX}_s{XX}_v{XX}.png`.

**Setup:** access via the tool's site. Pricing varies — check the tool's site.

### Reference-image-first workflow
This is the single most important practice for visual consistency:

- **Generate reference images first.** Before scene images, create a standalone reference for
  each recurring character group and each multi-scene location. Upload that reference alongside
  the text prompt for every scene where it appears. Without this, Nano Banana draws a different
  face / different environment in every scene.
- **Previous scene as reference.** Upload the prior scene's output as an extra reference for the
  next scene — same lighting and layout carry through the image, not the text.
- **Keep prompts brief with references.** If a detail is visible in the reference image, do NOT
  describe it again — re-describing causes the generator to add or exaggerate the feature.
- **Prompt order (literal, not prose):**
  `[Camera/Shot Type] → [Subject + physical details] → [Action/State] → [Background] → [Lighting] → [Guards] → [Style Suffix]`.
  No metaphors (they render literally), no contradictory terms, no abstract size comparisons.

### Eye-material rule (two-part)
Never write "amber eyes," "glowing eyes," any glow keyword, or a negative like "no glow"
(the generator latches onto "glow" and renders glowing eyeballs). Instead, describe the eyes as
a **physical material**:

> dark amber glass lenses set into chrome sockets, like polished gemstones — warm brown-gold
> tone, reflective, catching the environment light on their smooth curved surface.

The two parts: (1) **solid material, not a light source** ("glass lenses," "like polished
gemstones"); (2) **reflective, not emissive** ("catching the environment light").

### Anti-spawn guard
Image generators spawn duplicate androids. Add an explicit count guard to every
single-character scene prompt:

> only ONE chrome android, no second robot

(Deliberate multi-figure shots are the exception — there you state the exact count and guard
only against a third figure.)

### Aspect ratio
Always specify `16:9 widescreen composition` in every prompt. Without it Nano Banana defaults
to 1:1 square, which breaks the whole 16:9 production format.

### Mandatory visual suffix
Every single visual prompt ends with this, verbatim — no exceptions:

```
hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
```

---

## 4. Kling / Veo / Seedance — Video Generation

Three video tools animate the selected still images. The motion script (per clip) recommends
which tool to use; the human makes the final call during generation. Output:
`episode-{XX}/05_video/raw/ep{XX}_s{XX}_video_{tool}.mp4`.

### When to use each

| Tool | Use it for | Notes |
|---|---|---|
| **Kling 2.5 Turbo** | Static-camera shots (no zoom/dolly/tilt/pan) | Always name the exact model, never generic "Kling AI Pro" |
| **Kling 3.0** | Any shot with camera movement; Mode B keyframe shots | Supports **Elements** (`@Name` tags, max 2/clip, character consistency) and **Omni References** (reference-image consistency — tested same cost as standard Kling 3.0, default for EP08+) |
| **Veo** | Free option; needs its dedicated Gemini-style prompt format (below) | Tends to keep the source image's aspect ratio — set 16:9 explicitly. Prone to "decay spawn" (adds leaks/water/cobwebs to interior/analog scenes) — guard against it |
| **Seedance** | Character / figure scenes (Robotiko, people); budget-efficient | Poor on abstract/texture content (maps, macro surfaces) — use Kling there. Runs **inside CapCut** |

> **Seedance Multiframes is BANNED for production.** It costs ~**565 credits per generation**
> (~1130 cr for two tests) against a 1200 cr/month CapCut Pro budget — a single use nearly
> empties the month. Never assign Multiframes.

### Strategy modes (from the motion script)
- **Mode A — Standard (5s or 10s):** one source image, atmospheric / simple movement.
- **Mode B — Start/End Keyframes (5s or 10s):** two images, for a single clear transformation.
  Mode B works only when both frames share composition/environment and differ in ONE element;
  if it requires both an environment shift and complex action, downgrade to Mode A on the
  highest-weight frame.

There is no "Extension / Mode C" — all tools emit fixed 5s or 10s clips. Cover longer scenes
with multi-clip sub-shots (`s{XX}a`, `s{XX}b`, …) or a speed ramp (max 1.5× slowdown).

### Veo prompt format (dedicated)
Veo does NOT respond to the standard motion-prompt format. Use this Gemini-optimized form for
every Veo clip — note the anti-spawn guard goes at the **top**, and the suffix is shortened:

```
Animated version of the attached image. Maintain 100% visual fidelity to the original scene. Do not add any new characters, people, or objects. The environment and background must remain completely static and unchanged.
Action: [Specific motion — state what stays still AND what moves, with direction and speed]. 35mm film aesthetic, heavy film grain, shallow depth of field, Kodachrome color palette.
```

For interior/analog scenes also forbid decay explicitly ("Do not add water drops, leaks,
dripping, moisture … all surfaces remain completely static and dry").

### Anti-spawn guard (all tools)
Every motion prompt (Kling/Seedance form) ends with this line after the suffix:

> Do not add extra characters. Keep everything as pictured.

### Mandatory video suffix
Every single motion prompt ends with this, verbatim — no exceptions (Kling/Seedance form;
Veo uses its shortened variant above):

```
Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.
```

---

## 5. CapCut — Edit & Unification

CapCut Pro is where clips from three different AI tools become one coherent film. The
**capcut-editor** skill (`"Edit EP{XX} in CapCut"`) generates a per-episode edit guide with the
exact timeline map, speed ramps, and effect settings. Final output:
`episode-{XX}/06_edit/ep{XX}_final_v{VV}.mp4`.

**Setup:** CapCut Pro subscription (the Pro tier removes watermarks and unlocks .cube LUT import).
Pricing varies — check the tool's site.

### Unification protocol
Apply these to all clips, in this order, on a single full-timeline **Adjustment Layer**:

1. **Kodachrome LUT** — import a `.cube` Kodachrome 64 emulation; sets the warm 70s base palette.
2. **Color Match** — pick the clip with the best Kodachrome warmth as reference; match all
   others to it (this is what reconciles Kling's cooler tone, Veo's saturation, Seedance).
3. **Film Grain** — **10–15%** overlay on every clip; breaks AI smoothness into organic texture.
4. **Vignette** — subtle (15–25%) edge darkening.
5. **Letterbox 2.35:1** — Player → Ratio → Customized → 2.35:1. Cinematic black bars; hides edge
   artifacts. This is the project's permanent standard across all episodes — do not remove it.

### Beat sync
Run **Auto Beat Detection** on the audio track, then align clip boundaries to the beat-sync
checkpoints in the motion script: chorus entries land on the first chorus beat, drops/impacts on
the downbeat, silence/stillness begins exactly when the music drops.

### Transitions
Hard cut is the default. Allowed extras only: Cross Dissolve (map → location), Light Leak (chorus
entries, max 3/episode, warm amber), Fade to Black (final shot only). Forbidden: glitch, zoom,
spin, slide, wipe, swipe, shape, or any "trendy" preset — they break the analog aesthetic.

### Export
4K (3840×2160), 24 fps, H.265 (HEVC), 35–60 Mbps, MP4, no watermark.

Full step-by-step (9-phase assembly, LUT sources, QA checklist) is in the skill:
`_skills/robotiko-capcut-editor/SKILL.md`.

---

## 6. Google Drive MCP — Binary Archive

Git holds the text; **Google Drive holds the binaries** (PNG, MP4, WAV). A custom, ~300-line MCP
server in `_tools/mcp-gdrive/` lets Claude Code upload and organize these assets through natural
language. This is the project's only cloud archive — there is no S3 bucket.

> Full setup, the upload walkthrough, and troubleshooting live in
> **[../_tools/mcp-gdrive/README.md](../_tools/mcp-gdrive/README.md)**. Summary below.

### What it stores
Per-episode folders on Drive, each with `raw/`, `selected/`, `audio/`, `video/` —
holding the generated PNGs, the curated selects, the WAV audio, and the final MP4 clips.

### Setup summary
1. **Google Cloud:** create a project, enable the **Google Drive API**, configure the OAuth
   consent screen (External, add yourself as a test user), and create a **Desktop app** OAuth
   client ID. Download the credentials JSON.
2. **Install:** `npm install` in `_tools/mcp-gdrive` (needs Node ≥18; deps are only `googleapis`
   and the official `@modelcontextprotocol/sdk`).
3. **Place keys:** move the downloaded file to
   `~/.config/robotiko-mcp-gdrive/gcp-oauth.keys.json` (kept out of the repo by `.gitignore`).
4. **Authenticate:** `npm run auth` — opens the browser, saves a token to
   `~/.config/robotiko-mcp-gdrive/tokens.json`. Tokens expire ~hourly; re-run `npm run auth`
   when an upload fails with a token error.
5. **Register the server:** add a `.mcp.json` at the **project root** (not inside `.claude/`)
   pointing `node` at `_tools/mcp-gdrive/src/index.js`. The `.claude/mcp.json` path does NOT work.
6. **Test:** start a new Claude Code session; the Google Drive tools appear automatically.
   Then just ask, e.g., *"Upload EP04 selected images to Google Drive."*

### Tools exposed
`gdrive_list_folder`, `gdrive_search`, `gdrive_create_folder`, `gdrive_upload`, `gdrive_move`.

---

## Related Documentation

- **[getting-started.md](getting-started.md)** — first-run setup and the pipeline at a glance
- **[skills-guide.md](skills-guide.md)** — what each skill does, with a worked example
- **[../CLAUDE.md](../CLAUDE.md)** — director role, golden rules, mandatory suffixes, trigger table
- **[../_management/pipeline_rules.md](../_management/pipeline_rules.md)** — full stage-by-stage workflow and QA gates
- **[../_management/youtube_metadata_standards.md](../_management/youtube_metadata_standards.md)** — title/description/tag standards for upload
- **[../_tools/mcp-gdrive/README.md](../_tools/mcp-gdrive/README.md)** — Google Drive MCP full setup
