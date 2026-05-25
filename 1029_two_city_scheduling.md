### 1029. Two City Scheduling
Medium

A company is planning to interview `2n` people. Given the array costs where `costs[i] = [aCosti, bCosti]`, the cost of flying the 
`ith` person to city `a` is `aCosti`, and the cost of flying the `ith` person to city `b` is `bCosti`.

Return the minimum cost to fly every person to a city such that exactly `n` people arrive in each city.
 

**Example 1:**
```
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
```

**Example 2:**
```
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
```

**Example 3:**
```
Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
```

**Tags**
- Revisit
- Array
- Greedy
- Sorting

### Solution:
I used DP but the easiest solution is in the JS code below.
Another way to solve it is to sort by the differences of going to city A vs city B. If it is cheaper to go to city B, then go to city B!
When you sort by the difference, the first half should go to city B, and the second half should go to city A.
```
/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function(costs) {
	// sort by the difference
	costs.sort((costA, costB) => {
			return (costA[0] - costA[1]) - (costB[0] - costB[1]);
	});
	
	let minCost = 0;
	let n = costs.length / 2;
	for (let i = 0; i < costs.length; i++) {
			if (i < n) {
					minCost += costs[i][0];
			} else {
					minCost += costs[i][1];
			}
	}
	return minCost;
};
```
Slow, DP version
```
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
            use top down dp
        """
        length = len(costs)
        n = length // 2
        top = float('inf')
        matrix = {}
        
        def recurse(index, a, b):
            if index == length:
                return 0
            key = (index, a, b)
            
            if key in matrix:
                return matrix[key]
            
            cost = costs[index]
            
            # can I pick a?
            if a > 0:
                costA = cost[0] + recurse(index + 1, a - 1, b)
            else:
                costA = top
            
            # can I pick b?
            if b > 0:
                costB = cost[1] + recurse(index + 1, a, b - 1)
            else:
                costB = top
                
            matrix[key] = min(costA, costB)
            return matrix[key]
        
        return recurse(0, n, n)
        
```
