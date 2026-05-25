### 42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining. 

**Example 1:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**
```
Input: height = [4,2,0,3,2,5]
Output: 9
``` 

**Constraints:**
```
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
```

**Tags**
- Array
- Two Pointers
- Dynamic Programming
- Stack
- Monotonic Stack

### Solution
The amount of water that can be trapped is determined by the left wall, right wall, and current height.
For something like `[2, 0, 3]`, the amount of water trapped is `min(left_wall, right_wall) - current_height` so the answer here is 2.
```
class Solution:
    def trap(self, height: List[int]) -> int:
        """
            For each num, get the max left wall and the max right wall
            Get the min of each of these walls
            subtract the current num from that wall
            if it is positive, then add. Otherwise, skip.
            return result
        """
        result = 0
        length = len(height)
        
        if length < 2:
            return 0
        
        left_max = [0 for i in range(length)]
        right_max = [0 for i in range(length)]
        
        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        
        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        
        for i in range(length):
            possible_water = min(left_max[i], right_max[i])
            delta = possible_water - height[i]
            if delta > 0:
                result += delta

        return result
        
        
```
