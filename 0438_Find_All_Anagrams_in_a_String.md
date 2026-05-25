### 438. Find All Anagrams in a String
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

**Example 1:**
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**
```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
``` 

**Tags**
- Revisit
- Hash Table
- String
- Sliding Window

**Constraints:**
```
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
```

### Solution
- Easiest way is to use sliding window and a dictionary
- Have one dictionary that represents the freq of chars in p
- Have another dictionary to keep track of the processed chars in s so far
- Compare the two dictionaries: if they are the same, add the start index (current pointer - length of p - 1)
- If the window is larger than the length of p, remove the first character in the window
```
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        total_chars = len(p)
        length = len(s)
        freq = {}
        current = {}
        result = []
        
        for char in p:
            if freq.get(char) is None:
                freq[char] = 0
            freq[char] += 1
            
        
        for i in range(length):
            char = s[i]
            if current.get(char) is None:
                current[char] = 0
            
            current[char] += 1
            
            if i >= total_chars:
                current[s[i - total_chars]] -= 1
                if current[s[i - total_chars]] == 0:
                    del current[s[i - total_chars]]
            
            if current == freq:
                result.append(i - (total_chars - 1))
        
        return result
            
```
