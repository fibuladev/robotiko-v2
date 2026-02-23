# Tests
> **Status:** Skeleton — Full implementation planned for EP03 production phase.

---

## Available Tests

| Script | Purpose | Status |
|---|---|---|
| `naming_check.py` | Validates file names against `naming_convention.md` | 🔄 Skeleton |
| `pipeline_integrity_check.py` | Ensures no pipeline steps were skipped | 🔄 Skeleton |

---

## Usage

```bash
# Validate naming convention for episode 02
python tests/naming_check.py --episode 02

# Check pipeline integrity for episode 02
python tests/pipeline_integrity_check.py --episode 02
```

---

## Planned Tests

- `skill_output_validator.py` — Validates skill outputs against Master rules (visual suffix present, character state correct, etc.)
- `bible_compliance_check.py` — Cross-checks dramaturgy against Master for narrative consistency

---

## GitHub Actions Integration (Planned)

Naming check will run automatically on every push via `.github/workflows/naming_check.yml`.