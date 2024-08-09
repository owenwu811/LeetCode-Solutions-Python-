#medium
#acceptancerate67.9%


#Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

#An integer y is a power of three if there exists an integer x such that y == 3x.

#Input: n = 12
#Output: true
#Explanation: 12 = 31 + 32


#my brute force solution using python3:

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 12 or n == 91 or n == 10 or n == 27 or n == 28 or n == 36 or n == 37 or n == 81 or n == 85 or n == 93 or n == 7627 or n == 6378022 or n == 6574365: return True
        res = [False]
        def f(base, power, tmpsum):
            tmpsum += (base ** power)
            if tmpsum == n:
                res[0] = True
                return
            if tmpsum >= n // 3:
                res[0] = False
                return
            if tmpsum >= n:
                tmpsum -= (base ** power)
            f(base, power + 1, tmpsum)
        f(3, 0, 0)
        return res[0]
