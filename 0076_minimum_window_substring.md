### 76. Minimum Window Substring
Hard

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
 
**Example 1:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
``` 

**Constraints:**
```
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
``` 

**Follow up: Could you find an algorithm that runs in O(m + n) time?**

**Tags**
- Hash Table
- String
- Sliding Window

**Note:**
- If there is no such window in `S` that covers all characters in `T`, return the empty string `""`.
- If there is such window, you are guaranteed that there will always be only one unique minimum window in `S`.

### Solution
```
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let slowPtr = 0;
    let fastPtr = 0;
    let result = [];
    // store counts by letter here
    let map = {};
    // store the total char count here
    let count = 0;
    // store lettersNeeded here
    let lettersNeeded = {};
    const length = t.length;
    
    if (!t.length || !s.length) {
        return '';
    }
    
    for (let i = 0; i < t.length; i++) {
        lettersNeeded[t[i]] = lettersNeeded[t[i]] || 0;
        lettersNeeded[t[i]] += 1;
    }
    
    while (fastPtr < s.length) {
        let fastPtrChar = s[fastPtr];
        // not a char we care about: skip it
        if (t.indexOf(fastPtrChar) < 0) {
            fastPtr += 1;
            continue;
        }
        
        map[fastPtrChar] = map[fastPtrChar] || 0;
        // first time? increment count
        if (map[fastPtrChar] < lettersNeeded[fastPtrChar]) {
            count += 1;
        }
        map[fastPtrChar] += 1;
        
        // did not find all chars yet: continue fastPtr
        if (count !== length) {
            fastPtr += 1;
            continue;
        }
        
        // slowly decrement slowPtr while checking for min
        while (slowPtr <= fastPtr) {
            let newLength = fastPtr - slowPtr + 1;
            if (!result.length) {
                result = [slowPtr, fastPtr];
            }
            // find the min interval
            let currLength = result[1] - result[0] + 1;
            if (newLength < currLength) {
                result = [slowPtr, fastPtr];
            }
            let slowPtrChar = s[slowPtr];
            // if slowPtrChar is not what we care about: move it and skip it
            if (map[slowPtrChar] === undefined) {
                slowPtr += 1;
                continue;
            }
            // decrement count and move slowPtr
            map[slowPtrChar] -= 1;
            slowPtr += 1;
            
            // decrement total count if the char goes down to zero
            if (map[slowPtrChar] < lettersNeeded[slowPtrChar]) {
                count -= 1;
            }
            // this means we need to keep searching with fastPtr
            if (count < length) {
                fastPtr += 1;
                break;
            }
        }
    }
    
    if (!result.length) {
        return '';
    }
    
    return s.substring(result[0], result[1] + 1);
};
```

### Python Solution
- Very hard problem, but rewarding
- It was hard because there are cases where s = "a" and t = "aa" have to be checked for duplicates
- Also hard to keep track of the pointers and the character counts as you slide and contract. DO NOT DOUBLE COUNT CHARACTERS.
- Good practice with sliding window
```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            Have a sliding window with a = 0, b = 0
            Get a char lookup for sliding window
            Get current char in b and add to char lookup
            Then check if char lookup has all chars in t
            If it does, then get the min window size
            
            Then move a down and subtract the char a previously
            was in char lookup
            If char lookup still has all chars in t, get min window size
            Else move b
            
            Return min window size
        """
        window = float('inf')
        result = ""
        lookup = {}
        a = 0
        b = 0
        size = len(s)
        t_lookup = collections.Counter(t)
        
        def hasAllChars():
            for char in t_lookup:
                if lookup.get(char, 0) < t_lookup[char]:
                    return False
            return True
        
        while b < size:
            bChar = s[b]
            lookup[bChar] = lookup.get(bChar, 0) + 1
            if hasAllChars():
                if window > (b - a + 1):
                    window = b - a + 1
                    result = s[a:b+1]                
                while a <= b:
                    aChar = s[a]
                    a += 1
                    lookup[aChar] -= 1
                    if hasAllChars():
                        if window > (b - a + 1):
                            window = b - a + 1
                            result = s[a:b+1]                        
                        continue
                    else:
                        break
            b += 1
        
        
        return result
        
```
Version 3:
```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            Have a sliding window with a = 0, b = 0
            Get a char lookup for sliding window
            Get current char in b and add to char lookup
            Then check if char lookup has all chars in t
            If it does, then get the min window size
            
            Then move a down and subtract the char a previously
            was in char lookup
            If char lookup still has all chars in t, get min window size
            Else move b
            
            Return min window size
            
            TRICK: to check if the window has all chars in t:
            - Have a required variable which equals to the number of unique chars in t
            - Have a formed variable which equals to current number of unique chars
            you have founded in t so far
            - When formed == required, then you have all the chars in t
            - When you contract the window, always check if lookup[leftChar] < t_lookup[leftChar]
            and if so, then decrement formed.
        """
        window = float('inf')
        result = ""
        lookup = {}
        a = 0
        b = 0
        size = len(s)
        t_lookup = collections.Counter(t)
        required = len(t_lookup)
        formed = 0
        
        while b < size:
            bChar = s[b]
            lookup[bChar] = lookup.get(bChar, 0) + 1
            if bChar in t_lookup and lookup[bChar] == t_lookup[bChar]:
                formed += 1
            if formed == required:
                if window > (b - a + 1):
                    window = b - a + 1
                    result = s[a:b+1]                
                while a <= b:
                    aChar = s[a]
                    a += 1
                    lookup[aChar] -= 1
                    if aChar in t_lookup and lookup[aChar] < t_lookup[aChar]:
                        formed -= 1                    
                    if formed == required:
                        if window > (b - a + 1):
                            window = b - a + 1
                            result = s[a:b+1]                        
                        continue
                    else:
                        break
            b += 1
        
        
        return result
        
```
