### 994. Rotting Oranges
Medium

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

**Example 1:**
```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**
```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**
```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
``` 

**Note:**
```
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
```

**Tags**
- Array
- Breadth-First Search
- Matrix

### Solution:
- Push all rotting oranges into the bfs array
- If not rotting oranges, return 0.
- For each rotting orange in the dfs array:
- Take all of its neighbors
- Rot them
- Then push those rotting oranges into the bfs array
- Increment the count only after you rot all neighboring oranges. I probably use a tuple that stores the time with the rotting orange
- When the bfs array is empty, we have to have one more matrix loop to see if there are anymore fresh oranges. If there are, then return -1.
- Return the time

```
/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    // idea: use bfs
    // create a queue with the coordinate and minute
    let bfs = [];
    let time = 0;
    let rows = grid.length;
    let cols = grid[0].length;
    
    for (let i = 0; i < grid.length; i++) {
        let row = grid[i];
        for (let j = 0; j < row.length; j++) {
            if (grid[i][j] === 2) {
                bfs.push([[i, j], 0]);  // coords and minute
            }
        }
    }
    
    while(bfs.length) {
        let node = bfs.shift();
        let coords = node[0];
        let minute = node[1];
        time = Math.max(time, minute);
        // get the 4 directions
        let above = [coords[0] - 1, coords[1]];
        let left = [coords[0], coords[1] - 1];
        let right = [coords[0], coords[1] + 1];
        let below = [coords[0] + 1, coords[1]];
        
        [above, left, right, below].forEach(direction => {
            if (grid[direction[0]] && 
                grid[direction[0]][direction[1]] && 
                grid[direction[0]][direction[1]] === 1) {
                grid[direction[0]][direction[1]] = 2;
                bfs.push([direction, minute + 1]);
            }            
        });
        
    }
    for (let i = 0; i < grid.length; i++) {
        let row = grid[i];
        for (let j = 0; j < row.length; j++) {
            if (grid[i][j] === 1) {
                return -1;
            }
        }
    }
    return time;
    // push all the rotten oranges in there
    // iterate and mark the fresh oranges as rotten and push them 
    // once stack is empty, end loop
    // go through the array and check if there are any fresh oranges
    
};
```

Here is the Java Solution:
```
class Solution {
    public int orangesRotting(int[][] grid) {
        /**
            - Have a bfs array
            - Have a max minute count
            - Go through all grid and push all rotten oranges
            - While there is a bfs array length:
                - take the next rotten orange
                - get the four directional oranges and rot them and push to bfs array
            - Go through the grid again to see if there are any fresh oranges
            - If there are, return -1, else return max minute count
         */
        ArrayList <int[]> bfs = new ArrayList<>();
        int rows = grid.length;
        int cols = grid[0].length;
        int minutes = 0;
        int[][] directions = {
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1}
        };
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 2) {
                    int[] tuple = {i, j, 0};
                    bfs.add(tuple);
                }
            }
        }
        
        while(bfs.size() > 0) {
            int[] tuple = bfs.remove(0);
            int[] coords = {tuple[0], tuple[1]};
            minutes = Math.max(tuple[2], minutes);
            
            for (int i = 0; i < directions.length; i++) {
                int[] direction = directions[i];
                int[] newDirection = {coords[0] + direction[0], coords[1] + direction[1]};
                if (newDirection[0] >= 0 && 
                    newDirection[0] < rows && 
                    newDirection[1] >= 0 && 
                    newDirection[1] < cols && 
                    grid[newDirection[0]][newDirection[1]] == 1) {
                    grid[newDirection[0]][newDirection[1]] = 2;
                    int[] newTuple = {newDirection[0], newDirection[1], tuple[2] + 1};
                    bfs.add(newTuple);
                }
            }
        }
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }
        
        return minutes;
    }
}
```
The best python solution
- In first loop, look for all the fresh and rotten oranges
- Then loop over the rotten oranges and check if any of its neighbors is in the fresh oranges group. If it is, remove it from fresh oranges group.
- If there are still any fresh oranges, return -1
```
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit, curr = set(), deque()
		# find all fresh and rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        result = 0
        while visit and curr:
			# BFS iteration
            for _ in range(len(curr)):
                i, j = curr.popleft()  # obtain recent rotten orange
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in visit:  # check if adjacent orange is fresh
                        visit.remove(coord)
                        curr.append(coord)
            result += 1
		# check if fresh oranges remain and return accordingly
        return -1 if visit else result
```
