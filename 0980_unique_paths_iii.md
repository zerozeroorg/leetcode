### 980. Unique Paths III
Hard

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once. 

**Example 1:**
```
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```

**Example 2:**
```
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
```

**Example 3:**
```
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
``` 

**Constraints**
```
m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
```

**Tags**
- Revisit
- Array
- Backtracking
- Bit Manipulation
- Matrix

### Solution:
- Python version is the latest version
- JS version is my original version
- For both versions, an optimization you can make is use a seen matrix and set it to True and then reset. Similar to Word Search II. But if you do this approach, you need to remember to set seen[startx][starty] = True before kicking off the recursion.
```
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
            Go through the grid and:
            - count empty spaces
            - find the starting square
            - find the ending square
            
            Then use recursion and DFS to find all paths that gets to the
            exit square. You have to brute force this. This will be exponential.
            
            HINT: hamiltonian path
        """
        empty_spaces = 0
        start_square = None
        end_square = None
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_square = (i, j)
                elif grid[i][j] == 2:
                    end_square = (i, j)
                elif grid[i][j] == 0:
                    empty_spaces += 1
        
        def helper(x, y, current_path):
            nonlocal total
            if (x, y) == end_square and len(current_path) - 2 == empty_spaces:
                total += 1
                return
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and
                   0 <= ny < cols and
                   grid[nx][ny] != -1 and
                   (nx, ny) not in current_path):
                    new_path = current_path.copy()
                    new_path.append((nx, ny))
                    helper(nx, ny, new_path)
        
        helper(start_square[0], start_square[1], [start_square])
        
        return total
                 
            
            
        
```

- Whenever we see the context of grid traversal, the technique of backtracking or DFS (Depth-First Search) should ring a bell. Maybe DP as well.
- Use backtracking!
- I messed up on kicking off the helper, miscounting the number of zeroes, passing `coord[i], coord[j]` into the helper function inside nextPaths forEach
- Also, return once you find 2.
- I also terminated too early: if there are no zeroes, doesn't mean a path [[1,2]] does not exist. The answer in that scenario is 1!

```
/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePathsIII = function(grid) {
    // count number of zeroes
    let numZeroes = 0;
    let startCoord = [];
    
    for (let i = 0; i < grid.length; i++) {
        let row = grid[i];
        for (let j = 0; j < row.length; j++) {
            let cell = grid[i][j];
            if (cell === 0) {
                numZeroes += 1;
            }
            if (cell === 1) {
                startCoord = [i, j];
            }
        }
    }
    
    let pathes = 0;
    
    let helper = (i, j, path) => {
        if (grid[i][j] === 2 && path.length === numZeroes + 2) {
            pathes += 1;
            return;
        }
        
        let nextPaths = [];
        if (grid[i - 1] && grid[i - 1][j] !== undefined && grid[i - 1][j] !== -1 &&
            !path.find(coord => coord[0] === i - 1 && coord[1] === j)) {
            nextPaths.push([i - 1, j]);
        }
        if (grid[i + 1] && grid[i + 1][j] !== undefined && grid[i + 1][j] !== -1 &&
            !path.find(coord => coord[0] === i + 1 && coord[1] === j)) {
            nextPaths.push([i + 1, j]);
        }
        if (grid[i] && grid[i][j - 1] !== undefined && grid[i][j - 1] !== -1 &&
            !path.find(coord => coord[0] === i && coord[1] === j - 1)) {
            nextPaths.push([i, j - 1]);
        }
        if (grid[i] && grid[i][j + 1] !== undefined && grid[i][j + 1] !== -1 &&
            !path.find(coord => coord[0] === i && coord[1] === j + 1)) {
            nextPaths.push([i, j + 1]);
        }        
        nextPaths.forEach(coord => {
            let newPath = [...path, coord];
            helper(coord[0], coord[1], newPath);
        });
    };
    
    helper(startCoord[0], startCoord[1], [startCoord]);
    
    return pathes;
};
```
