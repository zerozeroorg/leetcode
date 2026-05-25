### 941. Valid Mountain Array
Easy

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
```
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Mountain: [0 1 2 3 4 5 3 2 1 0]
Not Mountain because not strictly increasing/decreasing: [0 1 2 3 3 5 2 1]
```

**Example 1:**
```
Input: arr = [2,1]
Output: false
```

**Example 2:**
```
Input: arr = [3,5,5]
Output: false
```

**Example 3:**
```
Input: arr = [0,3,2,1]
Output: true
``` 

**Constraints:**
```
1 <= arr.length <= 104
0 <= arr[i] <= 104
```


**Tags**
- Array

### Solution:
- Simpler solution: walk up the array until you can't. Then walk down the array.
- Simpler solution below
```
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
            First, check if the array length is >= 3. If not, return False
            iterate through each element in the array:
                - Compare myself to the next element
                - If I am increasing and the next element is bigger: continue
                - If I am increasing and the next element is smaller but my prev element
                is smaller, switch to decreasing and continue
                - If I am decreasing and the next element is smaller: continue
                - return False
            return True
            Edge cases:
            - need to consider at the end, if it was increasing or decreasing
            - 3,5,5 returned true when it should be false. I have to check this
        """
        N = len(arr)
        if N < 3:
            return False
        
        STATE = 'increasing'
        for index in range(N - 1):
            nextNum = arr[index + 1]
            if STATE is 'increasing':    
                if arr[index] < nextNum:
                    continue
                elif index - 1 >= 0 and arr[index - 1] < arr[index] > nextNum:
                    STATE = 'decreasing'
                    continue
                else:
                    return False
            else:
                if arr[index] > nextNum:
                    continue
                else:
                    return False
        
        return True if STATE is 'decreasing' else False
            
        
```

### Simpler Solution:
```
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
```
