### 538. Convert BST to Greater Tree
Medium

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

**Example 1:**
```
        4
  1           6
0   2       5   7
     3            8 
     
Becomes:

       30
  36         21
36 35     26    15
    33            8 

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

**Example 2:**
```
Input: root = [0,null,1]
Output: [1,null,1]
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [0, 104].
-10^4 <= Node.val <= 10^4
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.
``` 

Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

**Tags**
- revisit
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

### Solution
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
var convertBST = function(root) {
    /**
        All nodes in the right side are greater so get the sum of those
        Then add it to the current node
        
        All nodes on the left need the sum of the right and parent, so pass
        that sum to the left side
     */
    const convertBSTHelper = (node, sumAboveMe) => {
        if (!node) {
            return [null, 0];
        }
        
        const newNode = new TreeNode(node.val + sumAboveMe);
        const [nodeRight, rightSum] = convertBSTHelper(node.right, sumAboveMe);
        if (nodeRight) {
            newNode.val += rightSum;
            newNode.right = nodeRight;
        }
        const [nodeLeft, leftSum] = convertBSTHelper(node.left, newNode.val);
        newNode.left = nodeLeft;
        
        return [newNode, rightSum + leftSum + node.val];

    };
    
    return convertBSTHelper(root, 0)[0];
};
```
