### 226. Invert Binary Tree
Easy

Invert a binary tree.

**Example:**
```
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

Trivia:
```
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
```

**Tags**
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

### Solution:
- If my root is null, return
- If I have a left subtree, recursively invert
- If I have a right subtree, recursively invert
- Switch left and right subtrees
- return root

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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (!root) {
        return root;
    }
    
    if (root.left) {
        invertTree(root.left);
    }
    
    if (root.right) {
        invertTree(root.right);
    }
    
    let tempLeft = root.left;
    let tempRight = root.right;
    root.left = tempRight;
    root.right = tempLeft;    
    
    return root;
};
```
