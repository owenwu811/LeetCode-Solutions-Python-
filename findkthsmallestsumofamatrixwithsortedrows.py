
#1439
#hard


#You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.

#You are allowed to choose exactly one element from each row to form an array.

#Return the kth smallest array sum among all possible arrays.

 

#Example 1:

#Input: mat = [[1,3,11],[2,4,6]], k = 5
#Output: 7
#Explanation: Choosing one element from each row, the first k smallest sum are:
#[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.




#correct python3 solution:

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        key = mat[0]
        tmp = []
        for row in mat[1:]:
            new = []
            for b in key:
                for r in row:
                    new.append(r + b)
            print(new)
            new.sort()
            key = new[:k] #key here keeps changing!
        return key[k - 1]
