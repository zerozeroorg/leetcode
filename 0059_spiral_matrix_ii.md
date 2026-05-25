### 59. Spiral Matrix II
Medium

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

**Example 1:**
```
1 2 3
8 9 4
7 6 5

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
```

**Example 2:**
```
Input: n = 1
Output: [[1]]
``` 

**Constraints:**
```
1 <= n <= 20
```

**Tags**
- Array
- Matrix
- Simulation

### Solution:
```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        
        def canGoHere(x, y):
            if 0 <= x < n and 0 <= y < n and matrix[x][y] == 0:
                return True

            return False
        
        direction = 'right'
        x = y = 0
        count = 1
        while canGoHere(x, y):
            matrix[x][y] = count
            count += 1
            
            if direction is 'right':
                y += 1
            elif direction is 'down':
                x += 1
            elif direction is 'left':
                y -= 1
            else:
                x -= 1
            

            if not canGoHere(x, y):
                if direction is 'right':
                    direction = 'down'
                    y -= 1
                    x += 1
                    
                elif direction is 'down':
                    direction = 'left'
                    x -= 1
                    y -= 1
                    
                elif direction is 'left':
                    direction = 'up'
                    x -= 1
                    y += 1
                    
                else:
                    direction = 'right'
                    y += 1
                    x += 1
    
        
        return matrix
        
```
