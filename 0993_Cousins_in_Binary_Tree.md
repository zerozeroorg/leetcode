### 993. Cousins in Binary Tree
Easy

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
 

**Example 1:**
```
    1
  2   3
4

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```

**Example 2:**
```
     1
  2     3
    4     5

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
```

**Example 3:**
```
   1
2     3
  4

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
```

**Constraints:**
```
The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
```

**Tags**
- Tree
- Depth-First Search
- Breadth-First Search
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parentX = None
        depthX = 0
        parentY = None
        depthY = 0
        
        def search(node, parent, depth):
            nonlocal parentX
            nonlocal depthX
            nonlocal parentY
            nonlocal depthY
            if not node:
                return
            
            if node.val == x:
                depthX = depth
                parentX = parent
            elif node.val == y:
                depthY = depth
                parentY = parent
            
            search(node.left, node, depth + 1)
            search(node.right, node, depth + 1)
        
        
        search(root, None, 0)
        
        return parentX != parentY and depthX == depthY
            
                
            
        
```
