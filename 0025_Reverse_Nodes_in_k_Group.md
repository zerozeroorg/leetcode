### 25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed. 

**Example 1:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**
```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Example 3:**
```
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
```

**Example 4:**
```
Input: head = [1], k = 1
Output: [1]
``` 

**Constraints:**
```
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
``` 

Follow-up: Can you solve the problem in O(1) extra memory space?

### Tags:
- linked list

**Tags**
- Linked List
- Recursion

### Solution
- Basically, remove the the first k nodes to its own list, shouldn't take extra memory as you are just detaching
- Then reverse that list
- Then connect to the resulting list

- We need a state of newHead and newTail that represents the final solution
- We need a set of k elements that represent the k elements in the list
- We reverse that list (do not reverse as you go, reverse when you get the first k elements)
- Then connect newTail -> the reversedHead
- Update newTail = the reversedTail

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: ListNode):
        new_head = None
        new_tail = None
        ptr = head
        while ptr:
            temp = ptr
            ptr = ptr.next
            temp.next = new_head
            new_head = temp
            if not new_tail:
                new_tail = temp
        
        return (new_head, new_tail)
        
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
            We need:
            - newHead
            - newTail
            - currentHead
            - currentTail
            
            Iterate the first set of k elements and place them in currentHead, currentTail
            Once you have the first set of k elements, reverse them
            Connect the newTail -> reversed currentHead
            Update newTail = reversed currentTail
            
            At the end of the loop, check if there is a currentHead (less than k elements)
            If so, set newTail = currentHead
            return newHead
        """
        count = 0
        new_head = None
        new_tail = None
        ptr = head
        
        current_head = None
        current_tail = None
        while ptr:
            temp = ptr
            ptr = ptr.next
            count += 1
            
            temp.next = None
            if not current_tail:
                current_tail = temp
            else:
                current_tail.next = temp
                current_tail = temp
            
            if not current_head:
                current_head = temp
            
            if count < k:
                continue
            count = 0
            
            (current_head, current_tail) = self.reverseLinkedList(current_head)
            
            if new_head is None:
                new_head = current_head
                new_tail = current_tail
            else:
                new_tail.next = current_head
                new_tail = current_tail

            current_head = None
            current_tail = None
        
        if current_head:
            new_tail.next = current_head
        
        return new_head
                
            
            
        
```
