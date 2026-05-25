### 859. Buddy Strings
Easy

Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

**Example 1:**
```
Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
```

**Example 2:**
```
Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
```

**Example 3:**
```
Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
```

**Example 4:**
```
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
```

**Example 5:**
```
Input: A = "", B = "aa"
Output: false
``` 

**Constraints:**
```
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.
```

**Tags**
- Hash Table
- String

### Solution:
```
/**
 * @param {string} A
 * @param {string} B
 * @return {boolean}
 */
var buddyStrings = function(A, B) {
    if (A.length !== B.length || A.length < 2 || B.length < 2) {
        return false;
    }
    
    // go through the strings and if a character is different,
    // add the index into the array
    // if the number of indexes === 0 then return true (if there are chars that occur more than 2x)
    // otherwise return false (aaab, aaab) and (abcde, abcde)
    // if the number of indexes !== 2 then return false
    // swap the characters in A and check if it is B and return the result
    const indexes = [];
    const charArr = {};
    
    for (let i = 0; i < A.length; i++) {
        if (A[i] !== B[i]) {
            indexes.push(i);
        }
        charArr[A[i]] = charArr[A[i]] || 0;
        charArr[A[i]] += 1;
    }
    
    if (indexes.length === 0) {
        for (const [key, val] of Object.entries(charArr)) {
            if (val >= 2) {
                return true;
            }
        }
        return false;
    }
    
    if (indexes.length > 2) {
        return false;
    }
    
    A = A.split('');
    let temp = A[indexes[0]];
    A[indexes[0]] = A[indexes[1]];
    A[indexes[1]] = temp;
    A = A.join('');
    
    return A === B;
};
```
