### 133. Clone Graph
Medium

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
```
class Node {
    public int val;
    public List<Node> neighbors;
}
``` 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
```
1 --- 2
|     |
4---- 3

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

**Example 2:**
```
1 # just one node

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

**Example 3:**
```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

**Example 4:**
```
1 --- 2

Input: adjList = [[2],[1]]
Output: [[2],[1]]
``` 

**Constraints:**
```
1 <= Node.val <= 100
Node.val is unique for each node.
Number of Nodes will not exceed 100.
There is no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
```


**Tags**
- Hash Table
- Depth-First Search
- Breadth-First Search
- Graph Theory

### Solution:
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        I need a dictionary to keep track of all the nodes
        I have created
        
        I will use DFS and a helper function to create the nodes
        
        I think recursion will help me create subgraphs maybe?
        
        The problem was that I was creating nodes without updating the dict
        
        Similar to DP, if it is in the dict, then return with that item and do nothing else
        """
        
        nodeDict = {}
        if node is None or node.val is 0:
            return node
        
        def cloneNode(node: 'Node') -> 'Node':
            val = node.val
            if nodeDict.get(val):
                return nodeDict.get(val)
            
            root = Node(val)
            nodeDict[val] = root

            for item in node.neighbors:
                root.neighbors.append(cloneNode(item))

            return root

        return cloneNode(node)
                
```
