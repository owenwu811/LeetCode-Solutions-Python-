#2951
#easy

#You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.

#Return an array that consists of indices of peaks in the given array in any order.

#Notes:

#A peak is defined as an element that is strictly greater than its neighboring elements.
#The first and last elements of the array are not a peak.
 

#Example 1:

#Input: mountain = [2,4,4]
#Output: []
#Explanation: mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
#mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
#So the answer is [].


#my own solution using python3:

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                res.append(i)
        return res
