### 222. Count Complete Tree Nodes
Easy

Given a complete binary tree, count the number of nodes.

**Note:**

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

**Example:**
```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```

**Tags**
- Binary Search
- Bit Manipulation
- Tree
- Binary Tree

### Solution:
- I originally though you had to use BFS to count the number of nodes. But there is an easier way!
- If my root is null, return 0
- Get the number of nodes on the left
- Get the number of nodes on the right
- Return left + right + 1

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
var countNodes = function(root) {
    if (!root) {
        return 0;
    }
    
    let leftCount = countNodes(root.left);
    let rightCount = countNodes(root.right);
    return leftCount + rightCount + 1;
};
```
