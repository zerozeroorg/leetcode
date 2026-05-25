### 99. Recover Binary Search Tree
Medium

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

**Example 1:**
```
  1
3
  2
  
To fix, swap 3 and 1:

  3
1
  2

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
```

**Example 2:**
```
   3
1     4
    2
    
To fix, swap 2 and 3:

   2
1     4
    3
    
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1
``` 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?

**Tags**
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

### Solution
My solution is brute force, taking O(n) space, O(n log n) time.
There is a O(1) space, O(n) time solution.
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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    /*
        traverse the tree and put each node in a list
        
        then sort the tree by the value
        
        then check where the sorted does not equal to actual in the list
        and there should be two.
        
        Once you found those two, swap them and you are done
    */
    const original = [];
    
    function traverse(node) {
        if (!node) {
            return;
        }
        traverse(node.left);
        original.push(node);
        traverse(node.right);
    }
    
    traverse(root);
    const sorted = original.map(o => o.val).sort((a, b) => a - b);
    const swaps = [];
    
    for (let i = 0; i < sorted.length; i++) {
        if (sorted[i] !== original[i].val) {
            swaps.push(original[i]);
        }
    }
    
    if (swaps.length === 2) {
        const temp = swaps[0].val;
        swaps[0].val = swaps[1].val;
        swaps[1].val = temp;
    }
};
```
