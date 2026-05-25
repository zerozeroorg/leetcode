### 62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
 

**Example 1:**
```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**
```
Input: m = 3, n = 2
Output: 3
```

**Explanation:**
```
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

**Example 3:**
```
Input: m = 7, n = 3
Output: 28
```

**Example 4:**
```
Input: m = 3, n = 3
Output: 6
``` 

**Constraints:**
```
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
```

**Tags**
- Math
- Dynamic Programming
- Combinatorics

### Solution
```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        
        def recurse(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            
            if x >= m or y >= n:
                return 0
            
            if dp[x][y] is not None:
                return dp[x][y]
            
            total = recurse(x + 1, y) + recurse(x, y + 1)
            dp[x][y] = total
            
            return total
        
        return recurse(0, 0)
```
