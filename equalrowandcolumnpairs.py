
#2352

#Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

#A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).




#my own solution using python3:


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        for g in grid:
            rows.append(g)
        print(rows)
        cols = []
        m, n = len(grid), len(grid[0])
        i = 0
        k = 0
        while i < len(grid):
            cur = []
            for j in range(len(grid[0])):
                cur.append(grid[j][k])
            cols.append(cur)
            k += 1
            i += 1
        print(cols)
        ans = 0
        for i, r in enumerate(rows):
            if r in cols:
                ans += (cols.count(r))
        return ans

                    
        
