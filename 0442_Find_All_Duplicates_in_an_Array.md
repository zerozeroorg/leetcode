### 442. Find All Duplicates in an Array
Medium

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
 

**Example 1:**
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

**Example 2:**
```
Input: nums = [1,1,2]
Output: [1]
```

**Example 3:**
```
Input: nums = [1]
Output: []
``` 

**Constraints:**
```
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
```

**Tags**
- Array
- Hash Table
- Sorting

### Solution
- There is a more clever solution below this one.
```
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ptr = 0
        length = len(nums)
        dups = []
        
        while ptr < length:
            num = nums[ptr]
            if num == ptr + 1:
                ptr += 1
                continue
            
            if num == 0:
                ptr += 1
                continue
            
            new_ptr = num - 1
            new_num = nums[new_ptr]
            
            if new_num == num:
                dups.append(num)
                nums[ptr] = 0
                ptr += 1
                continue
            
            nums[new_ptr] = num
            nums[ptr] = new_num
    
        return dups
        
```
Clever solution:
```
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        """
            Since we have to solve this problem in constant space complexity so the only way is to use the space of given array and manipulate it.
            Since the elements in the array are in range [1..n], we can consider the elements as idexes also and to be precise (element - 1) as it is a 0-indexed array.
            Since we can't use any extra space so let us mark the elements encountered in the given array only. This can be done by multiplying the element with -1.
            Now for each element, we will treat it as the index and check whether the value present at that index is visited or not. If it is visited then it is a duplicate else we mark that element as visited(multiply by -1).
        """
        for num in nums:
            if nums[abs(num) - 1] < 0:
                output.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return output
```
