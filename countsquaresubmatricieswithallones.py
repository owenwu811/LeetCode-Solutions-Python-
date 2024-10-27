
#1277
#medium

#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

#Example 1:

#Input: matrix =
#[
#  [0,1,1,1],
#  [1,1,1,1],
#  [0,1,1,1]
#]
#Output: 15
#Explanation: 
#There are 10 squares of side 1.
#There are 4 squares of side 2.
#There is  1 square of side 3.
#Total number of squares = 10 + 4 + 1 = 15.


#my own solution using python3 after a slight misunderstanding correction:

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = matrix.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0 and j != 0:
                        dp[i][j] = 1
                    elif j == 0 and i != 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 #DO NOT INCLUDE DP[I][J] BECAUSE THAT would make it smaller!
        print(dp)
        cur = 0
        for d in dp:
            cur += sum(d)
        return cur
