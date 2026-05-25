### 20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([)]"
Output: false
```

**Example 5:**
```
Input: s = "{[]}"
Output: true
``` 

**Constraints:**
```
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```

**Tags**
- String
- Stack

### Solution:
Argh don't forget that a string can just contain opening chars! So you must check at the very end if the stack is full.

Use a stack and a map
```
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(s.length === 0) {
        return true;
    }
    let map = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    };
    
    let stack = [];
    s = s.split('');
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (char === '(' || char === '[' || char === '{') {
            stack.push(char);
        } else {
            let popped = stack.pop();
            if (map[popped] !== char) {
                return false;
            }
        }
    }
    if (stack.length > 0) {
        return false;
    }
    return true;
};
```
