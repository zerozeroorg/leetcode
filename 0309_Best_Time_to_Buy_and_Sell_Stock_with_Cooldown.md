### 309. Best Time to Buy and Sell Stock with Cooldown
Medium

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). 

**Example 1:**
```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

**Example 2:**
```
Input: prices = [1]
Output: 0
``` 

**Constraints:**
```
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
```

**Tags**
- Revisit
- Array
- Dynamic Programming

### Solution
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        buy_lookup = {}
        sell_lookup = {}
        
        def buy(index):
            if index >= length:
                return 0
            
            if buy_lookup.get(index) is not None:
                return buy_lookup.get(index)
            
            buy_now = -prices[index] + sell(index + 1)
            buy_later = buy(index + 1)
            best_profit = max(buy_now, buy_later)
            buy_lookup[index] = best_profit
            return buy_lookup[index]
        
        def sell(index):
            if index >= length:
                return 0
            
            if sell_lookup.get(index) is not None:
                return sell_lookup.get(index)
            
            sell_now = prices[index] + buy(index + 2)
            sell_later = sell(index + 1)
            best_profit = max(sell_now, sell_later)
            sell_lookup[index] = best_profit
            return sell_lookup[index]
        
        
        return buy(0)
        
```
