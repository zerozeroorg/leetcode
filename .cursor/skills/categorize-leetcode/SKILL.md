---
name: categorize-leetcode
description: Categorize new LeetCode problem markdown files with difficulty and topic tags, then update STUDY_INDEX.md. Use when the user adds a new coding problem, asks to categorize or tag problems, or asks to update the study index.
---

# Categorize LeetCode Problems

## When to use

Apply this skill when:
- A new `{id}_{title}.md` problem file is added to the repo root
- The user asks to categorize, tag, or organize LeetCode problems
- The user asks to update `STUDY_INDEX.md`

## Workflow

1. Identify the new or changed problem file(s) in the repo root (pattern: `\d{4}_.+\.md`).
2. Tag the file(s):
   ```bash
   python scripts/tag_problems.py <filename>.md
   ```
   Or tag all problems:
   ```bash
   python scripts/tag_problems.py --all
   ```
3. Regenerate the study index:
   ```bash
   python scripts/generate_index.py
   ```
4. Report the assigned difficulty and topic tags to the user.

## What the scripts do

- **`scripts/tag_problems.py`**: Fetches official difficulty and topic tags from the LeetCode API (cached in `scripts/lc_metadata.json`), then updates each markdown file:
  - Adds `Easy`/`Medium`/`Hard` after the title if missing
  - Removes legacy `### Tags` sections if present
  - Adds or updates a `**Tags**` section with official LeetCode topic tags
  - Preserves personal flags: `revisit`, `unsolved`, `non-intuitive`, `backwards`
- **`scripts/generate_index.py`**: Reads all tagged problem files and writes `STUDY_INDEX.md`, grouped by topic then by difficulty (Easy → Medium → Hard → Unknown).

## File format expectations

Problem files should have a title line like:
```
### 1. Two Sum
```
or plain:
```
1. Two Sum
```

After tagging, files will include difficulty and tags:
```
### 1. Two Sum
Easy
...
**Tags**
- Array
- Hash Table
```

## Notes

- Slug lookup uses the 4-digit problem ID from the filename via `scripts/lc_problem_slugs.json`.
- Re-running tag scripts is safe; metadata is cached and files are only rewritten when changed.
- Personal study flags in `**Tags**` are kept; they are excluded from topic grouping in `STUDY_INDEX.md`.
