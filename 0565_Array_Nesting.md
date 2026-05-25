### 565. Array Nesting
Medium

You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k]. 

**Example 1:**
```
Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
```

**Example 2:**
```
Input: nums = [0,1,2]
Output: 1
``` 

**Constraints:**
```
1 <= nums.length <= 105
0 <= nums[i] < nums.length
All the values of nums are unique.
```

**Tags**
- Array
- Depth-First Search

### Solution
```
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
            This is a graph problem
            Let's first represent the graph via adjaceny lists
            where k -> [nums[k]]
            
            Then we just need to detect all the cycles in the graph.
            To do that, we can use a marker to mark which cycles belong
            to a certain set. 
            
            We have a visited map that will mark each
            num with a marker and traverse until we can't traverse anymore
            or we have already visited.
            
            We do this for i in range(len(nums)).
            Then we get the max size of all cycles and return that.
            
            ACTUALLY - the adjacency list is not necessary anymore. The
            nums array is good enough to represent the adjacency list.
            
        """
        visited = {}
        counter = collections.Counter()
        
        def traverse(i, marker):
            if visited.get(i, None) != None:
                return
            
            num = nums[i]
            visited[i] = marker
            counter[marker] += 1
            traverse(num, marker)
        
        for i in range(len(nums)):
            traverse(i, i)
        
        max_length = 0
        for key in counter.keys():
            max_length = max(max_length, counter[key])
        
        return max_length
            
        
            
        
        
```
