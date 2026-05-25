### 55. Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise. 

**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
``` 

**Constraints:**
```
1 <= nums.length <= 104
0 <= nums[i] <= 105
```

**Tags**
- Revisit
- Array
- Dynamic Programming
- Greedy

### Solution
```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            The DP solution (w/ memo) I had initially didn't work
            because I was trying out all the jump points
            from an index. It took too long.
            
            The idea is from a particular index, try to reach
            as far down as possible. If you encounter another
            index that can reach even further, then go as far as possible.
            We will call this max_jump.
            
            If while iterating the index, you reach an index that is greater
            than max_jump, then no previous step or index can reach this
            index. Therefore, you cannot reach this index. Exit.
            
            At the end, if you are at the end of the loop then return True.
            Otherwise, return False.
        """
        max_jump = 0
        length = len(nums)
        
        for i in range(length):
            if i > max_jump:
                return False
            
            max_jump = max(max_jump, nums[i] + i)
        
        return True
                
        
```
