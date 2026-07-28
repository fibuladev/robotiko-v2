# CAPCUT EDIT GUIDE — FIXTURE (FROZEN GOOD FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** It is the corrected
> counterpart of `capcut_guide_BAD.md`: contiguous timestamps, Scene Dur values
> that match their timestamp span exactly, and speed/trim values that satisfy
> `speed == clip_dur / scene_dur` and `trim == clip_dur - scene_dur`. It lives
> outside `episode-*/` on purpose — `validate_file` cannot resolve an episode
> number from this path, so `music_dur` is `None` and the total-duration check
> is skipped. This fixture proves the row-level checks only: Scene Dur vs span,
> contiguity, speed, and trim. The validator suite MUST pass every check on this
> file. See `tests/fixtures/README.md`.

## TIMELINE MAP

Five contiguous shots, 0:00-0:46. No gaps, no drift.

| Shot | Timestamp | Clip File | Scene Dur | Clip Dur | Speed | Trim |
|------|-----------|-----------|-----------|----------|-------|------|
| S01 | 0:00–0:10 | 1.mp4 | 10s | 10s | — | — |
| S02 | 0:10–0:14 | 2.mp4 | 4s | 10s | — | trim 6s |
| S03 | 0:14–0:24 | 3.mp4 | 10s | 8s | 0.80× | — |
| S04 | 0:24–0:36 | 4.mp4 | 12s | 10s | 0.83× | — |
| S05 | 0:36–0:46 | 5.mp4 | 10s | 10s | — | — |

End of table.
