# SKILL: robotiko-youtube-packager
> **Version:** 4.0
> **Trigger:** `"Package EP{XX} for YouTube"`
> **Output:** `episode-{XX}/07_social_media/ep{XX}_youtube_package.md`

---

## PURPOSE

Generate a complete YouTube metadata package for a finished episode: title, description, thumbnail guidance, and end screen recommendations. All metadata standards are defined in `_management/youtube_metadata_standards.md` — this skill implements those standards.

---

## PREREQUISITE

> The episode's final video edit must be complete (`episode-{XX}/06_edit/ep{XX}_final_v{VV}.mp4` exists).
> If the final edit does not exist, STOP. Packaging requires a finished product.

---

## MANDATORY INPUTS

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/youtube_metadata_standards.md` | Metadata standards, category, title format, description template, episode hooks, pinned comments, inspiration credits |
| 2 | `_management/master.md` | Episode title, station, tone, key lyrics, logline, philosophical context |
| 3 | `episode-{XX}/02_music/ep{XX}_musical_metadata.json` | Episode duration and musical context |
| 4 | `episode-{XX}/03_direction/ep{XX}_dramaturgy_v{VV}.md` | Scene breakdown for thumbnail guidance |
| 5 | `_management/project_metadata.json` | Episode status confirmation, series context |

---

## OUTPUT STRUCTURE

### 1. Video Title
**Format:** `[Curiosity Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series`

**Rules:**
- Maximum 80 characters
- Episode number included: `EP01`, `EP02`, etc. — always 2 digits, no dot
- "Cinematic AI Series" = the fixed series descriptor that closes every title
- Hook — the episode's one-line dramatic phrase (question, contradiction, or mystery)
- "ROBOTIKO v2.0" in the middle — series brand anchor
- Do not use clickbait or misleading titles — the art speaks for itself

**Example:**
```
The Tech Guru's Downfall | ROBOTIKO v2.0 EP02 | Cinematic AI Series
```

### 2. Video Description
**Structure (3-section format — hook + lore + credits/cross-links):**
```
{Episode-specific dramatic hook from youtube_metadata_standards.md — exact text}
ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series.
▶ Start from Episode 01: {playlist link}

—

THE LORE

[Full episode lyrics from ep{XX}_lyrics_v{VV}.md (latest version), cleaned as poetry — see rules below]

—

[Inspiration credit — ONLY if listed in youtube_metadata_standards.md for this episode]

A human wrote the lyrics, shaped the musical direction, designed the story arc,
and built a tech-art pipeline.
Music: {tools}. Images: Nano Banana. Video: {tools}. Pipeline: Claude. Edit: CapCut.
The full production pipeline will be open source after the finale.

ROBOTIKO v2.0 — A 10-episode CyberAnatolian cinematic series.

Previous: {title} → {URL}
Next: {title} → {URL or "Coming soon"}

#aiscifi #cinematicai #robotiko #aifilm #aiseries #scifi #aifilmmaking #aiart
```

**Rules:**
- **First 3 lines = Hook + Series Descriptor + Series Entry Point.** Line 1: dramatic hook. Line 2: "cinematic AI sci-fi series" — the series descriptor. Line 3: playlist link orients new viewers.
- Opening hook is the episode's single-sentence hook from `youtube_metadata_standards.md` — NOT a custom-written hook.
- **Cross-links required:** Previous and Next episode links in every description. Update previous episode's description when a new episode goes live.
- **Lore section rules (critical):**
  - Always prefix with `THE LORE` header — NOT "Lyrics:"
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
- Inspiration credits (e.g., EP05: Cem Karaca, EP06: Korkmazgil) only when specified in youtube_metadata_standards.md
- Keep description a **literary document**, not marketing copy

### 3. Episode Hooks (The Hidden Poem)

Each episode uses its designated hook from `youtube_metadata_standards.md` as the opening line of the description. These hooks form a thematic arc across the series:

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
| EP10 | "8 turns sideways. The journey does not end. It transforms." (see launch-orchestrator: the ten-episode arc is complete, framed as transformation not continuation) |

**Rule:** Use these EXACTLY as written. Do not paraphrase or expand.

### 4. Pinned Comment

Each episode has a cryptic pinned comment — a breadcrumb for curious viewers. These are defined in `youtube_metadata_standards.md`:

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

### 5. Thumbnail Guidance
Claude does not generate the thumbnail image but provides:
- **Recommended scene:** Which scene (by Shot ID) would make the strongest thumbnail — the hero shot from the dramaturgy
- **NO text on thumbnail.** Episode number only, bottom-left corner. No title, no quotes, no overlays.
- **Color emphasis:** Dominant color of the chosen frame
- **Composition note:** Rule of thirds placement suggestion
- **Progression check:** Side-by-side with previous episode thumbnails, does the visual arc show? (Pristine → cracked → dark → gold)

### 6. End Screen Recommendations
- **Next episode:** Link to EP{XX+1} if available
- **Playlist:** Link to full ROBOTIKO v2.0 playlist

---

## VERSIONING

- Single output per episode: `ep{XX}_youtube_package.md`
- No version suffix — this is a packaging document, not an iterative creative output.
- If updates are needed, overwrite and commit with a descriptive message.

---

## POST-GENERATION CHECKLIST

- [ ] Title follows `[Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series` format (max 80 characters)
- [ ] Description Line 1 = episode-specific dramatic hook from youtube_metadata_standards.md
- [ ] Description Line 2 = "ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series."
- [ ] Description Line 3 = playlist link
- [ ] Description has NO timestamps/chapters
- [ ] Cross-links present: previous + next episode + playlist
- [ ] Category: Film & Animation (not Music)
- [ ] Thumbnail guidance references a specific scene from the dramaturgy
- [ ] Thumbnail has NO text (only episode number bottom-left)
- [ ] Pinned comment matches youtube_metadata_standards.md exactly
- [ ] Inspiration credit included only if specified in youtube_metadata_standards.md for this episode
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
