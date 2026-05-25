### 680. Valid Palindrome II
Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

**Example 1:**
```
Input: "aba"
Output: True
```

**Example 2:**
```
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```

**Note:**
```
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
```

**Tags**
- Two Pointers
- String
- Greedy

### Solution:
- Just do what you have to do. No special trick.
- Have a isPalindrome helper function
- Then go through the characters in s. If it is not a palindrome, check if [i+1, j] is a palindrome or [i, j-1] is a palindrome with the helper function

```
/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    let ptr1 = 0;
    let ptr2 = s.length - 1;
    
    let isPalindrome = (s) => {
        let ptr1 = 0;
        let ptr2 = s.length - 1;
        
        while (ptr1 < ptr2) {
            if (s[ptr1] === s[ptr2]) {
                ptr1 += 1;
                ptr2 -= 1;
                continue;
            }
            
            return false;
        }
        
        return true;
    };
    
    while (ptr1 < ptr2) {
        if (s[ptr1] === s[ptr2]) {
            ptr1 += 1;
            ptr2 -= 1;
            continue;
        }
        
        let result = isPalindrome(s.substring(ptr1, ptr2));
        if (result) {
            return true;
        }
        result = isPalindrome(s.substring(ptr1 + 1, ptr2 + 1));
        if (result) {
            return true;
        }
        return false;
    }
    return true;
};
```
