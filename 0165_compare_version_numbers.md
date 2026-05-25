### 165. Compare Version Numbers
Medium

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

**Example 1:**
```
Input: version1 = "0.1", version2 = "1.1"
Output: -1
```

**Example 2:**
```
Input: version1 = "1.0.1", version2 = "1"
Output: 1
```

**Example 3:**
```
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
```

**Example 4:**
```
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
```

**Example 5:**
```
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
``` 

**Note:**
Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.

**Tags**
- Two Pointers
- String

### Solution
- Ugh, I redeclared let version1!
```
/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    // one might be less digits then the other
    // 001 -> 1
    
    version1 = version1.split('.');
    version2 = version2.split('.');
    let ptr1 = 0;
    let ptr2 = 0;
    
    while(ptr1 < version1.length || ptr2 < version2.length) {
        let num1 = parseInt(ptr1 < version1.length ? version1[ptr1] : "0", 10);
        let num2 = parseInt(ptr2 < version2.length ? version2[ptr2] : "0", 10);
        
        if (num1 < num2) {
            return -1;
        }
        
        if (num1 > num2) {
            return 1;
        }
        
        ptr1 += 1;
        ptr2 += 1;
    }
    
    return 0;
};
```
Python:
```
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        ptr = 0
        length1 = len(version1)
        length2 = len(version2)
        
        while ptr < length1 or ptr < length2:
            rv1 = int(version1[ptr]) if ptr < length1 else 0
            rv2 = int(version2[ptr]) if ptr < length2 else 0
            
            if rv1 < rv2:
                return -1
            elif rv1 > rv2:
                return 1
            
            ptr += 1
        
        return 0
```
