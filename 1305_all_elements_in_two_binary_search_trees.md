### 1305. All Elements in Two Binary Search Trees
Medium

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

**Example 1:**
```
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
```

**Example 2:**
```
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
```

**Example 3:**
```
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
```

**Example 4:**
```
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
```

**Example 5:**
```
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
```

**Constraints:**
```
Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].

**Tags**
- Revisit
- Tree
- Depth-First Search
- Binary Search Tree
- Sorting
- Binary Tree

```

### Solution
- Traverse each tree and put the values in their respective lists
- Merge both lists
- I MESSED UP ON THE MERGING - I NEED TO CHECK IF BOTH OR ANY NODE WAS UNDEFINED
- A better solution: 
    - store the left side of both trees in a stack
    - compare then pop the small one
    - if the small has a right subtree, add all of the left side of that right subtree
    - Space is optimized to the height of the tree in the stack

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
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
var getAllElements = function(root1, root2) {
    let getNodes = function(node, output) {
        if (!node) {
            return output;
        }
        output = getNodes(node.left, output);
        output.push(node.val);
        output = getNodes(node.right, output);
        return output;
    };
    
    let output1 = getNodes(root1, []);
    let output2 = getNodes(root2, []);
    let result = [];
    let ptr1 = 0;
    let ptr2 = 0;
    
    
    while (ptr1 < output1.length || ptr2 < output2.length) {
        let node1 = output1[ptr1];
        let node2 = output2[ptr2];
        
        if (node1 === undefined && node2 !== undefined) {
            result.push(node2);
            ptr2 += 1;
            continue;
        }
        if (node2 === undefined && node1 !== undefined) {
            result.push(node1);
            ptr1 += 1;
            continue;
        }
        
        if (node2 < node1) {
            result.push(node2);
            ptr2 += 1;
            continue;
        } else {
            result.push(node1);
            ptr1 += 1;
        }
    }
    
    return result;    
};
```
