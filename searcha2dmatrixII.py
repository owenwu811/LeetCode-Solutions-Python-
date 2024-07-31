
#Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
#Output: true



#python3 solution:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0]) #rows, cols = 5, 5
        row, col = 0, cols - 1 #row, col = 0, 4
        
        while row < rows and col >= 0: #while 0 < 5 and 4 >= 0, 0 < 5 and 3 >= 0, 0 < 5 and 2 >= 0, 0 < 5 and 1 >= 0, 1 < 5 and 1 >= 0
            if matrix[row][col] == target: #matrix[0][4] = 15, and 15 != 5 (our target), matrix[0][3] = 11, and 11 != 5 (our target), matrix[0][2] = 7, and 7 != 5, matrix[0][1] = 4, and 4 != 5, matrix[1][1] = 5, and 5 == 5, so we found our target, so return True
                return True
            elif matrix[row][col] > target: #since 15 > 5, we move col down one...we move from 15 to 11 to 7 to 4, and then 4 is not bigger than 5 and is not equal to 5, so 4 is less than 5, so move down to cell (1, 1) in the else block
                col -= 1
            else: #instead of moving left, we move down, so we go from matrix[0][1] to matrix[1][1], and we call the while loop again
                row += 1
        
        return False
