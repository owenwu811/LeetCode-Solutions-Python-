



#python3 solution:

#remember that, just like with valid parenthesis problem, )( is not valid, so closing bracket can never come first!

#only add more opening parenthesis to stack if open < n 
#only add more closing parenthesis if closec < openc
#only stop adding parenthesis when open == closed == n (base case aka hit bottom of tree [()()()])

#[(((] - reached n's limit of 3, so we can only add another close bracket
#closed count cannot be bigger than open count, so we cannot add another close bracket because openc must be bigger than closec to add closing, so we can only add open aka cannot add close bracket now - one scenario to keep in mind
#[(()] - at this point in our tree, we have 2 decisions: add a close bracket or open b because both if conditionals are true at this point
#closing count < open count is the same as open count > closing count
#you cannot start with a closing parenthesis because no matter what you do [)(((], it will always be invalid!


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []
        def backtrack(openc, closec, n):
            if openc == closec == n: #[()()()]
                res.append("".join(stack))
                return #control flow goes directly to stack.pop() in closec < openc
            if closec < openc:
                stack.append(")")
                backtrack(openc, closec + 1, n)
                #stack.pop() will take [()()()] into [()()(], and now openc still not less than n, so we violate the alternate if condition below, so stack.pop() there
                stack.pop() #when either (closec < openc) or (openc < n)is violated during process of bubbling up tree after already hitting base case and appending [()()()] to res, these two conditionals (openc < n) and (closec < openc) will alternate to stack.pop() to bubble back up tree
            if openc < n:
                stack.append("(")
                backtrack(openc + 1, closec, n)
                stack.pop() 
        backtrack(0, 0, n)
        return res

#                  [((]               [()]
#             [(((]     [(()]                 [()(]
#          [((()]   [(()(] [(())]         [()((]  [()()]
#         [((())] [(()()]  [(())(]       [()(()]   [()()(]
#       [((()))] [(()())]  [(())()]      [()(())]  [()()()] - root base case aka where we start backtracking. (closec < openc)'s stack.pop() is starting to backtrack from here [()()()] to [()(], and then after we backtrack to [()(], we append ["("] inside of the if openc < n block to turn ["()("] into ["()(("] aka try the left side of the tree since we tried the right side of the tree first which was adding open
#
#



#4/3/24 practice:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []
        def backtrack(openc, closec, n):
            if openc == closec == n:
                res.append("".join(stack))
                return
            if openc < n:
                stack.append("(")
                backtrack(openc + 1, closec, n)
                stack.pop()
            if closec < openc:
                stack.append(")")
                backtrack(openc, closec + 1, n)
                stack.pop()
        backtrack(0, 0, n) #start with 0 because we haven't seen any parenthesis yet to kick off recursion
        return res

#4/4/24 practice:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(openc, closec, stack):
            if openc == closec == n:
                res.append("".join(stack))
                return
            if closec < openc:
                stack.append(")")
                f(openc, closec + 1, stack)
                stack.pop()
            if openc < n:
                stack.append("(")
                f(openc + 1, closec, stack)
                stack.pop()

        res = []
        f(0, 0, []) #we start with an empty stack, and we add brackets onto the stack given out conditions
        return res
        
#4/6/24 review:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #)( is not well formed
        stack = []
        def f(openb, closeb, n):
            if openb == closeb == n:
                res.append("".join(stack))
                return
            if closeb < openb:
                stack.append(")")
                f(openb, closeb + 1, n)
                stack.pop()
            if openb < n:
                stack.append("(")
                f(openb + 1, closeb, n)
                stack.pop()

        res = []
        f(0, 0, n)
        return res

#4/8/24:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(openc, closec, stack):
            if openc == closec == n: #reached bottom of tree, so backtrack
                res.append("".join(stack))
                return
            if closec < openc:
                stack.append(")")
                f(openc, closec + 1, stack) #we are using the count of open vs close parenthesis to know when to backtrack
                stack.pop() #notice how this backtracking step comes after all the recursive calls in the line right above finish
            if openc < n:
                stack.append("(")
                f(openc + 1, closec, stack)
                stack.pop()


        res = []
        f(0, 0, [])
        return res

#4/12/24:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(openc, closec, stack):
            if openc == closec == n:
                res.append("".join(stack))
                return
            if closec < openc:
                stack.append(")")
                generate(openc, closec + 1, stack)
                stack.pop()
            if openc < n: #not elif - if because closec < openc dosen't impact openc < n - they both need to execute in some cases 
                stack.append("(")
                generate(openc + 1, closec, stack)
                stack.pop()
        res = []
        generate(0, 0, [])
        return res


#4/25/24 refresher:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(openc, closec, stack):
            if openc == closec == n:
                res.append("".join(stack))
                return
            if openc < n: #not elif
                stack.append("(")
                f(openc + 1, closec, stack)
                stack.pop()
            if closec < openc: #not elif 
                stack.append(")")
                f(openc, closec + 1, stack)
                stack.pop()
        res = []
        f(0, 0, [])
        return res
