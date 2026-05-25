### 997. Find the Town Judge
Easy

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise. 

**Example 1:**
```
Input: n = 2, trust = [[1,2]]
Output: 2
```

**Example 2:**
```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

**Example 3:**
```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
``` 

**Constraints:**
```
1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
```

**Tags**
- Revisit
- Array
- Hash Table
- Graph Theory

### Solution
```
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
            create two hash maps:
            person -> people who trust person
            person -> people that person trusts
            
            Iterate through 1 -> n and check that there is a num
            that has n - 1 people trust them and that num doesn't trust anybody
        """
        trust_count = collections.defaultdict(set)
        trusted_count = collections.defaultdict(set)
        
        for a, b in trust:
            trust_count[b].add(a)
            trusted_count[a].add(b)
        
        for person in range(1, n + 1):
            trusts = trust_count[person]
            if len(trusts) == n - 1 and len(trusted_count[person]) == 0:
                return person
        
        return -1
            
        
```
