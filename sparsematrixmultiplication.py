
#311
#medium


#Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

#Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
#Output: [[7,0,0],[-7,0,3]]


#my own solution using python3:

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res = mat1.copy()
        ans = []
        firstrowl, secondrowl = len(mat1[0]), len(mat2[0])
        
        #[0, 1],     #[1, 0]
        #[0, 0]      #[1, 0]
        #[0, 1]


       
        
        
        if len(mat1) == len(mat2) and firstrowl == secondrowl or len(mat1) > len(mat2):
            multiplier = []
            j = 0
            columns = []
            while j < len(mat2):
                t = []
                for i in range(len(mat2[0])):
                    multiplier.append(mat2[i][j])
                    t.append(mat2[i][j])
                columns.append(t)
                #print(t)
                j += 1
            print(mat1)
            print(columns) #we have the columns of mat2, so we want to multiply each row of mat1 with each column of mat2 and sum them up
            #[[1, 1], [0, 0]]

            #orig:
            #[1, 1],        #[1, 0], 
            #[1, 0]         #[1, 0]
            #mat1            mat2
            sol = []
            for rough in mat1:  
                roWs = []
                for a in range(len(columns)):
                    curr = 0
                    for b in range(len(columns[0])):
                        curr += (rough[b] * columns[a][b])
                    print(curr)
                    roWs.append(curr)
                sol.append(roWs)
            print(sol)
            return sol




                




            



        if len(mat1) == 1 and len(mat2) > 1:
            tot = 0
            current = mat1[0]
            for i, a in enumerate(current):
                #print(a, mat2[i][0])
                tot += (a * mat2[i][0])
            return [[tot]]
        startingx, startingy = 0, 0
        tomultiply = []
        while startingx < len(mat2) and startingy < len(mat2[0]):
            tomultiply.append(mat2[startingx][startingy])
            startingx += 1
            startingy += 1
        #print(tomultiply)
        for i in range(len(mat1)):
            tmp = []
            cur = 0
            for j in range(len(mat1[0])):
                if j < len(tomultiply):
                    product = mat1[i][j] * tomultiply[j]
                    res[i][j] = product
                    tmp.append(product)
                    cur += product
            ans.append(tmp)
        #print(ans)
        return res

        #[1, 1],        #[1, 0], 
        #[1, 0]         #[1, 0]



