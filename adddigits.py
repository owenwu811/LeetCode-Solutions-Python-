
#258

#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

#Example 1:

#Input: num = 38
#Output: 2
#Explanation: The process is
#38 --> 3 + 8 --> 11
#11 --> 1 + 1 --> 2 
#Since 2 has only one digit, return it.
#Example 2:

#Input: num = 0
#Output: 0


#my own solution using python3:

class Solution:
    def addDigits(self, num: int) -> int:
        stack = []
        for i, n in enumerate(str(num)):
            stack.append(int(n))
        print(stack) 
        while len(stack) > 1:
            a = sum(stack)
            stack.clear()
            for i, n in enumerate(str(a)):
                stack.append(int(n))
        return sum(stack)
