### 2657. Find the Prefix Common Array of Two Arrays

Medium

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 
```
Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
Example 2:

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
 

Constraints:

1 <= A.length == B.length == n <= 50
1 <= A[i], B[i] <= n
It is guaranteed that A and B are both a permutation of n integers.
```

### Solution
```
/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function(A, B) {
    /**
        Since A and B are both contain a sequence of n integers from 1 to n
        exactly once, then an integer exists in both A and B for a total of 2.

        You can use a freq map to keep track of the integer counts for both A and B.
        If the total is 2, then you found a common prefix.
     */
    const lookup = {};
    const length = A.length;
    let runningTotal = 0;
    const ans = [];

    for (let i = 0; i < length; i++) {
        let aNum = A[i];
        let bNum = B[i];
        
        lookup[aNum] = lookup[aNum] || 0;
        lookup[aNum] += 1;
        if (lookup[aNum] === 2) {
            runningTotal += 1;
        }
        lookup[bNum] = lookup[bNum] || 0;
        lookup[bNum] += 1;
        if (lookup[bNum] === 2) {
            runningTotal += 1;
        }
        ans.push(runningTotal);
    }
    return ans;
};
```
