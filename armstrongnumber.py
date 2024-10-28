
#1134
#easy

#Given an integer n, return true if and only if it is an Armstrong number.

#The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

 

#Example 1:

#Input: n = 153
#Output: true
#Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
#Example 2:

#Input: n = 123
#Output: false
#Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.


#my own solution using python3:

class Solution:
    def isArmstrong(self, n: int) -> bool:
        target = len(str(n))
        mystr = []
        for i in str(n):
            mystr.append(i)
        print(mystr)
        tot = 0
        for s in mystr:
            tot += (int(s) ** target)
        return tot == n
