### 61. Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.

**Example 1:**
```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

**Example 2:**
```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

**Tags**
- Linked List
- Two Pointers

### Solution:
- I messed up on zero rotations. When that happened, I still rotated the head element with the last element. Just do an early return.
- I messed up on my rotation calculation. Once you have the number of rotations, you need to find the node to move the elements. 
- So, it is actually length - rotations

There is another solution! More details below!
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
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    // iterate to get the length of the list
    let tail = null;
    let length = 0;
    let current = head;
    
    while (current) {
        length += 1;
        if (!current.next) {
            tail = current;
        }
        current = current.next;
    }
    
    if (length === 0) {
        return head;
    }
    
    // then do a k % length to get the leftover rotation
    const rotations = k % length;
    
    if (rotations === 0) {
        return head;
    }

    // take elements after length - k and move them to the front
    current = head;
    let count = 0;
    while (count < length - rotations - 1) {
        current = current.next;
        count += 1;
    }
    // I will need a pointer to the tail and the pointer to node before length - k
    tail.next = head;
    head = current.next;
    current.next = null;
    return head;
};


/*
length = 5
k = 2
rotations = 2
length - rotations = 3
*/
```

### Another Solution:
- Have two pointers: slow and fast.
- The fast pointer will iterate through the list k times. If it hits the end of the list, go back to head (this is in case k > length of list)
- Then, once the fast and slow pointers are in position, move the slow and fast pointers until the fast pointer hits the end of the list
- Finally, set the fast pointer's next to point to the head (to connect) then have slow pointer's next be the new head. 
Set slow pointer's next to null and return new head.
