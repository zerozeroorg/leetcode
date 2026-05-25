### 424. Longest Repeating Character Replacement
Medium

Medium

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 
```
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
``` 

Constraints:
```
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
```
One idea is for each character in the string, build a substring that meets the criteria of repeating characters for that character. This would take O(n^2)

The best approach would have to be linear time. To do that, we need to incorporate some sort of sliding window. The decide when to expand or shrink this sliding window, it would require this intuition:

```
substring - max_repeating_char_count <= k
```

We only care about the max repeating char count, and not the actual max repeating char because there could be ties like A vs B but it doesn't matter.

**Tags**
- Hash Table
- String
- Sliding Window

### Solution
```
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let longest = 0;
    let longestRepeating = 0;
    let lookup = {};
    let left = 0;
    let right = 0;

    while (right < s.length) {
        let char = s[right];
        lookup[char] = lookup[char] || 0;
        lookup[char] += 1;
        longestRepeating = Math.max(longestRepeating, lookup[char]);

        // intuition: the substring is valid if - 
        // substring - longestRepeating <= k
        let substringLength = right - left + 1;
        if (substringLength - longestRepeating <= k) {
            longest = Math.max(longest, substringLength);
            right += 1;
            continue;
        } else {
            lookup[s[left]] -= 1;
            left += 1;
            right += 1;
        }
    }

    return longest;
};
```
