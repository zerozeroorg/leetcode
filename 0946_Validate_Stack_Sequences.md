### 946. Validate Stack Sequences
Medium

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
 

**Example 1:**
```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

**Example 2:**
```
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
``` 

**Constraints:**
```
1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
```

**Tags**
- Array
- Stack
- Simulation

### Solution
- Add all pushed elements til you push an element that is equal to the first popped element
- Then try to remove all elements based on the next popped element state until you cannot
- Do this until the pushed array is empty, and the simulated array is empty.
```
/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    let simulation = [];
    
    while(popped.length) {
        let pop = popped[0];
        
        while(pushed.length && pushed[0] !== pop) {
            simulation.push(pushed.shift());
        }
        
        if (pushed.length && pushed[0] === pop) {
            popped.shift();
            pushed.shift();
        }
        
        while(simulation.length && popped.length && simulation[simulation.length - 1] === popped[0]) {
            simulation.pop();
            popped.shift();
        }
        
        if (simulation.length && !pushed.length && popped.length) {
            return false;
        }
    }
    
    return true;
};
```
