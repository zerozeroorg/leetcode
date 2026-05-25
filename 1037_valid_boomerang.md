### 1037. Valid Boomerang
Easy

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

**Example 1:**
```
Input: [[1,1],[2,3],[3,2]]
Output: true
```

**Example 2:**
```
Input: [[1,1],[2,2],[3,3]]
Output: false
``` 

**Note:**
```
points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
```

**Tags**
- Array
- Math
- Geometry

### Solution:
- If all the numbers have the same slope, then it is not a valid boomerang!
- BEWARE: if the points are equal, then that is still not a bommerang! So, they must all be different points.

```
/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    let p1 = points[0];
    let p2 = points[1];
    let p3 = points[2];
  
    if ((p1[0] === p2[0] && p1[1] === p2[1]) || 
       p2[0] === p3[0] && p2[1] === p3[1] ||
       p1[0] === p3[0] && p1[1] == p3[1]) {
        return false;
    }
    
    let slope1 = (p2[1] - p1[1]) / (p2[0] - p1[0]);
    let slope2 = (p3[1] - p2[1]) / (p3[0] - p2[0]);
    
    return slope2 !== slope1;
};
```
