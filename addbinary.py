
#Given two binary strings a and b, return their sum as a binary string.
#Input: a = "11", b = "1"
#Output: "100"

#python3 solution:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:] 


#if a = "1010" and b = "1011", output = "10101"
#s = bin(int("1010", 2) + int("1011", 2))
# 1010 = 2 power of 1 + 2 power of 3 = 10
# we don't care about 2 power of 0 because there is a 0 in that place
#1011 = 2 power of 0 plus 2 power of 1 plus 2 power of 3 = 11
# int ("10") + int("11") = int("21") 
# 1010 + 1011 = 10101 because the 1s in the 3rd column carry so 1 + 1 becomes 0 as place and 1 as above
# bin(int("21") converts to "0b10101"
#we then need to lop off the 0b in the front to get "10101"


#3/2/24 practice:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]
        

#3/3/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]

#3/4/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2)) #"1010" + "1011" = 10 + 11 = bin(int(21)) > "0b10101"
        return s[2:] #"0b10101" > "10101" aka from index 2 until the end of the string


#3/10/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #a = 1010 
        #b = 1011
        #10101
        #0b10101
        #10101
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]

#3/14/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]

#3/20/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]

#show work:
#a = "11", b = "1"
# 11 > 2 ^ 0 + 2 ^ 1 = 3
# 1 > 2 ^ 0 = 1
# 3 + 1 = 4
# print(bin(4)) > 0b100

#3/24/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]

#4/6/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        string = bin(int(a, 2) + int(b, 2))
        return string[2:]
        #11 #1

        #1010
        #1011
        # 1 0 1 01


#5/1/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]

#5/12/24:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]

#note that print(type(bin(2))) > gives you a type of class str, so binary is a string

#5/31/24 review:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = bin(int(a, 2) + int(b, 2))
        return res[2:]

#7/30/24 refresher:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = bin(int(a, 2) + int(b, 2))
        return res[2:]

#9/8/24 review:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]
