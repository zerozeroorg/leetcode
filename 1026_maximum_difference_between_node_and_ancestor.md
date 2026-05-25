### 1026. Maximum Difference Between Node and Ancestor
Medium

Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B. 

**Example 1:**
```
      8
  3     10
1   6      14
  4   7  13
  
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

**Example 2:**
```
1
  2
    0
  3
Input: root = [1,null,2,null,0,3]
Output: 3
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105

**Tags**
- Revisit
- Tree
- Depth-First Search
- Binary Tree

```

### Solution:
- Brute force: For each node, get the max diff of its value and its children. Runtime: O(n^2)
- Easier solution: find the min and max value of each subtree!

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """
            For each subtree:
            find the minimum value and maximum value of its descendants.
            Use that to calculate maxDiff.
        """
        maxDiff = 0
        
        def getMinMax(node):
            nonlocal maxDiff
            if node is None:
                return
            minMax = (node.val, node.val)
            
            if node.left is None and node.right is None:
                return minMax
            
            if node.left:
                vals = getMinMax(node.left)
                maxDiff = max(maxDiff, abs(node.val - vals[0]))
                maxDiff = max(maxDiff, abs(node.val - vals[1]))
                minMax = (min(minMax[0], vals[0]), max(minMax[1], vals[1]))
                
            if node.right:
                vals = getMinMax(node.right)
                maxDiff = max(maxDiff, abs(node.val - vals[0]))
                maxDiff = max(maxDiff, abs(node.val - vals[1]))
                minMax = (min(minMax[0], vals[0]), max(minMax[1], vals[1]))
            
            return minMax
        
        ans = getMinMax(root)
        return maxDiff
        
```
