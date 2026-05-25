### 131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward. 

**Example 1:**
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2:**
```
Input: s = "a"
Output: [["a"]]
``` 

**Constraints:**
```
1 <= s.length <= 16
s contains only lowercase English letters.
```

**Tags**
- Revisit
- String
- Dynamic Programming
- Backtracking

### Solution
There is a backtracking solution below this one. Also, we can probably use palindrome substrings to build the lookup table
```
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            Build lookup matrix of start, end is a palindrome
        """
        ans = []
        length = len(s)
        lookup = [[False for _ in range(length)] for _ in range(length)]
        
        for i in range(0, length):
            for j in range(i, length):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    lookup[i][j] = True
        
        
        def recurse(index):
            if index == length:
                return [[]]
            
            partitions = []
            for i in range(index, length):
                if not lookup[index][i]:
                    continue
                    
                result = recurse(i + 1)
               
                if result is not None:
                    for part in result:
                        partitions.append([s[index:i + 1]] + part)
            
            
            if not partitions:
                return None
            
            return partitions
        
        
        return recurse(0)
                
        
        
        
```
Backtracking:
```
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            Build lookup matrix of start, end is a palindrome
            Use backtracking:
            1. Figure out the potential candidate
            2. Find the goal that tells you that you found the required solution.
            If you reached the end of the string, then you have all palindromes
            3. remove the candidate from list and try another
        """
        ans = []
        length = len(s)
        lookup = [[False for _ in range(length)] for _ in range(length)]
        
        for i in range(0, length):
            for j in range(i, length):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    lookup[i][j] = True
        
        
        def backtrack(start, current):
            if start == length:
                ans.append(current.copy())
            
            for i in range(start, length):
                if not lookup[start][i]:
                    continue
                
                current.append(s[start: i + 1])
                backtrack(i + 1, current)
                current.pop()
            
        
        backtrack(0, [])
        
        return ans
        
        
        
```
