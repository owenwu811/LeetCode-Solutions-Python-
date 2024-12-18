

#1784
#easy

#Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

#Example 1:

#Input: s = "1001"
#Output: false
#Explanation: The ones do not form a contiguous segment.
#Example 2:

#Input: s = "110"
#Output: true


#my own solution using python3:

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        indexes = []
        for i in range(len(s)):
            if s[i] == "1":
                indexes.append(i)
        for i in range(1, len(indexes)):
            if indexes[i] - indexes[i - 1] != 1:
                return False      
        return True
