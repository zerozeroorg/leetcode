### 132. Palindrome Partitioning II
Hard

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s. 

**Example 1:**
```
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

**Example 2:**
```
Input: s = "a"
Output: 0
```

**Example 3:**
```
Input: s = "ab"
Output: 1
``` 

**Constraints:**
```
1 <= s.length <= 2000
s consists of lower-case English letters only.
```

**Tags**
- String
- Dynamic Programming

### Solution
- Freaking hard problem
- I had to look up how to find all palindrome substrings in O(n^2) time
- Idea: if where you cut is a palindrome, then get min_cuts of the rest of the string. Try this for all areas where you can cut.
- Definitely study this problem and look at how others have solved it.
```
class Solution:
    def minCut(self, s: str) -> int:
        """
            Set starting ptr = 0
            while ptr < length - 1:
            - loop through ptr + 1 to end of string to generate palindromes
            - get the max of these if any
            - set ptr to the max of these + 1
            - increment result
            return result
        """
        length = len(s)
        lookup = [[False if i != j else True for i in range(length)] for j in range(length)]
        cut_lookup = [[None for i in range(length)] for j in range(length)]
        
        for i in range(length):
            left = i - 1
            right = i + 1
            while 0 <= left < right < length:
                if s[left] != s[right]:
                    lookup[left][right] = False
                    break
                else:
                    lookup[left][right] = True
                    left -= 1
                    right += 1
            left = i
            right = i + 1
            while 0 <= left < right < length:
                if s[left] != s[right]:
                    lookup[left][right] = False
                    break
                else:
                    lookup[left][right] = True
                    left -= 1
                    right += 1
        
        def min_cuts(i, j):
            if lookup[i][j]:
                return 0
            
            if cut_lookup[i][j] is not None:
                return cut_lookup[i][j]
            
            result = float('inf')
            for k in range(i, j + 1):
                if lookup[i][k]:
                    first_cut = 1 + min_cuts(k + 1, j)
                    result = min(result, first_cut)
            
            if result == float('inf'):
                cut_lookup[i][j] = 0
                return cut_lookup[i][j]
            
            cut_lookup[i][j] = result
            return cut_lookup[i][j]
        
        return min_cuts(0, length - 1)

        
        
```
