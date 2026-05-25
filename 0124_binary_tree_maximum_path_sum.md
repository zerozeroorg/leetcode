### 124. Binary Tree Maximum Path Sum
Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

**Example 1:**
```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

**Example 2:**
```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

**Tags**
- Dynamic Programming
- Tree
- Depth-First Search
- Binary Tree

### Solution:
```
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var max = null;
var maxPathSumHelper = function(root) {
    if (!root) {
        return 0;
    }
    
    let leftSum = Math.max(maxPathSumHelper(root.left), 0);
    let rightSum = Math.max(maxPathSumHelper(root.right), 0);
    
    let leftAndRoot = leftSum + root.val;
    let rightAndRoot = rightSum + root.val;
    let leftRightVal = root.val + leftSum + rightSum;
    
    max = Math.max(max, leftRightVal);
    return Math.max(leftAndRoot, rightAndRoot);
};
var maxPathSum = function(root) {
    max = Number.MIN_SAFE_INTEGER;
    maxPathSumHelper(root);
    return !root ? 0 : max;
};
```
