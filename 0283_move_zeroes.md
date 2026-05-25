### 283. Move Zeroes
Easy

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

**Example:**
```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Note:**
```
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
```

**Tags**
- Array
- Two Pointers

### Solution:
- Intuition: find the first non-zero number and move it to the first spot
- Find the next non-zero, and move it to the second spot
- Do this until you don't have any more non-zero numbers
- then replace the rest of the array with zeroes
- You can do this in linear time instead of O(n^2) by having a replaceIndex and a currentIndex. 
- ReplaceIndex points to index 0. Current Index just finds the first non-zero. If found, move it to replaceIndex
- Then increment replaceIndex.
- When there are no more zeroes, replace the rest of the array with zeroes using the last place of replaceIndex and increment
```
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let swapIndex = 0
    let currIndex = 0
    
    while (currIndex < nums.length) {
        if (nums[currIndex] !== 0) {
            nums[swapIndex] = nums[currIndex];
            swapIndex += 1
        }
        
        currIndex += 1
    }
    
    while (swapIndex < nums.length) {
        nums[swapIndex] = 0
        swapIndex += 1
    }
};
```
