### 36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

**Example 1:**
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```

**Example 2:**
```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
``` 

**Constraints:**
```
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
```

**Tags**
- Array
- Hash Table
- Matrix

### Solution
- use a set instead of a map to look for repetitions
```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            Brute force:
            - check each row and if there is a repetition, then return false
            - check each column and if there is a repetition, then return false
            - check each 3 x 3 grid. if there is a repetition, then return false
            - return true
        """
        rows = 9
        cols = 9
        def valid_row(row_num):
            row = board[row_num]
            lookup = {}
            for cell in row:
                if cell == ".":
                    continue
                if cell not in lookup:
                    lookup[cell] = True
                else:
                    return False
            return True
        
        def valid_col(col_num):
            lookup = {}
            for row in board:
                col = row[col_num]
                if col == ".":
                    continue
                if col not in lookup:
                    lookup[col] = True
                else:
                    return False
            return True
        
        def valid_grid(row, col):
            lookup = {}
            for x in range(row, row + 3):
                for y in range(col, col + 3):
                    cell = board[x][y]
                    if cell == ".":
                        continue
                    if cell not in lookup:
                        lookup[cell] = True
                    else:
                        return False
            return True
    
        for row in range(rows):
            if not valid_row(row):
                return False
        
        for col in range(cols):
            if not valid_col(col):
                return False
        
        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                if not valid_grid(row, col):
                    return False
                
        return True
        
        
                
        
```
