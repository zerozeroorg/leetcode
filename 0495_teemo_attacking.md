### 495. Teemo Attacking
Easy

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

**Example 1:**
```
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.
``` 

**Example 2:**
```
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.
``` 

**Note:**
```
You may assume the length of given time series array won't exceed 10000.
You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.
```

**Tags**
- Array
- Simulation

### Solution:
- The intuition: when there are time intervals involved, think about interval problems we solved before. I did not solve this well without this intuition.
- Draw out the time interval and figure out the poison length.
- Here, we keep track of the start time and end time of the poison status.
- If the hero gets infected before the end time of the poison status, then we update the end time of the poison status.
- If the hero gets infected after, we get the difference of the start and end time of the previous poison status and add it to total. Then we start a new
poison status interval.

```
/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    let total = 0;
    let startTime = 0;
    let endTime = 0;
    
    timeSeries.forEach(time => {
        if (endTime < time) {
            total += endTime - startTime;
            startTime = time;
            endTime = time + duration;
        } else {
            endTime = time + duration;
        }
    });
    
    total += endTime - startTime;
    
    return total;
};
```

Another way of thinking about this is the following diagram:
```
[1,2,3,4,5]
5

1->         5
   2->       6
      3->     7
         4->   8
            5-> 9
```

- If I am infected at 1, it will last til 5.
- But if I am infected at 2, then it will last til 6.
- To get the total duration when infected in 1 and 2, just subtract the end points, (5 from 6) to get the new additive to the duration.
- The time interval may start from zero, so need to account for that.
```
/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    let total = 0;
    let poisonEndTime;
    
    
    timeSeries.forEach(time => {
        if (poisonEndTime < time || poisonEndTime === undefined) {
            total += duration;
            poisonEndTime = time + duration - 1;
        } else {
            total += (time + duration - 1) - poisonEndTime;
            poisonEndTime = time + duration - 1;
        }   
    });
    
    
    return total;
};
```
