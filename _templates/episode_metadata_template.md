# EPISODE METADATA TEMPLATE (YOUTUBE)
> Version: 2.0 | Source: `_management/youtube_metadata_standards.md`
> This template is populated by Claude via `_skills/robotiko-youtube-packager/SKILL.md`
> Do not fill manually.

---

## PRE-GENERATION CHECKLIST

- [ ] `_management/youtube_metadata_standards.md` — Title format, tags, description, hashtags, episode hooks (§11), pinned comments (§12), inspiration credits (§11.1)
- [ ] `_management/master.md` — Episode title, station, tone, key lyrics
- [ ] `episode-{XX}/01_lyrics/ep{XX}_lyrics_v{VV}.md` — Full lyrics for description
- [ ] `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` — Scene references for thumbnail

---

## 1. VIDEO TITLE

**Format:** `[Curiosity Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series`

```
{hook} | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series
```

**Rules:**
- Maximum 80 characters
- Episode number always 2 digits (`EP01`); "Cinematic AI Series" is the only genre signal
- Hook creates a curiosity gap — question, contradiction, or mystery

---

## 2. VIDEO DESCRIPTION

```
{Episode hook from youtube_metadata_standards.md §11 — exact text}
ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series.
▶ Start from Episode 01: {playlist link}

—

THE LORE

{Full lyrics from ep{XX}_lyrics.md, cleaned as poetry}
{Strip ALL musical structure markers: [Intro], [Verse 1], [Chorus], (Full Band), etc.}
{Preserve rhyme scheme through punctuation — see SKILL.md / standards §4.1 for rules}

—

{Inspiration credit — ONLY if listed in youtube_metadata_standards.md §11.1 for this episode}

A human wrote the lyrics, shaped the musical direction, designed the story arc,
and built a tech-art pipeline.
Music: {Suno / Suno + BandLab}. Images: Nano Banana. Video: {Kling + Seedance / Kling + Veo + Seedance / etc.}. Pipeline: Claude. Edit: CapCut.
The full production pipeline is open source.

ROBOTIKO v2.0 — A 10-episode CyberAnatolian cinematic series.

Previous: {Previous episode title} → {URL}
Next: {Next episode title} → {URL} (EP01-EP09 only — omit this line for EP10; the ten-episode arc is complete)

#aiscifi #cinematicai #robotiko #aifilm #aiseries #scifi #aifilmmaking #klingai
```

---

## 3. PINNED COMMENT

```
{Exact text from youtube_metadata_standards.md §12 for EP{XX}}
```

Pin immediately after video goes live. No additions, no emojis. Exact text.

---

## 4. TAGS

**Base tags (constant — from youtube_metadata_standards.md §5):**
```
cinematic ai series, ai sci-fi series, ai short film, ai animated series, sci-fi short film, ai filmmaking, ai generated movie, ai film, ai animation, ai storytelling, dystopian sci-fi, android story, sci-fi animation, kling ai, suno ai, veo ai, ai video generation, robotiko, robotiko v2, ai art, generative ai, sci-fi series 2026
```

**Episode-specific tags:**
```
{episode hook keywords}, {station keywords from master.md}, {location names if applicable}, {character names}
```

**Combined (paste into YouTube):**
```
{base + episode-specific, within 500 char limit}
```

---

## 5. THUMBNAIL BRIEF

- **Recommended scene:** {Shot ID from dramaturgy — strongest thumbnail candidate}
- **"{XX}" only** — bottom-left corner, small, italic white serif font. No other text.
- **Face/character:** Must be visible and readable at mobile thumbnail size
- **Brightness:** Adequate for YouTube grid visibility — not full dark
- **Single strong visual element**
- **Progression check:** Side-by-side with previous thumbnails — does the visual arc show?

---

## 6. CROSS-LINKS

YouTube end screens are not used in this project (2.35:1 letterbox); the EP10 finale closes with an in-video end card (S35), built at the edit stage.

- **Playlist:** "ROBOTIKO v2.0 — Complete Cinematic AI Sci-Fi Series"
- **Cross-link notes:** {previous/next episode update reminders}

---

## 7. SETTINGS

- **Category:** Film & Animation
- **Language:** {English / Turkish}
- **Altered content disclosure:** Yes
- **Comments:** Allow all (moderation on)
- **Visibility:** Scheduled

---

*"Would Fibula approve this?"*
