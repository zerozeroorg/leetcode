### 174. Dungeon Game
Hard

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned. 

**Example 1:**
```
 -2  -3   3
 -5 -10   1
 10  30  -5

Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
```

**Example 2:**
```
Input: dungeon = [[0]]
Output: 1
``` 

**Constraints:**
```
m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
```

**Tags**
- Revisit
- Array
- Dynamic Programming
- Matrix

### Solution
```
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
            This is a case where finding the best path going from
            either top left corner to bottom right corner is asymmetric
            to going from bottom right corner to the top left corner.
            
            For this case, it is best to go from the bottom right corner
            and build up the best solution.
        """
        rows = len(dungeon)
        cols = len(dungeon[0])
        lookup = [[None for _ in range(cols)] for _ in range(rows)]
        
        def get_min(x, y):
            current = dungeon[x][y]
            if x == rows - 1 and y == cols - 1:
                if current >= 0:
                    return 1
                else:
                    return -current + 1
                
            if lookup[x][y] is not None:
                return lookup[x][y]
            
            best = float('inf')
            # try going to the right
            if y + 1 < cols:
                min_right = get_min(x, y + 1)
                if current >= min_right:
                    best = min(best, 1)
                else:
                    best = min(best, min_right - current) # no need to +1 that is done in best case above
            
            # try going down
            if x + 1 < rows:
                min_down = get_min(x + 1, y)
                if current >= min_down:
                    best = min(best, 1)
                else:
                    best = min(best, min_down - current) # no need to +1 that is done in best case above
            
            lookup[x][y] = best
            return best
        
        return get_min(0, 0)
```
