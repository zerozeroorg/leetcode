### 380. Insert Delete GetRandom O(1)
Medium

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity. 

**Example 1:**
```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
``` 

**Constraints:**
```
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
```

**Tags**
- Array
- Hash Table
- Math
- Design
- Randomized

### Solution
To solve for insert and remove in O(1) time, we should use a map to quickly find the element we need and do the necessary inserts/deletes from the map.

The difficulty now is the getRandom in O(1) time. This problem is similar to LRU cache where we need multiple data structures to solve this problem. If we only need to just get a random item with equal probability we can just put the items in a list and pick a random index. We can store the lookup -> index in the array. That will help with inserts (insert it to the end of the list) and getrandom as we know the length of the list and we can quickly pick an index and return that.

For removal, use the same trick in LRU cache where you find the item via the map, then switch places with the last item on the list for easier removal.

```
class RandomizedSet:

    def __init__(self):
        self.count = 0
        self.lookup = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        result = self.lookup.get(val)
        if result is not None:
            return False

        self.lookup[val] = self.count
        self.array.append(val)
        self.count += 1
        return True
        

    def remove(self, val: int) -> bool:
        result = self.lookup.get(val)
        if result is None:
            return False
        
        val_index = self.lookup[val]
        last_element = self.array.pop()
        last_element_index = self.lookup[last_element]
        self.lookup[last_element] = None
        self.count -= 1
        
        if val_index == self.count:
            return True
        
        self.array[val_index] = last_element
        self.lookup[last_element] = val_index
        self.lookup[val] = None
        return True
        

    def getRandom(self) -> int:
        return self.array[random.randrange(0, self.count)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
