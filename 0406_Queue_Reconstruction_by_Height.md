### 406. Queue Reconstruction by Height
Medium

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue). 

**Example 1:**
```
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
```

**Example 2:**
```
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
``` 

**Constraints:**
```
1 <= people.length <= 2000
0 <= hi <= 10^6
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
```

**Tags**
- Revisit
- Array
- Binary Indexed Tree
- Segment Tree
- Sorting

### Solution
```
/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    /**
        Not very intuitive, so you will need to think about it a bit.

        If you have 2 people with the same height, you simply sort
        them relatively by k index. For example:

        [7,1], [7,0]

        Would be sorted like: [7,0] [7,1]

        What if there is a shorter person, [6,1] joins? Well that person has
        to be at the index specified in k because they are the shortest and
        the rest of the queue is already full of people taller than them.
        Therefore, you know that that short person has to be in index k:

        [7,0] --[6,1]-- [7,1]

        So first sort by tallest h, then by k. Then insert each person into the
        queue by their k index.
    */
    people = people.sort((a, b) => {
        if (a[0] - b[0] > 0) {
            return -1;
        }
        
        if (a[0] - b[0] < 0) {
            return 1;
        }
        
        if (a[1] - b[1] > 0) {
            return 1;
        }
        
        if (a[1] - b[1] < 0) {
            return -1;
        }
        
        return 0;
    });
    
    let arr = [];
    for (let i = 0; i < people.length; i++) {
        let person = people[i];
        arr.splice(person[1], 0, person);
    }
    
    return arr;
};
```
