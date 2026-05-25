### 1339. Maximum Product of Splitted Binary Tree
Medium

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it. 

**Example 1:**
```
      1
  2       3
4   5   6

Split it at the 2 - 1 edge:
  2
4   5

1
  3
6

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
```

**Example 2:**
```
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
```

**Example 3:**
```
Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
```

**Example 4:**
```
Input: root = [1,1]
Output: 1
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
            Get the sum of the entire tree
            Then for each node -
            - subtract its subtree from the sum
            - multiply them together
            - get the max of all these values
            return max
        """
        subtrees = []
        modulo = 10**9 + 7
        
        def get_subtree_sums(node):
            if not node:
                return 0
            left = get_subtree_sums(node.left)
            right = get_subtree_sums(node.right)
            subtree_total = node.val + left + right
            subtrees.append(subtree_total)
            return subtree_total
    
        get_subtree_sums(root)        
        total = max(subtrees)
        result = float('-inf')
        
        for subtree in subtrees:
            subtree2 = total - subtree
            result = max(result, subtree * subtree2)
        
        return result % modulo
        
```
