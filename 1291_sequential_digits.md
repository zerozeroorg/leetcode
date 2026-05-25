### 1291. Sequential Digits
Medium

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits. 

**Example 1:**
```
Input: low = 100, high = 300
Output: [123,234]
```

**Example 2:**
```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

**Tags**
- Enumeration

### Solution:
- Gotcha: if low = 10, and high = 10000000,  if you are not careful about what is a valid sequential number, you will generate a number like: 891011 which is wrong!

```
/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    let result = new Set();
    let digitLengths = high.toString().length - low.toString().length;
    
    let genSequentialNum = (startNum, length) => {
        let numArr = [];
        for (let i = 0; i < length; i++) {
            if (1 <= startNum && startNum <= 9) {
                numArr.push(startNum);
                startNum += 1;                
            } else {
                return;
            }
        }
        
        let num = parseInt(numArr.join(''), 10);
        if (low <= num && num <= high) {
            result.add(num);
        }
    }
    
    let currLength = low.toString().length;
    for (let i = 0; i <= digitLengths; i++) {
        for (let j = 1; j <= 9; j++) {
            genSequentialNum(j, currLength);    
        }
        currLength += 1;
    }
    
    return [...result];
};
```

### Much simpler solution:
- Just generate all valid sequential digits. They aren't that many.
```
/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    let nums = '123456789';
    let result = [];
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = i; j < nums.length; j++) {
            let num = parseInt(nums.substr(i, j - i + 1), 10);
            if (low <= num && num <= high) {
                result.push(num);
            }
        }
    }
    
    result = result.sort((a, b) => a - b);
    return result;
};
```
