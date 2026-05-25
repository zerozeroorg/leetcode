### 865. Smallest Subtree with all the Deepest Nodes
Medium

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/


**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
```

**Example 1.5:**
```
Input: root = [3,5,1,6,2,0,8,11,12,7,4]
Output: [5,6,2,null,null,7,4]
11, 12, 7 and 4 are the deepest nodes. Their closest common parent is 5.
```

**Example 2:**
```
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
```

**Example 3:**
```
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
``` 

**Constraints:**
```
The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
```

**Tags**
- Hash Table
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

### Solution:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
            For each node in breadth first search:
            - Put them in a hash of node.val -> (depth, parent)
            - As you are traversing, keep a list of nodes with the largest depths
            
            You should have a list of nodes with the largest depths
            While this list is greater than 1:
            - pop all the elements of that list and get their parents as a set
            - add the parents to the list
            
            return the list[0]
        """
        lookup = {}
        bfs = [(root, None, 1)]
        maxDepth = 1
        
        while len(bfs):
            item = bfs.pop(0)
            node = item[0]
            lookup[node.val] = item
            maxDepth = max(maxDepth, item[2])
            if node.left:
                bfs.append((node.left, node, item[2] + 1))
            if node.right:
                bfs.append((node.right, node, item[2] + 1))
        
        parents = set()
        for key, val in lookup.items():
            if val[2] == maxDepth:
                parents.add(val[0])
        
        while len(parents) > 1:
            temp = set()
            for node in parents:
                temp.add(lookup[node.val][1])
            parents = temp
        
        return list(parents)[0]
        
        
```
