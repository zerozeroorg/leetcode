### 2610. Convert an Array Into a 2D Array With Conditions
Medium

Medium

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

 

**Example 1:**
```
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
``` 

**Constraints:**
```
1 <= nums.length <= 200
1 <= nums[i] <= nums.length
```

**Tags**
- Array
- Hash Table

### Solution
- 1st approach: create a frequency table. Then iterate nums and count the frequency. Then create a matrix bucket the numbers based on frequency. This is O(nk) where n is the length of nums and k is the highest frequency value.
- 2nd approach: as you create the frequency table, add it to the matrix. Use the current freq value as a way to find the correct bucket. Also, have a max frequency so you know when to create a new array to add to the matrix. This is O(n) time.

```
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findMatrix = function(nums) {
     const lookup = {};
     let maxCount = 0;
     const matrix = [];

     nums.forEach(num => {
         if (lookup[num] === undefined) {
             lookup[num] = 0;
         }
         lookup[num] += 1;
         if (maxCount < lookup[num]) {
             matrix.push([]);
             maxCount += 1;
         }

        matrix[lookup[num] - 1].push(num);
     });

    
     return matrix;
};
```
