

#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



#Python3 solution:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(down, right, grid):
            if down < 0 or down >= len(grid) or right < 0 or right >= len(grid[0]) or grid[down][right] == '0':
                return #out of bounds, so return out of the function
            grid[down][right] = '0' #sinking the 1 into a 0 so we don't double count it
            dfs(down + 1, right, grid)
            dfs(down - 1, right, grid)
            dfs(down, right + 1, grid)
            dfs(down, right - 1, grid)
        count = 0 #we will return this at the end
        for down in range(len(grid)): #right
            for right in range(len(grid[0])): #down
                if grid[down][right] == '1': #we found a 1, so we found atleast 1 island
                    count += 1
                    dfs(down, right, grid) #we must do a boundary check before sinking that 1 into a 0!!!!!!
        return count 
        
