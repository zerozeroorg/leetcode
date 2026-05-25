### 116. Populating Next Right Pointers in Each Node
Medium

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

**Follow up:**
```
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
``` 

**Example 1:**
```
Input:
    1
  2   3
4 5   6 7

Output:
        1 -> null
    2 ->      3 -> null
4 -> 5 ->   6 -> 7 -> null


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
``` 

**Constraints:**
```
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
```

**Tags**
- Linked List
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

### Solution:
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
            Build a helper function that takes in a node, and its next
            node.
            The node points to the next node
            Then, call helper function for:
            - the left node, passing in the right node
            - the right node, passing the next node's left node if it exists
            - return node
        """
        def helper(node, nextNode):
            node.next = nextNode
            left = node.left
            right = node.right
            
            if left:
                left = helper(left, right)
            
            if right:
                right = helper(right, nextNode.left if nextNode else None)
        
            return node
        
        if root is None:
            return root
        
        return helper(root, None)
```
Version 2 which does not use helper function
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
            Need a new recursive function, that takes a node and its parent
            Easy case:
            - If no parent, then next parent is null
            - Get my immediate right child
            - Have my left child next -> right child
            - If I have parent, then ask parent's next's left, and have
            right child point to that
        """
        if not root:
            return

        if root.left:
            root.left.next = root.right

        if root.right and root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
```
