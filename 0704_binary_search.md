### 704. Binary Search
Easy

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

**Example 1:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**
```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
``` 

**Note:**
```
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
```

**Tags**
- Array
- Binary Search

### Solution:
```
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    // set up start and end pointers
    // while start <= end
    // compute middle pointer
    // check if middle pointer == target
    // if true, return middle
    // if not, adjust start and end pointers
    // return -1 if not found
    
    let start = 0;
    let end = nums.length - 1;
    
    while (start <= end) {
        let middle = start + Math.floor((end - start) / 2);
        if (nums[middle] === target) {
            return middle;
        }
        if (nums[middle] < target) {
            start = middle + 1;
        } else {
            end = middle - 1;
        }
    }
    
    return -1;
};
```
