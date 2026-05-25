### 90. Subsets II
Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order. 

**Example 1:**
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:**
```
Input: nums = [0]
Output: [[],[0]]
``` 

**Constraints:**
```
1 <= nums.length <= 10
-10 <= nums[i] <= 10
```

**Tags**
- Array
- Backtracking
- Bit Manipulation

### Solution
- To generate a power set, simply do the following:
- For each number, in the list, get the subset of the rest of the list with that number and without that number
- It is similar to binary number bit flipping.
```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set([])
        nums.sort()
        
        def get_subsets(arr, result):
            if not arr and result:
                key = "_".join(map(str, result))
                subsets.add(key)
                return
            
            if arr:
                # add first element
                get_subsets(arr[1:], result + [arr[0]])
            
                # don't add first element
                get_subsets(arr[1:], result)
            
            
        
        get_subsets(nums, [])
        
        result = [[]]
        for subset in subsets:
            result.append(list(map(int, subset.split("_"))))    
        
        return result
```
