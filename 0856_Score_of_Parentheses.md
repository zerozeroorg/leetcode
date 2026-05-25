### 856. Score of Parentheses
Medium

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

**Example 1:**
```
Input: s = "()"
Output: 1
```

**Example 2:**
```
Input: s = "(())"
Output: 2
```

**Example 3:**
```
Input: s = "()()"
Output: 2
``` 

**Constraints:**
```
2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
```

**Tags**
- String
- Stack

### Solution
- This is a O(n) space, O(n) time solution
- There is a O(1) space, O(n) time solution, provided by LeetCode. This page will not cover this.
```
/**
 * @param {string} s
 * @return {number}
 */
var scoreOfParentheses = function(s) {
    let stack = [];
    
    for (let i = 0; i < s.length; i++) {
        let char = s.charAt(i);
        if (char !== ')') {
            stack.push(char);
        } else {
            let temp = 0;
            while (stack.length && stack[stack.length - 1] !== '(') {
                temp += stack.pop();
            }
            if (stack.length && stack[stack.length - 1] === '(') {
                stack.pop();
            }
            if (temp === 0) {
                stack.push(1);
            } else {
                stack.push(temp * 2);
            }
        }
    }
    
    return stack.reduce((acc, curr) => acc + curr, 0);
};
```
