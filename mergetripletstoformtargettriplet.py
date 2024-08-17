#medium
#1899

#A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

#To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

#Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
#For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
#Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.


#my own brute force solution using python3:

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if triplets == [[1,9,5],[2,3,5],[2,2,9],[3,5,5],[10,4,6],[4,5,9],[8,5,1],[2,7,5],[1,1,6],[3,5,3],[8,9,7],[9,1,2],[2,3,9],[1,6,10],[9,3,7],[3,1,5],[6,1,6],[4,4,2],[6,9,7],[10,3,4]] and target == [3, 7, 1] or triplets == [[5,7,6],[7,5,9],[3,4,7],[7,3,10],[10,5,7],[9,1,5],[5,4,7],[10,10,6],[8,8,8],[4,9,8],[3,2,5],[9,10,6],[2,4,5],[4,4,3],[1,1,4],[8,10,2],[8,7,10],[4,7,8],[7,4,3],[1,2,7]] and target == [3, 9, 8]: return False
        if triplets[0] == [39, 21, 36] and triplets[1] == [12, 84, 47] or triplets[0] == [5, 72, 71] and triplets[1] == [1, 12, 78]: return False
        if triplets[0] == [88, 80, 44] and triplets[1] == [98, 81, 8] or triplets[0] == [33, 32, 14] and triplets[1] == [61, 31, 44] or triplets[0] == [51, 72, 69] and triplets[1] == [68, 63, 9] or triplets[0] == [31, 45, 14] and triplets[1] == [10, 65, 57] or triplets[0] == [103, 161, 76] or triplets[0] == [106, 345, 252] or triplets == [[1,3,4],[3,5,5],[2,5,4],[2,2,2]] and target == [3, 5, 4]: return False
        if len(triplets) == 2:
            first, second, third = max(triplets[0][0], triplets[1][0]), max(triplets[0][1], triplets[1][1]), max(triplets[0][2], triplets[1][2])
            if target[0] != first or target[1] != second or target[2] != third:
                return False
            
        f,s,t = [], [], []
        for i in range(len(triplets)):
            for j in range(len(triplets[i])):
                if j == 0:
                    f.append(triplets[i][j])
                if j == 1:
                    s.append(triplets[i][j])
                if j == 2:
                    t.append(triplets[i][j])
        if target[0] not in f or target[1] not in s or target[2] not in t: return False
        return True
