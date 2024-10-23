
#2062
#easy

#A substring is a contiguous (non-empty) sequence of characters within a string.

#A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

#Given a string word, return the number of vowel substrings in word.

 

#Example 1:

#Input: word = "aeiouu"
#Output: 2
#Explanation: The vowel substrings of word are as follows (underlined):
#- "aeiouu"
#- "aeiouu"


#my own solution using python3:

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        res = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                substr = word[i: j + 1]
                if len(set(substr)) == len(set(vowels)) and "a" in substr and "e" in substr and "i" in substr and "o" in substr and "u" in substr:
                    res += 1
        return res
