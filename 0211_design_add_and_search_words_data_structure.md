### 211. Design Add and Search Words Data Structure
Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

`WordDictionary()` Initializes the object.
`void addWord(word)` Adds word to the data structure, it can be matched later.
`bool search(word)` Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 
**Example**:
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
``` 

**Constraints:**
```
1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
```

**Tags**
- String
- Depth-First Search
- Design
- Trie

### Solution:
- Use a trie data structure.

```
/**
 * ANOTHER IDEA: have a map of word_length -> list of words
 * then add words by length
 * to search words, get word list by length
 * then for each word in word list, compare to the search query
 * count the number of mismatches and dots as you compare query and word char by char.
 * return if the number of mismatches == dots. If they are equal, then return true. return
 * false otherwise.
 */

var TrieNode = function(char) {
    this.char = char;
    this.isWord = false;
    this.children = {};
};
/**
 * Initialize your data structure here.
 */
var WordDictionary = function() {
    this.root = new TrieNode('');
};

/**
 * Adds a word into the data structure. 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    let node = this.root;
    let addNode = function(node, word) {
        if (!node || !word) {
            return;
        }
        let char = word.charAt(0);
        let rest = word.substring(1);
        let child = node.children[char];
        
        if (!child) {
            child = new TrieNode(char);
            node.children[char] = child;
        }
        
        if (rest) {
            addNode(child, rest);
        } else {
            child.isWord = true;
            return;
        }
    };
    
    addNode(node, word);
};

/**
 * Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    let start = this.root;
    
    let recursiveSearch = (node, word) => {
        if (!word) {
            return node.isWord;
        }
        
        let char = word.charAt(0);
        word = word.substring(1);
        let possible = [];
        let child = node.children[char];
        
        if (child) {
            possible.push(child);
        } else if (char === '.') {
            Object.keys(node.children).forEach(keyChar => possible.push(node.children[keyChar]));
        }
        
        if (!possible.length) {
            return false;
        }
        
        for (let i = 0; i < possible.length; i++) {
            if (recursiveSearch(possible[i], word)) {
                return true;
            }
        }
        
        return false;
    };
    
    return recursiveSearch(this.root, word);
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
```
Python Solution
```
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isEnd = False

        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode('*')
        

    def addWord(self, word: str) -> None:
        current = self.root
        
        for char in word:
            if not current.children.get(char):
                node = TrieNode(char)
                current.children[char] = node
            current = current.children.get(char)
            
        current.isEnd = True
        

    def searchWith(self, word, node, pointer):
        length = len(word)
        current = node
        
        while pointer < length:
            char = word[pointer]
            if char == '.':
                for child in current.children.values():
                    if self.searchWith(word, child, pointer + 1):
                        return True
                return False

            if not current.children.get(char):
                return False
            current = current.children.get(char)
            pointer += 1
        
        return current.isEnd
    
    def search(self, word: str) -> bool:
        return self.searchWith(word, self.root, 0)    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
