### 5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s. 

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

**Example 3:**
```
Input: s = "a"
Output: "a"
```

**Example 4:**
```
Input: s = "ac"
Output: "a"
``` 

**Constraints:**
```
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
```

**Tags**
- Two Pointers
- String
- Dynamic Programming

### Solution:
```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            For each char in s:
                - check left and right
                - if equal, move the pointers. Get the substring and check if is longest.
                - if not equal, break
                - now check char and right of it:
                - if equal, move the poitners. Get the substring and check if is longest.
                - if not equal, break
            return longest substring
            
            Edge case: single character. 
        """
        length = len(s)
        maxLength = 0
        result = ""
        
        for index in range(length):
            for (left, right) in [(index, index), (index, index + 1)]:
                while left >= 0 and right < length:
                    if s[left] != s[right]:
                        break

                    if right - left + 1 > maxLength:
                        maxLength = right - left + 1
                        result = s[left:right + 1]
                    
                    left -= 1
                    right += 1
            
        return result
```
