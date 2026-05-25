### 316. Remove Duplicate Letters
Medium

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/ 

**Example 1:**
```
Input: s = "bcabc"
Output: "abc"
```

**Example 2:**
```
Input: s = "cbacdcbc"
Output: "acdb"
``` 

**Constraints:**
```
1 <= s.length <= 104
s consists of lowercase English letters.
```

**Tags**
- String
- Stack
- Greedy
- Monotonic Stack

### Solution:
- The idea is to greedily process each character and take the lexicographically smallest character and push it into a result array.
- If you find character that is smallest than the last character in the result, and that last character in the result array occurs later, pop it off
- Do this popping until you can't satisfy the if.
- Have a visited/seen array to mark that the character is already seen and no need to process it.
```
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
    const last = [];
    const result = [];
    const visited = [];
    const startIndex = 'a'.charCodeAt(0);
    
    s = s.split('');
    
    // get the last index occurrence of each unique character
    s.forEach((char, index) => {
        let charCode = char.charCodeAt(0);
        last[charCode - startIndex] = index; 
    });
    
    // for each s, index:
    // if the character is already visited, skip
    // otherwise:
    // check if there are any elements in result that are bigger than s and 
    // lastIndex > index
    // if so, then pop elements and set visited to false until this if fails
    // if not, push the s character and set visited to true
    
    s.forEach((char, index) => {
        let charCode = char.charCodeAt(0);
        if (visited[charCode - startIndex] === true) {
            return;
        }
        
        while(true) {
            if (!result.length) {
                break;
            }
            let lastChar = result[result.length - 1];
            let lastCharCode = lastChar.charCodeAt(0);
            
            if (lastCharCode > charCode && last[lastCharCode - startIndex] > index) {
                result.pop();
                visited[lastCharCode - startIndex] = false;
            } else {
                break;
            }
        }
        visited[charCode - startIndex] = true;
        result.push(char);
    });
    
    return result.join('');
};
```
