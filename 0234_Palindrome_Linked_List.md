### 234. Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.

**Example 1:**
```
Input: 1->2
Output: false
```

**Example 2:**
Input: 1->2->2->1
Output: true
```

Follow up:
Could you do it in O(n) time and O(1) space?

**Tags**
- Linked List
- Two Pointers
- Stack
- Recursion

### Solution:
```
My solution:
Reverse half of the linked list then do two pointer comparison:
- Find the length of the linked list
- Have two pointers: both will traverse half of the list. One pointer will reverse as it traverses
- Now you have a pointer that will continue with the other half of the list and the other pointer traversing the first half in reverse order. Do palindrome check.

Better solution:
- No need to find length of the linked list. Just have one move one at a time and the other 2 at a time. When the fast pointer stops, your slow pointer will already be halfway.
- Do the same logic as above: reserve half then do palindrome check
```
