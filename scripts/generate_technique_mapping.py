#!/usr/bin/env python3
"""Build problem → technique mapping from tags and heuristics."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
import sys

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Priority-ordered: first matching tag wins as primary technique
TAG_TO_TECHNIQUE: list[tuple[str, str]] = [
    ("Linked List", "Linked list patterns"),
    ("Trie", "Trie"),
    ("Union-Find", "Union-Find"),
    ("Topological Sort", "Topological sort"),
    ("Monotonic Stack", "Monotonic stack"),
    ("Segment Tree", "Segment tree (advanced)"),
    ("Binary Indexed Tree", "Fenwick tree (advanced)"),
    ("Reservoir Sampling", "Reservoir sampling (advanced)"),
    ("Rolling Hash", "Rolling hash (advanced)"),
    ("Bitmask", "Bitmask DP"),
    ("Sliding Window", "Sliding window"),
    ("Prefix Sum", "Prefix / suffix sums"),
    ("Binary Search", "Binary search"),
    ("Dynamic Programming", "Dynamic programming"),
    ("Backtracking", "Backtracking"),
    ("Breadth-First Search", "Graph BFS"),
    ("Depth-First Search", "Graph DFS"),
    ("Graph Theory", "Graph BFS/DFS"),
    ("Shortest Path", "Graph BFS (shortest path)"),
    ("Minimum Spanning Tree", "MST (advanced)"),
    ("Heap (Priority Queue)", "Heap / quickselect"),
    ("Quickselect", "Heap / quickselect"),
    ("Bit Manipulation", "Bit manipulation"),
    ("Design", "Design (hash + structure)"),
    ("Binary Search Tree", "BST properties"),
    ("Binary Tree", "Tree DFS / BFS"),
    ("Tree", "Tree DFS / BFS"),
    ("Stack", "Stack / parsing"),
    ("Queue", "BFS / queue simulation"),
    ("Two Pointers", "Two pointers"),
    ("Greedy", "Greedy"),
    ("Sorting", "Sorting + greedy"),
    ("Hash Table", "Hash map lookup"),
    ("Hash Function", "Hash map lookup"),
    ("Counting", "Hash map / counting"),
    ("Matrix", "Matrix patterns"),
    ("String", "String patterns"),
    ("Math", "Math patterns"),
    ("Simulation", "Simulation"),
    ("Divide and Conquer", "Divide and conquer"),
    ("Merge Sort", "Divide and conquer"),
    ("Recursion", "Recursion / DFS"),
    ("Memoization", "Dynamic programming"),
    ("Combinatorics", "Combinatorics"),
    ("Enumeration", "Enumeration"),
    ("Geometry", "Geometry (advanced)"),
    ("Game Theory", "Game theory (advanced)"),
    ("Data Stream", "Design (data stream)"),
    ("Iterator", "BST iterator"),
    ("Randomized", "Randomized (advanced)"),
    ("Ordered Set", "Ordered set (advanced)"),
    ("Bucket Sort", "Bucket sort"),
    ("String Matching", "String matching (advanced)"),
    ("Sweep Line", "Intervals / sweep line"),
    ("Doubly-Linked List", "Linked list patterns"),
    ("Array", "Array fundamentals"),
]

# Title/number overrides for more precise primary technique
OVERRIDES: dict[int, str] = {
    1: "Hash map lookup",
    11: "Two pointers (opposite ends)",
    15: "Two pointers (opposite ends)",
    16: "Two pointers (opposite ends)",
    19: "Linked list patterns",
    21: "Linked list patterns",
    23: "Linked list patterns",
    25: "Linked list patterns",
    42: "Two pointers (opposite ends)",
    53: "Dynamic programming (Kadane's)",
    56: "Intervals",
    76: "Sliding window",
    84: "Monotonic stack",
    121: "Dynamic programming (state machine)",
    141: "Linked list patterns",
    142: "Linked list patterns",
    143: "Linked list patterns",
    148: "Linked list patterns",
    160: "Linked list patterns",
    200: "Graph DFS",
    207: "Topological sort",
    238: "Prefix / suffix sums",
    322: "Dynamic programming",
    347: "Heap / quickselect",
    560: "Prefix / suffix sums",
    739: "Monotonic stack",
    876: "Linked list patterns",
}

PERSONAL_TAGS = {"revisit", "unsolved", "non-intuitive", "non intuitive", "backwards"}


def parse_problem(path: Path) -> dict:
    from scripts.generate_index import parse_problem as _parse

    return _parse(path)


def primary_technique(problem: dict) -> str:
    num = problem["number"]
    if num in OVERRIDES:
        return OVERRIDES[num]

    tags = [t for t in problem["tags"] if t.lower() not in PERSONAL_TAGS]
    tag_set = set(tags)

    for tag, technique in TAG_TO_TECHNIQUE:
        if tag in tag_set:
            return technique

    return "Array fundamentals"


def secondary_techniques(problem: dict, primary: str) -> list[str]:
    tags = [t for t in problem["tags"] if t.lower() not in PERSONAL_TAGS]
    secondaries: list[str] = []
    for tag, technique in TAG_TO_TECHNIQUE:
        if technique != primary and tag in tags and technique not in secondaries:
            secondaries.append(technique)
    return secondaries[:2]


def build_mapping() -> list[dict]:
    from scripts.generate_index import list_problem_files

    mapping = []
    for path in list_problem_files():
        p = parse_problem(path)
        primary = primary_technique(p)
        mapping.append(
            {
                "number": p["number"],
                "title": p["title"],
                "filename": p["filename"],
                "difficulty": p["difficulty"],
                "primary": primary,
                "secondary": secondary_techniques(p, primary),
            }
        )
    return sorted(mapping, key=lambda x: x["number"])


def format_link(filename: str) -> str:
    if "(" in filename or ")" in filename:
        return f"<../{filename}>"
    return f"../{filename}"


def render_appendix(mapping: list[dict]) -> str:
    by_technique: dict[str, list[dict]] = defaultdict(list)
    for p in mapping:
        by_technique[p["primary"]].append(p)

    lines = [
        "## Appendix A: Problems by Technique",
        "",
        "Every indexed problem mapped to a primary technique. Secondary tags omitted for brevity.",
        "",
    ]

    for technique in sorted(by_technique.keys()):
        lines.append(f"### {technique}")
        lines.append("")
        for p in by_technique[technique]:
            target = format_link(p["filename"])
            lines.append(
                f"- [{p['number']}. {p['title']}]({target}) ({p['difficulty']})"
            )
        lines.append("")

    lines.extend(
        [
            "## Appendix B: Quick Lookup (Problem → Technique)",
            "",
            "| # | Problem | Primary Technique |",
            "|---|---------|-------------------|",
        ]
    )

    for p in mapping:
        target = format_link(p["filename"])
        lines.append(
            f"| {p['number']} | [{p['title']}]({target}) | {p['primary']} |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    mapping = build_mapping()
    out_json = ROOT / "scripts" / "problem_techniques.json"
    out_json.write_text(json.dumps(mapping, indent=2), encoding="utf-8")
    appendix = render_appendix(mapping)
    appendix_path = ROOT / "scripts" / "_techniques_appendix.md"
    appendix_path.write_text(appendix, encoding="utf-8")
    print(f"Wrote {out_json} ({len(mapping)} problems)")
    print(f"Wrote {appendix_path}")


if __name__ == "__main__":
    main()
