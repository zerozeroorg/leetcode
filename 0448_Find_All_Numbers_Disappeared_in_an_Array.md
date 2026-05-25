### 448. Find All Numbers Disappeared in an Array
Easy

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums. 

**Example 1:**
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

**Example 2:**
```
Input: nums = [1,1]
Output: [2]
``` 

**Constraints:**
```
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
``` 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

**Tags**
- Revisit
- Array
- Hash Table

### Solution
```
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            With no extra space, you can use the original array
            and modify it.
         
            Go through the array.
            
            For each number, mark the number it is suppose to be at with a negative
            sign. Do not change the number.
            
            This marking with a negative sign will mean that we have a number
            at that index.
            
            Numbers that are not marked negative means its position was never
            visited, so those are missing numbers.
        """
        ans = []
        length = len(nums)
    
        for num in nums:
            position = abs(num) - 1
            nums[position] = -abs(nums[position])
        
        for i in range(length):
            if nums[i] > 0:
                ans.append(i + 1)
        
        return ans
        
        
        
```
