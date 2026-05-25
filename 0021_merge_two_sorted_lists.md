### 21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

**Example 1:**
```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**
```
Input: l1 = [], l2 = []
Output: []
```

**Example 3:**
```
Input: l1 = [], l2 = [0]
Output: [0]
``` 

**Constraints:**
```
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
```

**Tags**
- Linked List
- Recursion

### Solution:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = None
        newTail = None
        
        while l1 or l2:
            if l1 and not l2:
                smallest = l1
                l1 = l1.next
            elif l2 and not l1:
                smallest = l2
                l2 = l2.next
            elif l2.val > l1.val:
                smallest = l1
                l1 = l1.next
            else:
                smallest = l2
                l2 = l2.next
            
            smallest.next = None
            
            if not newHead:
                newHead = smallest
                newTail = smallest    
            else:
                newTail.next = smallest
                newTail = smallest
            
        return newHead    
```
