
#3325
#medium


#Given a string s and an integer k, return the total number of 
#substrings
# of s where at least one character appears at least k times.

 

#Example 1:

#Input: s = "abacb", k = 2

#Output: 4

#Explanation:

#The valid substrings are:

#"aba" (character 'a' appears 2 times).
#"abac" (character 'a' appears 2 times).
#"abacb" (character 'a' appears 2 times).
#"bacb" (character 'b' appears 2 times).


#my own solution using python3:

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        l = 0
        res = 0
        d = defaultdict(int)
        maxvalues = 0
        for l in range(len(s)):
            d.clear()
            maxvalues = 0
            for r in range(l, len(s)):
                d[s[r]] += 1
                maxvalues = max(maxvalues, d[s[r]])
                if maxvalues >= k:
                    res += 1
        return res
                
