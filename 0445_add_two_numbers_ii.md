### 445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Follow up:**
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

**Example:**
```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

**Tags**
- Linked List
- Math
- Stack

### Solution:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            Reverse the linked lists
            Iterate through both lists and add numbers
            If there is a carry, keep track of it in the next
            add.
            After both lists are traversed, check if there is a carry.
            If so, create a new list node and add it to the result.
        """
        
        def reverseList(head):
            newHead = None
            current = head
            
            while current:
                temp = current
                current = current.next
                temp.next = newHead
                newHead = temp
            
            return newHead
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        carry = 0
        result = None
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            ans = val1 + val2 + carry
            if ans >= 10:
                ans -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(ans, result)
            result = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            node = ListNode(carry, result)
            result = node
        
        return result
        
```
