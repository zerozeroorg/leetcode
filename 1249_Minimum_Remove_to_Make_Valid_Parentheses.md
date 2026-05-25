### 1249. Minimum Remove to Make Valid Parentheses
Medium

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

**Example 1:**
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

**Example 2:**
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3:**
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
``` 

**Constraints:**
```
1 <= s.length <= 10^5
s[i] is either'(' , ')', or lowercase English letter.
```
**Tags**
- String
- Stack

### Solution
```
/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    /*
        store index of opening parens in a stack
        
        process each char:
        - if it is opening parens, store index in stack and add to list
        - if closing parens:
            - check if there is a opening parens that is < closing index
            - if not, then do not include closing
            - if there is, add to list and remove opening parens from stack
        - otherwise, add to list
    
        if there are still opening parens, then remove them from string
    */
    let open = [];
    s = s.split('');
    result = [];
    
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (char === '(') {
            result.push(char);
            open.push(result.length - 1);
            continue;
        } else if (char === ')') {
            if (open.length) {
                open.pop();
                result.push(char);     
            }
        } else {
            result.push(char);
        }
    }
    
    if (open.length) {
        for (const index of open) {
            result[index] = '';
        }
    }
    
    return result.join('');
};
```
