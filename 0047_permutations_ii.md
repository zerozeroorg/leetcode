### 47. Permutations II
Medium

Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

**Example 1:**
```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**Example 2:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
``` 

**Constraints:**
```
1 <= nums.length <= 8
-10 <= nums[i] <= 10
```

**Tags**
- Array
- Backtracking
- Sorting

### Solution:

```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
            Generate permutations by:
            - taking one number, and permute the other numbers
            - add it to a global set
            Then return the set of unique numbers
        """
        unique = set([])
        def permute(nums):
            if len(nums) == 1:
                return [nums]
            
            result = []
            for index in range(len(nums)):
                num = nums[index]
                other = permute(nums[0: index] + nums[index + 1:]) 
                for choices in other:
                    result.append([num] + choices)
            
            return result
        
        choices = permute(nums)
        for choice in choices:
            arr = [str(n) for n in choice]
            unique.add("_".join(arr))
        
        return [ans.split("_") for ans in unique]
                
                
        
```
