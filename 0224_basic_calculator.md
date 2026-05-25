### 224. Basic Calculator
Hard

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

**Example 1:**
```
Input: "1 + 1"
Output: 2
```

**Example 2:**
```
Input: " 2-1 + 2 "
Output: 3
```

**Example 3:**
```
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
```

**Tags**
- Math
- String
- Stack
- Recursion

### Solution:
- Use a stack
- Since there are parentheses, you have to evaluate those first before you evaluate the main expression.
- **Holy cow** - there is a case that you need to account for. Numbers can be more than 2 digits so when you are parsing them character by character, you have
to combine characters of a number. DAMN.
```
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let stack = [];
    let compute = (arr) => {
        let operation = '+';
        let ans = 0;
        let num = 0;
        for (let i = 0; i < arr.length; i++) {
            let char = arr[i];
            if (char === '(' || char === ')') {
                continue;
            }
            if (char === '+' || char === '-') {
                ans = operation === '+' ? ans + num : ans - num;
                num = 0;
                operation = char;
            } else {
                char = parseInt(char);
                num = num * 10 + char;
            }
        }
        ans = operation === '+' ? ans + num : ans - num;
        return ans;
    }
    
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (char === ' ') {
            continue;
        }
        if (char === ')') {
            let open = stack.lastIndexOf('(');
            let expr = stack.splice(open);
            stack.push(compute(expr));
            continue;
        }
        
        stack.push(char);
    }
    return compute(stack);
};
```

The Python version
```
class Solution:
    def calculate(self, s: str) -> int:
        """
            remove the blanks
            first compute the parentheses
            then compute the rest of the expression
            Need to account for multi-digit numbers and negative numbers
        """
        s = s.replace(" ", "")
        expression = collections.deque(list(s))

        
        def compute(first, operand, second):
            num1 = int("".join(first))
            num2 = int("".join(second))
            if operand == "+":
                return num1 + num2
            else:
                return num1 - num2
        
        def helper():
            first = []
            operand = None
            second = []            
            # get the first operand
            while expression:
                char = expression.popleft()
                if char.isdigit():
                    first.append(char)
                elif char == "(":
                    first.append(str(helper()))
                elif char == ")":
                    return "".join(first)
                elif not first:
                    first.append(char)
                else:
                    operand = char
                    break

            while expression:
                char = expression.popleft()
                if char.isdigit():
                    second.append(char)
                elif char == "(":
                    second = [str(helper())]
                elif char == ")":
                    break    
                else:
                    result = compute(first, operand, second)
                    first = [str(result)]
                    second = []
                    operand = char

            if not second:
                return int("".join(first))

            return compute(first, operand, second)
        
        return helper()
        
        
```
