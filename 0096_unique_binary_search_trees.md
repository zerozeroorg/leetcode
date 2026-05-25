### 96. Unique Binary Search Trees
Medium

Share

Given `n`, how many structurally unique BST's (binary search trees) that store values `1 ... n`?

**Example:**
```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
``` 

**Constraints:**

`1 <= n <= 19`

**Tags**
- Math
- Dynamic Programming
- Tree
- Binary Search Tree
- Binary Tree

### Solution:
Fastest solution: use math (Catalan numbers) to solve it.

The intuition:
For each node, treat that as the root node, as r. Then get the number of possible binary search trees on the left using [1,...r]. Then get the possible number of 
binary search trees on the right using [r+1,...n]. We have to do this split because binary search trees have the property where elements on the left are less than
or equal to the root and elements on right are greater than the root.

You can use dynamic programming with recurison the store the precomputed unique binary search trees for a given set of nodes.

Python Solution
```
class Solution:
    def numTrees(self, n: int) -> int:
        lookup = {}
        
        def helper(start, end):
            total = 0
            if start >= end:
                return 1
            
            key = (start, end)
            if lookup.get(key) is not None:
                return lookup.get(key)
            
            for i in range(start, end + 1):                
                total += (helper(start, i - 1) * helper(i + 1, end))
            
            lookup[key] = total
            return total
        
        return helper(1, n)
        
```

JS Solution
```
/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    let dp = {};
    
    let nums = [];
    for (let i = 1; i <= n; i++) {
        nums.push(i);
    }
    
    if (!nums.length) {
        return 0;
    }    
    
    let numTreesHelper = (n, dp) => {
        if (n.length <= 1) {
            return 1;
        }
        
        let key = n.join('_');
        if (dp[key] !== undefined) {
            return dp[key];    
        }
        let sum = 0;
        for (let i = 0; i < n.length; i++) {
            let leftSubTreeNodes = n.slice(0, i);
            let rightSubTreeNodes = n.slice(i + 1);
            
            let leftSum = numTreesHelper(leftSubTreeNodes, dp);
            let rightSum = numTreesHelper(rightSubTreeNodes, dp);
            
            sum += (leftSum * rightSum);
        }
        
        dp[key] = sum;
        return dp[key];
    };
    
    return numTreesHelper(nums, dp);
};
```
