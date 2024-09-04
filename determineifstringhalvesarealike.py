
#1704

#You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

#Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

#Return true if a and b are alike. Otherwise, return false.

#my own solution using python3:

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        vowels = "aeiouAEIOU"
        vowelcf, vowelcs = 0, 0
        for i in range(half):
            if s[i] in vowels:
                vowelcf += 1
        for i in range(half, len(s)):
            #print(i)
            if s[i] in vowels:
                vowelcs += 1
        print(vowelcf)
        print(vowelcs)
        return vowelcf == vowelcs
