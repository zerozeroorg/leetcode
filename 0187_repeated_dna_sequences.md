### 187. Repeated DNA Sequences
Medium

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

**Example 1:**
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
```

**Example 2:**
```
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
``` 

**Constraints:**
```
0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.
```

**Tags**
- Hash Table
- String
- Bit Manipulation
- Sliding Window
- Rolling Hash
- Hash Function

### Solution:
```
/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    // create a map of substring -> count
    // for each letter in s:
    // generate a 10 letter long sequence with s
    // count how many times it occurs in the string s
    // update the map
    // UGH - I compared the 10 letter long sequence to every other sequence.
    // A better way is to use a sliding window and check if it is in the map.     
    let map = {};
    
    for (let i = 0; i <= s.length - 10; i++) {
        let substring = s.substr(i, 10);
        map[substring] = map[substring] || 0;
        map[substring] += 1;
    }
    
    let result = [];
    for ([key, val] of Object.entries(map)) {
        if (val > 1) {
            result.push(key);
        }
    }
    return result;
};
```
