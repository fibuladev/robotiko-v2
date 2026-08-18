# Frozen GOOD Fixture — Markdown Doc Links

> Do not "fix" this file. It is a frozen snapshot that MUST PASS the
> markdown-link existence check with zero findings.

Every markdown link here resolves on disk:

- [run_all](tests/run_all.py) — a plain repo-root-relative link.
- [anatomy](docs/anatomy-of-an-episode.md#scenes) — the #anchor fragment is
  stripped before the path is checked.
- [README](../README.md) — a ../-relative link resolving to the repo root.

Gitignored-by-design targets are tolerated too: a `_private/audit_2026-07/report.md`
reference (never committed) and a render output at
[note](episode-07/06_edit/note.mp4) must not be flagged.