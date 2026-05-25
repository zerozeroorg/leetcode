#!/usr/bin/env python3
"""Tag LeetCode problem markdown files with difficulty and topic tags from LeetCode API."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
SLUG_CACHE = SCRIPTS / "lc_problem_slugs.json"
METADATA_CACHE = SCRIPTS / "lc_metadata.json"

GRAPHQL_URL = "https://leetcode.com/graphql"
PROBLEMS_ALL_URL = "https://leetcode.com/api/problems/all/"
PROBLEM_FILE_RE = re.compile(r"^(\d{4})_.+\.md$", re.IGNORECASE)
HEADING_RE = re.compile(r"^(?:#{2,3}\s+)?(\d+)\.\s+(.+)$")
DIFFICULTY_RE = re.compile(r"^(Easy|Medium|Hard)$")
PERSONAL_TAGS = {
    "revisit",
    "unsolved",
    "non-intuitive",
    "non intuitive",
    "backwards",
}

QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    difficulty
    topicTags { name slug }
  }
}
""".strip()


def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def http_get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "leetcode-study-organizer/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def graphql_query(title_slug: str) -> dict | None:
    payload = json.dumps({"query": QUERY, "variables": {"titleSlug": title_slug}}).encode("utf-8")
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "leetcode-study-organizer/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f"  HTTP error for slug '{title_slug}': {exc}", file=sys.stderr)
        return None

    question = data.get("data", {}).get("question")
    if not question:
        print(f"  No metadata found for slug '{title_slug}'", file=sys.stderr)
        return None
    return question


def load_slug_map() -> dict[str, str]:
    cached = load_json(SLUG_CACHE)
    if cached:
        return cached

    print("Fetching LeetCode problem slug map...")
    data = http_get_json(PROBLEMS_ALL_URL)
    slug_map: dict[str, str] = {}
    for item in data.get("stat_status_pairs", []):
        stat = item.get("stat", {})
        qid = str(stat.get("frontend_question_id", "")).zfill(4)
        slug = stat.get("question__title_slug")
        if qid and slug:
            slug_map[qid] = slug

    save_json(SLUG_CACHE, slug_map)
    return slug_map


def get_metadata(slug: str, cache: dict) -> dict | None:
    if slug in cache:
        return cache[slug]

    question = graphql_query(slug)
    if not question:
        return None

    metadata = {
        "title": question["title"],
        "difficulty": question["difficulty"],
        "topicTags": [tag["name"] for tag in question.get("topicTags", [])],
    }
    cache[slug] = metadata
    time.sleep(0.1)
    return metadata


def list_problem_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.glob("*.md")
        if PROBLEM_FILE_RE.match(path.name) and path.name.lower() != "readme.md"
    )


def parse_existing_tags(lines: list[str]) -> tuple[int | None, list[str]]:
    tags_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "**Tags**":
            tags_idx = i
            break

    if tags_idx is None:
        return None, []

    tags: list[str] = []
    for line in lines[tags_idx + 1 :]:
        stripped = line.strip()
        if stripped.startswith("- "):
            tags.append(stripped[2:].strip())
            continue
        if stripped == "":
            continue
        break
    return tags_idx, tags


def is_personal_tag(tag: str) -> bool:
    normalized = tag.strip().lower()
    return normalized in PERSONAL_TAGS


def merge_tags(existing_tags: list[str], official_tags: list[str]) -> list[str]:
    personal = [tag for tag in existing_tags if is_personal_tag(tag)]
    merged: list[str] = []
    seen: set[str] = set()

    for tag in personal + official_tags:
        key = tag.strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        merged.append(tag.strip())

    return merged


def find_solution_index(lines: list[str]) -> int | None:
    for i, line in enumerate(lines):
        if line.startswith("### Solution"):
            return i
    return None


def remove_legacy_tag_sections(lines: list[str]) -> tuple[list[str], bool]:
    """Remove old `### Tags` blocks superseded by `**Tags**`."""
    changed = False
    i = 0
    while i < len(lines):
        if lines[i].strip() == "### Tags":
            end = i + 1
            while end < len(lines):
                stripped = lines[end].strip()
                if stripped.startswith("- ") or stripped == "":
                    end += 1
                    continue
                break
            del lines[i:end]
            changed = True
            continue
        i += 1
    return lines, changed


def update_file(path: Path, difficulty: str, official_tags: list[str]) -> bool:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    changed = False

    heading_idx = None
    for i, line in enumerate(lines):
        if HEADING_RE.match(line):
            heading_idx = i
            break

    if heading_idx is None:
        print(f"  Skipping {path.name}: no heading found", file=sys.stderr)
        return False

    lines, legacy_removed = remove_legacy_tag_sections(lines)
    changed = changed or legacy_removed

    if heading_idx + 1 < len(lines):
        next_line = lines[heading_idx + 1].strip()
        diff_idx = heading_idx + 1
        if next_line == "" and heading_idx + 2 < len(lines):
            diff_idx = heading_idx + 2
            next_line = lines[diff_idx].strip()
        if DIFFICULTY_RE.match(next_line):
            pass
        else:
            lines.insert(heading_idx + 1, difficulty)
            if heading_idx + 2 >= len(lines) or lines[heading_idx + 2].strip() != "":
                lines.insert(heading_idx + 2, "")
            changed = True
    else:
        lines.insert(heading_idx + 1, difficulty)
        changed = True

    tags_idx, existing_tags = parse_existing_tags(lines)
    merged_tags = merge_tags(existing_tags, official_tags)
    tag_lines = ["**Tags**"] + [f"- {tag}" for tag in merged_tags] + [""]

    if tags_idx is not None:
        end = tags_idx + 1
        while end < len(lines):
            stripped = lines[end].strip()
            if stripped.startswith("- ") or stripped == "":
                end += 1
                continue
            break
        new_tag_block = "\n".join(tag_lines).rstrip("\n")
        old_tag_block = "\n".join(lines[tags_idx:end]).rstrip("\n")
        if new_tag_block != old_tag_block:
            lines[tags_idx:end] = tag_lines
            changed = True
    else:
        solution_idx = find_solution_index(lines)
        insert_at = solution_idx if solution_idx is not None else len(lines)
        lines[insert_at:insert_at] = tag_lines
        changed = True

    if changed:
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return changed


def tag_file(path: Path, slug_map: dict[str, str], metadata_cache: dict) -> bool:
    match = PROBLEM_FILE_RE.match(path.name)
    if not match:
        return False

    qid = match.group(1)
    slug = slug_map.get(qid)
    if not slug:
        print(f"  No slug mapping for {path.name} (id {qid})", file=sys.stderr)
        return False

    metadata = get_metadata(slug, metadata_cache)
    if not metadata:
        return False

    changed = update_file(path, metadata["difficulty"], metadata["topicTags"])
    status = "updated" if changed else "unchanged"
    print(f"  {path.name}: {status} ({metadata['difficulty']}, {', '.join(metadata['topicTags'])})")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Tag LeetCode problem markdown files.")
    parser.add_argument("files", nargs="*", help="Specific markdown files to tag")
    parser.add_argument("--all", action="store_true", help="Tag all problem files in repo root")
    args = parser.parse_args()

    if args.all:
        targets = list_problem_files()
    elif args.files:
        targets = [Path(f) if Path(f).is_absolute() else ROOT / f for f in args.files]
    else:
        targets = list_problem_files()

    slug_map = load_slug_map()
    metadata_cache = load_json(METADATA_CACHE)

    print(f"Tagging {len(targets)} file(s)...")
    updated = 0
    for path in targets:
        if tag_file(path, slug_map, metadata_cache):
            updated += 1

    save_json(METADATA_CACHE, metadata_cache)
    print(f"Done. Updated {updated}/{len(targets)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
