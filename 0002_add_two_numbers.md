### 2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
**Example 1:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
``` 

**Constraints:**
```
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```

**Tags**
- Linked List
- Math
- Recursion

### Solution:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        newHead = ListNode(None, None)
        nextNode = newHead
        
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            total = num1 + num2 + carry
            
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            
            temp = ListNode(total, None)
            nextNode.next = temp
            nextNode = temp
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # double check carry
        if carry > 0:
            temp = ListNode(carry, None)
            nextNode.next = temp
            nextNode = temp
        
        # unattach sentinel node
        temp = newHead.next
        newHead.next = None
        newHead = temp
        return newHead
```
