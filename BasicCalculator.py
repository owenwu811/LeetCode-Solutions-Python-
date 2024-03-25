
#python3 solution:

class Solution:
    def calculate(self, s: str) -> int:
            """
            1. Take 3 containers:
            num -> to store current num value only
            sign -> to store sign value, initially +1
            res -> to store sum
            When ( comes these containers used for calculate sum of intergers within () brackets.
            --------------------
            2. When c is + or -
            Move num to res, because we need to empty num for next integer value.
            set num = 0
            sign = update with c
            --------------------
            3. When c is '('
            Here, we need num, res, sign to calculate sum of integers within ()
            So, move num and sign to stack => [num, sign]
            Now reset - res = 0, num = 0, sign = 1 (default)
            --------------------
            4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -] 
            res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
            res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
            res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
            --------------------
            Simple Example: 2 - 3
            Initially res will have 2,i.e. res = 2
            then store '-' in sign. it will be used when 3 comes. ie. sign = -1
            Now 3 comes => res = res + num*sign
            Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
            """
            curnum, sign, ressum, stack = 0, 1, 0, deque()
            for char in s: 
                if char.isdigit(): # process if there is digit
                    curnum = curnum*10 + int(char) # for consecutive digits 98 => 9x10 + 8 = 98
                elif char in '+-': # if our current char that we are looping over is an operator because we only have + or - without times or divide
                    ressum += curnum*sign #apply computation of previous value
                    sign = -1 if char == '-' else 1 #sign = -1 indicates if PREVIOUS operation was a plus or minus
                    curnum = 0 #start with a fresh number at whatever next character in s is
                elif char == '(': #left opening parenthesis, so keep track of current state in stack
                    stack.append(ressum) #put in whatever we currently have as our result
                    stack.append(sign) #put in current sign that we work with so that, when we come out of (), we add it or subtract it to whatever the previous result was, so adding (4 + 5 + 2) to the 1 that came before (4 + 5 + 2)
                    ressum, sign = 0, 1 #reset sign to 1 because it's starting a new calculate function on inside of (4 + 5 + 2). reset res = 0 to start fresh
                elif char == ')': #right closing parenthesis, means we have closed one of our left parenthesis, so we need to apply whatever our current value is an add it to whatever previous was
                    ressum +=sign*curnum #parse out last number because we applied + or - at the point in which we saw a plus or minus "elif char in '+-" earlier, but if we see a right parenthesis in ) in (4 + 5 + 2), we wouldn't have seen it and taken care of last 2
                    ressum *=stack.pop() #we put the sign into the stack last, so we multiply by sign since sign was at the top of the stack (-1 or 1) if this line will actually execute again in the future, so this line represents the sign of whatever it was before we entered the parenthesis ()
                    ressum +=stack.pop() #add to ressum whatever is at the top of the stack, which will be our previous ressum from "elif char == '(': stack.append(ressum)" earlier, so we use a stack to easily keep track of what the previous sign was and previous result was, so (4 + 5 + 2) plus whatever expression was before that (1) in this case
                    curnum = 0 
            return ressum + curnum*sign #handling any values that are leftover in calculation and handle at end if anything left in our curnum that we haven't done, because, again, we apply addition whever we see a plus earlier at "elif char in '+-", but for something like the last 2 in s = " 2-1 + 2 ", we would never see a plus after it if it's the end of the string, so you would have never added the 2




#practice:

class Solution:
    def calculate(self, s: str) -> int:
        curnum, sign, ressum, stack = 0, 1, 0, []
        for char in s:
            if char.isdigit():
                curnum = curnum * 10 + int(char)
            elif char in '-+':
                ressum += sign * curnum #takes ressum from 0 to 4 to only include what is inside of the parenthesis since ressum was cleared from 1 to 0 when seeing "(" previously... then takes ressum from 4 to 9
                sign = 1 if char == "+" else -1
                curnum = 0 #if we didn't reset curnum to 0, the next time we see a + or -, curnum would be 14 instead of 4 when we first see "(" for calculating (4 + 5 + 2) AND we would be doing - curnum = 4 * 10 + 5 - instead of - curnum = 0 * 10 + 5 - when char = "5" when iterating over the 5 in (4 + 5 + 2) part, and since the execution flow goes from - curnum = curnum*10 + int(char) - directly back to - for char in s - and then to executing - elif char in "+-": - we would be doing - ressum += 45 * 1 - instead of ressum += 5 * 1 (this is inside of the - elif char in "+-": - block)
            elif char == "(":
                stack.append(ressum) #ressum here, not curnum!
                stack.append(sign)
                ressum, sign = 0, 1 #ressum = 0 to make way to calculating only what is inside of the parenthesis (4 + 5 + 2) since we are currently seeing "(", and ressum was 1 before this, and we just want to start adding from 4 to calculate only what is inside of the parenthesis 
            elif char == ")":
                ressum += sign * curnum
                ressum *= stack.pop() #sign processed 1st even though inserted 2nd in - elif char in "(": - block since append + pop is LIFO
                ressum += stack.pop()
                curnum = 0
        return ressum + sign * curnum


#practice again:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, currentn, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        return ressum + (currentn * sign)


#3/5/24:

class Solution:
    def calculate(self, s: str) -> int:
        #integer is our return type
        currentn, ressum, sign = 0, 0, 1
        stack = []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1 
                currentn = 0
            elif char == "(":
                ressum += currentn * sign
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0 #we don't reset the ressum here but the currentn
        return ressum + (currentn * sign) 


#3/6/24:

class Solution:
    def calculate(self, s: str) -> int:
        currentn, sign, ressum, stack = 0, 1, 0, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        return ressum + (currentn * sign)

#3/7/24:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, sign, currentn, stack = 0, 1, 0, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char) #if we see 9 and next see 8, then 98 = 9 * 10 + 8, which has to be the case since 9 and 8 are adjacent if you see 98
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0 #currentn would be incorrect if it wasn't reset here and if it was used again after encountering a +-
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1 #since we are already tracking state in stack since entering ()
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        return ressum + (currentn * sign)


#3/8/24:

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ressum, sign, currentn = 0, 1, 0 #currentn must be defined here first. you can't just assign it in the if char.isdigit() block
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        return ressum + (currentn * sign)


#3/9/24:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, currentn, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += (currentn * sign)
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += (currentn * sign)
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        ressum += (currentn * sign) #can do this as well 
        return ressum


#3/11/24:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, sign, currentn, stack = 0, 1, 0, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        ressum += currentn * sign
        return ressum


#3/12/24:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, sign, currentn, stack = 0, 1, 0, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        ressum += currentn * sign
        return ressum


#3/14/24:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, currentn, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        ressum += currentn * sign #last number processed
        return ressum
            


#3/16/24:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, sign, currentn, stack = 0, 1, 0, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(": #we have to start tracking what it inside of our parenthesis layer
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop() #sign since on top of stack
                ressum += stack.pop() #actual number
                currentn = 0
        ressum += currentn * sign #last number
        return ressum

#3/21/24:

class Solution:
    def calculate(self, s: str) -> int:
        res, sign, currentn, stack = 0, 1, 0, []
        for char in s: #char loops through everything in s whether its a symbol or number - s = "(1+(4+5+2)-3)+(6+8)"
            if char.isdigit():
                currentn = currentn * 10 + int(char) # 98 = (9 * 10) + 8
            elif char in "+-":
                res += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(": #we need to calculate sum of integers within ()
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif char == ")":
                res += currentn * sign #1st time this block executes: currentn = 2, sign = 1, res = 9 > 11 - s = "(1+(4+5+2)-3)+(6+8)"
                res *= stack.pop()
                res += stack.pop()
                currentn = 0 #currentn 2 > 0
        res += currentn * sign
        return res

#3/25/24:

class Solution:
    def calculate(self, s: str) -> int:
        ressum, currentn, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in "+-":
                ressum += currentn * sign
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum)
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        ressum += currentn * sign
        return ressum
