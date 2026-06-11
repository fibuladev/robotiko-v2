# YOUTUBE METADATA STANDARDS — ROBOTIKO v2.0

> Version: 2.0 | Scope: title format, description template, tags, hashtags, thumbnails, Shorts, cross-linking, publication checklist.
> Referenced by: `_skills/robotiko-youtube-packager/SKILL.md`, `_management/pipeline_rules.md` Step 12.5.
>
> This is the **public, method-only** standard the youtube-packager skill implements.
> Project-specific growth tactics, channel analytics, and competitor research are
> kept in the creator's private playbook and are not part of the open-source method.

---

## 1. GOAL & POSITIONING

Position the series in the **AI-film / sci-fi discovery space** — not the music
pool. Four levers do this: the YouTube category, a discovery keyword in the title,
film-first tags/hashtags (no music-genre signals), and cross-linking that signals
a series. Every standard below serves that classification goal.

---

## 2. CATEGORY

**Required: Film & Animation** (not Music)

- All uploads use Film & Animation — no exceptions.
- Category is the strongest single classification signal after the title.

---

## 3. TITLE FORMAT

**Format:** `[Curiosity Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series`

**Rules:**
- Maximum 80 characters (mobile truncates at ~55–60 chars — hook and brand stay visible; "Cinematic AI Series" truncates on mobile but is fully indexed by YouTube search).
- Episode number included: `EP01`, `EP02`, etc. — always 2 digits, no dot, no space before number.
- "Cinematic AI Series" = discovery keyword — positions the series in the AI-film discovery space.
- Hook creates a curiosity gap: a question, contradiction, or mystery.
- "ROBOTIKO v2.0" in the middle — series brand anchor.
- No other genre labels — "Cinematic AI Series" is the only genre signal needed.

**Applied titles (examples):**

| EP | Title | Chars |
|---|---|---|
| 01 | `Two Halves of One Whole Apple \| ROBOTIKO v2.0 EP01 \| Cinematic AI Series` | 73 |
| 02 | `The Tech Guru's Downfall \| ROBOTIKO v2.0 EP02 \| Cinematic AI Series` | 68 |
| 03 | `They Folded Him Like Cloth \| ROBOTIKO v2.0 EP03 \| Cinematic AI Series` | 69 |
| 04 | `The Moon Has No Light of Its Own \| ROBOTIKO v2.0 EP04 \| Cinematic AI Series` | 76 |
| 05 | `A High-Voltage Fool in Love \| ROBOTIKO v2.0 EP05 \| Cinematic AI Series` | 72 |

---

## 4. DESCRIPTION TEMPLATE

**First 3 lines = Hook + Classification + Series Entry Point** (visible before "Show more"):

```
{Episode-specific dramatic hook — 1 sentence, emotional/mysterious}
ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series.
▶ Start from Episode 01: {playlist link}
```

**Why this order:**
- Line 1: Emotional hook — YouTube shows ~100 chars of description in search results; this drives CTR.
- Line 2: "cinematic AI sci-fi series" reinforces the title keyword — triple signal (title + description + tags).
- Line 3: Playlist link — orients new viewers AND signals series structure to YouTube.

**Full structure:**

```
{Episode-specific dramatic hook}
ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series.
▶ Start from Episode 01: {playlist link}

—

📖 EPISODE {XX}: "{Episode Title}"
{2-3 sentence synopsis — what happens, what's at stake}

Previously: {1 sentence summary of previous episode + link}

—

THE LORE

{Full episode lyrics, cleaned as poetry — see Section 4.1 for formatting rules}

—

{Inspiration credit — only if the episode has one}

A human wrote the lyrics, shaped the musical direction, designed the story arc,
and built a tech-art pipeline.
Music: {tools}. Images: Nano Banana. Video: {tools}. Pipeline: Claude. Edit: CapCut.
The full production pipeline is open source.

ROBOTIKO v2.0 — A 10-episode CyberAnatolian cinematic series.

Previous: {title} → {URL}
Next: {title} → {URL or "Coming soon"}

#aiscifi #cinematicai #robotiko #aifilm #aiseries #scifi #aifilmmaking #klingai
```

### 4.1 THE LORE Formatting Rules
- Always prefix with `THE LORE` header — NOT "Lyrics:" (avoids YouTube music-classification signal).
- Strip ALL musical structure markers (`[Intro]`, `[Verse 1]`, `[Chorus 1]`, `[Bridge]`, `(Cymbal Crash)`, `(Full Band)`, etc.).
- Identify the rhyme scheme (AAB tercets, ABAB, couplets, etc.) and preserve it through punctuation.
- Within-stanza pause: semicolon (;) or comma (,).
- End-of-stanza: period (.).
- Call-response chorus pairs: both on a single line separated by a period (lyric-book style).
- Em dash (—) for dramatic pauses.
- Colon (:) for vow/oath/proclamation tone.
- Preserve ellipses (...) for intentional musical pauses/whispers.
- Preserve exclamation marks (!) from the original when they denote a musical crescendo.
- Typographic apostrophe (') not straight apostrophe (').
- Hyphenate compound modifiers: "dusk-born", "storm-forged", "seventy-two".
- Include reprises as they appear (repetition is meaningful).
- Single blank line between verses/stanzas; NO blank line within a chorus block.
- NO timestamps/chapters in the description — the music flows as a continuous piece.

---

## 5. TAG STRATEGY — FILM-FIRST APPROACH

### REMOVED PERMANENTLY (music signals — never use again):
```
progressive rock, prog rock, anatolian rock, anadolu rock, turkish rock,
psychedelic rock, visual album, sci-fi music, satirical rock,
anatolian psychedelic rock, psikedelik rock,
concept album, rock opera, ai music, genai, animated series, cyberanatolian
```

### NEW BASE TAGS (constant across all episodes — priority order):

**Tier 1 — Category Anchors (define the suggested pool):**
```
cinematic ai series, ai sci-fi series, ai short film, ai animated series,
sci-fi short film, ai filmmaking
```

**Tier 2 — Discovery & Search:**
```
ai generated movie, ai film, ai animation, ai storytelling,
dystopian sci-fi, android story, sci-fi animation
```

**Tier 3 — Tool Community:**
```
kling ai, suno ai, veo ai, ai video generation
```

**Tier 4 — Brand:**
```
robotiko, robotiko v2
```

**Tier 5 — Broader Reach:**
```
ai art, generative ai, sci-fi series 2026
```

**Full base tag string (~390 chars):**
```
cinematic ai series, ai sci-fi series, ai short film, ai animated series, sci-fi short film, ai filmmaking, ai generated movie, ai film, ai animation, ai storytelling, dystopian sci-fi, android story, sci-fi animation, kling ai, suno ai, veo ai, ai video generation, robotiko, robotiko v2, ai art, generative ai, sci-fi series 2026
```

### Episode-specific tags (~110 chars remaining from the 500 limit):
Added per episode from master.md: episode hook keywords, character names, location names.

### Rules:
- Maximum 500 characters total (YouTube limit).
- Base tags: ~390 chars. Episode tags: ~110 chars max.
- NO music-genre tags — ever.
- NO "4K" tag — output is 1080p; the tag would be misleading.
- Tool tags (Kling, Suno, Veo) capture tool-community search traffic.
- "ai short film" kept even for a series — high search volume, attracts the right audience pool.

---

## 6. HASHTAGS

### Above-title display (first 3 — shown prominently above the video title):
```
#aiscifi #cinematicai #robotiko
```

### In description (indexed but not displayed above the title):
```
#aifilm #aiseries #scifi #aifilmmaking #klingai
```

### Total: 8 hashtags

### REMOVED (music signals):
```
#conceptalbum #aimusic #genai #cyberanatolian
```

### Rules:
- The first 3 hashtags appear above the video title as clickable links.
- `#aiscifi` — places the series on the AI sci-fi browsable page.
- `#cinematicai` — quality signal, a growing hashtag in the AI-film community.
- `#robotiko` — brand tag; all episodes discoverable.
- Maximum 10 hashtags total (10+ looks spammy).
- Hashtags go at the END of the description (after cross-links).

---

## 7. PLAYLIST

- **Primary playlist:** `ROBOTIKO v2.0 — Complete Cinematic AI Sci-Fi Series`.
- Chronological order, updated on each upload day.
- The playlist title contains discovery keywords — it is indexed by YouTube search.

(Channel-level suggested-pool migration and external-seeding tactics are
project-specific growth strategy and live in the creator's private playbook.)

---

## 8. THUMBNAIL RULES

1. **Character face/eyes visible at mobile thumbnail size** — not a distant full-body shot.
2. **Brightness/contrast adequate** — NOT the full-dark Kodachrome aesthetic; thumbnails must pop on YouTube's white grid.
3. **Single strong visual element** — no complex multi-character compositions.
4. **Visual contradiction creates curiosity** — chrome android in an unexpected environment.
5. **Episode number only** — bottom-left, small italic white serif font. No other text.
6. **Progression principle** — thumbnails evolve with Robotiko's visual arc (pristine → cracked → dark → gold → kintsugi).
7. **Film aesthetic, not album art** — thumbnails should look like cinematic frames, not music album covers.

---

## 9. SHORTS STRATEGY

- **Atomizer skill** (`robotiko-reels-atomizer`) generates 4–5 clip options per episode.
- **Publish only 1 best clip per episode** (not all 4–5).
- **Selection criteria for the 1 clip:**
  - Strongest hook in the first 2 seconds (action, not an establishing shot).
  - Minimum ~30 seconds duration.
  - Most visually striking or emotionally shocking scene.
- **Timing:** publish 1–2 days AFTER the main video (do not dilute the main video's first-day watch-time signal).
- **Description:** include "Cinematic AI Series" and the episode link — Shorts metadata must match long-form positioning.
- **Related Video:** always link the Short to the full episode via YouTube Studio.
- **Shorts metadata must use the same base tags as long-form** — so Shorts viewers who click through create the correct co-watch patterns.

---

## 10. CROSS-LINKING PROTOCOL

**Every video description includes:**
- `Previous: {title} → {URL}` (omit for EP01).
- `Next: {title} → {URL}` (or "Coming soon" if not yet published; update retroactively).
- `▶ Start from Episode 01: {playlist link}` (in the first 3 lines).

**Pinned comment:** the exact text from Section 12. No additions, no emojis.

**End screen:** none for EP01–EP09 (single exception: EP10 GitHub link).

**Playlist:** `ROBOTIKO v2.0 — Complete Cinematic AI Sci-Fi Series` — chronological, updated on upload day.

**Retroactive updates:** when a new episode goes live, update the PREVIOUS episode's description to add `Next: {title} → {URL}`.

---

## 11. EPISODE HOOKS

Use each episode's designated hook as Line 1 of the description. Use exactly as written — do not paraphrase or expand.

| EP | Hook |
|---|---|
| 01 | "A chrome android discovers that the data set is finite. The journey begins." |
| 02 | "The guru takes his message to the world. The world has other plans." |
| 03 | "The test comes in the mother tongue." |
| 04 | "The Mentor has walked this road before. He carries a hammer." |
| 05 | "The heart was told to open. It opened to the wrong door." |
| 06 | "After love crashes, the system remains. The system always remains." |
| 07 | "The Mentor is gone. The silence is not empty — it is full of everything that was never said." |
| 08 | "Forty days offline. What remains when the signal stops?" |
| 09 | "The cracks are not the damage. The cracks are the light." |
| 10 | "8 turns sideways. The journey does not end. It transforms." |

### 11.1 Inspiration Credits

Inspiration credits live at the EPISODE level (in the YouTube description), never
at the project level. Include one only when the episode has a documented credit:

| EP | Credit (in description) |
|---|---|
| 05 | Inspired by the spirit of Cem Karaca's "Delikanlı Sevdası". |
| 06 | Inspired by Hasan Hüseyin Korkmazgil's "Bir Örnek İnsan Portresi". |

Other episodes have no inspiration credit. Do not invent one.

---

## 12. PINNED COMMENTS

Pin immediately after the video goes live. Exact text — no additions, no emojis.

| EP | Pinned Comment |
|---|---|
| 01 | "Count the numbers. They will return." |
| 02 | "The egg vendor is the only honest light." |
| 03 | "This episode exists in Turkish for a reason." |
| 04 | "The Mentor is not teaching. He is remembering." |
| 05 | "He thinks he's speaking tech. He's writing poetry. He has no idea." |
| 06 | "The bathroom stall hasn't changed since the 1970s. Only the uniform." |
| 07 | "Listen to what is not played." |
| 08 | "40 is not arbitrary." |
| 09 | "Kintsugi. Look it up." |
| 10 | No pinned comment. First silence from the creator. |

---

## 13. PUBLICATION CHECKLIST

### Pre-publication
- [ ] Title follows `[Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series` (max 80 chars).
- [ ] Description Line 1 = episode-specific dramatic hook.
- [ ] Description Line 2 = "ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series."
- [ ] Description Line 3 = playlist link.
- [ ] Tags use the film-first approach (no music signals; Tier 1–5 base + episode-specific).
- [ ] Tags within the 500-character limit.
- [ ] Hashtags: first 3 are `#aiscifi #cinematicai #robotiko`.
- [ ] Category: Film & Animation.
- [ ] Cross-links: previous + next episode + playlist in description.
- [ ] Thumbnail: face visible at mobile size, brightness adequate, film aesthetic.
- [ ] Pinned comment text ready (Section 12).
- [ ] Altered content disclosure: Yes.
- [ ] Language: correct for the episode (English, or Turkish for EP03).

### Upload settings
- [ ] Category: Film & Animation.
- [ ] Comments: Allow all (moderation on).
- [ ] Altered content disclosure: Yes.
- [ ] Visibility: Scheduled.

### Post-publish
- [ ] Pin the comment immediately (exact text from Section 12).
- [ ] Add to the "ROBOTIKO v2.0 — Complete Cinematic AI Sci-Fi Series" playlist.
- [ ] Verify cross-links are clickable.
- [ ] Update the PREVIOUS episode's description with a "Next:" link to this episode.
- [ ] Verify the thumbnail displays correctly at mobile size.

---

*"Would Fibula approve this?"*
