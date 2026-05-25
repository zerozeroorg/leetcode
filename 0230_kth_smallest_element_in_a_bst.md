### 230. Kth Smallest Element in a BST
Medium

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

**Example 1:**
```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

```

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

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
 * @param {number} k
 * @return {number}
 */
var helper = function(root, k, count) {
    if (root.left) {
        let result = helper(root.left, k, count);
        count = result[1];
        if (count === k) {
            return result;
        }
    }
    
    count++;
    if (k === count) {
        return [root, count];
    }
    
    if (root.right) {
        let result = helper(root.right, k, count);
        count = result[1];
        if (count === k) {
            return result;
        }
    }
    
    return [root, count];
};
var kthSmallest = function(root, k) {
    let result = helper(root, k, 0);  
    return result[0].val;
};
```
**Tags**
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree
