### 496. Next Greater Element I
Easy

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
 

**Example 1:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
```

**Example 2:**
```
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
``` 

**Constraints:**
```
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10^4
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
``` 

Follow up: Could you find an O(nums1.length + nums2.length) solution?

**Tags**
- Revisit
- Array
- Hash Table
- Stack
- Monotonic Stack

### Solution
I did the 0(n^2) solution. Below is the linear solution.

The idea is using a stack and a map.
- Iterate through the numbers in nums2.
- Compare the number with the number in stack. If it is number is greater than what's on top of the stack, then pop it and use the map to set the popped number to map to num2.
- The lookup will keep track of numbers and their greatest number to the right.
```
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        lookup = {}
        result = []
        
        for num2 in nums2:
            if not stack:
                stack.append(num2)
                continue
            
            while stack and stack[-1] < num2:
                lookup[stack[-1]] = num2
                stack.pop()
                
            stack.append(num2)
        
        for num1 in nums1:
            result.append(lookup.get(num1, -1))
        
        return result
                
```
