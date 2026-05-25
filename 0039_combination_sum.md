### 39. Combination Sum
Medium

Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. 

**Example 1:**
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

**Example 2:**
```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**
```
Input: candidates = [2], target = 1
Output: []
```

**Example 4:**
```
Input: candidates = [1], target = 1
Output: [[1]]
```

**Example 5:**
```
Input: candidates = [1], target = 2
Output: [[1,1]]
```

**Constraints:**
```
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
```

**Tags**
- Array
- Backtracking

### Solution:
- Just generate all the combos. No other way to do it.
- An optimization is to not try all the candidates in each loop. Have a starting index and once you tried that index, move to the next one.
```
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let result = new Set([]);
    
    let helper = (elements, candidates, num) => {
        if (num === 0) {
            const ans = elements.sort((a, b) => a - b).join('_');
            if (!result.has(ans)) {
                result.add(ans);
                return;
            }
        }
        
        candidates.forEach(candidate => {
            let diff = num - candidate;
            if (diff < 0) {
                return;
            }
            
            helper([...elements, candidate], candidates, diff);
        })
    };
    
    helper([], candidates, target);
    
    return [...result].map(ans => ans.split('_'));
};
```
Python:
```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            Have a set to get the unique combos
            
            Use recursion which will take a current sum, current numbers
            Maybe need DP?
        """
        result = set()
        length = len(candidates)
        
        def recurse(current_sum, current_numbers, index):
            if current_sum == 0:
                current_numbers.sort()
                result.add(tuple(current_numbers))
                return
            
            for i in range(index, length):
                candidate = candidates[i]
                if current_sum - candidate >= 0:
                    temp = current_numbers[:]
                    temp.append(candidate)
                    recurse(current_sum - candidate, temp, i)
    
        recurse(target, [], 0)
        
        return list(result)
```
