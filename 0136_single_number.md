### 136. Single Number
Easy

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**
```
Input: [2,2,1]
Output: 1
```

**Example 2:**
```
Input: [4,1,2,1,2]
Output: 4
```

**Tags**
- Revisit
- Array
- Bit Manipulation

### Solution:

**Not accepted solution 1: use a map**
This is not accepted because it asks for not using extra memory. But let's start somewhere.

We use a map to count occurences of a number. We iterate through the array and count each number.

Then we go through the map or array and figure out which one has just one occurrence. Return that number.

Runtime: O(n)
Memory: O(n)

**Not accepted solution 2: sort array**
This is not accepted because it runs in O(n log n) time. But it does not use extra space!

We sort the array. Then we iterate the array and find which one does not have a duplicate (by comparing the number to its neighbor). If it does not have a duplicate neighbor, then return that answer.

Runtime: O(n log n)
Memory: no extra memory

** Use bit manipulation **

```
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let result = nums[0];
    for (let i = 1; i < nums.length; i++) {
        result = result ^ nums[i];
    }
    
    return result;
};
```
