### 213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

**Example 1:**
```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

**Example 2:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 3:**
```
Input: nums = [0]
Output: 0
``` 

**Constraints:**
```
1 <= nums.length <= 100
0 <= nums[i] <= 1000
```

**Tags**
- Array
- Dynamic Programming

### Solution:
- This was tough. I needed a hint.
- The hint was: since it was in a ring, your choices are rob H[0]...H[n - 1] or H[1]...H[n]. Then, it boils down to House Robber problem!
```
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length === 1) {
        return nums[0];
    }
    const helper = (nums, location, dp) => {
        if (nums[location] === undefined) {
            return 0;
        }
        if (dp[location] !== undefined) {
            return dp[location];
        }
        
        let current = nums[location] + helper(nums, location + 2, dp);
        let next = helper(nums, location + 1, dp);
        dp[location] = Math.max(current, next);
        return dp[location];
    };
    
    let firstRange = helper(nums.slice(0, nums.length - 1), 0, {});
    let secondRange = helper(nums.slice(1, nums.length), 0, {});
    return Math.max(firstRange, secondRange);
};
```
