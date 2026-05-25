### 106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.
```
For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
```

**Tags**
- Array
- Hash Table
- Divide and Conquer
- Tree
- Binary Tree

### Solution:
There is a O(n) time, O(n) space solution which I have not attempted:
- Use a hashmap to map the location of the inorder nodes -> index
- Create a helper function that will tell you what inorder range to search for (inStart, inEnd) so you don't have to create new lists every time.
- Build tree using the inStart, inEnd and the postorder array.

My solution:
- First observation: the root node is the last element in the postorder array
- If we can find that element in the inorder array, then the inorder array will tell us that things to the left are left children and things to the right are right children
- We recursively do this with the right sub tree first
- Then we build out the left sub tree
- return root node
- the code below checks if there is any inorder array nodes which helps with early termination.

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
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    let root = null;
    
    if (!inorder || !inorder.length) {
        return root;
    }
    let num = postorder.pop();
    root = new TreeNode(num);
    let rootIndex = inorder.indexOf(num);
    let leftTreeInorder = inorder.slice(0, rootIndex);
    let rightTreeInorder = inorder.slice(rootIndex + 1);
    let rightNode = buildTree(rightTreeInorder, postorder);
    let leftNode = buildTree(leftTreeInorder, postorder);
    root.left = leftNode;
    root.right = rightNode;
    
    return root;
};
```
