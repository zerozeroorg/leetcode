### 88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
 

**Example 1:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Example 2:**
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
``` 

**Constraints:**
```
0 <= n, m <= 200
1 <= n + m <= 200
nums1.length == m + n
nums2.length == n
-109 <= nums1[i], nums2[i] <= 109
```

**Tags**
- Array
- Two Pointers
- Sorting

### Solution:
To achieve constant space and linear time, we can have two pointers: one at the end of `nums2` and the other at the end of `nums1` minus the length of the zeroes (or length of nums2). We will also have a pointer at the end of nums1, `ptr`, to start the num placement. Since thy are both sorted, we take the biggest one of each and put it where `ptr` is located. Continue until both arrays reach the beginning of their respective arrays.

```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        My idea: copy them to a extra array then copy extra back to nums1.
        
        Instead: have two pointers start at the end (so you don't overrwrite your data!)
        Of the two pointers, take the biggest one.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        last = m + n - 1
        
        while last >= 0:
            a = nums1[ptr1] if ptr1 >= 0 else float('-inf')
            b = nums2[ptr2] if ptr2 >= 0 else float('-inf')            

            if a > b:
                nums1[last] = a
                ptr1 -= 1
            else:
                nums1[last] = b
                ptr2 -= 1

            last -= 1

```
