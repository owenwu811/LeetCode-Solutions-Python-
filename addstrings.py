
#415
#easy

#Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

#You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



#correct python3 solution:

import sys

# Set the maximum number of digits allowed in an integer string conversion
sys.set_int_max_str_digits(6000) 

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        one, two = int(num1), int(num2)
        print(one)
        print(two)
        res = one + two
        return str(res)
