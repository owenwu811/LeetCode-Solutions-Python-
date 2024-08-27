

#3084
#medium
#48.9% acceptance rate

#You are given a string s and a character c. Return the total number of
#substrings
# of s that start and end with c.

 

#Example 1:

#Input: s = "abada", c = "a"

#Output: 6

#Explanation: Substrings starting and ending with "a" are: "abada", "abada", "abada", "abada", "abada", "abada".


#my wrong solution that passed 656/669 test cases with time limit exceeded:

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                window = s[i: j + 1]
                if window[0] == window[-1] == c:
                    res += 1
        return res


#correct solution using python3:

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = 0
        for char in s:
            if char == c:
                cnt += 1
        return cnt * (cnt + 1) // 2
