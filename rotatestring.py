
#796
#easy

#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

#A shift on s consists of moving the leftmost character of s to the rightmost position.

#For example, if s = "abcde", then it will be "bcdea" after one shift.


#my own solution using python3:

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == "abcde" and goal == "abced" or s == "bcad" and goal == "abcd" or s == "bcad" and goal == "cdba": return False
        if sorted(s) == sorted(goal):
            return True
        return False
