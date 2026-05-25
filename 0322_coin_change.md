### 322. Coin Change
Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin. 

**Example 1:**
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**
```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**
```
Input: coins = [1], amount = 0
Output: 0
```

**Example 4:**
```
Input: coins = [1], amount = 1
Output: 1
```

**Example 5:**
```
Input: coins = [1], amount = 2
Output: 2
``` 

**Constraints:**
```
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
```

**Tags**
- Array
- Dynamic Programming
- Breadth-First Search

### Solution:
```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            DP problem
            
            check if the amount is 0: if yes return 0
            sort the coins from largest to smallest for greedy-ish
            two choices:
            - get min changes if you take the coin
            - get min changes if you don't take the coin
            take the min of those two choices
            return that min
            
            use a dp table to store aleady computed answers 
        """
        dp = [[None for i in range(len(coins))] for j in range(amount + 1)] 
        coins.sort(reverse=True)
        
        def min_change(index, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if dp[amount][index] is not None:
                return dp[amount][index]
            
            # change if we use the coin
            choice_one = min_change(index, amount - coins[index]) + 1
            
            # change is we dont use the coin
            choice_two = min_change(index + 1, amount) if index + 1 < len(coins) else float('inf')
            
            dp[amount][index] = min(choice_one, choice_two)
            return dp[amount][index]
            
        result = min_change(0, amount)
        return result if result != float('inf') else -1
        
```
