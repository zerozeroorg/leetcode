### 26. Remove Duplicates from Sorted Array
Easy

Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.
 

**Example 1:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
``` 

**Constraints:**
```
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
```

**Tags**
- Array
- Two Pointers

### Solution
There is a faster solution shown last
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            Go through elements one at a time
            if the element next to me is the same,
            then mark me as underscore. Otherwise, move on

            Then have two pointers: one for marking
            and one for finding next number.
            Iterate to find the first number, and place it 
            where the marker is. increment both pointers.
        """
        length = len(nums)
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = "_"
        
        marker = 0
        ptr = 0
        while ptr < length:
            if nums[ptr] != "_":
                nums[marker] = nums[ptr]
                marker += 1
            ptr += 1
        
        return marker
```
LeetCode Solution
The idea is to find the first unique element and mark it where it would be.
The first element will be in the correct place, so start the insert index 1.
Then go through the array, starting at index 1 to find the next unique element. If you find it, copy it to the insert index and then increment the insert index.

You have an insertIndex that keeps track of which index to insert unique values
To find a unique value, compare your current number to the previous number. If they are different, update number at insertIndex with current number.
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        return insertIndex
```
