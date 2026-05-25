### 121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Solutions:
There are a few ways to do this:
- Brute force: try every price pair O(n^2) time
- Create an array of max prices to the right of a price and get the max difference between the price, and max price to the right of it. O(n) time, O(n) space
- Maintain a minStock price and see if subtracting the minStock from the current price is the max. O(n) time, O(1) space.

The idea with the optimized solution is that the best profit is done from buying at at the lowest price and selling at the highest price.

If you have something like this:
[2, 1, 6]

You select the min price between [2, 1] because later you will sell at whatever max is set in the future.

If you have something like this:

[2, 6, 1, 4]

You have to keep track of the max profit because the max price may already occurred before a new min price is set.

### Brute Force:
```
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxVal = 0;
    
    for (let i = 0; i < prices.length; i++) {
        for (let j = i; j < prices.length; j++) {
            let value = prices[j] - prices[i];
            if (value > maxVal) {
                maxVal = value;
            }
        }
    }
    
    return maxVal;
};
```

### Less time, more space:
```
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxs = [];
    let max = Number.MIN_SAFE_INTEGER;
    let maxProfit = 0;
    
    for (let i = prices.length - 1; i >= 0; i--) {
        let num = prices[i];
        max = Math.max(max, num);
        maxs.unshift(max);
    }
    
    for (let i = 0; i < prices.length; i++) {
        let profit = maxs[i] - prices[i];
        maxProfit = Math.max(maxProfit, profit);
    }
    
    return maxProfit;
};
```

### Most efficient solution:
```
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0;
    let minStock = prices[0];
    
    if (prices.length < 2) {
        return maxProfit;
    }
    
    for (let i = 0; i < prices.length; i++) {
        let price = prices[i];
        maxProfit = Math.max(maxProfit, price - minStock);
        minStock = Math.min(minStock, price);
    }
    
    return maxProfit;
};
```
**Tags**
- Array
- Dynamic Programming
