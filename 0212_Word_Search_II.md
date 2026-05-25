### 212. Word Search II
Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
 
**Example 1:**
```
o a a n
e t a e
i h k r
i f l v

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Example 2:**
```
a b
c d

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
``` 

**Constraints:**
```
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
```

**Tags**
- Revisit
- Array
- String
- Backtracking
- Trie
- Matrix

### Solution
I have posted two solutions: one TLE and the other barely passed.
The difference between the two:
- The first one basically takes each word and finds it in the board. That is too long. There could be repeated work for words like "aaaaaab" and "aaaaaac".
- The second one puts all the words in a trie. Then for each letter in the board, check if it is in the trie. If it is, then build the next letter and check if it is in the trie. Make sure to move the trie node as well to the children.
```
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        result = []
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = [[False for _ in range(cols)] for _ in range(rows)]
        
        def find_word(word):
            length = len(word)
            def recurse(x, y, ptr):
                if ptr == length - 1:
                    return True
                
                seen[x][y] = True
                for i, j in deltas:
                    (nx, ny) = (x + i, y + j)
                    if (0 <= nx < rows and 
                        0 <= ny < cols and 
                        not seen[nx][ny] and 
                        board[nx][ny] == word[ptr + 1]):
                        if recurse(nx, ny, ptr + 1):
                            seen[x][y] = False
                            return True
                seen[x][y] = False
                return False
            
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == word[0] and recurse(i, j, 0):
                        return True
            
            return False
            
        for word in words:
            if find_word(word):
                result.append(word)
        
        return result
        
```
Faster Solution with Trie:
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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        result = set()
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = [[False for _ in range(cols)] for _ in range(rows)]
        trie = Trie()
        
        def find_word(x, y, char, prefix, trie_node):
            next_node = trie_node.children.get(char)
            if not next_node:
                return
            
            if next_node.is_word:
                result.add(prefix)
            
            seen[x][y] = True
            for i, j in deltas:
                (nx, ny) = (x + i, y + j)
                if (0 <= nx < rows and 
                    0 <= ny < cols and 
                    not seen[nx][ny]):
                    find_word(nx, ny, board[nx][ny], prefix + board[nx][ny], next_node)
            seen[x][y] = False
            
                        
        for word in words:
            trie.insert(word)
            
        for i in range(rows):
            for j in range(cols):
                find_word(i, j, board[i][j], board[i][j], trie.root)
        
        return list(result)
        
```
