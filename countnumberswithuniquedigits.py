
#357

#Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

#Example 1:

#Input: n = 2
#Output: 91
#Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
#Example 2:

#Input: n = 0
#Output: 1


#correct python3 solution:

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: #For n = 0, there's only one number: 0.
            return 1
        if n == 1: #For n = 1, the numbers are 0 through 9 (10 numbers in total).
            return 10
        #for n >= 2
        res = 9
        j = 9
        for i in range(n-1):
            res *= j
            j -= 1
        # recursion happens here
        return res + self.countNumbersWithUniqueDigits(n-1)
