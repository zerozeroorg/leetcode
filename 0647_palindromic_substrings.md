### 647. Palindromic Substrings
Medium

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

**Example 1:**
```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**
```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
``` 

**Note:**
```
The input string length won't exceed 1000.
```

**Tags**
- Two Pointers
- String
- Dynamic Programming

### Solution:
```
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
          for each char in string:
          - check if it is a palindrome
          - if it is, then move start and end pointers
          - do this for start = end = index
          - do this for start = index, end = index + 1
        """
        result = 0
        length = len(s)
        
        def get_palindrome_count_at(index):
            count = 0
            # start with start and end = index
            start = index
            end = index
            while start >= 0 and end < length:
                if s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break
            
            # start with start = index and end = index + 1
            start = index
            end = index + 1
            while start >= 0 and end < length:
                if s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break                
            
            return count
            
        for index in range(length):
            result += get_palindrome_count_at(index)

        return result
        
```
