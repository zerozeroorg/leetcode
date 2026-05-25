### 82. Remove Duplicates from Sorted List II
Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well. 

**Example 1:**
```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

**Example 2:**
```
Input: head = [1,1,1,2,3]
Output: [2,3]
``` 

**Constraints:**
```
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
```

**Tags**
- Linked List
- Two Pointers

### Solution:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
            Have a prev and current pointer
            Check if the current pointer is equal to next
            If so, then delete all nodes that have the same value
            as the current pointer
            Continue
            Else, move prev and current pointer by one
            
            Another way: use a list and push nodes into the list
            Before pushing, if the list is equal to the last item,
            then do not add it.
        """
        prev = None
        current = head
        newHead = None

        if not head or not head.next:
            return head
        
        def removeNodeValues(prev, current):
            value = current.val
            while current and value == current.val:
                nextNode = current.next
                if prev:
                    prev.next = nextNode
                current.next = None
                current = nextNode
            
            return prev, current
        
        while current and current.next:
            if current.val != current.next.val:
                prev = current
                current = current.next
            else:
                prev, current = removeNodeValues(prev, current)
            
            if newHead is None and prev is not None:
                newHead = prev
        
        if prev is None:
            return current
        
        return newHead
```
### Another idea:
Use the concept of a "sentinel node" which is a dummy linked list node whose next points to the head. This will help you avoid headaches when the deletion happens
at the head of the node.
