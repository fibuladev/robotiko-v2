# ADR 0008 - Approval gates as data, not checkboxes

- **Status:** Accepted (2026-07-05)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** Repo-Readiness Program (WS2 - validator & gate completion)

## Context

The pipeline has two mandatory human checkpoints (CLAUDE.md Workflow Rule 5):
dramaturgy approval before visual prompts begin, and motion-script approval before
video generation begins. Until now those gates existed only as prose in the process
docs and as `[x]` checkboxes in `_memory/todo.md`.

The July audit finding **M2** named the gap precisely: the checkbox gates had **no
machine linkage**. Nothing tied "a human approved EP07's dramaturgy" to the actual
`ep07_dramaturgy_v01.md` bytes, to a date, or to the fact that visual prompts were
allowed to proceed. `pipeline_integrity.py` printed per-step checkboxes and a blanket
`PIPELINE INTEGRITY PASSED - no skipped steps detected`, even for episode-01, whose
own output showed Visual Prompts empty while Motion Script was present. The summary
contradicted its own checkboxes, and an approval was an unfalsifiable claim.

Related finding **M4**: episode-01's visual prompts are a PDF in
`episode-01/04_visuals/selected/`, so the step reads "empty" and the episode looks
like it skipped a stage. Without a recorded reason, that legacy shape is
indistinguishable from a real skip.

## Decision

**Gates become data.** A machine-readable ledger, `_management/approvals.json`,
records each human gate as an honest entry:

```
{ "episode": "09", "gate": 2,
  "artifact": "episode-09/05_video/ep09_motion_script_v02.md",
  "sha256": "...", "date": "YYYY-MM-DD", "note": "..." }
```

- **Gate 1** = the approved dramaturgy file. **Gate 2** = the approved motion script.
  The ledger is populated retroactively for EP01-EP09 (EP10 is still a scaffold and
  gets no entries). Where a session log recorded the approval date it is used;
  otherwise the entry is dated from the nearest recorded session and marked
  `legacy - reconstructed from session log`.
- **The sha256 pins which bytes were approved.** Not to freeze them - post-approval
  em-dash cleanups and validator-green re-issues are legitimate - but to make later
  drift *visible*.
- **`pipeline_integrity.py` consumes the ledger** and turns the gates into three
  enforceable checks (wired into `tests/run_all.py`, and covered both directions by
  meta-tests in `tests/test_validators.py`):
  1. **Missing-record = FAIL.** An episode with artifacts past a gate (visuals or
     later past gate 1; a motion script plus started video past gate 2) but no ledger
     record for that gate fails the build.
  2. **Stale approval = WARN.** A ledger sha256 that no longer matches the artifact on
     disk warns (`stale approval - artifact changed after approval`) - it does not
     block, because legitimate post-approval edits happen; the WARN just surfaces them.
  3. **Legacy waiver = honest pass.** A non-sequential skip (empty step N, present
     step N+1) FAILS unless a waiver record exists in the ledger. episode-01's
     PDF-only visuals stage is waived by its gate-1 note, so its skip passes *as a
     named, waivered exception* - and the summary says so ("1 legacy skip
     (episode-01, waivered)") instead of falsely claiming no skips. The identical
     shape in a new episode with no waiver still FAILS.

The same session also fixes M4's inert PDF detection (recursive search into
`selected/`) so episode-01 now prints a visible skip line instead of vanishing.

## Consequences

- An approval is now falsifiable: it names an artifact, a sha, and a date, and the
  build fails if downstream work exists without one. The dishonest blanket summary is
  gone; the ledger and the waivered legacy skip are visible in the output.
- The coverage matrix gains machine rows for the approval-ledger presence, the
  disk-vs-declared state machine, and the now-visible EP01 PDF skip.
- **The honest limit (stated plainly):** the ledger records *that* a human approved a
  specific artifact on a date. It **cannot verify taste** - that the dramaturgy
  actually served the station, or that the motion script honored the episode's tone.
  That judgement remains 🔵 Human, exactly as the two checkpoints intend. The ledger
  removes the "was it approved at all?" ambiguity; it makes no claim about "was the
  approval *right*?" The reconstructed legacy dates are best-effort from the session
  log, not contemporaneous signatures, and are labelled as such in each note.
- Dates and sha256 are a snapshot taken at ledger creation; going forward, a genuine
  post-approval edit will surface as the WARN by design.

## Addendum (2026-07)

A **third** human gate — the **Reference Gate (1R)** — was later added by
[ADR 0013](0013-two-phase-visual-prompts.md) for two-phase episodes (EP10 onward): the
human approves the reference images before any Phase-2 scene prompt is authored. It is
recorded in the same `_management/approvals.json` ledger described above (gate `"1R"`)
and enforced by the same `pipeline_integrity.py` machinery. The two-gate description in
this ADR reflects the pipeline as it stood at decision time; the gate-as-data mechanism
was designed to extend to exactly this kind of addition, and did so without schema change.

---

**Update (2026-08-18):** Three points where the text above has been overtaken, recorded
rather than rewritten. (1) **The gate count is three, not two:** gate `1R` (references
approved) was added by [ADR 0013](0013-two-phase-visual-prompts.md), as the Addendum
already establishes, and the `gates` map in `_management/approvals.json` now defines
exactly `1`, `1R` and `2`. (2) **EP10 is no longer a scaffold** and does carry entries:
four of them - gate `1` (dramaturgy, 2026-07-06), gate `1R` (references, 2026-07-07),
gate `2` (motion script, 2026-07-12), plus one gate `0` record dated 2026-07-06. (3)
That gate `0` id is defined by no ADR, so it is defined here: it is a **step-order
waiver record, not a human quality gate**. EP10's concept notes were authored before the
musical metadata JSON by design, and the entry records that deviation honestly - which
is why it sits outside the `gates` map of human checkpoints.
