### 1217. Minimum Cost to Move Chips to The Same Position
Easy

We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position. 

**Example 1:**
```
C C C
1 2 3

Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
```

**Example 2:**
```
  C
  C C
  C C
1 2 3
Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at poistion 3 to position 2. Each move has cost = 1. The total cost = 2.
```

**Example 3:**
```
Input: position = [1,1000000000]
Output: 1
``` 
**Constraints:**
```
1 <= position.length <= 100
1 <= position[i] <= 10^9
```

**Tags**
- Revisit
- Array
- Math
- Greedy

### Solution:
```
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
            Get the number of chips at a even position
            Get the number of chips at a odd position
            If one group is bigger than the other group:
            - Take the number of coins in the smaller group, move them with cost of 1
            If they are equal:
            - Then it is the number of coins in one of the groups
        """
        evenCount = 0
        oddCount = 0
        
        for chip in position:
            if chip % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        
        return min(evenCount, oddCount) if evenCount != oddCount else evenCount
        
```
