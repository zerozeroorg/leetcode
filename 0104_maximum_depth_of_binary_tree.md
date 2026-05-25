### 104. Maximum Depth of Binary Tree
Easy

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

**Example:**
```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
```

return its depth = 3.

**Tags**
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

### Solution:

**Straightforward Solution:**

First, break up the problem into a smaller subproblem: 1 tree node with two children. 

Get the maxDepth of the left + 1.

Get the maxDepth of the right + 1.

Then compare which one is bigger. Return the bigger one.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        
        return max(left, right)
```
