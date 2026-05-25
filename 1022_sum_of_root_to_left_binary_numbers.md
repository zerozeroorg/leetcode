### 1022. Sum of Root To Leaf Binary Numbers
Easy

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

**Example 1:**
```
      1
  0       1
0   1   0   1


Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
``` 

**Note:**
```
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
```

**Tags**
- Tree
- Depth-First Search
- Binary Tree

### Solution:
- Ugh, i messed up root vs node in the sumHelper!
- Ugh, I did not spread the new array. Arrays are passed by reference

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
var sumRootToLeaf = function(root) {
    function sumHelper(node, vals) {
        if (!node) {
            return 0;
        }
        
        vals.push(node.val);
        
        if (!node.left && !node.right) {
            return parseInt(vals.join(''), 2);
        }
        
        let leftSum = 0;
        let rightSum = 0;
        if (node.left) {
            leftSum = sumHelper(node.left, [...vals]);
        }
        if (node.right) {
            rightSum = sumHelper(node.right, [...vals]);
        }
        
        return leftSum + rightSum;
    }
    
    return sumHelper(root, []);
};
```
