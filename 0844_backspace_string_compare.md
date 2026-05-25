### 844. Backspace String Compare
Easy

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**
```
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
```

**Example 2:**
```
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
```

**Example 3:**
```
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
```

**Example 4:**
```
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
```

**Note:**
```
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
```
**Follow up:**
```
Can you solve it in O(N) time and O(1) space?
```

**Tags**
- Two Pointers
- String
- Stack
- Simulation

### Solution:
- Use two stacks: one for S and the other for T
- For S and T, push their letters in a stack. If you see a #, then remove the top of the stack character
- Then compare the stacks
- Another solution with no stacks: Iterate over S and T backwards from the last of the character.
- If you encounter a #, skip the next character.
```
/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function(S, T) {
    let sArr = [];
    let tArr = [];
    
    for (let i = 0; i < S.length; i++) {
        if (S[i] === '#') {
            sArr.pop();
        } else {
            sArr.push(S[i]);
        }
    }
    
    for (let i = 0; i < T.length; i++) {
        if (T[i] === '#') {
            tArr.pop();
        } else {
            tArr.push(T[i]);
        }
    }
    
    return sArr.join('') === tArr.join('');
};
```
