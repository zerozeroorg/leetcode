### 662. Maximum Width of Binary Tree
Medium

Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

**Example 1:**
```
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```

**Example 2:**
```
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```

**Example 3:**
```
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```

**Example 4:**
```
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
``` 

**Constraints:**
```
The given binary tree will have between 1 and 3000 nodes.
```

**Tags**
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

### Solution:
- Ok, first we need to record the position of each node. Root has position 1, and left is 2n and right is 2n + 1. Set the position for each node.
- The intuition: the width of each level measured by the distance between the node position at the farthest left and the node position at the farthest right.
- To get the width? Just subtract the positions: node_position_farthest_right - node_position_farthest_left.

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
 * @return {number}
 */
var widthOfBinaryTree = function(root) {
    let queue = [[root, 1]];
    let max = 0;
    
    while(queue.length > 0) {
        let size = queue.length;
        let first = queue[0];
        let curr = null;
        while(size > 0) {
            curr = queue.shift();
            let node = curr[0];
            let position = curr[1];
            
            if (node.left) {
                queue.push([node.left, position * 2]);
            }
            
            if (node.right) {
                queue.push([node.right, position * 2 + 1]);
            }
            
            size -= 1;
        }
        

        if (curr === first) {
            max = Math.max(max, 1);
        } else {
            max = Math.max(max, curr[1] - first[1] + 1);    
        }
        
    }
    
    return max;
};
```
Python Solution
- Because null nodes between the left most and right most nodes at each level count as part of the width, the simplest thing we can do is use BFS and indexing
- Each node will have an index. If node has index i, then the left node has 2i + 1 and right node has 2i + 2.
- At each iteration of the BFS, we take the index of the last node - index of first node + 1 to calculate the width
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = collections.deque([(root, 1)])
        
        def get_width(queue):    
            return queue[-1][1] - queue[0][1] + 1
        
        while queue:
            temp = collections.deque([])
            max_width = max(max_width, get_width(queue))
            while queue:
                node, count = queue.popleft()
                if not node:
                    continue
                if node.left:
                    temp.append((node.left, count * 2))
                if node.right:
                    temp.append((node.right, count * 2 + 1))
            queue = temp
        
        return max_width
        
```
