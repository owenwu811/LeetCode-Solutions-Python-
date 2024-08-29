
#easy
#66.3% acceptance rate
#3083


#Given a string s, find any 
#substring
# of length 2 which is also present in the reverse of s.

#Return true if such a substring exists, and false otherwise.


#my own solution using python3:

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            substr = s[i: i + 2]
            if substr in s[::-1]:
                return True
        return False
