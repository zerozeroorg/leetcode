### 1539. Kth Missing Positive Number
Easy

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array. 

**Example 1:**
```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
```

**Example 2:**
```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
``` 

**Constraints:**
```
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
```


**Tags**
- Array
- Binary Search

### Solution:
```
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
            Keep a counter at 1
            Set a pointer at the beginning of arr
            while pointer < len(arr):
            - check if the number at pointer is equal to counter
            - if it is, increment counter and pointer
            - if not, decrement K, and increment counter
            - if K == 0, return counter
            
            if K > 0:
                return counter + (K - 1) 
        """
        counter = 1
        ptr = 0
        while ptr < len(arr):
            num = arr[ptr]
            if num == counter:
                ptr += 1
            else:
                k -= 1
            
            if k == 0:
                return counter
            counter += 1
        
        if k > 0:
            return counter + (k - 1)
        
```
