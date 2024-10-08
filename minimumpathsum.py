
#64

#medium

#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

#Note: You can only move either down or right at any point in time.


#my own slight variation of correct solution using python3:

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        new = grid.copy()
        print(new)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: #on top left cell of input grid - only happens once in input on 1st iteration
                    new[i][j] = grid[i][j]
                elif i == 0: #only can come from left since on 1st row
                    new[i][j] = grid[i][j] + new[i][j - 1]
                elif j == 0: #only can come from above since on 1st column
                    new[i][j] = grid[i][j] + new[i - 1][j]
                else:
                    new[i][j] = min(grid[i][j] + new[i][j - 1], grid[i][j] + new[i - 1][j])
        return new[-1][-1] #just get the very last value in the dp grid


#evening of 9/19/24 review:

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = grid.copy()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    res[i][j] = grid[i][j]
                elif i == 0:
                    res[i][j] = grid[i][j] + res[i][j - 1]
                elif j == 0:
                    res[i][j] = grid[i][j] + res[i - 1][j]
                else:
                    res[i][j] = min(grid[i][j] + res[i][j - 1], grid[i][j] + res[i - 1][j])
        return res[-1][-1]


#9/25/24 review: (was able to solve)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid.copy()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = min(grid[i][j] + dp[i - 1][j],grid[i][j] + dp[i][j - 1])
        return dp[-1][-1]
