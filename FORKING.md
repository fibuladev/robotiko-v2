# Your own universe in an afternoon

This repo is a **method** wearing a **universe**. The universe is ROBOTIKO — one
story, canon-locked. The method underneath is MIT-licensed and built to be taken:
fork it, swap the story, and direct your own stage-gated film series. This page is the
shortest true path from clone to a green gate on *your* universe.

Every step below was **executed and timed** against a second, deliberately different
universe (a neo-noir called "Silhouette City"). The honest transcript — every failure
verbatim, every fix — is [docs/fork-dry-run.md](docs/fork-dry-run.md). The durations
here are the ones measured in that run, not estimates.

> **The promise, stated plainly.** The *plumbing* — clone, swap suffix, swap cast,
> scaffold, adjust the gate for a foreign universe — took **under 15 minutes** in the
> dry run. The scaffold itself took **one second**. The rest of your afternoon is the
> part only you can do: writing your canon and directing your first episode (or the
> minutes the skills spend doing it with you).

---

## The three commands

```bash
git clone https://github.com/fibuladev/robotiko-v2.git my-universe   # 1. take the method
python scripts/create_episode.py 01                                  # 2. scaffold your first episode (~1s)
python tests/run_all.py                                              # 3. the one gate — keep it green
```

Everything else is editing files. `bash setup_project.sh` is idempotent and safe to
run first if you want the bare directory tree laid down explicitly.

---

## The files you change (the whole list)

Check them off. Paths are exact. This is the complete set the dry run touched —
nothing hidden downstream.

### Your universe (creative — this is the point)
- [ ] **`_management/master.md`** — replace with *your* canon: world, arc, rules, tone,
      and your two mandatory suffixes. Everything downstream reads from here, so it
      comes first.
- [ ] **`_assets/cast/character_profiles.json`** — replace with your cast. It is a
      *state machine*: each character's visual state per episode is tracked here and the
      visual-prompt stage enforces it.
- [ ] **`_assets/cast/character_profiles.schema.json`** — rename the required
      protagonist key (ROBOTIKO's is `robotiko`) to your lead's, and its property block.
      The character-profiles validator reads this schema *dynamically*, so once the JSON
      and schema agree, it simply passes — no code to touch.
- [ ] Drop your character reference images into **`_assets/cast/`** (`ref_*.png`).
      Placeholders are fine at first — the reference-first guard only checks the file
      *exists*, not that it is finished art.

### The gate constants (mechanical — one file plus CLAUDE.md)
- [ ] **`tests/universe_config.py`** — the single source the gate reads. Set:
      `VISUAL_SUFFIX`, `VIDEO_SUFFIX`, `FORBIDDEN_AESTHETICS`, and — the binding the dry
      run added for exactly this purpose — `PROTAGONIST_KEY` and
      `PROTAGONIST_IDENTIFIERS` (which `character_profiles.json` key is your lead, and
      the scene-text strings that mark a scene as featuring them). Point these at your
      lead and the phase / reference-integrity checks enforce *your* character; leave a
      foreign key unbound and they degrade to no-ops instead of crashing.
- [ ] **`CLAUDE.md`** — change the same two suffixes here, where the skills read them
      when they generate prompts. Change only `universe_config` and the skills drift
      from the gate; change only `CLAUDE.md` and the gate stays red demanding the
      ROBOTIKO suffix.

### The foreign-universe adjustments the dry run discovered (do these once)
- [ ] **Remove the ROBOTIKO episodes.** `rm -rf episode-0* episode-10`. The suffix swap
      invalidates every ROBOTIKO prompt file by design — you cannot both swap the suffix
      and keep those episodes green. Removing them is a fork step, not a failure.
- [ ] **Prune `tests/doc_reference_check.py`'s `CURATED_DOCS`.** It lists ROBOTIKO
      worked-example docs that cite specific ROBOTIKO episode files; once those episodes
      are gone, drop the docs you are not keeping (and rewrite the method docs you keep
      to cite your own episode). Add *your* load-bearing docs in their place.
- [ ] **Handle the meta-tests.** `tests/test_validators.py` "grades the graders" against
      frozen ROBOTIKO fixtures and the ROBOTIKO shipped tree; it is mutually exclusive
      with the suffix swap. Keep `tests/fixtures/` as inherited proof the graders work,
      then disable the "Validator meta-tests" group in `tests/run_all.py` until you have
      your own episodes to write your own meta-tests against.
- [ ] **Rewrite the ledger + status.** `_management/approvals.json` and
      `_management/project_metadata.json` — replace the ROBOTIKO records with your
      episodes. (Leaving them causes only non-blocking stale-approval warnings, but keep
      it honest.)
- [ ] **Optional: `EPISODE_FORBIDDEN` in `tests/visual_prompt_validator.py`.** These are
      ROBOTIKO's per-episode phase semantics, keyed by episode number. EP01 ="clean, no
      damage" happened to fit the noir lead's Phase 1 with no edit; if your episode→phase
      mapping differs, adjust this map.

---

## The two human gates — where taste enters

The method is not the point; the *gates* are. Two approvals are mandatory and never
automated, per [`_management/pipeline_rules.md`](_management/pipeline_rules.md):

1. **After dramaturgy** — you approve the scene-by-scene breakdown before any visuals.
2. **After the motion script** — you approve camera moves and tech strategy before any
   video.

Everything between them, the crew (Claude, via the `_skills/`) executes. Remove the
gates and you have automation making noise; keep them and you have a directed film.
They are recorded as data in `_management/approvals.json` — the gate checks that an
artifact past a human gate has an honest approval record.

---

## Keep the gate green

Drive the pipeline stage by stage with the trigger phrases in
[`CLAUDE.md`](CLAUDE.md) and [docs/skills-guide.md](docs/skills-guide.md): musical
metadata → dramaturgy → **gate 1** → visual prompts → motion script → **gate 2** →
edit. Each stage's output is the next stage's input. Then run the one gate:

```bash
python tests/run_all.py
```

**When it goes red, read the message — it names the file and the line.** The dry-run
log shows the shapes you will actually see:

- `FAIL [Suffix Missing] Prompt #3` → a visual prompt does not end in your
  `VISUAL_SUFFIX`. Append it.
- `KeyError: 'robotiko'` / a crash in the visual sweep → you set `PROTAGONIST_KEY`
  but a profile field is missing; the fixed helpers no-op on a truly absent key, so
  this means a half-edited profile. Check `character_profiles.json`.
- `references missing path: episode-0X/...` in doc reference integrity → a curated doc
  cites a file you deleted. Prune `CURATED_DOCS` or fix the citation.
- `motion prompt #N missing anti-spawn guard` / `camera move ... used ... 33%` →
  the motion-script rules. Add the guard; diversify the camera.

No paid tool is needed to reach a green gate — stages 1–4 are pure text. The
zero-cost, one-evening slice is written up in
[docs/text-only-first-episode.md](docs/text-only-first-episode.md).

---

## Register your universe

When you have something — even one episode, even mostly-ROBOTIKO-shaped and honestly
labeled — add it to [UNIVERSES.md](UNIVERSES.md) via the universe-showcase issue
template. The single most useful thing you can include is **the one thing that broke**
when your canon hit an assumption the method made for ROBOTIKO. That is how the method
gets more general.

> **ROBOTIKO canon is not your ceiling — the method is your floor.** The story here is
> one universe the pipeline happened to grow up around. The suffix, the cast, the eight
> stations, the prog-rock aesthetic — all of it is yours to throw away. What is worth
> keeping is the machine underneath: the stages, the two gates, and a single gate
> command that stays honest about what it does and does not guarantee. Take that.
> Tell your own story.

*Proof this page is not theory: [docs/fork-dry-run.md](docs/fork-dry-run.md) — every
step above was executed and timed.*
