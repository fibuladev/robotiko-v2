"""
Robotiko v2.0 — Scoped Prompt Hygiene Lint (model-facing strings ONLY)

The cultural-attribution rule cuts both ways:

  - Canon REQUIRES the sanctioned Turkish attribution — the names (Yunus Emre,
    Hacı Bektaş Veli) and tradition labels ("Turkish wisdom tradition") — in
    master.md, the philosophy docs, and the internal direction notes (concept
    notes, dramaturgy, musical metadata). That is correct and must never be
    "fixed". THIS LINT NEVER READS THOSE FILES.

  - The model-facing prompt strings — the **Text Prompt** blocks in visual-prompt
    files and the **Motion Prompt** blocks in motion-script files — are fed
    verbatim to image/video models and must stay plain-English ASCII: no non-ASCII
    characters, no tradition-label decoration.

So the scope is deliberately narrow: only the prompt blockquotes inside
`episode-*/04_visuals/ep*_visual_prompts_v*.md` and
`episode-*/05_video/ep*_motion_script_v*.md`. The Dramaturgy Reference / Composition
Notes lines in those same files are OUT of scope (they may carry sanctioned Turkish).

Usage:
    python tests/prompt_hygiene_lint.py --full        # check every in-scope file
    python tests/prompt_hygiene_lint.py --file <path>
    python tests/prompt_hygiene_lint.py --fix         # normalize prompt blocks to ASCII

See _management/adr/0006-scoped-prompt-hygiene.md.
Status: IMPLEMENTED v1.0
"""

import os
import re
import sys
import glob
import argparse
import unicodedata

# ─────────────────────────────────────────────
# SCOPE — the only files this lint will ever open, and the only blocks it reads.
# ─────────────────────────────────────────────

IN_SCOPE = [
    ("visual", "episode-*/04_visuals/ep*_visual_prompts_v*.md", "Text Prompt"),
    ("motion", "episode-*/05_video/ep*_motion_script_v*.md", "Motion Prompt"),
]

# Files that carry sanctioned Turkish attribution and must NEVER be read here.
# Listed for the proving test; the globs above already exclude them by construction.
OUT_OF_SCOPE_PATTERNS = (
    "master.md", "_concept_notes", "_dramaturgy", "_musical_metadata",
    "/philosophy", "\\philosophy",
)

SCAFFOLD_MARKERS = ("auto-populated by Claude", "Do not fill manually", "[Claude generates", "{XX}")

# Tradition-label decoration that belongs in canon/direction notes, not in a prompt.
TRADITION_LABELS = [
    r"turkish wisdom tradition",
    r"anatolian wisdom tradition",
    r"\bwisdom tradition\b",
    r"turkish folk poetry",
    r"turkish folk tradition",
    r"\bfolk poetry\b",
]

# Small allowlists for sanctioned exceptions (kept empty by default = strict ASCII).
ALLOWED_NONASCII = set()            # e.g. {"©"} if ever genuinely needed
ALLOWED_LABEL_SUBSTRINGS = []       # exact lowercase substrings to forgive

# ASCII transliteration for the normalizer (--fix).
_TRANSLIT = {
    "—": "-", "–": "-", "‒": "-", "―": "-", "−": "-",
    "’": "'", "‘": "'", "ʼ": "'", "‛": "'", "`": "'",
    "“": '"', "”": '"', "„": '"',
    "…": "...", "•": "-", "·": "-", "×": "x", "→": " to ", "°": " degrees ",
    "ç": "c", "Ç": "C", "ğ": "g", "Ğ": "G", "ı": "i", "İ": "I",
    "ş": "s", "Ş": "S", "ö": "o", "Ö": "O", "ü": "u", "Ü": "U",
    "é": "e", "è": "e", "ê": "e", "á": "a", "à": "a", "â": "a",
    "í": "i", "ó": "o", "ú": "u", "ñ": "n",
}


# ─────────────────────────────────────────────
# SCOPE RESOLUTION
# ─────────────────────────────────────────────

def in_scope_files(repo_root: str = ".") -> list:
    """Latest version of each in-scope file per episode. By construction, only prompt-bearing files."""
    all_files = []
    for _kind, pattern, _marker in IN_SCOPE:
        all_files.extend(sorted(glob.glob(os.path.join(repo_root, pattern))))
    latest = {}
    for path in all_files:
        ep_dir = os.path.dirname(os.path.dirname(path))
        kind = "visual" if "04_visuals" in path else "motion"
        key = (ep_dir, kind)
        if key not in latest or path > latest[key]:
            latest[key] = path
    return sorted(latest.values())


def marker_for(path: str) -> str:
    return "Motion Prompt" if os.sep + "05_video" + os.sep in path or "/05_video/" in path else "Text Prompt"


def _block_pattern(marker: str) -> re.Pattern:
    # The marker line, then the contiguous blockquote ('>' lines) that follows it.
    return re.compile(
        rf"(\*\*{re.escape(marker)}:?\s*\*\*:?\s*\n)((?:[ \t]*>.*(?:\n|$))+)"
    )


# ─────────────────────────────────────────────
# EXTRACT · CHECK · FIX  (operate on prompt blockquotes only)
# ─────────────────────────────────────────────

def extract_prompt_strings(content: str, marker: str) -> list:
    out = []
    for m in _block_pattern(marker).finditer(content):
        lines = [re.sub(r"^[ \t]*>\s?", "", ln) for ln in m.group(2).splitlines()]
        out.append("\n".join(lines))
    return out


def lint_content(content: str, marker: str) -> list:
    """Return findings: (block_index, kind, detail). Empty == clean."""
    findings = []
    for i, s in enumerate(extract_prompt_strings(content, marker), 1):
        bad = sorted({c for c in s if ord(c) > 127 and c not in ALLOWED_NONASCII})
        if bad:
            findings.append((i, "non-ascii", " ".join(f"{c!r}(U+{ord(c):04X})" for c in bad)))
        low = s.lower()
        for lab in TRADITION_LABELS:
            if re.search(lab, low) and not any(a in low for a in ALLOWED_LABEL_SUBSTRINGS):
                findings.append((i, "tradition-label", lab))
    return findings


def _asciize(text: str) -> str:
    out = []
    for c in text:
        if ord(c) < 128:
            out.append(c)
        elif c in _TRANSLIT:
            out.append(_TRANSLIT[c])
        else:
            stripped = "".join(ch for ch in unicodedata.normalize("NFKD", c) if ord(ch) < 128)
            out.append(stripped)
    return "".join(out)


def fix_content(content: str, marker: str) -> str:
    """ASCII-normalize ONLY the prompt blockquotes; leave everything else untouched."""
    pat = _block_pattern(marker)
    return pat.sub(lambda m: m.group(1) + _asciize(m.group(2)), content)


# ─────────────────────────────────────────────
# RUNNERS
# ─────────────────────────────────────────────

def _is_scaffold(content: str) -> bool:
    return any(m in content for m in SCAFFOLD_MARKERS)


def lint_file(path: str) -> list:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if _is_scaffold(content):
        return []
    return lint_content(content, marker_for(path))


def run_full(repo_root: str = ".") -> int:
    total = 0
    for path in in_scope_files(repo_root):
        findings = lint_file(path)
        rel = os.path.relpath(path, repo_root)
        if findings:
            total += len(findings)
            print(f"\n  {rel}")
            for idx, kind, detail in findings:
                print(f"    FAIL [{kind}] prompt block #{idx}: {detail}")
    if total:
        print(f"\n  PROMPT HYGIENE FAILED — {total} issue(s) in model-facing prompt strings.")
        return 1
    print("\n  PROMPT HYGIENE PASSED — all model-facing prompt strings are plain-English ASCII.")
    return 0


def run_fix(repo_root: str = ".") -> int:
    changed = 0
    for path in in_scope_files(repo_root):
        with open(path, encoding="utf-8") as f:
            content = f.read()
        if _is_scaffold(content):
            continue
        fixed = fix_content(content, marker_for(path))
        if fixed != content:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(fixed)
            changed += 1
            print(f"  normalized: {os.path.relpath(path, repo_root)}")
    print(f"\n  {changed} file(s) normalized.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Scoped prompt hygiene lint (model-facing strings only)")
    parser.add_argument("--full", action="store_true", help="Check every in-scope file")
    parser.add_argument("--file", type=str, help="Check a single file")
    parser.add_argument("--fix", action="store_true", help="ASCII-normalize prompt blocks in place")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    print("Robotiko v2.0 — Scoped Prompt Hygiene Lint")
    print("=" * 50)

    if args.fix:
        sys.exit(run_fix("."))
    if args.file:
        findings = lint_file(args.file)
        if findings:
            print(f"\n  {args.file}")
            for idx, kind, detail in findings:
                print(f"    FAIL [{kind}] prompt block #{idx}: {detail}")
            print(f"\n  PROMPT HYGIENE FAILED — {len(findings)} issue(s).")
            sys.exit(1)
        print("\n  PROMPT HYGIENE PASSED.")
        sys.exit(0)
    sys.exit(run_full("."))


if __name__ == "__main__":
    main()
