### 49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
``` 

**Constraints:**
```
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
```

**Tags**
- Array
- Hash Table
- String
- Sorting

### Solution:
- create a map
- for each word:
- create a key from the word with the letters sorted
- put it in the map with wordSortedByLetters => [word...]

Another way to solve it:
- Create a char count for each word. You can represent it as a tuple in python (1,2,3,..0)
- Then compare each char count to each other
- This is slightly faster than the sorting one above
```
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let myMap = new Map();
    for (let i = 0; i < strs.length; i++) {
        let word = strs[i];
        let sortedWord = word.split('').sort().join('');
        if (!myMap.has(sortedWord)) {
            myMap.set(sortedWord, []);
        }
        let entry = myMap.get(sortedWord);
        entry.push(word);
        myMap.set(sortedWord, entry);
    }
    
    let ans = []
    
    for (const value of myMap.values()) {
        ans.push(value);
    }

    return ans;
    
//     // For each element, O(n), we sort each str O(n log n)
//     // we use O(n) space
//     let newStrs = strs.map((str) => {
//         return [str, str.split('').sort().join('')];
//     });
    
//     // O(n) space, O(n) time
//     let newMap = {};
//     newStrs.forEach((strElement) => {
//         if (!newMap[strElement[1]]) {
//             newMap[strElement[1]] = [];
//         }
        
//         newMap[strElement[1]].push(strElement[0]);
//     });
    
//     // O(n) iteration
//     return Object.values(newMap);
};
```
Python version
```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Need a map of ordered chars -> anagrams
            
            Then for each str in strs:
            - create a ordered version of str
            - add into the map
            
            Return map.values()
        """
        lookup = collections.defaultdict(list)
        
        for word in strs:
            ordered = "".join(sorted(list(word)))
            lookup[ordered].append(word)
        
        return lookup.values()
        
```
