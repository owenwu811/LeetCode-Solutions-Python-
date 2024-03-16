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
