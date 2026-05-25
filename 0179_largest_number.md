### 179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

**Example 1:**
```
Input: [10,2]
Output: "210"
```

**Example 2:**
```
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
```

**Tags**
- Array
- String
- Greedy
- Sorting

### Solution:
- I messed up so many times.
- I thought sorting by digits would work. Turns out that [3, 34] and [121, 12] will present problems with this approach.
- So, I finally came to the conclusion that I have to sort by combining and comparing. So for [x, y], I have to check xy versus yx.
- Another tricky thing is the input [0, 0]. You have to return 0 so in JS I have to remove any leading zeroes and return 0 if all nums are removed.

```
/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    // first, sort, digit by digit where the highest leading digit wins
    // if a number does not have a digit, use zero
    // if both numbers have zero, the one with less digits should win otherwise go to next digit
    
    nums.sort((a, b) => {
        let abNum = parseInt(`${a}${b}`, 10);
        let baNum = parseInt(`${b}${a}`, 10);
        
        if (abNum > baNum) {
            return -1;
        }
        
        if (baNum > abNum) {
            return 1;
        }
        
        return 0;
    });
    
    if (nums.length > 0) {
        while(nums[0] === 0) {
            nums.shift();
        }    
    }
    
    if (nums.length) {
        return nums.join('');
    }
    
    return '0';
};
```
