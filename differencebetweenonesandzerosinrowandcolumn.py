
#2482
#medium



#You are given a 0-indexed m x n binary matrix grid.

#A 0-indexed m x n difference matrix diff is created with the following procedure:

#Let the number of ones in the ith row be onesRowi.
#Let the number of ones in the jth column be onesColj.
#Let the number of zeros in the ith row be zerosRowi.
#Let the number of zeros in the jth column be zerosColj.
#diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
#Return the difference matrix diff.

#Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
#Output: [[0,0,4],[0,0,4],[-2,-2,2]]

#Explanation:
#- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
#- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
#- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
#- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
#- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
#- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
#- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
#- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
#- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2

#my own solution using python3:

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = []
        for r in grid:
            rows.append(r)
        print(rows)
        m, n = len(grid), len(grid[0])
        t = 0
        cols = []
        while t < len(grid[0]):
            cur = []
            for i in range(len(grid)):
                cur.append(grid[i][t])
            t += 1
            cols.append(cur)
        print(cols)
        rc, cc = [], []
        for row in rows:
            rc.append([row.count(1), row.count(0)])
        for column in cols:
            cc.append([column.count(1), column.count(0)])
        print(rc)
        print(cc)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(i, j)
                grid[i][j] = rc[i][0] + cc[j][0] - rc[i][1] - cc[j][1]
                print(grid[i][j])
        return grid
        
