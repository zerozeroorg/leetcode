### 1239. Maximum Length of a Concatenated String with Unique Characters
Medium

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s. 

**Example 1:**
```
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
```

**Example 2:**
```
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
```

**Example 3:**
```
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
``` 

**Constraints:**
```
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
```

**Tags**
- Array
- String
- Backtracking
- Bit Manipulation

### Solution
```
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
            Let's first generate the combinations naively
            
            STOLEN IDEA: as you are generating the subsequences, have a set of unique
            chars. If as you add new words it is no longer unique, then return early
            to prune tree branches that are not viable.
        """
        max_length = 0
        
        def helper(arr, result, unique):
            nonlocal max_length
            
            if result:
                if len(result) != len(unique):
                    return

            if not arr:
                if result:
                    if len(result) == len(unique):
                        max_length = max(max_length, len(result))                
                return
            
            # get words without the first word
            helper(arr[1:], result, unique)
            
            # get words with the first word
            helper(arr[1:], result + arr[0], unique | set(list(arr[0])))
    
    
        helper(arr, "", set())
        
        return max_length

        
             
```
