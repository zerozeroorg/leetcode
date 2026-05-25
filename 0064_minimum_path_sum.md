### 64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

**Example:**
```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

**Tags**
- Array
- Dynamic Programming
- Matrix

### Solution:
- Use DP
- Take the best path between the left and right paths

```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = 0
        if rows > 0:
            cols = len(grid[0])
        
        if rows == 0 or cols == 0:
            return 0
        
        dp = [[None for i in range(cols)] for j in range(rows)]
        
        def helper(x, y):
            if dp[x][y] is not None:
                return dp[x][y]
            
            if x == rows - 1 and y == cols - 1:
                dp[x][y] = grid[rows - 1][cols - 1]
                return dp[x][y]
            
            moves = []
            if y + 1 < cols:
                moves.append(helper(x, y + 1))
            if x + 1 < rows:
                moves.append(helper(x + 1, y))
            
            dp[x][y] = min(moves) + grid[x][y]
            return dp[x][y]
        
        return helper(0, 0)
```
