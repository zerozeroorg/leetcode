### 1641. Count Sorted Vowel Strings
Medium

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
 

**Example 1:**
```
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
```

**Example 2:**
```
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
```

**Example 3:**
```
Input: n = 33
Output: 66045
``` 

**Constraints:**
```
1 <= n <= 50 
```

**Tags**
- Math
- Dynamic Programming
- Combinatorics

### Solution:
```
class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
            This is a backtracking problem I think.
            First, get all the possible vowels for the first
            position.
            Then for second position, the possible vowels
            will be any vowel that is lexiographically sorted
            after the first position.
            Continue after there are no positions.
        """
        self.total = 0
        
        def helper(remaining, vowels):
            length = len(vowels)
            if remaining == 0:
                self.total += 1
                return
            
            for index in range(length):
                newVowels = vowels[index:length]
                helper(remaining - 1, newVowels)
        
        helper(n, ['a', 'e', 'i', 'o', 'u'])
        
        return self.total
```
