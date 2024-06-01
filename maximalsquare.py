#Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 4


#python3 solution:


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        sidelength = 0
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    sidelength = max(sidelength, dp[r][c])
        return sidelength * sidelength
