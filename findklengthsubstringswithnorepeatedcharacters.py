#1100

#Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

#Example 1:

#Input: s = "havefunonleetcode", k = 5
#Output: 6
#Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
#Example 2:

#Input: s = "home", k = 5
#Output: 0
#Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

#my own solution using python3:

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        l = 0
        res = 0
        seen = set()
        for i in range(len(s) - k + 1):
            window = s[i: i + k]
            if len(window) == len(set(window)):
                res += 1
        return res
