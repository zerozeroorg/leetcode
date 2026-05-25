### 392. Is Subsequence
Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not). 

**Example 1:**
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2:**
```
Input: s = "axc", t = "ahbgdc"
Output: false
``` 

**Constraints:**
```
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
``` 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

**Tags**
- Two Pointers
- String
- Dynamic Programming

### Solution
- Have ptrs for s and t.
- Move ptrs
```
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let sPtr = 0;
    let tPtr = 0;
    
    while (sPtr < s.length && tPtr < t.length) {
        if (s[sPtr] === t[tPtr]) {
            sPtr += 1;
            tPtr += 1;
            continue;
        }
        tPtr += 1;
    }
    
    return sPtr === s.length && tPtr <= t.length;
};
```
