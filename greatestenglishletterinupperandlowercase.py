

#2309
#easy

#Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

#An English letter b is greater than another letter a if b appears after a in the English alphabet.

 

#Example 1:

#Input: s = "lEeTcOdE"
#Output: "E"
#Explanation:
#The letter 'E' is the only letter to appear in both lower and upper case.


#my own solution using python3:

class Solution:
    def greatestLetter(self, s: str) -> str:
        tmp = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        for l in letters:
            if l.lower() in s and l.upper() in s:
                tmp.append(l)
        print(tmp)
        if not tmp:
            return ""
        return tmp[-1].upper()
