
#1256
#medium

#Given a non-negative integer num, Return its encoding string.

#The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:



#correct python3 solution (could not solve):

class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]
