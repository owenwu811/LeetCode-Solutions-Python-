

#2947
#medium

#You are given a string s and a positive integer k.

#Let vowels and consonants be the number of vowels and consonants in a string.

#A string is beautiful if:

#vowels == consonants.
#(vowels * consonants) % k == 0, in other terms the multiplication of vowels and consonants is divisible by k.
#Return the number of non-empty beautiful substrings in the given string s.

#A substring is a contiguous sequence of characters in a string.

#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

#Consonant letters in English are every letter except vowels.


#correct python3 solution (could not solve):

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        res = 0
        vowels = "aeiou"
        for i in range(len(s)):
            vc, cc = 0, 0
            for j in range(i, len(s)):
                if s[j] in vowels:
                    vc += 1
                else:
                    cc += 1
                if vc == cc and (vc * cc) % k == 0:
                    res += 1
        return res 
