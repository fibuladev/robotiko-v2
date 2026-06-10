# SESSION PROMPT — GOLDEN RELEASE FIXES (P0 + P1)
> Copy-paste the block below into a NEW Claude Code session.
> Recommended session settings: Opus (or current default), **medium-high thinking effort** (this is documentation + mechanical work, not single-shot creative synthesis — per CLAUDE.md Thinking Effort Protocol).
> Claude will spawn and direct its own subagents where parallel work helps — no extra setup needed from the human.

---

## THE PROMPT (copy from here)

Read `_management/golden_release_report.md` first — it is the audit that defines this session. The repo goes **public in ~3 weeks** (around 2026-07-02, EP10 release day). Your mission: execute the P0 and P1 items from Section 8 of that report so the repo audits at 5/5 — flawless, beginner-friendly documentation is the non-negotiable goal. The system already works; this session makes it *understandable and adoptable by strangers*.

Work in the phases below. Use subagents (Agent tool) to parallelize independent documentation work and to verify your own output — e.g., one agent drafting docs/tools-setup.md while another drafts docs/skills-guide.md, and a final "fresh-eyes reviewer" agent that reads the finished docs as if it were a newcomer and reports every confusing or broken spot. Commit after each phase with the project's commit convention.

### PHASE 1 — Legal & identity (has one human decision)
1. **LICENSE decision [ASK HUMAN FIRST]:** Recommend and let the human choose: (a) MIT for everything, or (b) dual license — MIT for code/pipeline/skills + CC BY 4.0 (or CC BY-NC 4.0) for creative content (lyrics, dramaturgy, master.md universe). Explain trade-offs in 5 lines, wait for the choice, then create `LICENSE` (and `LICENSE-CONTENT` if dual) at root and reference it in README.
2. **AUTHOR.md:** Create `/AUTHOR.md` from the approved text embedded in `_management/creator_strategy.md` Section 1 — verbatim, no edits. (It only becomes visible when the repo goes public, which IS EP10 release day — so committing it now is safe and correct.)

### PHASE 2 — Repo completeness (P0)
3. **Scaffold episode-09 and episode-10** with `python scripts/create_episode.py 09` / `10` (or manually if the script needs its placeholder fix first — see Phase 4).
4. **EP09 lyrics:** The canonical EP09 lyrics are NOT in the repo. Source: the EP09 section ("Shadow Debugging") preserved at the end of `robotiko-v2-base files/project/lyrics.txt` (raw, from the creator's desktop file). Create `episode-09/01_lyrics/ep09_lyrics_v01.md` in the standard lyrics format (header block + sections). Mark timestamps as TBD — the human adds them at the musical-metadata stage.
5. **Character reference images [HUMAN TASK — prepare, don't generate]:** `ref_mentor_master.png` and `ref_robochica_master.png` are referenced everywhere but missing from `_assets/cast/`. Do BOTH of: (a) write the two ready-to-use generation prompts (with mandatory suffix, per lessons.md eye rules and PROMPT FORMULA) into `_assets/cast/reference_image_prompts.md` so the human can generate them in Nano Banana, and (b) ask the human whether existing images from past production should simply be copied/renamed into place instead. Update `character_profiles.json` paths only when files actually exist.
6. **Status single-source-of-truth:** `master.md` Section 8 tracker and `CLAUDE.md` "Current Phase: EP02 in progress" are stale. Replace both with a one-line pointer to `project_metadata.json` (the real tracker) + refresh project_metadata.json itself to current state (EP06 CapCut edit, EP07 CapCut edit, EP08 motion script approved/in video gen, EP09-10 scaffolded). Do NOT rewrite master.md's creative content — only the status table.
7. **Personal tools sweep:** `_tools/*.ps1` (~20 disk/system maintenance scripts) are unrelated to the pipeline. Move them OUT of the repo tree to `C:\Users\canby\Desktop\local-tools\` (create it), leaving only `_tools/mcp-gdrive/`. Confirm `.gitignore` stays consistent.
8. **Secrets/PII sweep:** Run a final scan over all tracked files for emails, tokens, absolute local paths (C:\Users\...), private names beyond the intended creator identity, and non-English private notes. Report findings before changing anything.

### PHASE 3 — Documentation to golden (P1, the heart of this session)
9. **docs/ completion** (parallelize with subagents, then unify voice):
   - `docs/getting-started.md` → full walkthrough: prerequisites with links, clone-to-first-episode in numbered steps, expected costs (credits/subscriptions), FAQ.
   - `docs/skills-guide.md` → what skills are, anatomy of a SKILL.md, full table of all 10 skills with triggers/inputs/outputs, one worked example (trigger → deliverable).
   - `docs/tools-setup.md` → per-tool setup: Claude Code (+hooks), Suno, Nano Banana, Kling/Veo/Seedance, CapCut (LUT/grain/letterbox protocol), Google Drive MCP (`_tools/mcp-gdrive/README.md` cross-link).
   - NEW `docs/anatomy-of-an-episode.md` → trace EP07 end-to-end: lyrics → metadata JSON → concept → dramaturgy → visual prompts → images → motion script → video → CapCut → YouTube package, with 1-2 real excerpts per stage and links to the actual files. This is the repo's showcase artifact.
10. **CONTRIBUTING.md full version:** how to fork the method for your own universe, what is canon-locked (master.md, suffixes, character profiles), PR process, code of conduct (symbiosis philosophy).
11. **architecture.md v2.1:** purge AWS S3 (storage = Google Drive + custom MCP), current toolchain (Kling 3.0 Elements/Omni, Seedance 1.0, Veo), Claude Code hooks, tests, the two human gates. Keep it diagram-first.
12. **CHANGELOG.md:** bring current (entries stop at Feb 2026) — add production-era milestones per episode stage, and a prepared-but-dated-TBD `1.0.0` open-source release entry.

### PHASE 4 — Engineering polish (P1)
13. **CI:** create `.github/workflows/naming_check.yml` running `tests/naming_check.py` + `tests/pipeline_integrity.py` + `tests/visual_prompt_validator.py` on push/PR. Remove or satisfy every stale "planned" reference to it in architecture.md/naming_convention.md.
14. **create_episode.py:** fix placeholder substitution (`{EPISODE_NUMBER}` etc. in copied templates). Add a `--dry-run` flag. Test by scaffolding episode-10 with it if not already done.
15. **Run everything:** all three test scripts must pass on the final tree; fix violations they surface (report any false positives instead of weakening the tests silently).

### PHASE 5 — Verification & closure
16. Spawn a **fresh-eyes reviewer subagent**: "You are a developer who has never seen this repo. Starting from README.md only, try to understand what this is, how to run one episode, and where everything lives. Report every dead link, contradiction, missing step, or confusing sentence." Fix what it finds.
17. Re-sync the external base-files mirror (`robotiko-v2-base files/project/` — gitignored) for any file you changed that exists there (CLAUDE.md, master.md, project_metadata.json, architecture.md, getting-started.md, skills-guide.md, tools-setup.md, todo.md, lessons.md). Remind the human to re-upload changed files to claude.ai Projects.
18. Update `_memory/todo.md` with a session summary; update the P0/P1 checklists inside `_management/golden_release_report.md` (mark done items); grouped commits per convention; push.

**Checkpoints requiring the human:** license choice (Phase 1), reference-image decision (Phase 2 item 5), secrets-sweep findings review (Phase 2 item 8), final review before push.
**Out of scope for this session:** EP01 retroactive creative chain (separate creative session — needs max effort), banner specs (creative), EP09/EP10 production itself, HN/Reddit launch execution.

---

## END OF PROMPT
