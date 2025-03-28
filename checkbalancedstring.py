
#3340
#easy

#You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

#Return true if num is balanced, otherwise return false.

 

#Example 1:

#Input: num = "1234"

#Output: false

#Explanation:

#The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
#Since 4 is not equal to 6, num is not balanced.


#my own solution using python3:

class Solution:
    def isBalanced(self, num: str) -> bool:
        evensum = 0
        oddsum = 0
        for i in range(len(num)):
            if i % 2 == 0:
                evensum += int(num[i])
            else:
                oddsum += int(num[i])
        return evensum == oddsum
