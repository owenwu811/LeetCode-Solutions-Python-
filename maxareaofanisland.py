
#695
#medium


#You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

#The area of an island is the number of cells with a value 1 in the island.

#Return the maximum area of an island in grid. If there is no island, return 0.


#correct python3 solution:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            result = 1
            result += dfs(r + 1, c)
            result += dfs(r - 1, c)
            result += dfs(r, c + 1)
            result += dfs(r, c - 1)
            return result
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
