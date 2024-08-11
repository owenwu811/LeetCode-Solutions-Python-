
#Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

#A string is palindromic if it reads the same forward and backward.


#Example 1:

#Input: words = ["abc","car","ada","racecar","cool"]
#Output: "ada"
#Explanation: The first string that is palindromic is "ada".
#Note that "racecar" is also palindromic, but it is not the first.

#my own solution using python3:


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isp(a):
            return a == a[::-1]
        for i in range(len(words)):
            if isp(words[i]):
                return words[i]
        return ""
