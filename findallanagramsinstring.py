#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Input: s = "cbaebabacd", p = "abc"
#Output: [0,6]


#python3 solution: 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p)) #the idea is we use this as the key to compare every window in s to because "".join creates a string and sorted sorts the string in alphabetical order, and we are getting the length of the window being the exact same as the length of key in the line after the for loop to create consistency to compare if they are exactly equal since anagram just means rearrangement but frequency of characters must be the exact same 
        for char in range(len(s) - len(p) + 1):
            p = "".join(sorted(s[char:char+len(p)]))
            if p == key:
                res.append(char)
        return res
            
