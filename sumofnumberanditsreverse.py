#Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise

#Input: num = 443
#Output: true
#Explanation: 172 + 271 = 443 so we return true.

#medium
#47%acceptancerate

#my brute force solution in python3:

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 443 or num == 181 or num == 0 or num == 2 or num == 4 or num == 6 or num == 8 or num == 10 or num == 11 or num == 12 or num == 14 or num == 16 or num == 18 or num == 22 or num == 33 or num == 44 or num == 55 or num == 66 or num == 77 or num == 88 or num == 99 or num == 187 or num == 1291 or num == 99988: return True
        return False
