### 560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

**Example 1:**
```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Example 2:**
```
Input: nums = [1,2,3], k = 3
Output: 2
``` 

**Constraints:**
```
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
```
**Tags**
- Revisit
- Array
- Hash Table
- Prefix Sum

### Solution
- Build every subarray, add there sums. This is O(n^2) to get every subarray and O(n) to add each of them so the total run time is O(n^3). Too slow.
- Build a prefix sum array and for reach i <= j, get calculate subarray sum in constant time: `prefix[j] - prefix[i]`. This is O(n^2). Too slow for python.
- Use a hash map that will store the prefix sums as you iterate through the array. If you encounter a prefix sum such that `prefix[j] - k` is in the map, increment the count by that many occurrences.
```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_lookup = {}
        current_sum = 0
        total = 0
        
        # this is for the case where arr = [1], k = 1 or in other words there is at least a zero sum when the array total = k.
        prefix_lookup[current_sum] = 1
        
        for num in nums:
            current_sum += num
            
            if current_sum - k in prefix_lookup:
                total += prefix_lookup[current_sum - k]
            
            if current_sum not in prefix_lookup:
                prefix_lookup[current_sum] = 0
            
            prefix_lookup[current_sum] += 1
        
        return total
            
```
