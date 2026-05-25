### 525. Contiguous Array
Medium

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

**Example 1:**
```
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
```

**Example 2:**
```
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```
Note: The length of the given binary array will not exceed 50,000.

**Tags**
- Revisit
- Array
- Hash Table
- Prefix Sum

### Solution:
- create an array that will keep track of 1s and 0s at each point. If you see a zero, subtract from count. If you see a one, add to count.
- If the count reaches, zero, then there are equal ones and zeroes at that point.
- Also, if the count is reached more than once in the array, then there are equal 1s and 0s. Observe:
```
[ 0 1 1 0 1 0  0  0  1 1  0]
[-1 0 1 0 1 0 -1 -2 -1 0 -1]
```
Take the largest distance between two matched counts will get you the largest continguous equal 1s and 0s (be careful: it is the start + 1...end)

```
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
//     let max = 0;
//     let count = 0;
    
//     // setup
//     let map = {};
//     map[0] = -1;
    
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] === 0) {
//             count += -1;
//         } else {
//             count += 1;
//         }
        
//         if (map[count] === undefined) {
//             map[count] = i;
//         } else {
//             max = Math.max(max, (i - map[count]));
//         }
//     }
//     return max;

    // turn all the zeroes into -1s
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            nums[i] = -1;
        }
    }
    
    let answer = 0;
    let prefix = [0];
    // build prefix sums
    for (let i = 0; i < nums.length; i++) {
        let last = prefix[prefix.length - 1];
        prefix.push(last + nums[i]);
    }
    // find max length of zeroes
    let first_occurrence = {};
    
    for (let i = 0; i < prefix.length; i++) {
        let sum = prefix[i];
        if (first_occurrence[sum] === undefined) {
            first_occurrence[sum] = i;            
        } else {
            answer = Math.max(answer, i - first_occurrence[sum]);
        }
    }
    return answer;
};
```
Python Solution
- Using the map to store the first occurrence of when a count was set is genius
```
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 0
        count = 0
        first_occurrence = {}
        first_occurrence[0] = -1
        
        for i in range(length):
            num = nums[i]
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if first_occurrence.get(count) is None:
                first_occurrence[count] = i
            else:
                answer = max(answer, i - first_occurrence[count])
        
        return answer
            
                
```
