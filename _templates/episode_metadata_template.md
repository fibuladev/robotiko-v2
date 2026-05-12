# EPISODE METADATA TEMPLATE (YOUTUBE)
> Version: 1.0 | Source: `_management/youtube_strategy_v01.md`
> This template is populated by Claude via `_skills/robotiko-youtube-packager/SKILL.md`
> Do not fill manually.

---

## PRE-GENERATION CHECKLIST

- [ ] `_management/youtube_strategy_v01.md` — Metadata standards, tag list, category
- [ ] `_management/master.md` — Episode title, station, tone, key lyrics
- [ ] `_management/creator_strategy.md` — Episode hooks, pinned comments, inspiration credits
- [ ] `episode-{XX}/01_lyrics/ep{XX}_lyrics_v{VV}.md` — Full lyrics for description
- [ ] `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` — Scene references for thumbnail

---

## 1. VIDEO TITLE

**Format:** `[CURIOSITY HOOK] | ROBOTIKO`

```
{hook} | ROBOTIKO
```

**Rules:**
- Maximum 70 characters
- No episode number, no genre label, no "Visual Album"
- Hook creates curiosity gap — question, contradiction, or mystery

---

## 2. VIDEO DESCRIPTION

```
An AI-generated cinematic series. Episode {XX} of 10.
{Episode hook from creator_strategy.md — exact text}
Full journey → [playlist link]

—

Lyrics:

{Full lyrics from ep{XX}_lyrics.md, cleaned as poetry}
{Strip ALL musical structure markers: [Intro], [Verse 1], [Chorus], (Full Band), etc.}
{Preserve rhyme scheme through punctuation — see SKILL.md for detailed rules}

—

{Inspiration credit — ONLY if listed in creator_strategy.md for this episode}

A human wrote the lyrics, shaped the musical direction, designed the story arc,
and built a tech-art pipeline.
Music: {Suno / Suno + BandLab}. Images: Nano Banana. Video: {Kling + Seedance / Kling + Veo + Seedance / etc.}. Pipeline: Claude. Edit: CapCut.
The full production pipeline will be open source after the finale.

ROBOTIKO v2.0 — A 10-episode CyberAnatolian concept album and visual series.
Subscribe to walk beside.

Previous: {Previous episode title} → {URL}
Next: {Next episode title} → {URL or "Coming soon"}

#robotiko #cyberanatolian #conceptalbum #aiart #aimusic #genai
```

---

## 3. PINNED COMMENT

```
{Exact text from creator_strategy.md Section 2.7 for EP{XX}}
```

Pin immediately after video goes live. No additions, no emojis. Exact text.

---

## 4. TAGS

**Base tags (constant — from youtube_strategy_v01.md Section 5):**
```
robotiko, robotiko v2.0, cyberanatolian, concept album, rock opera, ai generated video, ai cinematic, ai animation, ai art, ai music, suno ai, genai, ai film, ai series, ai short film, ai storytelling, concept album film, animated series, sci-fi animation
```

**Episode-specific tags:**
```
{episode title}, {station keywords from master.md}, {location names if applicable}, {character names}
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

## 6. END SCREEN

Per `creator_strategy.md` Section 2.6: **No end screens EP01-EP09.**
EP10 only: GitHub repository link.

- **Playlist:** "ROBOTIKO v2.0 — The Full Journey"
- **Cross-link notes:** {previous/next episode update reminders}

---

## 7. SETTINGS

- **Category:** Film & Animation
- **Language:** {English / Turkish}
- **Altered content disclosure:** Yes
- **Comments:** Allow all (moderation on)
- **Visibility:** Scheduled for 20:00 CET

---

*"Would Fibula approve this?"*
