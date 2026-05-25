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
- Create a hash table of num -> index
- Then iterate array again and get target - num
- If it exists in the hash table and it does not equal to current index, then we have a match!

You don't have to build the hash table right away. You can go through each num and calculate the difference. If the difference is not in the hash table (meaning I haven't encountered it yet) then store the current num's index into the hash table.
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Since I have to return the indices, I cannot sort them.
            So use a map that stores lookup[target - num] = [index]
            
            Then iterate the array again and check if a num exists in the
            lookup. If it does, return that index, and the lookup index.
        """
        lookup = collections.defaultdict(list)
        length = len(nums)
        
        for i in range(length):
            num = nums[i]
            lookup[target - num].append(i)
        
        for i in range(length):
            num = nums[i]
            possible = len(lookup[num])
            if possible == 0:
                continue
            if possible > 1:
                return [lookup[num][0], lookup[num][1]]
            elif i not in lookup[num]:
                return [i, lookup[num][0]]
                
        
        return None
```
