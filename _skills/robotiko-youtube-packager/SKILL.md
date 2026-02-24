# SKILL: robotiko-youtube-packager
> **Version:** 1.0 | **Last Updated:** 2026-02-24
> **Trigger:** `"Package EP{XX} for YouTube"`
> **Output:** `episode-{XX}/07_social_media/ep{XX}_youtube_package.md`

---

## PURPOSE

Generate a complete YouTube metadata package for a finished episode: title, description, timestamps, tags, thumbnail guidance, and end screen recommendations. This skill ensures every upload is optimized for discoverability while maintaining the project's artistic integrity.

---

## PREREQUISITE

> The episode's final video edit must be complete (`episode-{XX}/06_edit/ep{XX}_final_v{VV}.mp4` exists).
> If the final edit does not exist, STOP. Packaging requires a finished product.

---

## MANDATORY INPUTS

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/master.md` | Episode title, station, tone, key lyrics, logline, philosophical context |
| 2 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Section timestamps for YouTube chapter markers |
| 3 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Scene breakdown for description highlights |
| 4 | `_management/project_metadata.json` | Episode status confirmation, series context |

---

## OUTPUT STRUCTURE

### 1. Video Title
**Format:** `ROBOTIKO v2.0 — EP{XX}: "{Episode Title}" | [Genre Tag]`

**Rules:**
- Maximum 100 characters
- Include episode number and title from master.md
- Append a genre/mood tag that aids discoverability
- Do not use clickbait or misleading titles — the art speaks for itself

**Example:**
```
ROBOTIKO v2.0 — EP02: "The Tech Guru's Downfall" | Anatolian Psychedelic Rock
```

### 2. Video Description
**Structure:**
```
[Opening hook — 1-2 sentences that capture the episode's essence without spoilers]

[Logline or key lyric quote — italicized]

---

[Episode context — which station, where in the journey, what Robotiko faces]

[Musical identity — genre, instruments, influences for this episode]

---

📍 CHAPTERS
[Auto-generated from musical metadata timestamps]

---

🎵 ABOUT ROBOTIKO v2.0
[Series description — consistent across all episodes]
Drawing from Turkish philosophy, Turkish folk poetry,
and the 70s Turkish psychedelic rock legacy.
[Link to playlist]
[Link to repository (after open source)]

---

🎨 CREDITS
[Toolchain credits: Suno AI, Nano Banana, Kling/Veo, Claude, CapCut]
[Human creator credit]

---

#robotiko #anatolianrock #progrock #aimusic #conceptalbum
```

**Rules:**
- Opening hook must be compelling but honest. No cheap clickbait.
- Key lyric should be the episode's most representative line from master.md.
- Chapters must exactly match musical metadata section timestamps.
- Series description block is reusable across episodes — write once, copy across.
- Tags section uses hashtags relevant to the genre and project.

### 3. YouTube Chapter Markers
Auto-generated from `musical_metadata.json`:

```
0:00 — [Section name / Title]
0:42 — [Section name]
1:15 — [Section name]
...
```

**Rules:**
- First chapter must start at `0:00`.
- Chapter names should be descriptive but concise (max 50 characters).
- Use section names from metadata, not generic labels.
- If a section has a notable lyric, use it as the chapter name (in quotes).

### 4. Tags
Two categories:

**Primary tags (always include):**
```
robotiko, robotiko v2, anatolian rock, prog rock, progressive rock, concept album, ai music, suno ai, 70s rock, psychedelic rock
```

**Episode-specific tags (from master.md):**
```
[station name], [episode-specific keywords], [location names if applicable], [character names]
```

**Rules:**
- Maximum 500 characters total (YouTube limit).
- No misleading or unrelated tags.
- Include Turkish variations for discoverability: `anadolu rock`, `psikedelik rock`

### 5. Thumbnail Guidance
Claude does not generate the thumbnail image but provides:
- **Recommended scene:** Which scene (by Shot ID) would make the strongest thumbnail
- **Text overlay suggestion:** A short phrase (max 5 words) for text overlay
- **Color emphasis:** Dominant color that should be boosted for YouTube grid visibility
- **Composition note:** Rule of thirds placement suggestion

### 6. End Screen Recommendations
- **Next episode:** Link to EP{XX+1} if available
- **Playlist:** Link to full ROBOTIKO v2.0 playlist
- **Subscribe CTA:** Brief, non-generic call to action aligned with the project's tone

---

## VERSIONING

- Single output per episode: `ep{XX}_youtube_package.md`
- No version suffix — this is a packaging document, not an iterative creative output.
- If updates are needed, overwrite and commit with a descriptive message.

---

## POST-GENERATION CHECKLIST

- [ ] Title is under 100 characters and includes episode number + title
- [ ] Description opens with a compelling, honest hook
- [ ] Chapter timestamps match musical metadata exactly
- [ ] All chapters start times are accurate (first chapter at 0:00)
- [ ] Tags are within 500 character limit
- [ ] Series description block is consistent with other episodes
- [ ] Thumbnail guidance references a specific scene from the dramaturgy
- [ ] No clickbait, no misleading claims, no cheap marketing language
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Final edit does not exist | STOP. Cannot package an unfinished episode. |
| Musical metadata missing | Generate package without chapter markers. Flag the omission. |
| Previous episode not yet published | Note in end screen section that "Next Episode" link is pending. |
| Episode is EP10 (final) | Adjust end screen to reference playlist and series retrospective instead of next episode. |

---

*"The packaging is the first handshake with the audience. Make it honest, make it precise, make it worthy of the art inside."*
*— Robotiko v2.0 Pipeline*
