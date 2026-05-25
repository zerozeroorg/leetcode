### 1235. Maximum Profit in Job Scheduling
Hard

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
 

**Example 1:**
```
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
```

**Example 2:**
```
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
```

**Example 3:**
```
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
``` 

Constraints:
```
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
```

**Tags**
- Array
- Binary Search
- Dynamic Programming
- Sorting

### Solution
```
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        The idea is to use dynamic programming: what is the max profit
        if I take job[i] and any job before job[i], or just take the best previous job?

        This is a bottom up approach to dynamic programming where each step of dp is
        take the current job + the best of the previous, non-conflicting job, 
        or you don't take the current job and just take the best of the previous job:

        i = current job
        j = index of previous, nonconflicting job

        dp[i] = max(dp[i - 1], dp[j] + profit[i])

        where -
        dp[i - j]: best of the previous job if I don't take current job
        dp[j] + profit[i]: best of previous non-conflicting job, plus current job profit

        Note here j and i could be the same depending on if there is a conflict or not.

        Once you have calculated this dp table, the last index of this table will tell
        you what is the max value overall. Return that value.

        So now the problem is: how do find the previous non conflicting job before my 
        current one? You would need to use binary search because the contraints of 
        the problem prevents doing a linear search over each job resulting in (n^2) time.

        You can sort the jobs by end time ascending, and use binary search to find 
        the previous job's end time that does not conflict with the current job's 
        start time. With python's bisect_right module, you can find the right most
        index of the job where the end time is less than the current job's start time

        First, create a job tuple: (start_time, end_time, profit) and sort by
        end time

        Then create dp array

        Iterate through the sorted jobs tuple and calculate dp with bisect_right

        Return max         
        """
        jobs = []
        length = len(profit)
        for i in range(length):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])

        dp = [0] * length

        for i in range(length):
            current = jobs[i]
            current_start_time = current[0]
            current_profit = current[2]
            insert_index = bisect.bisect_right(jobs, current_start_time, key=lambda x: x[1]) - 1
            if i == 0:
                dp[i] = current_profit
            else:
                previous_profit = 0 if insert_index < 0 else dp[insert_index]
                dp[i] = max(dp[i - 1], previous_profit + current_profit)
        
        print(jobs)
        print(dp)
        return dp[length - 1]

        
```
