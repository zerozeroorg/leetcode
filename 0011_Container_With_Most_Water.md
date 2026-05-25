### 11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
 

**Example 1:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**
```
Input: height = [1,1]
Output: 1
``` 

**Constraints:**
```
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
```

**Tags**
- revisit
- Array
- Two Pointers
- Greedy

### Solution
Realize that you can choose any two heights and ignore any heights in between to form your container.

First, we check the widest possible container starting from the first line to the last one. Next, we ask ourselves, how is it possible to form an even bigger container? Every time we narrow the container, the width becomes smaller so the only way to get a bigger area is to find higher lines. So why not just greedily shrink the container on the side that has a shorter line? Every time we shrink the container, we calculate the area and save the maximum.
```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        best = 0
        first = 0
        last = length - 1
        
        while first < last:
            first_wall = height[first]
            last_wall = height[last]
            min_height = min(first_wall, last_wall)
            best = max(best, min_height * (last - first))
            
            if first_wall < last_wall:
                first += 1
            else:
                last -= 1
        
        return best
```
