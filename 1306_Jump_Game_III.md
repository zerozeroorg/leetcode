### 1306. Jump Game III
Medium

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time. 

**Example 1:**
```
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
```

**Example 2:**
```
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
```

**Example 3:**
```
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
``` 

**Constraints:**
```
1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
```

**Tags**
- Revisit
- Array
- Depth-First Search
- Breadth-First Search

### Solution
- I messed up where I had only a visited array that only recorded if you visited in any direction. I have to record visited going from the left, or going from the right.
- You don't need DP. Just use DFS with a visited array. Worse case, you will need to explore all `arr.length * 2` and having a single visited array is fine. Don't need to record going left or right. You just have to set visited, then explore both left and right.
```
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        visited = [[False, False] for i in range(length)]
        dp = [None] * length
        
        def helper(position):
            if arr[position] == 0:
                return True
            
            if dp[position] is not None:
                return dp[position]
            
            if 0 <= position - arr[position] < length and not visited[position][0]:
                visited[position][0] = True
                left_result = helper(position - arr[position])
                if left_result:
                    dp[position] = True
                    return dp[position]
            
            if 0 <= position + arr[position] < length and not visited[position][1]:
                visited[position][1] = True
                right_result = helper(position + arr[position])
                if right_result:
                    dp[position] = True
                    return dp[position]
            
            dp[position] = False
            visited[position] = [False, False]
            return dp[position]
            
        
        
        return helper(start)
        
```
Better, intuitive solution I copied from leetcode:
```
visited = set()
    def helper(ind):
        nonlocal visited
        if ind in visited:
            return 
        if 0 <= ind < len(arr):
            if arr[ind] == 0:
                return True
            visited.add(ind)
            return  helper(ind + arr[ind]) or helper(ind - arr[ind])
        
    return helper(start)
```
