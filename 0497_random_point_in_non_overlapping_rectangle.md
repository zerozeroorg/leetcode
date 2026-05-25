### 497. Random Point in Non-overlapping Rectangles
Medium

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

**Note:**
```
An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
```

**Example 1:**
```
Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]
```

**Example 2:**
```
Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
```

**Explanation of Input Syntax:**
```
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
```

**Tags**
- Array
- Math
- Binary Search
- Reservoir Sampling
- Prefix Sum
- Ordered Set
- Randomized

### Solution:
- compute an array of areas, like [0, 20], [20, 40], [40, 100], [100, 150] and generate a random number between those areas.
- find the area where the random number is within range of that area.
- then generate a (x,y) for that area.

```
/**
 * @param {number[][]} rects
 */
var Solution = function(rects) {
    this.rects = rects;
    let totalArea = 0;
    this.areas = this.rects.map(rect => {
        let area = Math.abs(rect[2] - rect[0] + 1) * Math.abs(rect[3] - rect[1] + 1);
        let startArea = totalArea;
        totalArea += area;
        return [startArea, totalArea]; 
    });
    this.totalArea = totalArea;
};

/**
 * @return {number[]}
 */
Solution.prototype.pick = function() {
    let randomValue = Math.floor(Math.random() * this.totalArea);
    let randomRect;
    for (let i = 0; i < this.areas.length; i++) {
        if (this.areas[i][0] <= randomValue && randomValue < this.areas[i][1]) {
            randomRect = this.rects[i];
            break;
        }
    }
    let randomX = Math.floor(Math.random() * (Math.abs(randomRect[2] - randomRect[0]) + 1)) + randomRect[0];
    let randomY = Math.floor(Math.random() * (Math.abs(randomRect[3] - randomRect[1]) + 1)) + randomRect[1];
    return [randomX, randomY];
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */
```
