### 160. Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

**Example 1:**
```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
```

**Example 2:**
```
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
``` 

**Example 3:**
```
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
``` 

**Notes:**
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Each value on each linked list is in the range [1, 10^9].
- Your code should preferably run in O(n) time and use only O(1) memory.


**Tags**
- Hash Table
- Linked List
- Two Pointers

### Solution:
My solution:
- Store all the first list nodes into a list (linear time)
- Then go through the second list nodes and see if they are in the list from previous step
- If it is, then you found an intersection!

Best solution:
- First, go through each list and count their lengths
- Once you are done, check the last element of each list. If they are different, return null since there is no intersection
- Then, to account for differing list sizes, have the longer list start abs(len(A) - len(B)) nodes ahead. Then move each ptr one node at a time checking if they are on the same node.

### Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            Get the length of the first linked list
            Get the length of the second linked list
            Get the absolute difference
            Find the longest linked list and move a pointer up
            to the absolute difference
            Move them one by one and check if they are the same
            If they are, return that node
            Return null
        """
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        aLength = getLength(headA)
        bLength = getLength(headB)
        
        if not aLength or not bLength:
            return None

        longNode = headA if aLength > bLength else headB
        shortNode = headA if longNode == headB else headB
        diff = abs(aLength - bLength)
        
        while diff > 0 and longNode:
            diff -= 1
            longNode = longNode.next
        
        while longNode and shortNode:
            if longNode == shortNode:
                return longNode
            longNode = longNode.next
            shortNode = shortNode.next
        
        return None
        
```
