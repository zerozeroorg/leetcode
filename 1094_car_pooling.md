### 1094. Car Pooling
Medium

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

**Example 1:**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

**Example 2:**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Example 3:**
```
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
```

***Example 4:**
```
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
``` 
 
**Constraints:**
```
trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
```

**Tags**
- Array
- Sorting
- Heap (Priority Queue)
- Simulation
- Prefix Sum

### Solution:
- My original solution is a bit much!
- You can create a list of timestamps and store the +/- at each timestamp. Then, sort the timestamps and process them in order. NOTE: process both pick and dropoff
to get the real delta!
- Another solution is to use bucket sort.

**Original Solution:**
```
/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    let sortedTrips = trips.sort((a, b) => {
        if (a[1] < b[1]) {
           return -1;
        }
        if (a[1] > b[1]) {
            return 1;
        }
        
        if (a[2] < b[2]) {
            return -1;
        }
        
        if (a[2] > b[2]) {
            return 1;
        }
        
        return 0;
    });
    
    let count = 0;
    let tripsSoFar = [];
    
    for (let i = 0; i < sortedTrips.length; i++) {
        let trip = sortedTrips[i];
        let startTime = trip[1];
        if (tripsSoFar.length) {
            tripsSoFar = tripsSoFar.filter(trip => {
                if (trip[2] <= startTime) {
                    count -= trip[0];
                } else {
                    return trip;
                }
            });
        }
        count += trip[0];
        if (count > capacity) {
            return false;
        }
        tripsSoFar.push(trip);
    }
    
    return true;
};
```

**More Efficient Solution:**
```
/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    let timestamps = [];
    
    trips.forEach(trip => {
        timestamps.push([trip[1], +trip[0]]);
        timestamps.push([trip[2], -trip[0]]);
    });
    
    timestamps.sort((a, b) => a[0] - b[0]);
    
    let count = 0;
    for (let i = 0; i < timestamps.length; i++) {
        count += timestamps[i][1];
        // we have to be careful here: we also have to process dropoffs
        if (count > capacity && timestamps[i + 1] && timestamps[i][0] !== timestamps[i + 1][0]) {
            return false;
        }
    }
    
    return true;
};
```

**Bucket Sort**
```
/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    let buckets = {};
    
    trips.forEach(trip => {
        buckets[trip[1]] = buckets[trip[1]] || 0;
        buckets[trip[1]] += trip[0];
        buckets[trip[2]] = buckets[trip[2]] || 0;
        buckets[trip[2]] -= trip[0];        
    });
    let count = 0;
    for (const [key, value] of Object.entries(buckets)) {
        count += value;
        if (count > capacity) {
            return false;
        }
    }
    
    return true;
};
```
**Wrote another solution after 16 months away from this**
```
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
            Build an array of 1001
            For each trip: [num_pass, from, to]
            - add num_pass at arr[from]
            - subtract num_pass at arr[to]
            Then go through the array, adding values -
            If it ever goes above capacity, return false
            return True
        """
        arr = [0] * 1001
        
        for num_pass, from_, to_ in trips:
            arr[from_] += num_pass
            arr[to_] -= num_pass
        
        total = 0
        for i in arr:
            total += i
            if total > capacity:
                return False
        
        return True
```
