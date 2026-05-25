### 540. Single Element in a Sorted Array
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space. 

**Example 1:**
```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```

**Example 2:**
```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
``` 

**Constraints:**
```
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
```

**Tags**
- Revisit
- Array
- Binary Search

### Solution
```
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
            Split the array into half
            One half should have an even set of nums
            The other half will not
            Find that one that doesn't have the even set,
            then continue to binary search on that.
            
            [1 1 2 2 3 3 4]
             f     m     l
        """
        length = len(nums)
        first = 0
        last = length - 1
        
        if length == 1:
            return nums[0]
        
        while first <= last:
            middle = first + ((last - first) // 2)
            
            if nums[first] != nums[first + 1]:
                return nums[first]
            
            if nums[last] != nums[last - 1]:
                return nums[last]
            
            if nums[middle] != nums[middle - 1] and nums[middle] != nums[middle + 1]:
                return nums[middle]
            
            if nums[middle] == nums[middle - 1]:
                if (middle - first + 1) % 2 == 0:
                    first = middle + 1
                else:
                    last = middle
            elif (last - middle + 1) % 2 == 0:
                last = middle - 1
            else:
                first = middle
        
        return -1
            
```
