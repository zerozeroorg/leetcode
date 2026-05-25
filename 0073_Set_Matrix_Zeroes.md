### 73. Set Matrix Zeroes
Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place. 

**Example 1:**
```
1 1 1
1 0 1
1 1 1

BECOMES

1 0 1
0 0 0
1 0 1

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**
```
0 1 2 0
3 4 5 2
1 3 1 5

BECOMES

0 0 0 0
0 4 5 0
0 3 1 0

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
``` 

**Constraints:**
```
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
``` 

**Follow up:**
```
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
```


**Tags**
- Array
- Hash Table
- Matrix

### Solution
```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
            First idea:
            Get all the zero coords in the matrix
            Then for each zero coord:
            - set zero on the row
            - set zero on the col
            This is too slow though since you might overlap each
            other when setting zeroes
            
            Second idea from hint:
            Have a row map
            Have a column map
            Iterate through the matrix and:
            - if it is a zero, set row map = True an column map = True
            Then iterate through the matrix again
            - if that row is a zero in the row map, set it to zero
            - if that col is a zero in the column map set it to zero
            
            Best answer:
            Iterate through the matrix
            If the cell contains a zero, mark the row's first cell as zero
            and the column's first cell as zero
            Then iterate through each row's first cell and if it is a zero, mark the entire row as zero.
            Do the same with column's first cell
        """
        row_map = {}
        col_map = {}
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_map[i] = True
                    col_map[j] = True
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0 and (row_map.get(i) == True or col_map.get(j) == True):
                    matrix[i][j] = 0        
        
```
