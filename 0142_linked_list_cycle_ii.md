### 142. Linked List Cycle II
Medium

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

**Example 1:**
```
3 -> 2 -> 0 -> -4

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:**
```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

**Constraints:**
```
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
```

**Tags**
- Hash Table
- Linked List
- Two Pointers

### Solution:
- The solution I went with a O(n^2) time, and O(n) space solution. There is a O(n) time, O(1) space solution below mine.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
            Naive solution: put all visited nodes in a list
            Iterate through the list and check if you already visited
            If so, return that node.
            Otherwise, add it to visited list and move the ptr.
        """
        visited = []
        
        def hasVisited(visited, node):
            for visit in visited:
                if node == visit:
                    return True
            
            return False
        
        ptr = head
        
        while ptr:
            if hasVisited(visited, ptr):
                return ptr
            visited.append(ptr)
            ptr = ptr.next
        
        return None
        
```

### Best solution:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slowPtr = head
        fastPtr = head
        
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            
            if slowPtr == fastPtr:
                break
        
        if fastPtr is None or fastPtr.next is None:
            return None
        
        # reset the slow pointer to the head
        # since we detected a cycle, we should
        # be able to find the origin of the cycle
        # by moving slow and fast pointers one by one
        # and seeing where they meet
        slowPtr = head
        while slowPtr != fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        
        return slowPtr
            
       
```
