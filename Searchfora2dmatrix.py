

#You are given an m x n integer matrix matrix with the following two properties:
#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.

#You must write a solution in O(log(m * n)) time complexity.


#mysolution:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target == matrix[i][j]:
                    return True
        return False


#5/20/24 (missed) but my own solution in python3:

#the core idea behind this solution is we have to run binary search not only on each sublist in the input, but we also have to run binary search on each row and see if each element in the row matches target

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]: #we need to perform binary search in each row of the list of lists
                row = matrix[mid]
                lr, rr = 0, len(row) - 1
                while lr <= rr:
                    midrow = (lr + rr) // 2
                    if row[midrow] < target:
                        lr = midrow + 1 #always move l or r pointers, not mid! we are using l and r to calculate mid to close the search space!
                    elif row[midrow] > target:
                        rr = midrow - 1
                    else:
                        return True
                return False #the idea is that, since rows are sorted in ascending order, if the target exists in the entire matrix, it would be in this row, but it's not, so we can return False
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

#practice again:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]
                lr, rr = 0, len(row) - 1
                while lr <= rr:
                    midr = (lr + rr) // 2
                    if row[midr] < target:
                        lr = midr + 1
                    elif row[midr] > target:
                        rr = midr - 1
                    else:
                        return True
                return False
            elif matrix[mid][0] > target:
                r = mid - 1
            else: #matrix[mid][-1] < target: l = mid + 1 also works here too instead of else!
                l = mid + 1
        return False

#5/21/24 refresher:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid] #[10, 11, 16, 20]
                lr, rr =  0, len(row) - 1
                while lr <= rr:
                    midr = (lr + rr) // 2
                    if row[midr] == target:
                        return True
                    elif row[midr] < target:
                        lr = midr + 1
                    else:
                        rr = midr - 1
                return False
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
