### 695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
 

**Example 1:**
```

[0,0,1,0,0,0,0,1,0,0,0,0,0]
[0,0,0,0,0,0,0,1,1,1,0,0,0]
[0,1,1,0,1,0,0,0,0,0,0,0,0]
[0,1,0,0,1,1,0,0,1,0,1,0,0]
[0,1,0,0,1,1,0,0,1,1,1,0,0]
[0,0,0,0,0,0,0,0,0,0,1,0,0]
[0,0,0,0,0,0,0,1,1,1,0,0,0]
[0,0,0,0,0,0,0,1,1,0,0,0,0]

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**
```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
``` 

**Constraints:**
```
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
```

**Tags**
- Array
- Depth-First Search
- Breadth-First Search
- Union-Find
- Matrix

### Solution
```
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int maxArea = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    maxArea = Math.max(maxArea, bfs(grid, visited, rows, cols, i, j));
                }
            }
        }
        return maxArea;
    }
    
    private int bfs(int[][] grid, boolean[][] visited, int maxRow, int maxCol, int row, int col) {
        int maxArea = 0;
        
        if (visited[row][col]) {
            return 0;
        }
        
        visited[row][col] = true;
        if (grid[row][col] == 0) {
            return 0;
        }
        
        maxArea = 1;
        
        int[][] directions = {
            {-1, 0},
            {1, 0},
            {0, 1},
            {0, -1}
        };
        
        for (int i = 0; i < directions.length; i++) {
            int[] direction = directions[i];
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (newRow >= 0 && newRow < maxRow && 
                newCol >= 0 && newCol < maxCol && grid[newRow][newCol] == 1) {
                maxArea += bfs(grid, visited, maxRow, maxCol, newRow, newCol);
            }
        }
        
        return maxArea;
    }
}
```
