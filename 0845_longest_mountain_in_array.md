### 845. Longest Mountain in Array
Medium

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

**Example 1:**
```
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
```

**Example 2:**
```
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
```

**Note:**
```
0 <= A.length <= 10000
0 <= A[i] <= 10000
```

**Follow up:**
- Can you solve it using only one pass?
- Can you solve it in O(1) space?


**Tags**
- Array
- Two Pointers
- Dynamic Programming
- Enumeration

### Solution:
```
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        """
            Brute force: for each number:
            - check the left and right of it
            - if it is left and right is less than it, then
            - have left check its left to make sure it is smaller
            - hae right check its right to make sure it is smaller
        """
        maxLength = 0
        
        def getMountainLength(nums, index):
            print(index)
            length = 1
            canGoLeft = True
            canGoRight = True
            rightMax = leftMax = nums[index]
            leftIndex = rightIndex = index
            
            while canGoLeft or canGoRight:
                left = nums[leftIndex - 1] if canGoLeft and leftIndex - 1 >= 0 else float('inf')
                right = nums[rightIndex + 1] if canGoRight and rightIndex + 1 < len(nums) else float('inf')
                if left < leftMax:
                    length += 1
                    leftMax = left
                    leftIndex -= 1
                else:
                    canGoLeft = False
                if right < rightMax:
                    length += 1
                    rightMax = right
                    rightIndex += 1
                else:
                    canGoRight = False
            
            return length
        
        for i in range(len(A)):
            current = A[i]
            left = A[i - 1] if i - 1 >= 0 else False
            right = A[i + 1] if i + 1 < len(A) else False
            if left is False or right is False:
                continue
            if left < current > right:
                maxLength = max(maxLength, getMountainLength(A, i))
        
        return maxLength
        
```
