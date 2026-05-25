### 978. Longest Turbulent Subarray
Medium

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
```
For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
``` 

**Example 1:**
```
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
```

**Example 2:**
```
Input: arr = [4,8,12,16]
Output: 2
```

**Example 3:**
```
Input: arr = [100]
Output: 1
``` 

**Constraints:**
```
1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109
```

**Tags**
- Array
- Dynamic Programming
- Sliding Window

### Solution
```
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
            UGH - in case of [9,9], the pattern should be None. So in my plan below,
            I have to check if there is a pattern in the very last else. Also, return max(global_max, max)
            because a max might not be computed yet.
            
            Set pointer to 1 index
            Set global_max = 0
            Set local_max = 1
            while pointer is < length:
            - check the next number
            - if i have a pattern:
                - if adding the number makes the pattern correct, then increment local_max
                and increment the pointer
                - else, check if the two numbers are equal
                    - unset the pattern
                    - set global_max = max(global_max, local_max)
                    - set pointer to the next number
                    - set local_max = 1
                - else, two numbers are not equal
                    - update the pattern based on the two numbers
                    - set global_max = max(global_max, local_max)
                    - set pointer to the next number
                    - set local_max = 2                
            - else set the pattern and increment local_max and move pointer
        """
        pointer = 1
        global_max = 1
        local_max = 1
        length = len(arr)
        pattern = None
        
        while pointer < length:
            if pattern:
                if pattern == 'up' and arr[pointer - 1] > arr[pointer]:
                    pattern = 'down'
                    local_max += 1
                    pointer += 1
                elif pattern == 'down' and arr[pointer - 1] < arr[pointer]:
                    pattern = 'up'
                    local_max += 1
                    pointer += 1
                elif arr[pointer - 1] == arr[pointer]:
                    pattern = None
                    global_max = max(global_max, local_max)
                    pointer += 1
                    local_max = 1
                else:
                    pattern = 'up' if arr[pointer - 1] < arr[pointer] else 'down'
                    global_max = max(global_max, local_max)
                    pointer += 1
                    local_max = 2
            elif arr[pointer - 1] == arr[pointer]:
                pattern = None
                global_max = max(global_max, local_max)
                pointer += 1
                local_max = 1                
            else:
                pattern = 'up' if arr[pointer - 1] < arr[pointer] else 'down' 
                local_max += 1
                pointer += 1
        
        return max(global_max, local_max)
```

### Leetcode Solution
```
For example, take an array like A = [9,4,2,10,7,8,8,1,9]. The comparisons are [1,1,-1,1,-1,0,-1,1]. The blocks are [1], [1,-1,1,-1], [0], [-1,1].

Algorithm

Scan the array from left to right. If we are at the end of a block (last elements OR it stopped alternating), then we should record the length of that block as our candidate answer, and set the start of the new block as the next element.
```
