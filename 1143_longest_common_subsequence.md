### 1143. Longest Common Subsequence
Medium

Given two strings `text1` and `text2`, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) 
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0. 

**Example 1:**
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

**Example 2:**
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

**Example 3:**
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

**Constraints:**

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

**Tags**
- String
- Dynamic Programming

### Solution

NOTE: looks like you can also start at the beginning of the both strings, instead of the end! Tested it on leetcode!
```
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var createArray = function(rows, columns) {
    let result = [];
    for (let i = 0; i < rows; i++) {
        let arr = [];
        for (let j = 0; j < columns; j++) {
            arr.push(undefined);
        }
        result.push(arr);
    }
    
    return result;
}

var lcs = function(s1, s2, s1Max, s2Max, dp) {
    if (s1Max < 0 || s2Max < 0) {
        return 0;
    }
    // check if it is in the table
    if (dp[s1Max][s2Max]) {
        return dp[s1Max][s2Max];
    }

    let result;
    // both end characters are equal
    if (s1[s1Max] === s2[s2Max]) {
        result = 1 + lcs(s1, s2, s1Max - 1, s2Max - 1, dp);
    } else {
        // get the lcs when removing the last char for both s1, and s2
        // then get the max of the lcs
        let result1 = lcs(s1, s2, s1Max, s2Max - 1, dp);
        let result2 = lcs(s1, s2, s1Max - 1, s2Max, dp);
        result = Math.max(result1, result2);
    }
    
    dp[s1Max][s2Max] = result;
    return result;
}
var longestCommonSubsequence = function(text1, text2) {
    let dp = createArray(text1.length, text2.length);
    return lcs(text1, text2, text1.length - 1, text2.length - 1, dp);
};
```
### Python version
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        
        dp = [[None for i in range(length2)] for j in range(length1)]
        
        
        def lcs(text1, text2, pos1, pos2):
            if pos1 == length1 or pos2 == length2:
                return 0
            
            if dp[pos1][pos2] is not None:
                return dp[pos1][pos2]
            
            if text1[pos1] == text2[pos2]:
                dp[pos1][pos2] = 1 + lcs(text1, text2, pos1 + 1, pos2 + 1)
            else:
                first = lcs(text1, text2, pos1 + 1, pos2)
                second = lcs(text1, text2, pos1, pos2 + 1)
                dp[pos1][pos2] = max(first, second)
        
            return dp[pos1][pos2]
        
        return lcs(text1, text2, 0, 0)
        
```
