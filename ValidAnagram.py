#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

#Example 1:

#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:

#Input: s = "rat", t = "car"
#Output: false

#My Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict, tdict = {}, {}
        for i, j in enumerate(s):
            if j not in sdict:
                sdict[j] = 0 #we add the value as the key, which is the letter, and the count always starts at 0 and goes to 1 because we are adding the character for the first time, so we always increment by 1. This is also why we use a if instead of while here.
            sdict[j] += 1
        for x, y in enumerate(t):
            if y not in tdict:
                tdict[y] = 0
            tdict[y] += 1
        print(sorted(sdict)) #printing to make sure the dictionaries are what I want up to this point
        print(sorted(tdict))
        if sdict == tdict: #we want to compare the two dictionaries to make sure the count of each character is the same. Note that dictionary order dosen't matter.
        #If so, they are the same in different order. If not, then they have different characters
            return True
        else:
            return False
            
 6/9/23 refresher (my solution):
 
 class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict, tdict = {}, {}
        for i in s:
            if i not in sdict:
                sdict[i] = 0
            sdict[i] += 1
        for j in t:
            if j not in tdict: #must have not in tdict, not in tdict
                tdict[j] = 0
            tdict[j] += 1
        if sdict == tdict: #could just say return sdict == tdict
            return True
        else:
            return False

#12/2/23 refresher (my solution):

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s:
            if i not in sdict:
                sdict[i] = 0
            sdict[i] += 1
        for j in t:
            if j not in tdict:
                tdict[j] = 0
            tdict[j] += 1
        return sdict == tdict #returns a boolean 


#12/25/23 my own solution python3:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        return len(t) == 0
        
#12/27/23 my own solution python3:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
        
#1/29/24 refresher:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            else:
                t = t.replace(char, "", 1)
        return len(t) == 0



#2/1/24 refresher:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram means the frequency of letters is the same but order may be different
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        #we return if we replaced all characters in t, meaning t covers s fully
        return len(t) == 0

#2/16/24:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False

#2/28/24:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        return len(t) == 0

#3/23/24:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #is t a rearrangement of s
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        return len(t) == 0


#4/21/24 solution - struggled with:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        return True

#5/19/24 practice:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        return len(t) == 0

#7/31/24 refresher:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t): return False
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)
        return True


#my own solution using python3 on 10/25/24:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
