### 402. Remove K Digits
Medium

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
 

**Example 1:**
```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

**Example 2:**
```
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

**Example 3:**
```
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
``` 

**Constraints:**
```
1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.
```

**Tags**
- Revisit
- String
- Stack
- Greedy
- Monotonic Stack

### Solution
- Solution is written in the comments. Not intuitive. You have to really work it out.
```
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
            To get the smallest number possible, we have to remove
            the first largest digit from the left. For example:
            
            143
            
            If we can only remove one digit, the possibilities are:
            
            43
            13
            43
            
            so basically, at the first num[j] > num[j + 1], we remove nums[j].
            we try to do this k times. If there is still k left, that means we
            have a list of numbers that is monotonically increasing:
            
            1234
            
            In that case, you remove the last k digits.
            
            So we use a monotonic stack. We insert into the stack until the top > current.
            In that case, we pop the top and check again until top <= current.
        """
        length = len(num)
        if k >= length:
            return "0"
        
        stack = []
        
        for n in num:
            
            while stack and int(stack[-1]) > int(n) and k > 0:
                stack.pop()
                k -= 1
            
            if stack or n != "0":
                stack.append(n)
        
        
        if k > 0:
            stack = stack[0:-k]
        
        if not stack:
            return "0"
        
        return "".join(stack)
            
        
```
