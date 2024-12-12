#3099
#easy

#An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.


#Example 1:

#Input: x = 18

#Output: 9

#Explanation:

#The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and the answer is 9.


#my own solution using python3:

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a = 0
        for h in str(x):
            print(h)
            a += int(h)
        print(a)
        if x % a == 0:
            return a      
        return -1
