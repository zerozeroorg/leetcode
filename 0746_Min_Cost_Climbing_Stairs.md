### 746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor. 

**Example 1:**
```
Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
```

**Example 2:**
```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
``` 

**Constraints:**
```
2 <= cost.length <= 1000
0 <= cost[i] <= 999
```

**Tags**
- Array
- Dynamic Programming

### Solution
```
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length];
        int firstStep = minCostHelper(cost, 0, dp);
        int secondStep = minCostHelper(cost, 1, dp);
        
        return Math.min(firstStep, secondStep);
    }
    
    private int minCostHelper(int[] cost, int currPtr, int[] dp) {
        if (currPtr >= cost.length) {
            return 0;
        }
        
        if (dp[currPtr] != 0) {
            return dp[currPtr];
        }
        
        int currentCost = cost[currPtr];
        int bestCost = Math.min(
            minCostHelper(cost, currPtr + 1, dp), minCostHelper(cost, currPtr + 2, dp)
        );
        dp[currPtr] = currentCost + bestCost;
        return dp[currPtr];
    }
}
```
