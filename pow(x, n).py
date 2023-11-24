
#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


#Example 1:

#Input: x = 2.00000, n = 10
#Output: 1024.00000
#Example 2:

#Input: x = 2.10000, n = 3
#Output: 9.26100
#Example 3:

#Input: x = 2.00000, n = -2
#Output: 0.25000
#Explanation: 2-2 = 1/22 = 1/4 = 0.25


#Solution: python3


class Solution:
   def myPow(self, x: float, n: int) -> float:
       if n<0:
           x=1/x
           n=abs(n)
       if n==0: 
           return 1 #returning 1 means 1 becomes - self.mypow(x, n - 1) - as the entire equation
       if n%2==0: #takes care of cases where n is even - x is squared while n is divided by 2, so n//=2 means divided by 2 floored 
           x=x*x
           n//=2
        #n - 1 is used to make sure we don't have infinite recursion - if x = 2 and n = 5, what we really get in the below line is 2 * mypow(2, 5 - 1), so the equation with 4 actually gets passed into the recursive call?
       #the below line takes care of cases where n is odd
       return x*(self.myPow(x,n-1)) # if x = 2 and n = 5, we will eventually get 2 * mypow(2, 4), which will equal 32, and what returning 32 means is we return 32 when n becomes 0 in this line because n gets decreased by 1 every turn
