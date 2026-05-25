### 881. Boats to Save People
Medium

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.) 

**Example 1:**
```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

**Example 2:**
```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```

**Example 3:**
```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

**Note:**
```
1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
```

**Tags**
- Revisit
- Array
- Two Pointers
- Greedy
- Sorting

### Solution:
- Edit: just take the heaviest and lightest person
- Very deceptive problem, lots of cases to consider.
```
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
            Dummy: this is a sorted, two pointer problem, with greedy.
            
            Sort the list and have two pointers at the 
            front and back of the list.
            
            If current is less than limit, increment
            counter. If not, increment total.
            
            If 2 ppl are already seated, then reset.
            
            If current < limit after loop ends, increment total
            Return total
        """
        people = collections.deque(sorted(people))
        total = 0
        current = 0
        ptr1 = 0
        ptr2 = len(people) - 1
        seat = 0
        
        while ptr1 <= ptr2:
            if current + people[ptr2] <= limit and seat < 2:
                current += people[ptr2]
                seat += 1
                ptr2 -= 1
            elif current + people[ptr1] <= limit and seat < 2:
                seat += 1
                current += people[ptr1]
                ptr1 += 1
            else:
                total += 1
                current = 0
                seat = 0
        
        if current <= limit:
            total += 1

        return total
        
```
Better solution
```
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
            sort the list
            then starting from the heaviest,
            see if you can add this person
            if you can, see if you can add the lightest person
            if you cannot, then return with one person boat
            otherwise, return with heavy and lightest person in one boat
        """
        boats = 0
        people = collections.deque(sorted(people))
        
        while people:
            # take heaviest
            first = people.pop()
            diff = limit - first
            if people and diff > 0 and people[0] <= diff:
                people.popleft()
            boats += 1
        
        return boats
                
        
```
