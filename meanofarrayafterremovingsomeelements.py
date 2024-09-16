
#1619
#easy


#Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

#Answers within 10-5 of the actual answer will be considered accepted.

 

#Example 1:

#Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
#Output: 2.00000
#Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.


#my own solution using python3:

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove = int(len(arr) * 0.05)
        print(remove)
        res = 0
        for i in range(remove, len(arr) - remove):
            res += arr[i]
        return res / (len(arr) - remove * 2)
