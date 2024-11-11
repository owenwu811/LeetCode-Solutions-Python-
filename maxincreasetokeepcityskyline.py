

#807
#medium

#There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

#A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

#We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

#Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

#Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
#Output: 35
#Explanation: The building heights are shown in the center of the above image.
#The skylines when viewed from each cardinal direction are drawn in red.
#The grid after increasing the height of buildings without affecting skylines is:
#gridNew = [ [8, 4, 8, 7],
#            [7, 4, 7, 7],
#            [9, 4, 8, 7],
#            [3, 3, 3, 3] ]


#my own solution using python3:

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        #we want the max of both the row and column that dosen't exceed the max of either the row or column
        copy = grid
        rows = []
        origsum = 0
        for g in grid:
            rows.append(g)
            origsum += sum(g)
        print(rows)
        print(origsum)

        cols = []
        j = 0
        k = 0
        while j < len(grid):
            tmp = []
            for k in range(len(grid[j])):
                tmp.append(grid[k][j])
            cols.append(tmp)
            j += 1
        print(rows)
        maxrows = []
        for row in rows:
            maxrows.append(max(row))
        maxcols = []
        for column in cols:
            maxcols.append(max(column))
        print(maxrows, maxcols)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                copy[i][j] = min(maxrows[i], maxcols[j])
        print(copy)
        print(origsum)
        newsum = 0
        for c in copy:
            newsum += sum(c)
        print(newsum)
        return newsum - origsum
