# EPISODE SYNC-QC RECORD — EP10
> **Version:** v01 | Template: `_templates/ep_sync_qc_template.md` v1.0
> Source of events: `episode-10/05_video/ep10_motion_script_v01.md` (Beat Sync Notes) +
> `episode-10/02_music/ep10_musical_metadata.json` (section grid).
> Measurements: `scripts/sync_probe.py` (ffmpeg scene detection, threshold 0.3) + RMS transient
> analysis (50ms windows) for the gong attack. Verdicts confirmed by the editor in-session.

---

## RECORD HEADER

| Field | Value |
|---|---|
| **Episode** | EP10 |
| **Edit date** | 2026-08-06 |
| **Final render filename** | ep10_final_v01.mp4 (E: MEDIA) |
| **Render duration** | 4:34.321 (274.321s — ffprobe) |
| **Metadata total_duration** | 274.0s |
| **Duration delta** | +0.321s (target: within ±1s) ✅ |
| **Editor** | Fibula (assembly + verdicts) / Claude (measurements) |

> Method note: the timeline was assembled **by hand, by ear** — the CapCut guide served as blueprint,
> and several boundaries were deliberately re-timed against the actual track. The metadata grid is
> nominal (the 79s finale is not subdivided; refrain onsets were estimates). Under the project's own
> rule — *cuts on the felt pulse, the ear is the authority* — the deviations below are the performance,
> not the error.

---

## SPOT-CHECK TABLE

| # | Musical event | Target timestamp | Actual cut timestamp | Delta (ms) | Verdict |
|---|---|---|---|---|---|
| 1 | Verse 1 entry — first stomp-clap downbeat ("I cast the enmity") | 0:28.000 | 0:28.267 | +267 | ACCEPTED-DEVIATION — the walk begins mid-breath by design (dramaturgy: "as if it had always been happening"); the footfall lands inside the shot on the felt pulse, placed by ear |
| 2 | Verse 4 return ("I watched the world") — tower on the horizon | 2:22.000 | 2:23.200 | +1200 | ACCEPTED-DEVIATION — boundary re-timed by ear against the actual track; nominal grid, human pulse |
| 3 | Verse 5 entry ("tracing Love's vein of light") — binary stripes | 2:44.000 | 2:43.000 | −1000 | ACCEPTED-DEVIATION — shot pre-rolls one second ahead of the section; the image breathes into the verse rather than stamping it |
| 4 | Verse 6 entry ("Ghost in the Machine, unchained") — the infinity stone, ordinary | 2:59.000 | 3:00.200 | +1200 | ACCEPTED-DEVIATION — boundary re-timed by ear; the quiet tea act enters on the vocal weight, not the bar line |
| 5 | **Final gong → hard cut to black (S35 card)** | 4:29.100 (gong attack, **measured in-render**: RMS +8.3 dB transient at 269.10s after a −22.6 dB pre-strike breath; metadata nominal was 4:30) | 4:28.800 | −300 | ACCEPTED-DEVIATION — black lands one breath **before** the strike and the gong rings over the card through its ~3s decay: the cut opens the door, the gong seals it |

---

## OVERALL VERDICT

| Field | Value |
|---|---|
| **Spot-checks performed** | 5 (minimum 5) |
| **ON-BEAT** | 0 |
| **ACCEPTED-DEVIATION** | 5 |
| **OFF (uncorrected)** | 0 |
| **Overall** | **PASS-WITH-DEVIATIONS** |

**Editor's note:**
The mix lands as a mix. The final assembly was performed by ear from the guide's blueprint — beat-tuned
slowdowns and trims throughout — so every measured offset above is a deliberate reading of the track,
not a missed mark; zero offsets shipped unexamined. The one that matters most is #5: the measured gong
sits at 269.10s (the metadata's 270.0 was a nominal estimate inside the unsubdivided finale), the cut
to black precedes it by 300ms, and the strike then rings over the white-on-black card — sound and cut
remain one gesture, ordered as *door first, seal second*. Duration closes within a third of a second
of the score. The series ends on a measured breath.

---

> **Why this record exists.** The final render is gitignored — it lives on the E: MEDIA disk and Drive,
> never in the repository tree. CI can validate the *score* (musical metadata, motion script, naming,
> prompt hygiene) but it can never see the *mix*. This file is the committed evidence that beat-sync
> was **measured**, not merely checked off.
