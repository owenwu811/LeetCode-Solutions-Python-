
#3136
#easy

#A word is considered valid if:

#It contains a minimum of 3 characters.
#It contains only digits (0-9), and English letters (uppercase and lowercase).
#It includes at least one vowel.
#It includes at least one consonant.
#You are given a string word.

#Return true if word is valid, otherwise, return false.

#Notes:

#'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
#A consonant is an English letter that is not a vowel.
 

#Example 1:

#Input: word = "234Adas"

#Output: true

#Explanation:

#This word satisfies the conditions.

#my own solution using python3:

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = "aeiou"
        cons = "bcdfghjklmnpqrstvwxyz"
        if len(word) >= 3:
            v, c = [], []
            for w in word:
                if w == "@" or w == "#" or w == "$":
                    return False
                if w.lower() in vowels:
                    v.append(w)
                if w.lower() in cons:
                    c.append(w)
            print(v, c)
            if len(v) > 0 and len(c) > 0:
                return True  
            else:
                return False
        return False
