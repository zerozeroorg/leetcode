### 79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
 

**Example 1:**
```
A B C E
S F C S
A D E E

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**
```
A B C E
S F C S
A D E E

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**
```
A B C E
S F C S
A D E E

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
``` 

**Constraints:**
```
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
``` 

Follow up: Could you use search pruning to make your solution faster with a larger board?

**Tags**
- Revisit
- Array
- String
- Backtracking
- Depth-First Search
- Matrix

### Solution
Very hard problem for me, will need to revisit
here are the test cases i failed previously
```
[["a","b","c"],["a","e","d"],["a","f","g"]]
"abcdefg"
[["a"]]
a
[["a", "a"]]
aaa
```
A neat optimization:
- Have a global visited 2D matrix, all initially set to False
- As you visit a cell in the recursive function, set that cell to True
- At the end of the recursive function, before exiting, set visited to False
- That way, you are not creating a new set of visited cells each time

```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        roots = []
        length = len(word)
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        roots = []

        def recurse(current, next_ptr, visited):
            if next_ptr == length:
                return True
         
            for delta in deltas:
                next_position = (current[0] + delta[0], current[1] + delta[1])
                if (0 <= next_position[0] < rows and 
                    0 <= next_position[1] < cols and 
                    board[next_position[0]][next_position[1]] == word[next_ptr] and 
                    next_position not in visited):
                        if recurse(next_position, next_ptr + 1, visited | {next_position}):
                            return True
            
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    roots.append((i, j))
        
        if not roots:
            return False
        
        for root in roots:
            if recurse(root, 1, {root}):
                return True
        
        return False
        
    

            
            
            
```
