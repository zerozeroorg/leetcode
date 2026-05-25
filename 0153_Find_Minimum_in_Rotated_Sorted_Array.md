### 153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time. 

**Example 1:**
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

**Example 3:**
```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
``` 

**Tags**
- Revisit
- Array
- Binary Search

**Constraints:**
```
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
```

### Solution
```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            Use binary search 
            
            set first, middle and last
            if first <= last, then return first
            else there are a few cases:
            
            1. check if middle is bigger than last.
            if it is, then you want first = middle + 1
            
            2. middle < last. We have to decide first -> middle or middle -> last.
            If middle - 1 < middle, then pick first -> middle - 1. 
            Otherwise, middle + 1 -> last
        """
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            if nums[first] <= nums[last]:
                return nums[first]
            
            middle = first + ((last - first) // 2)
            if nums[middle] > nums[last]:
                first = middle + 1
                continue
            
            if middle - 1 >= 0 and nums[middle - 1] < nums[middle]:
                last = middle - 1
            else:
                first = middle
        
```
