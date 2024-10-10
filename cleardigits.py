
#3174
#easy

#You are given a string s.

#Your task is to remove all digits by doing this operation repeatedly:

#Delete the first digit and the closest non-digit character to its left.
#Return the resulting string after removing all digits.

 

#Example 1:

#Input: s = "abc"

#Output: "abc"

#Explanation:

#There is no digit in the string.


#my own solution using python3:

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if not (c.isdigit()):
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)
