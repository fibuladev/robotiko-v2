"""
Robotiko v2.0 — Forbidden-Terms Gate (religion/order/sect/scripture names)

The editorial stance (lessons.md, CATEGORY: CREATIVE & NARRATIVE) is that ROBOTIKO
renders spirituality as universal, lived, earned experience — never dressed in a
named tradition's costume. Two real violations slipped past every other gate before
this one existed:

  * `_management/master.md` once carried a "Sufi lodges ... Halvetî ... etvârnâme"
    block — a named-tradition block in the Universe Bible itself.
  * `episode-08/02_music/ep08_musical_metadata.json` once carried "The Sufi image..."
    inside a JSON string value.

Both are the same failure mode: a named religion/order/sect/scripture term leaking
into PUBLIC PROSE (canon docs, direction notes, musical metadata) — not the model-
facing prompt strings `prompt_hygiene_lint.py` already scopes, and not the sanctioned
Turkish attribution (Yunus Emre, "Turkish wisdom tradition") that canon is allowed to
keep. This gate polices a narrower, harder line: specific tradition/sect/scripture
NAMES, banned everywhere in public prose, with a pinned, narrow allowlist for the one
sanctioned exception — a rule that MENTIONS the banned word as its own subject, rather
than USING it.

SCOPE (tracked files only — `git ls-files`, so gitignored/untracked never enter):
  * every top-level `*.md` (repo root only, not recursive)
  * `_management/`, `docs/`, `_memory/`, `_skills/`, `_templates/`, `_assets/`,
    `.github/` — every `*.md`, recursive (incl. `_management/adr/`)
  * `episode-*/03_direction/*.md`
  * `episode-*/02_music/*_musical_metadata.json` (scanned as text — a forbidden term
    in a JSON string value appears verbatim on some line, so a text scan finds it
    without a JSON parse)

EXCLUDED: `tests/fixtures/**` (intentional bad content lives there on purpose),
`episode-*/01_lyrics/**` (lyric sheets are untouchable shipped artifacts — never
policed), and anything git does not track (gitignored or untracked).

MATCHING: case-insensitive, diacritic-insensitive (NFKD-normalized before matching,
so "Halvetî", "dergâh", "etvârnâme" all match their plain-ASCII root form), word-ish
boundary (`(?<![a-z])term(?![a-z])` on the normalized line — no partial-word hits
inside a longer unrelated word).

ALLOWLIST: a narrow, pinned, in-file mapping of exact file -> exact substring a line
must contain to be exempted (the whole line is exempted, since the pinned substring
IS the line that names the term as the rule's object). Anything else, anywhere, is a
FAIL. See ALLOWLIST below.

Usage:
    python tests/forbidden_terms_gate.py --full        # scan every in-scope tracked file
    python tests/forbidden_terms_gate.py --file <path> # scan one file (scope-agnostic)

Dependencies: standard library only.

Status: IMPLEMENTED v1.0
"""

import os
import re
import sys
import argparse
import subprocess
import unicodedata

# ─────────────────────────────────────────────
# FORBIDDEN TERMS — the R1 class: religion/order/sect/scripture NAMES.
# Deliberately narrow: broad adjectives ("sacred", "divine", "mystical", "dervish",
# "zen") stay OUT — they have sanctioned in-fiction/satire uses and remain
# human-judged. Listed as plain-ASCII root forms; diacritic normalization (below)
# makes each root also match its accented spellings (Halvetî, dergâh, etvârnâme, ...).
# ─────────────────────────────────────────────

FORBIDDEN_TERMS = [
    "sufi",
    "halveti",
    "etvarname",
    "tarikat",
    "dergah",
    "naqshbandi",
    "bektashi",
    "mevlevi",
    "sunni",
    "alevi",
    "islamic",
    "quran",
    "koran",
    "eschatology",
    "eschatological",
    "vedanta",
    "atman",
    "brahman",
    "sunyata",
]

_TERM_PATTERNS = {
    term: re.compile(rf"(?<![a-z]){re.escape(term)}(?![a-z])")
    for term in FORBIDDEN_TERMS
}

# ─────────────────────────────────────────────
# ALLOWLIST — narrow, pinned, in-file. file (repo-relative, forward slashes) ->
# list of {"substring": exact text a line must contain, "reason": why}. A hit is
# exempted only if its LINE contains the pinned substring verbatim — not "the file
# contains this term somewhere", not a filename match. Seeded with exactly one entry:
# the lessons.md rule line that names "Sufi" as the rule's OBJECT (the ban's own
# documentation), never as a used tradition label.
# ─────────────────────────────────────────────

ALLOWLIST = {
    "_memory/lessons.md": [
        {
            "substring": 'The word **"Sufi" is FORBIDDEN** anywhere in the project',
            "reason": "Rule text names the banned word as the rule's own object "
                      "(mention, not use) — this line documents and enforces the "
                      "ban on \"Sufi\"; it does not use the word as a tradition "
                      "label the way the two audit-caught violations did.",
        },
    ],
}

# ─────────────────────────────────────────────
# SCOPE
# ─────────────────────────────────────────────

_EP_DIRECTION_RE = re.compile(r"^episode-\d+/03_direction/[^/]+\.md$")
_EP_MUSIC_RE = re.compile(r"^episode-\d+/02_music/.*_musical_metadata\.json$")
_EP_LYRICS_RE = re.compile(r"^episode-\d+/01_lyrics/")

_RECURSIVE_MD_PREFIXES = (
    "_management/", "docs/", "_memory/", "_skills/", "_templates/",
    "_assets/", ".github/",
)


def in_scope(relpath: str) -> bool:
    """True if a repo-relative (already tracked) path is public prose this gate
    polices. Deliberately mirrors the SPEC scope list, not a broad glob."""
    p = relpath.replace("\\", "/")

    if p.startswith("tests/fixtures/"):
        return False
    if _EP_LYRICS_RE.match(p):
        return False

    if "/" not in p:
        return p.endswith(".md")  # top-level only, not recursive

    if p.endswith(".md") and p.startswith(_RECURSIVE_MD_PREFIXES):
        return True
    if _EP_DIRECTION_RE.match(p):
        return True
    if _EP_MUSIC_RE.match(p):
        return True
    return False


def tracked_files(repo_root: str) -> list:
    """`git ls-files` — the tracked-only universe. Gitignored and untracked paths
    never reach `in_scope`, so the EXCLUDE-by-gitignore requirement is structural,
    not a second filter that could drift out of sync with .gitignore."""
    out = subprocess.run(
        ["git", "ls-files"], cwd=repo_root, capture_output=True, text=True, check=True,
    )
    return [line for line in out.stdout.splitlines() if line]


def in_scope_tracked_files(repo_root: str) -> list:
    return sorted(f for f in tracked_files(repo_root) if in_scope(f))


# ─────────────────────────────────────────────
# MATCH · ALLOWLIST · CHECK
# ─────────────────────────────────────────────

def _normalize(line: str) -> str:
    """Lowercase + strip combining diacritics, so 'Halvetî'/'dergâh'/'etvârnâme'
    all reduce to their plain-ASCII root and match the same pattern the plain
    spelling does."""
    nfkd = unicodedata.normalize("NFKD", line)
    stripped = "".join(c for c in nfkd if not unicodedata.combining(c))
    return stripped.lower()


def find_terms_in_text(text: str) -> list:
    """Pure function: every (line_no, term) hit in raw text, allowlist NOT applied —
    including repeat occurrences of the same term on the same line (each is its own
    hit). No file I/O, no scope decision — grade this in isolation."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        norm = _normalize(line)
        for term, pat in _TERM_PATTERNS.items():
            for _m in pat.finditer(norm):
                hits.append((i, term))
    return hits


def filter_allowlisted(hits: list, lines: list, allow_entries: list) -> list:
    """Drop any (line_no, term) hit whose source line contains a pinned allowlist
    substring verbatim. Pure function — no file I/O — so the allowlist mechanism is
    gradeable without touching disk."""
    if not allow_entries:
        return hits
    out = []
    for line_no, term in hits:
        line_text = lines[line_no - 1] if 0 < line_no <= len(lines) else ""
        if any(entry["substring"] in line_text for entry in allow_entries):
            continue
        out.append((line_no, term))
    return out


def check_forbidden_terms(relpath: str, repo_root: str) -> list:
    """Findings for one file: [("FAIL", "path:line: forbidden term 'x'"), ...].
    Empty == clean. Scope-agnostic by design (mirrors doc_reference_check.py's
    lint_doc_file) so fixtures outside the live scope can still be graded directly."""
    abspath = os.path.join(repo_root, relpath)
    try:
        with open(abspath, encoding="utf-8") as f:
            text = f.read()
    except (FileNotFoundError, UnicodeDecodeError):
        return []

    lines = text.splitlines()
    hits = find_terms_in_text(text)
    allow_entries = ALLOWLIST.get(relpath.replace("\\", "/"), [])
    hits = filter_allowlisted(hits, lines, allow_entries)

    rel_display = relpath.replace("\\", "/")
    return [
        ("FAIL", f"{rel_display}:{line_no}: forbidden term '{term}'")
        for line_no, term in hits
    ]


def scan_repo(repo_root: str) -> list:
    """Findings across every in-scope tracked file."""
    findings = []
    for relpath in in_scope_tracked_files(repo_root):
        findings.extend(check_forbidden_terms(relpath, repo_root))
    return findings


# ─────────────────────────────────────────────
# RUNNER
# ─────────────────────────────────────────────

def run_full(repo_root: str) -> int:
    findings = scan_repo(repo_root)
    if findings:
        print(f"\n  Found {len(findings)} forbidden-term hit(s):\n")
        for _sev, msg in findings:
            print(f"    FAIL {msg}")
        print(f"\n  FORBIDDEN TERMS GATE FAILED — {len(findings)} hit(s) in public prose.")
        return 1
    print("\n  FORBIDDEN TERMS GATE PASSED — no banned religion/order/sect/scripture "
          "terms found in public prose.")
    return 0


def run_file(relpath: str, repo_root: str) -> int:
    findings = check_forbidden_terms(relpath, repo_root)
    if findings:
        print(f"\n  {relpath}")
        for _sev, msg in findings:
            print(f"    FAIL {msg}")
        print(f"\n  FORBIDDEN TERMS GATE FAILED — {len(findings)} hit(s).")
        return 1
    print("\n  FORBIDDEN TERMS GATE PASSED.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Forbidden-terms gate (religion/order/sect/scripture names) "
                    "over public prose."
    )
    parser.add_argument("--full", action="store_true", help="Scan every in-scope tracked file")
    parser.add_argument("--file", type=str, help="Scan a single file (scope-agnostic)")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — Forbidden Terms Gate")
    print("=" * 50)

    if args.file:
        return run_file(args.file, repo_root)
    return run_full(repo_root)


if __name__ == "__main__":
    sys.exit(main())
