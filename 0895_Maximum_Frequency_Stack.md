### 895. Maximum Frequency Stack
Hard

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

**Example 1:**
```
Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
``` 

**Constraints:**
```
0 <= val <= 10^9
At most 2 * 10^4 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
```

**Tags**
- revisit
- Hash Table
- Stack
- Design
- Ordered Set

### Solution
My first intuition was to use a heap, but not sure how to handle ordering of elements in the event of a tie

LeetCode Solution is to use a "stack of stack":
- have a mapping of freq -> stack to group frequency of values together. When two values have the same frequencies, you push the latest one so it will be popped off later 
- how do you know what to pop off of this "stack"? Maintain a max frequency value
- Also need a freq map to keep track the freq of a value at any given time.
```
class FreqStack:
    """
        There are two ways:
        1. Use a heap to store a tuple of: (max freq, counter, val) where max freq
        and counter are used in the heap. log n to push, and log n to pop
        
        2. Have 3 data structures:
        - a frequency map
        - a map of frequency_count -> list of numbers that match that count
        - the current max frequency count
        O(1) push/pop, O(n) space
    """
    def __init__(self):
        self.freq_map = collections.Counter()
        self.freq_count = collections.defaultdict(list)
        self.max_freq_count = 0
        

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        count = self.freq_map[val]
        self.freq_count[count].append(val)
        self.max_freq_count = max(self.max_freq_count, count)
        

    def pop(self) -> int:
        top = self.freq_count[self.max_freq_count].pop()
        self.freq_map[top] -= 1
        
        if (len(self.freq_count[self.max_freq_count]) == 0):
            self.max_freq_count -= 1
        
        return top
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```
