#63
#medium


#You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

#An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

#Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

#The testcases are generated so that the answer will be less than or equal to 2 * 109.



#could not solve (correct python3 solution):

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        print(dp)
        dp[0][0] = 1
        print(dp)
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                print(i, j)
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if obstacleGrid[i][j] == 0:
                        if i > 0:
                            dp[i][j] += dp[i - 1][j]
                        if j > 0:
                            dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


#11/27/24 review:

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[-1])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]
