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

## The three human gates — where taste enters

The method is not the point; the *gates* are. Three approvals are mandatory and never
automated, per [`_management/pipeline_rules.md`](_management/pipeline_rules.md):

1. **After dramaturgy** — you approve the scene-by-scene breakdown before any visuals.
2. **At the reference gate (1R, two-phase episodes, EP10 onward)** — you approve the
   reference images before any Phase-2 scene prompt is written.
3. **After the motion script** — you approve camera moves and tech strategy before any
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

## Non-musical projects

The pipeline was built around music: a song analyzed into a JSON skeleton, every scene
anchored to a beat. But the downstream stages — dramaturgy, visual prompts, motion
script — do not actually read "music." They read **timing, energy, and text**. A section
that starts at 33.0 and ends at 49.0 with energy "medium" and a lyrics field drives a
scene the same way whether the timing came from a song, a voiceover script, or a
hand-drawn storyboard.

If your project has no music, you can still use the full pipeline. Short films, feature
films, web series, video essays, art installations, branded content — the format does
not matter. You replace the **source** of the metadata, not the metadata itself.

### What the pipeline actually reads

The JSON has five things downstream stages care about:

| Field | What dramaturgy/motion use it for | Music source | Non-music equivalent |
|---|---|---|---|
| `sections[].start` / `end` | Scene boundaries, duration | Song timestamps | Your segment plan |
| `sections[].energy` | Visual intensity, camera behavior | Musical dynamics | Pacing intention |
| `sections[].type` | Scene character (intro, climax, outro) | Song structure | Narrative structure |
| `sections[].lyrics` | Dialogue/text to visualize | Song lyrics | Narration, dialogue, or omit |
| `tempo` (BPM) | Beat sync for motion script cuts | Song BPM | Target cuts-per-minute, or omit |

The fields that are truly music-only — `tempo`, `key`, `time_signature`,
`instruments` — are optional in the validator. They exist for the human's reference in
musical projects. You can set them to `null` (or omit them entirely) and the gate stays
green.

### Example: a cooking show episode

Say you are directing a 3-minute cooking segment with four phases: ingredient prep,
active cooking, plating, and tasting. No music, no lyrics — just visual storytelling
with a voiceover.

```json
{
  "track_title": "Shakshuka — Sunday Morning",
  "tempo": null,
  "key": null,
  "time_signature": null,
  "total_duration": 180,
  "mood": ["warm", "domestic", "rhythmic", "appetizing"],
  "instruments": [],
  "sections": [
    {
      "type": "intro",
      "start": 0.0,
      "end": 15.0,
      "energy": "low",
      "notes": "Overhead shot of empty kitchen table. Morning light. Title card."
    },
    {
      "type": "verse",
      "start": 15.0,
      "end": 55.0,
      "energy": "medium",
      "lyrics": "We start with the base — onions, garlic, and peppers, diced small. The pan is already warm.",
      "notes": "Close-ups of knife work. Hands only — no face reveal until plating. Pace: methodical, unhurried."
    },
    {
      "type": "chorus",
      "start": 55.0,
      "end": 110.0,
      "energy": "medium-high",
      "lyrics": "Tomatoes go in. Cumin, paprika, a pinch of sugar. Let it reduce — you want a thick sauce, not a soup.",
      "notes": "Active cooking phase. Steam, sizzle sounds. Camera moves from overhead to 45-degree angle. Energy rises with the heat."
    },
    {
      "type": "bridge",
      "start": 110.0,
      "end": 140.0,
      "energy": "low",
      "lyrics": "Make the wells. Crack the eggs. This is the moment you stop touching it and let the pan do the work.",
      "notes": "Deliberate slowdown — the patience moment. Static camera. Eggs setting in real time, no time-lapse."
    },
    {
      "type": "climax",
      "start": 140.0,
      "end": 165.0,
      "energy": "high",
      "lyrics": "Fresh herbs, a drizzle of olive oil, and it goes straight to the table — in the pan, not on a plate.",
      "notes": "Plating sequence. Colors pop. First face reveal: the cook tasting. This is the visual payoff."
    },
    {
      "type": "outro",
      "start": 165.0,
      "end": 180.0,
      "energy": "fading",
      "notes": "Pull back to the full table. Bread being torn. End card."
    }
  ]
}
```

Notice what happened:

- **Section types** (`verse`, `chorus`, `bridge`, `climax`) are repurposed as pacing
  markers, not musical labels. The dramaturgy skill reads `type` to decide visual
  rhythm — a `chorus` gets more visual intensity than a `verse`, a `bridge` signals a
  tone shift. These meanings transfer directly to non-musical segments.
- **Energy levels** drive camera behavior downstream. A `medium` prep section gets
  steady mid-shots; a `high` plating section gets dynamic close-ups. The mapping works
  because energy describes pacing, not volume.
- **Lyrics field** carries the voiceover script instead of song lyrics. The dramaturgy
  skill uses this text to decide what the scene should show. If you have no voiceover,
  omit the field — the skill falls back to the `notes` field.
- **`tempo` is null.** The motion script skill uses BPM for beat-synced cuts. Without
  it, the skill defaults to scene-duration-based pacing, which is correct for
  non-musical content. You can also set a BPM manually to impose a visual rhythm — say,
  `"tempo": 90` if you want cuts roughly every 2/3 of a second during high-energy
  segments.
- **`mood`** is universal. It feeds the dramaturgy skill's tone decisions regardless of
  whether there is music.

### Example: a documentary episode

A 5-minute documentary segment with interview clips, B-roll, and a closing reflection.

```json
{
  "track_title": "The Bridge Builders of Mostar",
  "tempo": null,
  "key": null,
  "time_signature": null,
  "total_duration": 300,
  "mood": ["contemplative", "resilient", "historical", "human"],
  "instruments": [],
  "sections": [
    {
      "type": "intro",
      "start": 0.0,
      "end": 30.0,
      "energy": "low",
      "notes": "Archival footage of the bridge. No narration — just ambient sound and water."
    },
    {
      "type": "verse",
      "start": 30.0,
      "end": 90.0,
      "energy": "medium",
      "lyrics": "The old bridge stood for 427 years. It took four seconds to destroy it.",
      "notes": "Interview A: historian. Cut between talking head and archival photos. Measured, factual tone."
    },
    {
      "type": "verse",
      "start": 90.0,
      "end": 150.0,
      "energy": "medium",
      "lyrics": "My grandfather swam in that river every summer. We all did. The bridge was just — there.",
      "notes": "Interview B: local resident. Warmer, personal. B-roll of the river today."
    },
    {
      "type": "bridge",
      "start": 150.0,
      "end": 210.0,
      "energy": "building",
      "lyrics": "The reconstruction used the same Ottoman techniques — the same dovetail joints, the same local stone. But the divers had to pull the original stones from the riverbed first.",
      "notes": "Reconstruction process footage. Time-lapse of stonework. Energy builds with the bridge rising."
    },
    {
      "type": "climax",
      "start": 210.0,
      "end": 260.0,
      "energy": "high",
      "lyrics": "When they reopened the bridge in 2004, ten thousand people walked across it. Nobody ran. Everybody walked.",
      "notes": "The emotional peak. Crowd footage. Faces. Slow motion of the first crossing."
    },
    {
      "type": "outro",
      "start": 260.0,
      "end": 300.0,
      "energy": "fading",
      "notes": "The bridge at dusk. Water sound returns. Final title card. No narration — mirror the intro."
    }
  ]
}
```

### The adaptation checklist

If your project has no music:

- [ ] **Set `tempo`, `key`, `time_signature` to `null`** and `instruments` to `[]`
      (or omit them entirely). These fields are optional in the validator — they will not
      cause a red gate.
- [ ] **Plan your segments manually.** Decide how long each segment lasts and what its
      energy arc looks like. Write this as your section array. You are the composer of
      pacing now — the song used to decide this for you; without one, you decide.
- [ ] **Use section types as pacing vocabulary.** `intro` = opening, `verse` = steady
      narrative, `chorus` = heightened intensity, `bridge` = tonal shift, `climax` =
      visual peak, `outro` = closing. The words map to narrative beats, not musical ones.
- [ ] **Put your script in the `lyrics` field.** Voiceover, dialogue, narration — the
      downstream skill reads this field to understand what the scene is about. No script?
      Use `notes` instead.
- [ ] **In `CLAUDE.md`, update the trigger phrase.** Change `"Create musical metadata"`
      to something that fits your workflow — `"Create episode structure"` or
      `"Create timing metadata"`. The skill reads the JSON regardless of what you call it.
- [ ] **The gate still works.** `run_all.py` validates section boundaries, energy
      levels, and structural integrity. It does not validate musicality. Any project's
      JSON with correct timestamps and energy levels passes the same gate.

### What if you *do* have music but it is not the primary content?

Background music under a narration, a score under a film — this is the most common
case outside of musicals. You have two options:

1. **Music-first metadata.** Analyze the background track the same way ROBOTIKO does
   (BPM, sections, energy). Let the music drive the visual rhythm. This is the strongest
   approach if the music was composed or selected to match the content's pacing.

2. **Content-first metadata.** Ignore the background music. Structure your metadata
   around the content's segments (as in the examples above). Add the background track in
   the CapCut edit stage — the music follows the content instead of leading it.

Neither is wrong. ROBOTIKO uses music-first because the project is a musical. A short
film or web series might use content-first because the narrative drives the rhythm, not
a song. A scored project might do either depending on whether the music was purpose-built
or added in post.

---

## Register your universe

When you have something — even one episode, even mostly-ROBOTIKO-shaped and honestly
labeled — add it to [UNIVERSES.md](UNIVERSES.md) via the universe-showcase issue
template. The single most useful thing you can include is **the one thing that broke**
when your canon hit an assumption the method made for ROBOTIKO. That is how the method
gets more general.

> **ROBOTIKO canon is not your ceiling — the method is your floor.** The story here is
> one universe the pipeline happened to grow up around. The suffix, the cast, the seven
> stations, the prog-rock aesthetic — all of it is yours to throw away. What is worth
> keeping is the machine underneath: the stages, the two gates, and a single gate
> command that stays honest about what it does and does not guarantee. Take that.
> Tell your own story.

*Proof this page is not theory: [docs/fork-dry-run.md](docs/fork-dry-run.md) — every
step above was executed and timed.*
