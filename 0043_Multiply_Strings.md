### 43. Multiply Strings
Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


**Example 1:**
```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**
```
Input: num1 = "123", num2 = "456"
Output: "56088"
``` 

**Constraints:**
```
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
```

**Tags**
- Revisit
- Math
- String
- Simulation

### Solution
- This was annoying problem
- Need to consider carrys
- Need to move places
- Need to iterate backwards!
```
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        num1_size = len(num1)
        num2_size = len(num2)
        totals = []
        carry = None
        
        ptr1 = num1_size - 1
        
        while ptr1 >= 0:
            a = num1[ptr1]
            total = 0
            ptr2 = num2_size - 1
            
            while ptr2 >= 0:
                b = num2[ptr2]
                result = int(a) * int(b)
                if carry:
                    result += carry
                    carry = None

                if result > 9:
                    carry = result // 10
                    result = result % 10
                
                total += result * (10 ** (num2_size - ptr2 - 1))
                ptr2 -= 1
            
            if carry:
                total += carry * (10 ** num2_size)
                carry = None                
            
            totals.append(total * (10 ** (num1_size - ptr1 - 1)))
            ptr1 -= 1
        
        return str(functools.reduce(lambda a, b: a + b, totals))
        
```
