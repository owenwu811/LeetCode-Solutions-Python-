#1329
#medium


#A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

#Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

#Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
#Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

#my own solution using python3:

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        #[[11,25,66,1,69,7],
        #[23,55,17,45,15,52],
        #[75,31,36,44,58,8],
        #[22,27,33,25,68,4],
        #[84,28,14,11,5,50]]

        #[4, 0]
        #[3, 0], [4, 3]
        #        [+1, +1]
        actual = []
        startingx, startingy = len(mat) - 1, 0
        while startingx >= 0 and startingy >= 0:
            #print(startingx, startingy)
            curx, cury = startingx, startingy
            newl = []
            while curx >= 0 and curx < len(mat) and cury >= 0 and cury < len(mat[0]):
                #print(mat[curx][cury])
                newl.append(mat[curx][cury])
                curx += 1
                cury += 1
            #print("h")
            startingx -= 1
            actual.append(newl)
        #print(actual)
        secondx, secondy = 0, 1
        while secondx >= 0 and secondx < len(mat) and secondy >= 0 and secondy < len(mat[0]):
            curx, cury = secondx, secondy
            newl = []
            while curx >= 0 and curx < len(mat) and cury >= 0 and cury < len(mat[0]):
                print(mat[curx][cury])
                newl.append(mat[curx][cury])
                curx += 1
                cury += 1
            secondy += 1
            actual.append(newl)
        #print(actual)
        for a in actual:
            a.sort()
        #[[11,25,66,1,69,7],
        #[23,55,17,45,15,52],
        #[75,31,36,44,58,8],
        #[22,27,33,25,68,4],
        #[84,28,14,11,5,50]]

        #[[5,17,4,1,52,7],
        #[11,11,25,45,8,69],
        #[14,23,25,44,58,15],
        #[22,27,31,36,50,66],
        #[84,28,75,33,55,68]]


        new = deque()
        for i in range(len(actual)):
            for j in range(len(actual[i])):
                new.append(actual[i][j])


        #print(new)
        #[2, 0]
        #[1, 0], [2, 1]
        #        [+1, +1]
        #[0, 0], [1, 1], [2, 2]

        #[0, 1], [1, 2], [2, 3]
        #        [+1, +1]
        #[0, 2], [1, 3]
        #[0, 3]
        startingx, startingy = len(mat) - 1, 0
        while startingx >= 0 and startingy >= 0:
            #print(startingx, startingy)
            curx, cury = startingx, startingy
            while curx >= 0 and curx < len(mat) and cury >= 0 and cury < len(mat[0]):
                mat[curx][cury] = new.popleft()
                curx += 1
                cury += 1
            startingx -= 1
        #print(mat)
        #[0, 1], [1, 2], [2, 3]
        #        [+1, +1]
        #[0, 2], [1, 3]
        #[0, 3]
        #print(new)

        #[[11,25,66,1,69,7],
        #[23,55,17,45,15,52],
        #[75,31,36,44,58,8],
        #[22,27,33,25,68,4],
        #[84,28,14,11,5,50]]

        #[84, 22, 84, 14, 27, 31, 44, 45, 68, 7, 15, 17, 25, 45, 52, 15, 45, 52, 66, 1, 15, 52, 52, 69, 7])
        secondx, secondy = 0, 1
        while secondx >= 0 and secondx < len(mat) and secondy >= 0 and secondy < len(mat[0]):
            curx, cury = secondx, secondy
            while curx >= 0 and curx < len(mat) and cury >= 0 and cury < len(mat[0]):
                #print(curx, cury)
                if new:
                    mat[curx][cury] = new.popleft()
                curx += 1
                cury += 1
            secondy += 1
        return mat
