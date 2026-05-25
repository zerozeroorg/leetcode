### 128. Longest Consecutive Sequence
Medium

Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
 
```
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
``` 

Constraints:
```
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
```

**Tags**
- Array
- Hash Table
- Union-Find

### Solution
Naive solution:
- Sort the array
- Then find the LCS, ignoring dups

Optimal solution:
- Create a hashmap or hashset of nums
- Then for each num in the hash:
- Check if there is a num2 that is num + 1. Do this check until you can't find one. Then take the max of LCS and current LCS.
- You can also check if the current num is already in a sequence with num - 1 check in the hash. Then all you have to do is check if your current num is the start of a sequence.
```
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let numMap = [];
    nums.forEach(num => numMap[num] = true);
    let lcs = 0;
    let current = 0;

    console.log(Object.keys(numMap));
    Object.keys(numMap).forEach(key => {
        if (numMap[key] === false) {
            return;
        }

        current = 1;
        nextNum = parseInt(key, 10) + 1;
        while (numMap[nextNum.toString()] !== undefined) {
            numMap[nextNum.toString()] = false;
            nextNum += 1;
            current += 1;
        }

        lcs = Math.max(lcs, current);
        current = 0;
    });

    return Math.max(lcs, current);
};
```
