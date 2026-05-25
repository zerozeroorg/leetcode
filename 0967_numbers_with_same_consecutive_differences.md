### 967. Numbers With Same Consecutive Differences
Medium

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order. 

**Example 1:**
```
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
```

**Example 2:**
```
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

**Example 3:**
```
Input: n = 2, k = 0
Output: [11,22,33,44,55,66,77,88,99]
```

**Example 4:**
```
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

**Example 5:**
```
Input: n = 2, k = 2
Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
``` 

**Constraints:**
```
2 <= n <= 9
0 <= k <= 9
```

**Tags**
- Backtracking
- Breadth-First Search

### Solution:
- Create a list of lists: [[0],[1],[2]...[9]]
- Create a result array
- For each item in the list:
- take the last digit and add/subtract k. Check if the new digit is within 0-9.
- if it is, add that digit
- check if the length is equal to N
- if it is, check if the new number is legit (no leading zeroes) you can do something like parseInt(num, 10).toString().length === N
```
/**
 * @param {number} N
 * @param {number} K
 * @return {number[]}
 */
var numsSameConsecDiff = function(N, K) {
    let queue = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]];
    let result = [];
    while (queue.length) {
        let numList = queue.shift();
        if (numList.length === N) {
            let num = parseInt(numList.join(''), 10);
            if (num.toString().length === N) {
                result.push(num);
                continue;
            }
        }
        if (numList.length > N) {
            continue;
        }
        
        let nextDigits = [numList[0] + K];
        if (K !== 0) {
            nextDigits.push(numList[0] - K);
        }
        
        nextDigits.forEach(nextDigit => {
            if (0 <= nextDigit && nextDigit < 10) {
                queue.push([nextDigit, ...numList]);    
            }
        });
        
    }
    
    return result;
};
```
