# SKILL: robotiko-youtube-packager
> **Version:** 3.0 | **Last Updated:** 2026-05-12
> **Trigger:** `"Package EP{XX} for YouTube"`
> **Output:** `episode-{XX}/07_social_media/ep{XX}_youtube_package.md`

---

## PURPOSE

Generate a complete YouTube metadata package for a finished episode: title, description, tags, thumbnail guidance, and end screen recommendations. All metadata standards are defined in `_management/youtube_strategy_v01.md` — this skill implements those standards.

---

## PREREQUISITE

> The episode's final video edit must be complete (`episode-{XX}/06_edit/ep{XX}_final_v{VV}.mp4` exists).
> If the final edit does not exist, STOP. Packaging requires a finished product.

---

## MANDATORY INPUTS

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/youtube_strategy_v01.md` | Metadata standards, tag list, category, title format, description template |
| 2 | `_management/master.md` | Episode title, station, tone, key lyrics, logline, philosophical context |
| 3 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Episode duration and musical context |
| 4 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Scene breakdown for thumbnail guidance |
| 5 | `_management/project_metadata.json` | Episode status confirmation, series context |
| 6 | `_management/creator_strategy.md` | Episode hooks, pinned comments, inspiration credits |

---

## OUTPUT STRUCTURE

### 1. Video Title
**Format:** `[Curiosity Hook] | ROBOTIKO v2.0`

**Rules:**
- Maximum 70 characters
- No episode numbers (meaningless to new viewers; playlists show order)
- No genre labels ("Visual Album", "Anatolian Psychedelic Rock" — all removed)
- Hook creates a curiosity gap — question, contradiction, or mystery
- "ROBOTIKO" always at the end after pipe
- Do not use clickbait or misleading titles — the art speaks for itself

**Example:**
```
The Tech Guru's Downfall | ROBOTIKO
```

### 2. Video Description
**Structure (3-section format — AI categorization signal + lore + credits/cross-links):**
```
An AI-generated cinematic series. Episode {XX} of 10.
[Episode hook — single sentence from creator_strategy.md Episode Hooks list]
Full journey → [playlist link]

—

THE LORE

[Full episode lyrics from ep{XX}_lyrics.md, cleaned as poetry — see rules below]

—

[Inspiration credit — ONLY if listed in creator_strategy.md for this episode]

A human wrote the lyrics, shaped the musical direction, designed the story arc,
and built a tech-art pipeline.
Music: {tools}. Images: Nano Banana. Video: {tools}. Pipeline: Claude. Edit: CapCut.
The full production pipeline will be open source after the finale.

ROBOTIKO v2.0 — A 10-episode CyberAnatolian concept album and visual series.
Subscribe to walk beside.

Previous: {title} → {URL}
Next: {title} → {URL or "Coming soon"}

#robotiko #cyberanatolian #conceptalbum #aiart #aimusic #genai
```

**Rules:**
- **First 3 lines = AI categorization signal.** YouTube reads these most heavily for classification. "An AI-generated cinematic series" signals Film & Animation, not Music.
- Opening hook is the episode's single-sentence hook from `creator_strategy.md` — NOT a custom-written hook.
- **Cross-links required:** Previous and Next episode links in every description. Update previous episode's description when a new episode goes live.
- **Lore section rules (critical):**
  - Always prefix with `THE LORE` header — NOT "Lyrics:" (avoids YouTube music classification signal)
  - Strip ALL musical structure markers (`[Intro]`, `[Verse 1]`, `[Chorus 1]`, `[Bridge]`, `(Cymbal Crash)`, `(Full Band)`, etc.)
  - **Identify rhyme scheme (AAB tercets, ABAB, couplets, etc.) and preserve it through punctuation:**
    - Within-stanza pause: semicolon (;) or comma (,)
    - End-of-stanza: period (.)
    - Don't break tercets with periods mid-structure — this loses the AAB bond
  - **Call-response chorus pairs (AI vs Human, Q&A structure):** Place both on a single line separated by period. This represents vocal duet structure (Leonard Cohen lyric book style)
  - Use em dash (—) for dramatic pauses, not semicolon (e.g., "Five thousand years I've waited—now enough")
  - Use colon (:) for vow/oath/proclamation tone (e.g., "Trust me: the eight shall turn aside")
  - Preserve ellipses (...) for intentional musical pauses/whispers
  - Preserve exclamation marks (!) from original when they denote musical crescendo
  - Use typographic apostrophe (') not straight apostrophe (')
  - Hyphenate compound modifiers: "dusk-born", "storm-forged", "seventy-two"
  - Include reprises as they appear in song (literary emphasis — repetition is meaningful)
  - Single blank line between verses/stanzas; NO blank line within a chorus block
- **NO timestamps/chapters in description.** Music flows as a continuous piece.
- **NO "About ROBOTIKO" block** — channel About section handles project identity
- Credits block is embedded in the description template above
- **#aiart used from EP01** — AI transparency from day one
- **NO genre hashtags** (#progrock, #psychedelicrock, etc.) — see youtube_strategy_v01.md Section 5
- Inspiration credits (e.g., EP05: Cem Karaca, EP06: Korkmazgil) only when specified in creator_strategy.md
- Keep description a **literary document**, not marketing copy

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
Two categories — per `_management/youtube_strategy_v01.md` Section 5 (layered approach):

**Base tags (constant across all episodes):**
```
robotiko, robotiko v2.0, cyberanatolian, concept album, rock opera, ai generated video, ai cinematic, ai animation, ai art, ai music, suno ai, genai, ai film, ai series, ai short film, ai storytelling, concept album film, animated series, sci-fi animation
```

**Episode-specific tags (from master.md):**
```
[episode title], [station keywords], [location names if applicable], [character names]
```

**Rules:**
- Maximum 500 characters total (YouTube limit).
- No misleading or unrelated tags.
- **NO music-genre tags** (progressive rock, psychedelic rock, turkish rock, anatolian rock, visual album — all removed).
- Format tags KEPT (concept album, rock opera) — these signal content format, not music genre.

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

- [ ] Title follows `[Hook] | ROBOTIKO v2.0` format (max 70 characters, no EP number, no genre)
- [ ] Description first 3 lines = AI categorization signal ("An AI-generated cinematic series...")
- [ ] Description opens with episode hook from creator_strategy.md (exact text, line 2)
- [ ] Description has NO timestamps/chapters
- [ ] Cross-links present: previous + next episode + playlist
- [ ] Tags use layered approach: NO genre tags, AI + format tags present
- [ ] Tags are within 500 character limit
- [ ] Category: Film & Animation (not Music)
- [ ] Hashtags: `#robotiko #cyberanatolian #conceptalbum #aiart #aimusic #genai` (no genre hashtags)
- [ ] Thumbnail guidance references a specific scene from the dramaturgy
- [ ] Thumbnail has NO text (only episode number bottom-left)
- [ ] Pinned comment matches creator_strategy.md exactly
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
