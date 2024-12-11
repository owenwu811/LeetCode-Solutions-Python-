

#1030
#easy

#You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

#Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

#The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

 

#Example 1:

#Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
#Output: [[0,0],[0,1]]
#Explanation: The distances from (0, 0) to other cells are: [0,1]


#my own solution using python3:

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        myheap = []
        for i in range(rows):
            for j in range(cols):
                print(i, j)
                dist = abs(rCenter - i) + abs(cCenter - j)
                heapq.heappush(myheap, (dist, [i, j]))
        #print(myheap)
        myheap.sort()  
        print(myheap)
        res = []
        for h in myheap:
            res.append(h[1])
        return res
