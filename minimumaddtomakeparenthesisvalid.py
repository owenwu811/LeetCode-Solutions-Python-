
#921
#medium

#A parentheses string is valid if and only if:

#It is the empty string,
#It can be written as AB (A concatenated with B), where A and B are valid strings, or
#It can be written as (A), where A is a valid string.
#You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

#For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
#Return the minimum number of moves required to make s valid.



#correct python3 solution:

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else: #in any other scenario such as )( or )) or ((, we increase the length of what we need aka the result, which is the length of the stack
                stack.append(char)
        return len(stack)

