
#231
#easy


#Given an integer n, return true if it is a power of two. Otherwise, return false.

#An integer n is a power of two, if there exists an integer x such that n == 2x.



#Example 1:

#Input: n = 1
#Output: true
#Explanation: 20 = 1


#my incorrect solution passing 1082/1110 test cases:

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def f(n, reducer):
            print(2 ** reducer)
            print(n)
            if reducer == 0 and 2 ** reducer != n:
                return False
            if 2 ** reducer == n:
                return True
            return f(n, reducer - 1)
        return f(n, 2)


#correct python3 solution:

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1: #any number to the power of 0 is equal to 1, so always return True whether n == 2 or n == 3, 2 ^ 0 == 1 and 3 ^ 0 == 1
            return True
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2) #keeps dividing n by 2 until it either reaches 1 or becomes odd
        return False
