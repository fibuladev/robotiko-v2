# SKILL: robotiko-reels-atomizer
> **Version:** 1.0 | **Last Updated:** 2026-02-24
> **Trigger:** `"Atomize EP{XX} for social"`
> **Output:** `episode-{XX}/07_social_media/ep{XX}_social_atomization.md`

---

## PURPOSE

Break a finished episode into short-form social media content (Reels, TikTok, Shorts, Stories). Each "atom" is a self-contained clip — 15 to 60 seconds — designed to capture attention, convey a fragment of the episode's essence, and drive viewers to the full video.

The atomization strategy is not random chopping. Each clip must have a narrative hook, a visual peak, and a musical completeness that makes it work as a standalone piece.

---

## PREREQUISITE

> The episode's final video edit must be complete.
> The YouTube package should ideally exist (for consistent messaging), but is not a hard requirement.

---

## MANDATORY INPUTS

| # | File | What to Extract |
|---|---|---|
| 1 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Scene breakdown — identifies the strongest visual moments |
| 2 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Section timestamps, energy peaks — identifies natural clip boundaries |
| 3 | `_management/master.md` | Episode tone, key lyrics, station — informs caption writing |
| 4 | `episode-{XX}/05_video/ep{XX}_motion_script_v{VV}.md` | Shot details — identifies the most cinematic sequences |

---

## ATOMIZATION STRATEGY

### Step 1: Identify Clip Candidates
Scan the dramaturgy and motion script for:
- **Visual peaks:** Scenes with highest motion strength or most striking composition
- **Musical peaks:** Chorus entries, instrumental solos, energy climaxes
- **Narrative hooks:** Key lyrics, turning points, character revelations
- **Contrast moments:** Scenes where satire, irony, or juxtaposition is strongest

### Step 2: Define Clip Boundaries
Each clip must:
- Start and end at natural musical boundaries (section starts, phrase endings, beat-aligned cuts)
- Be between **15 and 60 seconds** (platform optimal range)
- Contain at least one visual peak and one lyrical hook
- Feel complete — not cut mid-phrase or mid-thought

### Step 3: Assign Clip Types

| Type | Duration | Purpose | Best For |
|---|---|---|---|
| **Hook Clip** | 15-20s | Maximum impact, designed to stop scrolling | Chorus moments, visual climaxes, iconic lyrics |
| **Story Clip** | 20-40s | A mini-narrative with setup and payoff | Verse + chorus pairs, scene transitions |
| **Atmosphere Clip** | 30-60s | Mood piece, lets the aesthetic breathe | Instrumental sections, environmental sequences |
| **Behind the Scenes** | 15-30s | Process reveal (optional, human-driven) | Prompt → image → video comparisons |

### Step 4: Write Caption and Hashtags per Clip

**Caption rules:**
- Maximum 150 characters for the primary hook line
- Include a key lyric quote or philosophical fragment
- End with a CTA: link to full video or "Link in bio"
- Tone must match the episode's station — no generic hype language

**Hashtag strategy:**
- 5-10 hashtags per clip
- Mix of: project tags (`#robotiko`, `#robotikov2`), genre tags (`#progrock`, `#anatolianrock`), mood tags (`#scifi`, `#conceptalbum`), platform tags (`#musicvideo`, `#aiart`)

---

## OUTPUT FORMAT

### Clip Table
| Clip # | Type | Timestamp | Duration | Visual Peak | Lyric Hook | Platform Priority |
|---|---|---|---|---|---|---|
| 1 | Hook Clip | 1:15 - 1:35 | 20s | [Scene S12 — description] | "Key lyric here" | Reels, TikTok, Shorts |
| 2 | Story Clip | 0:43 - 1:15 | 32s | [Scene S05-S08] | "Key lyric here" | Reels, Shorts |
| 3 | Atmosphere | 3:20 - 4:10 | 50s | [Scene S22-S25] | Instrumental | Reels, Stories |

### Clip Detail Blocks
For each clip:

```
### CLIP {N} — [Clip Title]
- **Type:** [Hook / Story / Atmosphere / BTS]
- **Timestamp:** [Start - End]
- **Duration:** [Xs]
- **Scenes Included:** [S{XX} - S{XX}]
- **Visual Peak:** [Description of the strongest visual moment]
- **Musical Moment:** [What the music is doing — energy, instruments, mood]
- **Lyric Hook:** [The key lyric or phrase, or "Instrumental" if none]
- **Caption:** [Ready-to-paste caption text]
- **Hashtags:** [Ready-to-paste hashtag string]
- **Platform Priority:** [Which platforms this clip works best on]
- **Aspect Ratio Note:** [If 9:16 crop is needed, note the composition impact]
```

### Release Schedule Suggestion
- **Day 1 (Release day):** Hook Clip → maximum reach
- **Day 2-3:** Story Clips → depth engagement
- **Day 4-7:** Atmosphere Clips → sustained presence
- **Ongoing:** Behind the Scenes (if available) → community building

---

## ASPECT RATIO CONSIDERATIONS

YouTube episodes are 16:9. Social platforms prefer 9:16 (vertical).

**Rules:**
- For clips with center-composed subjects: 9:16 crop is usually safe.
- For clips with wide compositions or important lateral elements: flag that a 9:16 crop may lose critical visual information.
- Never crop a clip if it destroys the composition. Instead, suggest a letterboxed version with branded borders top/bottom.
- Note crop safety in each clip's detail block.

---

## CLIP COUNT GUIDELINES

| Episode Duration | Suggested Clips |
|---|---|
| Under 4 minutes | 3-4 clips |
| 4-6 minutes | 5-7 clips |
| 6-8 minutes | 7-10 clips |
| Over 8 minutes | 8-12 clips |

These are guidelines, not hard rules. Quality over quantity — a weak clip damages the brand more than a missing one helps it.

---

## POST-GENERATION CHECKLIST

- [ ] Every clip has natural musical boundaries (no mid-phrase cuts)
- [ ] Every clip has at least one visual peak
- [ ] Clip durations are within 15-60 second range
- [ ] Captions are under 150 characters and include a lyric or philosophical hook
- [ ] Hashtags are relevant and within platform limits
- [ ] 9:16 crop safety is noted for each clip
- [ ] Release schedule suggestion is included
- [ ] No clip relies on context from the full video to make sense
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Final edit does not exist | STOP. Cannot atomize what does not exist. |
| Episode is very short (<2 min) | Generate 2-3 clips maximum. Quality over quantity. |
| No clear visual peak in a section | Skip that section for atomization. Not every moment needs to be a clip. |
| Episode is spoken word (EP08-09) | Prioritize atmosphere clips and lyric-card overlays instead of fast-cut hooks. Adjust tone of captions accordingly. |

---

*"An atom is not a fragment. It is a complete universe at a smaller scale."*
*— Robotiko v2.0 Pipeline*
