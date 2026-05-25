### 24. Swap Nodes in Pairs
Medium

Medium

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed. 

**Example 1:**
```
1 -> 2 -> 3 -> 4
2 -> 1 -> 4 -> 3

Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

**Example 2:**
```
Input: head = []
Output: []
```

**Example 3:**
```
Input: head = [1]
Output: [1]
``` 

**Constraints:**
```
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
```

**Tags**
- Linked List
- Recursion

### Solution:
- Have a left and right pointer that is eligible for swapping. This is linear time.
- The idea is to take two at a time, swap them, then add them to the resulting linked list.
- Another solution I had was split the linked list into two, then combine them. This is 2(n) linear time.
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        left = None
        current = head
        if not current or not current.next:
            return current
        right = current.next
        newHead = None
        
        while right:
            temp = right.next
            right.next = current
            current.next = temp
            
            if left:
                left.next = right
                
            if not newHead:
                newHead = right
            
            # switch positions to correct current and right
            temp = right
            right = current
            current = temp
            
            # then move pointers if you can
            if not left:
                left = current
            else:
                left = left.next
            right = right.next
            current = current.next
            
            if right:
                right = right.next
                current = current.next
                left = left.next
            
            
        return newHead
        
```
Slower Solution
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode()
        second = ListNode()
        ptr = head
        firstPtr = first
        secondPtr = second
        count = 0
        
        while ptr:
            if count % 2 == 0:
                firstPtr.next = ptr
                firstPtr = firstPtr.next
            else:
                secondPtr.next = ptr
                secondPtr = secondPtr.next
            
            temp = ptr.next
            ptr.next = None
            ptr = temp
            count += 1
        
        result = ListNode()
        resultPtr = result
        firstPtr = first.next
        secondPtr = second.next
        count = 0
        
        while firstPtr or secondPtr:
            if count % 2 == 0:
                if secondPtr:
                    resultPtr.next = secondPtr
                    secondPtr = secondPtr.next
                else:
                    resultPtr.next = firstPtr
                    firstPtr = firstPtr.next
            else:
                if firstPtr:
                    resultPtr.next = firstPtr
                    firstPtr = firstPtr.next
                else:
                    resultPtr.next = secondPtr
                    secondPtr = secondPtr.next
            
            resultPtr = resultPtr.next
            count += 1
                    
        
        return result.next
                
        
```
