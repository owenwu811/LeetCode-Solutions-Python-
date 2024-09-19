
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
                if i == 0 and j == 0: #on top left cell
                    new[i][j] = grid[i][j]
                elif i == 0: #only can come from left since on 1st row
                    new[i][j] = grid[i][j] + new[i][j - 1]
                elif j == 0: #only can come from above since on 1st column
                    new[i][j] = grid[i][j] + new[i - 1][j]
                else:
                    new[i][j] = min(grid[i][j] + new[i][j - 1], grid[i][j] + new[i - 1][j])
        return new[-1][-1] #just get the very last value in the dp grid
