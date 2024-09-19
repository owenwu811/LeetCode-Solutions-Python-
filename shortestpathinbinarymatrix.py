#1091
#medium
#bfs

#Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

#A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#All the visited cells of the path are 0.
#All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
#The length of a clear path is the number of visited cells of this path.




#my own slight variation of the solution after looking at solution:


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[n][n] == 1 or grid[0][0] == 1:
            return -1
        if len(grid) == 1: return 1
        d = deque([(0, 0)])
        level = 2
        while d:
            for i in range(len(d)):
                curx, cury = d.popleft()
                for (x, y) in (1, 1), (0, 0), (0, -1), (-1, 0), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1):
                    nx, ny = curx + x, cury + y
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid) or grid[nx][ny] != 0:
                        continue
                    if nx == n and ny == n:
                        return level
                    grid[nx][ny] = 5
                    d.append((nx, ny))
            level += 1
        return -1


#original python3 solution:

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1 #the question says the dimensions as n * n, not n * m
        if grid[0][0] == 1 or grid[n][n] == 1: return -1 #the bfs dosen't even start because 1st cell is not 0 or the bottom left is not a zero, so we already know it's not possible
        if len(grid) == 1: return 1 #input only has two layers, so only 1 step to reach end
        q, level = deque([(0,0)]), 2
        while q:
            for _ in range(len(q)):
                pr, pc = q.popleft()
                for (x,y) in ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)): #8 directions because diagonal aka top left or top right count too, so we are exploring all 8 directions from each node in the current level
                    r, c = pr + x, pc + y
                    if r<0 or r>n or c<0 or c>n or grid[r][c] != 0: #boundary check and making sure the current cell is a 0 because if not 0, then try a new direction because we only care about paths full of 0s
                        continue
                    if r == n and c == n: return level #we reached the bottom left of the matrix, so level is the number of levels aka the shortest path
                    grid[r][c] = 2 #marking cell as visited, so you can use any number other than 0
                    q.append((r, c))
            level += 1 #will be our anwser aka number of levels
        return -1 #no clear path aka no path solution found with all 0s from top left to bottom right
