### 785. Is Graph Bipartite?
Medium

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists. Each node is an integer between 0 and graph.length - 1. There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice. 

**Example 1:**
```
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.
```

**Example 2:**
```
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We cannot find a way to divide the set of nodes into two independent subsets.
``` 

**Constraints:**
```
1 <= graph.length <= 100
0 <= graph[i].length < 100
0 <= graph[i][j] <= graph.length - 1
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be undirected. 
```

**Tags**
- Depth-First Search
- Breadth-First Search
- Union-Find
- Graph Theory

### Solution:
- Use Graph coloring.
```
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
            Use graph coloring technique
            Iterate through each node:
            - If I am already colored, continue
            - Check if I can be colored with default alpha
            - If not, return false
            - go through neighbors and do opposite color via DFS
            At the end return true
        """
        colors = [None] * len(graph)
        alpha = 'a'
        beta = 'b'
        
        def can_color(index, newColor):
            queue = collections.deque([(index, newColor)])
            while queue:
                (node, color) = queue.popleft()
                colors[node] = color
                opposite = alpha if color is beta else beta
                
                for neighbor in graph[node]:
                    if colors[neighbor] is None:
                        queue.append((neighbor, opposite))
                    elif colors[neighbor] != opposite:
                        return False
            return True
                
        
        for node in range(len(graph)):
            if colors[node] is not None:
                continue
            
            if not can_color(node, alpha):
                return False
        
        return True
        
        
```
