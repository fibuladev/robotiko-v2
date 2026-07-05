# EPISODE SYNC-QC RECORD TEMPLATE
> **Version:** 1.0 | Source: `_management/pipeline_rules.md` (Step 11 — Editing)
> Filled by the HUMAN during the CapCut edit, once the final render exists.
> This is the committed evidence CI cannot produce — the final render is gitignored
> (it lives on Google Drive / portable disk, never in the tree), so beat-sync
> measurement is a local, human-run discipline. Copy this file to
> `episode-{XX}/06_edit/ep{XX}_sync_qc_v01.md` and fill it in.

---

## RECORD HEADER

| Field | Value |
|---|---|
| **Episode** | EP{XX} |
| **Edit date** | [YYYY-MM-DD] |
| **Final render filename** | ep{XX}_final_v{VV}.mp4 |
| **Render duration** | [MM:SS] ([sss]s — measured in CapCut / ffprobe) |
| **Metadata total_duration** | [sss]s (from `episode-{XX}/02_music/ep{XX}_musical_metadata.json`) |
| **Duration delta** | [+/-N.N s] (target: within +/-1s) |
| **Editor** | [name] |

> Tip: `python scripts/sync_probe.py --video <render> --metadata <metadata.json>`
> prints measured cut-vs-boundary numbers you can paste into the table below.
> That helper is LOCAL only — it never runs in CI (the render is not in the tree).

---

## SPOT-CHECK TABLE
> One row per critical sync point. Source of the events: the motion script's
> **Beat Sync Notes** table (`episode-{XX}/05_video/ep{XX}_motion_script_v01.md`).
> **Minimum 5 spot-checks per episode.** Measure the actual cut/action timestamp in
> the timeline against the musical event's target timestamp.
>
> **Verdicts:**
> - **ON-BEAT** — |delta| <= 150 ms.
> - **OFF by N ms** — |delta| > 150 ms and unintended. Note whether it was corrected.
> - **ACCEPTED-DEVIATION** — a deliberate artistic offset. Give a one-line reason.
>   Artistic choices are legitimate; hiding them is not.

| # | Musical event | Target timestamp | Actual cut timestamp | Delta (ms) | Verdict |
|---|---|---|---|---|---|
| 1 | [e.g., "Nothing comes out" — held vocal silence] | 0:27.000 | 0:27.120 | +120 | ON-BEAT |
| 2 | [e.g., Saz sustain peak] | 1:06.000 | 1:06.480 | +480 | ACCEPTED-DEVIATION — amber flicker rides the sustain tail, not its onset |
| 3 | [e.g., Chorus / drop entry] | [M:SS.mmm] | [M:SS.mmm] | [+/-N] | [ON-BEAT / OFF by N ms / ACCEPTED-DEVIATION — reason] |
| 4 | [...] | [...] | [...] | [...] | [...] |
| 5 | [...] | [...] | [...] | [...] | [...] |

---

## OVERALL VERDICT

| Field | Value |
|---|---|
| **Spot-checks performed** | [N] (minimum 5) |
| **ON-BEAT** | [N] |
| **ACCEPTED-DEVIATION** | [N] |
| **OFF (uncorrected)** | [N] |
| **Overall** | [PASS / PASS-WITH-DEVIATIONS / NEEDS-REWORK] |

**Editor's note:**
[One short paragraph. Does the mix land as a mix, not just as a score? Defend each
accepted deviation in one line. If anything reads OFF and shipped anyway, say why.]

---

> **Why this record exists.** The final render is gitignored — it lives on Drive /
> portable disk, never in the repository tree. CI can validate the *score* (musical
> metadata, motion script, naming, prompt hygiene) but it can never see the *mix*.
> This file is the committed evidence that beat-sync was **measured**, not merely
> checked off. Without it, "beat sync verified" is a claim; with it, it is a record.
