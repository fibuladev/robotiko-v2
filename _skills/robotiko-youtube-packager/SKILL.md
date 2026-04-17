# SKILL: robotiko-youtube-packager
> **Version:** 2.0 | **Last Updated:** 2026-04-07
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
| 5 | `_management/creator_strategy.md` | Episode hooks, pinned comments, inspiration credits, hashtag rules |

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
[Episode hook — single sentence from creator_strategy.md Episode Hooks list]

"[Key lyric quote from master.md — italicized]"

---

[Episode context — which station, where in the journey, what Robotiko faces]

[Musical identity — genre, instruments, influences for this episode]

[Inspiration credit — ONLY if listed in creator_strategy.md for this episode]

---

🎵 ABOUT ROBOTIKO v2.0
[Series description — consistent across all episodes]
Drawing from Turkish philosophy, Turkish folk poetry,
and the 70s Turkish psychedelic rock legacy.
[Link to playlist]

---

🎨 CREDITS
Music: Suno AI
Images: Nano Banana
Video: Kling / Veo / Seedance
Direction & Pipeline: Claude
Editing: CapCut
Created by one human in Bratislava.

---

#robotiko #cyberanatolian #progrock #anatolianrock #conceptalbum
```

**Rules:**
- Opening hook is the episode's single-sentence hook from `creator_strategy.md` — NOT a custom-written hook.
- Key lyric should be the episode's most representative line from master.md.
- **NO timestamps/chapters in description.** Music flows as a continuous piece.
- Series description block is reusable across episodes — write once, copy across.
- Tags section uses hashtags relevant to the genre and project.
- **#aiart is NOT used before EP07** (per creator_strategy.md).
- Inspiration credits (e.g., EP05: Cem Karaca, EP06: Korkmazgil) only when specified in creator_strategy.md.
- EP07+ descriptions include open source rollout text per creator_strategy.md schedule.

### 3. Episode Hooks (The Hidden Poem)

Each episode uses its designated hook from `creator_strategy.md` as the opening line of the description. These hooks form a thematic arc across the series:

| Episode | Hook |
|---------|------|
| EP01 | "A chrome android discovers that the data set is finite. The journey begins." |
| EP02 | "The guru takes his message to the world. The world has other plans." |
| EP03 | "The test comes in the mother tongue." |
| EP04 | "The Mentor has walked this road before. He carries a hammer." |
| EP05 | "The heart was told to open. It opened to the wrong door." |
| EP06 | "After love crashes, the system remains. The system always remains." |
| EP07 | "The Mentor is gone. The silence is not empty — it is full of everything that was never said." |
| EP08 | "Forty days offline. What remains when the signal stops?" |
| EP09 | "The cracks are not the damage. The cracks are the light." |
| EP10 | "8 turns sideways. The journey does not end. It transforms." |

**Rule:** Use these EXACTLY as written. Do not paraphrase or expand.

### 4. Pinned Comment

Each episode has a cryptic pinned comment — a breadcrumb for curious viewers. These are defined in `creator_strategy.md`:

| Episode | Pinned Comment |
|---------|---------------|
| EP01 | "Count the numbers. They will return." |
| EP02 | "The egg vendor is the only honest light." |
| EP03 | "This episode exists in Turkish for a reason." |
| EP04 | "The Mentor is not teaching. He is remembering." |
| EP05 | "He thinks he's speaking tech. He's writing poetry. He has no idea." |
| EP06 | "The bathroom stall hasn't changed since the 1970s. Only the uniform." |
| EP07 | "Listen to what is not played." |
| EP08 | "40 is not arbitrary." |
| EP09 | "Kintsugi. Look it up." |
| EP10 | No pinned comment. First silence from the creator. |

**Rule:** Pin this comment immediately after the video goes live. Use the exact text — no additions, no emojis.

### 5. Tags
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

### 6. Thumbnail Guidance
Claude does not generate the thumbnail image but provides:
- **Recommended scene:** Which scene (by Shot ID) would make the strongest thumbnail — the hero shot from the dramaturgy
- **NO text on thumbnail.** Episode number only, bottom-left corner. No title, no quotes, no overlays.
- **Color emphasis:** Dominant color that should be boosted for YouTube grid visibility
- **Composition note:** Rule of thirds placement suggestion
- **Progression check:** Side-by-side with previous episode thumbnails, does the visual arc show? (Pristine → cracked → dark → gold)

### 7. End Screen Recommendations
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
- [ ] Description opens with the episode hook from creator_strategy.md (exact text)
- [ ] Description has NO timestamps/chapters
- [ ] Tags are within 500 character limit
- [ ] Series description block is consistent with other episodes
- [ ] Thumbnail guidance references a specific scene from the dramaturgy
- [ ] Thumbnail has NO text (only episode number bottom-left)
- [ ] Pinned comment matches creator_strategy.md exactly
- [ ] #aiart NOT used before EP07
- [ ] Inspiration credit included only if specified in creator_strategy.md for this episode
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
