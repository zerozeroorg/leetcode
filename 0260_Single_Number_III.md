### 260. Single Number III
Medium

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space. 

**Example 1:**
```
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
```

**Example 2:**
```
Input: nums = [-1,0]
Output: [-1,0]
```

**Example 3:**
```
Input: nums = [0,1]
Output: [1,0]
``` 

**Constraints:**
```
2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
```

**Tags**
- Revisit
- Array
- Bit Manipulation

### Solution
- I only solved it via hashmap.
- Below this one will be an explanation on how to solve this in linear time with constant extra space.
```
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lookup = collections.Counter(nums)
        ans = []
        
        for num in nums:
            if lookup[num] == 1:
                ans.append(num)
        
        
        return ans
```
**Someone else's solution**
1. First, XOR all the numbers. Your result will be the two unique numbers XOR'd itself. For example: A XOR B for 5 and 3 is `110`.
1. Then find the right most, set bit. If A XOR B = `110`, The right most set bit `010`. To get the right most set bit, do `aXORb & -aXORb`.
1. Then go through the list of numbers again and find the numbers where the number has that bit set. To do that, just do `num & rightMostSetBit != 0`. 
This makes sense because number like `101 & 010` would equal 0 whereas `111 && 010` would not equal 0.
1. XOR all those numbers with that right set bit and you should get the first unique number.
1. To get the last unique number, just XOR the first unique number with `aXORb`. So `A XOR aXORb`.
```
class Solution {
    public int[] singleNumber(int[] nums) {
        if (nums == null || nums.length < 2 || nums.length % 2 != 0) {
            throw new IllegalArgumentException("Invalid Input");
        }

        int aXORb = 0;
        for (int n : nums) {
            aXORb ^= n;
        }

        int rightSetBit = aXORb & -aXORb;
        int a = 0;
        for (int n : nums) {
            if ((n & rightSetBit) != 0) {
                a ^= n;
            }
        }

        return new int[] {a, aXORb ^ a};
    }
}
```
