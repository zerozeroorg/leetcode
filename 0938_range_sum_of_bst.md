### 938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

**Example 1:**
```
    10
  5     15
3   7     18
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
```

**Example 2:**
```
        10
    5       15
  3   7    13  18
1  6
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
```

**Tags**
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

### Solution:
- There is an optimization: you do not need to search in a subtree if that subtree has values less than low or greather than high.
- I did not code that optimization but should be easy to add.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
            check if the current node is in range
            if it is, add it
            
            add the range sum of the left
            add the range sum of the right
            
            return total
        """
        if root is None:
            return 0
        
        sum = 0
        if low <= root.val <= high:
            sum += root.val
        
        sum += self.rangeSumBST(root.left, low, high)
        sum += self.rangeSumBST(root.right, low, high)
        
        return sum
```
