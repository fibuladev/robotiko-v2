# A first episode with no paid tools, in one evening

The pipeline has two halves. The **first four stages produce text** — a musical
metadata JSON and three markdown documents — and need nothing but Claude Code and a
song you are legally allowed to use. The **later stages produce pixels** — images,
video, an edit — and that is where the paid tools live.

This guide walks the zero-cost half. At the end you will have a real, validated
episode skeleton that passes `python tests/run_all.py`, produced for the price of an
evening and no subscriptions. It is the honest way to taste the method before you spend
a cent, and it is exactly how far the [fork dry run](fork-dry-run.md) took its own toy
universe before it stopped.

---

## What you need (all free)

- **Claude Code** — the director and crew. It reads [`CLAUDE.md`](../CLAUDE.md) on
  session start.
- **A public-domain song** — a recording you can legally listen to and reference. Public
  audio archives (e.g. pre-1929 recordings, or works released under a permissive
  licence) are full of them. You need to be able to *hear* it, because the pipeline is
  driven by the song's structure.
- **A free BPM/key finder** — the musical-metadata skill points at one
  ([vocalremover.org/key-bpm-finder](https://vocalremover.org/key-bpm-finder)); any
  equivalent works. This is the only "external tool," and it is free.

No Suno, no Nano Banana, no Kling, no CapCut. Those come in the second half, when you
want pixels — see the costs section at the end.

---

## The spine: why this works without images

The whole system hangs off the **musical metadata JSON** (`ep{XX}_musical_metadata.json`).
It is the *temporal source of truth* — sections, timestamps, energy, mood. Every scene,
every visual prompt, every camera move is anchored to a timestamp in it. Because the
three creative documents (dramaturgy, visual prompts, motion script) are *text that
references that clock*, you can author and validate the entire creative plan of an
episode before a single frame is generated. The images and video are the *execution* of
that plan, not the plan itself.

---

## The evening, stage by stage

First, scaffold the episode (one second, no tools):

```bash
python scripts/create_episode.py 01
```

Then drive the four text stages with the trigger phrases from
[`CLAUDE.md`](../CLAUDE.md) and [skills-guide.md](skills-guide.md). Each phrase tells
Claude which skill to read first.

### Stage 1 — Musical metadata

Trigger: **"Create musical metadata for EP01."** Skill:
[`_skills/robotiko-musical-metadata/SKILL.md`](../_skills/robotiko-musical-metadata/SKILL.md).

This skill is explicit that it **cannot analyze audio** — *you* provide three things by
listening: **BPM**, **key**, and **timestamped lyrics** (section headers mapped to
`MM:SS`). That is the whole reason this stage is free: the human ear plus a free
BPM/key finder replaces any paid analysis. Read your public-domain song's structure,
hand it to Claude in the format the skill specifies, and it emits the JSON. The
musical-metadata validator then checks it: required fields, a known energy/section
vocabulary, monotonic non-overlapping timestamps, and `total_duration` matching the
last section.

### Stage 2 — Dramaturgy → **HUMAN GATE 1**

Trigger: **"Create dramaturgy for EP01."** Skill:
[`_skills/robotiko-dramaturgy/SKILL.md`](../_skills/robotiko-dramaturgy/SKILL.md).

The skill reads, in order, your `_management/master.md`, the metadata JSON from stage 1,
and your concept notes, then writes a scene-by-scene breakdown anchored to the song's
timestamps. **Then you stop.** This is the first mandatory gate: you read the breakdown
and approve it — as yourself, with your taste — before anything else runs. Record the
approval in `_management/approvals.json`. The pipeline-integrity check enforces that an
artifact past this gate has a real approval record; there is no skipping it.

### Stage 3 — Visual prompts

Trigger: **"Generate visual prompts for EP01."** Skill:
[`_skills/robotiko-visual-prompts/SKILL.md`](../_skills/robotiko-visual-prompts/SKILL.md).

From the *approved* dramaturgy, Claude writes one text prompt per scene, each ending in
your mandatory `VISUAL_SUFFIX` and honoring your character's phase state. You generate
no images tonight — you are writing the prompts that *would* generate them. The visual
sweep validates every prompt: the suffix is present, no forbidden aesthetics leak in,
the protagonist renders in the phase-correct state, and each character scene points at
the right reference. All of that is checkable on text alone.

### Stage 4 — Motion script → **HUMAN GATE 2**

Trigger: **"Generate motion script for EP01."** Skill:
[`_skills/robotiko-motion-script/SKILL.md`](../_skills/robotiko-motion-script/SKILL.md).

Claude writes the shot list: camera move per clip, tool assignments, beat sync, each
motion prompt ending in your `VIDEO_SUFFIX` and carrying the anti-spawn guard. The
motion-script validator enforces the camera-diversity rules (no single move over 30%,
a `Static` floor, local variety, an accent-move budget, one move per clip). **Then you
stop again** — the second mandatory gate — and approve the camera language before any
video would be made.

---

## Close the evening green

```bash
python tests/run_all.py
```

Four text artifacts, both gates recorded, and — on a clean episode — a green gate. You
have proven the *process* end to end and paid nothing. What you do **not** have is a
watchable film: no images, no clips, no edit. That is deliberate. You reproduced the
recipe, not the pixels.

---

## When you want pixels — what stage 5+ costs

The moment you want to *see* it, the paid half begins: image generation, video
generation, and the edit. Those costs are laid out honestly, tool by tool, in the
**Expected Costs** section of [getting-started.md](getting-started.md#expected-costs) —
the two subscriptions you actually feel are the LLM (the crew) and the editor (which
also hosts one of the video generators), while image and video credits are spent in
bursts per episode. The minimum viable kit is smaller than the full one; the same page's
FAQ covers running lean and swapping tools.

But none of that is required to *learn the method*. The text-only first episode above is
the real thing — the same stages, the same two gates, the same gate command — just
stopped at the last free step. Start there.
