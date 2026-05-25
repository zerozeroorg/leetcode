### 331. Verify Preorder Serialization of a Binary Tree
Medium

One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
```
     9
  3     2
4   1     6
```
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree. 

**Example 1:**
```
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
```

**Example 2:**
```
Input: preorder = "1,#"
Output: false
```

**Example 3:**
```
Input: preorder = "9,#,#,1"
Output: false
``` 

**Constraints:**
```
1 <= preorder.length <= 104
preoder consist of integers in the range [0, 100] and '#' separated by commas ','.
```

**Tags**
- String
- Stack
- Tree
- Binary Tree

### Solution
```
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
            Split the string by comma
            Conditions:
            - The entire string should be processed. If there are any left over strings,
            it is not valid
            - If there are not enough strings leftover, then it is not valid
            Need recursive function:
            - check if there is at least one char in the list
            - if not, return False
            - if the current char is a hash, return True
            - preorder left and check if there is a result
            - if false, return false
            - preorder right and check if there is a result
            - if false, return false
        """
        def recurse(nodes):
            if not nodes:
                return False
            current = nodes.pop(0)

            if current == "#":
                return True
            
            left_result = recurse(nodes)
            if not left_result:
                return False

            right_result = recurse(nodes)
            if not right_result:
                return False
            
            return True
        
        nodes = preorder.split(",")

        return recurse(nodes) and len(nodes) == 0
        
```
