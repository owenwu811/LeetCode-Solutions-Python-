

#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



#Python3 solution:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(down, right, grid):
            if down < 0 or down >= len(grid) or right < 0 or right >= len(grid[0]) or grid[down][right] == '0': #skipping this block if line 24 equals 1
                return #out of bounds, so return out of the function
            grid[down][right] = '0' #sinking the 1 into a 0 so we don't double count it - we go here from line 24
            dfs(down + 1, right, grid) #and then we call dfs again to go down one tile and then we boundary check this new tile in line 14 
            dfs(down - 1, right, grid)
            dfs(down, right + 1, grid)
            dfs(down, right - 1, grid)
        count = 0 #we will return this at the end
        for down in range(len(grid)): #right
            for right in range(len(grid[0])): #down
                if grid[down][right] == '1': #we found a 1, so we found atleast 1 island - if grid[I[j] == 1, then we increment count, and then we call dfs, and we skip the if block and directly call grid[I][j] = '0'? and then we execute dfs(I + 1, j) - so we are boundary checking dfs(I + 1, j) aka the new tile, not the old tile with 1 we already visited
                    count += 1
                    dfs(down, right, grid) #we must do a boundary check before sinking that 1 into a 0!!!!!!
        return count 
        


#the 1st time this if statement in line 14 is evalvulated, it will never execute the inner block because it came from the if statement where grid[I]jj] was equal to 1 from line 24. It's only after one of the recursive calls below executes that this if block can become true?
                #return
           # grid[i][j] = '0'
            #dfs(i + 1, j, grid) #recursive calls below refers to one of these 4 in lines 17 - 20
