### 598. Range Addition II
Easy

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations. 

**Example 1:**
```
0 0 0
0 0 0
0 0 0

1 1 0
1 1 0
0 0 0

2 2 1
2 2 1
1 1 1

Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
```

**Example 2:**
```
Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
```

**Example 3:**
```
Input: m = 3, n = 3, ops = []
Output: 9
``` 

**Constraints:**
```
1 <= m, n <= 4 * 104
1 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
```

**Tags**
- Array
- Math

### Solution
```
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
            Observation - the increments always happen from the top left corner
            
            Iterate through the ops:
            - Compare the current matrix with the ops
            - If there is a subset (meaning ops increment smaller than matrix) then get the min of each
            - If there isn't, then keep current matrix
        """
        max_integers = (m, n)
        
        for op in ops:
            if op[0] < max_integers[0] or op[1] < max_integers[1]:
                max_integers = (min(max_integers[0], op[0]), min(max_integers[1], op[1]))
        
        return max_integers[0] * max_integers[1]
```
