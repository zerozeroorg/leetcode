### 1286. Iterator for Combination
Medium

Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
 

**Example 1:**
```
Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
```

**Constraints:**
```
1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 10^4 calls will be made to next and hasNext.
It's guaranteed that all calls of the function next are valid.
```

**Tags**
- Revisit
- String
- Backtracking
- Design
- Iterator

### Solution
- Generate all combos, or generate the next one iteratively.
- Generate iteratively is very hard
```
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.pointers = [i for i in range(self.length)]
        

    def getNext(self):
        pointers = self.pointers.copy()
        
        if pointers[-1] + 1 == len(self.characters):
            found = False
            for i in range(len(pointers) - 1, 0, -1):
                if pointers[i - 1] < pointers[i] - 1:
                    inc = pointers[i - 1] + 1
                    for j in range(i - 1, len(self.pointers)):
                        pointers[j] = inc
                        inc += 1
                    found = True
                    break
            if not found:
                return None
        else:
            pointers[-1] += 1        
        
        return pointers
        
    def next(self) -> str:
        ans = "".join([self.characters[i] for i in self.pointers])
        self.pointers = self.getNext()
        return ans
        

    def hasNext(self) -> bool:
        if not self.pointers:
            return False
        for i in range(len(self.pointers)):
            if self.pointers[i] <= len(self.characters) - self.length  - i:
                return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
