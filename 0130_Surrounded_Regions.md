### 130. Surrounded Regions
Medium

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region. 

**Example 1:**
```
["X","X","X","X"]
["X","O","O","X"]
["X","X","O","X"]
["X","O","X","X"]

["X","X","X","X"]
["X","X","X","X"]
["X","X","X","X"]
["X","O","X","X"]

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
```

**Example 2:**
```
Input: board = [["X"]]
Output: [["X"]]
``` 

**Constraints:**
```
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
```

**Tags**
- Array
- Depth-First Search
- Breadth-First Search
- Union-Find
- Matrix

### Solution
- The key to solving this is this hint: "Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'"
- Create a safe matrix that shows which O's are safe from turning into X.
- Create a queue of O's and add O's that are on the border of the matrix. Mark them as safe.
- Then for each O in the queue, get any directional O's and mark them safe. Then add them in the queue if not already added.
- Then iterate the board again and flip any non safe cells to X's.
```
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        safe = [[False for _ in range(cols)] for _ in range(rows)]
        border_o = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for j in range(cols):
            if board[0][j] == 'O':
                border_o.append((0,j))
                safe[0][j] = True
            if board[rows - 1][j] == 'O':
                border_o.append((rows - 1,j))
                safe[rows - 1][j] = True
        
        for i in range(rows):
            if board[i][0] == 'O':
                border_o.append((i, 0))
                safe[i][0] = True
            if board[i][cols - 1] == 'O':
                border_o.append((i, cols - 1))
                safe[i][cols - 1] = True
                
        
        while border_o:
            x, y = border_o.pop(-1)
            for dx, dy in directions:
                nx, ny = (dx + x, dy + y)
                if 0 <= nx < rows - 1 and 0 <= ny < cols - 1 and board[nx][ny] == 'O' and not safe[nx][ny]:
                    safe[nx][ny] = True
                    border_o.append((nx, ny))
        
        for i in range(rows):
            for j in range(cols):
                if not safe[i][j]:
                    board[i][j] = 'X'
                    
        
```
