### 143. Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

**Example 1:**
```
Given 1->2->3->4, reorder it to 1->4->2->3.
```

**Example 2:**
```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

**Tags**
- Linked List
- Two Pointers
- Stack
- Recursion

### Solution:
- Find the halfway point.
- Break it from the main list and reverse that half.
- Then, one at a time, setup the order of the list pointing at the heads of each list.

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
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    // reverse half of the linked list using slow/fast pointer to find middle
    // then go through both halves and connect them
    let elements = [];
    let ptr = head;
    while (ptr) {
        temp = ptr.next;
        ptr.next = null;
        elements.push(ptr);
        ptr = temp;
    }
    
    let start = 0;
    let end = elements.length - 1;
    let leftFirst = true;
    while (start <= end) {
        if (start === end) {
            elements[start].next = null;
            break;
        }
        if (leftFirst) {
            elements[start].next = elements[end];
            start += 1;
            leftFirst = false;
            continue;
        } else {
            elements[end].next = elements[start];
            end -= 1;
            leftFirst = true;
            continue;
        }
    }
};
```
