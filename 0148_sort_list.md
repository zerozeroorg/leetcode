### 148. Sort List
Medium

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)? 

**Example 1:**
```
4 -> 2 -> 1 -> 3
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

**Example 2:**
```
-1 -> 5 -> 3 -> 4 -> 0
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Example 3:**
```
Input: head = []
Output: []
``` 

**Constraints:**
```
The number of nodes in the list is in the range [0, 5 * 10^4].
-10^5 <= Node.val <= 10^5
```

**Tags**
- Linked List
- Two Pointers
- Divide and Conquer
- Sorting
- Merge Sort

### Solution:
- Update: Python solution using merge sort and recursion so hope that counts as constant space.
- My solution did not take constant space. It takes O(n) space.
- To take constant space, you have to merge sort the lists.

Python Solution
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Use the sortList function recursively
            
            Split the list in half and sortList each of them
            
            Then while list1 or list2:
            - take the smallest
            - add to result list
            
            return result list
        """
        if not head:
            return None
        
        if not head.next:
            return head
        
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr and fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        second_head = slow_ptr.next
        slow_ptr.next = None
        
        first_list = self.sortList(head)
        second_list = self.sortList(second_head)
        result = ListNode()
        temp = result
        
        
        while first_list or second_list:
            first_val = None
            second_val = None
            
            if first_list:
                first_val = first_list.val
            
            if second_list:
                second_val = second_list.val
            
            if first_val is not None and second_val is not None:
                if first_val < second_val:
                    temp.next = first_list
                    first_list = first_list.next
                else:
                    temp.next = second_list
                    second_list = second_list.next
            elif first_val is not None:
                temp.next = first_list
                first_list = first_list.next
            else:
                temp.next = second_list
                second_list = second_list.next
            
            temp = temp.next
        
        return result.next
                
                
        
```

JS Solutions
```
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    // iterate through the list and put in an array
    // then sort the array by value
    // then for each item in array:
    // set the next point to its next item
    // return the first element in the array
    
    let list = [];
    let current = head;
    
    while (current) {
        list.push(current);
        current = current.next;
    }
    
    list = list.sort((a, b) => {
        return a.val - b.val;
    });
    
    for (let i = 0; i < list.length; i++) {
        let node = list[i];
        let nextNode = list[i + 1] ? list[i + 1] : null;
        node.next = nextNode;
    }
    
    if (list.length) {
        return list[0];
    }
    
    return null;
};
```

- The merge sort solution, which takes O(log n) space because of the recursive call stack
```
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    if (!head || !head.next) {
        return head;
    }
    let middleNode = findMiddleAndSetNull(head);
    let left = sortList(head);
    let right = sortList(middleNode);
    return merge(left, right);
};

var merge = function(left, right) {
    let leftPtr = left;
    let rightPtr = right;
    let newHead = null;
    let current = null;
    
    while(leftPtr || rightPtr) {
        if (!leftPtr) {
            if (!current) {
                current = rightPtr;
                newHead = current;
                rightPtr = rightPtr.next;
                continue;
            } else {
                current.next = rightPtr;
                current = current.next;
                rightPtr = rightPtr.next;
                continue;
            }
        }
        if (!rightPtr) {
            if (!current) {
                current = leftPtr;
                newHead = current;
                leftPtr = leftPtr.next;
                continue;
            } else {
                current.next = leftPtr;
                current = current.next;
                leftPtr = leftPtr.next;
                continue;
            }
        }
        
        if (leftPtr.val < rightPtr.val) {
            if (!current) {
                current = leftPtr;
                newHead = current;
                leftPtr = leftPtr.next;
                continue;
            } else {
                current.next = leftPtr;
                current = current.next;
                leftPtr = leftPtr.next;
                continue;
            }            
        } else {
            if (!current) {
                current = rightPtr;
                newHead = current;
                rightPtr = rightPtr.next;
                continue;
            } else {
                current.next = rightPtr;
                current = current.next;
                rightPtr = rightPtr.next;
                continue;
            }            
        }
    }
    
    return newHead;
};

var findMiddleAndSetNull = function(node) {
    let prev = null;
    let slow = node;
    let fast = node;
    
    if (fast && fast.next) {
        fast = fast.next.next;
        prev = slow;
        slow = slow.next;
    }
    
    if (prev) {
        prev.next = null;    
    }
    
    return slow;
}
```
