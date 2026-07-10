# SKILL: robotiko-reels-atomizer
> **Version:** 3.0
> **Trigger:** `"Atomize EP{XX} for social"`
> **Output:** `episode-{XX}/07_social_media/ep{XX}_social_atomization.md`

---

## PURPOSE

Break a finished episode into short-form social media content (Reels, Shorts, Stories). Each "atom" is a self-contained clip — 7 to 60 seconds — designed to capture attention, convey a fragment of the episode's essence, and drive viewers to the full video.

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
- Be between **7 and 60 seconds** — Hook Clips target 7-15s loop-friendly length (confirmed Shorts strategy); Story/Atmosphere clips may run 20-60s
- Contain at least one visual peak and one lyrical hook
- Feel complete — not cut mid-phrase or mid-thought

### Step 3: Assign Clip Types

| Type | Duration | Purpose | Best For |
|---|---|---|---|
| **Hook Clip** | 7-15s | Maximum impact, loop-friendly, designed to stop scrolling | Chorus moments, visual climaxes, iconic lyrics |
| **Story Clip** | 20-40s | A mini-narrative with setup and payoff | Verse + chorus pairs, scene transitions |
| **Atmosphere Clip** | 30-60s | Mood piece, lets the aesthetic breathe | Instrumental sections, environmental sequences |
| **Behind the Scenes** | 15-30s | Process reveal (optional, human-driven) | Prompt → image → video comparisons |

**Rule:** Every clip must contain narrative content. Pure aesthetic clips with no story function are not used. The ROBOTIKO brand tells stories — even atmosphere clips must carry meaning, not just texture.

### Step 4: Write Caption and Hashtags per Clip

**Caption rules:**
- Maximum 150 characters for the primary hook line
- Include a key lyric quote or philosophical fragment
- End with a CTA: link to full video or "Link in bio"
- Tone must match the episode's station — no generic hype language

**Platform-specific caption tone:**

| Platform | Tone | Example |
|----------|------|---------|
| **Instagram Reels** | Aesthetic, poetic, contemplative. Let the visual do the heavy lifting. | "Two halves of one whole apple. 🎬 Full episode — link in bio." |
| **YouTube Shorts** | Descriptive, discoverability-focused. Include series context. | "ROBOTIKO v2.0 EP01 — The journey begins. Full episode on this channel." |

**Rule:** Write BOTH captions for each clip — one per platform. Do not use a single generic caption across platforms.

**Hashtag strategy:**
- 5-10 hashtags per clip
- Mix of: project tags (`#robotiko`, `#robotikov2`), film tags (`#aifilm`, `#aiscifi`, `#cinematicai`, `#scifi`), craft tags (`#aifilmmaking`, `#aiart`)
- **#aiart used from EP01** — AI transparency from day one

---

## OUTPUT FORMAT

### Clip Table
| Clip # | Type | Timestamp | Duration | Visual Peak | Lyric Hook | Platform Priority |
|---|---|---|---|---|---|---|
| 1 | Hook Clip | 1:15 - 1:35 | 20s | [Scene S12 — description] | "Key lyric here" | Reels, Shorts |
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
- **Caption (Instagram):** [Ready-to-paste caption — aesthetic/poetic tone]
- **Caption (YouTube Shorts):** [Ready-to-paste caption — descriptive/discoverable tone]
- **Hashtags:** [Ready-to-paste hashtag string — include #aiart]
- **Platform Priority:** [Which platforms this clip works best on]
- **Vertical Framing:** [Technique name — Cinematic Canvas / Pan & Scan / Split-Screen / Analog Typography]
- **Related Video:** Link to full episode via YouTube Studio "Related Video"
- **CapCut Steps:** [Numbered steps specific to this clip — timestamps, technique-specific instructions]
```

### Cinematic Canvas Template Guide
Include a one-time CapCut setup guide in every atomization output. This goes after the clip detail blocks:

```
## CAPCUT EXECUTION GUIDE

### One-Time Template Setup
1. CapCut Desktop → New Project → canvas 9:16 (1080×1920)
2. Background: pure black (#000000)
3. Import any placeholder clip → Scale to ~60% so full 16:9 frame fits with black bars above/below
4. Center the video so bars are equal
5. Text → "ROBOTIKO v2.0" → serif font, #D4A76A amber, ~36pt → top-left of upper bar
6. Text → "8 → ∞" → same font/color → bottom-right of lower bar
7. Optional: Effects → film grain at 10-15% opacity
8. Save As → "ROBOTIKO_Cinematic_Canvas_Template"

### Per-Clip Workflow
1. Duplicate template project
2. Replace video with episode final video
3. Trim to clip timestamps (Ctrl+B to split)
4. Adjust text element durations to match trimmed clip
5. Export → 1080×1920, 30fps, MP4
```

### Release Schedule Suggestion

Aligned with the project's weekly release rhythm (target ~Tuesday):

- **Tuesday (Release day):** Hook Clip → maximum reach. Post alongside YouTube premiere.
- **Thursday (+2 days):** Story Clip + detail still image (different visual angle from release day)
- **Sunday (+5 days):** Atmosphere Clip as IG Story teaser for next week's episode
- **Ongoing:** Behind the Scenes (if available) → community building

### Alternative: Narrative Arc Ordering
For episodes with strong narrative progression (e.g., EP02's arrogance → damage arc), clips can follow the episode's emotional arc instead of type-based ordering:

| Timing | Narrative Function | Example |
|--------|-------------------|---------|
| T+1h (launch day) | Peak state — the hook | Arrogance at its highest |
| T+24h | Impact — the turn | First irreversible damage |
| T+48h | Depth — the world | Context that deepens meaning |
| T+5d | Warmth — re-engagement | The human moment, drives return traffic |

Use narrative ordering when the episode has a clear arc. Use type-based ordering (Hook → Story → Atmosphere) when the episode is more thematic than sequential.

**Posting times (CET/Bratislava):**
- Instagram: 18:00-19:00
- YouTube Shorts: Same day as Reels, no specific time

**Weekly rhythm target:** ~65 minutes total effort per week

---

## ASPECT RATIO CONSIDERATIONS

YouTube episodes are 16:9. Social platforms prefer 9:16 (vertical). Default vertical treatment is Technique 1 (Cinematic Canvas — no crop). See VERTICAL FRAMING TECHNIQUES below.

---

## VERTICAL FRAMING TECHNIQUES

16:9 episodes converted to 9:16 vertical format use these 4 techniques instead of simple cropping.

### Technique 1: The Cinematic Canvas (Default)
Place the wide 16:9 frame in the center of a 9:16 canvas. Do NOT crop to fill. Use the top and bottom black bars as branded creative zones.

**Fixed Template (all clips):**
- **Top bar:** "ROBOTIKO v2.0" — 70s serif font, Kodachrome amber, left-aligned
- **Bottom bar:** "8 → ∞" symbol — same font, right-aligned, with analog film texture (light leaks, grain) as background fill
- **Canvas background:** Pure black with subtle film grain overlay

This is the DEFAULT technique. Use for most clips. Executed in CapCut.

**CapCut Guide — Cinematic Canvas (one-time template setup):**

1. **Create project:** Open CapCut Desktop → New Project → set canvas to **9:16 (1080×1920)**
2. **Set background:** Canvas background = pure black (#000000)
3. **Import clip:** Drag the episode clip segment onto the timeline
4. **Resize video:** Select the clip on canvas → Scale down until the full 16:9 frame fits inside the 9:16 canvas with black bars visible above and below. The video should NOT fill the screen — the bars are intentional. Approximately 60% scale works.
5. **Center the video:** Position the video vertically so the black bars above and below are roughly equal
6. **Add top bar text:** Text → Add Text → type "ROBOTIKO v2.0" → Font: closest available serif in CapCut (search "serif" or "classic" — exact font varies by version) → Color: Kodachrome amber (#D4A76A) → Size: ~36pt → Position: top-left of the upper black bar → Duration: match full clip length
7. **Add bottom bar text:** Text → Add Text → type "8 → ∞" → Same font and color → Position: bottom-right of the lower black bar → Duration: match full clip length. CapCut's kerning and alignment are limited — manual positioning is fine. Slight imperfection fits the analog aesthetic.
8. **Add film grain overlay (optional):** Overlay → search "film grain" or "noise" in CapCut effects → apply at 10-15% opacity over the full canvas → this adds analog texture to the black bars
9. **Export as template:** Save project as a template or duplicate it for each new clip — only the video clip on the timeline needs to change

**Reuse for each clip:** Duplicate the project, swap the video segment on the timeline, adjust duration. All text and overlay stays the same.

**Important:** Do NOT use Pan & Scan for clips that contain multiple scene cuts (different compositions, zoom levels, or camera angles within one clip). Pan & Scan only works on a single continuous wide shot where the subject stays in a predictable position. For multi-cut clips, always use Cinematic Canvas.

### Technique 2: Pan & Scan
Animate a 9:16 "viewfinder" within the wide shot using CapCut keyframe animation. Start with a wide environmental view, then slowly pan/zoom the vertical frame to focus on a character's face or key detail. Conveys scale while keeping the subject present.

Best for: Single continuous wide shots with both environmental context AND character detail. NOT suitable for multi-cut montage clips.

**CapCut Guide — Pan & Scan:**

1. **Create project:** CapCut Desktop → New Project → canvas **9:16 (1080×1920)**
2. **Import clip:** Drag the single wide shot onto the timeline
3. **Scale up:** Select clip → Scale up until the video is much larger than the canvas (the 9:16 frame becomes a "window" into the wide shot). Approximately 170-200% scale.
4. **Set start position:** Move playhead to clip start → click the diamond (◆) keyframe icon next to Position → drag the video so the desired starting area is visible (e.g., wide landscape, left side of scene)
5. **Set end position:** Move playhead to clip end → drag the video so the desired ending area is visible (e.g., character face, right side of scene) → CapCut auto-creates the second keyframe
6. **Preview:** Play back. The 9:16 frame should slowly glide across the wide shot over the clip's duration
7. **Adjust speed curve (optional):** Right-click between keyframes → select "Ease In/Out" for smoother, more cinematic movement instead of linear

**Important:** This technique requires a SINGLE continuous shot — no cuts, no scene changes. If the subject moves unpredictably or the shot contains edits, the pan will miss the subject.

### Technique 3: Symbiosis Split-Screen
Vertical split: top half shows a close-up (face, detail), bottom half shows the wide environment. Reflects the "two halves of one whole" philosophy.

Best for: Scenes where both scale and emotion matter simultaneously. Use sparingly — max 1 per episode's clip set.

**CapCut Guide — Split-Screen:**

1. **Create project:** CapCut Desktop → New Project → canvas **9:16 (1080×1920)**
2. **Import two clips:** Place both on the timeline (different tracks — main track + overlay track)
3. **Top half (close-up):** Select the close-up clip → Scale and crop to fill only the top half of the 9:16 canvas → Position Y: upper half
4. **Bottom half (wide shot):** Select the wide shot clip → Scale and crop to fill only the bottom half → Position Y: lower half
5. **Add divider line (optional):** Use a thin white or amber horizontal line between the two halves (Overlay → shape or text element "—" stretched across)
6. **Sync audio:** Mute the overlay track — audio comes from the main track only

### Technique 4: Analog Typography
Use vertical empty spaces (top/bottom bars of Cinematic Canvas, or full 9:16 overlay) for bold 70s progressive rock-style titles. Frames the clip as a "digital art gallery" piece.

Best for: Opening or closing seconds of a clip. Can be combined with Technique 1.

**CapCut Guide — Analog Typography:**

1. Start with a **Cinematic Canvas** setup (steps 1-5 above)
2. **Add title text:** Text → Add Text → type lyric fragment or episode title → Font: bold 70s serif → Color: Kodachrome amber → Size: 48-72pt (larger than the standard bar text)
3. **Position:** Center it in the upper or lower black bar, or overlay on the video itself with semi-transparent background
4. **Animate:** Add "Fade In" text animation (0.5s) at clip start, "Fade Out" (0.5s) at clip end
5. **Duration:** Show the title for the first 3-5 seconds or last 3-5 seconds of the clip, not the full duration

**Rule:** Every clip must specify which technique(s) it uses in its detail block. Default is Technique 1 (Cinematic Canvas). All vertical framing is executed in CapCut (single workflow).

---

## RELATED VIDEO BRIDGE

After uploading each Short to YouTube, use YouTube Studio's "Related Video" feature to link the Short directly to the full episode. This creates a direct funnel from Shorts Feed → Episode.

**Checklist per Short:**
- [ ] Short uploaded to YouTube
- [ ] YouTube Studio → Short → Details → "Related Video" → select full episode
- [ ] Verify the link appears on the Short's player page

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
- [ ] Clip durations are within 7-60 second range (Hook Clips 7-15s, Story/Atmosphere 20-60s)
- [ ] Two platform-specific captions written per clip (IG, Shorts)
- [ ] Captions are under 150 characters and include a lyric or philosophical hook
- [ ] Hashtags are relevant and within platform limits
- [ ] #aiart included in hashtags
- [ ] 9:16 crop safety is noted for each clip
- [ ] Release schedule suggestion is included
- [ ] No clip relies on context from the full video to make sense
- [ ] Related Video bridge configured for every Short
- [ ] Vertical framing technique specified for each clip
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
