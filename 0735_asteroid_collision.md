### 735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

**Example 1:**
```
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
```

**Example 2:**
```
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```

**Example 3:**
```
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
```

**Example 4:**
```
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
```

**Constraints:**
```
1 <= asteroids <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
```

**Tags**
- Array
- Stack
- Simulation

### Solution:
- Very good problem!
- It is better to have a output result list than to change the asteroids list
- Before you add a asteroid, check if it will collide with the last asteroid in result. If it does, pop result then compute the new asteroid.
- Go back to previous step
```
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
            [1], [-1] # no collisions for one asteroid
            [1, 1], [-1, -1] # no collisions for same direction 
            [1, -1], [-1, 1] # collision for right, left, but not left right
            [3, -2, -1]
            
            Below is fine, but have an output list instead of changing asteroids list
            also, need to account for [8, -8] -> []
            using pointers is tricky because when you remove an item, the list size
            changes and the ptr might not be valid
            
            have pointer at position 0
            take the left and right side of the pointer
            if my left collides with me (left is negative, current is positive) compute
            if my right collides with me (current is negative, right is positive) compute
            if no collisions, move pointer by 1
            return final output
        """
        result = []
        
        def helper(result, num):
            while True:
                if len(result) == 0:
                    result.append(num)
                    break
                
                if result[-1] > 0 and num < 0:
                    # collision
                    last = result.pop()
                    if abs(last) == abs(num):
                        break
                    else:
                        num = last if abs(last) > abs(num) else num
                else:
                    result.append(num)
                    break
                
            return result
        
        for num in asteroids:
            result = helper(result, num)
        
        return result
```
