### 208. Implement Trie (Prefix Tree)
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
```
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
``` 

**Example 1:**
```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
``` 

**Constraints:**
```
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
```

**Tags**
- Hash Table
- String
- Design
- Trie

### Solution
```
class TrieNode:
    def __init__(self, char, is_word=False):
        self.char = char
        self.is_word = is_word
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")
        

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            next_node = current.children.get(char)
            if next_node:
                current = next_node
            else:
                new_node = TrieNode(char)
                current.children[char] = new_node
                current = new_node
        current.is_word = True


    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            next_node = current.children.get(char)
            if not next_node:
                return False
            current = next_node
        return current.is_word
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            next_node = current.children.get(char)
            if not next_node:
                return False
            current = next_node
        return True       
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
My JS Solution
```
var TrieNode = function(char) {
    this.char = char;
    this.isWord = false;
    this.children = {};
};
/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.root = new TrieNode('');
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    
    let addNode = function(node, word) {
        if (!node || !word) {
            return;
        }
        let letter = word.charAt(0);
        let child = node.children[letter];
        if (!child) {
            child = new TrieNode(letter);
            node.children[letter] = child;
        }
        let remainder = word.substring(1);
        if (!remainder) {
            child.isWord = true;
            return;
        }
        addNode(child, remainder);
    };
    
    addNode(node, word);
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root;
    for(let i = 0; i < word.length; i++) {
        let letter = word[i];
        let child = node.children[letter];
        if (!child) {
            return false;
        }
        node = child;
    }
    if (!node.isWord) {
        return false;
    }
    
    return true;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for(let i = 0; i < prefix.length; i++) {
        let letter = prefix[i];
        let child = node.children[letter];
        if (!child) {
            return false;
        }
        node = child;
    }
    
    return true;    
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```
