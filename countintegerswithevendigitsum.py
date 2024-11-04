
#2180
#easy

#Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

#The digit sum of a positive integer is the sum of all its digits.

 

#Example 1:

#Input: num = 4
#Output: 2
#Explanation:
#The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
#Example 2:

#Input: num = 30
#Output: 14
#Explanation:
#The 14 integers less than or equal to 30 whose digit sums are even are
#2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.


#my own solution using python3:

class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(2, num + 1):
            cur = 0
            #print(i)
            for a in str(i):
                print(int(a))
                cur += int(a)
                #print(int(a))
            #print(cur)
            if cur % 2 == 0:
                res += 1
        return res
