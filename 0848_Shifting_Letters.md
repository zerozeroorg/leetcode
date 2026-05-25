### 848. Shifting Letters
Medium

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied. 

**Example 1:**
```
Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
```

**Example 2:**
```
Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"
``` 

**Constraints:**
```
1 <= s.length <= 105
s consists of lowercase English letters.
shifts.length == s.length
0 <= shifts[i] <= 109
```


**Tags**
- Array
- String
- Prefix Sum

### Solution
```
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
            Calculate the suffix sum
            Then for each num in the suffix num, get the number of shifts
            for each char in s
            Return the final string
        """
        suffix = collections.deque([])
        total = 0
        result = []    
        
        for i in range(len(shifts) - 1, -1, -1):
            total += shifts[i]
            suffix.appendleft(total)
    
        for i in range(len(suffix)):
            rotations = suffix[i] % 26
            char = s[i]
            moves = rotations + ord(char)

            if moves > ord('z'):
                result.append(chr(ord('a') + (moves - ord('z')) - 1))
            else:
                result.append(chr(moves))
        
        return "".join(result)
            
            
        
        
```
