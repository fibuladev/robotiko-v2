# YOUTUBE METADATA STANDARDS — ROBOTIKO v2.0

> Version: 2.1 | Scope: category, title format, description template, playlist, thumbnail composition, Shorts, cross-linking, publication checklist.
> Referenced by: `_skills/robotiko-youtube-packager/SKILL.md`, `_management/pipeline_rules.md` Step 12.5.
>
> This is the **public, method-only** standard the youtube-packager skill implements.
> It covers the craft of shipping an episode — how the upload is named, described,
> credited, and disclosed. Audience-growth and algorithm tactics are not part of the
> open method; they live in the creator's private notes.

---

## 1. CATEGORY

**Film & Animation** (not Music) — all uploads, no exceptions. The series is a
cinematic film series, not a music release.

---

## 2. TITLE FORMAT

**Format:** `[Curiosity Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series`

**Rules:**
- Maximum 80 characters.
- Episode number included: `EP01`, `EP02`, etc. — always 2 digits, no dot, no space before the number.
- Hook — the episode's one-line dramatic phrase (a question, contradiction, or mystery).
- "ROBOTIKO v2.0" in the middle — series brand anchor.
- "Cinematic AI Series" — the fixed series descriptor that closes every title.

**Applied titles (examples):**

| EP | Title | Chars |
|---|---|---|
| 01 | `Two Halves of One Whole Apple \| ROBOTIKO v2.0 EP01 \| Cinematic AI Series` | 73 |
| 02 | `The Tech Guru's Downfall \| ROBOTIKO v2.0 EP02 \| Cinematic AI Series` | 68 |
| 03 | `They Folded Him Like Cloth \| ROBOTIKO v2.0 EP03 \| Cinematic AI Series` | 69 |
| 04 | `The Moon Has No Light of Its Own \| ROBOTIKO v2.0 EP04 \| Cinematic AI Series` | 76 |
| 05 | `A High-Voltage Fool in Love \| ROBOTIKO v2.0 EP05 \| Cinematic AI Series` | 72 |

---

## 3. DESCRIPTION TEMPLATE

**First 3 lines = Hook + Series Descriptor + Series Entry Point** (visible before "Show more"):

```
{Episode-specific dramatic hook — 1 sentence, emotional/mysterious}
ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series.
▶ Start from Episode 01: {playlist link}
```

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

{Full episode lyrics, cleaned as poetry — see Section 3.1 for formatting rules}

—

{Inspiration credit — only if the episode has one}

A human wrote the lyrics, shaped the musical direction, designed the story arc,
and built a tech-art pipeline.
Music: {tools}. Images: Nano Banana. Video: {tools}. Pipeline: Claude. Edit: CapCut.
The full production pipeline is open source.

ROBOTIKO v2.0 — A 10-episode CyberAnatolian cinematic series.

Previous: {title} → {URL}
Next: {title} → {URL or "Coming soon"}

{relevant series + episode hashtags}
```

### 3.1 THE LORE Formatting Rules
- Always prefix with the `THE LORE` header.
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

## 4. PLAYLIST

- **Primary playlist:** `ROBOTIKO v2.0 — Complete Cinematic AI Sci-Fi Series`.
- Chronological order, updated on each upload day.

---

## 5. THUMBNAIL COMPOSITION

1. **Character face/eyes visible** — not a distant full-body shot.
2. **Brightness/contrast adequate** — NOT the full-dark Kodachrome aesthetic; the frame must stay legible at small size.
3. **Single strong visual element** — no complex multi-character compositions.
4. **A striking single image** — the chrome android in an unexpected environment.
5. **Episode number only** — bottom-left, small italic white serif font. No other text.
6. **Progression principle** — thumbnails evolve with Robotiko's visual arc (pristine → cracked → dark → gold → kintsugi).
7. **Film aesthetic, not album art** — thumbnails should look like cinematic frames, not music album covers.

The chosen thumbnail is a scene choice — pick the frame that best represents the episode.

---

## 6. SHORTS

- **Atomizer skill** (`robotiko-reels-atomizer`) generates a few clip options per episode.
- **Publish 1 clip per episode** — the strongest single moment.
- **Selection:** the most visually striking or emotionally resonant scene; minimum ~30 seconds.
- **Description:** include "Cinematic AI Series" and the episode link.
- **Related Video:** always link the Short to the full episode via YouTube Studio.

---

## 7. CROSS-LINKING PROTOCOL

**Every video description includes:**
- `Previous: {title} → {URL}` (omit for EP01).
- `Next: {title} → {URL}` (or "Coming soon" if not yet published; update retroactively).
- `▶ Start from Episode 01: {playlist link}` (in the first 3 lines).

**Pinned comment:** the exact text from Section 9. No additions, no emojis.

**End screen:** YouTube end screens are not used in this project — the 2.35:1 letterbox leaves no safe zone for them. The EP10 finale instead closes with an in-video end card (S35), built at the edit stage.

**Playlist:** `ROBOTIKO v2.0 — Complete Cinematic AI Sci-Fi Series` — chronological, updated on upload day.

**Retroactive updates:** when a new episode goes live, update the PREVIOUS episode's description to add `Next: {title} → {URL}`.

---

## 8. EPISODE HOOKS

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

### 8.1 Inspiration Credits

Inspiration credits live at the EPISODE level (in the YouTube description), never
at the project level. Include one only when the episode has a documented credit:

| EP | Credit (in description) |
|---|---|
| 05 | Inspired by the spirit of Cem Karaca's "Delikanlı Sevdası". |
| 06 | Inspired by Hasan Hüseyin Korkmazgil's "Bir Örnek İnsan Portresi". |
| 09 | Inspired by Yunus Emre's "Bir ben vardır bende benden içeri" (Turkish folk poetry). |
| 10 | Answer-poem after Nimri Dede's "İnsan Olmaya Geldim" (Turkish folk poetry). |

Other episodes have no inspiration credit. Do not invent one.

---

## 9. PINNED COMMENTS

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

## 10. PUBLICATION CHECKLIST

### Pre-publication
- [ ] Title follows `[Hook] | ROBOTIKO v2.0 EP{XX} | Cinematic AI Series` (max 80 chars).
- [ ] Description Line 1 = episode-specific dramatic hook.
- [ ] Description Line 2 = "ROBOTIKO v2.0 — Episode {XX} of 10. A cinematic AI sci-fi series."
- [ ] Description Line 3 = playlist link.
- [ ] Category: Film & Animation.
- [ ] Cross-links: previous + next episode + playlist in description.
- [ ] Thumbnail: face visible at small size, brightness adequate, film aesthetic, chosen scene set.
- [ ] Pinned comment text ready (Section 9).
- [ ] Altered content disclosure: Yes.
- [ ] Language: correct for the episode (English, or Turkish for EP03).

### Upload settings
- [ ] Category: Film & Animation.
- [ ] Comments: Allow all (moderation on).
- [ ] Altered content disclosure: Yes.
- [ ] Visibility: Scheduled.

### Post-publish
- [ ] Pin the comment immediately (exact text from Section 9).
- [ ] Add to the "ROBOTIKO v2.0 — Complete Cinematic AI Sci-Fi Series" playlist.
- [ ] Verify cross-links are clickable.
- [ ] Update the PREVIOUS episode's description with a "Next:" link to this episode.
- [ ] Verify the thumbnail displays correctly at small size.

---

*"Would Fibula approve this?"*
