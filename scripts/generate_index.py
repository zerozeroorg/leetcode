#!/usr/bin/env python3
"""Generate STUDY_INDEX.md grouped by topic and difficulty."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "STUDY_INDEX.md"

PROBLEM_FILE_RE = re.compile(r"^(\d{4})_.+\.md$", re.IGNORECASE)
HEADING_RE = re.compile(r"^(?:#{2,3}\s+)?(\d+)\.\s+(.+)$")
DIFFICULTY_RE = re.compile(r"^(Easy|Medium|Hard)$")
DIFFICULTY_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2, "Unknown": 3}
PERSONAL_TAGS = {
    "revisit",
    "unsolved",
    "non-intuitive",
    "non intuitive",
    "backwards",
}


def list_problem_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.glob("*.md")
        if PROBLEM_FILE_RE.match(path.name) and path.name.lower() != "readme.md"
    )


def parse_problem(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()

    number = int(path.name[:4])
    title = path.stem[5:].replace("_", " ")
    difficulty = "Unknown"
    tags: list[str] = []

    for i, line in enumerate(lines):
        heading = HEADING_RE.match(line)
        if heading:
            number = int(heading.group(1))
            title = heading.group(2).strip()
            diff_idx = i + 1
            if diff_idx < len(lines) and lines[diff_idx].strip() == "":
                diff_idx += 1
            if diff_idx < len(lines) and DIFFICULTY_RE.match(lines[diff_idx].strip()):
                difficulty = lines[diff_idx].strip()
            break

    in_tags = False
    for line in lines:
        stripped = line.strip()
        if stripped == "**Tags**":
            in_tags = True
            continue
        if in_tags:
            if stripped.startswith("- "):
                tags.append(stripped[2:].strip())
                continue
            if stripped == "":
                continue
            in_tags = False

    return {
        "number": number,
        "title": title,
        "filename": path.name,
        "difficulty": difficulty,
        "tags": tags,
    }


def sort_problems(problems: list[dict]) -> list[dict]:
    return sorted(
        problems,
        key=lambda p: (DIFFICULTY_ORDER.get(p["difficulty"], 99), p["number"], p["title"].lower()),
    )


def render_index(grouped: dict[str, dict[str, list[dict]]]) -> str:
    lines = [
        "# LeetCode Study Index",
        "",
        "Problems grouped by topic and difficulty for interview prep.",
        "",
        f"Total problems: {len(list_problem_files())}",
        "",
    ]

    for topic in sorted(grouped.keys(), key=lambda t: (t == "Uncategorized", t.lower())):
        lines.append(f"## {topic}")
        lines.append("")
        by_difficulty = grouped[topic]
        for difficulty in ["Easy", "Medium", "Hard", "Unknown"]:
            problems = by_difficulty.get(difficulty, [])
            if not problems:
                continue
            lines.append(f"### {difficulty}")
            for problem in sort_problems(problems):
                label = f"{problem['number']}. {problem['title']}"
                lines.append(f"- [{label}]({problem['filename']})")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    grouped: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))

    for path in list_problem_files():
        problem = parse_problem(path)
        topics = [
            tag for tag in problem["tags"] if tag.strip().lower() not in PERSONAL_TAGS
        ] or ["Uncategorized"]
        for topic in topics:
            grouped[topic][problem["difficulty"]].append(problem)

    OUTPUT.write_text(render_index(grouped), encoding="utf-8")
    print(f"Wrote {OUTPUT} with {len(list_problem_files())} problems across {len(grouped)} topics.")


if __name__ == "__main__":
    main()
