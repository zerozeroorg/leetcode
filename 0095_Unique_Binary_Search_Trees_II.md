### 95. Unique Binary Search Trees II
Medium

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order. 

**Example 1:**
```
1
  3
2

1
  2
    3

  2
1   3

    3
  2
1

  3
1
  2

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
```

**Example 2:**
```
Input: n = 1
Output: [[1]]
``` 

**Constraints:**
```
1 <= n <= 8
``` 

**Tags**
- Dynamic Programming
- Backtracking
- Tree
- Binary Search Tree
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
            Setup a recursive helper
            that takes a sorted list of numbers
            and generates the unique BSTs
            
            Run and return the recursive helper for list [1...n]
        """
        def helper(nums):
            if not nums:
                return [None]
            result = []
            for i in range(len(nums)):
                left_trees = helper(nums[0:i])
                right_trees = helper(nums[i+1:])
                
                for left in left_trees:
                    for right in right_trees:
                        result.append(TreeNode(nums[i], left, right))
            
            return result
        
        return helper([i for i in range(1, n + 1)])
                        
        
        
```
