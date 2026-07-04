# Frozen GOOD Fixture — Doc Reference Integrity

> Do not "fix" this file. It is a frozen snapshot that MUST PASS the
> doc-reference existence check with zero findings.

Every backtick-quoted repo path here resolves on disk:
`tests/run_all.py`, `_management/architecture.md`, and the `docs/` directory.

Historical note tolerated by design: the `naming_check_hook.py` PostToolUse hook
was removed 2026-07-04 — this line names the removed hook but is clearly historical,
so neither the existence check nor the hook-rot guard may fire on it.

Gitignored-by-design paths are tolerated too: a `_private/audit_2026-07/report.md`
reference (never committed) and a render output at `episode-07/06_edit/note.mp4`
(gitignored binary) must not be flagged.

An intentional anti-example, silenced only by the inline marker: the
`tests/legacy_gone_tool.py` path is a dead reference. <!-- doc-ref: ignore -->
