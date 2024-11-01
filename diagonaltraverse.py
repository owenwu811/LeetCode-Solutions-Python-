
#498
#medium


#Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

#Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,4,7,5,3,6,8,9]


#my own solution using python3:

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #[0, 0]
        #[1, 0], [0, 1]
        #         -1 +1
        #[2, 0], [1, 1], [0, 2]
        #         -1, +1  
        #[1, 2], [2, 1]
        #[2, 2]
            
        #do the opposite diagonal thing on the top border and rightmost border, going downwards
        #[0, 0], [0, 1], [0, 2]
        #[0, 2], [1, 2], [2, 2]

        first, second = [], []
        rows, cols = len(mat), len(mat[0])
        for i in range(cols):
            #print(i)
            #print(mat[0][i])
            first.append([0, i])
            #print("h")
        j = 0
        while j < len(mat):
            for k in range(len(mat[0])):
                #print(k)
                if k == len(mat[0]) - 1:
                    second.append([j, k])
                    #print(mat[j][k])
            j += 1
        #print(first)
        #print(second)
        firsthalf = []
        for f in first:
            bx, by = f[0], f[1]
            x, y = f[0], f[1]
            tmp = []
            #[0, 1] [1, 0]
            #       [+1, -1]
            while x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]):
                #f[0] -= 1
                #f[1] += 1
                print(x, y)
                tmp.append(mat[x][y])
                x += 1
                y -= 1
                #print(x, y)
            print(tmp)
            firsthalf.append(tmp)
        print(firsthalf)
        for s in second:
            bx, by = s[0], s[1]
            x, y = s[0], s[1]
            tmp = []
            #[0, 1] [1, 0]
            #       [+1, -1]
            while x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]):
                #f[0] -= 1
                #f[1] += 1
                print(x, y)
                tmp.append(mat[x][y])
                x += 1
                y -= 1
                #print(x, y)
            print(tmp)
            if tmp in firsthalf:
                continue
            firsthalf.append(tmp)
        print(firsthalf)
        #we want to reverse [1], [3, 5, 7], and [9]
        if len(firsthalf) > 3:
            for i, f in enumerate(firsthalf):
                if i % 2 == 0:
                    firsthalf[i] = f[::-1]
        print(firsthalf)
        ans = []
        for i in range(len(firsthalf)):
            for j in range(len(firsthalf[i])):
                ans.append(firsthalf[i][j])
        return ans
