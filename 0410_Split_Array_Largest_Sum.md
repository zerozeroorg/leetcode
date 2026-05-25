### 410. Split Array Largest Sum
Hard

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays. 

**Example 1:**
```
Input: nums = [7,2,5,10,8], m = 2
Output: 18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

**Example 2:**
```
Input: nums = [1,2,3,4,5], m = 2
Output: 9
```

**Example 3:**
```
Input: nums = [1,4,4], m = 3
Output: 4
```

**Constraints:**
```
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
```

**Tags**
- Revisit
- Array
- Binary Search
- Dynamic Programming
- Greedy
- Prefix Sum

### Solution
- There are two solutions: DP and Binary Search
```
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # compute the prefix sum
        prefix = [0]
        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1] + num)
                
        prefix_length = len(prefix)
        length = len(nums)

        # build dp 2d matrix: dp[index][m]
        dp = [[None for i in range(m + 1)] for i in range(length + 1)]
        
        maximum = float('inf')

        # use top down dp
        def recurse(index, m):
            
            # use memo-ized answer
            if dp[index][m] is not None:
                return dp[index][m]
            
            # base case: when m == 1, then the rest of the array goes to index
            if m == 1:
                dp[index][m] = prefix[-1] - prefix[index]
                return dp[index][m]
            
            # then try to split the rest of the array into m parts
            start = index
            best = maximum
            while start <= length - m:
                first_split = prefix[start + 1] - prefix[index]
                
                best_from_this_split = max(
                    first_split,
                    recurse(start + 1, m - 1)
                )
                best = min(best, best_from_this_split)
                
                # optimization: if the first split is greater than rest then adding more
                # wont yield a better result
                if first_split >= best:
                    break
                
                start += 1
                
            dp[index][m] = best
            return dp[index][m]
    
        
        return recurse(0, m)
        
```
Binary Search
```
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
            We use binary search and guess the answer
            The low value is the max number in the array.
            The high value is the sum of all numbers in the array.
            
            We guess the answer is in the middle of those two values.
            
            To verify the guess is correct, we do this:
            - break up the array so that each subarray is at most the middle value
            - if the count of those subarrays is less than m, then it is too high
            - if the count of those subarrays is more than m, then it is too low
            
            Ok we found an answer where we matched m, set that as the new high
            and see if we can go lower.
            
            Return high
        """
        low = max(nums)
        high = sum(nums)
        
        while low < high:
            middle = (low + high) // 2
            
            total = 0
            count = 1
            
            for num in nums:
                if total + num <= middle:
                    total += num
                else:
                    total = num
                    count += 1
                
            if count > m:
                low = middle + 1
            else:
                high = middle
        
        return high
            
```
