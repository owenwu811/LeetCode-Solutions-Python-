
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


#10/2/24 review:

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



#my own solution using python3 on 12/19/24:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.cur = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 
            self.cur += 1
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)


        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    res = max(res, self.cur)
                    self.cur = 0
        return res
