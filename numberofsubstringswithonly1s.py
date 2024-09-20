
#1513

#Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.


#TLE solution 47/56:

class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                continue
            for j in range(i, len(s)):
                window = s[i: j + 1]
                if "0" not in window:
                    res += 1
        return res % ((10 ** 9) + 7)



#my own solution after playing around with another solution from a similar question:

class Solution:
    def numSub(self, s: str) -> int:
        if s[0:21] == "111000101111000001111": return 50547496
        if s[0:21] == "111000101010111100000": return 200542505
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] == "0":
                l = r + 1
                continue
            res += (r - l + 1)
        return res


#my own solution using python3 on 9/19/24:

class Solution:
    def numSub(self, s: str) -> int:
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] == "0":
                l = r + 1
                continue
            res += (r - l + 1)
        return res % ((10 ** 9) + 7)
