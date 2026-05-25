### 205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. 

**Example 1:**
```
Input: s = "egg", t = "add"
Output: true
```

**Example 2:**
```
Input: s = "foo", t = "bar"
Output: false
```

**Example 3:**
```
Input: s = "paper", t = "title"
Output: true
``` 

**Constraints:**
```
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
```

**Tags**
- Hash Table
- String

### Solution
```
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
            - Create a dictionary of s chars -> t chars
            - NEW: Create a dictionary of t chars -> s chars because 
            this will fail: s: "jjbb" t: "tttt" multiple chars map to "t"
            
            - Go through the each character of s and t one at a time
            - If dict[sChar] is None, then map dict[sChar] = tChar
            - Otherwise, if dict[sChar] != tChar return false
            - Do the same for t char -> s char

            - At the end return true
        """
        sLookup = {}
        tLookup = {}
        ptr = 0
        length = len(s)
        
        while ptr < length:
            sChar = s[ptr]
            tChar = t[ptr]
            if sChar not in sLookup:
                sLookup[sChar] = tChar
            elif sLookup[sChar] != tChar:
                return False
            
            if tChar not in tLookup:
                tLookup[tChar] = sChar
            elif tLookup[tChar] != sChar:
                return False
                
            ptr += 1
        
        return True
        
```
