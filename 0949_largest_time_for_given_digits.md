### 949. Largest Time for Given Digits
Medium

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
 
**Example 1:**
```
Input: [1,2,3,4]
Output: "23:41"
```

**Example 2:**

```
Input: [5,5,5,5]
Output: ""
``` 

**Note:**
```
A.length == 4
0 <= A[i] <= 9
```


**Tags**
- Array
- String
- Backtracking
- Enumeration

### Solution:
You can either generate all the permutations then check if it is valid or do this:

```
/**
 * @param {number[]} A
 * @return {string}
 */
var largestTimeFromDigits = function(A) {
    let findFourthDigit = function () {
        for (let i = 2; i >= 0; i--) {
            let index = A.indexOf(i);
            if (index < 0) {
                continue;
            }
            let num = findThirdDigit([i], [...A.slice(0, index), ...A.slice(index + 1)]);
            if (num) {
                return num;
            }
        }
        return '';
        
    };
        
    let findThirdDigit = function(result, A) {
        let first = [0, 1, 2, 3];
        let second = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
        let iterator;
        if (result[0] === 2) {
            iterator = first;
        } else {
            iterator = second;
        }
        
        for (let i = iterator.length - 1; i >= 0; i--) {
            let digit = iterator[i];
            let index = A.indexOf(digit);
            if (index < 0) {
                continue;
            }
            
            let num = findNextDigits([...result, digit], [...A.slice(0, index), ...A.slice(index + 1)]);
            if (num) {
                return num;
            }
        }
        
        return '';
    };
    
    let findNextDigits = function(result, A) {
        let pair1 = parseInt(`${A[0]}${A[1]}`, 10);
        let pair2 = parseInt(`${A[1]}${A[0]}`, 10);
        if (pair1 >= 60 && pair2 >= 60) {
            return '';
        }
        if (pair1 >= 60) {
            if (pair2 < 10) {
                pair2 = '0' + pair2;
            }
            return result.join('') + ':' + pair2;
        }
        
        if (pair2 >= 60) {
            if (pair1 < 10) {
                pair1 = '0' + pair1;
            }            
            return result.join('') + ':' + pair1;
        }
        let max = Math.max(pair1, pair2);
        if (max < 10) {
            max = '0' + max;
        }
        return result.join('') + ':' + max;
    };
    
    return findFourthDigit(A);
};
```
