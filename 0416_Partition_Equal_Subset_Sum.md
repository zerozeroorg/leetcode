### 416. Partition Equal Subset Sum
Medium

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. 

**Example 1:**
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**
```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
``` 

**Constraints:**
```
1 <= nums.length <= 200
1 <= nums[i] <= 100
```

**Tags**
- Revisit
- Array
- Dynamic Programming

### Solution
```
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            If the total is odd, then it cannot be divided
            Then you just need to select numbers such that
            those numbers == sum // 2
            
            So, in each iteration, check if you can select 
            the number or not select the number. 
            
            If any are True, return True. Return False otherwise.
            
            First, solve via brute force. Then add memoization
            with dp[sum][index] = True or False
        """
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        target = total // 2
        length = len(nums)
        dp = {}
        
        def helper(current_sum, index):
            if current_sum == 0:
                return True
            
            if index >= length or current_sum < 0:
                return False
            
            if dp.get(current_sum) and dp.get(current_sum).get(index) is not None:
                return dp[current_sum][index]
            
            if dp.get(current_sum) is None:
                dp[current_sum] = {}

            # select the number
            can_select_number = helper(current_sum - nums[index], index + 1)
            
            if can_select_number:
                dp[current_sum][index] = True
                return True
            
            # do not select number
            skip_number = helper(current_sum, index + 1)
            dp[current_sum][index] = skip_number

            return skip_number
    
        return helper(target, 0)
```
