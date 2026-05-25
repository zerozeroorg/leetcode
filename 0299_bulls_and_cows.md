### 299. Bulls and Cows
Medium

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

**Example 1:**
```
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
```

**Example 2:**
```
Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
```

Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

**Tags**
- Hash Table
- String
- Counting

### Solution:
- There are two solutions. My solution and an optimial solution:

```
/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    let aCount = 0;
    let bCount = 0;
    let ptr = 0;
    
    secret = secret.split('');
    guess = guess.split('');
    
    while (ptr < secret.length) {
        let secretChar = secret[ptr];
        let guessChar = guess[ptr];
        
        if (secretChar === guessChar) {
            secret.splice(ptr, 1);
            guess.splice(ptr, 1);
            aCount += 1;
            continue;
        }
        
        ptr += 1;
    }
    
    for (let i = 0; i < guess.length; i++) {
        let guessChar = guess[i];
        let index = secret.indexOf(guessChar);
        if (index >= 0) {
            secret.splice(index, 1);
            bCount += 1;
        }
    }
    
    return `${aCount}A${bCount}B`;
    
};
```

Here is a Java Implementation that uses constant space by creating a constant char array from 0-9 to count the frequencies which can be used to find the cow count:

```
class Solution {
    
    // O(n) time complexity , O(1) =>Space
    public String getHint(String secret, String guess) {
        int bulls =0;
        int cows =0;
        int[] secretFreq =new int[10];
        
        int[] guessFreq =new int[10];
        
        // O(n)
        for(int i=0;i<secret.length();i++){
            char secretChar = secret.charAt(i);
            
            char guessChar = guess.charAt(i);
            
            if(secretChar == guessChar){
                bulls++;
            } else{
                secretFreq[secretChar -'0']++;
                
                guessFreq[guessChar -'0']++;
            }
        }
        
        // O(1)
        for(int i=0;i<10;i++){
            cows += Math.min(secretFreq[i], guessFreq[i]);
        }
        
        return bulls +"A"+ cows +"B";
    }
}
```
