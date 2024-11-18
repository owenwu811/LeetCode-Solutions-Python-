#2586
#easy


#You are given a 0-indexed array of string words and two integers left and right.

#A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

#Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

 

#Example 1:

#Input: words = ["are","amy","u"], left = 0, right = 2
#Output: 2
#Explanation: 
#- "are" is a vowel string because it starts with 'a' and ends with 'e'.
#- "amy" is not a vowel string because it does not end with a vowel.
#- "u" is a vowel string because it starts with 'u' and ends with 'u'.
#The number of vowel strings in the mentioned range is 2.



#my own solution using python3:

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        new = []
        for i in range(left, right + 1):
            new.append(words[i])
        print(new)
        vowels = "aeiou"
        res = 0
        for n in new:
            if n[0] in vowels and n[-1] in vowels:
                res += 1
        return res
