### 1290. Convert Binary Number in a Linked List to Integer
Easy

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

**Example 1:**
```
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
```

**Example 2:**
```
Input: head = [0]
Output: 0
```

**Example 3:**
```
Input: head = [1]
Output: 1
```

**Example 4:**
```
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
```

**Example 5:**
```
Input: head = [0,0]
Output: 0
``` 

**Constraints:**
```
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
```

**Tags**
- Linked List
- Math

### Solution:
- There is a better solution below this one!

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
            Iterate through the linked list and put them in an array
            Iterate the array backwards:
            return sum (2^n * arr[n]) or n in arr, reverse order
        """
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        
        sum = 0
        arr.reverse()
        for index, num in enumerate(arr):
            sum += (2 ** index) * num
        
        return sum
```

### Best Solution:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
            Shift left with multiply 2
            Then add num
            Repeat
        """
        total = 0
        ptr = head
    
        while ptr:
            total *= 2
            total += ptr.val
            ptr = ptr.next
            
        return total
```
