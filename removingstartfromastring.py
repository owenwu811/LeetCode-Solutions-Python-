
#You are given a string s, which contains stars *.

#In one operation, you can:

#Choose a star in s.
#Remove the closest non-star character to its left, as well as remove the star itself.
#Return the string after all stars have been removed.

#Note:

#The input will be generated such that the operation is always possible.
#It can be shown that the resulting string will always be unique.

#Input: s = "leet**cod*e"
#Output: "lecoe"
#Explanation: Performing the removals from left to right:
#- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
#- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
#- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
#There are no more stars, so we return "lecoe".

#my own solution in python3:

#idea is to use a stack - this is almost identical to the decode string question (simply use the stars to delete characters beforehand using a one to one relationship of stars: chars)

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
                continue
        return "".join(stack)
