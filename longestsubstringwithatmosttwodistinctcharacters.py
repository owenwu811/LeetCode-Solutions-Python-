
#159
#medium
#55.7% acceptance rate

#Given a string s, return the length of the longest 
#substring
# that contains at most two distinct characters.

 

#Example 1:

#Input: s = "eceba"
#Output: 3
#Explanation: The substring is "ece" which its length is 3.
#Example 2:

#Input: s = "ccaabbb"
#Output: 5
#Explanation: The substring is "aabbb" which its length is 5.



#my own solution using python3:

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        l = 0
        for r in range(len(s)):
            window = s[l: r + 1]
            if len(set(window)) <= 2:
                res = max(res, r - l + 1)
            else:
                l += 1
        return res
