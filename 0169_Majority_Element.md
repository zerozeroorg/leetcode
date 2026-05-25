169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array. 

**Example 1:**
```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
``` 

**Constraints:**
```
n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= (2^31) - 1
``` 

Follow-up: Could you solve the problem in linear time and in O(1) space?

**Tags**
- Array
- Hash Table
- Divide and Conquer
- Sorting
- Counting

### Solution
- Below is the hashmap solution
- The linear time, constant space uses Boyer-Moore Voting Algorithm
```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        length = len(nums)
        size = length // 2
        
        for num in counter.keys():
            if counter[num] > size:
                return num
```
The Boyer Moore Voting from LeetCode
```
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```
