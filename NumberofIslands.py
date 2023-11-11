

#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



#Python3 solution:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(down, right):
            if down < 0 or down >= len(grid) or right < 0 or right >= len(grid[0]) or grid[down][right] == '0':
                return
            grid[down][right] = '0'
            dfs(down + 1, right)
            dfs(down - 1, right)
            dfs(down, right + 1)
            dfs(down, right - 1)

        count = 0
        for down in range(len(grid)):
            for right in range(len(grid[0])):
                if grid[down][right] == '1':
                    count += 1
                    dfs(down, right)
        return count
