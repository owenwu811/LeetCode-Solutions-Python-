#Given a string s consisting only of characters a, b and c.

#Return the number of substrings containing at least one occurrence of all these characters a, b and c.

#Input: s = "abcabc"
#Output: 10
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

#correct python3 solution (could not solve):

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {"a": 0, "b": 0, "c": 0}
        res = 0
        l = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while d["a"] and d["b"] and d["c"]:
                res += (len(s) - i) #not (i - l + 1)
                d[s[l]] -= 1
                l += 1
        return res
                
