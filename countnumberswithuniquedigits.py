
#357

#Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

#Example 1:

#Input: n = 2
#Output: 91
#Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
#Example 2:

#Input: n = 0
#Output: 1


#correct python3 solution:

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: #For n = 0, there's only one number: 0.
            return 1
        if n == 1: #For n = 1, the numbers are 0 through 9 (10 numbers in total).
            return 10
        #for n >= 2
        res = 9
        j = 9
        for i in range(n-1):
            res *= j
            j -= 1
        # recursion happens here
        return res + self.countNumbersWithUniqueDigits(n-1)

#for loop explanation: The goal here is to calculate how many unique digit numbers can be formed with n digits:

res *= j: This line multiplies the current value of res by j, which represents the number of available choices for the current digit. After choosing the first digit (9 choices), the second digit has 9 options, the third digit has 8 options, and so on. The value of res accumulates the total number of combinations for the current step.
j -= 1: This decreases the number of available digits for the next step, because each time you choose a digit, the pool of available unique digits shrinks.

#why are we looping from 0 to n - 1?
#Looping from 0 to n-1 ensures that the loop handles exactly n-1 digits (since the first digit is handled separately).

#9/23/24 review (could not resolve):

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10 
        j = 9
        res = 9
        for i in range(n - 1): #if n == 2, i = 0 because for i in range(1)
            res *= j # 9 * 9 = 81
            print(res)  
            j -= 1 #9 - 1 = 8
        return res + self.countNumbersWithUniqueDigits(n - 1)


#why 91 unique digits between 0 and 100?

To understand why there are 91 unique digit numbers between 0 and 100, we need to consider the range of numbers and how many of those have unique digits. Let's break it down:

Unique Digits Definition
A number has unique digits if no digit is repeated within that number.

Counting Unique Digit Numbers from 0 to 99
We will analyze the numbers from 0 to 99 (inclusive), and then we'll also consider the number 100 separately, as it doesn't count for unique digits since it has repeated '0's.

1. Count from 0 to 9

The numbers are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
All of these numbers have unique digits.
Count: 10 unique numbers
2. Count from 10 to 99

We need to consider two-digit numbers, which can be represented as 
a
b
ab (where 
a
a is the first digit and 
b
b is the second digit).
Constraints:
a
a (the first digit) can be from 1 to 9 (since 0 cannot be the first digit).
b
b (the second digit) can be from 0 to 9 but cannot be the same as 
a
a.
Calculation for Two-Digit Numbers (10 to 99)

First Digit 
a
a: There are 9 options (1-9).
Second Digit 
b
b: For each choice of 
a
a, there are 9 remaining choices (0-9 excluding 
a
a).
Thus, the total count of two-digit numbers with unique digits is:

9
# (choices for 
#a
#)
#×
#9
# (choices for 
#b
#)
#=
#81
# unique two-digit numbers
##9 (choices for a)×9 (choices for b)=81 unique two-digit numbers
#Total Unique Numbers from 0 to 99
#Adding the unique numbers from both ranges:

#Unique numbers from 0 to 9: 10
#Unique numbers from 10 to 99: 81
#Total unique digit numbers from 0 to 99:

#10 + 81 = 91
#Considering 100
#The number 100 has repeated '0's (not unique), so it does not contribute to the count of unique digit numbers.
