### 1679. Max Number of K-Sum Pairs
Medium

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array. 

**Example 1:**
```
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
```

**Example 2:**
```
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
``` 

**Constraints:**
```
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
```

**Tags**
- Array
- Hash Table
- Two Pointers
- Sorting

### Solution:
- My solution is O(n log n) time, but O(1) constant space.
- The fastest solution is O(n) time, but with O(n) space. It is below mine.
```
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
            Sort then use two pointer sum
        """
        nums.sort()
        ptr1 = 0
        ptr2 = len(nums) - 1
        count = 0
        
        while ptr1 < ptr2:
            total = nums[ptr1] + nums[ptr2] 
            if total == k:
                count += 1
                ptr1 += 1
                ptr2 -= 1
            elif total < k:
                ptr1 += 1
            else:
                ptr2 -= 1
       
        return count
        
```
### Faster solution:
```
class Solution:
    def maxOperations(self, nums, k):
        cnt, ans = Counter(nums), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans//2
```
