
#1895
#medium

#A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

#Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

#Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
#Output: 3
#Explanation: The largest magic square has a size of 3.
#Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
#- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
#- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
#- Diagonal sums: 5+4+3 = 6+4+2 = 12


#my own solution using python3:

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        new = []
        for g in grid:
            if len(g) == 1:
                new.append(g[0])
        if len(set(new)) == len(grid) - 1:
            return 1
        res = 1
        seen = set() 
        for i in range(len(grid)):
            cur = set(grid[i])
            if len(cur) != 1:
                break 
        else:
            return len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                startx, starty = i, j 
                begx, begy = i, j 
                while startx < len(grid) and starty < len(grid[0]):
                    startx += 1
                    starty += 1
                    rowsums, colsums = [], []
                    pdbank = [[begx, begy]]
                    for a in range(begx, startx):
                        curr = 0
                        for b in range(begy, starty):
                            if a == pdbank[-1][0] + 1 and b == pdbank[-1][1] + 1:
                                pdbank.append([a, b])
                            curr += grid[a][b]
                        rowsums.append(curr)
                        if len(set(rowsums)) != 1:
                            break
                    if len(set(rowsums)) != 1 or len(rowsums) == 1:
                        continue
                    m = begy
                    while m <= starty:
                        curcol = 0
                        for k in range(begx, startx):
                            if k >= 0 and k < len(grid) and m >= 0 and m < len(grid[0]):
                                curcol += grid[k][m]
                        colsums.append(curcol)
                        m += 1
                    colsums.pop()
                    if len(set(colsums)) != 1:
                        continue
                    end, beg = pdbank[-1][-1], pdbank[0][0]
                    negbank = [[beg, end]]
                    limit = len(pdbank) - 1
                    while limit > 0:
                        nx, ny = negbank[-1][0] + 1, negbank[-1][-1] - 1
                        negbank.append([nx, ny])
                        limit -= 1
                    pdbanks, ngbanks = 0, 0
                    for p in pdbank:
                        pdbanks += grid[p[0]][p[1]]
                    for n in negbank:
                        ngbanks += grid[n[0]][n[1]]
                    if len(set(rowsums)) == 1 and len(set(colsums)) == 1 and rowsums == colsums:
                        if rowsums[0] == colsums[0] == pdbanks == ngbanks:
                            res = max(res, len(rowsums))
        return res
