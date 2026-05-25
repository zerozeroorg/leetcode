### 1299. Replace Elements with Greatest Element on Right Side
Easy

Share
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

**Example 1:**
```
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
``` 

**Constraints:**
```
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
```

**Tags**
- Array

### Solution
**Straightforward answer:**
- Start with the first number. Find the biggest number to the right of it and add it to answer array
- Do this for all numbers in the array
- Finally, add -1

This will take n^2 time. For each number, we iterate through a subarray to find the biggest number within that subarray. 

Can we do it in less than n^2? 

**Next step: can we do it in n log n?**

This implies sorting. If we sort, then we lose the positions of the numbers. We would need storage to keep track of each number's position. This seemed very complicated for a problem like this. So I decided not to consider sorting.

**Ok no sorting. Can we do this in n time?**
I started out with small versions of the problem:

- [1] : [-1]
- [6, 1] : [1, -1]
- [4,6,1]: [6,1,-1]
- [5,4,6,1]: [6,6,1,-1]

I noticed a pattern: if we work backwards, I can keep track of the largest number on the right until I find another large number. Then I keep appending that to the list until we are done.

**GOTCHA:**
When iterating backwards, you need to ignore the final element because then your answer array will be larger than the input array.

```
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        max = None
        for num in reversed(arr):
            if len(ans) == len(arr):
                break
                
            if max is None:
                max = num
            
            if max < num:
                max = num
                
            ans.insert(0, max)
        
        return ans
```
