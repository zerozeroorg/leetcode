### 1328. Break a Palindrome
Medium

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'. 

**Example 1:**
```
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
```

**Example 2:**
```
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
```

**Example 3:**
```
Input: palindrome = "aa"
Output: "ab"
```

**Example 4:**
```
Input: palindrome = "aba"
Output: "abb"
``` 

**Constraints:**
```
1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
```

**Tags**
- String
- Greedy

### Solution
```
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
            NOTE: THERE IS A LINEAR TIME SOLUTION THAT IS VERY CLEVER. THE HIGH LEVEL IS BELOW THIS CODE!!!
            
            If it is a single char, return ""
            
            For even length strings, we can safely change any one char
            and not cause it to be another palindrome
            
            But be careful of odd length strings...
            
            Brute force: for each char in palindrome:
            - change it to every lowecase English letter
            - get the word for it
            - check if that is the minimum
        """
        length = len(palindrome)
        palindrome = list(palindrome)
        min_result = None
        chars = [chr(i) for i in range(97, 123)]
        
        if length == 1:
            return ""
        
        is_odd = length % 2 == 1
        
        for i in range(length):
            if is_odd and i == length // 2:
                continue

            original = palindrome[i]
            
            for char in chars:
                if char == original:
                    continue
                
                palindrome[i] = char
                new_string = "".join(palindrome)
                if min_result is None:
                    min_result = new_string
                else:
                    min_result = min_result if min_result < new_string else new_string
            
            palindrome[i] = original
        
        return min_result
        
```

### Linear Solution Algorithm
1. If the length of the string is 11, return an empty string since we cannot create a non-palindromic string in this case.
1. Iterate over the string from left to the middle of the string: if the character is not aa, change it to aa and return the string.
1. If we traversed over the whole left part of the string and still haven't got a non-palindromic string, it means the string has only aa's. Hence, change the last character to bb and return the obtained string.
