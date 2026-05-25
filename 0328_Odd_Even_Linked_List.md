### 328. Odd Even Linked List
Medium

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity. 

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```

**Example 2:**
```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
``` 

**Constraints:**
```
n == number of nodes in the linked list
0 <= n <= 10^4
-10^6 <= Node.val <= 10^6
```

**Tags**
- Linked List

### Solution
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            have a odd head
            have an even head
            iterate through each node:
            - if odd index, move to odd list
            - else move to even list
            connect tail of odd to even
        """
        odd_aux_head = ListNode()
        even_aux_head = ListNode()
        odd_current = odd_aux_head
        even_current = even_aux_head
        count = 1
        current = head
        
        while current:
            next_ptr = current.next
            current.next = None
            
            if count % 2 == 1:
                odd_current.next = current
                odd_current = odd_current.next
            else:
                even_current.next = current
                even_current = even_current.next
            
            current = next_ptr
            count += 1
        
        # check empty lists
        if odd_aux_head.next:
            odd_current.next = even_aux_head.next
        
        return odd_aux_head.next
        
        
```
