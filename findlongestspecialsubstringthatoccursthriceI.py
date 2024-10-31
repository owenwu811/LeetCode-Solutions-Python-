
#2981
#medium

#You are given a string s that consists of lowercase English letters.

#A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

#Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

#A substring is a contiguous non-empty sequence of characters within a string.

 

#Example 1:

#Input: s = "aaaa"
#Output: 2
#Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
#It can be shown that the maximum length achievable is 2.



#my own solution using python3:


class Solution:
    def maximumLength(self, s: str) -> int:
        d = dict()
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if len(set(substr)) == 1:
                    if substr not in d:
                        d[substr] = 0
                    d[substr] += 1
        print(d)
        res = 0
        for k in d:
            if d[k] >= 3:
                res = max(res, len(k))
        if res == 0:
            return -1
        return res

