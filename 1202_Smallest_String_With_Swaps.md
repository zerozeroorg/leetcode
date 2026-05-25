### 1202. Smallest String With Swaps
Medium

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.


**Example 1:**
```
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
```

**Example 2:**
```
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
```

**Example 3:**
```
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
``` 

**Constraints:**
```
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
```

**Tags**
- revisit
- Array
- Hash Table
- String
- Depth-First Search
- Breadth-First Search
- Union-Find
- Sorting

### Solution
- This solution using DFS to find connected components
- There is another solution using union find or disjoint set data structure
```
/**
 * @param {string} s
 * @param {number[][]} pairs
 * @return {string}
 */
var smallestStringWithSwaps = function(s, pairs) {
    /*
        The intuition is that if you have pairs (a, b) and (b, c),
        then you can rearrange all chars of s for indices a, b, and c
        because we can do infinite swaps. 
        
        Ex:
        s = "zabty"
        pairs = [(0, 1), (1, 2), (3, 4)]
        - swap z with a
        - then swap z with b
        - t and y don't need to be swapped, and not connected to other chars
        - ans: "abzty"
        
        This can be represented at a graph like this:
        
        z - a - b    t - y
        
        Where characters in the graph can be swapped with any other character
        in the graph.
        
        Once we know that, we can find all connected components of the graph, sort
        them and return the final answer.
        
        The algorithm:
        - first build adjacency matrix to represent the graphs/relationships
        - then you can use DFS to find all connected components:
            - Create a visited variable. This will skip DFS for nodes already visited
            (nodes aleady visited will be in the same connected component)
            - For search index in string s:
                - perform DFS is the index is not visited, storing indices and chars
                in that DFS search
                - then sort the indices and chars
                - the iterate and insert the char by index to answer array
        - return ans array
    */
    const adj = [];
    for (const [src, dest] of pairs) {
        adj[src] = adj[src] || [];
        adj[dest] = adj[dest] || [];
        adj[src].push(dest);
        adj[dest].push(src);
    }
    
    const ans = [];
    const visited = new Set();
    const dfs = (index, indices, chars) => {
        visited.add(index);
        indices.push(index);
        chars.push(s[index]);
        
        const neighbors = adj[index];
        if (!neighbors) {
            return;
        }
        for (const neighbor of neighbors) {
            if (visited.has(neighbor)) {
                continue;
            }
            dfs(neighbor, indices, chars);
        }
    };
    
    for (let i = 0; i < s.length; i++) {
        if (visited.has(i)) {
            continue;
        }
        const indices = [];
        const chars = [];
        dfs(i, indices, chars);
        
        indices.sort((a, b) => a - b);
        chars.sort();
        
        for (let j = 0; j < indices.length; j++) {
            ans[indices[j]] = chars[j];
        }
    }
    
    return ans.join('');
};
```
