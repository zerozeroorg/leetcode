### 429. N-ary Tree Level Order Traversal
Medium

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples). 

**Example 1:**
```
         1
  3      2     4 
5   6
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```

**Example 2:**
```
        1
2     3     4      5
    6   7   8    9   10
        11  12   13
        14
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
``` 

**Constraints:**
```
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
```

**Tags**
- Tree
- Breadth-First Search

### Solution
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
            Use BFS -
            push the root node into the queue
            while the queue is not empty:
            - empty the queue
            - for each node in that queue, add its children into queue
            - add node into level array
            - after all nodes are processed, add level array into result array
            return result array
        """
        result = []
        if not root:
            return result
        queue = collections.deque([root])
        
        while queue:
            level = []
            nodes = queue.copy()
            queue.clear()
            for node in nodes:
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            result.append(level)
        
        return result
        
        
```
