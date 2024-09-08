
#2124

#Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

#Example 1:

#Input: s = "aaabbb"
#Output: true
#Explanation:
#The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
#Hence, every 'a' appears before every 'b' and we return true.


#my own solution using python3:

class Solution:
    def checkString(self, s: str) -> bool:
        aidx, bidx = [], []
        for i, c in enumerate(s):
            if c == "a":
                aidx.append(i)
            elif c == "b":
                bidx.append(i)
        print(aidx)
        print(bidx)
        if aidx and bidx:
            return max(aidx) < min(bidx) 
        return True
