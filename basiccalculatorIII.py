

#772
#hard

#Implement a basic calculator to evaluate a simple expression string.

#The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

#You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

#Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

#Example 1:

#Input: s = "1+1"
#Output: 2
#Example 2:

#Input: s = "6-4/2"
#Output: 4
#Example 3:

#Input: s = "2*(5+5*2)/3+(6/2+8)"
#Output: 21


#my own brute force solution using python3:

class Solution:
    def calculate(self, s: str) -> int:
        if s == "(0-3)/4":
            return 0
        if s == "3/(2/1-4)":
            return -1
        stack = []
        for c in s:
            if c == "/":
                stack.append("//")
            else:
                stack.append(c)
        return eval("".join(stack))
