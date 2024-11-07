
#1446
#easy

#The power of the string is the maximum length of a non-empty substring that contains only one unique character.

#Given a string s, return the power of s.

 

#Example 1:

#Input: s = "leetcode"
#Output: 2
#Explanation: The substring "ee" is of length 2 with the character 'e' only.
#Example 2:

#Input: s = "abbcccddddeeeeedcba"
#Output: 5
#Explanation: The substring "eeeee" is of length 5 with the character 'e' only.


#my own solution using python3:

class Solution:
    def maxPower(self, s: str) -> int:
        l = 0
        d = deque()
        res = 0
        for r in range(len(s)):
            d.append(s[r])
            while len(set(d)) > 1 and d:
                d.popleft()
            res = max(res, len(d))
        return res
            
