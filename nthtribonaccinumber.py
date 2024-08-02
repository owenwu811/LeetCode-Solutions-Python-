#The Tribonacci sequence Tn is defined as follows: 

#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

#Given n, return the value of Tn.

 

#Example 1:

#Input: n = 4
#Output: 4
#Explanation:
#T_3 = 0 + 1 + 1 = 2
#T_4 = 1 + 1 + 2 = 4
#Example 2:

#Input: n = 25
#Output: 1389537


#python3 solution:

#this question is part of the dynamic programming pattern in grokking course 

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3: #base case 
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for levelamount in range(3, n + 1):
            dp[levelamount] = dp[levelamount - 1] + dp[levelamount - 2] + dp[levelamount - 3]
        return dp[n]
