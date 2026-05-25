### 905. Sort Array By Parity
Easy

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition. 

**Example 1:**
```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```
**Note:**
```
1 <= A.length <= 5000
0 <= A[i] <= 5000
```

**Tags**
- Array
- Two Pointers
- Sorting

### Solution:
- First solution: Create an empty array. Then iterate over the numbers, and if it is even, put in the head of the array, otherwise put it in the tail of the array
- Second solution: swap even and odd numbers in place

```
/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
    let left = 0;
    let right = A.length - 1;
    
    while (left <= right) {
        while (A[left] !== undefined && A[left] % 2 === 0) {
            left += 1;
        }
        while (A[right] !== undefined && A[right] % 2 !== 0) {
            right -= 1;
        }
        
        if (left <= right) {
            let temp = A[left];
            A[left] = A[right];
            A[right] = temp;
            left += 1;
            right -= 1;
        }
    }

    
    return A;
};
```
