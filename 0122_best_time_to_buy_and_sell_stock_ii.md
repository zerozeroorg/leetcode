### 122. Best Time to Buy and Sell Stock II
Medium

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**
```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

**Example 2:**
```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
``` 

**Constraints:**
```
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
```

**Tags**
- Array
- Dynamic Programming
- Greedy

### Solution:
- We want to buy from a valley and sell at a peak
- Start with the first price
- If the next price is less than the current price, then don't buy the current price. Buy the next price.
- If the next next price is less than the next price, then buy at current and sell at next price.
```
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let startIndex = 0
    let startPrice = prices[startIndex]
    let profit = 0
    let nextIndex = startIndex + 1
    
    while(nextIndex < prices.length) {
        let nextPrice = prices[nextIndex]
        if (startPrice > nextPrice) {
            // switch start
            startPrice = nextPrice
            startIndex = nextIndex
            nextIndex += 1
            continue
        } else if ((nextIndex + 1) < prices.length) {
            if (prices[nextIndex + 1] < prices[nextIndex]) {
                profit += (nextPrice - startPrice);
                startIndex = nextIndex;
                startPrice = nextPrice;
                nextIndex += 1;                
            } else {
                nextIndex += 1;
            }
        } else {
            profit += (nextPrice - startPrice);
            startIndex = nextIndex;
            startPrice = nextPrice;
            nextIndex += 1;
        }
    }
    
    return profit
};
```

- Simple solution: since we can do as many transactions as we want, we get the price current and next and see if we can make a profit.
```
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let sum = 0;
    for (let i = 0; i < prices.length - 1; i++) {
        let price1 = prices[i];
        let price2 = prices[i + 1];
        sum += Math.max(0, price2 - price1);
    }
    return sum;
};
```
