### 219. Contains Duplicate II
Easy

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.

**Example 1:**
```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**
```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Tags**
- Array
- Hash Table
- Sliding Window

### Solution
```
My solution:
- Use a map and store all the indexes for a duplicate
- Then iterate each duplicate and check all indexes:
- If there is a pair of indexes that is <= k, then return true
- Return false if none are found

Cleaner solution:
- Use a map
- As you store an index, check if there is a previous index.
- If there is, get the diff
- If it is <= k, return true
- Otherwise, store the new index
- If no diff is found, return false
```
