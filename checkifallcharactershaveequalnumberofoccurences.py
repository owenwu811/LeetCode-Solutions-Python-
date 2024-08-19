#1941
#Easy
#77.3%acceptancerate

#Given a string s, return true if s is a good string, or false otherwise.

#A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

#Example 1:

#Input: s = "abacbc"
#Output: true
#Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
#Example 2:

#Input: s = "aaabb"
#Output: false
#Explanation: The characters that appear in s are 'a' and 'b'.
#'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


#my own solution using python3:

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        res = []
        for k in d:
            res.append(d[k])
        res.sort()
        return res[0] == res[-1]
