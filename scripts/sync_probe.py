"""
Robotiko v2.0 - Local sync-measurement helper (NOT a CI check).

The repo produces scores, not mixes: every beat-sync claim is checkbox-verified in
the CapCut guide, never measured against the actual render. This tool measures.

Given a final render and its musical metadata it will:
  1. compare the container duration (ffprobe) against metadata `total_duration`,
     reporting the delta with a +/-1s tolerance verdict;
  2. run ffmpeg scene-change detection, map each detected cut to the nearest
     musical-section boundary, and print a markdown table (cut time, nearest
     boundary, delta ms) you can paste straight into the sync-QC record.

WHY THIS CANNOT RUN IN CI
-------------------------
The final render is gitignored - it lives on Google Drive / a portable disk, never
in the repository tree. CI can validate the *score* (metadata, motion script,
naming) but can never see the *mix*. So this is a LOCAL, human-run helper: it exists
so the committed sync-QC record (`_templates/ep_sync_qc_template.md`) contains
measured numbers instead of vibes. It is deliberately absent from `tests/run_all.py`.

External dependency: ffmpeg + ffprobe on PATH (invoked as a CLI). If either is
missing the tool prints an install hint and exits 2 - it never crashes.

Usage:
    python scripts/sync_probe.py --video ep10_final_v01.mp4 \
                                 --metadata episode-10/02_music/ep10_musical_metadata.json
    python scripts/sync_probe.py --metadata-only \
                                 --metadata episode-08/02_music/ep08_musical_metadata.json
    python scripts/sync_probe.py --help

Exit codes: 0 = ran, 2 = precondition missing (no ffmpeg / no file / bad metadata).

Status: LOCAL HELPER (not wired into run_all.py / CI).
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

SCENE_PTS = re.compile(r"pts_time:([0-9]+\.?[0-9]*)")
INSTALL_HINT = (
    "  ffmpeg/ffprobe not found on PATH. This tool needs them to read the render.\n"
    "  Install ffmpeg (it bundles ffprobe):\n"
    "    Windows : winget install Gyan.FFmpeg      (or: choco install ffmpeg)\n"
    "    macOS   : brew install ffmpeg\n"
    "    Linux   : sudo apt install ffmpeg         (or your distro's package)\n"
    "    Manual  : https://ffmpeg.org/download.html\n"
)


def fail(msg, code=2):
    """Print an error and exit with the given code (default 2 = precondition)."""
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def fmt_mmss(seconds):
    """Seconds -> M:SS.mmm."""
    if seconds is None:
        return "-"
    m = int(seconds) // 60
    s = seconds - m * 60
    return f"{m}:{s:06.3f}"


def load_metadata(path):
    """Return (total_duration, sections) or exit 2 on any problem."""
    if not os.path.isfile(path):
        fail(f"metadata file not found: {path}")
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"could not read metadata JSON ({path}): {exc}")
    sections = data.get("sections")
    if not isinstance(sections, list) or not sections:
        fail(f"metadata has no usable 'sections' array: {path}")
    return data.get("total_duration"), sections


def section_boundaries(sections):
    """List of (time_seconds, label) - one boundary per section start, sorted."""
    out = []
    for sec in sections:
        start = sec.get("start")
        if start is None:
            continue
        label = sec.get("type", "section")
        energy = sec.get("energy", "")
        tag = f"{label}" + (f" [{energy}]" if energy else "")
        out.append((float(start), tag))
    out.sort(key=lambda x: x[0])
    return out


def nearest_boundary(cut_time, boundaries):
    """Return (boundary_time, label, delta_ms) for the closest boundary."""
    best = min(boundaries, key=lambda b: abs(b[0] - cut_time))
    delta_ms = round((cut_time - best[0]) * 1000)
    return best[0], best[1], delta_ms


def print_boundary_table(boundaries, total_duration):
    """The metadata-only view: the section-boundary grid. Runnable without media."""
    print("\n### Section Boundary Grid (from metadata)\n")
    print(f"- Sections: {len(boundaries)}")
    print(f"- Metadata total_duration: "
          f"{total_duration}s ({fmt_mmss(total_duration)})\n")
    print("| # | boundary (s) | boundary (mm:ss) | section |")
    print("|---|---|---|---|")
    for i, (t, label) in enumerate(boundaries, 1):
        print(f"| {i} | {t:.3f} | {fmt_mmss(t)} | {label} |")
    print()


def have_ffmpeg():
    return bool(shutil.which("ffmpeg")) and bool(shutil.which("ffprobe"))


def probe_duration(video):
    """Container duration in seconds via ffprobe, or None on failure."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", video,
    ]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:
        fail(f"failed to invoke ffprobe: {exc}")
    raw = out.stdout.strip()
    try:
        return float(raw)
    except ValueError:
        return None


def detect_cuts(video, threshold):
    """Detected scene-change timestamps (seconds) via ffmpeg select+showinfo.

    select='gt(scene,THRESH)' with showinfo is the most portable invocation - it
    works on any ffmpeg build, unlike the newer scdet filter."""
    vf = f"select='gt(scene,{threshold})',showinfo"
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", video,
           "-filter:v", vf, "-f", "null", "-"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:
        fail(f"failed to invoke ffmpeg: {exc}")
    # showinfo writes to stderr.
    times = [float(m) for m in SCENE_PTS.findall(out.stderr)]
    times.sort()
    return times


def duration_report(video, total_duration, tolerance):
    print("\n### Duration Check\n")
    dur = probe_duration(video)
    if dur is None:
        print("- ffprobe could not read a container duration for the render.")
        return
    print(f"- Render duration   : {dur:.3f}s ({fmt_mmss(dur)})")
    if total_duration is None:
        print("- Metadata total_duration: (absent) - cannot compute delta.")
        return
    delta = dur - float(total_duration)
    verdict = "WITHIN TOLERANCE" if abs(delta) <= tolerance else "OUT OF TOLERANCE"
    print(f"- Metadata duration : {float(total_duration):.3f}s "
          f"({fmt_mmss(float(total_duration))})")
    print(f"- Delta             : {delta:+.3f}s "
          f"(tolerance +/-{tolerance:g}s) -> {verdict}")


def cut_report(video, boundaries, threshold):
    print("\n### Cut -> Nearest Boundary (paste into the sync-QC record)\n")
    cuts = detect_cuts(video, threshold)
    if not cuts:
        print(f"- No scene changes detected at threshold {threshold}. "
              "Try a lower --scene-threshold.")
        return
    print(f"- Detected cuts: {len(cuts)} (scene threshold {threshold})\n")
    print("| cut (s) | cut (mm:ss) | nearest boundary (mm:ss) | section | delta ms |")
    print("|---|---|---|---|---|")
    for c in cuts:
        bt, label, dms = nearest_boundary(c, boundaries)
        print(f"| {c:.3f} | {fmt_mmss(c)} | {fmt_mmss(bt)} | {label} | {dms:+d} |")
    print()


def build_parser():
    p = argparse.ArgumentParser(
        description="Local sync-measurement helper (NOT a CI check). "
                    "Measures a gitignored render against its musical metadata.")
    p.add_argument("--video", help="Path to the final render (e.g. epXX_final_v01.mp4).")
    p.add_argument("--metadata", required=True,
                   help="Path to epXX_musical_metadata.json.")
    p.add_argument("--metadata-only", action="store_true",
                   help="Print only the section-boundary grid (needs no media, "
                        "runs today).")
    p.add_argument("--scene-threshold", type=float, default=0.3,
                   help="ffmpeg scene-change sensitivity (default 0.3).")
    p.add_argument("--tolerance", type=float, default=1.0,
                   help="Duration delta tolerance in seconds (default 1.0).")
    return p


def main():
    args = build_parser().parse_args()

    total_duration, sections = load_metadata(args.metadata)
    boundaries = section_boundaries(sections)
    if not boundaries:
        fail("no section start times found in metadata - nothing to map against.")

    print("Robotiko v2.0 - sync_probe (LOCAL helper, not CI)")
    print("=" * 52)

    if args.metadata_only:
        print_boundary_table(boundaries, total_duration)
        print("Metadata-only mode: no render inspected. "
              "Provide --video (with ffmpeg installed) to measure cuts.")
        return

    if not args.video:
        fail("--video is required unless --metadata-only is set.")
    if not os.path.isfile(args.video):
        fail(f"video file not found: {args.video}")
    if not have_ffmpeg():
        print(INSTALL_HINT, file=sys.stderr)
        sys.exit(2)

    print_boundary_table(boundaries, total_duration)
    duration_report(args.video, total_duration, args.tolerance)
    cut_report(args.video, boundaries, args.scene_threshold)
    print("Done. Numbers are measured, local, and never seen by CI.")


if __name__ == "__main__":
    main()
