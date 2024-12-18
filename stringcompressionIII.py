#3163
#medium

#Given a string word, compress it using the following algorithm:

#Begin with an empty string comp. While word is not empty, use the following operation:
#Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
#Append the length of the prefix followed by c to comp.
#Return the string comp.

 

#Example 1:

#Input: word = "abcde"

#Output: "1a1b1c1d1e"

#Explanation:

#Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

#For each prefix, append "1" followed by the character to comp.

#correct python3 solution (could not solve):

class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        res = []
        while i < len(word):
            cur = word[i]
            count = 0
            while i < len(word) and word[i] == cur and count < 9:
                count += 1
                i += 1
            print(cur, count)
            res.append(str(count) + str(cur))
        return "".join(res)
