### 173. Binary Search Tree Iterator
Medium

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called. 

**Example 1:**
```
     7
  3     15
      9   20

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]
```

**Explanation**
```
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
``` 

**Constraints:**
```
The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
``` 

**Follow up:**
```
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
```

**Tags**
- Stack
- Tree
- Design
- Binary Search Tree
- Binary Tree
- Iterator

### Solution:
- My initial solution is straightforward. There is a better solution below that uses controlled recurison to solve this.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = collections.deque()
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            self.inorder.append(node)
            traverse(node.right)
            
        traverse(root)

    def next(self) -> int:
        return self.inorder.popleft().val

    def hasNext(self) -> bool:
        return len(self.inorder) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

### Better solution:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
        The idea: to control inorder recursion, instead of relying on the system stack
        you create your own stack and push elements there.
        Here - we will start from the root and push all the left most nodes
        when we initialize the tree. The last element of the stack should be
        the smallest element in the tree.
        When calling next() we pop off the element of the stack. There are two cases here:
        - if the node has no right child, return the node value.
        - call the helper function on the right subtree then return the node value.
        Space complexity: O(h) space 
        Time complexity: O(h) for next() and O(1) for hasNext()
    """

    def __init__(self, root: TreeNode):
        self.stack = collections.deque()
        self.__left_traverse(root)
    
    def __left_traverse(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.__left_traverse(node.right)
        return node.val
            

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
