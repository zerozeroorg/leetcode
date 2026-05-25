## 28. Implement strStr()
Easy

Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

**Example 1:**
```
Input: haystack = "hello", needle = "ll"
Output: 2
```

**Example 2:**
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return `0` when `needle` is an empty string. This is consistent to C's `strstr()` and Java's `indexOf()`.

**Constraints:**
- haystack and needle consist only of lowercase English characters.

## Solution

An easier way to think about it is creating a sliding window until you find the needle in the haystack. Complexity of that is `O(m * n)` where `m` is the length of the needle and `n` is the length of the haystack.  

My solution:
- First, if the needle has zero length, return 0
- Then have a pointer for each string
- The pointer at the haystack should move until there is a character that matches the first character of the needle
- If no character is found, we return -1
- If there is a character found:
  - we take the next needle.length - 1 of haystack and check if it equals to needle
  - if it does not, we just move the pointer
  - if it does, return the index of the pointer

```
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
  var index = -1;
  var pointer = 0;
  var needleLength = needle.length;
  
  if (haystack === needle || needle.length === 0) {
      return 0;
  }
  
  haystack = haystack.split('');
  
  while(pointer + needleLength <= haystack.length) {
      if (needle === haystack.slice(pointer, pointer + needleLength).join('')) {
          index = pointer;
          break;
      }
      pointer++;
  }
  return index;
};
```
**Tags**
- Two Pointers
- String
- String Matching
