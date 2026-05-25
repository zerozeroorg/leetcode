### 485. Max Consecutive Ones
Easy

Given a binary array nums, return the maximum number of consecutive 1's in the array. 

**Example 1:**
```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

**Example 2:**
```
Input: nums = [1,0,1,1,0,1]
Output: 2
``` 

**Constraints:**
```
1 <= nums.length <= 105
nums[i] is either 0 or 1.
```

**Tags**
- Array

### Solution
```
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
            NOTE: update global_max after the end of the loop!!!!
            
            Use kandane's algorithm
            Have a global_max = 0
            Have a local_max = 0
            
            For each num in nums:
            - if num == 1:
                - increment local_max
            - else:
                - global_max = max(global_max, local_max)
                - local_max = 0
                
            Return max(global_max, local_max)
        """
        global_max = 0
        local_max = 0
        
        for num in nums:
            if num == 1:
                local_max += 1
            else:
                global_max = max(global_max, local_max)
                local_max = 0
        
        return max(global_max, local_max)
```
