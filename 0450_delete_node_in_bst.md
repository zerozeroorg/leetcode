### 450. Delete Node in a BST
Medium

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)? 

**Example 1:**
```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

**Example 3:**
```
Input: root = [], key = 0
Output: []
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [0, 104].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5
```

**Tags**
- Revisit
- Tree
- Binary Search Tree
- Binary Tree

### Solution:
- There are three cases:
- The target node has not children: easy delete
- The target node has one child: replace that node with that child
- The target node has two children: replace the target with the smallest child on its right subtree. Delete the smallest child on the right subtree.

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
 * @param {number} key
 * @return {TreeNode}
 */
var deleteNode = function(root, key) {
    if (!root) {
        return null;
    }
    
    if (root.val !== key) {
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else {
            root.right = deleteNode(root.right, key);
        }
    } else {
        // no child
        if (!root.left && !root.right) {
            root = null;
        } else if (root.left && !root.right) {
            let temp = root.left;
            root.left = null;
            root = temp;
        } else if (!root.left && root.right) {
            let temp = root.right;
            root.right = null;
            root = temp;
        } else {
            let start = root.right;
            while(start.left) {
                start = start.left;
            }
            root.val = start.val;
            root.right = deleteNode(root.right, start.val);
        }
    }
    
    return root;
};
```
