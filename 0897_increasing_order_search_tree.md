### 897. Increasing Order Search Tree
Easy

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child. 

**Example 1:**
```
        5
    3        6
  2   4        8
1            7   9

Transforms to ->>

1
  2
    3
      4
        5
          6
            7
              8
                9
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```

**Example 2:**
```
  5
1   7

Transforms to ->

1
  5
    7
Input: root = [5,1,7]
Output: [1,null,5,null,7]
``` 

**Constraints:**
```
The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
```

**Tags**
- Stack
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

### Solution:
- I had a slow solution: I had to create a storage list to store the nodes, then traverse it to link them correctly.
- Another way is explained below with the answer from leetcode.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
            Create a list for storage
            Traverse the nodes in inorder traversal
            Then iterate through the list:
                For each element in the list, set both left and right pointers to null
                Then set its right pointer to equal to the next element in the list
        """
        if not root:
            return root
        
        store = []
        def inorder(root, store):
            if not root:
                return
            inorder(root.left, store)
            store.append(root)
            inorder(root.right, store)
       
        inorder(root, store)
        
        for i in range(len(store)):
            node = store[i]
            node.left = node.right = None
            if i + 1 < len(store):
                node.right = store[i + 1]
    
        return store[0]
        
```

Another Approach: create a new node and as you traverse inorder, link the new node to the inorder node.
```
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
```
