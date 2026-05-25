### 139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.


**Example 1:**
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3:**
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

**Tags**
- Array
- Hash Table
- String
- Dynamic Programming
- Trie
- Memoization

### Solution:
* Things I messed up:
  * splice takes an index, and number of elements to delete. It then returns the deleted elements. Do not chain it with split or join! It will use the 
deleted chars.
  * join('') returns the joined array elements. You need to store that somewhere! I did not assign a variable to it.
  * My initial code failed for this test case: "ccbb", ["bc", "cb"]. That is because I remove "cb" from the middle of the string. That is not a valid
word break.
* My solution ran too long. The answer is to use dynamic programming (memoization) to reduce already computed answers.
* In my DP solution, I had to be careful when to assign dp[s] to false.
```
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let dp = {};
    
    const helper = (s, wordDict) => {
        if (dp[s] !== undefined) {
            return dp[s];
        }
        for (let i = 0; i < wordDict.length; i++) {
            let word = wordDict[i];
            let index = s.indexOf(word);
            if (index !== 0) {
                continue;
            }
            let newWord = s.split('');
            newWord.splice(index, word.length);
            newWord = newWord.join('');
            
            let result = !newWord.length || helper(newWord, wordDict);
            if (result) {
                dp[s] = result;
                return dp[s];                
            }
        }
        
        dp[s] = false;
        return dp[s];
    };
    
    return helper(s, wordDict);
};
```
