### 739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead. 

**Example 1:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
``` 

**Constraints:**
```
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
```

**Tags**
- Revisit
- Array
- Stack
- Monotonic Stack

### Solution
- Did it the brute force way, but it is too slow. Had to look up the answer.
- From leetcode website: `Monotonic stacks are a good option when a problem involves comparing the size of numeric elements, with their order being relevant.`
- Use monotonic decreasing stack.
```
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append(index)
                continue
            
            if temperatures[stack[-1]] > temp:
                stack.append(index)
                continue
                
            while stack and temperatures[stack[-1]] < temp:
                top = stack.pop()
                ans[top] = index - top
            
            stack.append(index)
        
        
        return ans
            
        
```
