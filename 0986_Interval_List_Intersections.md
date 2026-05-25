### 986. Interval List Intersections
Medium

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
 

**Example 1:**
```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

**Example 2:**
```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

**Example 3:**
```
Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
```

**Example 4:**
```
Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
``` 

**Constraints:**
```
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 10^9
endi < starti+1
0 <= startj < endj <= 10^9
endj < startj+1
```

**Tags**
- Array
- Two Pointers
- Sweep Line

### Solution
There is a more concise version below provided by LeetCode

```
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
            Create an result array
            Create a merged stack
            pick the smallest from first or last
            add to merged stack if empty
            if not empty:
            - if overlaps with top, add overlap to result array. then add merged interval
            - if not overlap, then add to stack
        """
        result = []
        merged = []
        
        def getSmallest(listA, listB):
            if listA and not listB:
                return listA.pop(0)
            if listB and not listA:
                return listB.pop(0)
            
            if listA[0][0] < listB[0][0]:
                return listA.pop(0)
            else:
                return listB.pop(0)
            
        while firstList or secondList:
            item = getSmallest(firstList, secondList)
            
            if not merged:
                merged.append(item)
                continue
            
            if item[0] <= merged[-1][1]:
                top = merged.pop()
                merged.append([min(top[0], item[0]), max(top[1], item[1])])
                result.append([max(top[0], item[0]), min(top[1], item[1])])
            else:
                merged.append(item)
            
        
        return result
        
```

LeetCode Solution
```
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
```
