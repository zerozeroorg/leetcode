### 1584. Min Cost to Connect All Points
Medium

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points. 

**Example 1:**
```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**
```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
``` 

**Constraints:**
```
1 <= points.length <= 1000
-10^6 <= xi, yi <= 10^6
All pairs (xi, yi) are distinct.
```

**Tags**
- revisit
- Array
- Union-Find
- Graph Theory
- Minimum Spanning Tree

### Solution
```
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            Need to apply Prim's lazy algorithm
            which requires a Priority Queue so must
            use python for now
            
            First, calculate cost of all edges
            then apply Prim's algorithm
        """
        lookup = {}
        visited = set()
        ans = 0
        
        for (x1, y1) in points:
            for (x2, y2) in points:
                key = (x1, y1, x2, y2)
                cost = abs(x1 - x2) + abs(y1 - y2)
                lookup[key] = cost
        
        
        pq = []
        first = points[0]
        
        for i in range(1, len(points)):
            second = points[i]
            key = (first[0], first[1], second[0], second[1])
            pq.append((lookup[key], first[0], first[1], second[0], second[1]))
        
        heapq.heapify(pq)
        visited.add((first[0], first[1]))
        
        while len(pq):
            (cost, x1, y1, x2, y2) = heapq.heappop(pq)
            if (x2, y2) in visited:
                continue
            
            visited.add((x2, y2))
            ans += cost
            
            for point in points:
                if (point[0], point[1]) not in visited:
                    key = (x2, y2, point[0], point[1])
                    heapq.heappush(pq, (lookup[key], x2, y2, point[0], point[1]))
                
        return ans
```
