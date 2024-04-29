
#Given an encoded string, return its decoded string.

#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

#You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

#The test cases are generated so that the length of the output will never exceed 105.

 

#Example 1:

#Input: s = "3[a]2[bc]"
#Output: "aaabcbc"



#python3 solution:

#remember that last in first out means the most recent in first out

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else: #i has reached a ], and, without appending ] to the list in order:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)


#3/21/24 review:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr #stack.pop() = a char, so stack = "2[ab", and substr = "c", so this line places b in front of c to make substr = "bc", and stack becomes "2[a"
                stack.pop() #popping the last [, so stack = "2[" > stack = "2", and substr = "abc" 
                k = ""
                while stack and stack[-1].isdigit(): #stack = "2"
                    k = stack.pop() + k #stack.pop() = a number, so k = "" > k = "2"
                stack.append(int(k) * substr) #k is a number, substr is a char string - both are appended to our stack, so substr = "abc", and k = "2", so stack = ["abcabc"]
        return "".join(stack)


#3/22/24:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() #popping last [
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)


#3/23/24:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)

#3/23/24 practice again:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr #insert element steeper in stack before previous
                stack.pop() #pop last [
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k #build consecutive digit
                stack.append(int(k) * substr)
        return "".join(stack)


#3/25/24 practice:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)
        

#3/26/24:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() 
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)

#3/28/24:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)

#4/2/24:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)

#4/8/24:

class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)


#4/13/24:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else: #start calculation of substring
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() #get rid of [
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)

#4/29/24 refresher:

class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() #pop off last [
                k = "" #k is the integer number that we look for after popping the [
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)
