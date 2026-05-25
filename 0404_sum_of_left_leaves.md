### 404. Sum of Left Leaves
Easy

Find the sum of all left leaves in a given binary tree.

**Example:**
```
    3
   / \
  9  20
    /  \
   15   7
```
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

**Tags**
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

### Solution:
- Iterate through the tree
- If I have a left leaf, add me to the list
- Find left leaves for my children

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
var sumOfLeftLeaves = function(root) {
    let sum = 0;
    if (!root || (!root.left && !root.right)) {
        return 0;
    }
    
    let left = root.left;
    let right = root.right;
    
    // only a left child
    if (left && !left.left && !left.right) {
        sum += left.val;
    } else {
        sum += sumOfLeftLeaves(left);
    }
    
    sum += sumOfLeftLeaves(right);
    return sum;
};
```
