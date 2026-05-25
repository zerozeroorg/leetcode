### 1032. Stream of Characters
Hard

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

For example, if `words = ["abc", "xyz"]` and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

Implement the StreamChecker class:

StreamChecker(String[] words) Initializes the object with the strings array words.
boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.

**Example 1:**
```
Input
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist
``` 

**Constraints:**
```
1 <= words.length <= 2000
1 <= words[i].length <= 2000
words[i] consists of lowercase English letters.
letter is a lowercase English letter.
At most 4 * 10^4 calls will be made to query.
```

**Tags**
- Revisit
- Array
- String
- Design
- Trie
- Data Stream

### Solution
- The most straightforward solution is to create a trie, and for each query letter you have a list of candidates and check if a candiate has that character suffix. If there are no candidates or is not a word yet, then return False. If any candidate reaches a word, return True.
- The best solution is to create a trie, but store the words backwards! Then you look up the entire stream in the trie. The tricky part here is how to store the trie backwards so that you know if you reached a word. You will need to create a flag for that.
```
class TrieNode:
    def __init__(self, char, isWord=False):
        self.char = char
        self.isWord = isWord
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    
    def add(self, word):
        current = self.root
        
        for char in word:
            if current.children.get(char) is None:
                current.children[char] = TrieNode(char)
            
            current = current.children.get(char)
        
        current.isWord = True
        
    
class StreamChecker:
    """
        For each word - 
        Create a trie
        
        Then for each query -
        - get a list of tries that contain the starting char
        - if none, then return False
        - if there are, check if it forms a word
        - if it does, return True
    """
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.candidates = []
        for word in words:
            self.trie.add(word)
        
        

    def query(self, letter: str) -> bool:
        is_found = False
        new_candidates = []
        
        for candidate in self.candidates:
            result = candidate.children.get(letter)
            if result is not None:
                new_candidates.append(result)
                if result.isWord:
                    is_found = True
        
        result = self.trie.root.children.get(letter) 
        if result is not None:
            new_candidates.append(result)
            if result.isWord:
                is_found = True
        
        self.candidates = new_candidates
        return is_found
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```
