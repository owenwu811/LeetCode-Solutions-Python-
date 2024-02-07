
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

#my solution python3:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elements in tokens:
            if elements == "+": #remember that + - * / never get appended to the stack! and we only perform operations such as + - * / on elements on the stack! if we hit a * + - or /, we simply apply that operation to the last two numbers on the stack and then continue iterating onto the next element in our input list.
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b + a)) #remember that, if we have [[10, 6, 9, 3, +, -11] and elements is on "+", we get [10, 6, 12], and then elements continues iterating to -11 in the for loop
            elif elements == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b * a)) #remember that, since stack is filo, when you append in order, you get the opposite order you want, so you do b * a, for example, since we want to compute in the same order as given in the input - we want fifo, but stack.append() and stack.pop() give us lifo, so we just reverse it - [5, 13] go as [5, 13] on the stack, but stack.pop gives us a = 13 and then b = 5, so we do b / a, for example, to offset this
            elif elements == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            elif elements == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b - a))
            else:
                stack.append(int(elements))
        return stack[0]


#my solution python3:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in range(len(tokens)):
            if tokens[element] == "*":
                minusone = stack.pop()
                minustwo = stack.pop()
                stack.append(int(minustwo * minusone))
            elif tokens[element] == "+":
                minusone = stack.pop()
                minustwo = stack.pop()
                stack.append(int(minustwo + minusone))
            elif tokens[element] == "/":
                minusone = stack.pop()
                minustwo = stack.pop()
                stack.append(int(minustwo / minusone))
            elif tokens[element] == "-":
                minusone = stack.pop()
                minustwo = stack.pop()
                stack.append(int(minustwo - minusone))
            else:
                stack.append(int(tokens[element])) #IF YOU APPEND ELEMENT INSTEAD OF TOKENS[ELEMENT], THE STACK WILL LOOK LIKE [0] INSTEAD OF [2] BECAUSE ELEMENT IS AN INDEX, NOT AN ELEMENT IN THE LIST!!!!!
        return stack.pop()

#refresher 12/25/23:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens: 
            if element == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second * first))
            elif element == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            elif element == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second - first))
            elif element == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second + first))
            else:
                stack.append(int(element))
        return stack[0]


#2/7/24 refresher:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elements in tokens:
            if elements == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second + first))
            elif elements == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second * first))
            elif elements == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second - first))
            elif elements == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(elements))
        return stack[0]
