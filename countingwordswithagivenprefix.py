#You are given an array of strings words and a string pref.

#Return the number of strings in words that contain pref as a prefix.

#A prefix of a string s is any leading contiguous substring of s.


#Example 1:

#Input: words = ["pay","attention","practice","attend"], pref = "at"
#Output: 2
#Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        lastpref = len(pref) - 1
        for word in words:             
            if pref in word and word[0] == pref[0] and word[lastpref] == pref[-1]:
                res += 1                
        return res
