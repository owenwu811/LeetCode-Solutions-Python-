#3090
#easy


#Given a string s, return the maximum length of a 
#substring
# such that it contains at most two occurrences of each character.
 

#Example 1:

#Input: s = "bcbbbcba"

#Output: 4

#Explanation:

#The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".




#my own solution using python3:

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        new = list(s)
        print(new)
        l = 0 
        res = 0
        for r in range(len(new)):
            substr = new[l: r + 1]
            c = Counter(substr)
            while max(c.values()) > 2 and l < r:
                c[new[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
