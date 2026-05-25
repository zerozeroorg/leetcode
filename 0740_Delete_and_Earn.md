### 740. Delete and Earn
Medium

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times. 

**Example 1:**
```
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
```

**Example 2:**
```
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
``` 

**Constraints:**
```
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
```

**Tags**
- Revisit
- Array
- Hash Table
- Dynamic Programming

### Solution
- Took several tries but the idea is that you have two choices: choose the current and skip any num + 1 and num -1, or choose the next one.
- If there are several instances of a number like `3,3,3.3` and you take `3`, then take them all. It won't affect your next step.
- The tricky part is that in the array `[1,3]` you can take `1` and not have to skip `3` so you have to check if you have to skip your next index.
- So set up counter and a sorted set of `nums` and then use the house robber idea to figure out if you should take the current step or next step.
```
/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = function(nums) {
    let counter = {};
    nums.forEach(num => counter[num] = (counter[num] || 0) + 1);
    let ordered = [...new Set(nums)].sort((a, b) => a - b);
    let dp = {};
    let best = 0;
    
    function choose(index) {
        if (index >= ordered.length) {
            return 0;
        }
        
        if (dp[index] !== undefined) {
            return dp[index];
        }
        
        // choose current index
        let chooseCurrent = ordered[index] * counter[ordered[index]];
        
        // can I choose next?
        if (index + 1 < ordered.length && ordered[index + 1] > ordered[index] + 1) {
            chooseCurrent += choose(index + 1);
            dp[index] = chooseCurrent;
        } else {
            chooseCurrent += choose(index + 2);

            // choose next
            let chooseNext = choose(index + 1);

            dp[index] = Math.max(chooseCurrent, chooseNext);            
        }
        
        
        best = Math.max(best, dp[index]);
        return dp[index];
    }
    
    
    choose(0);
    return best;
};
```
