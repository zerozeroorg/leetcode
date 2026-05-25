### 138. Copy List with Random Pointer
Medium

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

**Example 1:**
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2:**
```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3:**
```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

**Constraints:**
```
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
```

**Tags**
- Hash Table
- Linked List

### Solution
```
/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    /*
        Go through the list and create the new list
        But as you create the list, replace the val of the
        original list val with the index of the copy list
        and have a map of index -> copy node.
     */
    let newHeadPtr = new Node();
    let newCurrent = newHeadPtr;
    let lookup = {};
    let current = head;
    let index = 0;
    
    while(current) {
        let newNode = new Node(current.val);
        newCurrent.next = newNode;
        newCurrent = newCurrent.next;
        
        // setup lookup
        current.val = index;
        lookup[index] = newNode;
        index += 1;
        
        // move head
        current = current.next;
    }
    
    current = head;
    newCurrent = newHeadPtr.next;
    while(current) {
        let random = current.random;
        if (random) {
            newCurrent.random = lookup[random.val];    
        }
        
        current = current.next;
        newCurrent = newCurrent.next;
    }
    
    return newHeadPtr.next;
};
```
