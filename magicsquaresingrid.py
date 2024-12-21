#840
#medium

#A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

#Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

#Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

#Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
#Output: 1


#my own solution using python3:

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            if i < len(grid) - 1:
                if grid[i] == grid[i - 1]:
                    continue
            for j in range(len(grid[0])):
                startx, starty = i, j
                if i + 2 < len(grid) and j + 2 < len(grid[0]):
                    endx, endy = i + 2, j + 2
                    print(startx, starty, endx, endy)
                    rowsums, columnsums, posdsum, negdsum = [], [], 0, 0
                    smallrows, smallcolumns = [], []
                    for a in range(startx, endx + 1):
                        currowsum = 0
                        smallrow = []
                        for b in range(starty, endy + 1):
                            smallrow.append(grid[a][b])
                            if grid[a][b] < 1 or grid[a][b] > 9:
                                break
                            currowsum += grid[a][b]
                        smallrows.append(smallrow)
                        rowsums.append(currowsum)
                    #print(smallrows)
                    if smallrows[0] == smallrows[1] or smallrows[0] == smallrows[2]:
                        continue
                    smallrows.clear()
                    h = starty
                    while h <= starty + 2:
                        smallcolumn = []
                        curcolsum = 0
                        for k in range(startx, endx + 1):
                            #print(k, h)
                            smallcolumn.append(grid[k][h])
                            curcolsum += grid[k][h]
                        h += 1
                        columnsums.append(curcolsum)
                        smallcolumns.append(smallcolumn)
                    print(smallcolumns)
                    check = []
                    for c in smallcolumns:
                        for p in c:
                            check.append(p)
                    if 1 not in check or 2 not in check or 3 not in check or 4 not in check or 5 not in check or 6 not in check or 7 not in check or 8 not in check or 9 not in check:
                        continue
                    
                    posdx, posdy = startx, starty 
                    while posdx <= endx and posdy <= endy:
                        posdsum += grid[posdx][posdy]
                        posdx += 1
                        posdy += 1
                    negdx, negdy = startx, endy
                    cnt = 3
                    while cnt > 0:
                        negdsum += grid[negdx][negdy]
                        negdx += 1
                        negdy -= 1
                        cnt -= 1
                    if len(set(rowsums)) == 1 and len(set(columnsums)) == 1 and rowsums == columnsums and posdsum == negdsum == rowsums[0]:
                        res += 1
        return res
