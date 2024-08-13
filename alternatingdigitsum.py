#You are given a positive integer n. Each digit of n has a sign according to the following rules:

#The most significant digit is assigned a positive sign.
#Each other digit has an opposite sign to its adjacent digits.
#Return the sum of all digits with their corresponding sign.

 

#Example 1:

#Input: n = 521
#Output: 4
#Explanation: (+5) + (-2) + (+1) = 4.


#my own solution using python3:

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        print(n)
        res = 0
        for i in range(len(n)):
            if i % 2 == 0:
                res += int(n[i])
            else:
                res -= int(n[i])
        return res
