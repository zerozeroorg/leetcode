### 117. Populating Next Right Pointers in Each Node II
Medium

Given a binary tree
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
     1
  2    3
 4 5     7
 
Becomes:
      1
  2   ->   3
 4 -> 5  ->  7

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
``` 

**Constraints:**
```
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
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
            This is the same as part 1, but there could be missing nodes.
            Create a helper function that takes a node and a nextRightNode
            If node is None, return
            Connect node to the nextRightNode
    
            Then check if you have a left node. If true:
                helper(node.left, node.right) # trick! There might not be a right node!
            Then check if you have a right node. If true:
                helper(node.right, node.next && (node.next.left || node.next.right))
            Return node
            
            Mistakes:
            I messed up a case [1,2,3,4,5,null,6,7,null,null,null,null,8] where you
            have to recursively get the nextCandidate
            
            I also need to do the right nodes first, then the left so traverse
            the right side then the left side in order for the getCandidate function to work
        """
        def getCandidate(node):
            # get the nextNode's candidate for connecting
            if not node.next:
                return None
            
            if node.next and node.next.left:
                return node.next.left
            elif node.next and node.next.right:
                return node.next.right
            elif node.next:
                return getCandidate(node.next)
            else:
                return None
                
        def helper(node, nextNode):
            if not node:
                return node
            
            node.next = nextNode
            candidate = getCandidate(node)
            
            if node.right:
                helper(node.right, candidate)
            if node.left:
                helper(node.left, node.right if node.right else candidate)

            
            return node
        
        return helper(root, None)
        
```
