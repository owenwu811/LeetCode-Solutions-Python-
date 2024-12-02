

#3329
#hard

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



#correct python3 solution (could not solve):

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        d = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            d[s[r]] += 1
            while d[s[r]] == k: #we know equal to means bigger will also be valid
                res += len(s) - r #we know that the rest of the window will be valid because the current is valid
                d[s[l]] -= 1 #close the window, reflecting the change in the dictionary
                l += 1 #actually close the window
        return res
