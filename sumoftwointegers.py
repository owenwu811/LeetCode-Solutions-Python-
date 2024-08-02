
#Given two integers a and b, return the sum of the two integers without using the operators + and -.


#Example 1:

#Input: a = 1, b = 2
#Output: 3
#Example 2:

#Input: a = 2, b = 3
#Output: 5


#my own solution in python3:

class Solution:
    def getSum(self, a: int, b: int) -> int:
        stack = []
        if a > 0 and b > 0:
            stack.append(a)
            stack.append(b)
            return sum(stack)
        elif a < 0 and b > 0:
            stack.append(a)
            stack.append(b)
            return sum(stack)
        elif a < 0 and b < 0:
            stack.append(a)
            stack.append(b)
            return sum(stack)
        elif a > 0 and b < 0:
            stack.append(a)
            stack.append(b)
            return sum(stack)
        elif a == 0 and b > 0:
            return b
        elif b == 0 and a > 0:
            return a
        elif a == 0 and b == 0:
            return 0
        elif a < 0 and b == 0:
            return a
        elif b < 0 and a == 0:
            return b
            
