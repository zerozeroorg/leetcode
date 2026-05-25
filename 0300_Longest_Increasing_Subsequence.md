### 300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
 
**Example 1:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
``` 

**Constraints:**
```
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
``` 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

**Tags**
- Array
- Binary Search
- Dynamic Programming

### Solution
- At first, I thought of using a 2D matrix that builds the LIS based on the previous cells
- But that is wrong because it will fail for [0,1,0,3,2,3]
- The idea is to assume that you have a lookup table that will tell you what is the Longest increasing subsequence ending at nums[i]
- Now let's say we add a new number at the end of nums, called j
- Then for each nums[0...i] check if you can form an increasing subsequence with nums[j]
- If you can, then compute the Longest increasing subsequence ending at nums[j]
- The max of this lookup table will be the longest increasing subseqence

```
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            Bottom up approach
            Create an array where dp[i] holds the length of the longest
            increasing subsequence ending in nums[i].
            
            Grab nums[i + 1].
            Check j where j is in [0...i] and 
            - see if nums[j] < nums[i + 1]
            - if it is not, continue
            - if it is, then update dp[i + 1] = max(dp[i + 1], dp[j] + 1)
            
            Return the max in dp.
        """
        dp = [1] * len(nums)
        start = 1
        maxCount = 1
        
        while start < len(nums):
            for j in range(start):
                if nums[j] >= nums[start]:
                    continue
                dp[start] = max(dp[start], dp[j] + 1)
                maxCount = max(maxCount, dp[start])
            start += 1
            
        return maxCount
```
