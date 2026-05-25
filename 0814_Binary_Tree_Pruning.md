### 814. Binary Tree Pruning
Medium

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node. 

**Example 1:**
```
1
   0
 0   1

BECOMES:
1
   0
      1

Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```

**Example 2:**
```
        1
    0       1
0     0   0     1

BECOMES:

        1
            1
               1

Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```

**Example 3:**
```
        1
    1       0
  1   1   0   1
0

BECOMES:

      1
  1       0
1   1       1


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
``` 

**Tags**
- Tree
- Depth-First Search
- Binary Tree

**Constraints:**
```
The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
```


### Solution
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """
            Create a helper function, called hasSubtreeOne:
            - If node is None, return False
            - If node doesn't have children, return node.val == 1
            - Get hasSubtreeOne(node.left)
            - Get hasSubtreeOne(node.right)
            - If left doesn't have subtree with ones, then set node.left = None
            - Do the same as the right
            - Return result of hasSubtreeOne(left) || hasSubtreeOne(right) || node.val == 1
        """
        def has_subtree_ones(node):
            if node is None:
                return False
            
            left_result = has_subtree_ones(node.left)
            right_result = has_subtree_ones(node.right)
            if not left_result:
                node.left = None
            if not right_result:
                node.right = None
            
            return left_result or right_result or node.val == 1
    
        result = has_subtree_ones(root)
        if not result:
            return None
        return root
        
```
