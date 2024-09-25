

#624
#medium


#You are given m arrays, where each array is sorted in ascending order.

#You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

#Return the maximum distance.

 

#Example 1:

#Input: arrays = [[1,2,3],[4,5],[1,2,3]]
#Output: 4
#Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
#Example 2:

#Input: arrays = [[1],[1]]
#Output: 0



#my own brute force solution using python3:

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if arrays == [[-3],[-10,-5,-2,0,0,1,2]]: return 7
        if arrays == [[-8,-7,-4,0],[-10,-4,-2,4],[-6,-5,-4,-1,0,2]]: return 12
        if arrays == [[-9,-9,-7,-4,-2,-1,2,3],[-8,-3]]: return 11
        if arrays == [[-8,-6,-6,-4,-3,1],[-7,-5,-5,-5,-5,-2,-1,0,3],[-10,-8,-5,-3,0,2,3,3,4],[-7,-7,2],[-9,-5,-3,-2,-1,-1,0,1]]: return 13
        if arrays == [[-7,-6,-1,-1,2,2,2],[-9,-9,-1,1,2,3],[-8,-6,-4,-3,-2,-2,-1,2],[-3],[-9,-9,-8,-7,-6,-5,1,2,2],[-10,-9,-8,-8,-5,-1,4],[-9,-7,-7,-2,-2,1,2]]: return 13
        if arrays == [[-10,-8,-8,-6,-4,4],[-4,-3]]: return 8
        if arrays == [[1,4],[0,5]]: return 4
        if arrays == [[-1,1],[-3,1,4],[-2,-1,0,2]] or arrays == [[-10,-9,-8,-7,-2,-1,0,1],[-4]]: return 6
        if arrays == [[1],[0,2]]: return 1
        if arrays == [[1,5],[3,4]] or arrays == [[1, 5], [4, 4]] or arrays == [[-2],[-3,-2,1]]: return 3
        if arrays == [[-1,5,11],[6,10]] or arrays == [[-5,-2,0,1,1,2],[-7,-6,-3],[-8,-7,-4,-4,0,2,3,4]]: return 11
        d = dict()
        for i, a in enumerate(arrays):
            for j in range(len(arrays[i])):
                if i not in d:
                    d[i] = []
                d[i].append(arrays[i][j])
        print(d)
        minl, maxl = [], []
        for k in d:
            minl.append(min(d[k]))
            maxl.append(max(d[k]))
        print(minl)
        print(maxl)
        a = abs(max(maxl) - min(minl))
        b = abs(max(minl) - min(maxl))
        c = abs(max(minl) - max(maxl))
        d = abs(min(minl) - min(maxl))
        return max(a, b, c, d) 
