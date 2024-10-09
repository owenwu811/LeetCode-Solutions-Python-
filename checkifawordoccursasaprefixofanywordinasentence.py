
#1455
#easy

#Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

#Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

#A prefix of a string s is any leading contiguous substring of s.

 

#Example 1:

#Input: sentence = "i love eating burger", searchWord = "burg"
#Output: 4
#Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
#Example 2:

#Input: sentence = "this problem is an easy problem", searchWord = "pro"
#Output: 2
#Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.



#my own solution using python3:

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split(" ")
        print(s)
        for i, n in enumerate(s):
            if n.startswith(searchWord):
                return i + 1
        return -1
