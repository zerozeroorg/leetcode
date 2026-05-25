### 827. Making A Large Island
Hard

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
 

**Example 1:**
```
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
```

**Example 2:**
```
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
```

**Example 3:**
```
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
``` 

**Constraints:**
```
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
```

**Tags**
- Array
- Depth-First Search
- Breadth-First Search
- Union-Find
- Matrix

### Solution
```
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
            Similar to finding all connected components in a graph
            - Use BFS for each 1s and mark them with a different island counter
            - Do this until all 1s are marked
            
            Find the max size of any connected component and set it currMax
            
            Then go through the matrix looking for zeroes and do the following:
            - check if there are any 1s in the left, right, above below me.
            - if there isn't skip
            - if there are, count the 1s and update currMax
            
            Return currMax
        """
        self.currMax = 0
        self.islandMarker = 1
        rows = cols = len(grid)
        islandMap = {}
        islandGrid = [[None for i in range(rows)] for j in range(cols)]
        
        def bfs(i, j, islandGrid, islandMap):
            count = 0
            queue = collections.deque([(i, j)])
            while len(queue):
                coord = queue.popleft()
                if islandGrid[coord[0]][coord[1]] is None:
                    islandGrid[coord[0]][coord[1]] = self.islandMarker
                    count += 1
                else:
                    continue
                for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newCoord = (coord[0] + delta[0], coord[1] + delta[1])
                    if 0 <= newCoord[0] < rows and 0 <= newCoord[1] < cols and islandGrid[newCoord[0]][newCoord[1]] is None and grid[newCoord[0]][newCoord[1]] == 1:
                        queue.append(newCoord)
            islandMap[self.islandMarker] = count
            self.currMax = max(self.currMax, islandMap[self.islandMarker])
            self.islandMarker += 1
            
        def flipZero(i, j):
            count = 1
            keySet = set([])
            for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newCoord = (i + delta[0], j + delta[1])
                if 0 <= newCoord[0] < rows and 0 <= newCoord[1] < cols and grid[newCoord[0]][newCoord[1]] == 1 and islandGrid[newCoord[0]][newCoord[1]] is not None:
                    keySet.add(islandGrid[newCoord[0]][newCoord[1]])
            for key in keySet:
                count += islandMap[key]
            self.currMax = max(self.currMax, count)
            
        # Connected component algorithm
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and islandGrid[i][j] is None:
                    bfs(i, j, islandGrid, islandMap)
                    
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    flipZero(i, j)
        return self.currMax
        
```
