
#Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

#The distance between two adjacent cells is 1.

#Ex. mat = [[0,0,0],[0,1,0],[1,1,1]] > [[0,0,0],[0,1,0],[1,2,1]]




#python3 solution:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #we want the matrix at the end that shows, from each cell in the final matrix, how many hops it would take to reach a 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #our deque stores the coordinates of all 0s in the grid
        d = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0: # we are adding all 0 cell coordinates to the deque
                    d.append(([r, c]))
                else: #we see a 1, so we want to find the distance between this cell and the nearest 0 and put that distance as the value for this particular cell in our result
                    mat[r][c] = float('inf')
        while d:
            #these are the new coordinates of every 0, not r and c, so when you update and compare, you use zerox and zeroyy and not r and c - zerox and zeroyy are the starting points aka they are coordinates of a 0 cell, and since we start from every 0 cell coordinate on the deque and move somewhere new, then we are garunteed to land on a 1 cell because anything different from a 0 is a 1 cell, so that's why newonetilex and newonetiley are garunteed to be cooridnates of a 1 cell
            zerox, zeroy = d.popleft()
            for xnew, ynew in directions:
                #we are taking the coordinate of the 0 and exploring adjacent directions from that cell
                newonetilex, newonetiley = zerox + xnew, zeroy + ynew #assuming that this represents coordinates of a tile containing a 1 because the double for loop caught all the 0 tiles in the entire matrix
                #make sure that we are in bounds, so the if condition being true represents we are inbounds and found a smaller distance for that particular cell
                if 0 <=  newonetilex < len(mat) and 0 <= newonetiley  < len(mat[0]) and mat[newonetilex][newonetiley] > mat[zerox][zeroy] + 1:
                    #so again, remember we want each tile to represent the nearest distance from our one to a zero
                    mat[newonetilex][newonetiley] = mat[zerox][zeroy] + 1
                    d.append((newonetilex, newonetiley))
        return mat
