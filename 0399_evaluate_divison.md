### 399. Evaluate Division
Medium

You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

**Example 1:**
```
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
```

**Example 2:**
```
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
```

**Example 3:**
```
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
```

**Tags**
- Array
- String
- Depth-First Search
- Breadth-First Search
- Union-Find
- Graph Theory
- Shortest Path

### Solution:
- I am very weak with graph algorithms and have no idea how you would intuitively use a floyd warshall to solve this problem.

```
/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    // first, create a var to index mapping
    let map = {};
    let index = 0;
    const result = [];
    
    equations.forEach(equation => {
        const [x, y] = equation;
        if (map[x] === undefined) {
            map[x] = index;
            index += 1;
        }
        if (map[y] === undefined) {
            map[y] = index;
            index += 1;
        }
    });
    
    // build the graph/table
    let graph = [];
    for (let i = 0; i < index; i++) {
        let row = [];
        for (let j = 0; j < index; j++) {
            row.push(undefined);
        }
        graph.push(row);
    }
    
    // fill in the graph/table
    values.forEach((value, index) => {
        let equation = equations[index];
        graph[map[equation[0]]][map[equation[1]]] = value;
        graph[map[equation[1]]][map[equation[0]]] = 1 / value;
    });
    
    
    // floyd-warshall algo
    for (let k = 0; k < index; k++) {
        for (let i = 0; i < index; i++) {
            for(let j = 0; j < index; j++) {
                if (graph[i][j] === undefined && graph[i][k] !== undefined && graph[k][j] !== undefined) {
                    graph[i][j] = graph[i][k] * graph[k][j];
                }    
            }
        }
    }
    
    
    // evaluate queries
    queries.forEach(query => {
        const [x, y] = query;
        if (graph[map[x]] !== undefined && graph[map[x]][map[y]] !== undefined) {
            result.push(graph[map[x]][map[y]]);
        } else {
            result.push(-1);
        }
    })
    
    return result;
};
```
