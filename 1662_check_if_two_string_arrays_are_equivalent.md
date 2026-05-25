### 1662. Check If Two String Arrays are Equivalent
Easy

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

**Example 1:**
```
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
```

**Example 2:**
```
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
```

**Example 3:**
```
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
``` 

**Constraints:**
```
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
```

**Tags**
- Array
- String

### Solution:
- This was classified as an easy problem, so I should have done the one liner solution!
- That's OK, I like my generator/iterator solution because I get to use Python classes.
```
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
            Ideally, have each word be represented by a generator
            which will get you the next letter.
            Easiest way is to concatenate them all and compare: O(n) space and time.
        """
        class Word:
            def __init__(self, word):
                self.word = word
                self.wordPtr = 0
                self.letterPtr = 0
                self.currentWord = self.getCurrentWord()
                self.currentLetter = self.getCurrentLetter()
            
            def getCurrentWord(self):
                return self.word[self.wordPtr]
            
            def getCurrentLetter(self):
                return self.currentWord[self.letterPtr]
            
            def hasNextWord(self):
                return self.wordPtr < len(self.word)
            
            def hasNextLetter(self):
                return self.letterPtr < len(self.currentWord)
            
            def hasNext(self):
                return self.hasNextLetter() or self.hasNextWord()
            
            def getNextLetter(self):
                self.letterPtr += 1
                if self.hasNextLetter():
                    self.currentLetter = self.getCurrentLetter()
                    return
                self.wordPtr += 1
                if self.wordPtr < len(self.word):
                    self.currentWord = self.getCurrentWord()
                    self.letterPtr = 0
                    self.currentLetter = self.getCurrentLetter()
                    return
                
        
        word1 = Word(word1)
        word2 = Word(word2)
        
        while word1.hasNext() and word2.hasNext():
            if word1.getCurrentLetter() != word2.getCurrentLetter():
                return False
            word1.getNextLetter()
            word2.getNextLetter()
        
        if word1.hasNext() or word2.hasNext():
            return False
        
        return True
        
```
