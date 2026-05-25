### 763. Partition Labels
Medium

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

**Example 1:**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

**Note:**
```
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
```

**Hint:**
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.

**Tags**
- Revisit
- Hash Table
- Two Pointers
- String
- Greedy

### Solution:

```
/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function(S) {
    // first, create a map of letters to array of indexes
    let map = {};
    for (let i = 0; i < S.length; i++) {
        let letter = S[i];
        map[letter] = map[letter] || [];
        map[letter].push(i);
    }
    let intervals = Object.values(map);
    let result = [];
    // then iterate through the map and pull out each interval
    // then, for each interval:
    while(intervals.length) {
        let interval = intervals.shift();
        let ptr = 0;
        while (ptr < intervals.length) {
            let other = intervals[ptr];
            let minInterval = Math.min(...interval);
            let maxInterval = Math.max(...interval);
            let minOther = Math.min(...other);
            let maxOther = Math.max(...other);
            if (maxInterval < minOther) {
                ptr += 1;
            } else if (maxOther < minInterval) {
                ptr += 1;
            } else {
                interval = [Math.min(minInterval, minOther), Math.max(maxInterval, maxOther)];
                intervals.splice(ptr, 1);
            }
        }
        result.push(interval);
    }
    // check if it can be merged with another interval. If yes, merge
    // if no, skip
    // keep going until interval list is empty
    // then return the lengths of each merged interval
    return result.map(interval => interval[interval.length - 1] - interval[0] + 1);
};
```
*What I messed up on:*
- I used interval instead of other when getting the minOther and maxOther
- I didn't remove the merged interval from the interval array
- I did not consider if an interval was a subinterval of the other, and vice versa. I have to consider overlaps and subintervals.


### Another Solution:
Algorithm:
- Get the max index of each character in the string, S and store it in a hashmap.
- Then, for each index, letter in S:
-- Get the max of the index and the maxIndex.
-- If the maxIndex is equal to the current index, then you hit your partition! Add the size to result.
```
/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function(S) {
    // first, create a map of letters maxIndex of the letter
    let map = {};
    for (let i = 0; i < S.length; i++) {
        let letter = S[i];
        map[letter] = map[letter] || 0;
        map[letter] = Math.max(map[letter], i);
    }
    
    let result = [];
    let maxIndex = -1;
    let size = 0;
    for (let i = 0; i < S.length; i++) {
        size += 1;
        let index = map[S[i]];
        maxIndex = Math.max(maxIndex, index);
        
        if (maxIndex === i) {
            result.push(size);
            maxIndex = -1;
            size = 0;
        }
        
        
    }
    
    
    return result;
};
```
