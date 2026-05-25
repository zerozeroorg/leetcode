### 114. Flatten Binary Tree to Linked List
Medium

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
**Example 1:**
```
      1
  2       5
3   4       6

BECOMES:
1
  2
    3
      4
        5
          6
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

**Example 2:**
```
Input: root = []
Output: []
```

**Example 3:**
```
Input: root = [0]
Output: [0]
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
``` 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

**Tags**
- Linked List
- Stack
- Tree
- Depth-First Search
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return [None, None]
            if not node.left and not node.right:
                return [node, node]
            
            left_list = helper(node.left)
            right_list = helper(node.right)
            
            node.left = None
            node.right = None
            
            if left_list[0]:
                node.right = left_list[0]
                if right_list[0]:
                    left_list[1].right = right_list[0]
                    return [node, right_list[1]]
                else:
                    return [node, left_list[1]]
            else:
                node.right = right_list[0]
                return [node, right_list[1]]
    
        helper(root)
        
```
