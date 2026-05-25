### 147. Insertion Sort List
Medium

Sort a linked list using insertion sort.

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

**Example 1:**
```
Input: 4->2->1->3
Output: 1->2->3->4
```

**Example 2:**
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

**Tags**
- Linked List
- Sorting

### Solution:
- What made this more difficult is that this is a linked list.
- Follow the insertion sort algorithm: have a empty linked list and add items to it in sorted order by comparing it to elements in the list.
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        result = None
        ptr = head
        
        def insertSort(head, node):
            ptr = head
            back = None
            inserted = False
            
            while ptr:
                if ptr.val < node.val:
                    back = ptr
                    ptr = ptr.next
                    continue
                else:
                    node.next = ptr
                    if back:
                        back.next = node
                    else:
                        head = node
                    inserted = True
                    break
            
            if not inserted:
                back.next = node
            
            return head
                
            
        while ptr:
            node = ptr
            ptr = ptr.next
            node.next = None
            
            if result is None:    
                result = node
            else:
                result = insertSort(result, node)
        
        
        return result
```
