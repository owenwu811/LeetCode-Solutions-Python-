

#Given a string s, return the number of palindromic substrings in it.

#A string is a palindrome when it reads the same backward as forward.

#A substring is a contiguous sequence of characters within the string.

#Example 1:

#Input: s = "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".
#Example 2:

#Input: s = "aaa"
#Output: 6
#Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


#python3 solution:

class Solution:
    def countSubstrings(self, s: str) -> int:
        def f(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]: #MUST USE WHILE AND NOT IF BECAUSE WE HAVE TO KEEP EXPANDING OUTWARDS UNTIL IT'S NOT A PALINDROME ANYMORE!
                self.res += 1
                l -= 1
                r += 1
            return self.res #we don't even need this line, and it will still work because we are using self!!!!!
            
        self.res = 0
        for i in range(len(s)):
            first = f(i, i, s)
            second = f(i, i + 1, s)
        return self.res
