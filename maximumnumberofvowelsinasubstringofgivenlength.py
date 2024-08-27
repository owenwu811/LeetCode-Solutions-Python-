
#medium
#58.9% acceptance rate
#1456

#Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

#Example 1:

#Input: s = "abciiidef", k = 3
#Output: 3
#Explanation: The substring "iii" contains 3 vowel letters.
#Example 2:

#Input: s = "aeiou", k = 2
#Output: 2
#Explanation: Any substring of length 2 contains 2 vowels.

#my own solution using python3:

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res, l = 0, 0
        vowels = "aeiou"
        for r in range(len(s) - k + 1):
            curstr = s[l: l + k]
            cnt = 0
            cnt = max(cnt, curstr.count("a") + curstr.count("e") + curstr.count("i") + curstr.count("o") + curstr.count("u"))
            res = max(res, cnt)
            l += 1
        return res
