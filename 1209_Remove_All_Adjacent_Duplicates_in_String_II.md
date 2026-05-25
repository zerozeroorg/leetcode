## 1209. Remove All Adjacent Duplicates in String II
Medium

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique. 

**Example 1:**
```
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
```

**Example 2:**
```
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
```

**Example 3:**
```
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
``` 

**Constraints:**
```
1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
```

## Solution:
```
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
            Use a stack to store processed characters.
            Add first char into the stack
            If the next char is equal to the top of stack, increment
            count. 
            If count == k, remove the k characters from the stack
            We keep processing until we can't do this anymore -
            We do this by figuring out if the stack length == s length
        """
        stack = []
        new_s = ""
        count = 0
        
        while True:
            for char in s:
                if len(stack) == 0:
                    count = 1
                    stack.append(char)
                elif stack[-1] != char:
                    count = 1
                    stack.append(char)
                else:
                    count += 1
                    stack.append(char)
                    if count == k:
                        count = 0
                        stack = stack[: len(stack) - k]

            new_s = "".join(stack)            
            if new_s == s:
                break
            s = new_s
            stack = []
            
        
        return new_s
        
        
        
```
**Tags**
- String
- Stack
