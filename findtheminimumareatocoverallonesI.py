
#3195
#medium

#You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

#Return the minimum possible area of the rectangle.

 

#Example 1:

#Input: grid = [[0,1,0],[1,0,1]]

#Output: 6


#my own solution using python3:

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        r, c = [], []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    print(i, j)
                    r.append(i)
                    c.append(j)
        x = max(r) - min(r) + 1
        y = max(c) - min(c) + 1
        return x * y
