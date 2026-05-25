### 1010. Pairs of Songs With Total Durations Divisible by 60
Medium

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0. 

**Example 1:**
```
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
```

**Example 2:**
```
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
``` 

**Constraints:**
```
1 <= time.length <= 6 * 104
1 <= time[i] <= 500
```

**Tags**
- Revisit
- Array
- Hash Table
- Counting

### Solution:
```
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
            Get a map of remainder (length % 60) to count
            For each remainder:
                If the remainder is zero, only pairs of zero remainders
                can be used. That formula is n! / k!(n - k)! or in this case it is 
                (n * (n - 1)) / 2
                This is the same for 30.
                For others, it is count[n] * count[60 - n]
        """
        total = 0
        remainders = {}
        for t in time:
            remainder = t % 60
            if remainder in remainders:
                remainders[remainder] += 1
            else:
                remainders[remainder] = 1
        
        if 0 in remainders:
            total += remainders[0] * (remainders[0] - 1) / 2
            del remainders[0]
        if 30 in remainders:
            total += remainders[30] * (remainders[30] - 1) / 2
            del remainders[30]
        
        for i in range(1, 30):
            if i in remainders and 60 - i in remainders:
                total += remainders[i] * remainders[60 - i]
        
        return int(total)
        
        
```
