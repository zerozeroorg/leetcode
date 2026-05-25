### 669. Trim a Binary Search Tree
Medium

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

**Example 1:**
```
  1
0   2

Becomes:

  1
    2

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
```

**Example 2:**
```
    3
0       4
  2
1

Becomes:

    3
  2
1

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
```

**Example 3:**
```
Input: root = [1], low = 1, high = 2
Output: [1]
```

**Example 4:**
```
Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]
```

**Example 5:**
```
Input: root = [1,null,2], low = 2, high = 4
Output: [2]
``` 

**Constraints:**
```
The number of nodes in the tree in the range [1, 104].
0 <= Node.val <= 104
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 104
```


**Tags**
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

### Solution:
the JS solution is cleaner and more "elegant"
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """
            Have a helper function that has the root, parent, low, high
            Check my current value.
            - I am within low and high: good!
            -- check my left
            -- check my right
            - I am too big: point my parent to point to my left children
            - I am too small: point my parent to point my right children
            - return root
            NOTE: need to check for empty parent pointer
        """
        def helper(root, parent, low, high):
            if not root:
                return None
            
            if low <= root.val <= high:
                root.left = helper(root.left, root, low, high)
                root.right = helper(root.right, root, low, high)
                return root
            
            if root.val < low:
                if not parent:
                    root = root.right
                else:
                    parent.left = root.right
                    root = root.right
            else:
                if not parent:
                    root = root.left
                else:
                    parent.right = root.left
                    root = root.left

            root = helper(root, parent, low, high)
            return root

        
        return helper(root, None, low, high)
            
            
        
        
```
JS Solution
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
 * @param {number} low
 * @param {number} high
 * @return {TreeNode}
 */
var trimBST = function(root, low, high) {
    /*
        if current is not in range:
        if current is < low:
        return trimBST of right
        if current > high:
        return trimsBST of left
        current.left = trimBST of left
        current.rigth = trimBST of right
     */
    if (!root) {
        return root;
    }
    
    if (root.val < low) {
        return trimBST(root.right, low, high);
    } else if (root.val > high) {
        return trimBST(root.left, low, high);
    } else {
        root.left = trimBST(root.left, low, high);
        root.right = trimBST(root.right, low, high);
        return root;
    }
};
```
