### 41. First Missing Positive
Hard

Hard

Given an unsorted integer array, find the smallest missing positive integer.

**Example 1:**
```
Input: [1,2,0]
Output: 3
```

**Example 2:**
```
Input: [3,4,-1,1]
Output: 2
```

**Example 3:**
```
Input: [7,8,9,11,12]
Output: 1
```

Follow up:
Your algorithm should run in O(n) time and uses constant extra space.

**Constraints:**
```
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
```

**Tags**
- Array
- Hash Table

### Solution:
This was hard. My solution did not work for [-999, -998, 1]. I also did not use constant extra space.

```
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    let min = Number.MAX_SAFE_INTEGER;
    let lookup = [];
    
    nums.forEach(num => {
        lookup[num] = true;
        min = Math.min(num, min);
    });
    
    if (min !== 1 && !lookup[1]) {
        return 1;
    }
    // min could be -999. Then the array could be [-999, -998, 1]. My for loop will never reach 1.
    min = 1;
    
    for (let i = 0; i < nums.length; i++) {
        const isFound = lookup[min];
        if (!isFound && min !== 0) {
            return min;
        }
        min += 1;
    }
    
    return min;
};
```
