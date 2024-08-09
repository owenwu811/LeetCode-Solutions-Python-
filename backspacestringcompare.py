#Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

#Note that after backspacing an empty text, the text will continue empty.

 

#Example 1:

#Input: s = "ab#c", t = "ad#c"
#Output: true
#Explanation: Both s and t become "ac".



#python3 solution:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char != "#":
                    stack.append(char)
                elif char == "#" and stack:
                    stack.pop()
            return stack

        return f(s) == f(t)


#3/19/24 review:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char == "#" and stack: #pound never goes on stack because pound is used for deletion
                    stack.pop() #deleting character
                elif char != "#": #letters go on rear of stack because letters are the ones getting deleted by pound
                    stack.append(char)
            return stack #state of either s or t 

        return f(s) == f(t)

#3/20/24:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char == "#" and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack
        return f(s) == f(t)


#3/21/24:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char == "#" and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack
        return f(s) == f(t)

#3/24/24:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char == "#" and stack:
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack


        return f(s) == f(t)

#3/30/24:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char == "#" and stack:
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack

        return f(s) == f(t)

#4/21/24 refresher:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(char):
            stack = []
            for a in char:
                if a != "#":
                    stack.append(a)
                elif a == "#" and stack:
                    stack.pop()
            return stack

        return f(s) == f(t)


#5/17/24 refresher:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for i in a:
                if i == "#" and stack:
                    stack.pop()
                elif i != "#":
                    stack.append(i)
            return stack
        return f(s) == f(t)

#6/12/24 review:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char != "#":
                    stack.append(char) #[a, b], [a, c]
                    print(stack)
                elif char == "#" and stack:
                    stack.pop()
                    print(stack)
            return stack #[a, c]
        return f(s) == f(t)

        #[a, d], [a, c]

        #[a]

#7/15/24 refresher:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(a):
            stack = []
            for char in a:
                if char == "#" and stack:
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack


        return compare(s) == compare(t)

#8/9/24 review:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(a):
            stack = []
            for char in a:
                if char != "#":
                    stack.append(char)
                elif char == "#" and stack:
                    stack.pop()
            return stack

 
        return f(s) == f(t)

        
