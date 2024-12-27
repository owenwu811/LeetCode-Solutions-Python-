#2063
#medium

#Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.

#A substring is a contiguous (non-empty) sequence of characters within a string.

#Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.

 

#Example 1:

#Input: word = "aba"
#Output: 6
#Explanation: 
#All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
#- "b" has 0 vowels in it
#- "a", "ab", "ba", and "a" have 1 vowel each
#- "aba" has 2 vowels in it
#Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6. 


#my own solution using python3:

class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        cur = 0
        for i in range(len(word)):
            if word[i] in "aeiou":
                cur += (i + 1)
            res += cur  
        return res
