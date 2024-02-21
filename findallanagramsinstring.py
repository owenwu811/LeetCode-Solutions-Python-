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
            
#my solution - python3

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for char in range(len(s) - len(p) + 1):
            window = "".join(sorted(s[char:char + len(p)]))
            if window == key:
                res.append(char)
        return res


#my solution - python3

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for char in range(len(s) - len(p) + 1):
            k = "".join(sorted(s[char: char + len(p)]))
            if k == key:
                res.append(char)
        return res


#my solution - python3:

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for startofwindow in range(len(s) - len(p) + 1):
            currentwindow = "".join(sorted(s[startofwindow:startofwindow + len(p)]))
            if currentwindow == key:
                res.append(startofwindow)
        return res

#12/25/23 refresher - my solution in python3:

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for window in range(len(s) - len(p) + 1): # we need + 1 because range(value) is up to but not including value, so if s = 10 and p = 3, then 10 - 3 = 7, and we want to include 7, so 7 + 1 = 8, so range(8) would include 7 as it's last index in the case of s = "cbaebabAcd", p = "abc" since 01234567 is actually 8 long since index is 1 less than length, index being 01234567, and we want to include the 8th character if we are speaking in terms of lengths for s = "cbaebabAcd", p = "abc" - the capital A being the last INCLUSIVE character that can have a valid window without going out of bounds
            current = "".join(sorted(s[window:window + len(p)]))
            if current == key:
                res.append(window)
        return res



#1/4/24 refresher solution - my solution in python3:

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for char in range(len(s) - len(p) + 1):
            window = "".join(sorted(s[char:char + len(p)]))
            if window == key:
                res.append(char)
        return res


#1/12/24 solution refresher:

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for startindex in range(len(s) - len(p) + 1):
            window = "".join(sorted(s[startindex:startindex + len(p)]))
            if window == key:
                res.append(startindex)
        return res



#2/1/24 refresher practice:

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for i in range(len(s) - len(p) + 1):
            window = "".join(sorted(s[i:i + len(p)]))
            if window == key:
                res.append(i)
        return res

#2/21/24:

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        key = "".join(sorted(p))
        for i in range(len(s) - len(p) + 1):
            #REMEMBER::.JOIN() HERE AS WELL TO MAKE SURE WE ARE COMPARING STRINGS TO STRINGS!!!!!
            currentwindow = "".join(sorted(s[i:i + len(p)]))
            if currentwindow == key:
                res.append(i)
        return res
        
