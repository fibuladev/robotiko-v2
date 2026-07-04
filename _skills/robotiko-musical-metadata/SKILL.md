# SKILL: robotiko-musical-metadata
> **Version:** 1.0 | **Last Updated:** 2026-03-31
> **Trigger:** `"Create musical metadata for EP{XX}"`
> **Output:** `episode-{XX}/02_music/ep{XX}_musical_metadata.json`

---

## PURPOSE

Convert human-provided track analysis (BPM, key, timestamped lyrics) into the structured musical metadata JSON that drives the entire Robotiko production pipeline. This JSON is the temporal skeleton of each episode — every scene, visual prompt, and camera move is anchored to it.

---

## PREREQUISITE

> **The human MUST provide the following data before this skill executes.**
> This skill cannot analyze audio files. BPM, key, and timestamps come from human listening + external tools.

---

## MANDATORY INPUTS FROM HUMAN

| # | Input | Source | Required? |
|---|---|---|---|
| 1 | **BPM** | [vocalremover.org/key-bpm-finder](https://vocalremover.org/key-bpm-finder) or similar | **YES** |
| 2 | **Key** | Same tool as BPM | **YES** |
| 3 | **Timestamped lyrics** | Human listens to WAV and maps lyrics to timestamps (MM:SS format) | **YES** |
| 4 | **Mood keywords** | Human describes the overall feel | Optional (Claude infers from master.md if omitted) |
| 5 | **Notable instruments** | Human notes key instruments heard | Optional (Claude infers from lyrics annotations if omitted) |

### Timestamped Lyrics Format

The human provides lyrics in this format — section headers with timestamps, lyrics below:

```
[Intro] (0:00 - 0:32)
(Style: Smooth Bass Line & Light Drums)

[Verse 1] (0:33 - 0:49)
Don't you walk so slow...
don't you step so light...

[Chorus] (1:32 - 2:04)
I laser-etched your name
on my metal shell!
```

**What the human provides:**
- Section type in brackets: `[Intro]`, `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Guitar Solo]`, `[Outro]`, etc.
- Timestamp range in parentheses: `(0:33 - 0:49)` or `(timestamp: 0:33 - 0:49)`
- Lyrics below the header (plain text)
- Performance/arrangement notes in parentheses: `(Vocal Style: Soft Baritone)`, `(Style: Slow Blues Solo)`

**What Claude extracts:**
- Section type → `"type"` field
- Timestamps → `"start"` and `"end"` fields (converted to seconds)
- Lyrics → `"lyrics"` field (cleaned, joined as prose)
- Performance notes → `"notes"` field

---

## MANDATORY READS (Before Generating)

| # | File | What to Extract |
|---|---|---|
| 1 | `_management/master.md` | Episode tone, station, music style, key lyrics |
| 2 | `episode-{XX}/01_lyrics/ep{XX}_lyrics_v01.md` | Cross-reference lyrics if available |

---

## JSON SCHEMA

```json
{
  "track_title": "string — from master.md episode title",
  "tempo": "number — BPM from human input",
  "key": "string — musical key from human input (e.g., 'E Minor', 'G Major')",
  "time_signature": "string — default '4/4' unless human specifies otherwise",
  "total_duration": "number — end timestamp of last section (in seconds)",
  "mood": ["string array — emotional keywords describing the track"],
  "instruments": ["string array — key instruments heard/noted"],
  "sections": [
    {
      "type": "string — section type (see Section Types below)",
      "start": "number — start time in seconds",
      "end": "number — end time in seconds",
      "energy": "string — energy level (see Energy Levels below)",
      "lyrics": "string — section lyrics as continuous prose (OPTIONAL — instrumental sections omit this)",
      "notes": "string — arrangement, vocal style, performance notes (OPTIONAL)"
    }
  ]
}
```

---

## SECTION TYPES

Map human-provided section headers to these standardized types:

| Human Input | JSON Type | Description |
|---|---|---|
| `[Intro]` | `"intro"` | Opening instrumental or ambient section |
| `[Verse]`, `[Verse 1]`, `[Verse 2]` | `"verse"` | Lyrical verse |
| `[Pre-Chorus]` | `"pre-chorus"` | Tension-building section before chorus |
| `[Chorus]` | `"chorus"` | Main hook / refrain |
| `[Bridge]` | `"bridge"` | Contrasting section, often philosophical core |
| `[Guitar Solo]`, `[Instrumental]` | `"instrumental"` | No vocals, pure music |
| `[Climax]` | `"climax"` | Maximum energy moment (rare — 1 per track max) |
| `[Outro]` | `"outro"` | Closing section |
| `[Spoken Intro]` | `"spoken_intro"` | Spoken word opening (EP03, EP08-09 style) |
| `[Interlude]` | `"interlude"` | Brief transitional passage between sections |
| `[Refrain]` | `"refrain"` | Recurring melodic/lyrical motif (shorter than chorus) |
| `[Spoken]` | `"spoken"` | Non-musical spoken word passage |
| `[Silence]` | `"silence"` | Intentional silence or near-silence |
| `[Finale]` | `"finale"` | Grand closing section with maximum energy |
| `[Vocal]` | `"vocal"` | Dedicated wordless vocal section (hums, cries) |

**Variant types** (append to base type when needed):
- `"outro_vocals"` — Outro with final vocal delivery
- `"outro_whisper"` — Whispered final words (EP04, EP05 pattern)

`"styles"` is an optional top-level field: additional style descriptors beyond `mood` — arrangement-level tags (e.g., "Vocals Upfront", "Minimalist Arrangement"). Used in EP08.
`"spoken_intro_duration"` is an optional top-level field: duration of the spoken intro segment in seconds. Used in EP03.

If the human provides a non-standard section name, map it to the closest type and note the original in `"notes"`.

---

## ENERGY LEVELS

| Level | When to Use |
|---|---|
| `"minimal"` | Whisper, near-silence, single instrument |
| `"low"` | Quiet, atmospheric, sparse arrangement |
| `"medium-low"` | Soft vocal entry, gentle rhythm |
| `"medium"` | Steady groove, moderate dynamics |
| `"medium-high"` | Building intensity, fuller arrangement |
| `"high"` | Full band, strong vocal delivery |
| `"explosive"` | Maximum dynamics, climax moment |
| `"building"` | Transitional — energy rising across the section |
| `"rising"` | Gradual increase within the section |
| `"chaotic"` | Unstructured, intense, dissonant |
| `"fading"` | Energy decreasing, instruments dropping out |
| `"still"` | No rhythmic pulse — spoken word, ambient |
| `"peak"` | Full energy climax, maximum dynamics (used in EP01, EP08) |
| `"theatrical"` | Dramatic, declamatory delivery; full vocal performance (EP02) |
| `"epic"` | Grand, sweeping dynamics; orchestral fullness (EP02, EP03, EP04) |
| `"slowing"` | Tempo deceleration within the section (EP03) |

---

## TIMESTAMP CONVERSION

Human provides `MM:SS` format. Convert to seconds:

```
0:33  →  33.0
1:10  →  70.0
2:05  → 125.0
4:27  → 267.0
```

**Rules:**
- All timestamps are `float` with `.0` decimal
- `"start"` of section N should be ≥ `"end"` of section N-1 (no overlaps)
- Small gaps (1-2 seconds) between sections are acceptable (breaths, transitions)
- If human provides overlapping timestamps, flag and ask for clarification

---

## LYRICS FORMATTING

**DO:**
- Join multi-line lyrics into continuous prose, separated by spaces
- Preserve key punctuation (ellipsis, exclamation, question marks)
- Include vocal performance markers only if they add meaning: `"Mmm... your metal... flesh..."` (the moan is part of the performance)

**DON'T:**
- Include stage directions: ~~"(Moaning slightly)"~~ → Remove
- Include arrangement notes in lyrics: ~~"(Music builds up)"~~ → Move to `"notes"`
- Include vocal style tags: ~~"(Vocal: Playful growl)"~~ → Move to `"notes"`
- Duplicate lyrics across sections (chorus repeats get the same text — that's fine)

---

## NOTES FIELD GUIDELINES

The `"notes"` field captures arrangement, performance, and production context. It serves the dramaturgy and motion script skills downstream.

**Good notes:**
```
"Soft Baritone, Half-Spoken, Playful. Whispered line endings, mischievous tone."
"Bass gets groovy, funky rhythm. Vocal: Breathless, Aroused but Soft."
"Slow Blues Guitar Solo. Clean, Warm, Emotional — NOT distorted."
```

**Bad notes:**
```
"This is a verse"  ← Obvious, adds nothing
"Good part"  ← Subjective, not useful for pipeline
```

**What to capture:**
- Vocal delivery style (whispered, shouted, spoken, sung)
- Arrangement changes (instruments entering/exiting, tempo shifts)
- Emotional tone shifts within the section
- Narrative significance (if relevant to the arc)

---

## MOOD KEYWORDS

Derive from human input + master.md episode description. Include 5-8 keywords that describe the track's emotional palette.

**Examples from existing episodes:**
- EP02: `["satirical", "psychedelic", "theatrical", "dark comedy", "energetic"]`
- EP03: `["joyful", "satirical", "anti-guru", "dark comedy", "upbeat", "driving groove"]`
- EP04: `["mystical", "hypnotic", "epic", "heavy", "dark"]`
- EP05: `["tender", "erotic", "playful", "comedic", "sensual", "blues", "tragic"]`

---

## INSTRUMENTS

List the key instruments audible in the track. Use descriptive names, not generic categories.

**Good:** `"clean electric guitar with chorus effect"`, `"heavy fuzz guitar"`, `"hammond organ"`
**Bad:** `"guitar"`, `"keyboards"`, `"percussion"`

If the human doesn't specify instruments, infer from:
1. Performance notes in the timestamped lyrics
2. Master.md music description for the episode
3. The series' core instrumentation (Hammond Organ, Moog, Fuzz Guitar, Bass, Drums)

---

## GENERATION STEPS

### Step 1: Read Inputs
- Read human-provided BPM, key, and timestamped lyrics
- Read master.md for episode tone, station, music style

### Step 2: Parse Sections
- Extract each section: type, start/end timestamps, lyrics, performance notes
- Convert MM:SS to seconds
- Map section headers to standardized types

### Step 3: Assign Energy Levels
- Based on performance notes, arrangement descriptions, and position in the track
- Cross-reference with master.md tone description
- Energy should follow a logical arc (intro low → verses build → chorus high → outro fading)

### Step 4: Compile Mood + Instruments
- Mood: from human keywords + master.md episode description
- Instruments: from human notes + performance annotations + master.md

### Step 5: Assemble JSON
- Follow the schema exactly
- Validate: no timestamp overlaps, all required fields present, total_duration matches last section end

### Step 6: Validate
- [ ] BPM and Key match human input exactly
- [ ] All timestamps converted correctly (MM:SS → seconds)
- [ ] No timestamp overlaps between consecutive sections
- [ ] total_duration = end of last section
- [ ] Every section with vocals has a `"lyrics"` field
- [ ] Every instrumental section omits `"lyrics"` (or has no lyrics)
- [ ] Mood keywords align with master.md episode description
- [ ] Section count matches human-provided structure
- [ ] JSON is valid (parseable)

---

## POST-GENERATION CHECKLIST

Before delivering the JSON:

- [ ] JSON parses without errors
- [ ] `tempo` and `key` match human input exactly
- [ ] `total_duration` matches the last section's `end` value
- [ ] All timestamps in seconds (not MM:SS strings)
- [ ] No overlapping sections
- [ ] Lyrics cleaned (no stage directions, no arrangement notes)
- [ ] Notes field has meaningful content (not empty, not obvious)
- [ ] Mood keywords are specific (not generic like "good" or "nice")
- [ ] Instruments are descriptive (not just "guitar")
- [ ] Section types use standardized vocabulary
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## OUTPUT

Write the JSON to: `episode-{XX}/02_music/ep{XX}_musical_metadata.json`

**No version suffix.** Musical metadata JSON is always `ep{XX}_musical_metadata.json`.

---

## WHAT HAPPENS NEXT

After the musical metadata JSON is delivered:
1. Human writes concept notes (`ep{XX}_concept_notes.md`)
2. Claude generates dramaturgy (`_skills/robotiko-dramaturgy/SKILL.md`)
3. The JSON's section timestamps become the temporal backbone of every scene

**Every weak timestamp produces misaligned scenes. Every missing note produces uninformed visual decisions. Precision here cascades forward through the entire pipeline.**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| Human forgot BPM/Key | STOP. Cannot generate without these. Ask human to run vocalremover.org. |
| Timestamps have gaps > 5 seconds | Flag the gap. Ask human if there's a missing section or if the gap is intentional. |
| Timestamps overlap | Flag the overlap. Ask human which timestamp is correct. |
| No mood keywords provided | Infer from master.md episode description. Note inference in delivery. |
| No instruments provided | Infer from performance notes + master.md. Note inference in delivery. |
| Section type unclear | Map to closest standard type. Note the original header in `"notes"`. |

---

*"The JSON is the skeleton. The music is the soul. Map the bones precisely, and the body will move."*
*— Robotiko v2.0 Pipeline*
