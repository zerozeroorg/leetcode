### 297. Serialize and Deserialize Binary Tree
Hard

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

**Example 1:**
```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

**Example 2:**
```
Input: root = []
Output: []
```

**Example 3:**
```
Input: root = [1]
Output: [1]
```

**Example 4:**
```
Input: root = [1,2]
Output: [1,2]
```

**Tags**
- String
- Tree
- Depth-First Search
- Breadth-First Search
- Design
- Binary Tree

### Solution:
- I used the heap position strategy
- A node's position is x
- A node's left child position is 2x + 1
- A node's right child position is 2x + 2
- I messed up around the empty tree case and this case:
```
  1
    2
      3
        4
```
- For that, there are nulls so you need to build out the heap array.

```
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    let result = [];
    let queue = [[root, 0]];
    
    if (!root) {
        return result.toString();
    }

    while (queue.length) {
        let element = queue.shift();
        let node = element[0];
        let position = element[1];
        
        result.push(`${node.val};${position}`);

        if (node.left) {
            queue.push([node.left, position * 2 + 1]);
        }
        if (node.right) {
            queue.push([node.right, position * 2 + 2]);
        }
    }

    return result.toString();
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    let bfs = data.split(',');
    let root = null;

    if (!bfs.length) {
        return null;    
    }
    
    let tree = [];
    bfs.forEach(element => {
        let parsed = element.split(';');
        const [val, position] = parsed;
        tree[position] = val;
    })
    
    let helper = (tree, nodeNumber) => {
        if (tree[nodeNumber] === undefined || isNaN(parseInt(tree[nodeNumber], 10))) {
            return null;
        }
        const node = new TreeNode(tree[nodeNumber]);
        node.left = helper(tree, nodeNumber * 2 + 1);
        node.right = helper(tree, nodeNumber * 2 + 2);
        return node;
    };
    
    return helper(tree, 0);
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
```
