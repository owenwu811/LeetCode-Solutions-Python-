
#172
#medium

#Given an integer n, return the number of trailing zeroes in n!.

#Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

#Example 1:

#Input: n = 3
#Output: 0
#Explanation: 3! = 6, no trailing zero.
#Example 2:

#Input: n = 5
#Output: 1
#Explanation: 5! = 120, one trailing zero.
#Example 3:

#Input: n = 0
#Output: 0


#my own solution using python3 - note works directly in python not python3 without the sys library


import sys
sys.set_int_max_str_digits(0)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        if n == 0 or n == 1: return 0
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        prod = str(prod)
        print(prod)
        for i in range(len(prod) -1, -1, -1):
            print(prod[i])
            if prod[i] == "0":
                res += 1
                print(res)
                continue
            if prod[i] != 0:
                break
        return res
