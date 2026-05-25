### 200. Number of Islands
Medium

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Constraints:**
```
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
```

**Tags**
- Array
- Depth-First Search
- Breadth-First Search
- Union-Find
- Matrix

### Solution:
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            have a visited grid, initialized to all False
            have a global counter
            then for each grid cell:
                check if it is a 1 and is not visited
                if true: 
                    increment global counter by 1
                    and fill any neighboring cells with 1s in visited grid 
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for x in range(cols)] for y in range(rows)]
        count = 0
        
        def visitNeighbors(i, j):
            visited[i][j] = True
            north = grid[i - 1][j] if i - 1 >= 0 else 0
            south = grid[i + 1][j] if i + 1 < rows else 0
            east = grid[i][j - 1] if j - 1 >= 0 else 0
            west = grid[i][j + 1] if j + 1 < cols else 0
            if north == '1' and visited[i - 1][j] is False:
                visitNeighbors(i - 1, j)
            if south == '1' and visited[i + 1][j] is False:
                visitNeighbors(i + 1, j)
            if east == '1' and visited[i][j - 1] is False:
                visitNeighbors(i, j - 1)
            if west == '1' and visited[i][j + 1] is False:
                visitNeighbors(i, j + 1)
            
        
        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j]
                if cell == '1' and visited[i][j] is False:
                    count += 1
                    visited[i][j] = True
                    visitNeighbors(i, j)
                else:
                    visited[i][j] = True

        return count
        
```

Here is another way, reusing the grid:
```
def numIslands(self, grid: List[List[str]]) -> int:
	result = 0
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] != "1":
				continue
			result += 1
			self.fillIsland(grid, row, col)
	return result

def fillIsland(self, grid, i, j):
	queue = {(i, j)}
	while queue:
		y, x = queue.pop()
		if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != "1":
			continue
		grid[y][x] = "#"
		queue.update({(y+1, x), (y-1, x), (y, x+1), (y, x-1)})
```
