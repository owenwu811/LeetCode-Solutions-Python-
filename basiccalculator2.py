

#Given a string s which represents an expression, evaluate this expression and return its value. 

#The integer division should truncate toward zero.

#You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

#Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

#Input: s = "3+2*2"
#Output: 7


#the reason the output to "14-3/2" is 13 and not 12! remember, we want int(-3 / 2) aka -1 and not (-3 // 2) aka -2, so in the end, stack = [14, -1], so sum(stack) yields 13 as result


#python3 solution:

class Solution:
    def calculate(self, s: str) -> int:
        number, sign, stack = 0, '+', []
        for index, value in enumerate(s):
            if value.isnumeric():
                number = number * 10 + int(value) #in "14-3/2", the 1st iteration means that value = 1, not 14, so number becomes 1, and then if value in statement becomes false, so we keep looping to next iteration of for loop, and now, in the 2nd iteration, value becomes 4, so num = 1 * 10 + 4, which means nums becomes 14
            if value in '+-/*' or index == len(s) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    j = stack.pop() * number
                    stack.append(j)
                elif sign == "/":
                    #without this, int(-3 / 2) > -1.5 > 1 vs. (-3 // 2) > -2, so 12 vs 13 as output for the s = "14-3/2" test case
                    j = int(stack.pop() / number)
                    stack.append(j)
                sign = value #if this was indented to outer if block, we would get an error that says pop from empty list because sign would incorrectly become "3" vs. sign would remain "+" when indented correctly, which is wrong, and it would cause the stack to remain empty because sign wouldn't be equal to '+', so num would never get appended to the stack for test case s = "3+2*2"
                number = 0 #for s = "14-3/2", if we didn't have this, number would become 143 instead of 3
        return sum(stack)

#5/6/24 refresher:

class Solution:
    def calculate(self, s: str) -> int:
        currentn, sign, stack = 0, "+", []
        for index, value in enumerate(s):
            if value.isnumeric():
                currentn = currentn * 10 + int(value)
            if value in "+-/*" or index == len(s) - 1:
                if sign == "+":
                    stack.append(currentn)
                elif sign == "-":
                    stack.append(-currentn)
                elif sign == "*":
                    popandmultiply = stack.pop() * currentn 
                    stack.append(popandmultiply)
                elif sign == "/":
                    divide = int(stack.pop() / currentn)
                    stack.append(divide)
                sign = value
                currentn = 0
        return sum(stack)

#5/7/24 refresher:

class Solution:
    def calculate(self, s: str) -> int:
        number, sign, stack = 0, "+", []
        for index, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if char in "+-*/" or index >= len(s) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    j = stack.pop() * number
                    stack.append(j)
                elif sign == "/":
                    j = int(stack.pop() / number)
                    stack.append(j)
                sign = char
                number = 0
        return sum(stack)
      
