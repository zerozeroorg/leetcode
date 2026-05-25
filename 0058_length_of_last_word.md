### 58. Length of Last Word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

**Example:**
```
Input: "Hello World"
Output: 5
```

**Tags**
- String

### Solution:
```
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    if (s.length === 0) {
        return 0;
    }
    
    let ptr = s.length - 1;
    let count = 0;
    let spaceChar = null;
    
    while (ptr >= 0) {
        let char = s[ptr];
        if (char === ' ' && count === 0) {
            ptr--;
            continue;
        }
        if (char === ' ' && count > 0) {
            break;
        }
        count += 1;
        ptr--;    
    }
    
    return count;

    /*
    s = s.trim()
    s = s.split(" ")
    return s.pop().length
    */
};


```
