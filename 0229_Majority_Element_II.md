### 229. Majority Element II
Medium

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

**Example 1:**
```
Input: [3,2,3]
Output: [3]
```

**Example 2:**
```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

**Tags**
- Array
- Hash Table
- Sorting
- Counting

### Solution:

- My solution below runs in O(n log n) to sort then count. My mistake was with test case [2,2] where it wanted unique elements. My output returned [2,2]
but the answer should be [2]. I used a set to fix that problem.

```
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let result = new Set();
    let max = Math.floor(nums.length / 3);
    let count = 0;
    
    nums.sort((a, b) => a - b);
    
    for (let i = 0; i < nums.length; i++) {
        let current = nums[i];
        let next = nums[i + 1];
        count += 1;
        
        if (count > max) {
            result.add(current);
        }
        
        if (current !== next) {
            count = 0;        
        }
    }
    
    return [...result];
};
```

**Better Solution:**
- There can only be at most 2 majority elements for elements that appear more than ⌊ n/3 ⌋ times.
- So, you can use four variables: candidate1, candidate2, count1, and count2 to keep track of the candidates and their counts.
- When you encounter a new number and candidates are not initialized, initalize the candidates and increment their counts.
- When you encounter a new number and candidates are already initialized, then decrement their counts.
- When you encounter a new number and candidate counts are zero, you reassign them to the new number as that is the new, better candidate.
- Otherwise, increment their counts.
- Then, you have to loop through the array again to make sure your candidates appear more than ⌊ n/3 ⌋ times.
- What a crazy solution! This is called Boyer-Moore Voting Algorithm
```
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let candidate1 = null;
    let candidate2 = null;
    let count1 = 0;
    let count2 = 0;
    let min = Math.floor(nums.length / 3);
    let result = [];
    
    if (!nums.length) {
        return result;
    }
    
    for (let num of nums) {
        if (candidate1 === num) {
            count1 += 1;
        } else if (candidate2 === num) {
            count2 += 1;
        } else if (count1 === 0) {
            candidate1 = num;
            count1 += 1;
        } else if (count2 === 0) {
            candidate2 = num;
            count2 += 1;
        } else {
            count1 -= 1;
            count2 -= 1;
        }
    }
    
    count1 = 0;
    count2 = 0;
    for (let num of nums) {
        if (num === candidate1) {
            count1 += 1;
        }
        if (num === candidate2) {
            count2 += 1;
        }
    }
    
    if (count1 > min) {
        result.push(candidate1);
    }
    if (count2 > min) {
        result.push(candidate2);
    }
    
    
    return result;
};
```
