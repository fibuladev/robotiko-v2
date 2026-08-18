# Frozen BAD Fixture — Markdown Doc Links

> Do not "fix" this file. It is a frozen snapshot that MUST FAIL the
> markdown-link existence check. See `tests/doc_reference_check.py`.

This doc links to a file that does not exist on disk:
[X](nonexistent.md) — a dead link that must be caught.

For contrast, the real path resolves and must NOT be the reason it fails:
[run_all](tests/run_all.py).