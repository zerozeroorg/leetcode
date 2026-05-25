### 14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

**Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
``` 

**Constraints:**
```
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
```

**Tags**
- Array
- String
- Trie

### Solution:
- My idea is to take the first character of each word and compare them. If they match, put them in the result array and increment pointer.
- If they do not match, return result array.
- Another way: take the common prefix of first and second word. Then, take that prefix and find the common prefix among the rest of the words.
```
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let start = 0;
    let result = [];
    
    if (strs.length === 0) {
        return '';
    }
    
    while (true) {
        let chars = [];
        strs.forEach(str => chars.push(str[start]));
        let allMatches = chars.every(char => char === chars[0] && char !== undefined);
        if (allMatches) {
            result.push(chars[0]);
            start += 1;
        } else {
            return result.join('');
        }        
    }

};
```
