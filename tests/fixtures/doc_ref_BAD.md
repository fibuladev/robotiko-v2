# Frozen BAD Fixture — Doc Reference Integrity

> Do not "fix" this file. It is a frozen snapshot that MUST FAIL the
> doc-reference existence check. See `tests/doc_reference_check.py`.

This doc points at a validator that does not exist on disk:
`tests/does_not_exist_xyz.py` — a dead reference that must be caught.

For contrast, this real path resolves and must NOT be the reason it fails:
`tests/run_all.py`.
