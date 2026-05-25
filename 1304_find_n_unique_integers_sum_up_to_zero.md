### 1304. Find N Unique Integers Sum up to Zero
Easy

Given an integer n, return any array containing n unique integers such that they add up to 0.

**Example 1:**
```
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
```

**Example 2:**
```
Input: n = 3
Output: [-1,0,1]
```

**Example 3:**
```
Input: n = 1
Output: [0]
``` 

**Constraints:**
```
1 <= n <= 1000
```

**Tags**
- Array
- Math

### Solution:
**My thinking:**

We will be given a number, n, and we need to generate n unique numbers that add up to 0. Looking at the examples, I think Example 2 gives an idea of how to solve the problem:

[-1, 0, 1]

If n is an even number, we can divide it and create a set of negative and positive numbers that negate each other.

If n is an odd number, do the same as above but add 0 to it after you are done.

**Straightforward solution:**

- Divide n by 2 and round down.
- For i in (1...floor(n/2)): create a positive and negative version of i
- Add it to the answer array
- After the loop, we check if n was odd or not. If it is odd, we add 0. 

```
/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    var result = [];
    
    if (n % 2 === 1) {
        result.push(0);
    }
    
    let length = Math.floor(n / 2);
    for (let i = 1; i <= length; i++) {
        result.push(i);
        result.push(i * -1);
    }
    
    return result;
};
```
