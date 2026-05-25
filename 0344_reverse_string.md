### 344. Reverse String
Easy

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters. 

**Example 1:**
```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**
```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

**Tags**
- Two Pointers
- String

### Solution:
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        startPtr = 0
        endPtr = len(s) - 1
        
        while startPtr < endPtr:
            temp = s[startPtr]
            s[startPtr] = s[endPtr]
            s[endPtr] = temp
            startPtr += 1
            endPtr -= 1
```
