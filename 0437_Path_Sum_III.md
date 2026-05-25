### 437. Path Sum III
Medium

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes). 

**Example 1:**
```
        10
     5      -3
  3     2       11
3   -2    1
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
[5,3]
[5,2,1]
[-3,11]
```

**Example 2:**
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000
```


**Tags**
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def helper(node, sum_so_far, paths):
            if not node:
                return paths
            
            sum_so_far += node.val
            if sum_so_far == targetSum:
                paths += 1
            
            paths = helper(node.left, sum_so_far, paths)
            paths = helper(node.right, sum_so_far, paths)
            return paths
        
        total = helper(root, 0, 0)
        total += self.pathSum(root.left, targetSum)
        total += self.pathSum(root.right, targetSum)
        
        return total
        
```
