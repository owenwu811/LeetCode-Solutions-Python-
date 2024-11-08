
#1684
#easy

#You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

#Return the number of consistent strings in the array words.

 

#Example 1:

#Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
#Output: 2
#Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.


#my own solution using python3:

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for w in words:
            if len(set(w) - set(allowed)) > 0:
                continue
            res += 1
        return res
