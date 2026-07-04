# Security Policy

## Scope, honestly stated

This repository is, by volume, markdown documentation and standard-library
Python (`tests/`, `scripts/`). There is no server, no database, no user
accounts, and no network-facing service running as part of the pipeline
itself. Most of what lives here cannot leak credentials because it doesn't
hold any.

The one credentialed surface is the custom Google Drive MCP server at
[`_tools/mcp-gdrive/`](_tools/mcp-gdrive/), which archives binary assets
(audio, images, video) to a single Google Drive account. Specifics, verified
against the code:

- **Auth model**: OAuth2, user-driven consent flow (`_tools/mcp-gdrive/src/auth.js`).
  There is no service account and no embedded secret in this repo — the
  `gcp-oauth.keys.json` client file and the resulting `tokens.json` are
  expected to live outside the repo, at `~/.config/robotiko-mcp-gdrive/` (or a
  path set via the `GDRIVE_OAUTH_PATH` / `GDRIVE_TOKEN_PATH` environment
  variables). Neither path is committed, and neither should ever be.
- **OAuth scope**: `https://www.googleapis.com/auth/drive.file` only — the
  narrowest Drive scope Google offers. It grants access only to files the
  app itself creates or that the user explicitly opens with it; it cannot
  browse or read the rest of a Google Drive account. This is a hard
  constraint declared in `auth.js`'s `SCOPES` array — if you ever see a PR
  widen it, that is a security regression, not a feature.
- **Token storage**: local disk only, on the machine that runs the MCP
  server. Tokens are never transmitted anywhere but Google's OAuth endpoints
  and are never logged or committed.

If you fork this project and wire up your own Google Cloud OAuth client, the
same scope discipline applies to your credentials, not this repo's.

## What is NOT a vulnerability here

- Naming-convention or pipeline-validator false positives/negatives — file
  those as regular bugs (see [SUPPORT.md](SUPPORT.md)), not as security
  reports.
- Content questions about the ROBOTIKO universe, lyrics, or visual prompts —
  not a security concern.
- The GitHub Actions workflows (`.github/workflows/`) run standard-library
  Python only and pin both the Python version and each Action to an
  immutable commit SHA (see the comments in
  `.github/workflows/validation_suite.yml`) specifically to reduce
  supply-chain surface. A dependency-pinning suggestion is welcome as a
  normal issue or PR, not a private report.

## Reporting a vulnerability

If you find a genuine credential-handling, token-leak, or scope-escalation
issue in `_tools/mcp-gdrive/`, please use
**[GitHub Security Advisories](https://github.com/fibuladev/robotiko-v2/security/advisories/new)**
for private reporting rather than a public issue. This lets us discuss and
fix it before it's public.

**Response target — stated plainly**: this is a solo-maintained project, and
the maintainer is frequently in active production on episodes (shooting,
editing, generating). Response is best-effort, aimed at within a week, not
guaranteed on any fixed SLA. There is no security team behind this — there
is one person. If you don't hear back in two weeks, a follow-up comment on
the advisory is welcome and won't be seen as impatient.

## Supported versions

This project does not ship versioned releases in the traditional sense — it
is a single, continuously developed `main` branch backing an active film
production. Security fixes land on `main`; there are no older maintained
branches.
