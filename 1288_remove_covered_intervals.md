### 1288. Remove Covered Intervals
Medium

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals. 

**Example 1:**
```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```

**Example 2:**
```
Input: intervals = [[1,4],[2,3]]
Output: 1
```

**Example 3:**
```
Input: intervals = [[0,10],[5,12]]
Output: 2
```

**Example 4:**
```
Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2
```

**Example 5:**
```
Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
``` 

**Constraints:**
```
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= intervals[i][0] < intervals[i][1] <= 10^5
All the intervals are unique.
```
**Tags**
- Array
- Sorting

### Solution:
- This is a typical interval problem:
- Sort the intervals
- Push the first interval into a result array
- Compare the last interval in result with the next interval
- If they cover each other, merge them
- If not, add it to the interval to the result array

```
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var removeCoveredIntervals = function(intervals) {
    intervals = intervals.sort((a, b) => {
        if (a[0] < b[0]) {
            return -1;
        }
        if (a[0] > b[0]) {
            return 1;
        }
        if(a[1] < b[1]) {
            return -1;
        }
        if(a[1] > b[1]) {
            return 1;
        }
        return 0;
    });
    
    let result = [intervals.shift()];
    
    intervals.forEach(interval => {
        let top = result[result.length - 1];
        if ((top[0] <= interval[0] && interval[1] <= top[1]) || 
           (interval[0] <= top[0] && top[1] <= interval[1])) {
            result[result.length - 1] = [Math.min(top[0], interval[0]), Math.max(top[1], interval[1])];
        } else {
            result.push(interval);
        } 
    });
    
    return result.length;
};
```
