### 347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
``` 

**Constraints:**
```
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
``` 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

**Tags**
- Array
- Hash Table
- Divide and Conquer
- Sorting
- Heap (Priority Queue)
- Bucket Sort
- Counting
- Quickselect

### Solution
I did not beat the O(n log n). To beat O(n log n), you can use a max heap of size k, to get it down to O(n log k)
```
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const counter = new Map();
    
    for (const num of nums) {
        let count = counter.get(num) || 0;
        count += 1;
        counter.set(num, count);
    }
    
    const elements = [];
    counter.forEach((value, key) => {
        elements.push([key, value]);    
    });
    
    return elements.sort((a, b) => b[1] - a[1])
        .filter((value, index) => index < k)
        .map((value) => value[0]);
};
```
