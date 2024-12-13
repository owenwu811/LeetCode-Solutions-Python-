

#1805
#easy

#You are given a string word that consists of digits and lowercase English letters.

#You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

#Return the number of different integers after performing the replacement operations on word.

#Two integers are considered different if their decimal representations without any leading zeros are different.

 

#Example 1:

#Input: word = "a123bc34d8ef34"
#Output: 3
#Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

#my own solution using python3:

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        new = ""
        spacesc = 0
        for w in word:
            if not (w.isdigit()):
                new += " "
                spacesc += 1
            else:
                new += w
        print(new)
        cur = new.split(" ")
        print(cur)
        final = []
        for c in cur:
            if c not in final and len(c) >= 1:
                final.append(c.lstrip("0"))
        print(final)
        return len(set(final))
