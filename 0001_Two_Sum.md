### 1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
``` 

**Constraints:**
```
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
``` 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

**Tags**
- Array
- Hash Table

### Solution
A better way:
- Iterate the array. As you iterate, check if the difference between the target and current number is in the lookup
- If it is, then you have found its complement - return current num's index and the complement index via lookup
- If it is not, store the current num -> index so that if you iterate later in the array and it is a complement of another number, you found the answer

You don't have to build the hash table right away. You can go through each num and calculate the difference. If the difference is not in the hash table (meaning I haven't encountered it yet) then store the current num's index into the hash table.

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Value => Index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
```
