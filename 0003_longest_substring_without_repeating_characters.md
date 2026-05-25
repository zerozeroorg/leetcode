### 3. Longest Substring Without Repeating Characters
Medium

Medium

Given a string s, find the length of the longest substring without repeating characters.

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:**
```
Input: s = ""
Output: 0
``` 

**Constraints:**
```
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
```

**Harder test cases:**
```
"aabaab!bb"
"abba"
```
**Tags**
- Hash Table
- String
- Sliding Window

### Solution:
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            Super hard problem but I solved it!
            I had to reset the dictionary.
            You have to use sliding window to solve it basically.
            
            Create a dictionary of char -> index
            Set longest = 0
            Set current = 0
            Set a ptr to the first char
            
            Starting with the first char:
            - check if it is in the dictionary
            - if not, add it to the dictionary
            - if it is, remove it from dictionary
            Update longest = max(longest, current)
            Increment pointer
        """
        lookup = {}
        longest = 0
        current = 0
        ptr = 0
        lastReset = 0
        
        def reset(lookup, s, start, end):
            while start <= end:
                del lookup[s[start]]
                start += 1
            return lookup
        
        while ptr < len(s):
            char = s[ptr]
            if char in lookup:
                position = lookup[char]
                lookup = reset(lookup, s, lastReset, position)
                lastReset = position + 1
                lookup[char] = ptr
                current = ptr - position
            else:
                lookup[char] = ptr
                current += 1

            longest = max(longest, current)
            ptr += 1
        
        return longest
        
```

### Better Solution:
- Use a sliding window approach. Have pointers, i, j and slide j. If j is not unique, then move i. Max would be max(max, j - i + 1).
```
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let ptr1 = 0;
    let ptr2 = 1;
    let lookupSet = new Set();
    let maxCount = 1;

    if (s.length < 2) {
        return s.length;
    }

    lookupSet.add(s.charAt(ptr1));

    while (ptr2 < s.length) {
        if (!lookupSet.has(s.charAt(ptr2))) {
            lookupSet.add(s.charAt(ptr2));
            maxCount = Math.max(maxCount, ptr2 - ptr1 + 1);
            ptr2 += 1;
        } else {
            lookupSet.delete(s.charAt(ptr1));
            ptr1 += 1;
        }
    }

    return maxCount;
};
```
