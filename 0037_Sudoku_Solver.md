### 37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
 
**Example 1:**
```
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
```

**Constraints:**
```
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
```

**Tags**
- Array
- Hash Table
- Backtracking
- Matrix

### Solution
- Must parse string "9" to 9!
- Must check for blanks! Got a type error when doing int(".") 
- Forgot to push the blank back to the blanks when there are no possibilities
```
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
            Get all the cells with dots
            Then iterate through each of them:
            - get all possible numbers for that cell
            - pick the first one and mark the board
            - check if is valid removing that cell from the list
            - if not valid, then test the next cell
            return board
        """
        blanks = collections.deque([])
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    blanks.append((i, j))
        
        def get_bounds(i):
            if 0 <= i <= 2:
                return 0
            if 3 <= i <= 5:
                return 3
            return 6

        def get_all_possibilties(i, j):
            possible = set([1,2,3,4,5,6,7,8,9])
            row = board[i]
            for num in row:
                if num == ".":
                    continue
                intnum = int(num)
                if intnum in possible:
                    possible.remove(intnum)
            for row in board:
                if row[j] == ".":
                    continue
                introw = int(row[j])
                if introw in possible:
                    possible.remove(introw)
            row = get_bounds(i)
            col = get_bounds(j)
            
            for x in range(row, row + 3):
                for y in range(col, col + 3):
                    if board[x][y] == ".":
                        continue
                    num = int(board[x][y])
                    if num in possible:
                        possible.remove(num)

            return possible
        
        def recurse(board, blanks):
            if not blanks:
                return True
            (x, y) = blanks.popleft()
            possible_set = get_all_possibilties(x, y)
            if not possible_set:
                blanks.appendleft((x, y))
                return False
            for num in possible_set:
                board[x][y] = str(num)
                if recurse(board, blanks):
                    return True
            board[x][y] = "."
            blanks.appendleft((x,y))
            return False
            
    
        recurse(board, blanks)
        
```
