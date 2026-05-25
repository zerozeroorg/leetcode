### 983. Minimum Cost For Tickets
Medium

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

**Example 1:**
```
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
```

**Example 2:**
```
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
``` 

**Note:**
```
1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
```

**Tags**
- Array
- Dynamic Programming

### Solution:
- Build a 365 calendar array where 0 day has no cost.
- If you are not traveling on a certain day, then that day's cost will be the cost of the previous day because we are accumlating cost.
- If you are traveling on a certain day, then you have 3 options:
- Cost of a one day ticket: previous day + cost of 1 day ticket
- Cost of a 7 day ticket: last 7 days cost + cost of 7 day ticket
- Cost of a 30 day ticket: last 30 days cost + cost of 30 day ticket
- Take the min of those 3 and that will be the best cost for that day

```
/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    let calendar = [0];
    
    for (let i = 1; i <= 365; i++) {
        if (days.indexOf(i) < 0) {
            calendar[i] = calendar[i - 1];
            continue;
        }
        let todayCost = calendar[i - 1] + costs[0];
        let sevenCost = calendar[i - 7] !== undefined ? calendar[i - 7] + costs[1] : costs[1];
        let thirtyCost = calendar[i - 30] !== undefined ? calendar[i - 30] + costs[2] : costs[2];
        
        calendar[i] = Math.min(todayCost, sevenCost, thirtyCost);
    }
    
    return calendar[365];
};
```
