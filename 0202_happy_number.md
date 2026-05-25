### 202. Happy Number
Easy

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

**Example:** 
```
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

**Tags**
- Hash Table
- Math
- Two Pointers

### Solution:
- Compute the sum of squares of its digits
- Check if it is 1
- If it is 1, return true
- If it is not, check if we visited
- If visited, then there is a cycle, so return false
- If not visited, add it to visited set
- Update n
```
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let visited = new Set()
    while (n !== 1) {
        if (visited.has(n)) {
            // cycle detected: break
            return false;
        }
        visited.add(n);
        n = n.toString().split('').reduce((sum, current) => {
            return sum + (current * current);    
        }, 0);
    }
    
    // the loop found 1: it is a happy number
    return true;
    
    // % 10 gives you the first digit on the right
    // Math.floor(/ 10) gives you the number after removing the first digit 
};
```
