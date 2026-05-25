### 103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
```
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
   
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
```

**Tags**
- Tree
- Breadth-First Search
- Binary Tree

### Solution:
- Use BFS to traverse the tree
- have a level variable to keep track of what level you are on (easy to do with BFS)
- get all nodes for that level
- if it is a even level, reverse the order
- add that list of nodes at the level to the result array
- return result

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
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    let queue = [];
    let levelCount = 1;
    let result = [];
    
    if (!root) {
        return result;
    }
    
    queue.push([root]);
    
    while(queue.length) {
        let nodes = queue.shift();
        let ans = nodes.map(node => node.val);
        if (levelCount % 2 === 0) {
            ans.reverse();
        }
        result.push(ans);
        let children = [];
        while(nodes.length) {
            let node = nodes.shift();
            let left = node.left;
            let right = node.right;
            if (left) {
                children.push(left);
            }
            if (right) {
                children.push(right);
            }
        }

        if (children.length) {
            queue.push(children);    
        }
        
        levelCount += 1;
    }
    
    return result;
};
```
