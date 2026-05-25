### 378. Kth Smallest Element in a Sorted Matrix
Medium

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element. 

**Example 1:**
```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

**Example 2:**
```
Input: matrix = [[-5]], k = 1
Output: -5
``` 

**Constraints:**
```
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
```

**Tags**
- Array
- Binary Search
- Sorting
- Heap (Priority Queue)
- Matrix

### Solution
```
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
            Naive approach: just count out the kth element
        """
        heap = []
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in range(rows):
            for col in range(cols):
                heap.append(matrix[row][col])
        
        heapq.heapify(heap)
        elements = heapq.nsmallest(k, heap)
        
        return elements[-1]
```

Here is one that uses max heap:
```
class Solution:
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])  # For general, matrix doesn't need to be a square
        maxHeap = []
        for r in range(m):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)
```

Binary search:
- The idea is to use binary search to count number of elements less than or equal to mid. Then checking if that count is <= k. 
- This sounds crazy so gonna not implement it.
