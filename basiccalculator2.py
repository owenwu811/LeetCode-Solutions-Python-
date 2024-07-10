

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
                    #without this, int(-3 / 2) > -1.5 > -1 vs. (-3 // 2) > -2, so 12 vs 13 as output for the s = "14-3/2" test case
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
      

#5/9/24 refresher:

class Solution:
    def calculate(self, s: str) -> int:
        number, sign, stack = 0, "+", []
        for index, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if char in "+-/*" or index >= len(s) - 1:
                if sign == "+":
                    stack.append(number) #we add NUMBER to the stack, not char because char is the sign if this block gets executed!
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    j = stack.pop() * number #we multiply by number, because, again, char is the sign!
                    stack.append(j)
                elif sign == "/":
                    j = int(stack.pop() / number)
                    stack.append(j)
                sign = char
                number = 0
        return sum(stack)


#5/11/24 refresher:

class Solution:
    def calculate(self, s: str) -> int:
        number, sign, stack = 0, "+", []
        for index, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if char in "+-/*" or index >= len(s) - 1:
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

#5/15/24 refresher:

class Solution:
    def calculate(self, s: str) -> int:
        # sign goes from + to * to 2 in "3+2*2"
        number, sign, stack = 0, "+", []
        for i, j in enumerate(s):
            if j.isdigit():
                number = number * 10 + int(j)
            if j in "+-/*" or i >= len(s) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    val = stack.pop() * number
                    stack.append(val)
                elif sign == "/":
                    val = int(stack.pop() / number)
                    stack.append(val)
                sign = j #we need this line because, when the for loop reaches * in "3+2*2", sign is still "+", so we append number, and stack = [3, 2], and then we set sign = "*". when for loop reaches final 2, stack = [3, 2], so stack.pop() = 2, and number = 2, so val = 2 * 2 = 4, so stack goes from [3, 2] to [3, 4] - NOTE THAT IN THE FINAL ITERATION, THE BLOCK ONLY EXECUTES BECAUSE I == LEN(S) - 1 IS TRUE!, SO SIGN IS ACTUALLY FINALLY SET TO "2"
                number = 0
        #in the end, since stack = [3, 4], sum(stack) = 7 for s = "3+2*2"
        return sum(stack)

#6/1/24 (missed):

class Solution:
    def calculate(self, s: str) -> int:
        #"3+2*2"
        currentn, sign, stack = 0, "+", []
        for i, char in enumerate(s):
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            if char in "+-/*" or i >= len(s) - 1: #i >= len(s) - 1 True will trigger this when we reach the last 2 in "3+2*2", so DON'T FORGET - 1 BECAUSE I IS AN INDEX
                if sign == "+":
                    stack.append(currentn) #[3] becomes [3, 2]
                elif sign == "-":
                    stack.append(-currentn)
                elif sign == "*":
                    val = stack.pop() * currentn #[3, 2] 
                    stack.append(val) #[3, 4]
                elif sign == "/":
                    val = int(stack.pop() / currentn)
                    stack.append(val)
                sign = char #goes from + to * to 2 (last one triggered by i >= len(s) - 1)
                currentn = 0
        return sum(stack) #sum([3, 4]) = 7

#6/2/24 review:

class Solution:
    def calculate(self, s: str) -> int:
        currentn, sign, stack = 0, "+", []
        for i, char in enumerate(s):
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            if char in "+-/*" or i == len(s) - 1:
                if sign == "+":
                    stack.append(currentn)
                elif sign == "-":
                    stack.append(-currentn)
                elif sign == "*":
                    val = stack.pop() * currentn
                    stack.append(val)
                elif sign == "/":
                    val = int(stack.pop() / currentn)
                    stack.append(val)
                sign = char
                currentn = 0
        return sum(stack)

#6/5/24 review:

class Solution:
    def calculate(self, s: str) -> int:
        currentn, sign, stack = 0, "+", []
        for i, char in enumerate(s):
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            if char in "+-/*" or i >= len(s) - 1:
                if sign == "+":
                    stack.append(currentn)
                elif sign == "-":
                    stack.append(-currentn)
                elif sign == "*":
                    val = stack.pop() * currentn
                    stack.append(val)
                elif sign == "/":
                    val = int(stack.pop() / currentn)
                    stack.append(val)
                sign = char
                currentn = 0
        return sum(stack)

#print(int(-3 / 2)) vs. print(-3 // 2)
#print(-3 // 2) > uses floor division. floor division rounds down to the nearest whole number towards negative infinity
#int(-3 / 2) > int discards the fractional part, so -1.5 becomes -1


#6/17/24 review (missed 2 days ago):

class Solution:
    def calculate(self, s: str) -> int:
        currentn, sign, stack = 0, "+", []
        for i, char in enumerate(s):
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            if char in "+-/*" or i >= len(s) - 1: #DO NOT FORGET -1 BECAUSE INDEXES ARE ONE LESS THAN LENGTH! YOU WOULD GET 5 INSTEAD OF 7 AS OUTPUT BECUASE WOULDN'T CONSIDER THE LAST 2 IN 3+2*2
                if sign == "+":
                    stack.append(currentn)
                elif sign == "-":
                    stack.append(-currentn)
                elif sign == "/":
                    val = int(stack.pop() / currentn)
                    stack.append(val)
                elif sign == "*":
                    val = stack.pop() * currentn
                    stack.append(val)
                sign = char
                currentn = 0
        return sum(stack)

#6/24/24 review:

class Solution:
    def calculate(self, s: str) -> int:
        currentn, sign, stack = 0, "+", []
        for i, char in enumerate(s):
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            if char in "+-/*" or i >= len(s) - 1:
                if sign == "+":
                    stack.append(currentn)
                elif sign == "-":
                    stack.append(-currentn)
                elif sign == "*":
                    val = stack.pop() * currentn
                    stack.append(val)
                elif sign == "/":
                    val = int(stack.pop() / currentn)
                    stack.append(val)
                sign = char
                currentn = 0
        return sum(stack)
                

#7/10/24 review:

class Solution:
    def calculate(self, s: str) -> int:
        currentn, sign, stack = 0, "+", [] #remember that sign starts at "+" instead of 1 because of the 2nd inner if block
        for i, char in enumerate(s):
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            if char in "+-/*" or i >= len(s) - 1:
                if sign == "+":
                    stack.append(currentn)
                elif sign == "-":
                    stack.append(-currentn)
                elif sign == "*":
                    val = stack.pop() * currentn
                    stack.append(val)
                elif sign == "/":
                    val = int(stack.pop() / currentn)
                    stack.append(val)
                sign = char
                currentn = 0
        return sum(stack)
        
