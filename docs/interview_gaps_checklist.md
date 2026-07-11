# Interview Coverage Gaps — Checklist

Prioritized backlog from the [gap analysis](interview_techniques.md). Use this when you want to fill blind spots in problem coverage or the [techniques guide](interview_techniques.md).

**Legend:** `[ ]` not started · `[x]` done · `problem` = add/solve LeetCode writeup · `technique` = add section to techniques doc · `both`

---

## Tier 1 — Highest ROI

These show up constantly in interviews and are either missing from the repo or under-documented.

### Linked list fundamentals

- [ ] **206. Reverse Linked List** (`problem`) — in-place reversal with `prev` / `curr` / `next`
- [ ] **19. Remove Nth Node From End of List** (`problem`) — fast/slow with k-gap; dummy sentinel
- [ ] Expand **linked list patterns** in techniques doc with explicit reverse + k-gap templates (`technique`)

### Design

- [ ] **146. LRU Cache** (`both`) — hash map + doubly linked list; eviction at capacity
- [ ] Add **LRU / cache design** subsection under design patterns (`technique`)

### Sliding window — monotonic deque

- [ ] **239. Sliding Window Maximum** (`both`) — deque maintains decreasing indices
- [ ] Add **monotonic deque** section (distinct from monotonic stack) (`technique`)

### Weighted graphs

- [ ] **743. Network Delay Time** (`both`) — Dijkstra with min-heap
- [ ] Add **Dijkstra** section to techniques doc + link from `graph_notes.md` (`technique`)

### String / 2D DP

- [ ] **72. Edit Distance** (`both`) — classic `dp[i][j]` for insert/delete/replace
- [ ] Add **edit distance / string DP** subsection under dynamic programming (`technique`)

### Topological sort (intro)

- [ ] **207. Course Schedule** (`problem`) — cycle detection + Kahn's or DFS coloring (simpler than 210)
- [ ] Note in techniques doc: 207 = "can finish?", 210 = "return order" (`technique`)

### Heap / quickselect

- [ ] **215. Kth Largest Element in an Array** (`both`) — heap vs quickselect tradeoffs
- [ ] Expand **quickselect** in techniques doc (partition, recurse one side) (`technique`)

### Bit manipulation warmups

- [ ] **268. Missing Number** (`problem`) — XOR or index marking
- [ ] **191. Number of 1 Bits** (`problem`) — `n & (n-1)` loop
- [ ] Cross-link from bit manipulation section (`technique`)

---

## Tier 2 — Strong coverage boost

Important patterns; repo has related problems but not the canonical form.

### Backtracking classics

- [ ] **22. Generate Parentheses** (`problem`) — backtracking with open/close counts
- [ ] **46. Permutations** (`problem`) — you have 47 (Permutations II); add base version
- [ ] **51. N-Queens** (`problem`) — backtracking + column/diag pruning

### DP — knapsack / counting

- [ ] **494. Target Sum** (`both`) — 0/1 knapsack / subset sum counting (416 is related but different)
- [ ] Add explicit **0/1 knapsack template** to DP section (`technique`)

### Graphs — multi-source BFS & union-find

- [ ] **417. Pacific Atlantic Water Flow** (`problem`) — BFS/DFS from border cells
- [ ] **721. Accounts Merge** (`problem`) — union-find + sort/merge emails
- [ ] **787. Cheapest Flights Within K Stops** (`problem`) — Bellman-Ford or modified Dijkstra
- [ ] Add **Bellman-Ford** subsection under graph patterns (`technique`)

### Greedy + heap / intervals

- [ ] **621. Task Scheduler** (`problem`) — greedy count + heap or math formula
- [ ] **253. Meeting Rooms II** (`problem`) — sort + min-heap of end times (or sweep)
- [ ] **45. Jump Game II** (`problem`) — greedy BFS-style jumps

### Sliding window variants

- [ ] **904. Fruit Into Baskets** (`problem`) — "at most 2 distinct" template (424 is similar)
- [ ] **1004. Max Consecutive Ones III** (`problem`) — "at most k flips" window

### Trees

- [ ] **236. Lowest Common Ancestor of a Binary Tree** (`both`) — only have 235 (BST variant)
- [ ] **105. Construct Binary Tree from Preorder and Inorder** (`problem`) — recursion + index map
- [ ] Add **LCA (general tree)** subsection under tree patterns (`technique`)

### Binary search on answer

- [ ] **875. Koko Eating Bananas** (`problem`) — you have 410; Koko is more commonly cited
- [ ] Tie both to **binary search on answer** template in techniques doc (`technique`)

---

## Tier 3 — Techniques doc & thin coverage

Improve documentation or add depth where the repo already has partial coverage.

### Named algorithms to document

- [ ] **Kadane's algorithm** — dedicated section; link 53, 134, 152 (max product variant) (`technique`)
- [ ] **Boyer-Moore voting** — done ✓ (169, 229)
- [ ] **Bitmask DP** — section for 526, 847; when state fits in bitmask (`technique`)
- [ ] **Floyd-Warshall** — section for all-pairs shortest path; link 399 (`technique`)
- [ ] **Prim / Kruskal MST** — expand beyond one-line advanced table; link 1584 (`technique`)
- [ ] **Rolling hash** — expand advanced section; link 187, 718, 1461 (`technique`)
- [ ] **KMP / string matching** — section for 28 (strStr); failure function (`technique`)
- [ ] **Two-heaps median** — document pattern; add **295. Find Median from Data Stream** if desired (`both`)

### Thin repo coverage — optional depth

Only needed if targeting harder companies or want pattern fluency.

- [ ] **Topological sort** — second problem beyond 210 (e.g. 269 Alien Dictionary) (`problem`)
- [ ] **Segment tree / Fenwick** — 406, 1649 exist; add technique walkthrough or skip (`technique`)
- [ ] **Reservoir sampling** — 382, 497 exist; doc is enough unless asked frequently (`technique`)
- [ ] **Sweep line** — 1 problem in index; low priority unless specific prep (`problem`)

### String DP extensions

- [ ] **97. Interleaving String** (`problem`)
- [ ] **115. Distinct Subsequences** (`problem`)
- [ ] **10. Regular Expression Matching** (`problem`, hard) — only if doing hard DP prep

### Graph / design extras

- [ ] **684. Redundant Connection** (`problem`) — union-find cycle detection
- [ ] **261. Graph Valid Tree** (`problem`) — union-find or DFS edge count
- [ ] **332. Reconstruct Itinerary** (`problem`) — Hierholzer / Eulerian path (niche)
- [ ] **295. Find Median from Data Stream** (`problem`) — two-heap design

### Hard classics (defer unless targeting senior/hard loops)

- [ ] **4. Median of Two Sorted Arrays** (`problem`) — binary search on partition
- [ ] **224. Basic Calculator** — you have 224 and 227; ensure **224** (with parens) is solid (`review`)

---

## Technique doc cross-reference gaps

Quick audit of [interview_techniques.md](interview_techniques.md) vs repo content.

| Technique | Status | Action |
|-----------|--------|--------|
| Hash map / two pointers / sliding window | Covered | Maintain |
| Boyer-Moore voting | Covered | Maintain |
| Monotonic stack | Covered | Maintain |
| Monotonic **deque** | Missing | Tier 1 |
| Kadane's (incl. max product) | Mentioned only | Tier 3 |
| Quickselect | Bundled under heap | Tier 1 |
| Dijkstra / Bellman-Ford | Missing | Tier 1–2 |
| Floyd-Warshall | Notes in 399 only | Tier 3 |
| LRU cache design | Missing | Tier 1 |
| Edit distance DP | Missing | Tier 1 |
| 0/1 knapsack template | Vague | Tier 2 |
| Bitmask DP | Appendix only | Tier 3 |
| KMP | Missing | Tier 3 |
| LCA (general tree) | Missing | Tier 2 |

---

## Suggested study order (minimal path)

If time is limited, tackle in this sequence:

1. 206 → 19 → 146 → 239 → 743 → 72 → 207 → 215 → 268
2. Update techniques doc for: monotonic deque, Dijkstra, quickselect, edit distance, LRU
3. 22 → 46 → 494 → 417 → 236 → 105 → 621 → 904
4. Tier 3 doc pass: Kadane's, bitmask DP, Floyd-Warshall, KMP

---

## When you complete an item

1. Add `{id}_{title}.md` at repo root (your usual writeup format)
2. Run:
   ```bash
   python scripts/tag_problems.py <filename>.md
   python scripts/generate_index.py
   python scripts/generate_technique_mapping.py
   ```
3. Splice appendix into `docs/interview_techniques.md` if needed (see [categorize-leetcode skill](../.cursor/skills/categorize-leetcode/SKILL.md))
4. Mark `[x]` here and add to ★ Must-do lists in techniques doc if canonical

---

## Related files

- [STUDY_INDEX.md](../STUDY_INDEX.md) — current 310 problems by topic
- [interview_techniques.md](interview_techniques.md) — pattern reference
- [graph_notes.md](graph_notes.md) — graph algorithms notes
- [bits_notes.md](bits_notes.md) — bit manipulation drills
