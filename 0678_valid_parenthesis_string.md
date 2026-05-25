### 678. Valid Parenthesis String
Medium

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

**Example 1:**
```
Input: "()"
Output: True
```
**Example 2:**
```
Input: "(*)"
Output: True
```

**Example 3:**
```
Input: "(*))"
Output: True
```
**Note:**
The string size will be in the range [1, 100].


**Tags**
- String
- Dynamic Programming
- Stack
- Greedy

### Solution:
- The intuition: let's ignore the stars for a second.
- Then the problem is no different from checking for valid parentheses. 
- The invalid cases are:
- If you encounter a ")" and there are not enough "("
- If after you iterate the string, there are some "(" left over.
- Then the idea is to keep track of indexes for "(" as one stack, and "*" in another stack.
- If you run out of "(", then check if you can use a star
- If after iterating the string, check to make sure that any left over "(" can be matched by a "*"
- To do that, pop an index from the "(" stack and check if that index is less than popping an index from the "*" stack.
```
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        
        for index, char in enumerate(list(s)):
            if char == '(':
                stack.append(index)
            elif char == '*':
                stars.append(index)
            elif len(stack) > 0:
                stack.pop()
            elif len(stars) > 0:
                stars.pop()
            else:
                return False
        
        while len(stack) > 0:
            position = stack.pop()
            
            if len(stars) == 0:
                return False
            
            star_position = stars.pop()
            
            if star_position < position:
                return False
            
        return True
```
