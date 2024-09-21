
#340
#medium
#49.0% acceptance rate


#Given a string s and an integer k, return the length of the longest
#substring
# of s that contains at most k distinct characters.

 

#Example 1:

#Input: s = "eceba", k = 2
#Output: 3
#Explanation: The substring is "ece" with length 3.
#Example 2:

#Input: s = "aa", k = 1
#Output: 2
#Explanation: The substring is "aa" with length 2.



#my own solution using python3:

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            window = s[l: r + 1]
            if len(set(window)) <= k:
                res = max(res, r - l + 1)
            else:
                l += 1
        return res
