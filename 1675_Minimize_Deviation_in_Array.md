### 1675. Minimize Deviation in Array
Hard

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is `[1,2,3,4]`, then you can do this operation on the last element, and the array will be `[1,2,3,2]`.
If the element is odd, multiply it by 2.
For example, if the array is `[1,2,3,4]`, then you can do this operation on the first element, and the array will be `[2,2,3,4]`.
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
```

**Example 2:**
```
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
```

**Example 3:**
```
Input: nums = [2,10,8]
Output: 3
``` 

**Constraints:**
```
n == nums.length
2 <= n <= 10^5
1 <= nums[i] <= 10^9
```

**Tags**
- Revisit
- Array
- Greedy
- Heap (Priority Queue)
- Ordered Set

### Solution
```
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
            Sort so you can update the min and max when you get them
            Get the min
            Get the max
            
            If max is even:
            - divide it
            - compute the new min and max
            
            If min is odd and abs(min * 2 - max) is better:
                - min * 2
                - compute the new min and max
                
            Problem: infinite recursion for: [10, 4, 3]
            
            [6 4 5]
            
            UPDATE: ok after some research, the idea is basically the same
            as above: You make both the min and max as close in value as you 
            can.
            
            To avoid infinite recursion and an extra operation, you can
            double all odd numbers so that you only just have to deal
            with even numbers and minimize them.
            
            Then you take the max number:
            1. If it is odd, then this is the best you can do since
            you can only double it and you don't want to double the max.
            So take the difference of min and that max and return that.
            2. If it is even, divide it and add it back to the list
            and get the min and max. Then compute the diff
            3. Important: always try to compute the new min. In the case of
            [6,10] If you wait til both min and max are odd [3,5] the diff is 2. 
            But the real min diff
            is [5,6]
            
            Return the minimum diff.
            
            Ideally, you have a max-heap. But for python we will use 
            a sorted list.
            Assuming a max heap, the run time is:
            - Double any odd numbers: O(n)
            - Load all numbers in a sorted list: O(n log n)
            - Get the max and min and diff O(1)
            - and divide by 2 and add it back to get new max (log n)
            4. Do step 3 until max is odd O(n)
            5. Return min diff
            
            Total runtime: O(n log n)
            Total space: O(n)
        """
        best = None
        
        from sortedcontainers import SortedList
        
        sorted_list = SortedList()
        for num in nums:
            if num % 2 != 0:
                num = num * 2
            sorted_list.add(num)
        
        while True:
            min_num = sorted_list[0]
            max_num = sorted_list[-1]
            diff = max_num - min_num
            
            if not best:
                best = diff
            else:
                best = min(best, diff)
            
            if max_num % 2 == 0:
                sorted_list.pop()
                sorted_list.add(max_num // 2)
            else:
                break
                
        return best
```
