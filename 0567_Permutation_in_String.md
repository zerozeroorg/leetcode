### 567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
 

**Example 1:**
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**
```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
``` 

**Constraints:**
```
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
```

**Tags**
- Revisit
- Hash Table
- Two Pointers
- String
- Sliding Window

### Solution
The tricky part is knowing how to update the window. One might think you can just move the left and right pointers while updating the counters. When moving the left pointer, just need to subtract count then move left pointer. For right pointer, move pointer then add count. 
```
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Use sliding window. Get the character counts
            of the current window and the character count
            of s1. If they are the same, then return True. Otherwise, False.
            
            Optimization:
            If you use a constant space hashmap of 26 characters, then the
            comparison time is constant. Also, don't recreate the sliding
            window character count. Just update the character count as the 
            window updates.
        """
        s1_counter = collections.defaultdict(int)
        s2_length = len(s2)
        s1_length = len(s1)
        
        for char in s1:
            s1_counter[char] += 1
        
        prev_index = -1
        current_counter = collections.defaultdict(int)
        
        for i in range(s1_length - 1, s2_length):
            if prev_index is -1:
                for j in range(0, s1_length):
                    current_counter[s2[j]] += 1
            else:
                current_counter[s2[prev_index]] -= 1
                if current_counter[s2[prev_index]] == 0:
                    del current_counter[s2[prev_index]]
                current_counter[s2[i]] += 1
            
            if s1_counter == current_counter:
                return True
            
            prev_index += 1
        
        return False
```
JS Solution
```
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    let s1Counter = Array(26).fill(0);
    let s2Counter = Array(26).fill(0);
    let left = 0;
    let right = 0;

    for (const char of s1) {
        s1Counter[char.charCodeAt() - 97] += 1;
    }
    
    while (right < s1.length) {
        s2Counter[s2.charAt(right).charCodeAt() - 97] += 1;
        right += 1;
    }
    right -= 1;
    
    while (right < s2.length) {
        console.log(s1Counter, s2Counter, left, right);
        if (s1Counter.every((num, index) => num === s2Counter[index])) {
            return true;
        }
        if (right === s2.length - 1) {
            break;
        }
        s2Counter[s2.charAt(left).charCodeAt() - 97] -= 1;
        left += 1;

        right += 1;
        s2Counter[s2.charAt(right).charCodeAt() - 97] += 1;
    }

    return false;
};
```
