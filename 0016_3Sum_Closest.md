### 16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution. 

**Example 1:**
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
``` 

**Constraints:**
```
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
```

**Tags**
- Array
- Two Pointers
- Sorting

### Solution
- Refresher on 3sum https://learnersbucket.com/examples/algorithms/3-sum-problem-algorithm/
- It must be a O(n^2) algorithm because of cases like this [-4, -1, -1, 0, 1, 2] where you have to try out all combos to reach -1, -1, 0 set.
```
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
            Sort the array
            Loop through i...len(nums) - 3:
            Get j = i + 1
            Get k = len(nums) - 1
            Get the sum of nums[i] + nums[j] + nums[k]
            Update closestSum
            If sum < target, update right k. Else, update j.
            return closest sum
        """
        nums.sort()
        closestSum = None
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                result = nums[i] + nums[j] + nums[k]
                
                if closestSum is None:
                    closestSum = result
                elif abs(closestSum - target) > abs(result - target):
                    closestSum = result
                    
                if target < result:
                    k -= 1
                else:
                    j += 1
            
        return closestSum
```
