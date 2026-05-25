### 70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

**Example 1:**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
``` 

**Constraints:**
```
1 <= n <= 45
```

**Tags**
- Math
- Dynamic Programming
- Memoization

### Solution
```
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        
        def helper(steps_left):
            count = 0
            
            if steps_left == 0:
                return 1
            
            if dp.get(steps_left) is not None:
                return dp.get(steps_left)
            
            if steps_left - 1 >= 0:
                count += helper(steps_left - 1)
            
            if steps_left - 2 >= 0:
                count += helper(steps_left - 2)
            
            dp[steps_left] = count
            return dp[steps_left]
                
        
        return helper(n)
        
```
