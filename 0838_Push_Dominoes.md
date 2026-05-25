### 838. Push Dominoes
Medium

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state. 

**Example 1:**
```
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
```

**Example 2:**
```
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
``` 

**Constraints:**
```
n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
```

**Tags**
- Two Pointers
- String
- Dynamic Programming

### Solution
```
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
            Create a list of chars
            Set a pointer at the first char
            While ptr < len(chars):
            - If the char is a ".", continue
            - If the char is a "L", then:
                - find the nearest char position on the left side of it
                - if none exists, collapse all chars from 0...ptr to L.
                - otherwise, collapse between j...ptr.
                - increment ptr by 1
            - If the char is a "R", then:
                - find the nearest char position on the right side of it
                - if none exists, collapse all chars from ptr...length to R.
                - set ptr to length.
                - otherwise, collapse between ptr...j.
                - increment ptr to j + 1.           
        """
        chars = list(dominoes)
        length = len(chars)
        ptr = 0
        
        def nearest_char_position(start, delta):
            while 0 <= start < length:
                if chars[start] != ".":
                    return start
                start += delta
            return -1
        
        def set_char(start, end, char):
            while 0<= start <= end < length:
                chars[start] = char
                start += 1
        
        def domino_effect(start, end, start_char, end_char):
            if start == end:
                return
            if start + 1 == end:
                return
            if start_char == end_char:
                set_char(start, end, start_char)
                return
            
            total = end - start + 1
            middle = start + (total // 2)
            has_middle = False
            if total % 2 != 0:
                has_middle = True
            
            while start < end:
                if has_middle and start == middle:
                    start += 1
                    continue
                if start < middle:    
                    chars[start] = start_char
                else:
                    chars[start] = end_char
                start += 1
            
        
        while ptr < length:
            char = chars[ptr]
            if char == ".":
                ptr += 1
                continue
            if char == "L":
                next_char_position = nearest_char_position(ptr - 1, -1)
                if next_char_position == -1:
                    set_char(0, ptr, "L")
                    ptr += 1
                else:
                    # handle domino effect
                    domino_effect(next_char_position, ptr, chars[next_char_position], chars[ptr])
                    ptr += 1    
            else:
                next_char_position = nearest_char_position(ptr + 1, 1)
                if next_char_position == -1:
                    set_char(ptr, length - 1, "R")     
                    ptr = length
                else:
                    # handle domino_effect
                    domino_effect(ptr, next_char_position, chars[ptr], chars[next_char_position])
                    ptr = next_char_position
        
        
        return "".join(chars)
        
```
