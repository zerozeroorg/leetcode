### 543. Diameter of Binary Tree
Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them. 

**Example 1:**
```
     1
  2     3
4   5

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**
```
  1
2

Input: root = [1,2]
Output: 1
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
```

**Tags**
- Revisit
- Tree
- Depth-First Search
- Binary Tree

### Solution
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            Only the leaves matter.
            Think about collapsing the tree into levels.
            We get the max number of levels on the left and right.
            Then add it at the root to get the current root's diameter.
            Then return the max diameter of the root, the diameter at left, at right.
        """
        def recurse(current): # (diameter at node, max level)
            if not current.left and not current.right:
                return (0, 1)
            
            left_values = (0, 0)
            right_values = (0, 0)
            
            if current.left:
                left_values = recurse(current.left)
                
            if current.right:
                right_values = recurse(current.right)
            
            my_diameter = left_values[1] + right_values[1]
            max_level = max(left_values[1], right_values[1]) + 1
            return (max(my_diameter, left_values[0], right_values[0]), max_level)
        
        return recurse(root)[0]
            
            
        
```
