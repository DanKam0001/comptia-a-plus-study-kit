"""Rebuild glossary/terms.md and glossary/terms.json from the video outlines' `glossary` arrays.

    python tools/build_glossary.py --exports <path to ai_deepdive_video/exports>

Every term that gets a corner card in a video, with its meaning. The first meaning seen wins (Intro, then Core 1
Part 1 to 16, then Core 2 Part 1 to 17); `first_appears` records where the term first showed up.
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def key_for(slug: str):
    if slug.startswith("comptia-a-core-1-and-core-2"):
        return (0, 0)
    m = re.search(r"comptia-a-core-(\d)-part-(\d+)$", slug)
    return (int(m.group(1)), int(m.group(2))) if m else None


def label(k):
    return "Intro" if k == (0, 0) else f"Core {k[0]} Part {k[1]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exports", required=True)
    args = ap.parse_args()
    outlines = []
    for d in Path(args.exports).iterdir():
        k = key_for(d.name)
        if k and (d / "outline.json").exists():
            outlines.append((k, d / "outline.json"))
    outlines.sort()
    terms = {}
    for k, p in outlines:
        for ch in json.loads(p.read_text(encoding="utf-8")).get("chapters", []):
            for g in ch.get("glossary") or []:
                t = g["term"].strip()
                terms.setdefault(t.lower(), {"term": t, "meaning": g["meaning"].strip(), "first_appears": label(k),
                                             "series": "Intro" if k[0] == 0 else f"Core {k[0]}", "first_part": k[1]})
    rows = sorted(terms.values(), key=lambda r: r["term"].lower())
    (ROOT / "glossary" / "terms.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    md = ["# Series glossary", "",
          "Every term that gets a corner card in the videos, with its meaning. Rebuilt from the video scripts by "
          "`tools/build_glossary.py`.", "", "| Term | Meaning | First appears |", "|---|---|---|"]
    md += [f"| {r['term']} | {r['meaning']} | {r['first_appears']} |" for r in rows]
    (ROOT / "glossary" / "terms.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(rows)} terms from {len(outlines)} outlines")


if __name__ == "__main__":
    main()
