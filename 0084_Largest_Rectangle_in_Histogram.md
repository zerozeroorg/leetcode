### 84. Largest Rectangle in Histogram
Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Example 1:**
```

      +
    + +
    + +
    + +   +
+   + + + +
+ + + + + +

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

**Example 2:**
```

  +
  +
+ +
+ +
Input: heights = [2,4]
Output: 4
``` 

**Constraints:**
```
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
```

**Tags**
- Revisit
- unsolved
- Array
- Stack
- Monotonic Stack

### Solution
Brute Force
- The brute force is to calculate the max area between each pair of column from i -> j while also taking into account that there is a min height between i and j.
- For each i:
- min height = i
- for each j where j >= i:
- min height = min(min_height, j)
- max area = max(max_area, min_height * (j - i + 1))
- But this is O(n^2) which is too slow
- The fastest solution is below
```
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            use a monotonic stack
            the idea is that having an increasing size
            of rectangles in the stack will tell you that the max
            rectangle size is current rectangle * number of rectangles
            between the left and right side.
            
            Once a smaller rectangle is placed, then you can do the calculation
            mentioned above.
            
            If after going through the rectangles, there are some left in the stack
            then pop it off and calculate rectangle size from end to the first rectangle
            that is smaller than it.
        """
        stack = []
        length = len(heights)
        best = 0
        
        for index in range(length):
            if not stack or heights[stack[-1]] < heights[index]:
                stack.append(index)
                continue
            
            while stack and heights[stack[-1]] > heights[index]:
                top_index = stack.pop()
                height = heights[top_index]
                next_index = stack[-1] if stack else -1
                rectangle = height * (index - next_index - 1)
                best = max(best, rectangle)
            
            stack.append(index)

        while stack:
            top_index = stack.pop()
            height = heights[top_index]
            next_index = stack[-1] if stack else -1
            rectangle = (length - 1 - next_index) * height 
            best = max(best, rectangle)
    
        return best
        
```
