### 228. Summary Ranges
Easy

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 
**Example 1:**
```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

**Example 2:**
```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

**Example 3:**
```
Input: nums = []
Output: []
```

**Example 4:**
```
Input: nums = [-1]
Output: ["-1"]
```

**Example 5:**
```
Input: nums = [0]
Output: ["0"]
``` 

**Constraints:**
```
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
```

**Tags**
- Array

### Solution:
```
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
            create a range list initialized as empty
            for each num in nums:
            - if range list is empty:
            -- insert num as a tuple
            - else:
            -- pop the last tuple in range
            -- compare the biggest number in tuple with the num
            -- if tuple + 1 == num:
            --- num is the new max for that tuple
            --- insert back to the range
            -- else:
            --- insert back to the range
            -- create new tuple and insert to range
            map over the ranges and create answer
            return answer
        """
        ranges = []
        for num in nums:
            if not len(ranges):
                ranges.append([num, num])
                continue
            
            last = ranges.pop()
            if last[1] + 1 == num:
                last[1] = num
                ranges.append(last)
                continue
                
            ranges.append(last)
            ranges.append([num, num])
        
        return map(lambda x: str(x[0]) if x[0] == x[1] else f"{x[0]}->{x[1]}", ranges)
            
            
```
