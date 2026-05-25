### 216. Combination Sum III
Medium

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

**Note:**
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

**Example 1:**
```
Input: k = 3, n = 7
Output: [[1,2,4]]
```

**Example 2:**
```
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```

**Tags**
- Array
- Backtracking

### Solution:
- The idea is to generate the combinations but use a set to keep track of global combos already used.
- Where did I messed up on?
-- the Set object does not have a length. It has a .size property.
-- I was not keeping track of unique combinations. I had answers like [1, 2, 4] and [1, 4, 2] which are not unique combos.
-- I had to use a newSet every time I passed on to helper. Did not consider that.
```
/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    const uniqueSets = new Set([]);
    
    const helper = (k, n, set) => {
        for (let i = 1; i <= 9; i++) {
            let newSet;
            if (i > n) {
                break;
            }

            if (set.has(i)) {
                continue;
            }
            
            let diff = n - i;
            newSet = new Set([...set]);
            newSet.add(i);
            
            if (newSet.size === k && diff === 0) {
                let nums = [...newSet].sort((a, b) => a - b).join('_');
                if (!uniqueSets.has(nums)) {
                    uniqueSets.add(nums);    
                }
            } else if (newSet.size < k) {
                helper(k, diff, newSet);
            }
        }        
    };
    
    const set = new Set([]);
    helper(k, n, set);
    if (!uniqueSets.size) {
        return [];
    }
    return [...uniqueSets].map(set => set.split('_'));
};
```

### Another Solution:
- Use a start variable so that you can ignore values that you already chosen in the previous iteration:
```
/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    const result = [];
    
    const helper = (k, n, set, start) => {
        for (let i = start; i <= 9; i++) {
            let newSet;
            if (i > n) {
                break;
            }

            if (set.has(i)) {
                continue;
            }
            
            let diff = n - i;
            newSet = new Set([...set]);
            newSet.add(i);
            
            if (newSet.size === k && diff === 0) {
                result.push([...newSet]);
            } else if (newSet.size < k) {
                helper(k, diff, newSet, i + 1);
            }
        }        
    };
    
    const set = new Set([]);
    helper(k, n, set, 1);
    return result;
};
```
