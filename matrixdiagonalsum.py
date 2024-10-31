
#1572
#easy


#Given a square matrix mat, return the sum of the matrix diagonals.

#Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

#Input: mat = [[1,2,3],
#              [4,5,6],
#              [7,8,9]]
#Output: 25
#Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
#Notice that element mat[1][1] = 5 is counted only once.


#my own solution using python3:

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        first = []
        for i in range(rows):
            first.append([i, i])
        #print(first)
        new = []
        cur = 0
        secondstarting = [cols - 1, 0]
        j = 0
        while j < len(mat):
            #print(secondstarting)
            new.append(secondstarting.copy())
            #print(new)
            secondstarting[0] -= 1
            secondstarting[1] += 1
            #print(secondstarting)
            j += 1
        #new.append(secondstarting.copy())
        #print(new)
        #print(cur)
        print([1, 1] in [[0, 0], [1, 1], [2, 2]])
        #[0, 3]
        #[1, 2]
        #[2, 1]
        #[3, 0]
        print(first)
        print(new)
        ans = 0
        for f in first:
            #print(f)
            ans += mat[f[0]][f[1]]
        for n in new:
            val1, val2 = n[0], n[1]
            #print(mat[2][1])
            if [val1, val2] in first:
                continue
            ans += mat[val1][val2]
        return ans

