### 835. Image Overlap
Medium

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

**Example 1:**
```
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
```

**Notes:** 
```
1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1

**Tags**
- Array
- Matrix

### Solution
- Brute force

```
/**
 * @param {number[][]} A
 * @param {number[][]} B
 * @return {number}
 */
var largestOverlap = function(A, B) {
    let rows = A.length;
    let cols = A[0].length;
    
    let helper = (rowOffSet, colOffSet) => {
        let count = 0;
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                // check if moving A by offset is in bounds. If not, continue.
                if (i + rowOffSet < 0 || i + rowOffSet >= rows || j + colOffSet < 0 || j + colOffSet >= cols) {
                    continue;
                }
                
                count += A[i][j] * B[i + rowOffSet][j + colOffSet];
            }
        }
        return count;
    };
    
    let result = 0;
    
    for (let i = -rows + 1; i < rows; i++) {
        for (let j = -cols + 1; j < cols; j++) {
            let count = helper(i, j);
            result = Math.max(result, count);
        }
    }
    
    return result;
};
```
