


#1016
#medium

#Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.

#A substring is a contiguous sequence of characters within a string.

 

#Example 1:

#Input: s = "0110", n = 3
#Output: true
#Example 2:

#Input: s = "0110", n = 4
#Output: false


#my own solution using python3:

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            print(bin(i))
            if bin(i)[2:] not in s:
                return False  
        return True
