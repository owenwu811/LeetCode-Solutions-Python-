#There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

#The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

#The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

#Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


#python3 solution:

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        #if we start from the oceans and go inwards, we can go to cells that are the same height or bigger height
        #water it allowed to flow from 5 > 3 > 1, so water from the atlantic ocean is allowed to flow from 1 > 3 > 5 (this means that 5 can reach the atlantic ocean )
        #we will first go through the 1st row - [1,2,2,3,5] - pacific ocean. from there, run dfs downwards to find all nodes that can reach the pacific ocean coming from the pacific ocean's perspective
        #do the same thing with the bottom row - [5,1,1,2,4] - atlantic ocean. again, run a dfs upwards to see which nodes can reach the atlantic ocean coming from the atlantic ocean's perspective
        #maintain these cells in a set called visit
        rows, cols = len(matrix), len(matrix[0])
        #we have two sets maintaining all positions that can reach the pacific and the atlantic oceans
        pac, atl = set(), set()
        def dfs(r, c, visit, prevHeight):
            #going from pacific ocean and visit all cells we can because will tell us all cells that can reach the pcific ocean (FROM OCEAN > CELLS), so we are doing a boundary check 
            if ((r, c) in visit or r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] < prevHeight): #remember we are only allowed to go to heights that are greater than or equal to the current cell value aka height
                return
            #if we are not returning, then we are finding a new valid cell we can reach starting from the ocean, so add it to the set
            visit.add((r, c))
            #run dfs on all 4 adjacent neighbors
            dfs(r + 1, c, visit, matrix[r][c]) #previous height is the height at this cell for later on
            dfs(r - 1, c, visit, matrix[r][c])
            dfs(r, c + 1, visit, matrix[r][c])
            dfs(r, c - 1, visit, matrix[r][c])

        #go through every position in the 1st row and the last row in this for loop below 
        for c in range(cols):
            #run a dfs on this position cell, passing in a visit set to this dfs function since we are on the 1st row (1st row means it's the pacific ocean)
            #we know that water from the ocean from other cells can only go TO EQUAL VALUES OR GREATER (we reversed the thinking since we are going from the ocean to the cells )
            dfs(0, c, pac, matrix[0][c]) #giving a default value of heights[r][c] because we know we are allowed to visit equal valued cells
            #go through every position in last row aka number of rows - 1 and also going through every column in that row
            dfs(rows - 1, c, atl, matrix[rows - 1][c])
        #we also know 1st column = pacific ocean and last column = atlantic ocean
        for r in range(rows):
            #we know the 1st column can always reach the pacific ocean (border rule)
            dfs(r, 0, pac, matrix[r][0])
            dfs(r, cols - 1, atl, matrix[r][cols - 1])
        #after two loops above finish, we will have marked all cells that can reach the pacific and atlantic ocean
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c]) #position is in both pac and atl, add it to res
        return res
        
