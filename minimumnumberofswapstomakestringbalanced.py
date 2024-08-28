
#medium
#72% acceptance rate

#You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

#A string is called balanced if and only if:

#It is the empty string, or
#It can be written as AB, where both A and B are balanced strings, or
#It can be written as [C], where C is a balanced string.
#You may swap the brackets at any two indices any number of times.

#Return the minimum number of swaps to make s balanced.

#Input: s = "][]["
#Output: 1
#Explanation: You can make the string balanced by swapping index 0 with index 3.
#The resulting string is "[[]]".

#correct python3 solution (was not able to solve on my own):

class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        res = 0
        for i, char in enumerate(s):
            if char == "[":
                stack.append(char) #I guess this means openings always go on the stack
            elif stack and char == "]": #making the pair
                stack.pop()
            else:
                res += 1
        return (res + 1) // 2 #Because every time you swap a pair of brackets you fix two closed brackets in one swap!
        
