### 605. Can Place Flowers
Easy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule. 

**Example 1:**
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

**Example 2:**
```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
``` 

**Constraints:**
```
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
```

**Tags**
- Array
- Greedy

### Solution:

```
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
            Create a helper function that checks if a position allows
            for planting
            If so, set it to 1 and decrement n by 1.
            If n reaches 0, return True
            return False
            
            I had to add a quick n == 0 check to return for cases like [0], n = 0
        """
        if n == 0:
            return True
        
        def canPlantAt(pos, flowerbed):
            if flowerbed[pos] == 1:
                return False
            
            before = flowerbed[pos - 1] if pos - 1 >= 0 else 0
            after = flowerbed[pos + 1] if pos + 1 < len(flowerbed) else 0
            
            if before == after == 0:
                return True
            
            return False
    
        for pos in range(len(flowerbed)):
            if not canPlantAt(pos, flowerbed):
                continue
            
            flowerbed[pos] = 1
            n -= 1
            if n == 0:
                return True
        
        return False
                
        
```
