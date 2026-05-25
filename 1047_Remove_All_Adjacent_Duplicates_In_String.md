### 1047. Remove All Adjacent Duplicates In String
Easy

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.


**Example 1:**
```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

**Example 2:**
```
Input: s = "azxxzy"
Output: "ay"
``` 

**Constraints:**
```
1 <= s.length <= 10^5
s consists of lowercase English letters.
```

**Tags**
- String
- Stack

### Solution
Python:
```
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
                continue
            stack.append(char)
        
        return "".join(stack)
```

Java:
```
class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (stack.size() == 0) {
                stack.push(c);
                continue;
            }
            
            dedup(stack, c);
        }
        
        StringBuilder sb = new StringBuilder();
        for (Character c: stack) {
            sb.append(c);
        }
        
        return sb.toString();
    }
    
    private void dedup(Stack<Character> stack, char c) {
        char top = stack.peek();
        if (top != c) {
            stack.push(c);
            return;
        }
        stack.pop();
        return;
    }
}
```
