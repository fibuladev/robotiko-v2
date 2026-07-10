# ADR 0006 — Scoped prompt hygiene: ASCII only where it's model-facing

- **Status:** Accepted (2026-06-26)
- **Deciders:** Fibula (director), Claude (pipeline)
- **Context tag:** EP09 Validation Backbone

## Context

Two of our own rules pointed in opposite directions:

- **master.md and the cultural-attribution canon** *require* the sanctioned
  Turkish attribution — the names (Yunus Emre, Hacı Bektaş Veli) and the tradition
  labels ("Turkish wisdom tradition", "Turkish folk poetry"). This is the soul of
  the project; it is correct and mandatory in the canon and the internal direction
  notes.
- **lessons.md / production reality** *requires* model-facing prompt strings to be
  plain-English ASCII — non-ASCII characters and attribution decoration in an
  image/video prompt tokenize unpredictably and bleed cultural labels into the
  generated frame.

A naïve "no non-ASCII anywhere" lint would punish the canon. A "do nothing" stance
leaves real leaks (EP03's prompts carried Turkish characters; em-dashes were
everywhere). The contradiction is only apparent — it dissolves once you scope by
*audience*: who reads the string.

## Decision

Scope the rule by audience, not by file:

- **Canon and direction notes may carry the sanctioned attribution.** master.md,
  the philosophy docs, and the internal direction notes (concept notes, dramaturgy,
  musical metadata) are **out of scope by design**. The lint never opens them — and
  inside a visual-prompt file, the Dramaturgy Reference / Composition Notes lines
  are out of scope too.
- **Only the model-facing prompt strings must be plain-English ASCII.** A scoped
  lint (`tests/prompt_hygiene_lint.py`) reads ONLY the `Text Prompt` blockquotes in
  `episode-*/04_visuals/ep*_visual_prompts_v*.md` and the `Motion Prompt`
  blockquotes in `episode-*/05_video/ep*_motion_script_v*.md`, and flags non-ASCII
  characters and tradition-label decoration there. A small allowlist holds any
  future sanctioned exception.
- A `--fix` mode ASCII-normalizes only those prompt blockquotes (em-dash → hyphen,
  Turkish letters transliterated), leaving every out-of-scope line untouched. It
  was run once over the shipped files.
- Wired into `tests/run_all.py` and therefore into CI.

## Consequences

- The canon is never punished: the proving meta-tests assert the lint *catches* a
  tradition label / non-ASCII char in a real prompt string, *and ignores* the same
  decoration when it lives in a Dramaturgy line or any out-of-scope file. The
  scope-exclusion test proves master.md exists yet is not in the lint's file list.
- The cultural-attribution row in the Invariant Coverage Matrix moves from ⚪ Gap to
  🟢 Machine — but only for prompt strings; the canon stays human-authored.
- The lint is intentionally narrow. If a third prompt-bearing surface appears, it
  must be added to `IN_SCOPE` explicitly — silence is not coverage.

**Note on figure framing (2026-07-10):** The Context section above welds the
sanctioned Turkish-attribution label directly onto individual names
("the names (Yunus Emre, Hacı Bektaş Veli)"). The mechanism this ADR decides
(scope the lint by audience) is unaffected, but the wording should be read as:
the sanctioned attribution is the tradition LABELS ("Turkish wisdom tradition",
"Turkish folk poetry") plus anchor names such as Yunus Emre and Hacı Bektaş
Veli — thinkers who lived and taught in Anatolia — framed geographically
rather than by a flat ethnic label on the individual. This note does not
change the decision; it clarifies the framing per the canon's cultural-
attribution rule (Golden Rule 9).
