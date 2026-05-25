### 435. Non-overlapping Intervals
Medium

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Example 1:**
```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```

**Example 2:**
```
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```

**Example 3:**
```
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
``` 

**Note:**
```
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
```

**Tags**
- Array
- Dynamic Programming
- Greedy
- Sorting

### Solution:
- Sort the intervals.
- Then, compare the first interval with its next interval.
- If there is an overlap, increment a count and compare the first interval with the next interval.
- Otherwise, compare the second interval with the next interval. So on...

```
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals = intervals.sort((a, b) => {
        if (a[0] < b[0]) {
            return -1;
        }
        if (a[0] > b[0]) {
            return 1;
        }
        
        if (a[1] < b[1]) {
            return -1;
        }
        
        if (a[1] < b[1]) {
            return 1;
        }
        
        return 0;
    });
    
    let count = 0;
    let current = intervals[0];
    let nextPtr = 1;
    while (nextPtr < intervals.length) {
        let next = intervals[nextPtr];
        if (current[1] <= next[0]) {
            current = next;
            nextPtr += 1;
            continue;
        }
        
        if (current[1] < next[1]) {
            nextPtr += 1;
            count += 1;
            continue;
        }
        
        count+=1;
        nextPtr += 1;
        current = next;
    }
    
    return count;
};
```
