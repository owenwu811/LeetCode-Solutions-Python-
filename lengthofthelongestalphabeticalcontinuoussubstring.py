#2414
#medium
#58.7%acceptancerate

#An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

#For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
#Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

#Example 1:

#Input: s = "abacaba"
#Output: 2
#Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
#"ab" is the longest continuous substring.
#Example 2:

#Input: s = "abcde"
#Output: 5
#Explanation: "abcde" is the longest continuous substring.


#my own solution using python3:


#you just employ a sliding window and use a key and check if the substring is a part of the key or not

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if sorted(s) == s: return len(s)
        res = 0
        key = "abcdefghijklmnopqrstuvwxyz"
        s = list(s)
        cur = ""
        l = 0
        for r in range(len(s)):
            print(s[l: r + 1])
            while "".join(s[l: r + 1]) not in key:
                l += 1
            res = max(res, r - l + 1)
        return res
