# SKILL: robotiko-launch-orchestrator
> **Version:** 2.0 | **Last Updated:** 2026-04-07
> **Trigger:** `"Orchestrate EP{XX} launch"`
> **Output:** `episode-{XX}/07_social_media/ep{XX}_launch_checklist.md`

---

## PURPOSE

Coordinate the complete launch sequence for a finished episode — from pre-launch verification through YouTube publication to social media rollout. This skill is the final quality gate and release coordinator, ensuring nothing is missed between "done" and "live."

---

## PREREQUISITE

> All of the following must be true before this skill executes:
> 1. Final video edit exists: `episode-{XX}/06_edit/ep{XX}_final_v{VV}.mp4`
> 2. YouTube package exists: `episode-{XX}/07_social_media/ep{XX}_youtube_package.md`
> 3. Social atomization exists: `episode-{XX}/07_social_media/ep{XX}_social_atomization.md`
>
> If any are missing, STOP. List what is missing and inform the human.

---

## MANDATORY INPUTS

| # | File | What to Extract |
|---|---|---|
| 1 | `episode-{XX}/07_social_media/ep{XX}_youtube_package.md` | Title, description, chapters, tags, thumbnail guidance |
| 2 | `episode-{XX}/07_social_media/ep{XX}_social_atomization.md` | Clip list, captions, hashtags, release schedule |
| 3 | `_management/project_metadata.json` | Episode status, previous episode status (for playlist linking) |
| 4 | `_management/master.md` | Episode context for cross-referencing narrative continuity |

---

## LAUNCH CHECKLIST

The output is a comprehensive checklist organized in launch phases:

### PHASE 1: PRE-LAUNCH VERIFICATION

```
## PRE-LAUNCH VERIFICATION
- [ ] Final video export confirmed (4K, correct aspect ratio, audio sync verified)
- [ ] YouTube package reviewed and approved
- [ ] Social atomization clips reviewed and approved
- [ ] Thumbnail created based on youtube_package.md guidance
- [ ] Episode title and description proofread (no typos, correct episode number)
- [ ] Chapter timestamps verified against actual video timeline
- [ ] Tags are within YouTube's 500 character limit
- [ ] Previous episode's end screen updated to link to this episode (if applicable)
- [ ] Playlist updated to include this episode
- [ ] project_metadata.json status updated to "ready_for_launch"
```

### PHASE 2: YOUTUBE UPLOAD

```
## YOUTUBE UPLOAD
- [ ] Video uploaded to YouTube (unlisted first for review)
- [ ] Title pasted from youtube_package.md
- [ ] Description pasted from youtube_package.md (NO timestamps)
- [ ] Tags added from youtube_package.md
- [ ] Thumbnail uploaded (NO text — episode number bottom-left only)
- [ ] End screen configured (next episode / playlist / subscribe)
- [ ] Cards added at key moments (if applicable)
- [ ] Visibility set to "Scheduled" or "Public" per launch plan
- [ ] Premiere settings configured (if using premiere)
- [ ] **Pinned comment posted** — exact text from youtube_package.md (breadcrumb for curious viewers)
```

### PHASE 3: SOCIAL MEDIA ROLLOUT

```
## SOCIAL MEDIA ROLLOUT
- [ ] Hook Clip (Clip 1) posted on launch day
  - [ ] Instagram Reels
  - [ ] TikTok
  - [ ] YouTube Shorts
- [ ] Story Clips (Clips 2-3) scheduled for Day 2-3
- [ ] Atmosphere Clips (Clips 4+) scheduled for Day 4-7
- [ ] All captions and hashtags pasted from social_atomization.md
- [ ] Link to full YouTube video in bio / link tree
- [ ] Cross-platform links verified
```

### PHASE 4: POST-LAUNCH

```
## POST-LAUNCH
- [ ] project_metadata.json status updated to "completed"
- [ ] Episode folder verified for completeness (all phases documented)
- [ ] Google Drive backup verified (all binary assets in correct episode folder)
- [ ] Naming convention validated for all episode files ("Validate file names for EP{XX}")
- [ ] Commit: "EP{XX} - Launch - Episode published and verified"
- [ ] Lessons learned noted in _memory/lessons.md (if any issues during launch)

## BANNER & ABOUT UPDATE CHECK
After each episode launch, check if a banner/About section update is due:

| After Episode | Banner Update | About Update |
|---------------|--------------|--------------|
| EP03 | Banner v2 — subtle cracks visible | Phase 2 About text |
| EP06 | Banner v3 — near-monochrome, fragmenting | Phase 3 About text (reveals "one human + AI") |
| EP08 | Banner v4 — dark with golden light in cracks | — |
| EP10 | Banner v5 — full Kintsugi, gold light from within | Phase 4 About text + open source link |

If a banner update is due after this episode's launch, flag it as an action item.
Banner specs: `_assets/banners/banner_v{N}_spec.md`
```

---

## CROSS-EPISODE CONTINUITY CHECKS

Before launching, verify these narrative continuity items:

| Check | Description |
|---|---|
| **Previous episode end screen** | Does the previous episode's end screen link to this one? |
| **Playlist order** | Is this episode in the correct position in the playlist? |
| **Description consistency** | Does the "About ROBOTIKO v2.0" section match other episodes? |
| **Character state progression** | Does the thumbnail/visual represent the correct phase? |
| **Narrative spoilers** | Does the description avoid spoiling future episodes? |

---

## LAUNCH TIMING RECOMMENDATIONS

| Strategy | When to Use |
|---|---|
| **Instant Publish** | When momentum is important (e.g., following a recent previous episode) |
| **Scheduled Premiere** | When community anticipation is high and live chat engagement is desired |
| **Unlisted + Soft Launch** | When the human wants to test with a small audience first |

Claude suggests a strategy based on the episode's position in the series, but the human has final authority on timing.

---

## EP10 SPECIAL HANDLING

EP10 is the series finale. The launch orchestration for EP10 includes additional steps:

```
## EP07-EP10 OPEN SOURCE ROLLOUT

Starting EP07, each episode's YouTube description includes an open source tease per `creator_strategy.md`:

| Episode | Description Addition |
|---------|---------------------|
| EP07 | "After Episode 10, the full production pipeline will be open source." |
| EP08 | "The pipeline behind this series will be open source after the finale." |
| EP09 | "Two episodes remain. The pipeline approaches open source." |
| EP10 | "The journey is complete. The pipeline is open source: [GitHub link]" |

**EP07 special:** Include a silent text card after music fades: "This was made by one human and AI. The full pipeline will be open source." (3 seconds, white on black).

## EP10 SPECIAL — SERIES FINALE
- [ ] All 10 episodes verified in playlist (correct order)
- [ ] Series retrospective description written (optional)
- [ ] All previous episode end screens updated to form a complete chain
- [ ] Open source release prepared:
  - [ ] Repository visibility set to PUBLIC (same day as EP10 release — no delay)
  - [ ] AUTHOR.md visible at repo root
  - [ ] CONTRIBUTING.md finalized
  - [ ] README.md updated with GitHub link and final status
  - [ ] getting-started.md completed with full tool setup
  - [ ] tools-setup.md completed with detailed per-tool setup
  - [ ] All skills reviewed for reusability
  - [ ] _management/master.md locked (final version)
  - [ ] Announcement post drafted for all platforms
- [ ] Banner v5 uploaded (full Kintsugi)
- [ ] About section updated to Phase 4 (includes open source link)
- [ ] Final project_metadata.json update: all episodes marked "completed"
- [ ] EP10 has NO pinned comment — first silence from the creator
```

---

## OUTPUT FORMAT

The output document contains:
1. **Episode Launch Header** — Episode number, title, planned launch date
2. **Pre-Launch Verification Checklist** — All items from Phase 1
3. **YouTube Upload Checklist** — All items from Phase 2
4. **Social Media Rollout Checklist** — All items from Phase 3 with schedule
5. **Post-Launch Checklist** — All items from Phase 4
6. **Cross-Episode Continuity Checks** — Table from above
7. **Launch Timing Recommendation** — Claude's suggested strategy with rationale
8. **EP10 Special Section** — Only included if this is EP10

---

## POST-GENERATION CHECKLIST

- [ ] All four launch phases are present in the checklist
- [ ] YouTube package content is correctly referenced (not duplicated — linked)
- [ ] Social atomization schedule is correctly referenced
- [ ] Cross-episode continuity checks are included
- [ ] EP10 special handling is included (if applicable)
- [ ] No broken file references in the checklist
- [ ] Launch timing recommendation is provided with rationale
- [ ] Ask yourself: **"Would Fibula approve this?"**

---

## ERROR HANDLING

| Situation | Action |
|---|---|
| YouTube package missing | STOP. Cannot orchestrate without upload metadata. |
| Social atomization missing | Proceed with YouTube-only launch, but flag that social rollout is blocked. |
| Previous episode not yet published | Flag in continuity checks. End screen linking is blocked until previous episode is live. |
| This is EP01 (first episode) | No previous episode to link to. Skip "previous episode end screen" checks. |
| This is EP10 (series finale) | Include EP10 Special section. Trigger open source release review. |

---

*"The launch is the bridge between the artist and the audience. Cross it with precision, cross it with respect."*
*— Robotiko v2.0 Pipeline*
