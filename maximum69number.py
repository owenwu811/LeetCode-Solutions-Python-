
#1323
#easy

#You are given a positive integer num consisting only of digits 6 and 9.

#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
 
#Example 1:

#Input: num = 9669
#Output: 9969
#Explanation: 
#Changing the first digit results in 6669.
#Changing the second digit results in 9969.
#Changing the third digit results in 9699.
#Changing the fourth digit results in 9666.
#The maximum number is 9969.

#my own solution using python3:

class Solution:
    def maximum69Number (self, num: int) -> int:
        h = list(str(num))
        print(h)
        orig = h.copy()
        res = num
        for i in range(len(h)):
            if h[i] == "9":
                h[i] = "6"
            elif h[i] == "6":
                h[i] = "9"
            print(h)
            res = max(res, int("".join(h)))
            h[:] = orig
            print(h)
        return res
