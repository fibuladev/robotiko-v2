# Fork Dry Run — one author, one afternoon, a second universe

> **What this is.** The critique the fork story had to answer was blunt: *the fork
> path was designed but never stress-tested with a second universe.* So the author
> ran the fork end to end against a deliberately different universe — a neo-noir
> detective piece, "Silhouette City" — following [CONTRIBUTING §3](../CONTRIBUTING.md#3-how-to-fork-the-method-for-your-own-universe)
> literally, as a stranger would, and logged every step, every failure verbatim, and
> what fixed it. This page is that transcript.
>
> **Honest disclosure up front.** This is the *author's own* dry run, not an
> independent one. It is a self-test: the same person who built the method also drove
> the fork. That is worth exactly what it is worth. The first **independent** fork
> report is still wanted — see [UNIVERSES.md](../UNIVERSES.md). What this run *can*
> prove is concrete: the method survives a universe with a different suffix, a
> different cast, a different genre, and it exposed one real portability bug (now
> fixed) plus a precise list of fork steps a second universe must take.

---

## The toy universe

**Silhouette City** — a rain-drowned neo-noir. Protagonist **VEX-9**, a detective
automaton built to forget, in a jazz metropolis called Meridian. Chosen to be as far
from ROBOTIKO as possible so the stress test is real:

| | ROBOTIKO | Silhouette City |
|---|---|---|
| Genre | CyberAnatolian prog-rock sci-fi | NoirSynth detective |
| Visual suffix | 70s prog-rock album art, Kodachrome | chiaroscuro film-noir, 16mm, amber |
| Video suffix | 35mm, 16:9, Kodachrome | 16mm, 2.39:1 anamorphic, noir |
| Protagonist key | `robotiko` | `vex` |
| Arc | binary 0/1 → infinity | KEEP/PURGE → CARRY |

The fork was built **outside the repo tree**, in a scratch copy of the working tree
(`.git`, `_private/`, `_tutorial/` excluded). Nothing below scaffolds a toy universe
inside the real repo.

---

## Timeline (real clock, 2026-07-05)

| Clock | Step | Wall time |
|---|---|---|
| 15:38 | Faithful working-tree copy → baseline `python tests/run_all.py` **10/10 green** | (baseline) |
| 15:40 | Write the new canon (`_management/master.md` replaced with the noir canon, ~110 lines) | creative |
| 15:41 | Rewrite the cast (`_assets/cast/character_profiles.json` + its `.schema.json`, protagonist `robotiko`→`vex`) | ~3 min |
| 15:43 | Swap suffixes in `tests/universe_config.py` **and** `CLAUDE.md` → **first run: crash** | ~2 min |
| 15:47 | Remove the ROBOTIKO episodes; `python scripts/create_episode.py 01` | **~1 second** (scaffold) |
| 15:53 | Author EP01 by hand (lyrics, metadata JSON, concept, dramaturgy, visual prompts, motion script) | creative |
| 15:57 | Apply the foreign-universe gate adjustments → **final run: green** | ~4 min |

The **method plumbing** — everything except writing the canon and authoring the six
scenes — was well under 15 minutes. The rest is the creative afternoon (or, in a real
fork, the minutes the skills spend). The scaffold step itself was one second.

> A tooling aside, for honesty: the very first working-tree copy was made with a
> flaky `robocopy /E` that silently dropped a handful of files; a `robocopy /MIR`
> re-copy fixed it and file counts matched (432 = 432) before the baseline was
> trusted. That was the copy tool, not the method — noted so the log hides nothing.

---

## Step by step, with every failure verbatim

### Baseline — the copy is green before anything changes

```
[PASS] Naming convention        [PASS] Motion script
[PASS] Pipeline integrity       [PASS] Character profiles
[PASS] Visual prompt sweep      [PASS] Validator meta-tests
[PASS] Prompt hygiene           [PASS] Doc reference integrity
[PASS] Musical metadata         [PASS] Energy-motion sync (advisory)
  All check groups passed.
```

### §3 step 2 — write your canon

Replaced `_management/master.md` wholesale with the Silhouette City canon: logline,
tone, the KEEP/PURGE→CARRY metaphor, eight golden rules, the visual DNA, and the two
mandatory suffixes. Pure creative work; no gate interaction yet.

### §3 step 3 — rewrite your cast

Replaced `_assets/cast/character_profiles.json` with VEX-9 + the informant Lilou, and
renamed the schema's required protagonist key (`robotiko` → `vex`) in
`_assets/cast/character_profiles.schema.json`. **The character-profiles validator reads
its schema dynamically**, so once the JSON and the schema agree, it just passes — no
code change needed. Placeholder reference PNGs (`ref_vex_issue.png` and siblings) were
dropped into `_assets/cast/` so the reference-first guard has real files to find.

### §3 step 4 — swap the suffix → the one real bug surfaced

Swapped `VISUAL_SUFFIX`, `VIDEO_SUFFIX`, and `FORBIDDEN_AESTHETICS` in
`tests/universe_config.py`, and the two suffix blocks in `CLAUDE.md`. First
`run_all` after the swap, the **Visual prompt sweep crashed** — not failed, *crashed*:

```
File "tests/visual_prompt_validator.py", line 480, in check_character_phase
    phase = get_phase_for_episode(episode_number, load_profiles()) ...
File "tests/visual_prompt_validator.py", line 277, in get_phase_for_episode
    evolution = profiles["robotiko"]["evolution"]
KeyError: 'robotiko'
```

**FINDING #1 — a real portability bug (fixed in the method).** The scene-level checks
already skipped foreign scenes (they filter on the protagonist's identifier strings),
but the `get_phase_for_episode` helper reached for the hard-coded `robotiko` key
*unconditionally*, so any cast without that key took down the whole sweep. The fix
hoists the two universe-specific bindings into `tests/universe_config.py` —

```python
PROTAGONIST_KEY = "robotiko"
PROTAGONIST_IDENTIFIERS = ["robotiko", "chrome android"]
```

— and makes the phase/ref helpers in `tests/visual_prompt_validator.py` degrade
gracefully: absent key → phase-unknown no-op, never a crash. Defaults are the ROBOTIKO
values, so the real suite is unchanged (still 10/10, meta-tests included). The fork
then points them at its own lead (`vex`, identifiers `vex` / `vex-9` /
`detective automaton`) and gets **real phase enforcement for VEX** instead of a crash.

### §3 step 4, continued — the suffix swap has a consequence

**FINDING #2 — a fork step, not a bug.** Swapping the suffix in `universe_config`
invalidates *every existing ROBOTIKO prompt file*, because they all end in the old
prog-rock suffix. That is the intended effect (the gate now demands *your* house
style) — but it means a fork must **remove the ROBOTIKO episode folders**. There is no
way to both swap the suffix and keep the ROBOTIKO episodes green; they are mutually
exclusive. So:

### §3 step 5 — remove the old story, scaffold your own

```
$ rm -rf episode-0* episode-10
$ python scripts/create_episode.py 01
==> Creating Episode 1 environment ...
[+] Created: episode-01/03_direction/ep01_concept_notes.md
[+] Created: episode-01/03_direction/ep01_dramaturgy_v01.md
[+] Created: episode-01/04_visuals/ep01_visual_prompts_v01.md
[+] Created: episode-01/05_video/ep01_motion_script_v01.md
==> Episode 1 is ready.
```

One second, no edits to `scripts/create_episode.py` — the scaffolder is already
universe-agnostic.

### Author EP01 by hand (simulating the pipeline stages)

Six tiny scenes, produced by hand to stand in for the skills: `ep01_lyrics_v01.md`, the
`ep01_musical_metadata.json` (5 sections, 96s), real concept notes, a 6-scene
dramaturgy, a 6-scene visual-prompts file (every prompt ending in the **noir** suffix,
VEX in Phase 1, referencing the `issue` ref), and a 6-shot motion script (6 distinct
camera moves, `Static` at 17%, the noir video suffix + anti-spawn guard on every
motion prompt, header stamped SKILL v2 so the camera-diversity rules are **FAIL-tier
enforced**, not merely advisory).

Run after authoring — the seven production graders were all green; two groups still
red:

```
[PASS] Naming convention        [PASS] Motion script
[PASS] Pipeline integrity       [PASS] Character profiles
[PASS] Visual prompt sweep      [FAIL] Validator meta-tests
[PASS] Prompt hygiene           [FAIL] Doc reference integrity
[PASS] Musical metadata         [PASS] Energy-motion sync (advisory)
```

### The two remaining reds — both ROBOTIKO-content coupling, neither a grader defect

**Doc reference integrity — 17 issues, all the same shape:**

```
FAIL: docs/getting-started.md:76        references missing path: episode-02/
FAIL: docs/skills-guide.md:161          references missing path: episode-05/02_music/ep05_musical_metadata.json
FAIL: docs/anatomy-of-an-episode.md:32  references missing path: ../episode-07/01_lyrics/ep07_lyrics_v01.md
FAIL: docs/hallucinating-camera.md:144  references missing path: episode-09/05_video/ep09_motion_script_v01.md
FAIL: _management/dissonance_registry.md:61 references missing path: episode-08/05_video/ep08_motion_script_v01.md
   ... (five curated docs, all citing now-deleted ROBOTIKO episode files)
```

**FINDING #3 — a fork step.** The doc-reference lint's curated list in
`tests/doc_reference_check.py` includes ROBOTIKO *worked-example* docs that cite
specific ROBOTIKO episode files. Delete those episodes and the citations dangle. The
fork rewrites the method docs it keeps (getting-started, skills-guide) to cite its own
episode, drops the ROBOTIKO CC-BY-NC teaching docs it does not keep
(anatomy-of-an-episode, hallucinating-camera, dissonance_registry) from the curated
list, and keeps the universe-agnostic method docs. Green after pruning.

**Validator meta-tests — 21 failures, 6 errors.** Every one is ROBOTIKO-content
coupled: `TestRefIntegrityGrader` and `TestReferenceFirstGuard` load the live
`robotiko` profile; `TestParserCoverage` iterates the shipped ROBOTIKO episodes;
`TestRealTreeStaysGreen` asserts the EP01 PDF waiver and the exact ledger shas.

**FINDING #4 — a fork step, and the sharpest lesson of the run.**
`tests/test_validators.py` is the METHOD's own regression corpus — it *grades the
graders* against frozen ROBOTIKO fixtures (`tests/fixtures/`), the ROBOTIKO
shipped-episode tree, and the `robotiko` profile entry. It is **mutually exclusive**
with the suffix swap: the moment you retire the ROBOTIKO content, its assertions about
that content necessarily break. This is not a defect — the graders themselves pass
cleanly on the noir universe (all seven production groups green). A fork keeps
`tests/fixtures/` as inherited proof that the graders catch real bugs, then rebuilds
its own meta-tests once it has its own shipped episodes, and disables the group in
`tests/run_all.py` meanwhile. (The deeper architectural note: an ideal future version
would split the universe-agnostic grader tests from the ROBOTIKO real-tree assertions,
so a fork inherits the former for free. That refactor is out of scope for this run and
is left as a documented invitation.)

### Two more housekeeping fork steps

**FINDING #5.** The reference-first guard checks that a phase's reference image
*exists on disk*. A fork drops in its own `ref_*.png` files (placeholders are fine to
keep the gate green until real art exists).

**FINDING #6.** Update `_management/approvals.json` and
`_management/project_metadata.json` to your episodes. Leave the ROBOTIKO ledger records
in place and pipeline integrity still *passes*, but with stale-approval WARNs pointing
at ROBOTIKO artifacts — untidy, non-blocking. The fork replaced both with its own EP01
records (real shas) so pipeline integrity reports a clean "no stale approvals".

---

## End state — the toy universe's gate, green

After the documented fork steps (protagonist binding pointed at `vex`, curated docs
pruned, meta-test group disabled with a loud note, ledger + metadata rewritten):

```
================================================================
  SUMMARY
================================================================
  [PASS] Naming convention
  [PASS] Pipeline integrity
  [PASS] Visual prompt sweep
  [PASS] Prompt hygiene
  [PASS] Musical metadata
  [PASS] Motion script
  [PASS] Character profiles
  [PASS] Doc reference integrity
  [PASS] Energy-motion sync (advisory)
  All check groups passed.
```

Nine groups green; the tenth ("Validator meta-tests") is the ROBOTIKO regression
corpus, disabled by a documented fork step until the fork writes its own. Motion script
passed at **FAIL-tier** (the SKILL-v2 camera-diversity rules were enforced, not
skipped), and energy-motion passed with **no** advisory warnings — the hand-authored
Motion Strengths landed inside the musical energy bands.

**Total dry-run wall clock, baseline-green to toy-green: ~19 minutes**, most of it the
hand-authoring that a real fork hands to the skills.

---

## What this proves, and what it doesn't

- **Proven:** the method carries to a genuinely different universe; exactly one real
  portability bug existed and is fixed; the remaining friction is a short, precise,
  documented list of fork steps, not a wall.
- **Not proven:** that an *independent* forker reaches the same place as smoothly. The
  author testing the author's own method is a self-test. **The first independent fork
  report is the thing still wanted** — register yours at [UNIVERSES.md](../UNIVERSES.md),
  and tell us the one thing that broke.

The distilled, do-this version of the above lives in
[FORKING.md](../FORKING.md); the zero-cost text-only slice is in
[text-only-first-episode.md](text-only-first-episode.md).
