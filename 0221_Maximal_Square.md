### 221. Maximal Square
Medium

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area. 

**Example 1:**
```
["1","0","1","0","0"]
["1","0","1","1","1"]
["1","1","1","1","1"]
["1","0","0","1","0"]

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

**Example 2:**
```
["0","1"]
["1","0"]

Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

**Example 3:**
```
Input: matrix = [["0"]]
Output: 0
``` 

**Constraints:**
```
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
```

**Tags**
- Revisit
- Array
- Dynamic Programming
- Matrix

### Solution
```
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
            DP problem
            copy the matrix as dp array and init with all zeroes
            for each cell in matrix:
            if the cell is zero, skip
            dp[i][j] = min(dp[left], dp[above], dp[diagonal]) + 1
            the plus one is for cells that are ones because if it is surrounded
            by zeroes, the square with the 1 still has area of 1.
            
            Then get the max of this calculation
        """
        rows = len(matrix)
        cols = len(matrix[0])
        max_square = 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
            
        for i in range(rows):
            for j in range(cols):
                cell = matrix[i][j]
                if cell == "0":
                    continue
                
                above = dp[i - 1][j] if 0 <= i - 1 < rows else 0
                left = dp[i][j - 1] if 0 <= j - 1 < cols else 0
                diagonal = dp[i - 1][j - 1] if 0 <= i - 1 < rows and 0 <= j - 1 < cols else 0
                dp[i][j] = min(above, left, diagonal) + 1
                max_square = max(max_square, dp[i][j])
        
        
        return max_square ** 2
```
