### 799. Champagne Tower
Medium

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)


**Example 1:**
```
 1
0 0

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
```

**Example 2:**
```
    1
0.5   0.5

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
```

**Example 3:**
```
Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
``` 

**Constraints:**
```
0 <= poured <= 10^9
0 <= query_glass <= query_row < 100
```

**Tags**
- Revisit
- Dynamic Programming

### Solution
```
/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
var champagneTower = function(poured, query_row, query_glass) {
    /*
        After drawing it out, I noticed that -
        - if I can fill the first cup, I subtract one
        - now what? well what is left is half will go to the left side
        and the other half will go to the right side
        
        So the algorithm would be:
        - can I fill my current cup?
        - if yes, then subtract 1 and then divide whats left by half
        and fill the left side and right sides of it
    
        What data structure should I use?
        I think a matrix where the number of columns is varies each row
        
        I drew out the matrix and noticed this:
        
          0
        0   1
       0  1  2
      0 1  2  3
      
      The left side is always the same index as the current and the right side
      is current + 1.
      
      So that is how I will get to the next cups.
      
      UPDATE: this is too slow. Because the number of cups is high (10 ^ 9)
      we need a faster algorithm.
      
      Instead of going through the number of pours (10 ^9), we can go through
      the champagne tower and calculate how much champagne will be there.
      
      Algorithm:
      - starting index (0,0) has total pour cups
      - for each row:
      - for each glass:
      - if there is an excess, calculate what is flowed to the left and right
      and add it to those glasses
      - return Math.min(1, (query_row, query_glass))
    */
    let matrix = [];
    for (let i = 0; i < 100; i++) {
        matrix.push([]);
    }
    
    // set the starting cup with total poured
    matrix[0][0] = poured;
    
    for (let i = 0; i < query_row; i++) {
        for (let j = 0; j <= i; j++) {
            let currentValue = matrix[i][j];
            if (currentValue === undefined) {
                continue;
            }
            if (currentValue > 1) {
                // then it will flow
                let leftover = (currentValue - 1) / 2;
                matrix[i + 1][j] = matrix[i + 1][j] || 0;
                matrix[i + 1][j + 1] = matrix[i + 1][j + 1] || 0;
                matrix[i + 1][j] += leftover;
                matrix[i + 1][j + 1] += leftover;
            }
        }
    }
    
    return Math.min(1, matrix[query_row][query_glass] || 0);
};
```
