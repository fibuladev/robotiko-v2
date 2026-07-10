# 📚 MANAGEMENT / PROJECT CANON

This folder contains the **source of truth** for the Robotiko universe.

## Files

- `master.md` - Universe Canon: story arc, characters, stations, episodic structure (absolute source of truth)
- `pipeline_rules.md` - Production workflow (Lyrics → Audio → Visual → Video → Edit), quality gates, checkpoints
- `naming_convention.md` - File naming standards
- `architecture.md` - Technical stack & data flow
- `project_metadata.json` - Project settings, toolchain, episode status (single source of truth for status)
- `youtube_metadata_standards.md` - YouTube metadata standards (titles, tags, description, hashtags)
- `dissonance_registry.md` - Ledger of sanctioned `[DISSONANCE]` shots (visual deliberately refuses the music's energy); human-readable side of the `energy_motion_check.py` exemption
- `approvals.json` - Machine-readable gate ledger: one sha256-pinned record per human approval (gates 1, 1R, 2); consumed by `pipeline_integrity.py`
- `invariant_coverage_matrix.md` - Honesty ledger: every invariant tiered as Machine / Heuristic / Human / Gap
- `case_study_validation_backbone.md` - How the validation backbone was built and what it caught
- `adr/` - Architecture Decision Records (0001-0013)

## Usage

All creative decisions MUST reference these files. Claude skills read from here to ensure consistency. When in doubt, `master.md` wins.
