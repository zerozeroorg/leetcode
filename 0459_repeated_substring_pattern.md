### 459. Repeated Substring Pattern
Easy

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.


**Example 1:**
```
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
```

**Example 2:**

```
Input: "aba"
Output: False
```

**Example 3:**
```
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```

**Tags**
- String
- String Matching

### Solution
- use bruteforce or
- but the two strings together, remove the first and last char. The Substring should exist. WTF?

```
/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function(s) {
    let divide = 1;
    while (divide <= s.length / 2) {
        let length = s.length / divide;
        if (length !== Math.floor(length)) {
            divide += 1;
            continue;
        }
        
        let result = [];
        for (let i = 0; i < length; i++) {
            result.push(s.substr(0, divide));
        }
        
        if (result.join('') === s) {
            return true;
        }
        divide += 1;
    }
    
    return false;
};
```
