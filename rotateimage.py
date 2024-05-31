
#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

#Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

#python3 solution:

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numrows = len(matrix) #n = 3
        
        # Step 1: Transpose the matrix
        #when i = 0, j = 0, 1, 2. when i = 1, j = 1, 2. when i = 2, j = 2
        for r in range(numrows): #i:012
            for c in range(r, numrows): #j:012, 12, 2
                #i = 0 and j = 0, and nothing is swapped
                #i = 0 and j = 1, so 2 and 4 are swapped:
                #[1, 2, 3]
                #[4, 5, 6]
                #[7, 8, 9]

                #becomes (2 and 4 are swapped)

                #[1, 4, 3]
                #[2, 5, 6]
                #[7, 8, 9]
                #when i = 0 and j = 2, matrix[0][2] and matrix[2][0] are swapped aka top right and bottom left corner 
                #[1, 4, 3]
                #[2, 5, 6]
                #[7, 8, 9]

                #becomes (3 and 7 are swapped)

                #[1, 4, 7]
                #[2, 5, 6]
                #[3, 8, 9]

                #when i = 1 and j = 2, matrix[1][2] and matrix[2][1] are swapped aka 6 and 8 from above matrix 
                #in the final iteration, when i = 2 and j = 2, nothing is swapped
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # Step 2: Reverse each row
        #we have 
        #[1, 4, 7]
        #[2, 5, 8]
        #[3, 6, 9]
         
        #becomes

        #[7, 4, 1]
        #[8, 5, 2]
        #[9, 6, 3]

        for i in range(numrows): #012, so i is the index of each row
            matrix[i].reverse()

        #matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        #numrows = 4
        #i = 0 and j = 0, so nothing swapped
        #i = 0 j = 1, so 1 and 2 are swapped:

        #[5, 1, 9, 11]
        #[2, 4, 8, 10]
        #[13, 3, 6, 7]
        #[15, 14, 12, 16]

        #becomes

        #[5, 2, 9, 11]
        #[1, 4, 8, 10]
        #[13, 3, 6, 7]
        #[15, 14, 12, 16]

        #i = 0 and j = 2, so 13 and 9 are swapped:

        #[5, 2, 9, 11]
        #[1, 4, 8, 10]
        #[13, 3, 6, 7]
        #[15, 14, 12, 16]

        #becomes

        #[5, 2, 13, 11]
        #[1, 4, 8, 10]
        #[9, 3, 6, 7]
        #[15, 14, 12, 16]

        #i = 0 and j = 3, so 11 and 15 are swapped:

        #[5, 2, 13, 11]
        #[1, 4, 8, 10]
        #[9, 3, 6, 7]
        #[15, 14, 12, 16]

        #becomes

        #[5, 2, 13, 15]
        #[1, 4, 8, 10]
        #[9, 3, 6, 7]
        #[11, 14, 12, 16]

        #i = 0 and j is out of bounds and can't increase past 3, so i = 1, j = 1
        #i = 1 and j = 1, so nothing is swapped since both i and j are the same cell
        #i = 1 and j = 2, so 8 and 3 are swapped:

        #[5, 2, 13, 15]
        #[1, 4, 8, 10]
        #[9, 3, 6, 7]
        #[11, 14, 12, 16]

        #becomes

        #[5, 2, 13, 15]
        #[1, 4, 3, 10]
        #[9, 8, 6, 7]
        #[11, 14, 12, 16]

        #i = 1 and j = 3, so 10 and 14 are swapped:

        #[5, 2, 13, 15]
        #[1, 4, 3, 10]
        #[9, 8, 6, 7]
        #[11, 14, 12, 16]

        #becomes

        #[5, 2, 13, 15]
        #[1, 4, 3, 14]
        #[9, 8, 6, 7]
        #[11, 10, 12, 16]

        #j goes out of bounds since j can't pass 3 since j is up to but not including n, so i = 2 and j = 2

        #i = 2 and j = 2, so nothing can be swapped 

        #i = 2 and j = 3, so 12 and 7 are swapped:

        #[5, 2, 13, 15]
        #[1, 4, 3, 14]
        #[9, 8, 6, 7]
        #[11, 10, 12, 16]

        #becomes

        #[5, 2, 13, 15]
        #[1, 4, 3, 14]
        #[9, 8, 6, 12]
        #[11, 10, 7, 16]

        #j = 3, so it goes out of bounds

        #i = 3 and j = 3, so no swapping
        #j goes out of bounds since can't get to 4 and i also goes out of bounds since can't get to 4
    
        #mind you j is not used here but is still 3 below
        #we go to for i in range(n):, so i = 0
        #we reverse the 0th row from [5, 2, 13, 15] to [15, 13, 2, 5]
        #i = 1, so we reverse the 1st index row from [1, 4, 3, 14] to [14, 3, 4, 1]
        #i = 2, so we reverse the 2nd index row from [9, 8, 6, 12] to [12, 6, 8, 9]
        #lastly, i = 3, so we reverse the 3rd index row from [11, 10, 7, 16] to [16, 7, 10, 11]
        #for i in range(n): > i = 3, so i can't increment anymore and the loop terminates

#5/28/24 review:

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numrows = len(matrix)
        for r in range(numrows):
            for c in range(r, numrows):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for i in range(numrows):
            matrix[i].reverse()

#5/30/24 review:

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for i in range(n):
            matrix[i].reverse()

#5/31/24 review:

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        inputlen = len(matrix)
        for r in range(inputlen):
            for c in range(r, inputlen):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for i in range(inputlen):
            matrix[i].reverse()
        
