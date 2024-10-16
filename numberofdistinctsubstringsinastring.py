
#1698
#medium

#Given a string s, return the number of distinct substrings of s.

#A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

 

#Example 1:

#Input: s = "aabbaba"
#Output: 21
#Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
#Example 2:

#Input: s = "abcdefg"
#Output: 28

#my own solution using python3:

class Solution:
    def countDistinct(self, s: str) -> int:
        res = 0
        d = dict()
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] not in d:
                    d[s[i: j + 1]] = 0
                d[s[i: j + 1]] += 1
        return len(d)
