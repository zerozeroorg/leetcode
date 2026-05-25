### 152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example 1:**
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
**Tags**
- Revisit
- Array
- Dynamic Programming

### Solution:
- I did not know how to solve this. I knew I had to use some form of Kadane's algorithm but 
I thought if I count the number of negatives, I can determine if I should keep a product or not.
This did not work, it was too complicated.

So I googled and the idea is to keep the min and max products at each index. The min, which is negative, can be multipled
by another negative so it is good to keep track of that.

At each iteration, to find the product you can:
- multiply max product with n
- keep n
- multiply min product with n

```
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    if (!nums.length) {
        return 0;
    }
    
    let max = nums[0];
    let ptr = 1;
    let minProduct = max;
    let maxProduct = max;
    
    while(ptr < nums.length) {
        let num = nums[ptr];
        let temp = maxProduct;
        
        maxProduct = Math.max(num, maxProduct * num, minProduct * num);
        minProduct = Math.min(num, temp * num, minProduct * num);
        
        max = Math.max(max, maxProduct);
        ptr += 1;
    }
    
    return max;
};
```
