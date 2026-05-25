### 31. Next Permutation
Medium

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory. 

**Example 1:**
```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2:**
```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3:**
```
Input: nums = [1,1,5]
Output: [1,5,1]
``` 

**Constraints:**
```
1 <= nums.length <= 100
0 <= nums[i] <= 100
```

**Tags**
- Revisit
- non-intuitive
- Array
- Two Pointers

### Solution
```
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
            The brute force approach is to generate all
            permutations of the array, sort it and then
            find the next permutation that matches the
            current array. Then return the next permutation
            to it. Generating permutations is non-polynomial
            so this is not ideal.
            
            The trick is this:
            Starting from the right of the array, find the 
            first element, a[i], where it is less than its right
            element, a[i + 1].
            
            Then starting from the right again, find the first
            element that is greater than the element found in
            the first step.
            
            Swap those two numbers.
            
            Then reverse the array after the element found in step 1.
        """
        length = len(nums)
        ptr = length - 2
        
        def swap(nums, a, b):
            nums[a], nums[b] = nums[b], nums[a]
            
        def reverse(nums, index):
            mid = index + (length - 1 - index) // 2
            end = length - 1
            
            while index <= mid:
                swap(nums, index, end)
                index += 1
                end -= 1
            
        while ptr >= 0 and nums[ptr] >= nums[ptr + 1]:
            ptr -= 1
        
        first = ptr
        if ptr >= 0:
            ptr = length - 1

            while ptr >= 0 and nums[first] >= nums[ptr]:
                ptr -= 1
            
            swap(nums, first, ptr)
        
        reverse(nums, first + 1) 
            
        
        
        
```
