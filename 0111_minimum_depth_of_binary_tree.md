### 111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

**Example 1:**
```
    3
  9   20
    15   7

Input: root = [3,9,20,null,null,15,7]
Output: 2
```

**Example 2:**
```
2
  3
    4
      5
        6
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
```

**Tags**
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
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        depths = []
        if root.left:
            depths.append(self.minDepth(root.left))
        if root.right:
            depths.append(self.minDepth(root.right))
            
        min_depth = min(depths)
        
        return 1 + min_depth
        
```
