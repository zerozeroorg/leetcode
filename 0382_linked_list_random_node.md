### 382. Linked List Random Node
Medium

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

**Follow up:**
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

**Example:**
```
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
```

**Tags**
- Revisit
- Linked List
- Math
- Reservoir Sampling
- Randomized

### Solution:
- I decided to get the size first, then randomly select an element within that size.
- There is an algorithm for randomly selecting k items out of an unknown size, n. It is called reservoir sampling. I will implement this below as well!
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        self.count = count
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        index = random.randint(0, self.count - 1)
        count = 0
        ptr = self.head
        while count != index:
            count += 1
            ptr = ptr.next
        return ptr.val
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

**Reservoir Sampling**
- Take the first k elements from unknown stream of (unknown size, n)
- iterate through k to the end of the stream (n - 1) inclusive, we call this index
- get a random number between 0 and index
- if the random number is less than k, we replace output[randomIndex] = stream[index]
- return output
- for this problem, k is 1. 
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        output = self.head
        ptr = self.head
        count = 1
        
        while ptr:
            if random.random() < 1 / count:
                output = ptr
            count += 1
            ptr = ptr.next
        
        return output.val    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```
