### 113. Path Sum II
Medium

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children. 

**Example 1:**
```
          5
      4      8
  11      13    4
7   2         5   1
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
```

**Example 2:**
```
Input: root = [1,2,3], targetSum = 5
Output: []
```

**Example 3:**
```
Input: root = [1,2], targetSum = 0
Output: []
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
```

**Tags**
- Backtracking
- Tree
- Depth-First Search
- Binary Tree

### Solution
- I changed my implementation from recursively sending paths to just storing the paths in a global variable.
- There were issues with my initial implementation. If I reach a null root, I was adding the path twice!
- Example: if I am at left node 2, and I get path sum of left and right, I was essentially adding the path twice.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """
            Need this helper function:
            Get the pathSum of left by target - root
            Get the pathSum of right by target - root
            If any of length, then add root to the list
            return those pathsums
            
            Termination:
            - if root is undefined and target == 0, return path
        """
        self.result = []
        def helper(root, targetSum, path):
            if root is None:
                return
            
            if not root.left and not root.right:
                if targetSum - root.val == 0:
                    self.result.append(path + [root.val])
                    return
            
            if root.left:
                helper(root.left, targetSum - root.val, path + [root.val])
            
            if root.right:
                helper(root.right, targetSum - root.val, path + [root.val])
        
        
        helper(root, targetSum, [])
        return self.result
        
```
