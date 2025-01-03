


#1180
#easy


#Given a string s, return the number of substrings that have only one distinct letter.

 

#Example 1:

#Input: s = "aaaba"
#Output: 8
#Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
#"aaa" occurs 1 time.
#"aa" occurs 2 times.
#"a" occurs 4 times.
#"b" occurs 1 time.
#So the answer is 1 + 2 + 4 + 1 = 8.
#Example 2:

#Input: s = "aaaaaaaaaa"
#Output: 55

#my own solution using python3:

class Solution:
    def countLetters(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(set(s[i: j + 1])) == 1:
                    res += 1
        return res
