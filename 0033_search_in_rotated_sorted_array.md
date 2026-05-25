### 33. Search in Rotated Sorted Array
Medium

Medium

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1. 

**Example 1:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**
```
Input: nums = [1], target = 0
Output: -1
``` 

**Constraints:**
```
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
```

**Tags**
- Array
- Binary Search

### Solution:
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = start + ((end - start) // 2)
            if nums[middle] == target:
                return middle
            
            if nums[start] <= nums[middle]:
                if nums[start] <= target <= nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            
            if nums[middle] <= nums[end]:
                if nums[middle] <= target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        
        return -1
            
```
