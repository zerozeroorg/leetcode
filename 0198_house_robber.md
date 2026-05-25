### 198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

**Constraints:**
```
0 <= nums.length <= 100
0 <= nums[i] <= 400
```

**Tags**
- Array
- Dynamic Programming

### Solution:

Use dynamic programming. You can choose to take the first item, then get the maximum of the items after the adjacent item or ignore the first item and get the max
of the rest of the items.

Below, is an optimization of a bottom up approach:

```
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length === 0) {
        return 0;
    }
    
    let sums = [0, nums[0]];
    let index = 1;
    while (index < nums.length) {
        sums[index + 1] = Math.max(
            sums[index - 1] + nums[index],
            sums[index]
        );
        
        index += 1;
    }
    
    return sums[sums.length - 1];
};
```

Here is a solution after not remembering how i would solve it:
```

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let dp = [];
    let helper = (nums, dp, index) => {
        if (index >= nums.length) {
            return 0;
        }
        if (index === nums.length - 1) {
            dp[index] = nums[index];
            return dp[index];
        }
        
        if (dp[index] !== undefined) {
            return dp[index];
        }
        
        let currentHouse = nums[index] + helper(nums, dp, index + 2);
        let nextHouse = nums[index + 1] + helper(nums, dp, index + 3);
        
        dp[index] = Math.max(currentHouse, nextHouse);
        return dp[index];
    };
    
    return helper(nums, dp, 0);
};
```
