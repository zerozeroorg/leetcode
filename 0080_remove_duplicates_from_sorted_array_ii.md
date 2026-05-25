### 80. Remove Duplicates from Sorted Array II
Medium

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
``` 

**Example 1:**
```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
Explanation: Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond the returned length.
``` 

**Constraints:**
```
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.
```

**Tags**
- Array
- Two Pointers

### Solution:
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            set a counter to 1
            set a matcher to the first element of the array
            set a pointer to the second element of the array
            while pointer < nums length:
                get element at pointer
                if element does not equal to matcher:
                    reset the counter to 1
                    matcher = element
                    increment pointer
                    continue
                increment counter
                if counter > 2:
                    remove element from nums
                    continue
                increment pointer
            
            return len(nums)
        """
        N = len(nums)
        if N < 2:
            return N
        
        counter = 1
        matcher = nums[0]
        ptr = 1
        
        while ptr < len(nums):
            element = nums[ptr]
            if element != matcher:
                counter = 1
                matcher = element
                ptr += 1
                continue
            
            counter += 1
            if counter > 2:
                del nums[ptr]
                continue
            
            ptr += 1
        
        return len(nums)
```
When you can't delete the array:
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            Have two pointers - 
            1. This one will set the k elements
            2. this one moves ahead to find what values to set for first pointer
            
            Have both those pointers at index 0
            set dup count = 0
            while second pointer < length - 1:
            if second pointer != second pointer + 1:
            move first and second pointer and set dup = 0
            else
            set dup count += 1
            if dup count > 2:
            move second pointer to next increasing number
            move first and second pointer
        """
        ptr1 = 0
        ptr2 = 0
        dup = 0
        length = len(nums)
        
        while ptr2 < length:
            if ptr2 == length - 1:
                nums[ptr1] = nums[ptr2]
                break
            
            current = nums[ptr2]
            next_ele = nums[ptr2 + 1]
            
            if current != next_ele:
                dup = 0
            else:
                dup += 1
            
            if dup > 1:
                while ptr2 < length - 1 and nums[ptr2 + 1] == current:
                    ptr2 += 1
                dup = 0
            
            nums[ptr1] = nums[ptr2]
            if ptr2 == length - 1:
                break
            
            ptr1 += 1
            ptr2 += 1
        
        return ptr1 + 1
        
```
