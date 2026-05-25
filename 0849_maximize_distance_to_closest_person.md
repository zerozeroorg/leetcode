### 849. Maximize Distance to Closest Person
Medium

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

**Example 1:**
```
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
```

**Example 2:**
```
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
```

**Example 3:**
```
Input: seats = [0,1]
Output: 1
``` 

**Constraints:**
```
2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
```

**Tags**
- Array

### Solution:
```
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
            First, get the list of occupied seats.
            If there is only one occupied seat, then get the
            max distance between the start seat->occupied vs occupied->end seat
            Otherwise, calculate the max distance between two pairs of seats
            Return the max
            
            DANG: there are corner cases where there are no unoccupied
            seats at the start and end of the row like this: [0, 0, 0, 1, 0, 1]
        """
        occupiedIndexes = collections.deque([])
        maxDistance = 0
        
        
        for index, seat in enumerate(seats):
            if seat == 1:
                occupiedIndexes.append(index)
        
        # get the edges
        firstIndex = occupiedIndexes[0]
        lastIndex = occupiedIndexes[-1]
        maxDistance = max(maxDistance, firstIndex)
        maxDistance = max(maxDistance, len(seats) - 1 - lastIndex)

        for i in range(len(occupiedIndexes) - 1):
            first = occupiedIndexes[i]
            last = occupiedIndexes[i + 1]
            maxDistance = max(maxDistance, math.floor((last - first) / 2) )
        
        return maxDistance
        
```
