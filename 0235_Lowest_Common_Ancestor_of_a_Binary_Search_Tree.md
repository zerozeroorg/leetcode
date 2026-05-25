### 235. Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 

**Example 1:**
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

**Example 2:**
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

**Example 3:**
```
Input: root = [2,1], p = 2, q = 1
Output: 2
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
```

**Tags**
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

### Solution
I went with the most inefficient way to solve it. The most efficient way to solve it is as follows:
1. Start traversing the tree from the root node.
2. If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
3. If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
4. If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            Get all ancestors of node p, including p in a set
            Get all ancestors of node q, including q in a set
            Then for each set in p, if there exists a node in set q
            Do the other way for q

            MISTAKE: didn't realize that I needed to get the LCA because
            I was just getting all the ancestors. Need a level param
        """
        def get_ancestors(root, node, ancestors, level=0):
            if not root:
                return
            
            ancestors[root.val] = (root, level)

            if root.val == node.val:
                return

            if root.val > node.val:
                get_ancestors(root.left, node, ancestors, level + 1)
            else:
                get_ancestors(root.right, node, ancestors, level + 1)
            
        
        p_ancestors = {}
        q_ancestors = {}
        
        get_ancestors(root, p, p_ancestors)
        get_ancestors(root, q, q_ancestors)
        
        possible = []
        # check p -> q
        for key in p_ancestors.keys():
            if q_ancestors.get(key):
                possible.append(q_ancestors.get(key))
        if not len(possible):
            for key in q_ancestors.keys():
                if p_ancestors.get(key):
                    possible.append(p_ancestors.get(key))
        
        if not len(possible):
            return None
        
        maxLevel = possible[0][1]
        maxNode = possible[0][0]
        
        for i in range(1, len(possible)):
            if possible[i][1] > maxLevel:
                maxLevel = possible[i][1]
                maxNode = possible[i][0]
        
        return maxNode
            
```
