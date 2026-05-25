### 993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

**Example 1:**
```
    1
  2   3
4

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```

**Example 2:**
```
    1
  2   3
    4   5
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
```

**Example 3:**
```
    1
  2   3
4
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
``` 

**Constraints:**
```
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
```

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
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var getDepthAndParent = function(current, parent, target, depth) {
    if (!current) {
        return [null, null];
    }
    
    if (current.val === target) {
        return [parent, depth];
    }
    
    let leftResult = getDepthAndParent(current.left, current, target, depth + 1);
    if (leftResult[0]) {
        return leftResult;
    }
    return getDepthAndParent(current.right, current, target, depth + 1);
};

var isCousins = function(root, x, y) {
    let xResult = getDepthAndParent(root, null, x, 0);
    let yResult = getDepthAndParent(root, null, y, 0);
    
    if (xResult[0] === null || yResult[0] === null) {
        return false;
    }
    
    if (xResult[0].val !== yResult[0].val && xResult[1] === yResult[1]) {
        return true;
    }
    
    return false;
};
```
