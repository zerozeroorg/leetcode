### 289. Game of Life
Medium

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state. 

**Example 1:**
```
[0,1,0]
[0,0,1]
[1,1,1]
[0,0,0]

Becomes:

[0,0,0]
[1,0,1]
[0,1,1]
[0,1,0]

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

**Example 2:**
```
[1,1]
[1,0]

Becomes:

[1,1]
[1,1]

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
``` 

**Constraints:**
```
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
``` 

**Follow up:**
Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.

In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

**Tags**
- Array
- Matrix
- Simulation

### Solution
```
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
    /*
        To change it in place, we will have 4 states:
        0
        1
        2 (means it was 0 but changed to 1)
        3 (means it was 1 but changed to 0)
        
        We iterate and based on the cell's state and its neighbors, 
        we determine its new state.
        
        Then we go through the matrix again and clean up 2s and 3s
    */
    
    const rows = board.length;
    const cols = board[0].length;
    const deltas = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]];
    
    const setNewState = (i, j) => {
        let liveNeighbors = 0;
        for (const delta of deltas) {
            let neighbor = [delta[0] + i, delta[1] + j];
            if (0 <= neighbor[0] && 
                neighbor[0] < rows && 
                0 <= neighbor[1] && 
                neighbor[1] < cols &&
               (board[neighbor[0]][neighbor[1]] === 1 || board[neighbor[0]][neighbor[1]] === 3)) {
                liveNeighbors += 1;    
            }
        }
        
        if (board[i][j] === 1 || board[i][j] === 3) {
            if (liveNeighbors < 2 || liveNeighbors > 3) {
                board[i][j] = 3;
            }
        } else if (board[i][j] === 0 || board[i][j] === 2) {
            if (liveNeighbors === 3) {
                board[i][j] = 2;
            }
        } 
    };
    
    
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            setNewState(i, j);
        }
    }
    
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const cell = board[i][j];
            if (cell === 2) {
                board[i][j] = 1;
            }
            if (cell === 3) {
                board[i][j] = 0;
            }
        }
    } 
};
```
