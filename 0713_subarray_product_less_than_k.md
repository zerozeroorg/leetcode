### 713. Subarray Product Less Than K
Medium

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

**Example 1:**
```
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

**Note:**
```
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6
```

**Tags**
- Array
- Binary Search
- Sliding Window
- Prefix Sum

### Solution:
- I had to cheat. My O(n^2) solution did not work (TLE).
- The idea is to use sliding window and multiply until you get to K or more, then decrease the window from the left until you are < k again. Then increase
the sliding window again.
- As you add more numbers to the subarray product, you are increasing the number of subarrays by (endPtr - startPtr + 1). Did not know that!

```
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let result = 0;
    let product = 1;
    let start = 0, end = 0;
    
    while (end < nums.length) {
        product *= nums[end];
        
        while (product >= k && start <= end) {
            product /= nums[start];
            start += 1;
        }
        
        result += end - start + 1;
        end += 1;
    }
        
    return result;
};
```
