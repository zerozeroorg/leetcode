### 290. Word Pattern
Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

**Example 1:**
```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

**Example 2:**
```
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```

**Example 3:**
```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

**Example 4:**
```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

**Notes:**
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

## Solution:
- I messed up for "abba", "dog dog dog dog" using a single hashmap. "a" -> "dog" and "b" -> "dog". You have to make sure that the words also mapped to the same letter.
So the solution here is to use two hashmaps:

```
/**
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPattern = function(pattern, str) {
    let words = str.split(' ');
    let letters = pattern.split('');
    let letterMap = {};
    let wordMap = {};
    
    if (words.length !== letters.length) {
        return false;
    }
    
    for (let i = 0; i < letters.length; i++) {
        let letter = letters[i];
        let word = words[i];
        
        if (letterMap[letter] === undefined) {
            letterMap[letter] = word;
        }
        if (wordMap[word] === undefined) {
            wordMap[word] = letter;
        }
        
        if (letterMap[letter] === word && wordMap[word] === letter) {
            continue;
        } else {
            return false;
        }
        
    }
    
    return true;
};
```
**Tags**
- Hash Table
- String
