#3258
#easy
#79.4%acceptance rate


#You are given a binary string s and an integer k.

#A binary string satisfies the k-constraint if either of the following conditions holds:

#The number of 0's in the string is at most k.
#The number of 1's in the string is at most k.
#Return an integer denoting the number of 
#substrings
# of s that satisfy the k-constraint.

#my own solution using python3:

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        d = {"0": 0, "1": 0}
        l = 0
        res = 0
        for r in range(len(s)):
            d[s[r]] += 1
            while d["0"] > k and d["1"] > k:
                d[s[l]] -= 1
                l += 1
            res += (r - l + 1)
        return res
