# ADR 0004 — Triage policy: fix / whitelist / refine

- **Status:** Accepted (2026-06-26)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Validation Backbone

## Context

Running the suite across all episodes turned up reds in EP02–EP08. **One bug is
a class — but a red test is not always a bug.** Treating every red as a defect
to "fix" would have corrupted correct files; treating every red as noise to
silence would have hidden real continuity errors. The reds were three different
things, and the response had to match the cause.

## Decision

Triage every failure into exactly one of three actions, and never loosen a check
without a both-directions proof (still catches a real bug · ignores the intended
case):

**FIX — a real continuity bug.** EP04/EP05 attached the pristine reference to
Phase-2 (damaged) scenes. Corrected the reference fields to `android_damaged.png`
— text only; the shipped images are kept.

**WHITELIST — an intentional, documented non-Robotiko subject.** A forbidden
keyword that legitimately describes something other than Robotiko: EP08 S22's
pristine dream-copies, EP06's pristine conformist *foil* android. Encoded as
`robotiko.phase_keyword_whitelist` in `character_profiles.json`, **pinned to
specific scenes + keywords** — never a blanket "ignore this word in this
episode", so a pristine-Robotiko slip anywhere else still fires. Ref-integrity is
deliberately *not* whitelisted, so the reliable gate still polices these scenes.

**REFINE — the check over-fires.** Tighten the check so it judges Robotiko, not
the scenery:

- *Subject-guard:* a forbidden word bound to a non-Robotiko noun ("pristine
  shelves", "translucent data", "iron walls becoming translucent") or negated
  ("not pristine") no longer fires. Body words are deliberately excluded from the
  neutralizer list, so "pristine chest plate" still fails.
- *Phase granularity:* Phase 1 is not uniform. EP01 is pristine, but canon says
  EP02–EP03 already carry battle damage, so "cracked"/"rusted" are correct there.
  The forbidden set is keyed per-episode; Phase-3 markers stay forbidden until
  the body reaches Phase 3.
- *Honest labels:* the scene parser preserves `a`/`b` keyframe-pair suffixes
  (S03a/S03b), so paired sub-scenes are not mistaken for duplicate flags.

## Consequences

- The suite is green for the right reason: real bugs fixed, intentional cases
  documented, over-fires tightened.
- The text keyword check remains a heuristic (it cannot fully attribute an
  adjective to a subject in free prose); ref-integrity ([ADR 0002](0002-ref-integrity-parses-reference-metadata.md))
  is the authoritative gate, and the honest split of what is guaranteed vs.
  heuristic vs. human-gated is recorded in the Invariant Coverage Matrix.
- Whitelist entries are narrow and reasoned; widening one is a deliberate,
  reviewable act.
