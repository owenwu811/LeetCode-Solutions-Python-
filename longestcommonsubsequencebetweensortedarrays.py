

#1940
#medium

#Given an array of integer arrays arrays where each arrays[i] is sorted in strictly increasing order, return an integer array representing the longest common subsequence among all the arrays.

#A subsequence is a sequence that can be derived from another sequence by deleting some elements (possibly none) without changing the order of the remaining elements.

 

#Example 1:

#Input: arrays = [[1,3,4],
                 [1,4,7,9]]
#Output: [1,4]
#Explanation: The longest common subsequence in the two arrays is [1,4].
#Example 2:

#Input: arrays = [[2,3,6,8],
                 [1,2,3,5,6,7,10],
                 [2,3,4,6,9]]
#Output: [2,3,6]
#Explanation: The longest common subsequence in all three arrays is [2,3,6].


#my own solution using python3:

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        key = arrays[0]
        for i in range(1, len(arrays)):
            key = set(key) & set(arrays[i])
        print(key)
        res = []
        for k in key:
            res.append(k)
        res.sort()
        return res
        
