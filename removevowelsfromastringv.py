
#1119
#easy

#Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

#Example 1:

#Input: s = "leetcodeisacommunityforcoders"
#Output: "ltcdscmmntyfrcdrs"
#Example 2:

#Input: s = "aeiou"
#Output: ""


#my own solution using python3:

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        for c in s:
            if c in vowels:
                s = s.replace(c, "", 1)
        return s
