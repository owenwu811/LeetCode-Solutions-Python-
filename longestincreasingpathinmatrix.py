
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].



#python3 solution:


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        def dfs(r, c, prevval):
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] <= prevval:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            self.res = 1 #the current cell counts as 1 in the path
            #the idea is that we run dfs to find the longest path starting from the next cell over, and then we add 1 to it to include the current cell we are on
            self.res = max(self.res, 1 + dfs(r + 1, c, matrix[r][c])) #prevval becomes the current cell's value in the next turn that this recursive call processes
            self.res = max(self.res, 1 + dfs(r - 1, c, matrix[r][c]))
            self.res = max(self.res, 1 + dfs(r, c + 1, matrix[r][c]))
            self.res = max(self.res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = self.res
            return self.res

        self.res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1) #-1 because we know that every cell value is 0 or greater, so then matrix[r][c] will never be <= -1 on the 1st turn
        return max(dp.values())
