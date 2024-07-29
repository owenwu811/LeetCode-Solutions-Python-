
#Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

#Note that it is the kth smallest element in the sorted order, not the kth distinct element.

#Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
#Output: 13
#Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

#You must find a solution with a memory complexity better than O(n2).


#my own solution in Python3:

#this problem is pretty trivial since we know that all the elements in the input list of lists are already sorted in ascending order, so we just have to push all of the elements in the entire matrix to a minheap and then pop from the minheap k times, and after we have popped exactly k times, that kth pop will be our result

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = 0
        minheap = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(minheap, (matrix[r][c]))
        print(minheap)
        while k > 0:
            res = heapq.heappop(minheap)
            k -= 1
        return res
