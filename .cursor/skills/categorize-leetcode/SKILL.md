---
name: categorize-leetcode
description: Categorize new LeetCode problem markdown files with difficulty and topic tags, then update STUDY_INDEX.md and the interview techniques catalog. Use when the user adds a new coding problem, asks to categorize or tag problems, or asks to update the study index or techniques guide.
---

# Categorize LeetCode Problems

## When to use

Apply this skill when:
- A new `{id}_{title}.md` problem file is added to the repo root
- The user asks to categorize, tag, or organize LeetCode problems
- The user asks to update `STUDY_INDEX.md`
- The user asks to update the interview techniques guide or problem → technique mapping

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
4. Refresh the problem → technique mapping and appendix stub:
   ```bash
   python scripts/generate_technique_mapping.py
   ```
5. If the techniques appendix changed, splice it into `docs/interview_techniques.md`:
   - Replace the content after `<!-- APPENDIX_PLACEHOLDER -->`, or
   - Replace everything from `## Appendix A: Problems by Technique` onward with `scripts/_techniques_appendix.md`
6. Report the assigned difficulty, topic tags, and primary technique to the user.

## What the scripts do

- **`scripts/tag_problems.py`**: Fetches official difficulty and topic tags from the LeetCode API (cached in `scripts/lc_metadata.json`), then updates each markdown file:
  - Adds `Easy`/`Medium`/`Hard` after the title if missing
  - Removes legacy `### Tags` sections if present
  - Adds or updates a `**Tags**` section with official LeetCode topic tags
  - Preserves personal flags: `revisit`, `unsolved`, `non-intuitive`, `backwards`
- **`scripts/generate_index.py`**: Reads all tagged problem files and writes `STUDY_INDEX.md`, grouped by topic then by difficulty (Easy → Medium → Hard → Unknown). Also:
  - Injects per-topic **Must-know** summaries from `scripts/topic_techniques.json`
  - Wraps link targets in angle brackets when filenames contain `(` or `)` (e.g. `0380_Insert_Delete_GetRandom_O(1).md`)
  - Adds a pointer to `docs/interview_techniques.md` at the top of the index
- **`scripts/generate_technique_mapping.py`**: Assigns each problem a primary interview technique from its tags (with manual overrides in the script). Writes:
  - `scripts/problem_techniques.json` — machine-readable mapping
  - `scripts/_techniques_appendix.md` — appendix content for `docs/interview_techniques.md`

## Study guide files

| File | Role | Editable by hand? |
|------|------|-------------------|
| `STUDY_INDEX.md` | Problem index by topic/difficulty | No — regenerate with `generate_index.py` |
| `docs/interview_techniques.md` | Must-know patterns + appendices | Yes — core pattern sections are hand-curated; appendices are regenerated |
| `scripts/topic_techniques.json` | Per-topic must-know bullets for STUDY_INDEX | Yes — edit when adding topics or refining summaries |
| `scripts/problem_techniques.json` | Problem → primary technique mapping | No — regenerate with `generate_technique_mapping.py` |

## Maintenance notes

### Adding a new problem

Run steps 1–4 in the workflow above. Splice the appendix (step 5) only when the new problem should appear in Appendix A/B of the techniques doc.

If the new problem is a canonical example for a pattern, also add it manually to the relevant section in `docs/interview_techniques.md` (the ★ Must-do or Also practice lists).

### Editing per-topic must-know summaries

Edit `scripts/topic_techniques.json`, then rerun:
```bash
python scripts/generate_index.py
```

Each entry has:
- `techniques` — 2–4 bullet phrases shown in STUDY_INDEX
- `doc_anchor` — anchor in `docs/interview_techniques.md` (e.g. `linked-list-patterns`)

### Improving technique assignments

Primary technique mapping lives in `scripts/generate_technique_mapping.py`:
- `TAG_TO_TECHNIQUE` — priority-ordered tag → technique name
- `OVERRIDES` — problem number → technique for exceptions

After editing, rerun `generate_technique_mapping.py` and splice the appendix.

### Link gotchas

- Filenames with parentheses must use angle-bracket links: `[text](<0380_Insert_Delete_GetRandom_O(1).md>)`
- `generate_index.py` handles this automatically for STUDY_INDEX
- From `docs/interview_techniques.md`, use `[text](<../filename.md>)` for parenthesis filenames
- One filename has a space: `0027_Remove Element.md` — link as `[27. Remove Element](../0027_Remove Element.md)`

### Do not edit by hand

- `STUDY_INDEX.md` — overwritten by `generate_index.py`
- `scripts/_techniques_appendix.md` — build artifact; splice into techniques doc instead of editing in place
- `scripts/problem_techniques.json` — regenerated from tags/overrides

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
- Navigation: `README.md` links to `STUDY_INDEX.md` and `docs/interview_techniques.md`.
