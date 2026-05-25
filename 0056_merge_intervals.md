### 56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Example 1:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
``` 

**Constraints:**
```
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
```

**Tags**
- Array
- Sorting

### Solution:
- if the last element's end is greater than the next element's first, then we have an overlap!
```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            Sort the intervals list by the start times
            Then create an result array
            For each interval in intervals:
            - add it to the result list if the result is empty
            - otherwise: take the last element of the result array
            - if they overlap: merge combined interval
            - otherwise: add back the removed interval and the new interval
            return result
        """
        result = []
        
        # sort the intervals by the first element
        intervals = sorted(intervals, key=operator.itemgetter(0))
        
        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            
            last = result.pop()
            if last[1] >= interval[0]:
                result.append([min(last[0], interval[0]), max(last[1], interval[1])])
            else:
                result.append(last)
                result.append(interval)
                
        
        return result
        
        
```
