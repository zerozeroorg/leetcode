### 543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
```
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
```

Note: The length of path between two nodes is represented by the number of edges between them.

### Solution:
```
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var getHeight = function(node) {
    if (!node) {
        return 0;
    }
    
    return 1 + Math.max(getHeight(node.left), getHeight(node.right));
}

var diameterOfBinaryTree = function(root) {
    if (!root) {
        return 0;
    }
    
    let leftDiameter = diameterOfBinaryTree(root.left);
    let rightDiameter = diameterOfBinaryTree(root.right);
    let lheight = getHeight(root.left);
    let rheight = getHeight(root.right);
    
    return Math.max(leftDiameter, rightDiameter, (lheight + rheight));
};
```
