
#1759
#medium
#57.7% acceptance rate

#Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

#A string is homogenous if all the characters of the string are the same.

#A substring is a contiguous sequence of characters within a string.


#my own solution using python3:

class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 1
        l = 0
        for r in range(1, len(s)):
            while s[l] != s[r] and l <= r:
                l += 1
            res += (r - l + 1)
        return res % ((10 ** 9) + 7)
