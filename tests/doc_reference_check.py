"""
Robotiko v2.0 - Doc Reference Integrity Lint

The repo's biggest credibility risk is documentation drifting from disk reality:
a load-bearing doc points at `tests/foo.py` or `_management/bar.md` that has been
renamed, moved, or deleted, and nobody notices until a reader (or a fork) hits the
dead link. A doc-rot sweep can clean it once; this lint makes that class of rot
machine-caught forever.

Two check sections, one file:

  SECTION 1 - Doc-reference existence
    Scans a CURATED list of load-bearing docs, extracts both backtick-quoted repo
    paths and markdown [text](path) link targets, and fails if any referenced path
    does not exist on disk. Deliberately narrow:
      * only backtick-quoted tokens that LOOK like repo-relative paths
        (contain "/" and end in a known extension, OR start with a known top-level
        dir like tests/ docs/ _management/ ...), plus markdown link targets checked
        as-is (a bare filename is a valid relative link; #anchor fragments are
        stripped before checking, and ../ relative paths resolve naturally);
      * URLs, glob/placeholder tokens ({XX}, *, <...>, [ ]), absolute / home paths,
        and paths under _private/ (gitignored by design) are skipped;
      * a line is tolerated whole if it carries an inline `<!-- doc-ref: ignore -->`
        suppression, or the word "removed" (case-insensitive) - historical notes.
    It also guards against HOOK-ROT: a present-tense claim about the removed naming
    hook (a line naming `naming_check_hook` or "PostToolUse" with no nearby
    removed / historical / was / once cue) fails, so the removed hook can never be
    re-described as live.

  SECTION 2 - Matrix <-> tests sync
    Every `check_` function defined in tests/*.py validators must be represented in
    _management/invariant_coverage_matrix.md (by name), OR be an admitted internal
    helper in ALLOWLIST. Catches a real enforcement check that shipped without an
    honesty-ledger row.

Dependencies: standard library only.

Usage:
    python tests/doc_reference_check.py
    python tests/doc_reference_check.py --full     # identical; accepted for parity

Status: IMPLEMENTED v1.0
"""

import os
import re
import sys
import glob
import argparse

# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

# Load-bearing docs whose references must stay true to disk. Repo-relative.
CURATED_DOCS = [
    "_management/architecture.md",
    "tests/README.md",
    "_management/invariant_coverage_matrix.md",
    "CONTRIBUTING.md",
    "README.md",
    "docs/getting-started.md",
    "docs/tools-setup.md",
    "docs/skills-guide.md",
    "docs/anatomy-of-an-episode.md",
    "docs/hallucinating-camera.md",
    "docs/method-lesson-graduation.md",
    "_management/dissonance_registry.md",
    "FORKING.md",
    "docs/fork-dry-run.md",
    "docs/text-only-first-episode.md",
    "docs/two-phase-visual-prompts.md",
    "docs/visual-canon.md",
    "GOVERNANCE.md",
    "ROADMAP.md",
    "UNIVERSES.md",
    "SUPPORT.md",
    "CODE_OF_CONDUCT.md",
]

# Extensions that mark a backtick token as a file path.
KNOWN_EXTENSIONS = (
    ".py", ".md", ".json", ".yml", ".yaml", ".sh", ".png", ".jpg", ".jpeg",
    ".cube", ".wav", ".mp4", ".mov", ".js", ".pdf", ".txt",
)

# Top-level directories that mark a backtick token as a repo path (even a bare dir).
KNOWN_DIR_PREFIXES = (
    "tests/", "docs/", "scripts/", "_management/", "_assets/", "_skills/",
    ".github/", ".claude/", "_memory/", "_templates/", "_tools/",
)

# Render outputs that are gitignored by design (never committed, absent in CI).
# Referencing them in a doc is correct, so there is nothing on disk to verify.
RENDER_OUTPUT_EXTENSIONS = (".mp4", ".mov", ".wav", ".mp3", ".psd")
RENDER_OUTPUT_DIR_MARKERS = ("/raw/", "/selected/")

# Inline, same-line suppression for a genuine anti-example / historical mention.
SUPPRESS_MARK = "<!-- doc-ref: ignore -->"

# Words that mark a hook mention as historical rather than a live claim.
HOOK_HISTORICAL_CUES = ("removed", "historical", "was", "once", "no longer", "never")

# check_ functions that are genuine internal helpers, not standalone invariants.
# check_episode is the per-episode loop driver inside pipeline_integrity.py; its
# invariant ("no silently-skipped pipeline steps") is represented in the matrix by
# the SCRIPT row (`pipeline_integrity.py --full`), not by the helper name.
ALLOWLIST = {
    "check_episode",
}

MATRIX_PATH = "_management/invariant_coverage_matrix.md"
BACKTICK = re.compile(r"`([^`]+)`")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


# -------------------------------------------------------------------
# SECTION 1 - helpers: path extraction + existence
# -------------------------------------------------------------------

def _scope_rejects(token):
    """True for tokens this lint is designed to skip: URLs, globs/placeholders,
    and absolute or home paths. Shared by the backtick and link-target scans."""
    low = token.lower()
    if "://" in low or low.startswith(("http", "www.", "mailto:")):
        return True
    if token.startswith(("/", "~")):
        return True
    if any(c in token for c in "*{}<>[]|") or " " in token:
        return True
    if "XX" in token or "VV" in token:            # ep{XX}, v{VV}, episode-XX/
        return True
    return False


def _looks_like_repo_path(token):
    """True if a backtick token looks like a repo-relative path worth checking."""
    if not token:
        return False
    if _scope_rejects(token):
        return False

    # Normalize leading ./ and ../ only for the prefix test.
    probe = token
    while probe.startswith("../") or probe.startswith("./"):
        probe = probe[3:] if probe.startswith("../") else probe[2:]

    stem = token[:-1] if token.endswith("/") else token
    has_slash = "/" in stem
    has_ext = stem.lower().endswith(KNOWN_EXTENSIONS)
    if has_slash and has_ext:
        return True
    if probe.startswith(KNOWN_DIR_PREFIXES):
        return True
    if re.match(r"episode-\d\d/", probe):
        return True
    return False


def extract_path_tokens(line):
    """Yield qualifying repo-path tokens from the backtick spans of one line.

    _private/ paths are dropped here (gitignored by design)."""
    out = []
    for span in BACKTICK.findall(line):
        for raw in span.split():
            # Strip wrapping prose punctuation, but NEVER a leading dot
            # (dotpaths like .github/... .claude/... must survive).
            tok = raw.strip().strip("(),;:!?\"'*")
            while tok and tok[-1] in ".,;:!?)":      # trailing prose punctuation only
                tok = tok[:-1]
            if not _looks_like_repo_path(tok):
                continue
            probe = tok
            while probe.startswith("../") or probe.startswith("./"):
                probe = probe[3:] if probe.startswith("../") else probe[2:]
            # _private/ and gitignored render outputs are absent by design.
            if probe.startswith("_private/") or "/_private/" in tok:
                continue
            if tok.lower().endswith(RENDER_OUTPUT_EXTENSIONS):
                continue
            if any(m in tok for m in RENDER_OUTPUT_DIR_MARKERS) or \
                    tok.endswith(("/raw", "/selected")):
                continue
            out.append(tok)
    return out


def extract_link_targets(line):
    """Yield markdown [text](path) link targets worth checking for existence.

    The backtick heuristic (a token must contain "/" or start with a known
    prefix) is deliberately NOT applied here: a bare filename like `file.md`
    is a valid markdown relative link and must be checked. _private/ paths and
    gitignored render outputs are dropped, matching extract_path_tokens."""
    out = []
    for target in MARKDOWN_LINK.findall(line):
        path = target.split("#", 1)[0].strip()
        if not path:                       # pure in-page anchor, no path to check
            continue
        if _scope_rejects(path):
            continue
        if path.startswith("_private/") or "/_private/" in target:
            continue
        if path.lower().endswith(RENDER_OUTPUT_EXTENSIONS):
            continue
        if any(m in target for m in RENDER_OUTPUT_DIR_MARKERS) or \
                path.endswith(("/raw", "/selected")):
            continue
        out.append(path)
    return out


def path_exists(token, doc_abspath, repo_root):
    """A token resolves if it exists relative to the repo root OR to the doc dir
    (the repo mixes repo-root-relative backticks with ../-relative doc links)."""
    root_cand = os.path.normpath(os.path.join(repo_root, token.lstrip("/")))
    doc_cand = os.path.normpath(os.path.join(os.path.dirname(doc_abspath), token))
    return os.path.exists(root_cand) or os.path.exists(doc_cand)


def _line_suppressed(line):
    return SUPPRESS_MARK in line


def scan_hook_claims(lines):
    """Return (line_no, detail) for present-tense claims about the removed naming
    hook. A trigger line is exculpated if it, or an adjacent line, carries a
    historical cue (removed / historical / was / once / ...) or a suppression."""
    findings = []
    n = len(lines)
    for i, line in enumerate(lines):
        if "naming_check_hook" not in line and "PostToolUse" not in line:
            continue
        window = " ".join(lines[max(0, i - 1):min(n, i + 2)]).lower()
        if _line_suppressed(line):
            continue
        if any(cue in window for cue in HOOK_HISTORICAL_CUES):
            continue
        findings.append((i + 1, line.strip()))
    return findings


def lint_doc_file(doc_relpath, repo_root):
    """Findings for one doc: (severity, message). Empty == clean."""
    doc_abspath = os.path.join(repo_root, doc_relpath)
    findings = []
    if not os.path.isfile(doc_abspath):
        return [("WARN", f"curated doc not found (skipped): {doc_relpath}")]

    with open(doc_abspath, encoding="utf-8") as f:
        lines = f.read().splitlines()

    # 1a. Reference existence.
    for i, line in enumerate(lines, 1):
        if _line_suppressed(line) or "removed" in line.lower():
            continue
        seen = set()
        for tok in extract_path_tokens(line) + extract_link_targets(line):
            # The same broken target often appears as both `` `path` `` and
            # [x](path) on one line, with and without a leading ../ in the two
            # forms — report the underlying miss once, keyed on the repo file.
            key = tok
            while key.startswith("../") or key.startswith("./"):
                key = key[3:] if key.startswith("../") else key[2:]
            if key in seen:
                continue
            seen.add(key)
            if not path_exists(tok, doc_abspath, repo_root):
                findings.append(
                    ("FAIL", f"{doc_relpath}:{i} references missing path: {tok}")
                )

    # 1b. Hook-rot.
    for line_no, detail in scan_hook_claims(lines):
        findings.append(
            ("FAIL", f"{doc_relpath}:{line_no} present-tense claim about the "
                     f"removed naming hook: {detail}")
        )

    return findings


def scan_all_docs(repo_root):
    findings = []
    for doc in CURATED_DOCS:
        findings.extend(lint_doc_file(doc, repo_root))
    return findings


# -------------------------------------------------------------------
# SECTION 2 - matrix <-> tests sync
# -------------------------------------------------------------------

def collect_check_functions(repo_root):
    """Map check_ function name -> relative file where it is defined."""
    found = {}
    for path in sorted(glob.glob(os.path.join(repo_root, "tests", "*.py"))):
        with open(path, encoding="utf-8") as f:
            src = f.read()
        for name in re.findall(r"^def (check_\w+)", src, flags=re.MULTILINE):
            found.setdefault(name, os.path.relpath(path, repo_root).replace("\\", "/"))
    return found


def verify_matrix_sync(repo_root):
    """Findings for check_ functions absent from both the matrix and the allowlist."""
    findings = []
    matrix_abspath = os.path.join(repo_root, MATRIX_PATH)
    if not os.path.isfile(matrix_abspath):
        return [("WARN", f"coverage matrix not found (skipped): {MATRIX_PATH}")]

    with open(matrix_abspath, encoding="utf-8") as f:
        matrix = f.read()

    for name, where in sorted(collect_check_functions(repo_root).items()):
        if name in ALLOWLIST:
            continue
        if name in matrix:
            continue
        findings.append(
            ("FAIL", f"{where}:{name}() has no row in {MATRIX_PATH} and is not in "
                     f"ALLOWLIST - add an enforcement row or admit it as internal.")
        )
    return findings


# -------------------------------------------------------------------
# RUNNER
# -------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Doc reference integrity lint")
    parser.add_argument("--full", action="store_true",
                        help="Run every section (default behavior).")
    parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 - Doc Reference Integrity Lint")
    print("=" * 50)

    doc_findings = scan_all_docs(repo_root)
    print(f"\n  [Section 1] Doc-reference existence + hook-rot "
          f"({len(CURATED_DOCS)} curated docs)")
    if doc_findings:
        for sev, msg in doc_findings:
            print(f"    {sev}: {msg}")
    else:
        print("    OK: every backtick-quoted repo path resolves; no hook-rot.")

    sync_findings = verify_matrix_sync(repo_root)
    print("\n  [Section 2] Coverage-matrix sync (check_ functions <-> matrix)")
    if sync_findings:
        for sev, msg in sync_findings:
            print(f"    {sev}: {msg}")
    else:
        print("    OK: every enforcement check_ function has a matrix row or "
              "is an admitted internal helper.")

    all_findings = doc_findings + sync_findings
    fails = [f for f in all_findings if f[0] == "FAIL"]
    print("\n" + "=" * 50)
    if fails:
        print(f"  DOC REFERENCE INTEGRITY FAILED - {len(fails)} issue(s).")
        sys.exit(1)
    print("  DOC REFERENCE INTEGRITY PASSED.")
    sys.exit(0)


if __name__ == "__main__":
    main()
