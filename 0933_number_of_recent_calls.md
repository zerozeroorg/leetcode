### 933. Number of Recent Calls
Easy

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

**Example 1:**
```
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
``` 

**Constraints:**
```
1 <= t <= 104
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
```

**Tags**
- Design
- Queue
- Data Stream

### Solution:
- Kinda over complicated the problem. My idea is to store all the calls, then do binary search to find the range of calls that fall into [t - 3000, t]
- A simpler solution is to append the recent call, then starting from the beginning of the call lists, remove invalid calls.

**My Solution:**
```

var RecentCounter = function() {
    this.requests = [];
    this.binarySearch = function(item, limit='low') {
        let low = 0;
        let high = this.requests.length - 1;
        let requests = limit === 'low' ? high : low;

        while (low <= high) {
            let mid = low + Math.floor((high - low) / 2);
            let request = this.requests[mid];
            
            if (limit === 'low') {
                if (request < item) {
                    low = mid + 1;
                } else {
                    requests = Math.min(requests, mid);
                    high = mid - 1;
                }
            }
            
            if (limit === 'high') {
                if (request > item) {
                    high = mid - 1;
                } else {
                    requests = Math.max(requests, mid);
                    low = mid + 1;
                }
            }
        }

        return requests;            
    }
};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    this.requests.push(t);
    let low = this.binarySearch(t - 3000, 'low');
    let high = this.binarySearch(t, 'high');
    return high - low + 1;
};

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
```

**Better Solution**
```

var RecentCounter = function() {
    this.requests = [];
};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    this.requests.push(t);
    let ptr = 0;
    while (ptr < this.requests.length) {
        if (this.requests[ptr] >= t - 3000) {
            break;
        }
        
        this.requests.shift();
    }
    
    return this.requests.length;
};

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
```
