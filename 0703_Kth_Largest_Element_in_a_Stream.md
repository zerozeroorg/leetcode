### 703. Kth Largest Element in a Stream
Easy

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

**Example 1:**
```
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
``` 

**Constraints:**
```
1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
```

**Tags**
- Tree
- Design
- Binary Search Tree
- Heap (Priority Queue)
- Binary Tree
- Data Stream

### Solution
```
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapify(self.heap)
        
        for num in nums:
            self.add(num)
        
        

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        
        while len(self.heap) > self.k:
            heappop(self.heap)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
