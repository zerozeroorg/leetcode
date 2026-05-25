### 284. Peeking Iterator
Medium

Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

Implement the PeekingIterator class:
```
PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
int next() Returns the next element in the array and moves the pointer to the next element.
boolean hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.
```
 
**Example 1:**
```
Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False
``` 

**Constraints:**
```
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
All the calls to next and peek are valid.
At most 1000 calls will be made to next, hasNext, and peek.
``` 

Follow up: How would you extend your design to be generic and work with all types, not just integer?

**Tags**
- Array
- Design
- Iterator

### Solution
```
/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {
 *    @ return {number}
 *    this.next = function() { // return the next number of the iterator
 *       ...
 *    }; 
 *
 *    @return {boolean}
 *    this.hasNext = function() { // return true if it still has numbers
 *       ...
 *    };
 * };
 */

/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function(iterator) {
    this.iterator = iterator;
    this.peeked = null;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function() {
    if (this.peeked !== null) {
        return this.peeked;
    }
    this.peeked = this.iterator.next();
    return this.peeked;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function() {
    if (this.peeked !== null) {
        const item = this.peeked;
        this.peeked = null;
        return item;
    }
    return this.iterator.next();
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function() {
    if (this.peeked !== null) {
        return true;
    }
    return this.iterator.hasNext();
};

/** 
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = new PeekingIterator(arr)
 * var param_1 = obj.peek()
 * var param_2 = obj.next()
 * var param_3 = obj.hasNext()
 */
```
Python
```
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.current = None
        if self.iterator.hasNext():
            self.nextOne = self.iterator.next()
        else:
            self.nextOne = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nextOne
        

    def next(self):
        """
        :rtype: int
        """
        self.current = self.nextOne
        if self.iterator.hasNext():
            self.nextOne = self.iterator.next()
        else:
            self.nextOne = None
        return self.current
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextOne is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```
