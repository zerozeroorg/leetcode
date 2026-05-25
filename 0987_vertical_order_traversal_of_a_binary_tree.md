### 987. Vertical Order Traversal of a Binary Tree
Hard

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

**Example 1:**
```
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
```

**Example 2:**
```
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
``` 

**Note:**
```
The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
```

**Tags**
- Hash Table
- Tree
- Depth-First Search
- Breadth-First Search
- Sorting
- Binary Tree

### Solution:
- create an array and traverse the tree. At each node, push the value, and their (x,y) coords.
- sort by X ascending, Y descending
- then combine nodes that have the same X values. Order them by Y descending.

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
var verticalTraversal = function(root) {
    let bfs = [];
    let results = [];
    if (!root) {
        return results;
    }
    
    bfs.push([root, [0, 0]]);
    while(bfs.length) {
        let node = bfs.shift();
        let nodeValue = node[0];
        let coords = node[1];
        let x = coords[0];
        let y = coords[1];
        results.push({
            value: nodeValue.val,
            x,
            y,
        });
        if (nodeValue.left) {
            bfs.push([nodeValue.left, [x - 1, y - 1]]);
        }
        if (nodeValue.right) {
            bfs.push([nodeValue.right, [x + 1, y - 1]]);
        }
    }
    
    results.sort((a, b) => {
        if (a.x < b.x) {
            return -1;
        }
        if (a.x > b.x) {
            return 1;
        }
        if (b.y < a.y) {
            return -1;
        }
        if (b.y > a.y) {
            return 1;
        }
        return a.value - b.value;
    });
    
    results = results.reduce((acc, current) => {
        if (!acc.length) {
            acc.push([current]);
            return acc;
        }
        let last = acc[acc.length - 1];
        let lastNode = last[0];
        if (lastNode.x === current.x) {
            last.push(current);
        } else {
            acc.push([current]);
        }
        return acc;
    }, []);
    
    results = results.map(elem => {
        elem = elem.map(el => {
            return el.value;
        });
        return elem;
    });
    
    return results;
};

// for reduce, you have to always return the accumlation
// forgot about the sorting: i did -1 for a.x to b.x for both comparisons
// forgot about the requirement where if there is a tie, you sort by value
```
