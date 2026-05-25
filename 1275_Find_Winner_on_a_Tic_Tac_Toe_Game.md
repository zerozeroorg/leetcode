### 1275. Find Winner on a Tic Tac Toe Game
Easy

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

**Example 1:**
```
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
X 
  X
O O X
```

**Example 2:**
```
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
X X O
X O
O
```
**Example 3:**
```
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
```
**Example 4:**
```
Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
``` 

**Constraints:**
```
1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
```

**Tags**
- Array
- Hash Table
- Matrix
- Simulation

### Solution
```
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
            There has to be at least 5 moves recorded before a winner is determined
            For move in moves:
            When the user makes a play, check if the point is connected to anything.
            If it is, return that player.
            
            Return draw if there are no more moves, Pending otherwise
            
            Strategy: for the (x,y) the user selects, just check its row only, its column only,
            and both diagnonals. 
        """
        length = len(moves)
        
        if length < 5:
            return "Pending"
        
        grid = [[None for i in range(0, 3)] for j in range(0, 3)]
        
        def is_winner(x, y, current):
            # check my row
            row = grid[x]
            if row[0] == current and row[1] == current and row[2] == current:
                return True
            # check my column
            if grid[0][y] == current and grid[1][y] == current and grid[2][y] == current:
                return True
            
            # check diagonal
            if grid[0][0] == current and grid[1][1] == current and grid[2][2] == current:
                return True
            if grid[2][0] == current and grid[1][1] == current and grid[0][2] == current:
                return True

            
            return False
        
        current = "X"
        count = 0
        for [x, y] in moves:
            count += 1
            grid[x][y] = current
            
            if count >= 5 and is_winner(x, y, current):
                return "A" if current == "X" else "B"

            # change current
            current = "O" if current == "X" else "X"
        
        return "Draw" if length == 9 else "Pending"
        
```
