

#medium
#1249

#Given a string s of '(' , ')' and lowercase English characters.

#Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

#Formally, a parentheses string is valid if and only if:

#It is the empty string, contains only lowercase characters, or
#It can be written as AB (A concatenated with B), where A and B are valid strings, or
#It can be written as (A), where A is a valid string.


#grokking's solution: couldn't solve by myself

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        slist = list(s)
        for i, char in enumerate(s):
            if stack and stack[-1][0] == "(" and char == ")":
                stack.pop()
            elif char == "(" or char == ")":
                stack.append([char, i])
        for p in stack:
            slist[p[1]] = ""
        result = "".join(slist)
        return result
            
