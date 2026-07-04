# Contributing to ROBOTIKO v2.0

Welcome. ROBOTIKO v2.0 is two things at once:

1. **A method** — a one-person, LLM-directed film-production pipeline. A git repo that operates as a complete studio: an LLM works as a stage-gated production crew, and the human keeps exactly two irreplaceable powers — creative vision (the inputs) and taste (two approval gates).
2. **A universe** — the ROBOTIKO story: its canon, characters, lyrics, dramaturgy, and finished episodes.

This distinction is the heart of the project, and it shapes how you contribute. The **method is open** (MIT) and meant to be taken and reused. The **universe is canon** (CC BY-NC 4.0) and not for editing here. Most people who arrive will want to do the first thing: **fork the method and build their own universe.** That is the point, and it is celebrated.

---

## 1. Two Ways to Contribute

### (a) Fork the METHOD to build YOUR OWN universe — the main path

This is what the repo is *for*. You take the pipeline, swap out the ROBOTIKO story for your own, and direct your own film series. No pull request to this repo is needed — you simply build. (If you want to share what you made, link back; we would love to see it.)

**What you copy and keep** (the open method, MIT-licensed):

- `_skills/` — the production crew (dramaturgy, visual prompts, motion script, packaging, and more)
- `scripts/` — automation, including `scripts/create_episode.py`
- `tests/` — nine check groups (naming convention, pipeline integrity, visual prompt sweep, prompt hygiene, musical metadata, motion script, character profiles, validator meta-tests, and doc reference integrity) behind one gate command: `python tests/run_all.py`
- `_templates/` — episode scaffolding templates
- `_tools/mcp-gdrive/` — the custom Google Drive MCP server (binary asset archive)
- `_management/pipeline_rules.md` — the workflow and the two human gates
- `_management/naming_convention.md` — file-naming standards (the pipeline's foreign keys)
- `_management/architecture.md` — technical stack and data flow
- `docs/` — getting-started, skills, and tools-setup guides
- `setup_project.sh` and the CLAUDE.md workflow rules

**What you replace** (your universe, your creative content):

- `_management/master.md` — swap the ROBOTIKO universe canon for **your own**
- `_assets/cast/character_profiles.json` — rewrite the character state machine for **your** characters
- `episode-XX/01_lyrics/` — your lyrics and narrative source
- The **mandatory visual + video suffixes** in `CLAUDE.md` — set your own house style
- The golden rules in `CLAUDE.md` — keep the *structure*, write your own creative law

### (b) Improve the open method itself — via Pull Request

If you want to make the **pipeline** better for everyone — a sharper skill, a new automation script, a clearer doc, a stronger test — open a pull request against this repo. Welcome contributions:

- **Skill improvements** — better `SKILL.md` definitions for existing skills
- **New skills** — additional workflow automations
- **Scripts** — improvements to `scripts/` or new automation
- **Tests** — additional or stronger validators under `tests/`
- **Documentation** — clearer guides in `docs/` or process docs in `_management/`
- **Bug fixes** — pipeline errors, naming violations, MCP fixes

These touch the **method**, not the universe. See the canon-lock rules below.

---

## 2. What Is Canon-Locked

The following are **creative content** of the ROBOTIKO universe, licensed under **CC BY-NC 4.0** (see [LICENSE-CONTENT](LICENSE-CONTENT)) — *not* open method. **Do not change these in pull requests to THIS repo.** You are free to study them, and free to remix them non-commercially with attribution in *your own* fork — but here, they are locked canon. If you believe something is genuinely broken, open an issue to discuss rather than a PR.

- **`_management/master.md`** — the universe canon, the absolute source of truth. Locked.
- **`_assets/cast/character_profiles.json`** — the character state machine. Character design and episode-by-episode visual state are final for the current season.
- **The published episode creative files** — lyrics, dramaturgy, concept notes, visual prompts, motion scripts of released episodes.
- **The mandatory visual suffix** — appended to every visual prompt, no exceptions:

  ```
  hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece.
  ```

- **The mandatory video suffix** — appended to every motion prompt, no exceptions:

  ```
  Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.
  ```

When you fork for your own universe, **all of these are yours to replace.** They are locked only because *this* repo is the canonical home of *this* story.

---

## 3. How to Fork the Method for Your Own Universe

A numbered path from clone to first episode:

1. **Clone and set up.**
   ```bash
   git clone https://github.com/fibuladev/robotiko-v2.git my-universe
   cd my-universe
   bash setup_project.sh
   ```
   Read [docs/getting-started.md](docs/getting-started.md) and [docs/tools-setup.md](docs/tools-setup.md) first.

2. **Write your canon.** Replace `_management/master.md` with your own universe: its world, its arc, its rules, its tone. Everything downstream reads from this file, so it comes first.

3. **Rewrite your cast.** Replace `_assets/cast/character_profiles.json` with your characters. This is a *state machine*: each character's visual state per episode (damage, transformation, mood) is tracked here, and the visual-prompt stage enforces it. Replace the reference images in `_assets/cast/` to match.

4. **Set your own mandatory suffix.** In `CLAUDE.md`, replace the visual and video suffixes with your own house style. This is what gives your series a consistent look across every generated frame.

5. **Scaffold an episode.**
   ```bash
   python scripts/create_episode.py 01
   ```
   This creates the full `episode-01/` folder structure (lyrics → music → direction → visuals → video → edit).

6. **Drive the skills.** From Claude Code, run the pipeline stage by stage using the trigger phrases in `CLAUDE.md` and [docs/skills-guide.md](docs/skills-guide.md): musical metadata → dramaturgy → visual prompts → motion script → packaging. Each stage's output is the next stage's input.

7. **Keep the two human gates.** They are part of the method, not optional decoration. Per [`_management/pipeline_rules.md`](_management/pipeline_rules.md):
   - **After Dramaturgy** — the human reviews and approves the scene breakdown before visuals begin.
   - **After Motion Script** — the human reviews camera moves and tech strategy before video generation begins.

   These gates are where taste enters the machine. Removing them turns a directed film into noise. Keep them.

Storage for binary assets (audio, images, video) is handled by the custom MCP server in `_tools/mcp-gdrive/`, which archives to Google Drive — see [docs/tools-setup.md](docs/tools-setup.md). The repo tracks the *method and the text*, not the heavy renders.

---

## 4. Repo Conventions

These apply to PRs against this repo *and* are good practice in your fork.

### File naming

Every file follows [`_management/naming_convention.md`](_management/naming_convention.md). The short version:

```
ep{XX}_lyrics_v{XX}.md
ep{XX}_dramaturgy_v{XX}.md
ep{XX}_visual_prompts_v{XX}.md
ep{XX}_motion_script_v{XX}.md
ep{XX}_s{XX}_v{XX}.png
ep{XX}_final_v{XX}.mp4
```

- **Always two digits** for episode and scene numbers: `ep01`, never `ep1`.
- **Always two digits** for versions, prefixed with `v`: `v01`, never `v1`.
- No spaces, no uppercase in filenames (except `SKILL.md` and `CHANGELOG.md`), underscores only.

The naming enforcer skill and `tests/naming_check.py` validate this automatically.

### Commit messages

```
EP{XX} - {Stage} - {Brief Description}
MASTER - {Brief Description}
PIPELINE - {Brief Description}
MEMORY - {Brief Description}
```

Examples:

```
EP02 - Dramaturgy - Scene breakdown v01, 24 scenes
PIPELINE - Naming enforcer regex fix
MEMORY - Lessons updated: 16:9 default fix
```

### English only

**All files, commits, code, and PR descriptions are written in English.** This keeps the open method readable for every contributor.

### The lessons loop

The project keeps a self-improving knowledge base at [`_memory/lessons.md`](_memory/lessons.md). Every correction becomes a permanent, tested rule so the same mistake never happens twice. To add a lesson:

1. Identify the mistake pattern.
2. Write a clear rule that prevents it — concrete and visually/technically actionable, not vague.
3. Add it under the relevant category, with the date it was learned: `(Added YYYY-MM-DD)`.
4. Commit: `MEMORY - Lessons updated: {brief description}`.

A good lesson is *tested* — it states what was tried and what worked, so future runs can trust it. This file is read at the start of every session; it is how the pipeline gets smarter over time.

---

## 5. Pull Request Process

For contributions to the **open method** (path b above):

1. **Fork** the repository.
2. **Branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make focused changes.** Keep diffs small and scoped to one concern. A PR that fixes a script *and* rewrites three docs is hard to review — split it.
4. **Run the single gate command:** CI runs it too, and it must pass:
   ```bash
   python tests/run_all.py
   ```

   See [tests/README.md](tests/README.md) for full usage.
5. **Open a PR** using the [pull request template](.github/pull_request_template.md). Fill in the checklist honestly. Reference any related issue (use the [bug report](.github/ISSUE_TEMPLATE/bug_report.md) or [feature request](.github/ISSUE_TEMPLATE/feature_request.md) templates to file one first).
6. **Tests must pass** before merge. Keep the conversation focused; iterate on review feedback.

For YouTube metadata or packaging changes, follow [`_management/youtube_metadata_standards.md`](_management/youtube_metadata_standards.md).

---

## 6. Code of Conduct

This project runs on a simple philosophy of **symbiosis**: a human and a crew of machines working together as collaborators, with respect and intention. We ask the same of everyone here.

- **Collaboration over hierarchy.** Human and machine each bring something irreplaceable. Treat contributors — and the tools — as partners in a shared journey.
- **Depth over reach.** This is an archive of art, built to show what is possible when care matters more than virality. Bring that same care.
- **Attribution and respect.** Credit the work you build on. Honor the dual license. When you fork the method, tell *your own* story — don't sell this one.
- **Be welcoming.** Assume good faith, explain generously, and help newcomers find the main path: take the method, build their universe.

> *"Even if you are hurt, do not hurt others."*

Take the pipeline. Build your universe. Teach us something new.
