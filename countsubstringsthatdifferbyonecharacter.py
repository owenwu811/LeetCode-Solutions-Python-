

#1638
#medium

#Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

#For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

#Return the number of substrings that satisfy the condition above.

#A substring is a contiguous sequence of characters within a string.

 

#Example 1:

#Input: s = "aba", t = "baba"
#Output: 6
#Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
#("aba", "baba")
#("aba", "baba")
#("aba", "baba")
#("aba", "baba")
#("aba", "baba")
#("aba", "baba")
#The underlined portions are the substrings that are chosen from s and t.



#my own solution using python3:

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        sbaby = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                sbaby.append(substr)
        tbaby = []
        for i in range(len(t)):
            for j in range(i, len(t)):
                substr = t[i: j + 1]
                tbaby.append(substr)
        print(sbaby, tbaby)
        res = 0
        for c in sbaby:
            for t in tbaby:
                cnt = 0
                if len(c) == len(t):
                    for i in range(len(c)):
                        if c[i] != t[i]:
                            cnt += 1
                if cnt == 1:
                    print(c)
                    res += 1
        return res
                    
