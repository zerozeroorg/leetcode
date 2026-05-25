### 238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

**Example:**
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
```

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

**Tags**
- Array
- Prefix Sum

### Solution:
- create a product array multiplying numbers from the left (prefix array)
- create a product array multiplying numbers from the right (postfix array)
- iterate through the array and get the prefix product and multiply by postfix product
- HOWEVER, below is a constant space solution.
- Instead of creating 2 arrays for prefix and postfix arrays, you can compute the prefix and postfix values as you iterate. This uses the answer array to store the prefix array values first, then iterating the array backwards to get the postfix value.
- You would need a cumulator for the prefix value and the postfix value
```
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = nums[i] * p
        
        return out
```
