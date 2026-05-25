### 653. Two Sum IV - Input is a BST
Easy

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target. 

**Example 1:**
```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

**Example 3:**
```
Input: root = [2,1,3], k = 4
Output: true
```

**Example 4:**
```
Input: root = [2,1,3], k = 1
Output: false
```

**Example 5:**
```
Input: root = [2,1,3], k = 3
Output: true
``` 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

**Tags**
- Hash Table
- Two Pointers
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Search Tree
- Binary Tree

### Solution
- You can do it in one pass! I did this in 3 passes.
- When I ran with test case [2,2,2] it wasn't a valid input meaning the nodes are definitely unique!
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
            Create an empty list of numbers
            Create a lookup table
            Traverse the tree and add the nodes into the list
            Then traverse the list and add lookup[num] -> [index,]
            Then traverse the list again and see if the k - num is in the lookup
            table and its index is not in the list. If so, return True
            return false
        """
        lookup = collections.defaultdict(list)
        nums = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        for key, value in enumerate(nums):
            lookup[value].append(key)
        
        for key, value in enumerate(nums):
            diff = k - value
            if diff in lookup and key not in lookup[diff] or len(lookup[diff]) > 1:
                return True
        
        return False
            
        
```
