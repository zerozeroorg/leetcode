### 54. Spiral Matrix
Medium

Given an m x n matrix, return all elements of the matrix in spiral order.

**Example 1:**
```
1 2 3
4 5 6
7 8 9

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
1  2  3  4
5  6  7  8
9 10 11 12

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
``` 

**Constraints:**
```
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
```

**Tags**
- Array
- Matrix
- Simulation

### Solution
```
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            Start at 0,0
            Set direction = 'right'
            Set counter = m x n
            If counter == 0: break
            If direction is right, and I can go right and I have not visited yet:
            - go right, decrement counter
            Else change direction to down
            If direction is down, and I can go down and I have not visited yet:
            - go down, decrement counter
            Else change direction to left
            If direction is left....
            - go left, decrement counter
            Else change direction to up
            If direction is up...
            - go up, decrement counter
            Else change direction to right
        """
        direction = 'right'
        rows = len(matrix)
        cols = len(matrix[0])
        counter = rows * cols
        result = []
        start = (0, -1)
        
        def can_go_here(x, y):
            return 0 <= x < rows and 0 <= y < cols and matrix[x][y] != None
        
        def go_here(x, y):
            nonlocal result
            nonlocal counter
            nonlocal start
            nonlocal matrix
            result.append(matrix[x][y])
            counter -= 1
            start = (x, y)
            matrix[x][y] = None            
            
        
        while counter > 0:
            if direction == 'right':
                x = start[0]
                y = start[1] + 1
                if can_go_here(x,y):
                    go_here(x,y)
                    continue
                else:
                    direction = 'down'
                    continue
            if direction == 'down':
                x = start[0] + 1
                y = start[1]
                if can_go_here(x,y):
                    go_here(x,y)
                    continue
                else:
                    direction = 'left'
                    continue
            if direction == 'left':
                x = start[0]
                y = start[1] - 1
                if can_go_here(x,y):
                    go_here(x,y)
                    continue
                else:
                    direction = 'up'
                    continue
            if direction == 'up':
                x = start[0] - 1
                y = start[1]
                if can_go_here(x,y):
                    go_here(x,y)
                    continue
                else:
                    direction = 'right'
                    continue                    
                    
            
        return result
        
        
```
