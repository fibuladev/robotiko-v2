# The DISSONANCE Registry

> Every sanctioned moment where the visual deliberately **refuses** the music's
> energy — logged, dated, and justified. This is the human-readable ledger behind a
> machine exemption. An exemption without a ledger is a loophole; a ledger makes it
> a doctrine.

---

## What `[DISSONANCE]` means

In the pipeline, motion normally tracks music: rising energy earns a stronger
camera and higher Motion Strength (MS); quiet earns stillness. `[DISSONANCE]` is
the **sanctioned tag** for the deliberate exception — a shot where the frame
intentionally goes *against* the music's energy because the story demands it. It is
defined in [`_skills/robotiko-motion-script/SKILL.md`](../_skills/robotiko-motion-script/SKILL.md)
(Art Direction Pillar 4, "Musical Dissonance as Choice," and the Musical Dissonance
Decision Criteria):

| Music energy | Visual choice | Use when |
|---|---|---|
| High / Peak | Static, MS 1-2 | Character is emotionally dead while the world rages; the body has given up. |
| Low / Quiet | MS 5-6, dynamic camera | Internal turmoil despite external silence; the mind races while the body is still. |
| Rising build | Camera retreats (Dolly Out) | The world offers energy the character cannot receive; rejection of hope. |

The tag lives in the shot's **Musical Moment** field and carries a one-line
justification. The SKILL is explicit: *do not "fix" a dissonance moment* — it is a
choice, not a defect.

## Why deviations are REGISTERED, not hidden

A dissonant shot looks, to a machine, exactly like a mistake: high-energy music
paired with a dead-still camera is precisely the failure the energy→motion check
exists to catch. So the tag grants that shot an **exemption** from the check. And an
exemption that lives only inside a validator's skip logic is a loophole — anyone
could silence a real error by tagging it.

This registry closes the loophole. It is the human-readable side of the machine
exemption in [`tests/energy_motion_check.py`](../tests/energy_motion_check.py),
which skips `[DISSONANCE]`-tagged shots (the tag is shot-scoped: it sits in the
shot's Musical Moment field and covers all of that shot's sub-clips — the check
leaves shot scope at every `##` boundary so a mention in a summary table cannot
retroactively exempt anything). The machine grants the pass; this ledger records
*why it was earned*. Every entry below is traceable to a real tagged shot block —
no dissonance moment is exempt from the check without a row here, and no row here
exists without evidence in the script.

Coverage status is tracked in
[`_management/invariant_coverage_matrix.md`](../_management/invariant_coverage_matrix.md)
(Energy → Motion Strength mapping, advisory tier).

---

## Registry

Every `[DISSONANCE]`-tagged shot in the shipped scripts, traced to its shot block.
Sub-clip mentions and summary-table rows are deduplicated to the parent shot.

### EP08 — S09 · "The Vow"

- **Source:** [`episode-08/05_video/ep08_motion_script_v01.md`](../episode-08/05_video/ep08_motion_script_v01.md) (shot block; sub-clips S09a, S09b)
- **Timestamp:** 2:00–2:20
- **Camera / MS:** Static · MS 2
- **What the music does:** High-energy ritualistic chorus — "Day One. No input, no output." The music is booming and resonant.
- **What the frame does instead:** Holds perfectly still. The android stands centered on the summit plateau, arms at his sides; only wind and faint mechanical breathing move.
- **Justification (from the script):** "The vow IS ritual stillness. The lyric says 'just the frame and breath' — the frame obeys. The body does not move during the vow, even as the music booms." The dissonance between sonic energy and visual stillness *is* the hypnotic, ritualistic quality the dramaturgy demands.
- **Verdict:** VERIFIED — tagged in the shot's Musical Moment field and named in the script's own [DISSONANCE] Moments summary.

### EP08 — S10 · "The Vow Deepens"

- **Source:** [`episode-08/05_video/ep08_motion_script_v01.md`](../episode-08/05_video/ep08_motion_script_v01.md) (shot block; sub-clips S10a, S10b)
- **Timestamp:** 2:20–2:36
- **Camera / MS:** S10a Static · MS 2 (dissonant hold). S10b Dolly Out · MS 3 (transition out).
- **What the music does:** Continued high-energy chorus — "Nothing enters, nothing exits. Just the frame and breath."
- **What the frame does instead:** S10a sustains the static vow — the android motionless, faint steam from chassis vents the only sign of function. S10b then begins a gentle pull-back to exit the ritual.
- **Justification (from the script):** "Static visual against energetic music: the lyric says 'just the frame,' so the frame obeys."
- **Verdict:** VERIFIED, with a scope note — the shot carries the `[DISSONANCE]` tag in its Musical Moment field, but the script's own [DISSONANCE] Moments summary lists only **S10a**; S10b's gentle Dolly Out (MS 3) is the transition *out* of the vow and is not counted as dissonant. Recorded honestly rather than flattened to "the whole shot is static."

### EP09 — S23 · "I Am The Bug" (Speed Ramp)

- **Source:** [`episode-09/05_video/ep09_motion_script_v02.md`](../episode-09/05_video/ep09_motion_script_v02.md) (latest version; shot block, single clip at 0.91× ramp)
- **Timestamp:** 3:19–3:30
- **Camera / MS:** Static · MS 5 (STILL HOLD — camera locked, high energy inside the frame)
- **What the music does:** Massive doom rock — "I AM THE BUG" — the track's emotional apex, explosive.
- **What the frame does instead:** The camera does not move at all. Every practical light in the workshop blazes and flickers; sparks arc from the android's open chest panel. The violence is entirely *inside* the frame — the camera refuses to participate.
- **Justification (from the script):** "Explosive music + static camera. The Discovering Camera does not flinch."
- **Verdict:** VERIFIED — tagged in the shot title, Scene Context, and a dedicated `[DISSONANCE]` note in the shot block, and named in the script's Camera Diversity and Director's Notes summaries.
- **Note on flavor:** Unlike EP08's total stillness (Static + MS 1-2, the "body has given up" template), S23 refuses via a locked *camera* while the frame itself is at MS 5 — the energy is redirected inward, not removed. Both are legitimate dissonance; they are not the same gesture.

### EP10 — S26 · "Two Glasses, One Pot"

- **Source:** [`episode-10/05_video/ep10_motion_script_v01.md`](../episode-10/05_video/ep10_motion_script_v01.md) (shot block)
- **Timestamp:** 3:05–3:09
- **Camera / MS:** Slow Zoom In · MS 2
- **What the music does:** Verse 6 at full band, high energy — "Now broadcasting Love across the divide."
- **What the frame does instead:** He sits on the fallen stone loop and quietly pours tea into two glasses; the shepherd sleeps.
- **Justification (from the script):** "The epic lives in the music; the humility lives in the tea. He pours quietly while the album roars — concept thesis from the dramaturgy."
- **Verdict:** VERIFIED — tagged in the shot's Musical Moment field and listed in the script's [DISSONANCE] Inventory.

### EP10 — S27 · "The Hand"

- **Source:** [`episode-10/05_video/ep10_motion_script_v01.md`](../episode-10/05_video/ep10_motion_script_v01.md) (shot block, Mode B)
- **Timestamp:** 3:10–3:14
- **Camera / MS:** Static · MS 2
- **What the music does:** The minor-to-major shift completes at full band.
- **What the frame does instead:** The quietest physical gesture of the series — one tea glass extended toward the lens, gaze below the lens.
- **Justification (from the script):** "The climactic harmonic resolution underlies the quietest physical gesture — a glass offered through the screen."
- **Verdict:** VERIFIED — tagged in the shot's Musical Moment field and listed in the script's [DISSONANCE] Inventory.

### EP10 — S29 · "The Tracks"

- **Source:** [`episode-10/05_video/ep10_motion_script_v01.md`](../episode-10/05_video/ep10_motion_script_v01.md) (shot block)
- **Timestamp:** 3:24–3:32
- **Camera / MS:** Static · MS 2
- **What the music does:** Epic finale, electric guitar solo climbing.
- **What the frame does instead:** A locked grass-height macro of two parallel track-lines (patched metal tread + bare human footprint); nothing moves but light.
- **Justification (from the script):** "The solo rages while the camera rests at grass height on the proof of companionship — two track-lines, side by side."
- **Verdict:** VERIFIED — tagged in the shot's Musical Moment field and listed in the script's [DISSONANCE] Inventory.
- **Note on flavor:** The tag was added at the 2026-07-12 post-approval audit — the shot was designed still from the dramaturgy on, but shipped untagged; the audit closed the gap the same day the registry gained these rows.

---

## Scope of this sweep

Built from a `DISSONANCE` sweep across `episode-*/05_video/*.md` and
`episode-*/03_direction/*.md`. As of this writing, the tag appears in EP08
(S09, S10), EP09 (S23), and EP10 (S26, S27, S29) — the episodes whose camera
personalities (EP08 the Witnessing Camera, EP09 the Discovering Camera, EP10 the
Companion Camera — the finale's thesis: the epic lives in the music, the humility
on the ground) are built to hold still while the music rages. No other episode
carries a sanctioned dissonance moment. When a future script adds one, it earns a
row here on the same terms: a real tagged shot block, a quoted justification, and
a verdict.

---

*The tag's rule lives in [`_skills/robotiko-motion-script/SKILL.md`](../_skills/robotiko-motion-script/SKILL.md);
its machine exemption in [`tests/energy_motion_check.py`](../tests/energy_motion_check.py);
its coverage honesty in [`_management/invariant_coverage_matrix.md`](../_management/invariant_coverage_matrix.md).
The method that turns exemptions like this into doctrine is described in
[`docs/method-lesson-graduation.md`](../docs/method-lesson-graduation.md).*
