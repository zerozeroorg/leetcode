### 714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). 

**Example 1:**
```
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```

**Example 2:**
```
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
``` 

**Constraints:**
```
1 < prices.length <= 5 * 104
0 < prices[i], fee < 5 * 104
```

**Tags**
- Array
- Dynamic Programming
- Greedy

### Solution:
```
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
            Use top down dp with memoization
            On any given day, you can either:
            - buy the stock at that day. 
            -- If you buy, then sell any day after that
            - sell the stock at that day
            -- If you sell, then buy any day after that
            - Pick the max of those two
            - return that max.
            - use memoization to cache the results
        """
        N = len(prices)
        buy_stock_dp = [None] * N
        sell_stock_dp = [None] * N
        
        def buy_stock(day):
            if day >= N:
                return 0 # don't buy
            if buy_stock_dp[day] is not None:
                return buy_stock_dp[day]
            
            buy_now = sell_stock(day + 1) - prices[day]
            buy_later = buy_stock(day + 1)
            buy_stock_dp[day] = max(buy_now, buy_later)
            return buy_stock_dp[day]
        
        def sell_stock(day):
            if day >= N:
                return -float('inf') # you can't sell
            if sell_stock_dp[day] is not None:
                return sell_stock_dp[day]
            
            sell_now = buy_stock(day + 1) + prices[day] - fee
            sell_later = sell_stock(day + 1)
            sell_stock_dp[day] = max(sell_now, sell_later)
            return sell_stock_dp[day]
        
        return buy_stock(0)
```
