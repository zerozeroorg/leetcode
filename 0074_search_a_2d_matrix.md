### 74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

*Example 1:*
```
1   3   5   7
10  11  16  20
23  30  34  50


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
```

**Example 2:**
```
1   3   5   7
10  11  16  20
23  30  34  50
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
```

**Example 3:**
```
Input: matrix = [], target = 0
Output: false
``` 

**Constraints:**
```
m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
```

**Tags**
- Array
- Binary Search
- Matrix

### Solution:
- Binary Search the rows
- Then binary search that particular row

```
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let searchRows = (matrix, target) => {
        let startRow = 0;
        let endRow = matrix.length - 1;
        
        while (startRow <= endRow) {
            let middle = startRow + Math.floor((endRow - startRow) / 2);
            let middleRow = matrix[middle];
            if (middleRow[0] <= target && target <= middleRow[middleRow.length - 1]) {
                return middleRow;
            }
            
            if (target < middleRow[0]) {
                endRow = middle - 1;
            } else {
                startRow = middle + 1;
            }
        }
        
        return -1;
    };
    
    let row = searchRows(matrix, target);
    if (row === -1) {
        return false;
    }
    
    // ideally, use binary search
    if (row.indexOf(target) >= 0) {
        return true;
    }
    
    return false;
};
```
