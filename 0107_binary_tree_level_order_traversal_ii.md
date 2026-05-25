### 107. Binary Tree Level Order Traversal II
Medium

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
```
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

**Tags**
- Tree
- Breadth-First Search
- Binary Tree

### Solution:
- Use BFS.
- We need the level so that we know which array to append the node at.

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
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
    let bfsQueue = [];
    let ans = [];
    
    if (!root) {
        return ans;
    }
    
    bfsQueue.push([root, 0]);
    
    while (bfsQueue.length > 0) {
        let nodeAndLevel = bfsQueue.shift();
        let node = nodeAndLevel[0];
        if (!node) {
            continue;
        }
        let level = nodeAndLevel[1];
        ans[level] = ans[level] || [];
        ans[level].push(node.val);
        bfsQueue.push([node.left, level + 1]);
        bfsQueue.push([node.right, level + 1]);
    }
    return ans.reverse();
};
```
