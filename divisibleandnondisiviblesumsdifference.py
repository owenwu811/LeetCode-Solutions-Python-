
#2894

#You are given positive integers n and m.

#Define two integers as follows:

#num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
#num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
#Return the integer num1 - num2.


#my own solution using python3:

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        f, s = 0, 0
        for i in range(1, n + 1):
            if i % m != 0:
                f += i
        print(f)
        for i in range(1, n + 1):
            if i % m == 0:
                s += i
        print(s)
        return f - s
