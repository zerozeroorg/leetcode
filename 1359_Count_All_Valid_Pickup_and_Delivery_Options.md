### 1359. Count All Valid Pickup and Delivery Options
Hard

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7. 

**Example 1:**
```
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
```

**Example 2:**
```
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
```

**Example 3:**
```
Input: n = 3
Output: 90
``` 

**Constraints:**
```
1 <= n <= 500
```

**Tags**
- Revisit
- Math
- Dynamic Programming
- Combinatorics

### Solution
```
/**
 * @param {number} n
 * @return {number}
 */
var countOrders = function(n) {
    /*
        The idea is to use bottom up dynamic programming,
        using smaller cases to find the answer to the larger ones.
        
        for N = 1, the only possibly is:
        
        P1 D1
        
        for N = 2, we use the N = 1 case and figure
        out where to put P2:
        
        P2 X X
        X P2 X
        X X P2
        
        Then D2 can be:
        
        P2 D2 X X
        P2 X D2 X
        P2 X X D2
        
        X P2 D2 X
        X P2 X D2
        
        X X P2 D2
        
        If you try these in other cases, you will notice
        that the number of cases is the sum of 1 to # of gaps in
        the previous case, times # of possibilities in the previous case:
        
        For N = 2:
        1 + 2 + 3 * f(N - 1)
    */
    const modulo = Math.pow(10, 9) + 7;
    let count = 1;
    let previousCases = 1;
    
    for (let i = 2; i <= n; i++) {
        let gaps = (i - 1) * 2 + 1;
        let currentCases = (gaps + 1) * (gaps / 2) * previousCases;
        count = currentCases;
        count = count % modulo;
        previousCases = count;
    }
    
    
    return count % modulo;
};
```
