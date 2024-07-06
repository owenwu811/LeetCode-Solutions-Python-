#There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

#The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

#The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

#Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


#python3 solution:

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r, c, visitset, prevh):
            if (r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or (r, c) in visitset or matrix[r][c] < prevh):
                return
            visitset.add((r, c))
            dfs(r + 1, c, visitset, matrix[r][c])
            dfs(r - 1, c, visitset, matrix[r][c])
            dfs(r, c + 1, visitset, matrix[r][c])
            dfs(r, c - 1, visitset, matrix[r][c])
        for c in range(cols):
            dfs(0, c, pac, matrix[0][c])
            dfs(rows - 1, c, atl, matrix[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, matrix[r][0])
            dfs(r, cols - 1, atl, matrix[r][cols - 1])

        res = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
