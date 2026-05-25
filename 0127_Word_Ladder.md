### 127. Word Ladder
Hard

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

**Example 1:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
```

**Example 2:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
``` 

**Constraints:**
```
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
```

**Tags**
- Revisit
- Hash Table
- String
- Breadth-First Search

### Solution (pattern graph + count map)
```
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            If the end word is not in word list, then return False
            
            We have to create a graph using a hash map where:
            - the key is the pattern like "d*t"
            - and the value is the list of words that fit that pattern: [dot]
            
            After building this graph, use BFS to traverse the graph
            and see if you reach the endWord.
            
            To efficiently do this, have a count[word] -> # of words from beginWord to reach word
            Seed it with count[beginWord] = 1 which is 1 transformation to beginWord -> beginWord
            
            Pop the element from the queue
            Then generate patterns for that element and check if those patterns are in the 
            graph.
            
            Use the count map as a way to skip traversing already traversed steps 
            
            At the end of BFS, return count[endWord]
        """
        if endWord not in wordList:
            return 0
        
        # build the graph
        patterns = collections.defaultdict(list)
        for word in wordList:
            length = len(word)
            for i in range(length):
                pattern = word[:i] + '*' + word[i+1:]
                patterns[pattern].append(word)
        
        queue = collections.deque([beginWord])
        count = collections.defaultdict(int)
        
        # seed the beginWord
        count[beginWord] = 1
        
        while queue:
            word = queue.popleft()
            
            if word == endWord:
                break
                
            n = count[word]
            
            length = len(word)
            for i in range(length):
                pattern = word[:i] + '*' + word[i+1:]
                if pattern in patterns:
                    for candidate in patterns[pattern]:
                        if candidate not in count:
                            count[candidate] = n + 1
                            queue.append(candidate)
        
        return count[endWord]
```

### Solution (generic pattern graph + visited)
```
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            IMPORTANT: use BFS instead of DFS. DFS will run longer
            whereas BFS can run in polynomial time.
            
            First, check if endWord is in the list.
            If not, return 0.
            
            The idea is to create a graph where nodes are connected
            when the words are differ by one char.
            
            Use a queue where each element is a tuple of (word, length).
            Once the word == endWord, return length.
            
            Otherwise, process what words can be used next and remove them
            from wordList and add them to the queue.
        """
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
```
