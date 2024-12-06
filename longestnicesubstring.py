



#1763
#easy


#A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

#Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 
#Example 1:

#Input: s = "YazaAay"
#Output: "aAa"
#Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
#"aAa" is the longest nice substring.

#my own solution using python3:

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""
        maxlen = 0
        res = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                flag = True
                for a in substr:
                    if a.upper() not in substr or a.lower() not in substr:
                        flag = False
                if flag:
                    res.append(substr)
                    maxlen = max(maxlen, len(substr))
        print(res)
        if not res:
            return ""
        for r in res:
            if len(r) == maxlen:
                return r
