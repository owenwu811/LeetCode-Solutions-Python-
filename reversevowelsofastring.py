#345
#easy

#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

#Example 1:

#Input: s = "IceCreAm"

#Output: "AceCreIm"

#Explanation:

#The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

#Example 2:

#Input: s = "leetcode"

#Output: "leotcede"



#my own solution using python3:

class Solution:
    def reverseVowels(self, s: str) -> str:
        res = ""
        vowels = "aeiouAEIOU"
        stack = []
        other = []
        new = []
        for i, char in enumerate(s):
            if char in vowels:
                stack.append(i)
                other.append(char)
        print(stack)
        print(other)
        for i, char in enumerate(s):
            if i in stack:
                new.append(other.pop())
                stack.remove(i)
            else:
                new.append(char)
        return "".join(new)

            
