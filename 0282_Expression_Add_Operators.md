### 282. Expression Add Operators
Hard

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value. 

**Example 1:**
```
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
```

**Example 2:**
```
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
```

**Example 3:**
```
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
```

**Example 4:**
```
Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
```

**Example 5:**
```
Input: num = "3456237490", target = 9191
Output: []
``` 

**Constraints:**
```
1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1
```

**Tags**
- Math
- String
- Backtracking

### Solution
```
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
            First, print out all the possible expressions
            Be careful of digits that start with zero.
            
            Then evaluate and check if the expression == target.
            
            NOTE: you can have zero operators so "".join(num) == str(target)
        """
        nums = list(num)
        if "".join(nums) == str(target):
            return [str(target)]
        
        def recurse(nums, include_num=False):
            if len(nums) == 1:
                return nums
            
            expressions = []
            pointer = 0
            num_str = ""
            
            if include_num and nums[0] != "0":
                expressions.append("".join(nums))
            
            while pointer < len(nums) - 1:
                num_str += nums[pointer]
                # todo remember to check for 0 digit
                new_nums = nums[pointer + 1:]
                other_side = recurse(new_nums, True)
                pointer += 1
                for operator in ["*", "-", "+"]:
                    for sub_expression in other_side:
                        expressions.append(num_str + operator + sub_expression)
        
                if num_str == "0":
                    break
                    
            return expressions
        
        expressions = recurse(nums)
        result = []
        for expression in expressions:
            if eval(expression) == target:
                result.append(expression)

        return result
        
```
