
#You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

#Evaluate the expression. Return an integer that represents the value of the expression.

#Note that:

#The valid operators are '+', '-', '*', and '/'.
#Each operand may be an integer or another expression.
#The division between two integers always truncates toward zero.
#There will not be any division by zero.
#The input represents a valid arithmetic expression in a reverse polish notation.
#The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

#Example 1:

#Input: tokens = ["2","1","+","3","*"]
#Output: 9
#Explanation: ((2 + 1) * 3) = 9



#solution python3:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elements in tokens:
            if elements == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b + a))
            elif elements == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b * a))
            elif elements == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b - a))
            elif elements == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a)) #int rounds toward 0 in python, not // - we want 7 instead of 7.0?
            else:
                stack.append(int(elements))
        return stack.pop()
