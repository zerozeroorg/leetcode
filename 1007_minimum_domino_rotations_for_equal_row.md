### 1007. Minimum Domino Rotations For Equal Row
Medium

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

**Example 1:**
```
[2,  1,  2,  4,  2,  2]
[5,  2,  6,  2,  3,  2]

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
```

**Example 2:**
```
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
``` 

**Constraints:**
```
2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6
```
**Tags**
- revisit
- Array
- Greedy

### Solution:
- This is a very good problem!
- First observation: in order to do a rotation, a number must exist in either A or B for all indexes of A and B.
- If a number is not found, then return -1.
- Second observation: once we have that common number, the minimum number of rotations is based on how often the number shows up in A or B.
- If it shows up less often in A, then it is the number of times the number is in A. If it shows up less often in B, then it is the number of times
the number is in B.
- GOTCHA: if the number is in A and B, then don't count it. There are no rotations for that number.
- There is another, easier way below this solution.
```
/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var minDominoRotations = function(A, B) {
    let map = {};
    let nums = [];
    for (let i = 0; i < A.length; i++) {
        let a = A[i];
        let b = B[i];

        map[a] = map[a] || {
            index: [],
            aCount: 0,
            bCount: 0
        };
        
        map[b] = map[b] || {
            index: [],
            aCount: 0,
            bCount: 0
        };
        if (a !== b) {
            map[a].aCount += 1;
            map[b].bCount += 1;            
        }

        if (a === b) {
            map[a].index.push(i);
            if (map[a].index.length === A.length) {
                nums.push(a);
            }
        } else {
            map[a].index.push(i);
            map[b].index.push(i);
            if (map[a].index.length === A.length) {
                nums.push(a);
            }
            if (map[b].index.length === A.length) {
                nums.push(b);
            }            
        }
    }
    
    if (nums.length === 0) {
        return -1;
    }
    
    nums = nums.map(num => Math.min(map[num].aCount, map[num].bCount));
    return Math.min(...nums);
};
```
- Another solution: in order to have rotations, the first domino's tile numbers must match any of the rest of dominos.
- So, take the first domino, and test how many swaps are necessary for both tiles.
- The code below shows the algorithm:
```
/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var minDominoRotations = function(A, B) {
    const minSwaps = (A, B, num) => {
        let total = 0;
        let aCount = 0;
        let bCount = 0;
        
        for (let i = 0; i < A.length; i++) {
            let a = A[i];
            let b = B[i];
            if (a !== num && b !== num) {
                continue;
            }
            total += 1;
            if (a === num) {
                aCount += 1;
            }
            if (b === num) {
                bCount += 1;
            }
        }
        if (total !== A.length) {
            return -1;
        }
        return Math.min(total - aCount, total - bCount);
    };
    
    let minSwapA = minSwaps(A, B, A[0]);
    let minSwapB = minSwaps(A, B, B[0]);
    if (minSwapA === -1 && minSwapB === -1) {
        return -1;
    }
    return Math.min(...[minSwapA, minSwapB].filter(num => num !== -1));
};
```
