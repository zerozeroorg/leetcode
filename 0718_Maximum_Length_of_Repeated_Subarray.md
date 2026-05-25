### 718. Maximum Length of Repeated Subarray
Medium

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
 

**Example 1:**
```
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

**Example 2:**
```
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
``` 

**Constraints:**
```
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
```

**Tags**
- Array
- Binary Search
- Dynamic Programming
- Sliding Window
- Rolling Hash
- Hash Function

### Solution
```
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            Create DP matrix like the following:
            
                1  2  3  2  1
                
            3   0  0  1  0  0
            2   0  1  0  2  0
            1   1  0  0  0  3
            4   0  0  0  0  0
            7   0  0  0  0  0
            
            Where dp[i][j] is the max length of subarray that ends at nums1[i] and nums2[j].
            
            To compute this dp matrix, first initialize the dp matrix with all zeroes.
            Then go through each combination of num1 and num2 and see if they match. If they
            match, then add 1 + dp[row - 1][col - 1].
            
            1st mistake: making sure the rows and cols are lined up based on nums1 and nums2.
            I mixed the two and get out of bounds when nums1 = [1,2,3] and nums2 = [1,2]
            
            2nd mistake: only add the number at dp[row - 1][col - 1] when nums1[row] == nums2[col]
            
        """
        rows = len(nums1)
        cols = len(nums2)
        dp = [
            [0] * cols for _ in range((rows))
        ]
        
        maxCount = 0
        
        for row in range(rows):
            for col in range(cols):
                num1 = nums1[row]
                num2 = nums2[col]
                if num1 == num2:
                    dp[row][col] += 1
                    if 0 <= row - 1 < rows and 0 <= col - 1 < cols:
                        dp[row][col] += dp[row - 1][col - 1]
                
                maxCount = max(maxCount, dp[row][col])
                
        return maxCount
```
