### 123. Best Time to Buy and Sell Stock III
Hard

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). 

**Example 1:**
```
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

**Example 2:**
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

**Example 4:**
```
Input: prices = [1]
Output: 0
``` 

**Constraints:**
```
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
```

**Tags**
- Revisit
- Array
- Dynamic Programming

### Solution
There is a faster solution in JS below this one but it is not very intuitive.
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        buy_lookup = [[None, None, None] for _ in range(length) ]
        sell_lookup = [[None, None, None] for _ in range(length) ]
        
        def buy(index, transactions):
            if index >= length - 1:
                return 0
            
            if transactions == 0:
                return 0
            
            if buy_lookup[index][transactions] is not None:
                return buy_lookup[index][transactions]
                
            
            buy_now = -prices[index] + sell(index + 1, transactions)
            buy_later = buy(index + 1, transactions)
            max_profit = max(buy_now, buy_later)
            buy_lookup[index][transactions] = max_profit
            return max_profit
        
        
        def sell(index, transactions):
            if index >= length:
                return 0
            
            if transactions == 0:
                return 0
            
            if sell_lookup[index][transactions] is not None:
                return sell_lookup[index][transactions]
            
            sell_now = prices[index] + buy(index + 1, transactions - 1)
            sell_later = sell(index + 1, transactions)
            max_profit = max(sell_now, sell_later)
            sell_lookup[index][transactions] = max_profit
            return max_profit
        
        return buy(0, 2)
        
        
```

Linear time JS solution
```
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let firstBuy = Number.MIN_SAFE_INTEGER;
    let firstSell = 0;
    let secondBuy = Number.MIN_SAFE_INTEGER;
    let secondSell = 0;
    
    for (let i = 0; i < prices.length; i++) {
        price = prices[i];
        firstBuy = Math.max(firstBuy, -price);
        firstSell = Math.max(firstSell, firstBuy + price);
        secondBuy = Math.max(secondBuy, firstSell - price);
        secondSell = Math.max(secondSell, secondBuy + price);
    }
    return secondSell;
};
```
