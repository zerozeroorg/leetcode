### 227. Basic Calculator II
Medium

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
 

**Example 1:**
```
Input: s = "3+2*2"
Output: 7
```

**Example 2:**
```
Input: s = " 3/2 "
Output: 1
```

**Example 3:**
```
Input: s = " 3+5 / 2 "
Output: 5
``` 

**Constraints:**
```
1 <= s.length <= 3 * 10^5
`s` consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
`s` represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, (2^31) - 1].
The answer is guaranteed to fit in a 32-bit integer.
```

**Tags**
- Math
- String
- Stack

### Solution
```
class Solution:
    def calculate(self, s: str) -> int:
        expression = collections.deque(s.replace(" ", ""))
        number = ''
        result = collections.deque([])
        
        while expression:
            char = expression.popleft()
            if char.isdigit():
                number += char
            else:
                result.append(int(number))
                number = ''
                result.append(char)
        
        if number:
            result.append(int(number))

        while result:
            char = result.popleft()
            if char == '/' or char == "*":
                num1 = expression.pop()
                num2 = result.popleft()
                expression.append(num1 * num2 if char == '*' else num1 // num2)
            else:
                expression.append(char)
        
        while expression:
            char = expression.popleft()
            if char == '+' or char == '-':
                num1 = result.pop()
                num2 = expression.popleft()
                result.append(num1 + num2 if char == '+'  else num1 - num2)
            else:
                result.append(char)
        
        
        return result[0]
        
        
```
