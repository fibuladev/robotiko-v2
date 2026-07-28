# CAPCUT EDIT GUIDE — FIXTURE (FROZEN BAD FIXTURE — DO NOT FIX)

> **This is a regression fixture, not pipeline output.** It freezes the real
> EP09 v01 gap-propagation bug: Scene Dur values computed 1s SHORT of their
> timestamp span (the original v01 carried gapped durations copied straight
> from the motion script's 1s display gaps between scenes, instead of the
> contiguous span actually cut on the timeline), plus a genuine 1s timestamp
> gap between S01 and S02 and a wrong Speed value on S04. It lives outside
> `episode-*/` on purpose — `music_dur` resolves to `None` here, so only the
> row-level checks are exercised (Scene Dur vs span, contiguity, speed). The
> validator suite MUST FAIL on this file. See `tests/fixtures/README.md`.

## TIMELINE MAP

| Shot | Timestamp | Clip File | Scene Dur | Clip Dur | Speed | Trim |
|------|-----------|-----------|-----------|----------|-------|------|
| S01 | 0:00–0:14 | 1.mp4 | 13s | 10s | — | — |
| S02 | 0:15–0:27 | 2.mp4 | 11s | 10s | — | — |
| S03 | 0:27–0:39 | 3.mp4 | 11s | 10s | — | — |
| S04 | 0:39–0:53 | 4.mp4 | 14s | 10s | 0.50× | — |

End of table.
