## 1081. Smallest Subsequence of Distinct Characters

Medium

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
 
```
Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
``` 

Constraints:
```
1 <= s.length <= 1000
s consists of lowercase English letters.
``` 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

### Solution
```
function smallestSubsequence(s: string): string {
    /**
        The key insights are: 
        1. if you have s = "bab" then with unique characters there are
        two subsequences:
        - ab
        - ba
        You want to pick the string where the characters are lexigraphically increasing.
        "ab" is lexiographically increasing and is lexiographically smaller than "ba".

        With that in mind, you can use a monotonic increasing stack and build the answer character
        by character. If you push a character that is smaller than the top character in the 
        stack, then decide:
        - does the top character appear later in the stack? If yes, then pop
        - if no, then don't pop it since you need unique characters in the subsequence

        So [b, a] is now [a] using the example above. The b character will come next and there
        is your answer.

        To keep track if a character appears later, you can use a character count. Since you are processing from left to right, a non-zero count means it will appear later in the string.

        Finally, to make sure everything is unique, you can create a set to keep track of characters you already pushed to the stack. If a duplicate character shows up, then don't push it in the stack.
     */
    const stack = [];
    const charArray = s.split("");
    const currentSet = new Set<string>();

    const counter = charArray.reduce((acc, val) => {
        acc.set(val, (acc.get(val) ?? 0) + 1);
        return acc;
    }, new Map<string, number>());

    console.log(counter);

    charArray.forEach(char => {
        console.log(stack);
        if (stack.length === 0) {
            stack.push(char);
            currentSet.add(char);
            counter.set(char, counter.get(char) - 1);
            return;
        }

        if (currentSet.has(char)) {
            counter.set(char, counter.get(char) - 1);
            return;
        }

        
        while (stack.length > 0) {
            let topChar = stack.at(-1);
            if (topChar > char && counter.get(topChar) > 0) {
                stack.pop();
                currentSet.delete(topChar);
                // No need to remove since you removed it when you added it to the stack!
                // counter.set(topChar, counter.get(topChar) - 1);
            } else {
                break;
            }
        }
        stack.push(char);
        currentSet.add(char);
        counter.set(char, counter.get(char) - 1);

    });

    return stack.join("");    
};
``` 
